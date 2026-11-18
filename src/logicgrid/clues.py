"""The clue intermediate representation.

Every clue is built from **atoms**: small frozen dataclasses that know how to

* evaluate themselves against a solution (:meth:`Atom.holds`),
* test a candidate position-assignment of their own refs (:meth:`Atom.check`),
  which is all the constraint propagator needs,
* render themselves as unambiguous English (:meth:`Atom.render`),
* explain their own exact semantics to an LLM (:meth:`Atom.gloss`), and
* round-trip through JSON.

Two design decisions matter a lot downstream:

**Symmetric arguments are normalised at construction.**  ``Adjacent(a, b)`` and
``Adjacent(b, a)`` build the *same* object, so ordinary ``==`` and ``set()``
comparison is already semantic comparison.  The narrative round-trip gate in
:mod:`logicgrid.verify` relies on this.

**Gaps are measured as absolute position difference, never as "things in
between".**  Natural language is hopelessly ambiguous here -- "two days later"
means a difference of 2, while "two days between them" means a difference of 3 --
and that off-by-one is the single most likely way for an LLM to silently change a
clue's meaning.  We therefore render gaps only as "N positions apart" and say so
loudly in the gloss.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, ClassVar, Iterable, Mapping, Sequence

from .model import PuzzleError, Ref, Schema, Solution

# Technique tiers.  See logicgrid.human_solver for the full ladder; these are
# the tiers a *clue* can demand.
TIER_DIRECT = 1
TIER_BIJECTION = 2
TIER_ORDER = 3
TIER_DISJUNCTION = 4

Assign = Mapping[Ref, int]


def _sorted_refs(refs: Iterable[Ref]) -> tuple[Ref, ...]:
    return tuple(sorted(refs))


def _name(schema: Schema, ref: Ref, start: bool = False) -> str:
    """An item, cased for its position in the sentence."""
    return schema.category_of(ref).display(ref.item, start)


#: Numbers spelled out, as printed puzzles do.
_WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
    6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
}


def _spell(n: int) -> str:
    return _WORDS.get(n, str(n))


def _poss(name: str) -> str:
    """Possessive that copes with a name already ending in -s."""
    return f"{name}'" if name.endswith(("s", "S")) else f"{name}'s"


def _entity(schema: Schema, ref: Ref, start: bool = False) -> str:
    """Name the entity this ref identifies.

    A name stands for itself; anything else becomes a descriptor, "the grower
    who is troubled by thrips". Never possessive, so it drops into any slot.
    """
    cat = schema.category_of(ref)
    if cat.subject:
        return cat.display(ref.item, start)
    text = cat.describe(ref.item, schema.entity_noun, schema.entity_who)
    return text[0].upper() + text[1:] if start else text


def _pos(schema: Schema, ref: Ref, start: bool = False) -> str:
    """Name a point on the spine: the value itself, or whoever sits there."""
    if schema.is_spine(ref):
        return _name(schema, ref, start)
    return _entity(schema, ref, start)


def _article(word: str) -> str:
    return "an" if word[:1].casefold() in "aeiou" else "a"


def _entity_first(schema: Schema, a: Ref, b: Ref) -> tuple[Ref, Ref]:
    """Order a symmetric pair so an entity leads and a spine value follows."""
    if schema.is_spine(a) and not schema.is_spine(b):
        return b, a
    return a, b


def _split_link(schema: Schema, a: Ref, b: Ref) -> tuple[Ref, Ref]:
    """Decide which ref is the sentence's subject and which is said about it.

    The names axis wins; failing that the spine makes the better predicate, so
    it goes second.
    """
    ca, cb = schema.category_of(a), schema.category_of(b)
    if cb.subject and not ca.subject:
        return b, a
    if ca.subject:
        return a, b
    if schema.is_spine(a) and not schema.is_spine(b):
        return b, a
    return a, b


def _link_sentence(schema: Schema, a: Ref, b: Ref, negative: bool) -> str:
    subject_ref, attr_ref = _split_link(schema, a, b)
    subject = _entity(schema, subject_ref, start=True)
    attr_cat = schema.category_of(attr_ref)
    # A descriptor cannot take a possessive, so tell the category which form
    # of subject it is being handed.
    is_name = schema.category_of(subject_ref).subject
    body = attr_cat.say(subject, _name(schema, attr_ref), negative, possessive=is_name)
    return _finish(body[0].upper() + body[1:])


def _compare(schema: Schema, a: Ref, b: Ref) -> str:
    """"X is earlier than Y in harvest month order." -- a before b."""
    noun, less, more, _step = _spine_words(schema)
    if schema.is_spine(a) and not schema.is_spine(b):
        # Flip it so the entity leads and the value is the yardstick.
        return (
            f"{_entity(schema, b, True)} is {more} than {_name(schema, a)} "
            f"in {noun} order."
        )
    return (
        f"{_pos(schema, a, True)} is {less} than {_pos(schema, b)} "
        f"in {noun} order."
    )


def _finish(text: str) -> str:
    """End a sentence, without doubling a stop the item already supplied."""
    return text if text.endswith((".", "!", "?")) else text + "."


def _enumerate(parts: Sequence[str]) -> str:
    """Label sub-clauses (a), (b), ... so compounds need no re-casing."""
    labels = "abcdefgh"
    return " ".join(f"({labels[i]}) {p}" for i, p in enumerate(parts))


def _set_frozen(obj: Any, **kw: Any) -> None:
    for k, v in kw.items():
        object.__setattr__(obj, k, v)


class Atom:
    """Base class for all clue atoms."""

    kind: ClassVar[str] = "atom"
    tier: ClassVar[int] = TIER_DIRECT
    #: True when the atom needs an ordered spine.
    needs_order: ClassVar[bool] = False
    #: True when the atom needs numeric spine values.
    needs_values: ClassVar[bool] = False

    # -- interface -------------------------------------------------------
    def refs(self) -> tuple[Ref, ...]:
        raise NotImplementedError

    def check(self, assign: Assign, schema: Schema) -> bool:
        """Is this atom satisfied by the given positions for :meth:`refs`?"""
        raise NotImplementedError

    def render(self, schema: Schema) -> str:
        raise NotImplementedError

    def gloss(self, schema: Schema) -> str:
        """A pedantic restatement, for an LLM that must not change the meaning."""
        return self.render(schema)

    def to_json(self) -> dict:
        raise NotImplementedError

    # -- derived ---------------------------------------------------------
    def holds(self, solution: Solution) -> bool:
        assign = {r: solution.position(r) for r in self.refs()}
        return self.check(assign, solution.schema)

    def validate(self, schema: Schema) -> None:
        for r in self.refs():
            schema.validate_ref(r)
        if self.needs_order and not schema.ordered:
            raise PuzzleError(f"{self.kind} requires an ordered spine")
        if self.needs_values and not schema.numeric:
            raise PuzzleError(f"{self.kind} requires a numeric spine")

    def subatoms(self) -> tuple["Atom", ...]:
        """Nested atoms, for compound clues."""
        return ()

    def is_positive_link(self) -> bool:
        """Does this atom hand the solver a filled-in cell outright?"""
        return False

    def __repr__(self) -> str:  # pragma: no cover - debug aid
        return f"{self.kind}({', '.join(r.key for r in self.refs())})"


# ---------------------------------------------------------------------------
# Tier 1 -- direct links
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True, eq=True)
class Link(Atom):
    """``a`` and ``b`` belong to the same entity."""

    a: Ref
    b: Ref
    kind: ClassVar[str] = "link"
    tier: ClassVar[int] = TIER_DIRECT

    def __post_init__(self) -> None:
        if self.b < self.a:
            _set_frozen(self, a=self.b, b=self.a)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a,) if self.a == self.b else (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return assign[self.a] == assign[self.b]

    def is_positive_link(self) -> bool:
        return True

    def render(self, schema: Schema) -> str:
        return _link_sentence(schema, self.a, self.b, negative=False)

    def gloss(self, schema: Schema) -> str:
        ca = schema.category_of(self.a).label
        cb = schema.category_of(self.b).label
        return (
            f"The entity whose {ca} is {self.a.item} is the SAME entity as the one "
            f"whose {cb} is {self.b.item}."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key}


@dataclass(frozen=True, slots=True, eq=True)
class NotLink(Atom):
    """``a`` and ``b`` belong to different entities."""

    a: Ref
    b: Ref
    kind: ClassVar[str] = "not_link"
    tier: ClassVar[int] = TIER_DIRECT

    def __post_init__(self) -> None:
        if self.b < self.a:
            _set_frozen(self, a=self.b, b=self.a)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a,) if self.a == self.b else (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return assign[self.a] != assign[self.b]

    def render(self, schema: Schema) -> str:
        return _link_sentence(schema, self.a, self.b, negative=True)

    def gloss(self, schema: Schema) -> str:
        ca = schema.category_of(self.a).label
        cb = schema.category_of(self.b).label
        return (
            f"The entity whose {ca} is {self.a.item} is NOT the same entity as the one "
            f"whose {cb} is {self.b.item}."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key}


# ---------------------------------------------------------------------------
# Tier 2 -- distinctness bundles
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True, eq=True)
class Distinct(Atom):
    """All of ``members`` belong to pairwise different entities."""

    members: tuple[Ref, ...]
    kind: ClassVar[str] = "distinct"
    tier: ClassVar[int] = TIER_BIJECTION

    def __post_init__(self) -> None:
        uniq = _sorted_refs(set(self.members))
        if len(uniq) < 2:
            raise PuzzleError("distinct needs at least two refs")
        _set_frozen(self, members=uniq)

    def refs(self) -> tuple[Ref, ...]:
        return self.members

    def check(self, assign: Assign, schema: Schema) -> bool:
        seen = {assign[r] for r in self.members}
        return len(seen) == len(self.members)

    def render(self, schema: Schema) -> str:
        names = [_pos(schema, r) for r in self.members]
        names[0] = _pos(schema, self.members[0], True)
        noun = schema.entity_noun_plural
        listed = ", ".join(names[:-1]) + f" and {names[-1]}"
        return f"{listed} are {_spell(len(names))} different {noun}."

    def gloss(self, schema: Schema) -> str:
        names = ", ".join(r.item for r in self.members)
        return (
            f"No two of these refer to the same entity: {names}. "
            "This asserts mutual non-identity only; it says nothing about order."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "members": [r.key for r in self.members]}


# ---------------------------------------------------------------------------
# Tier 3 -- positional clues (ordered spine)
# ---------------------------------------------------------------------------


def _spine_words(schema: Schema) -> tuple[str, str, str, str]:
    sp = schema.spine
    noun = sp.noun or "position"
    return noun, sp.cmp_less or "earlier", sp.cmp_more or "later", sp.step_noun or noun


@dataclass(frozen=True, slots=True, eq=True)
class Before(Atom):
    """``a`` is strictly earlier on the spine than ``b`` -- not necessarily adjacent."""

    a: Ref
    b: Ref
    kind: ClassVar[str] = "before"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return assign[self.a] < assign[self.b]

    def render(self, schema: Schema) -> str:
        return _compare(schema, self.a, self.b)

    def gloss(self, schema: Schema) -> str:
        noun, less, _more, _step = _spine_words(schema)
        return (
            f"{self.a.item} is STRICTLY {less} than {self.b.item} in {noun} order. "
            f"The gap may be any size -- do NOT imply they are adjacent or "
            f"immediately consecutive."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key}


@dataclass(frozen=True, slots=True, eq=True)
class ImmediatelyBefore(Atom):
    """``b`` sits exactly one spine position after ``a``."""

    a: Ref
    b: Ref
    kind: ClassVar[str] = "immediately_before"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return assign[self.b] - assign[self.a] == 1

    def render(self, schema: Schema) -> str:
        noun, less, _more, step = _spine_words(schema)
        return (
            f"{_pos(schema, self.a, True)} is exactly one {step} {less} than "
            f"{_pos(schema, self.b)}, with no {noun} in between."
        )

    def gloss(self, schema: Schema) -> str:
        noun, less, _more, step = _spine_words(schema)
        return (
            f"{self.b.item} is exactly ONE {step} after {self.a.item}; they are "
            f"consecutive {noun}s in that specific direction ({self.a.item} first). "
            f"Direction matters -- do not reverse it."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key}


@dataclass(frozen=True, slots=True, eq=True)
class Adjacent(Atom):
    """``a`` and ``b`` are one spine position apart, in either direction."""

    a: Ref
    b: Ref
    kind: ClassVar[str] = "adjacent"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True

    def __post_init__(self) -> None:
        if self.b < self.a:
            _set_frozen(self, a=self.b, b=self.a)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return abs(assign[self.a] - assign[self.b]) == 1

    def render(self, schema: Schema) -> str:
        noun, _less, _more, step = _spine_words(schema)
        x, y = _entity_first(schema, self.a, self.b)
        return (
            f"{_pos(schema, x, True)} and {_pos(schema, y)} are exactly "
            f"one {step} apart in {noun} order, in one direction or the other."
        )

    def gloss(self, schema: Schema) -> str:
        noun, _less, _more, step = _spine_words(schema)
        return (
            f"{self.a.item} and {self.b.item} are exactly one {step} apart in "
            f"{noun} order. Which one comes first is NOT specified -- keep it "
            f"symmetric and do not imply a direction."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key}


@dataclass(frozen=True, slots=True, eq=True)
class Between(Atom):
    """``a`` sits strictly between ``b`` and ``c`` on the spine."""

    a: Ref
    b: Ref
    c: Ref
    kind: ClassVar[str] = "between"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True

    def __post_init__(self) -> None:
        if self.c < self.b:
            _set_frozen(self, b=self.c, c=self.b)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b, self.c)

    def check(self, assign: Assign, schema: Schema) -> bool:
        pa, pb, pc = assign[self.a], assign[self.b], assign[self.c]
        return pb < pa < pc or pc < pa < pb

    def render(self, schema: Schema) -> str:
        noun, _less, _more, _step = _spine_words(schema)
        return (
            f"{_pos(schema, self.a, True)} falls somewhere between "
            f"{_pos(schema, self.b)} and {_pos(schema, self.c)} in {noun} order."
        )

    def gloss(self, schema: Schema) -> str:
        noun, _less, _more, _step = _spine_words(schema)
        return (
            f"In {noun} order, {self.a.item} is strictly after one of "
            f"{self.b.item}/{self.c.item} and strictly before the other. "
            f"Which of {self.b.item} and {self.c.item} is the earlier one is NOT "
            f"specified. 'Between' is exclusive: {self.a.item} is neither of them. "
            f"The gaps may be any size."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key, "c": self.c.key}


@dataclass(frozen=True, slots=True, eq=True)
class Gap(Atom):
    """Absolute spine distance between ``a`` and ``b``, compared against ``k``."""

    a: Ref
    b: Ref
    k: int
    rel: str = "eq"  # eq | ge | le
    kind: ClassVar[str] = "gap"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True
    _RELS: ClassVar[dict[str, Callable[[int, int], bool]]] = {
        "eq": lambda d, k: d == k,
        "ge": lambda d, k: d >= k,
        "le": lambda d, k: d <= k,
    }

    def __post_init__(self) -> None:
        if self.rel not in self._RELS:
            raise PuzzleError(f"gap rel must be eq/ge/le, got {self.rel!r}")
        if self.k < 1:
            raise PuzzleError(f"gap k must be >= 1, got {self.k}")
        if self.b < self.a:
            _set_frozen(self, a=self.b, b=self.a)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        d = abs(assign[self.a] - assign[self.b])
        return self._RELS[self.rel](d, self.k)

    def render(self, schema: Schema) -> str:
        noun, _less, _more, step = _spine_words(schema)
        word = {"eq": "exactly", "ge": "at least", "le": "at most"}[self.rel]
        plural = step if self.k == 1 else schema.spine.step_plural
        x, y = _entity_first(schema, self.a, self.b)
        return (
            f"{_pos(schema, x, True)} and {_pos(schema, y)} are "
            f"{word} {_spell(self.k)} {plural} apart in {noun} order."
        )

    def gloss(self, schema: Schema) -> str:
        noun, _less, _more, step = _spine_words(schema)
        word = {"eq": "exactly", "ge": "at least", "le": "at most"}[self.rel]
        return (
            f"The absolute difference between the {noun} positions of "
            f"{self.a.item} and {self.b.item} is {word} {self.k}. "
            f"CRITICAL: this is a difference of {self.k} {step}(s), i.e. "
            f"'{self.k} {step}(s) apart' or '{self.k} {step}(s) later'. It is NOT "
            f"'{self.k} {step}(s) in between' -- that would mean {self.k + 1}. "
            f"Direction is not specified."
        )

    def to_json(self) -> dict:
        return {
            "kind": self.kind,
            "a": self.a.key,
            "b": self.b.key,
            "k": self.k,
            "rel": self.rel,
        }


@dataclass(frozen=True, slots=True, eq=True)
class Parity(Atom):
    """Whether ``a`` and ``b`` sit on same-parity spine positions (1-based)."""

    a: Ref
    b: Ref
    same: bool = True
    kind: ClassVar[str] = "parity"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True

    def __post_init__(self) -> None:
        if self.b < self.a:
            _set_frozen(self, a=self.b, b=self.a)

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return ((assign[self.a] - assign[self.b]) % 2 == 0) == self.same

    def render(self, schema: Schema) -> str:
        noun, _less, _more, _step = _spine_words(schema)
        plural = schema.spine.step_plural
        a, b = _pos(schema, self.a, True), _pos(schema, self.b)
        if self.same:
            return (
                f"{a} and {b} both sit at odd-numbered {plural} or both at "
                f"even-numbered {plural}."
            )
        return (
            f"One of {_pos(schema, self.a)} and {b} sits at an odd-numbered "
            f"{noun} and the other at an even-numbered {noun}."
        )

    def gloss(self, schema: Schema) -> str:
        noun, _less, _more, _step = _spine_words(schema)
        rel = "the SAME parity" if self.same else "OPPOSITE parity"
        return (
            f"Counting {noun}s from 1, {self.a.item} and {self.b.item} have {rel}. "
            f"This constrains parity only, not distance or direction."
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "a": self.a.key, "b": self.b.key, "same": self.same}


@dataclass(frozen=True, slots=True, eq=True)
class Arith(Atom):
    """Numeric relation on spine values: ``value(a) = value(b) <op> k``."""

    a: Ref
    b: Ref
    k: float
    op: str = "add"  # add | mul
    kind: ClassVar[str] = "arith"
    tier: ClassVar[int] = TIER_ORDER
    needs_order: ClassVar[bool] = True
    needs_values: ClassVar[bool] = True

    def __post_init__(self) -> None:
        if self.op not in ("add", "mul"):
            raise PuzzleError(f"arith op must be add/mul, got {self.op!r}")

    def refs(self) -> tuple[Ref, ...]:
        return (self.a, self.b)

    def check(self, assign: Assign, schema: Schema) -> bool:
        va = schema.value_at(assign[self.a])
        vb = schema.value_at(assign[self.b])
        target = vb + self.k if self.op == "add" else vb * self.k
        return abs(va - target) < 1e-9

    def render(self, schema: Schema) -> str:
        sp = schema.spine
        noun = sp.noun or sp.label.casefold()
        a = _pos(schema, self.a, True)
        b = _pos(schema, self.b)
        if self.op == "add":
            amount = sp.format_value(self.k)
            return _finish(
                f"{a} has {_article(noun)} {noun} exactly {amount} more than {b}"
            )
        return _finish(
            f"{a} has {_article(noun)} {noun} exactly {self.k:g} times that of {b}"
        )

    def gloss(self, schema: Schema) -> str:
        sp = schema.spine
        label = sp.noun or sp.label
        if self.op == "add":
            amount = sp.format_value(self.k)
            return (
                f"{self.a.item}'s {label} MINUS {self.b.item}'s {label} equals "
                f"{amount}. {self.a.item} is the larger one. Direction matters."
            )
        return (
            f"{self.a.item}'s {label} divided by {self.b.item}'s {label} equals "
            f"{self.k:g}. {self.a.item} is the larger one. Direction matters."
        )

    def to_json(self) -> dict:
        return {
            "kind": self.kind,
            "a": self.a.key,
            "b": self.b.key,
            "k": self.k,
            "op": self.op,
        }


# ---------------------------------------------------------------------------
# Tier 4 -- compound / epistemic clues
# ---------------------------------------------------------------------------


def _union_refs(atoms: Sequence[Atom]) -> tuple[Ref, ...]:
    seen: list[Ref] = []
    for at in atoms:
        for r in at.refs():
            if r not in seen:
                seen.append(r)
    return tuple(seen)


@dataclass(frozen=True, slots=True, eq=True)
class Not(Atom):
    """Negation of any atom."""

    inner: Atom
    kind: ClassVar[str] = "not"
    tier: ClassVar[int] = TIER_DISJUNCTION

    @property
    def needs_order(self) -> bool:  # type: ignore[override]
        return self.inner.needs_order

    @property
    def needs_values(self) -> bool:  # type: ignore[override]
        return self.inner.needs_values

    def refs(self) -> tuple[Ref, ...]:
        return self.inner.refs()

    def subatoms(self) -> tuple[Atom, ...]:
        return (self.inner,)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return not self.inner.check(assign, schema)

    def render(self, schema: Schema) -> str:
        return f"The following is NOT true: {self.inner.render(schema)}"

    def gloss(self, schema: Schema) -> str:
        return f"The following is FALSE: {self.inner.gloss(schema)}"

    def to_json(self) -> dict:
        return {"kind": self.kind, "inner": self.inner.to_json()}


@dataclass(frozen=True, slots=True, eq=True)
class Or(Atom):
    """At least one of ``options`` holds (inclusive disjunction)."""

    options: tuple[Atom, ...]
    kind: ClassVar[str] = "or"
    tier: ClassVar[int] = TIER_DISJUNCTION

    def __post_init__(self) -> None:
        uniq: list[Atom] = []
        for at in self.options:
            if at not in uniq:
                uniq.append(at)
        if len(uniq) < 2:
            raise PuzzleError("or needs at least two distinct options")
        # Sort by canonical JSON so Or(x, y) == Or(y, x).
        _set_frozen(self, options=tuple(sorted(uniq, key=lambda a: repr(a.to_json()))))

    @property
    def needs_order(self) -> bool:  # type: ignore[override]
        return any(a.needs_order for a in self.options)

    @property
    def needs_values(self) -> bool:  # type: ignore[override]
        return any(a.needs_values for a in self.options)

    def refs(self) -> tuple[Ref, ...]:
        return _union_refs(self.options)

    def subatoms(self) -> tuple[Atom, ...]:
        return self.options

    def check(self, assign: Assign, schema: Schema) -> bool:
        return any(a.check(assign, schema) for a in self.options)

    def render(self, schema: Schema) -> str:
        parts = _enumerate([a.render(schema) for a in self.options])
        return (
            "At least one of the following holds, and possibly more than one: "
            f"{parts}"
        )

    def gloss(self, schema: Schema) -> str:
        parts = "\n".join(f"      - {a.gloss(schema)}" for a in self.options)
        return (
            "AT LEAST ONE of the following is true (an inclusive 'or' -- it is "
            "fine if more than one is true, and the clue does not say which):\n"
            + parts
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "options": [a.to_json() for a in self.options]}


@dataclass(frozen=True, slots=True, eq=True)
class NotBoth(Atom):
    """At most one of ``x`` and ``y`` holds."""

    x: Atom
    y: Atom
    kind: ClassVar[str] = "not_both"
    tier: ClassVar[int] = TIER_DISJUNCTION

    def __post_init__(self) -> None:
        if repr(self.y.to_json()) < repr(self.x.to_json()):
            _set_frozen(self, x=self.y, y=self.x)
        if self.x == self.y:
            raise PuzzleError("not_both needs two distinct atoms")

    @property
    def needs_order(self) -> bool:  # type: ignore[override]
        return self.x.needs_order or self.y.needs_order

    @property
    def needs_values(self) -> bool:  # type: ignore[override]
        return self.x.needs_values or self.y.needs_values

    def refs(self) -> tuple[Ref, ...]:
        return _union_refs((self.x, self.y))

    def subatoms(self) -> tuple[Atom, ...]:
        return (self.x, self.y)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return not (self.x.check(assign, schema) and self.y.check(assign, schema))

    def render(self, schema: Schema) -> str:
        parts = _enumerate([self.x.render(schema), self.y.render(schema)])
        return (
            "The following two do NOT both hold; either one alone may hold, and "
            f"so may neither: {parts}"
        )

    def gloss(self, schema: Schema) -> str:
        return (
            "AT MOST ONE of the following two statements is true. They cannot both "
            "hold, but either one alone may hold, and it is also possible that "
            "neither holds:\n"
            f"      - {self.x.gloss(schema)}\n"
            f"      - {self.y.gloss(schema)}"
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "x": self.x.to_json(), "y": self.y.to_json()}


@dataclass(frozen=True, slots=True, eq=True)
class IfThen(Atom):
    """Material implication: if ``x`` holds then ``y`` holds."""

    x: Atom
    y: Atom
    kind: ClassVar[str] = "if_then"
    tier: ClassVar[int] = TIER_DISJUNCTION

    def __post_init__(self) -> None:
        if self.x == self.y:
            raise PuzzleError("if_then needs two distinct atoms")

    @property
    def needs_order(self) -> bool:  # type: ignore[override]
        return self.x.needs_order or self.y.needs_order

    @property
    def needs_values(self) -> bool:  # type: ignore[override]
        return self.x.needs_values or self.y.needs_values

    def refs(self) -> tuple[Ref, ...]:
        return _union_refs((self.x, self.y))

    def subatoms(self) -> tuple[Atom, ...]:
        return (self.x, self.y)

    def check(self, assign: Assign, schema: Schema) -> bool:
        return (not self.x.check(assign, schema)) or self.y.check(assign, schema)

    def render(self, schema: Schema) -> str:
        parts = _enumerate([self.x.render(schema), self.y.render(schema)])
        return (
            "If (a) holds then (b) also holds, but not necessarily the reverse: "
            f"{parts}"
        )

    def gloss(self, schema: Schema) -> str:
        return (
            "An implication. IF the first statement holds THEN the second must "
            "also hold. If the first does not hold the clue says nothing at all. "
            "The converse is NOT asserted -- do not reverse it:\n"
            f"      - IF: {self.x.gloss(schema)}\n"
            f"      - THEN: {self.y.gloss(schema)}"
        )

    def to_json(self) -> dict:
        return {"kind": self.kind, "x": self.x.to_json(), "y": self.y.to_json()}


# ---------------------------------------------------------------------------
# construction helpers + JSON codec
# ---------------------------------------------------------------------------

ATOM_CLASSES: dict[str, type[Atom]] = {
    cls.kind: cls
    for cls in (
        Link,
        NotLink,
        Distinct,
        Before,
        ImmediatelyBefore,
        Adjacent,
        Between,
        Gap,
        Parity,
        Arith,
        Not,
        Or,
        NotBoth,
        IfThen,
    )
}

#: Clue kinds grouped into the difficulty tiers the generator exposes.
TIER_A_KINDS = ("link", "not_link")
TIER_B_KINDS = (
    "distinct",
    "before",
    "immediately_before",
    "adjacent",
    "between",
    "gap",
    "parity",
    "arith",
)
TIER_C_KINDS = ("not", "or", "not_both", "if_then")
ALL_KINDS = TIER_A_KINDS + TIER_B_KINDS + TIER_C_KINDS


def make_not(atom: Atom) -> Atom:
    """Negate ``atom``, collapsing the cases that have a simpler spelling."""
    if isinstance(atom, Link):
        return NotLink(atom.a, atom.b)
    if isinstance(atom, NotLink):
        return Link(atom.a, atom.b)
    if isinstance(atom, Not):
        return atom.inner
    if isinstance(atom, Parity):
        return Parity(atom.a, atom.b, not atom.same)
    if isinstance(atom, Before):
        # not (a < b)  <=>  b < a  or  a == b; positions of distinct entities
        # can coincide only when the refs are in the same category, so for the
        # general case keep the explicit negation.
        return Not(atom)
    return Not(atom)


def atom_from_json(data: Mapping) -> Atom:
    """Rebuild an atom from its JSON form, validating structure strictly."""
    if not isinstance(data, Mapping):
        raise PuzzleError(f"atom must be an object, got {type(data).__name__}")
    try:
        kind = data["kind"]
    except KeyError:
        raise PuzzleError(f"atom is missing 'kind': {data!r}") from None
    cls = ATOM_CLASSES.get(kind)
    if cls is None:
        raise PuzzleError(f"unknown clue kind {kind!r}; expected one of {sorted(ATOM_CLASSES)}")

    def ref(field: str) -> Ref:
        try:
            return Ref.parse(str(data[field]))
        except KeyError:
            raise PuzzleError(f"{kind} is missing field {field!r}") from None

    def sub(field: str) -> Atom:
        try:
            return atom_from_json(data[field])
        except KeyError:
            raise PuzzleError(f"{kind} is missing field {field!r}") from None

    if cls is Link:
        return Link(ref("a"), ref("b"))
    if cls is NotLink:
        return NotLink(ref("a"), ref("b"))
    if cls is Distinct:
        members = data.get("members")
        if not isinstance(members, Sequence) or isinstance(members, str):
            raise PuzzleError("distinct needs a 'members' list")
        return Distinct(tuple(Ref.parse(str(m)) for m in members))
    if cls is Before:
        return Before(ref("a"), ref("b"))
    if cls is ImmediatelyBefore:
        return ImmediatelyBefore(ref("a"), ref("b"))
    if cls is Adjacent:
        return Adjacent(ref("a"), ref("b"))
    if cls is Between:
        return Between(ref("a"), ref("b"), ref("c"))
    if cls is Gap:
        return Gap(ref("a"), ref("b"), int(data.get("k", 1)), str(data.get("rel", "eq")))
    if cls is Parity:
        return Parity(ref("a"), ref("b"), bool(data.get("same", True)))
    if cls is Arith:
        return Arith(ref("a"), ref("b"), float(data.get("k", 0)), str(data.get("op", "add")))
    if cls is Not:
        return Not(sub("inner"))
    if cls is Or:
        options = data.get("options")
        if not isinstance(options, Sequence) or isinstance(options, str):
            raise PuzzleError("or needs an 'options' list")
        return Or(tuple(atom_from_json(o) for o in options))
    if cls is NotBoth:
        return NotBoth(sub("x"), sub("y"))
    if cls is IfThen:
        return IfThen(sub("x"), sub("y"))
    raise PuzzleError(f"unhandled clue kind {kind!r}")  # pragma: no cover


def atoms_from_json(items: Iterable[Mapping]) -> tuple[Atom, ...]:
    return tuple(atom_from_json(d) for d in items)


def is_trivial(atom: Atom, schema: Schema) -> bool:
    """Is ``atom`` true for *every* solution, and therefore worthless as a clue?

    Catches the degenerate forms the generator could otherwise emit, e.g. a
    ``NotLink`` between two items of the same category (automatic), or a
    positional claim between two spine items (already fixed by the spine).
    """
    refs = atom.refs()
    if len(refs) < 2:
        return True
    cats = {r.cat for r in refs}
    if len(cats) == 1:
        # Everything about a single category is already pinned by its bijection.
        return True
    if all(schema.is_spine(r) for r in refs):
        return True
    if isinstance(atom, Distinct):
        # Two members of the same category are automatically different
        # entities, so such a clue is partly self-evident -- and it reads
        # terribly ("the bottom shelf and the third shelf are 2 different
        # modellers"). Require one member per category.
        cats_seen = [r.cat for r in atom.members]
        if len(cats_seen) != len(set(cats_seen)):
            return True
    return False
