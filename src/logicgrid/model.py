"""Core data model for Penny Dell-style logic grid puzzles.

A puzzle is a set of ``N`` categories, each holding exactly ``M`` items.  The
solution pairs the items up into ``M`` entities, each holding one item from every
category.

One category is the **spine**.  It supplies the puzzle's index: entity ``p`` is
the entity holding ``spine.items[p]``.  Fixing the spine this way removes the
``M!`` relabelling symmetry that a bare "entity id" model suffers from, and it
makes every positional clue trivial to evaluate -- the position of an entity
*is* its index.

If the spine is ``ordered`` then positional clues (before / adjacent / between)
are available.  If it additionally carries ``values`` then arithmetic clues
("paid three dollars more than") are available too.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Mapping, Sequence


class PuzzleError(ValueError):
    """Raised when a puzzle definition is internally inconsistent."""


@dataclass(frozen=True, slots=True)
class Category:
    """One axis of the grid.

    Attributes
    ----------
    name:
        Machine key, e.g. ``"day"``.  Must be unique within a puzzle and must
        not contain ``":"``.
    label:
        Human heading, e.g. ``"Wedding day"``.
    items:
        The category's members.  When ``ordered`` is true the sequence order is
        the canonical order used by positional clues.
    ordered:
        Whether the items have a meaningful order.
    values:
        Optional numeric value per item, aligned with ``items``.  Enables
        arithmetic clues.  Only meaningful on an ordered category.
    unit / unit_suffix:
        Rendering affixes for numeric values, e.g. ``unit="$"`` gives ``$12``,
        ``unit_suffix=" miles"`` gives ``12 miles``.
    noun:
        Singular noun for prose, e.g. ``"day"``.
    """

    name: str
    label: str
    items: tuple[str, ...]
    ordered: bool = False
    values: tuple[float, ...] | None = None
    unit: str = ""
    unit_suffix: str = ""
    noun: str = ""
    #: Comparative words used when this category is the spine, e.g.
    #: ("earlier", "later") for days, ("cheaper", "dearer") for prices.
    cmp_less: str = ""
    cmp_more: str = ""
    #: Unit of distance along the spine, e.g. "day" so that a gap reads
    #: "three days apart".
    step_noun: str = ""
    #: How an entity relates to one of this category's items, in the third
    #: person: ``"harvests in"`` gives "Leocadia harvests in April" and, via
    #: :func:`negate_verb`, "Leocadia does not harvest in April". Left empty,
    #: clues fall back to a possessive ("Leocadia's pest is thrips"), which is
    #: always grammatical but flatter.
    verb: str = ""
    #: True for the one category whose items are the puzzle's actors -- the
    #: names. Clues use it as the grammatical subject wherever they can.
    subject: bool = False
    #: Set for items whose spelling must never be touched. Rendering only ever
    #: capitalises an item's first letter at the start of a sentence, which is
    #: already correct for both proper nouns ("Odette" -> "Odette") and common
    #: phrases ("a lattice top" -> "A lattice top"); this flag exists for the
    #: rare item that has to stay lowercase, such as a stylised name.
    proper: bool = False

    def __post_init__(self) -> None:
        if ":" in self.name:
            raise PuzzleError(f"category name may not contain ':': {self.name!r}")
        if len(self.items) != len(set(self.items)):
            raise PuzzleError(f"duplicate items in category {self.name!r}: {self.items!r}")
        if not self.items:
            raise PuzzleError(f"category {self.name!r} has no items")
        for it in self.items:
            if ":" in it:
                raise PuzzleError(f"item may not contain ':': {it!r}")
        if self.values is not None:
            if len(self.values) != len(self.items):
                raise PuzzleError(
                    f"category {self.name!r}: {len(self.values)} values for "
                    f"{len(self.items)} items"
                )
            if not self.ordered:
                raise PuzzleError(f"category {self.name!r} has values but is not ordered")

    @property
    def size(self) -> int:
        return len(self.items)

    def index(self, item: str) -> int:
        try:
            return self.items.index(item)
        except ValueError:
            raise PuzzleError(f"{item!r} is not an item of category {self.name!r}") from None

    def value(self, item: str) -> float:
        if self.values is None:
            raise PuzzleError(f"category {self.name!r} has no numeric values")
        return self.values[self.index(item)]

    @property
    def step_plural(self) -> str:
        """Plural of :attr:`step_noun`, for "three days apart"."""
        word = self.step_noun or self.noun or "position"
        head, _, tail = word.rpartition(" ")
        if tail.endswith("fe"):
            tail = tail[:-2] + "ves"
        elif tail.endswith("f"):
            tail = tail[:-1] + "ves"
        elif tail.endswith(("s", "x", "z", "ch", "sh")):
            tail = tail + "es"
        elif tail.endswith("y") and tail[-2:-1] not in "aeiou":
            tail = tail[:-1] + "ies"
        else:
            tail = tail + "s"
        return f"{head} {tail}".strip()

    def display(self, item: str, start: bool = False) -> str:
        """Render an item for prose.

        At the start of a sentence a common phrase is capitalised ("a lattice
        top" -> "A lattice top"); a proper noun is left exactly as written, so
        "Odette" never becomes "odette" and "the timetable" never stays
        lowercase mid-paragraph.
        """
        if not start or self.proper or not item:
            return item
        return item[0].upper() + item[1:]

    def say(
        self,
        subject: str,
        item: str,
        negative: bool = False,
        possessive: bool = True,
    ) -> str:
        """"<subject> harvests in April" / "... does not harvest in April".

        With no verb declared the fallback is a possessive, which reads well
        for a name ("Odette's pie is rhubarb") but collapses for a descriptor:
        "the entry whose baker is Odette's pie is rhubarb" is unparseable.
        ``possessive=False`` picks a form that survives a phrase subject.
        """
        if not self.verb:
            noun = self.noun or self.label.casefold()
            if possessive:
                tail = "is not" if negative else "is"
                return f"{subject}'s {noun} {tail} {item}"
            tail = "is not matched with" if negative else "is matched with"
            return f"{subject} {tail} the {noun} {item}"
        verb = negate_verb(self.verb) if negative else self.verb
        return f"{subject} {verb} {item}"

    def describe(self, item: str, entity_noun: str, who: str = "who") -> str:
        """Name an entity by one of its attributes: "the grower who ...".

        Needed when a clue relates two attributes with no person in sight, and
        deliberately possessive-free so it can be dropped into any sentence
        slot without producing "the grower whose pest is thrips's month".
        ``who`` is "that" for an inanimate entity -- "the clock that sounds
        Westminster".
        """
        if not self.verb:
            noun = self.noun or self.label.casefold()
            return f"the {entity_noun} whose {noun} is {item}"
        return f"the {entity_noun} {who} {self.verb} {item}"

    def format_value(self, v: float) -> str:
        """Render a numeric value, trimming a pointless trailing ``.0``."""
        body = f"{v:g}"
        return f"{self.unit}{body}{self.unit_suffix}"

    def refs(self) -> tuple["Ref", ...]:
        return tuple(Ref(self.name, it) for it in self.items)


@dataclass(frozen=True, slots=True, order=True)
class Ref:
    """A reference to one item of one category: the atom of every clue."""

    cat: str
    item: str

    @property
    def key(self) -> str:
        return f"{self.cat}:{self.item}"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.key

    @classmethod
    def parse(cls, text: str) -> "Ref":
        cat, sep, item = text.partition(":")
        if not sep:
            raise PuzzleError(f"malformed ref {text!r}, expected 'category:item'")
        return cls(cat.strip(), item.strip())


#: Verbs that negate by taking "not" directly, with no do-support.
#: "has" is deliberately absent: in a clue it is a main verb ("has a price of"),
#: which needs "does not have", not "has not".
#: Heads that take a bare "not" rather than do-support.
_AUX = frozenset({"is", "was", "are", "were"})

#: Heads that take a bare "not" only when they are auxiliary to something else.
#: "has grown" negates to "has not grown", but bare "has" wants do-support --
#: "does not have a trowel", since "has not a trowel" is a century out of date.
_PERFECT = frozenset({"has", "had", "have"})

#: Third-person forms the -s rules get wrong.
_IRREGULAR_STEMS = {"has": "have", "does": "do", "goes": "go", "is": "be"}


def third_person_stem(verb: str) -> str:
    """Strip third-person -s so do-support can be applied.

    "harvests" -> "harvest", "flies" -> "fly", "watches" -> "watch". Only used
    on the verbs the theme packs declare, and
    ``tests/test_phrasing.py`` asserts every one of them survives the round
    trip, so an irregular slipping in is caught rather than shipped.
    """
    if verb.casefold() in _IRREGULAR_STEMS:
        return _IRREGULAR_STEMS[verb.casefold()]
    if verb.endswith("ies") and len(verb) > 4:
        return verb[:-3] + "y"
    for suffix in ("sses", "shes", "ches", "xes", "zes", "oes"):
        if verb.endswith(suffix):
            return verb[:-2]
    if verb.endswith("s") and not verb.endswith("ss"):
        return verb[:-1]
    return verb


def negate_verb(phrase: str) -> str:
    """Negate a third-person verb phrase.

    "is troubled by" -> "is not troubled by"; "harvests in" -> "does not
    harvest in"; "has grown" -> "has not grown".
    """
    head, _, tail = phrase.partition(" ")
    if head.casefold() in _AUX or (head.casefold() in _PERFECT and tail):
        return f"{head} not {tail}".strip()
    stem = third_person_stem(head)
    return f"does not {stem} {tail}".strip()


#: Leading words prose adds or drops freely; stripped for lenient lookup only.
_ARTICLES = ("the ", "a ", "an ")


def _loose_key(item: str) -> str:
    """Casefold, collapse whitespace and drop a leading article."""
    key = " ".join(item.split()).casefold()
    for article in _ARTICLES:
        if key.startswith(article):
            return key[len(article) :]
    return key


class Schema:
    """The categories of a puzzle plus the spine designation.

    Carries the lookups that clue evaluation and propagation need, so that
    neither has to re-derive them.
    """

    def __init__(
        self,
        categories: Sequence[Category],
        spine: str,
        entity_noun: str = "entry",
        entity_noun_plural: str = "",
        entity_animate: bool = True,
    ) -> None:
        if len(categories) < 2:
            raise PuzzleError("a puzzle needs at least two categories")
        names = [c.name for c in categories]
        if len(names) != len(set(names)):
            raise PuzzleError(f"duplicate category names: {names}")
        sizes = {c.size for c in categories}
        if len(sizes) != 1:
            raise PuzzleError(f"all categories must be the same size, got {sizes}")
        by_name = {c.name: c for c in categories}
        if spine not in by_name:
            raise PuzzleError(f"spine {spine!r} is not one of {names}")

        # Item names must be unique across the whole puzzle, not merely within
        # a category.  This is what lets a clue -- and a narrative paragraph --
        # name an item without also naming its category, which removes a large
        # class of LLM extraction ambiguity in phase 2.
        everything = [it for c in categories for it in c.items]
        if len(everything) != len(set(everything)):
            dupes = sorted({x for x in everything if everything.count(x) > 1})
            raise PuzzleError(f"item names must be globally unique; repeated: {dupes}")

        self.categories: tuple[Category, ...] = tuple(categories)
        self.by_name: Mapping[str, Category] = by_name
        self.spine_name = spine
        self.spine: Category = by_name[spine]
        self.size: int = self.spine.size
        self.positions: tuple[int, ...] = tuple(range(self.size))
        self.entity_noun = entity_noun
        self.entity_noun_plural = entity_noun_plural or f"{entity_noun}s"
        self.entity_animate = entity_animate
        #: Relative pronoun for a descriptor: people get "who", things "that".
        self.entity_who = "who" if entity_animate else "that"
        # Every (category, item) pair in the puzzle.
        self.all_refs: tuple[Ref, ...] = tuple(
            r for c in self.categories for r in c.refs()
        )
        self._ref_set = frozenset(self.all_refs)
        self._by_item: Mapping[str, Ref] = {r.item: r for r in self.all_refs}
        # A lenient index for reading LLM output back. Prose cannot be relied on
        # to echo a leading article: "the Last Resort finished second" is how the
        # sentence has to start, and every reader strips the "the" when naming
        # the item. That is normalisation, not renaming, so resolve it -- but
        # only where the stripped form stays unambiguous, and never for anything
        # beyond articles, so a genuine misname ("Annie" for "Anne") still fails.
        loose: dict[str, Ref | None] = {}
        for ref in self.all_refs:
            key = _loose_key(ref.item)
            loose[key] = None if key in loose else ref
        self._loose: Mapping[str, Ref] = {k: v for k, v in loose.items() if v}

    # -- queries ---------------------------------------------------------
    @property
    def ordered(self) -> bool:
        return self.spine.ordered

    @property
    def numeric(self) -> bool:
        return self.spine.values is not None

    def validate_ref(self, ref: Ref) -> None:
        if ref not in self._ref_set:
            raise PuzzleError(f"unknown ref {ref.key!r}")

    def category_of(self, ref: Ref) -> Category:
        try:
            return self.by_name[ref.cat]
        except KeyError:
            raise PuzzleError(f"unknown category {ref.cat!r}") from None

    def is_spine(self, ref: Ref) -> bool:
        return ref.cat == self.spine_name

    def spine_position(self, ref: Ref) -> int:
        """Position forced by a spine ref (spine items are positionally fixed)."""
        if not self.is_spine(ref):
            raise PuzzleError(f"{ref.key!r} is not a spine ref")
        return self.spine.index(ref.item)

    def value_at(self, position: int) -> float:
        if self.spine.values is None:
            raise PuzzleError("spine has no numeric values")
        return self.spine.values[position]

    def other_categories(self) -> tuple[Category, ...]:
        return tuple(c for c in self.categories if c.name != self.spine_name)

    def resolve(self, item: str) -> Ref:
        """Find the ref for a bare item name (names are globally unique)."""
        try:
            return self._by_item[item]
        except KeyError:
            raise PuzzleError(f"no item named {item!r} in this puzzle") from None

    def try_resolve(self, item: str) -> Ref | None:
        """Lenient lookup for parsing LLM output. ``None`` if it is not our item.

        Tolerates case, surrounding whitespace and a missing or added leading
        article -- all of which are artefacts of how prose has to be written,
        not changes of meaning. Everything else fails, so a renamed cast member
        is still caught.
        """
        if item in self._by_item:
            return self._by_item[item]
        return self._loose.get(_loose_key(item))

    def try_match(self, item: str) -> Ref | None:
        """Like :meth:`try_resolve`, but also accepts an unambiguous abbreviation.

        Deliberately *not* used for the facts in a clue. There, a wrong name
        changes the puzzle, so only case, spacing and a leading article are
        forgiven. This looser form is for comparing a reader's *listing* of the
        cast, where "gelatine cube" for "a gelatine cube of unclear provenance"
        is abbreviation rather than renaming -- and where an item the narrative
        genuinely dropped still fails, because nothing would mention it at all.
        """
        exact = self.try_resolve(item)
        if exact is not None:
            return exact
        needle = _loose_key(item)
        if len(needle) < 3:
            return None
        hits = [
            ref for name, ref in self._loose.items() if needle in name
        ]
        return hits[0] if len(hits) == 1 else None

    def to_json(self) -> dict:
        return {
            "spine": self.spine_name,
            "entity_noun": self.entity_noun,
            "entity_noun_plural": self.entity_noun_plural,
            "entity_animate": self.entity_animate,
            "categories": [
                {
                    "name": c.name,
                    "label": c.label,
                    "items": list(c.items),
                    "ordered": c.ordered,
                    **({"values": list(c.values)} if c.values is not None else {}),
                    **({"unit": c.unit} if c.unit else {}),
                    **({"unit_suffix": c.unit_suffix} if c.unit_suffix else {}),
                    **({"noun": c.noun} if c.noun else {}),
                    **({"cmp_less": c.cmp_less} if c.cmp_less else {}),
                    **({"cmp_more": c.cmp_more} if c.cmp_more else {}),
                    **({"step_noun": c.step_noun} if c.step_noun else {}),
                    **({"proper": c.proper} if c.proper else {}),
                    **({"verb": c.verb} if c.verb else {}),
                    **({"subject": c.subject} if c.subject else {}),
                }
                for c in self.categories
            ],
        }

    @classmethod
    def from_json(cls, data: Mapping) -> "Schema":
        cats = [
            Category(
                name=c["name"],
                label=c["label"],
                items=tuple(c["items"]),
                ordered=bool(c.get("ordered", False)),
                values=tuple(c["values"]) if c.get("values") is not None else None,
                unit=c.get("unit", ""),
                unit_suffix=c.get("unit_suffix", ""),
                noun=c.get("noun", ""),
                cmp_less=c.get("cmp_less", ""),
                cmp_more=c.get("cmp_more", ""),
                step_noun=c.get("step_noun", ""),
                proper=bool(c.get("proper", False)),
                verb=c.get("verb", ""),
                subject=bool(c.get("subject", False)),
            )
            for c in data["categories"]
        ]
        return cls(
            cats,
            data["spine"],
            entity_noun=data.get("entity_noun", "entry"),
            entity_noun_plural=data.get("entity_noun_plural", ""),
            entity_animate=bool(data.get("entity_animate", True)),
        )


class Solution:
    """A complete assignment: ``table[category][position] -> item``."""

    __slots__ = ("schema", "table", "_pos")

    def __init__(self, schema: Schema, table: Mapping[str, Sequence[str]]) -> None:
        self.schema = schema
        norm: dict[str, tuple[str, ...]] = {}
        for cat in schema.categories:
            try:
                row = tuple(table[cat.name])
            except KeyError:
                raise PuzzleError(f"solution is missing category {cat.name!r}") from None
            if sorted(row) != sorted(cat.items):
                raise PuzzleError(
                    f"solution row for {cat.name!r} is not a permutation of its items"
                )
            norm[cat.name] = row
        if norm[schema.spine_name] != schema.spine.items:
            raise PuzzleError(
                "the spine row must be in canonical item order "
                f"({schema.spine.items!r}), got {norm[schema.spine_name]!r}"
            )
        self.table: Mapping[str, tuple[str, ...]] = norm
        self._pos: dict[Ref, int] = {
            Ref(cat, item): p
            for cat, row in norm.items()
            for p, item in enumerate(row)
        }

    def position(self, ref: Ref) -> int:
        """The position (entity index) that ``ref`` belongs to."""
        try:
            return self._pos[ref]
        except KeyError:
            raise PuzzleError(f"unknown ref {ref.key!r}") from None

    def value(self, ref: Ref) -> float:
        return self.schema.value_at(self.position(ref))

    def entity(self, position: int) -> dict[str, str]:
        return {cat: row[position] for cat, row in self.table.items()}

    def entities(self) -> Iterator[dict[str, str]]:
        for p in self.schema.positions:
            yield self.entity(p)

    def same_entity(self, a: Ref, b: Ref) -> bool:
        return self.position(a) == self.position(b)

    def to_json(self) -> dict[str, list[str]]:
        return {k: list(v) for k, v in self.table.items()}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Solution):
            return NotImplemented
        return self.table == other.table

    def __hash__(self) -> int:
        return hash(tuple(sorted((k, v) for k, v in self.table.items())))

    def __repr__(self) -> str:  # pragma: no cover - debug aid
        rows = ", ".join(f"{k}={v}" for k, v in self.table.items())
        return f"Solution({rows})"


@dataclass(slots=True)
class Clue:
    """One *numbered* clue, which may bundle several atoms.

    Penny Dell clues routinely carry more than one fact -- "Anne was married on
    Monday, but not to Wally" is two constraints under one number.  Bundling is
    presentational only: the logical content of a puzzle is the flat union of
    every clue's atoms.
    """

    atoms: tuple = ()
    style: str = "sentences"  # sentences | but_not | and | parenthetical

    def __iter__(self):
        return iter(self.atoms)

    def __len__(self) -> int:
        return len(self.atoms)
