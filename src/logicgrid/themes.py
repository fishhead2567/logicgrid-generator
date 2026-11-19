"""Theme packs: the raw material puzzles are dressed in.

A theme supplies a **spine** (the ordered axis everything else is pinned to) and
four **axes** of flavour.  Each axis offers more items than any puzzle needs, so
the generator can sample a different cast from the same theme on a different
seed.

Two invariants are enforced by :func:`Theme.build`:

* every item name in a built puzzle is globally unique, so a clue can say
  "Marigold" without also saying which category that is -- which removes a
  large class of LLM ambiguity in the narrative round-trip;
* the spine is ordered, so positional clues are always available.

Spines are shared between themes.  A numeric spine (prices, distances) unlocks
arithmetic clues but suppresses gap/parity clues, because "two price-slots
apart" is a horrible thing to say in prose and an easy thing to mistranslate.
"""

from __future__ import annotations

from dataclasses import dataclass, field, replace
from random import Random
from typing import Sequence

from .model import Category, PuzzleError, Schema

# ---------------------------------------------------------------------------
# spines
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class SpineSpec:
    """An ordered axis. Puzzles take a prefix of ``items`` (and ``values``)."""

    name: str
    label: str
    noun: str
    items: tuple[str, ...]
    cmp_less: str = "earlier"
    cmp_more: str = "later"
    step_noun: str = ""
    values: tuple[float, ...] | None = None
    unit: str = ""
    unit_suffix: str = ""
    allow_gap: bool = True
    allow_parity: bool = True

    def build(self, size: int) -> Category:
        if size > len(self.items):
            raise PuzzleError(
                f"spine {self.name!r} has {len(self.items)} items, need {size}"
            )
        return Category(
            name=self.name,
            label=self.label,
            items=self.items[:size],
            ordered=True,
            values=self.values[:size] if self.values is not None else None,
            unit=self.unit,
            unit_suffix=self.unit_suffix,
            noun=self.noun,
            cmp_less=self.cmp_less,
            cmp_more=self.cmp_more,
            step_noun=self.step_noun or self.noun,
        )


WEEKDAYS = SpineSpec(
    name="day",
    label="Day",
    noun="day",
    items=("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"),
    cmp_less="earlier",
    cmp_more="later",
    step_noun="day",
)

MONTHS = SpineSpec(
    name="month",
    label="Month",
    noun="month",
    items=("January", "February", "March", "April", "May", "June"),
    cmp_less="earlier",
    cmp_more="later",
    step_noun="month",
)

PLACINGS = SpineSpec(
    name="place",
    label="Placing",
    noun="placing",
    items=("first", "second", "third", "fourth", "fifth", "sixth"),
    cmp_less="better",
    cmp_more="worse",
    step_noun="place",
)

SLOTS = SpineSpec(
    name="slot",
    label="Running order",
    noun="slot",
    items=(
        "slot one",
        "slot two",
        "slot three",
        "slot four",
        "slot five",
        "slot six",
    ),
    cmp_less="earlier",
    cmp_more="later",
    step_noun="slot",
)

MORNINGS = SpineSpec(
    name="time",
    label="Start time",
    noun="start time",
    items=("8am", "9am", "10am", "11am", "noon", "1pm"),
    cmp_less="earlier",
    cmp_more="later",
    step_noun="hour",
)

SHELVES = SpineSpec(
    name="shelf",
    label="Shelf",
    noun="shelf",
    items=(
        "the bottom shelf",
        "the second shelf",
        "the third shelf",
        "the fourth shelf",
        "the fifth shelf",
        "the top shelf",
    ),
    cmp_less="lower",
    cmp_more="higher",
    step_noun="shelf",
)

PRICES = SpineSpec(
    name="price",
    label="Price",
    noun="price",
    items=("$3", "$5", "$7", "$9", "$11", "$13"),
    cmp_less="cheaper",
    cmp_more="dearer",
    step_noun="price step",
    values=(3, 5, 7, 9, 11, 13),
    unit="$",
    allow_gap=False,
    allow_parity=False,
)

DISTANCES = SpineSpec(
    name="distance",
    label="Distance",
    noun="distance",
    items=("200 miles", "300 miles", "400 miles", "500 miles", "600 miles", "700 miles"),
    cmp_less="shorter",
    cmp_more="longer",
    step_noun="hundred miles",
    values=(200, 300, 400, 500, 600, 700),
    unit_suffix=" miles",
    allow_gap=False,
    allow_parity=False,
)

ENTRY_FEES = SpineSpec(
    name="fee",
    label="Entry fee",
    noun="entry fee",
    items=("$2", "$4", "$6", "$8", "$10", "$12"),
    cmp_less="cheaper",
    cmp_more="dearer",
    step_noun="fee step",
    values=(2, 4, 6, 8, 10, 12),
    unit="$",
    allow_gap=False,
    allow_parity=False,
)

ROUNDS = SpineSpec(
    name="round",
    label="Round",
    noun="round",
    items=(
        "round one",
        "round two",
        "round three",
        "round four",
        "round five",
        "round six",
    ),
    cmp_less="earlier",
    cmp_more="later",
    step_noun="round",
)

POINTS = SpineSpec(
    name="points",
    label="Score",
    noun="score",
    items=("61 points", "64 points", "67 points", "70 points", "73 points", "76 points"),
    cmp_less="lower",
    cmp_more="higher",
    step_noun="point",
    values=(61, 64, 67, 70, 73, 76),
    unit_suffix=" points",
    allow_gap=False,
    allow_parity=False,
)

THROWS = SpineSpec(
    name="throw",
    label="Best throw",
    noun="best throw",
    items=("28 feet", "32 feet", "36 feet", "40 feet", "44 feet", "48 feet"),
    cmp_less="shorter",
    cmp_more="longer",
    step_noun="foot",
    values=(28, 32, 36, 40, 44, 48),
    unit_suffix=" feet",
    allow_gap=False,
    allow_parity=False,
)

SPINES = {
    s.name: s
    for s in (
        WEEKDAYS, MONTHS, PLACINGS, SLOTS, MORNINGS, SHELVES,
        PRICES, DISTANCES, ENTRY_FEES, ROUNDS, POINTS, THROWS,
    )
}


# ---------------------------------------------------------------------------
# themes
# ---------------------------------------------------------------------------


@dataclass(frozen=True, slots=True)
class Axis:
    """One non-spine category, with a pool to sample items from.

    ``verb`` is how an entity relates to one of these items, third person:
    "is troubled by" gives "Leocadia is troubled by thrips" and, negated,
    "Leocadia is not troubled by thrips". ``subject`` marks the one axis whose
    items are the puzzle's actors, which clues prefer as their subject.
    """

    name: str
    label: str
    noun: str
    pool: tuple[str, ...]
    verb: str = ""
    subject: bool = False

    def build(self, items: Sequence[str]) -> Category:
        return Category(
            name=self.name,
            label=self.label,
            items=tuple(items),
            noun=self.noun,
            verb=self.verb,
            subject=self.subject,
        )


@dataclass(frozen=True, slots=True)
class Theme:
    """A complete setting: a title, a cast, a spine and some flavour axes."""

    slug: str
    title: str
    entity_noun: str
    #: One or two sentences of setting, handed to the narrator as raw material.
    blurb: str
    spine: SpineSpec
    axes: tuple[Axis, ...]
    entity_noun_plural: str = ""
    #: False when the entity is a thing, so descriptors read "the clock that
    #: sounds Westminster" rather than "the clock who".
    entity_animate: bool = True
    #: Verb for the shared spine in *this* theme's words: the same MONTHS spine
    #: reads "harvests in April" here and "is due in April" elsewhere.
    spine_verb: str = ""
    #: Likewise for its noun -- "harvest month" rather than bare "month".
    spine_noun: str = ""

    def max_categories(self) -> int:
        return 1 + len(self.axes)

    def max_items(self) -> int:
        return min([len(self.spine.items)] + [len(a.pool) for a in self.axes])

    def build(self, categories: int, items: int, rng: Random) -> Schema:
        """Sample a concrete schema of the requested shape."""
        if categories < 2 or categories > self.max_categories():
            raise PuzzleError(
                f"theme {self.slug!r} supports 2..{self.max_categories()} categories, "
                f"got {categories}"
            )
        if items > self.max_items():
            raise PuzzleError(
                f"theme {self.slug!r} supports up to {self.max_items()} items, got {items}"
            )
        spine = self.spine.build(items)
        if self.spine_verb:
            spine = replace(spine, verb=self.spine_verb)
        if self.spine_noun:
            # Not step_noun: the unit of distance stays "month", so a gap reads
            # "one month apart in harvest month order" rather than repeating it.
            spine = replace(
                spine,
                noun=self.spine_noun,
                label=self.spine_noun[:1].upper() + self.spine_noun[1:],
            )
        # The subject axis holds the names, and a puzzle without them reads
        # entirely in descriptors ("the pigeon that descends from a Janssen
        # flies 200 miles"). It is always in, and the rest are sampled.
        actors = [a for a in self.axes if a.subject]
        rest = [a for a in self.axes if not a.subject]
        wanted = categories - 1
        if actors and wanted >= 1:
            chosen = actors[:1] + rng.sample(rest, wanted - 1)
        else:
            chosen = rng.sample(list(self.axes), wanted)
        # Keep a stable presentation order (the pack's own order).
        order = {a.name: i for i, a in enumerate(self.axes)}
        chosen.sort(key=lambda a: order[a.name])
        cats = [spine]
        for axis in chosen:
            picked = rng.sample(list(axis.pool), items)
            cats.append(axis.build(picked))
        return Schema(
            cats,
            spine.name,
            entity_noun=self.entity_noun,
            entity_noun_plural=self.entity_noun_plural,
            entity_animate=self.entity_animate,
        )


def _axis(name: str, label: str, noun: str, verb: str, *pool: str) -> Axis:
    return Axis(name=name, label=label, noun=noun, pool=pool, verb=verb)


def _actor(name: str, label: str, noun: str, *pool: str) -> Axis:
    """The axis whose items are the puzzle's actors -- the names."""
    return Axis(name=name, label=label, noun=noun, pool=pool, subject=True)


THEMES: tuple[Theme, ...] = (
    Theme(
        slug="county_fair",
        title="The Hollow Creek Pie Judging",
        entity_noun="baker",
        entity_noun_plural="bakers",
        blurb=(
            "The Hollow Creek county fair runs its pie judging with more ceremony "
            "than the state legislature."
        ),
        spine=PLACINGS,
        spine_verb="places",
        axes=(
            _actor("baker", "Baker", "baker", "Odette", "Bramwell", "Loretta",
                  "Caspian", "Marigold", "Thaddeus", "Winnie"),
            _axis("filling", "Filling", "filling", "bakes", "rhubarb", "sour cherry",
                  "pecan", "buttermilk", "green tomato", "blackberry", "mincemeat"),
            _axis("county", "Home county", "county", "comes from", "Fenwick", "Ardmore",
                  "Little Pell", "Hobbs Bend", "Quarry Hill", "Sweetwater", "Dunmore"),
            _axis("crust", "Crust", "crust", "uses", "a lattice top", "a braided edge",
                  "a crumb topping", "a fluted rim", "a cut-out star top",
                  "a double crust", "a fork-crimped edge"),
        ),
    ),
    Theme(
        slug="lighthouse",
        title="The Saltmarsh Light Rotation",
        entity_noun="keeper",
        entity_noun_plural="keepers",
        blurb=(
            "The lighthouses along the Saltmarsh coast share a single relief keeper "
            "roster, and the logbooks have become a scholarly mess."
        ),
        spine=WEEKDAYS,
        spine_verb="works on",
        axes=(
            _actor("keeper", "Keeper", "keeper", "Hollis", "Perpetua", "Emmerich",
                  "Saoirse", "Barnaby", "Clementine", "Lucian"),
            _axis("light", "Lighthouse", "lighthouse", "is stationed at", "Gannet Rock", "Cold Harbour",
                  "Mawes Point", "Siren Shoal", "Blackwater Bar", "Thimble Reef",
                  "Pelter Head"),
            _axis("chore", "Logged chore", "chore", "logs", "regrinding the lens",
                  "repainting the gallery", "splicing the hoist rope",
                  "overhauling the foghorn", "rebedding the storm glass",
                  "whitewashing the base", "rewiring the beacon"),
            _axis("weather", "Weather noted", "weather", "notes", "sleet", "sea fog",
                  "a flat calm", "a gale", "hail", "thunder", "drizzle"),
        ),
    ),
    Theme(
        slug="bookshop",
        title="Mrs Pell's Impossible Shelves",
        entity_noun="volume",
        entity_noun_plural="volumes",
        entity_animate=False,
        blurb=(
            "Mrs Pell's secondhand bookshop shelves by a system she alone "
            "understands, and she has gone to Margate for a fortnight."
        ),
        spine=SHELVES,
        spine_verb="sits on",
        axes=(
            _actor("book", "Volume", "volume", "a water-stained atlas",
                  "a beekeeping manual", "a book of sea shanties",
                  "a Latin primer", "a guide to fungi", "a treatise on clocks",
                  "an album of pressed ferns"),
            _axis("buyer", "Buyer", "buyer", "was bought by", "Ottoline", "Rodrigo", "Fenella",
                  "Augustus", "Verity", "Ignatius", "Sybilla"),
            _axis("bookmark", "Found inside", "keepsake", "contains", "a tram ticket",
                  "a pressed violet", "a laundry list", "a lock of hair",
                  "a pawn ticket", "a recipe for quince jelly", "a postcard from Hull"),
            _axis("price_tag", "Pencilled price", "price", "is priced at", "ninepence",
                  "one and six", "two shillings", "half a crown", "four shillings",
                  "seven and six", "a guinea"),
        ),
    ),
    Theme(
        slug="balloon",
        title="The Thistledown Balloon Ascent",
        entity_noun="pilot",
        entity_noun_plural="pilots",
        blurb=(
            "The Thistledown Ascent is less a race than a slow argument conducted "
            "at two thousand feet."
        ),
        spine=MORNINGS,
        spine_verb="launches at",
        axes=(
            _actor("pilot", "Pilot", "pilot", "Isolde", "Grover", "Anneliese",
                  "Montague", "Delphine", "Horatio", "Rosalind"),
            _axis("envelope", "Envelope", "envelope", "flies", "the striped envelope",
                  "the saffron envelope", "the kingfisher envelope",
                  "the patchwork envelope", "the oxblood envelope",
                  "the silver envelope", "the moss-green envelope"),
            _axis("landing", "Landed at", "landing site", "comes down in", "a cricket pitch",
                  "a flooded quarry", "a cabbage field", "a caravan park",
                  "a railway siding", "a golf course bunker", "a reservoir bank"),
            _axis("ballast", "Ballast", "ballast", "carries", "sandbags", "pea gravel",
                  "bottled water", "lead shot", "rock salt", "iron filings",
                  "dried beans"),
        ),
    ),
    Theme(
        slug="observatory",
        title="A Bad Week at the Pinhole Observatory",
        entity_noun="astronomer",
        entity_noun_plural="astronomers",
        blurb=(
            "The Pinhole Amateur Astronomical Society has one good telescope and "
            "a great many strong opinions about who may point it where."
        ),
        spine=WEEKDAYS,
        spine_verb="observes on",
        axes=(
            _actor("astronomer", "Astronomer", "astronomer", "Niamh", "Ptolemy",
                  "Ingrid", "Cornelius", "Beatrix", "Dmitri", "Sunniva"),
            _axis("target", "Observed", "target", "studies", "the Crab Nebula",
                  "a lunar occultation", "Saturn's rings", "a variable star",
                  "the Andromeda galaxy", "a comet fragment", "sunspots"),
            _axis("mishap", "Mishap", "mishap", "is undone by", "a dewed-up eyepiece",
                  "a dropped lens cap", "a seized mount", "a neighbour's floodlight",
                  "a flat battery", "a cracked filter", "an unexpected cloud bank"),
            _axis("snack", "Thermos contents", "thermos", "brings", "oxtail soup",
                  "stewed tea", "cocoa", "mulled cider", "black coffee",
                  "barley water", "bone broth"),
        ),
    ),
    Theme(
        slug="pigeon",
        title="Andy's Swiftest Birds",
        entity_noun="pigeon",
        entity_noun_plural="pigeons",
        entity_animate=False,
        blurb=(
            "Andy races pigeons, and each bird is bred for a different "
            "combination of stubbornness and speed."
        ),
        spine=DISTANCES,
        spine_verb="flies",
        axes=(
            _actor("bird", "Pigeon", "pigeon", "Cadwallader", "Pip", "Hieronymus",
                  "Dot", "Alabaster", "Nutmeg", "Grimsby"),
            _axis("plumage", "Plumage", "plumage", "is", "slate blue", "chequered black",
                  "mealy red", "pied white", "grizzle", "dun", "bronze"),
            _axis("breed", "Breed", "breed", "descends from", "a Janssen", "a Busschaert",
                  "a Delbar", "a Sion", "a Stichelbaut", "a Vandenabeele",
                  "a Van Loon"),
            _axis("loft", "Loft", "loft", "is kept in", "the orchard loft", "the gable loft",
                  "the garage loft", "the canal loft", "the allotment loft",
                  "the stable loft", "the chapel loft"),
        ),
    ),
    Theme(
        slug="cheese",
        title="The Cheesemongers' Standoff",
        entity_noun="cheese",
        entity_noun_plural="cheeses",
        entity_animate=False,
        blurb=(
            "A case of opinionated cheeses, their equally opinionated makers, and one "
            "display that has begun to smell like a political scandal."
        ),
        spine=PRICES,
        spine_verb="sells for",
        axes=(
            _actor("cheese", "Cheese", "cheese", "Fenland Blue", "Oakmoss",
                  "Winter Tarn", "Bellringer", "Saltpans", "Glebe Farmhouse",
                  "Old Thrashing"),
            _axis("maker", "Maker", "maker", "was made by", "Ambrose", "Sigrid", "Teodoro",
                  "Hepzibah", "Lachlan", "Perdita", "Olubunmi"),
            _axis("rind", "Rind", "rind", "has", "a cloth-bound rind", "a washed rind",
                  "an ash-coated rind", "a nettle-wrapped rind",
                  "a waxed rind", "a natural rind", "a cider-washed rind"),
            _axis("age", "Aged for", "ageing", "was aged for", "three weeks", "two months",
                  "five months", "nine months", "fourteen months",
                  "two years", "thirty months"),
        ),
    ),
    Theme(
        slug="radio",
        title="The Graveyard Shift at WPKX",
        entity_noun="host",
        entity_noun_plural="hosts",
        blurb=(
            "Nobody at WPKX has met anyone on the overnight schedule, which is "
            "how the station likes it."
        ),
        spine=SLOTS,
        spine_verb="broadcasts in",
        axes=(
            _actor("host", "Host", "host", "Dustin Crowe", "Maribel Sosa",
                  "Gideon Park", "Nadia Vell", "Arlo Finch", "Bea Okonjo",
                  "Rusty Lamarr"),
            _axis("show", "Show", "show", "presents", "Night Freight", "The Sleepless Hour",
                  "Static & Sons", "Coffee and Regrets", "The Long Haul",
                  "Owls Calling", "Signal Fade"),
            _axis("genre", "Format", "format", "plays", "trucker country",
                  "obscure jazz", "listener call-ins", "forgotten soul",
                  "radio plays", "lost surf rock", "church organ recordings"),
            _axis("sponsor", "Sponsor", "sponsor", "is sponsored by", "a mattress warehouse",
                  "a bail bondsman", "a chain of car washes", "a psychic hotline",
                  "a taxidermist", "a discount dentist", "a storage facility"),
        ),
    ),
    Theme(
        slug="allotment",
        title="Plot Wars on the Ashcombe Allotments",
        entity_noun="plot-holder",
        entity_noun_plural="plot-holders",
        blurb=(
            "The Ashcombe allotment committee has been locked in a slow war over "
            "compost, shade and the correct way to stake a bean."
        ),
        spine=PLACINGS,
        spine_verb="places",
        axes=(
            _actor("holder", "Plot-holder", "plot-holder", "Ewan", "Rosamund",
                  "Kasimir", "Philippa", "Obadiah", "Senga", "Alphonse"),
            _axis("crop", "Prize crop", "crop", "grows", "a marrow", "a rhubarb crown",
                  "a row of leeks", "a pumpkin", "a bed of beetroot",
                  "a runner bean", "a cauliflower"),
            _axis("plot", "Plot", "plot", "works", "plot 2", "plot 7", "plot 11",
                  "plot 14", "plot 19", "plot 23", "plot 31"),
            _axis("shed", "Shed", "shed", "keeps", "a tar-paper shed", "a greenhouse",
                  "a converted privy", "a corrugated lean-to",
                  "an upturned boat", "a brick bothy", "a tarpaulin frame"),
        ),
    ),
    Theme(
        slug="clockmaker",
        title="A Benchful of Clocks, and No Agreement",
        entity_noun="clock",
        entity_noun_plural="clocks",
        entity_animate=False,
        blurb=(
            "Mr Halloran repairs clocks. Those on the bench are all insisting on a "
            "different hour."
        ),
        spine=SHELVES,
        spine_verb="sits on",
        axes=(
            _actor("clock", "Clock", "clock", "a carriage clock", "a cuckoo clock",
                  "a ship's chronometer", "a longcase clock",
                  "a mantel clock under glass", "a station clock",
                  "an anniversary clock"),
            _axis("owner", "Owner", "owner", "belongs to", "Ms Abernathy", "Dr Vasquez",
                  "Father Brennan", "Mrs Oyelaran", "Captain Mott",
                  "Miss Trevelyan", "Mr Dziedzic"),
            _axis("fault", "Fault", "fault", "suffers from", "a snapped mainspring",
                  "a worn escape wheel", "a bent pendulum rod",
                  "a seized fusee", "a cracked suspension spring",
                  "a missing click spring", "a gummed-up pivot"),
            _axis("chime", "Chime", "chime", "sounds", "Westminster", "a single strike",
                  "Whittington", "a bell and gong", "a cuckoo call",
                  "a ship's bell", "no chime at all"),
        ),
    ),
    Theme(
        slug="regatta",
        title="The Mudflat Regatta",
        entity_noun="crew",
        entity_noun_plural="crews",
        blurb=(
            "The Mudflat Regatta is rowed over a course that is only a course at "
            "high tide, which is where most of the trouble starts."
        ),
        spine=PLACINGS,
        spine_verb="finishes",
        axes=(
            _actor("crew", "Crew", "crew", "the Tannery crew", "the Brickworks crew",
                  "the Seminary crew", "the Gasworks crew", "the Customs crew",
                  "the Almshouse crew", "the Creamery crew"),
            _axis("stroke", "Stroke", "stroke", "is stroked by", "Ondine", "Bartholomew",
                  "Maeve", "Crispin", "Yusuf", "Thomasina", "Everard"),
            _axis("boat", "Boat", "boat", "rows", "the Dauntless", "the Wet Hen",
                  "the Peregrine", "the Mudlark", "the Obstinate",
                  "the Gilded Eel", "the Last Resort"),
            _axis("colours", "Colours", "colours", "wears", "mustard and black",
                  "cherry and grey", "bottle green", "pink and cream",
                  "navy with a white band", "scarlet", "lilac and bronze"),
        ),
    ),
    Theme(
        slug="beekeeper",
        title="The Honey Show Scandal",
        entity_noun="beekeeper",
        entity_noun_plural="beekeepers",
        blurb=(
            "The annual honey show has been judged, and at least two people are "
            "writing letters about it."
        ),
        spine=ENTRY_FEES,
        spine_verb="pays",
        axes=(
            _actor("keeper", "Beekeeper", "beekeeper", "Wilhelmina", "Fausto",
                  "Breda", "Ezekiel", "Antonina", "Mungo", "Priya"),
            _axis("honey", "Honey", "honey", "enters", "heather honey", "lime blossom honey",
                  "borage honey", "chestnut honey", "clover honey",
                  "ivy honey", "sea lavender honey"),
            _axis("hive", "Hive type", "hive", "keeps", "a national hive", "a WBC hive",
                  "a Warre hive", "a top-bar hive", "a Langstroth hive",
                  "a skep", "a long deep hive"),
            _axis("verdict", "Judge's note", "note", "has a jar noted as", "crystallised early",
                  "exemplary clarity", "a trace of wax", "slightly over-filtered",
                  "an overbearing aroma", "a cloudy jar", "an unlabelled lid"),
        ),
    ),
    Theme(
        slug="puppet",
        title="A Fortnight at the Little Vesper Theatre",
        entity_noun="puppeteer",
        entity_noun_plural="puppeteers",
        blurb=(
            "The Little Vesper Theatre seats forty people and employs a company of "
            "puppeteers who will not be in the same room together."
        ),
        spine=SLOTS,
        spine_verb="performs in",
        axes=(
            _actor("puppeteer", "Puppeteer", "puppeteer", "Lorcan", "Mirabel",
                  "Stellan", "Josefa", "Quentin", "Halima", "Bowen"),
            _axis("puppet", "Lead puppet", "puppet", "works", "a tin soldier",
                  "a moth queen", "a one-eyed cat", "a drowned sailor",
                  "a paper crane", "a brass magistrate", "a shepherd boy"),
            _axis("play", "Play", "play", "stages", "The Drowned Bell", "Winterling",
                  "Six Spoons", "The Clockwork Orchard", "Marrowbone",
                  "The Glass Tide", "Hollowmas"),
            _axis("music", "Accompaniment", "accompaniment", "is accompanied by", "a hurdy-gurdy",
                  "a musical saw", "a prepared piano", "a bowed psaltery",
                  "a pump organ", "two kettle drums", "a glass harmonica"),
        ),
    ),
    Theme(
        slug="tea",
        title="The Blind Tasting at Pemberton's",
        entity_noun="taster",
        entity_noun_plural="tasters",
        blurb=(
            "Pemberton's holds a blind tasting each spring. The tasters are blind "
            "to the tea; the tea is not blind to them."
        ),
        spine=MORNINGS,
        spine_verb="tastes at",
        axes=(
            _actor("taster", "Taster", "taster", "Ignatia", "Rolf", "Chidi",
                  "Marguerite", "Soren", "Yolanda", "Bertrand"),
            _axis("tea", "Tea", "tea", "samples", "a smoked Lapsang", "a first-flush Darjeeling",
                  "a roasted oolong", "a pressed pu-erh", "a silver needle white",
                  "a Keemun", "a Nilgiri frost"),
            _axis("note", "Tasting note", "note", "reports", "wet slate", "stewed apricot",
                  "pine smoke", "hay and honey", "iron filings",
                  "bruised peach", "cold butter"),
            _axis("cup", "Cup", "cup", "drinks from", "a chipped blue cup", "a bone china cup",
                  "a pewter beaker", "a glass tumbler", "an enamel mug",
                  "a lacquered bowl", "a stoneware cup"),
        ),
    ),
    Theme(
        slug="kite",
        title="The Wind Is Free, the Field Is Not",
        entity_noun="flier",
        entity_noun_plural="fliers",
        blurb=(
            "The Dunnage Kite Festival charges by the kite, which has produced "
            "some creative definitions of 'one kite'."
        ),
        spine=ENTRY_FEES,
        spine_verb="pays",
        axes=(
            _actor("flier", "Flier", "flier", "Aurelio", "Tansy", "Gunnar",
                  "Ifeoma", "Blaise", "Morwenna", "Kipling"),
            _axis("kite", "Kite", "kite", "flies", "a box kite", "a delta wing",
                  "a seven-metre centipede", "a paper sled kite",
                  "a rokkaku fighter", "a parafoil", "a hand-painted dragon"),
            _axis("mishap", "Mishap", "mishap", "is undone by", "a tangled line",
                  "a snapped spar", "a tree", "a sudden lull",
                  "a trespassing dog", "a lost tail", "a power line scare"),
            _axis("line", "Line", "line", "uses", "waxed cotton", "braided dacron",
                  "nylon twine", "fishing monofilament", "hemp cord",
                  "kevlar thread", "parcel string"),
        ),
    ),
    Theme(
        slug="mushroom",
        title="The Foragers of Thorn Bottom",
        entity_noun="forager",
        entity_noun_plural="foragers",
        blurb=(
            "The Thorn Bottom foraging club keeps meticulous records, chiefly so "
            "that blame can be apportioned later."
        ),
        spine=WEEKDAYS,
        spine_verb="forages on",
        axes=(
            _actor("forager", "Forager", "forager", "Ottokar", "Eilish", "Ramiro",
                  "Guinevere", "Tobias", "Annika", "Solomon"),
            _axis("find", "Find", "find", "finds", "a hen of the woods", "a horn of plenty",
                  "a parasol mushroom", "a cauliflower fungus",
                  "a saffron milk cap", "a chicken of the woods", "a penny bun"),
            _axis("wood", "Wood", "wood", "searches", "Hangman's Copse", "Bell Wood",
                  "the Larches", "Dovecote Wood", "Scrag End",
                  "the Old Deer Park", "Nettlebed"),
            _axis("basket", "Basket", "basket", "carries", "a wicker trug", "a canvas satchel",
                  "a tin pail", "a willow creel", "a string bag",
                  "an upturned hat", "a wooden box"),
        ),
    ),
    Theme(
        slug="archive",
        title="The Mislabelled Drawers",
        entity_noun="archivist",
        entity_noun_plural="archivists",
        blurb=(
            "The Vance Municipal Archive was reorganised in 1974 by somebody who "
            "has since left no forwarding address."
        ),
        spine=SHELVES,
        spine_verb="files on",
        axes=(
            _actor("archivist", "Archivist", "archivist", "Ms Okafor",
                  "Mr Ravensworth", "Dr Lindqvist", "Ms Bhattacharya",
                  "Mr Pelletier", "Ms Castellano", "Dr Mwangi"),
            _axis("holding", "Holding", "holding", "catalogues", "the harbour dredging reports",
                  "a box of unopened wills", "the smallpox ledgers",
                  "a set of tram timetables", "the workhouse admissions book",
                  "a folder of libel writs", "the lost property register"),
            _axis("decade", "Decade", "decade", "covers", "the 1830s", "the 1860s",
                  "the 1890s", "the 1910s", "the 1940s", "the 1950s",
                  "the 1970s"),
            _axis("damage", "Condition", "condition", "describes theirs as", "foxed", "water-damaged",
                  "mouse-chewed", "fire-scorched", "immaculate",
                  "over-repaired with tape", "bound upside down"),
        ),
    ),
    Theme(
        slug="chess",
        title="The Ravelston Chess Club Ladder",
        entity_noun="player",
        entity_noun_plural="players",
        blurb=(
            "The Ravelston Chess Club ladder is recalculated monthly and disputed "
            "continuously."
        ),
        spine=PLACINGS,
        spine_verb="places",
        axes=(
            _actor("player", "Player", "player", "Yevgenia", "Dermot", "Adaeze",
                  "Casimir", "Birgitta", "Olumide", "Hieronyma"),
            _axis("opening", "Favourite opening", "opening", "favours", "the Dutch Defence",
                  "the Catalan", "the Vienna Game", "the Scandinavian",
                  "the Grunfeld", "the London System", "the Bird's Opening"),
            _axis("clock", "Clock", "clock", "uses", "a wooden analogue clock",
                  "a borrowed digital clock", "a chipped BHB clock",
                  "a phone app", "a hotel alarm clock", "no clock at all",
                  "a tournament DGT clock"),
            _axis("habit", "Table habit", "habit", "is known for", "humming",
                  "rearranging the captured pieces", "leaving between moves",
                  "narrating in a whisper", "eating boiled sweets",
                  "writing notation in pencil", "removing their shoes"),
        ),
    ),
    Theme(
        slug="ferry",
        title="The Crossings to Inverlaig",
        entity_noun="skipper",
        entity_noun_plural="skippers",
        blurb=(
            "The Inverlaig ferry runs a full day of crossings in theory, and a "
            "variable number in practice."
        ),
        spine=MORNINGS,
        spine_verb="sails at",
        axes=(
            _actor("skipper", "Skipper", "skipper", "Eilidh", "Murdo", "Calla",
                  "Fearghas", "Tormod", "Senga", "Ruaridh"),
            _axis("cargo", "Notable cargo", "cargo", "carries", "a church organ",
                  "nineteen sheep", "a wedding party", "a refrigerated van",
                  "a brass band", "a consignment of bees",
                  "a film crew and no permits"),
            _axis("vessel", "Vessel", "vessel", "commands", "the Siller Grey",
                  "the Kelpie", "the Steadfast", "the Broch Maid",
                  "the Ailsa Belle", "the Three Brothers", "the Tern"),
            _axis("delay", "Delay blamed on", "reason", "blames", "fog", "a slipway repair",
                  "a missing deckhand", "a fouled propeller",
                  "the tide", "a passenger's dog", "paperwork"),
        ),
    ),
    Theme(
        slug="knitting",
        title="The Ashfold Knitting Circle",
        entity_noun="knitter",
        entity_noun_plural="knitters",
        blurb=(
            "The Ashfold Knitting Circle meets weekly and has not agreed on "
            "anything since 1998."
        ),
        spine=WEEKDAYS,
        spine_verb="knits on",
        axes=(
            _actor("knitter", "Knitter", "knitter", "Ebba", "Lionel", "Nkechi",
                  "Wilhelm", "Serafina", "Angus", "Maudie"),
            _axis("project", "Project", "project", "is making", "a fisherman's gansey",
                  "a shawl of impossible lace", "a pair of argyle socks",
                  "a dog coat", "a Fair Isle tam", "a cable-knit blanket",
                  "a tea cosy shaped like a hen"),
            _axis("yarn", "Yarn", "yarn", "works in", "undyed Shetland", "hand-spun alpaca",
                  "recycled sari silk", "oily Guernsey wool",
                  "mohair of great expense", "mill-end acrylic",
                  "nettle fibre"),
            _axis("snag", "Setback", "setback", "is set back by", "a dropped stitch in row nine",
                  "running out of dye lot", "a cat", "a misread chart",
                  "a broken circular needle", "unexplained shrinkage",
                  "losing the pattern entirely"),
        ),
    ),
    Theme(
        slug="jam",
        title="Preserves, and the Preservation of Grudges",
        entity_noun="entrant",
        entity_noun_plural="entrants",
        blurb=(
            "The preserves tent is the most competitive building at the show, and "
            "the only one with a locked door."
        ),
        spine=PRICES,
        spine_verb="charges",
        axes=(
            _actor("entrant", "Entrant", "entrant", "Drusilla", "Emeka", "Harriet",
                  "Stanislaw", "Ottilie", "Rafferty", "Bernadette"),
            _axis("preserve", "Preserve", "preserve", "enters", "quince jelly",
                  "damson cheese", "green walnut pickle", "rosehip syrup",
                  "medlar jam", "sloe and apple butter", "hot pepper jelly"),
            _axis("jar", "Jar", "jar", "uses", "a squat kilner", "a recycled honey jar",
                  "a hexagonal jar", "a tall french jar",
                  "a jar with a cloth lid", "a sealed crock", "an unlabelled jar"),
            _axis("secret", "Secret ingredient", "ingredient", "adds", "a bay leaf",
                  "a splash of gin", "black pepper", "orange zest",
                  "a spoon of treacle", "star anise", "nothing whatsoever"),
        ),
    ),
    Theme(
        slug="aquarium",
        title="The Night Shift at Coldwater Hall",
        entity_noun="keeper",
        entity_noun_plural="keepers",
        blurb=(
            "Coldwater Hall Aquarium keeps a night rota of tanks, and one keeper who "
            "is definitely feeding the wrong things."
        ),
        spine=SLOTS,
        spine_verb="works",
        axes=(
            _actor("keeper", "Keeper", "keeper", "Marisol", "Oskar", "Chiamaka",
                  "Fitzwilliam", "Agnetha", "Bartolo", "Rhiannon"),
            _axis("tank", "Tank", "tank", "tends", "the kelp tank", "the jellyfish column",
                  "the touch pool", "the deep reef", "the estuary tank",
                  "the seahorse nursery", "the octopus enclosure"),
            _axis("feed", "Feed", "feed", "feeds", "brine shrimp", "chopped squid",
                  "frozen krill", "live mysis", "nori sheets",
                  "mussel meat", "a gelatine cube of unclear provenance"),
            _axis("incident", "Logged incident", "incident", "logs", "a cracked viewing pane",
                  "an escapee", "a failed chiller", "an algal bloom",
                  "a blocked skimmer", "a visitor's dropped phone",
                  "an unexplained pH swing"),
        ),
    ),
    Theme(
        slug="karaoke",
        title="Tuesday Night at the Dented Bell",
        entity_noun="singer",
        entity_noun_plural="singers",
        blurb=(
            "The Dented Bell runs karaoke on Tuesdays. Attendance is loyal; "
            "talent is not."
        ),
        spine=SLOTS,
        spine_verb="sings in",
        axes=(
            _actor("singer", "Singer", "singer", "Deshawn", "Pernilla", "Vikram",
                  "Caitriona", "Bogdan", "Annalise", "Mercy"),
            _axis("song", "Song", "song", "performs", "a power ballad",
                  "a novelty country number", "an eight-minute prog epic",
                  "a disco standard", "a maudlin folk song",
                  "a rap performed entirely from memory", "a sea shanty"),
            _axis("drink", "Drink", "drink", "orders", "a pint of mild", "a lime and soda",
                  "a double whisky", "a cider in a plastic cup",
                  "a glass of the house red", "a rum and coke", "tap water"),
            _axis("reception", "Reception", "reception", "gets", "a standing ovation",
                  "polite silence", "a singalong", "one heckler",
                  "the landlord cutting the power", "scattered applause",
                  "a request for an encore nobody wanted"),
        ),
    ),
    Theme(
        slug="sandcastle",
        title="The Grindle Bay Sandcastle Open",
        entity_noun="builder",
        entity_noun_plural="builders",
        blurb=(
            "The Grindle Bay Open is judged at four o'clock, whatever the tide is "
            "doing."
        ),
        spine=PLACINGS,
        spine_verb="places",
        axes=(
            _actor("builder", "Builder", "builder", "Juniper", "Aleksy", "Temperance",
                  "Khalid", "Fenwick", "Bronagh", "Hartley"),
            _axis("build", "Build", "build", "builds", "a moated keep",
                  "a scale model of the pier", "a sleeping dragon",
                  "a cathedral with flying buttresses", "a hollow lighthouse",
                  "a recumbent walrus", "a spiral ziggurat"),
            _axis("tool", "Chief tool", "tool", "works with", "a cake slice", "a soup spoon",
                  "a paint scraper", "a bucket with no handle",
                  "a pastry brush", "bare hands", "a child's rake"),
            _axis("ruin", "Undone by", "cause", "is undone by", "the incoming tide",
                  "a loose dog", "a gull", "a cricket ball",
                  "structural overreach", "a sudden shower", "a rival's elbow"),
        ),
    ),
    Theme(
        slug="train",
        title="The Loft Layout Dispute",
        entity_noun="modeller",
        entity_noun_plural="modellers",
        blurb=(
            "The members of the model railway society share one loft layout and a "
            "deep well of resentment."
        ),
        spine=SHELVES,
        spine_verb="stores on",
        axes=(
            _actor("modeller", "Modeller", "modeller", "Cuthbert", "Lavinia",
                  "Abiodun", "Hendrik", "Rosamond", "Gilbert", "Esperanza"),
            _axis("stock", "Rolling stock", "stock", "owns", "a brass pannier tank",
                  "a kit-built brake van", "a rake of milk tankers",
                  "an unpainted shunter", "a gleaming Pacific",
                  "a scratch-built crane wagon", "a battered autocoach"),
            _axis("scenery", "Scenery", "scenery", "builds", "a cardboard viaduct",
                  "a flocked cutting", "a plaster tunnel mouth",
                  "a coal staithe", "a working level crossing",
                  "a sheet of static grass", "a river of resin"),
            _axis("grievance", "Grievance", "grievance", "complains about", "the timetable",
                  "the wiring", "somebody else's couplings",
                  "the choice of era", "the position of the fiddle yard",
                  "the lighting", "a missing screwdriver"),
        ),
    ),
    Theme(
        slug="orchid",
        title="The Orchid House Reckoning",
        entity_noun="grower",
        entity_noun_plural="growers",
        blurb=(
            "The orchid house at Fenn Park is shared by its growers, each convinced "
            "the others are overwatering."
        ),
        spine=MONTHS,
        spine_verb="harvests in",
        spine_noun="harvest month",
        axes=(
            _actor("grower", "Grower", "grower", "Leocadia", "Ambrose",
                  "Nkiruka", "Sigismund", "Rowena", "Taavi", "Columbine"),
            _axis("orchid", "Orchid", "orchid", "grows", "a moth orchid",
                  "a slipper orchid", "a vanilla vine", "a dancing lady",
                  "a jewel orchid", "a ghost orchid", "a bucket orchid"),
            _axis("mix", "Potting mix", "potting mix", "pots in", "bark chip", "sphagnum moss",
                  "perlite and charcoal", "coconut husk", "lava rock",
                  "tree fern fibre", "bare root on cork"),
            _axis("pest", "Pest", "pest", "is troubled by", "scale insects", "mealybug",
                  "thrips", "fungus gnats", "red spider mite",
                  "a persistent slug", "root rot"),
        ),
    ),
    Theme(
        slug="detective",
        title="The Case of the Missing Trowel",
        entity_noun="investigator",
        entity_noun_plural="investigators",
        blurb=(
            "The Marchmont Mutual Improvement Society has taken on the case of "
            "the missing trowel with a seriousness it has never shown a book."
        ),
        spine=MORNINGS,
        spine_verb="reports at",
        axes=(
            _actor("sleuth", "Investigator", "investigator", "Hortensia",
                  "Barnabas", "Ngozi", "Leopold", "Ariadne", "Fergus", "Immaculata"),
            _axis("theory", "Theory", "theory", "favours", "an inside job",
                  "a magpie", "a clerical error", "the postman",
                  "a jealous rival", "nothing happened at all",
                  "a conspiracy of two"),
            _axis("clue", "Clue produced", "clue", "produces", "a bootprint",
                  "a torn receipt", "a smell of creosote",
                  "an anonymous note", "a dropped glove",
                  "a tyre mark", "an unexplained hole"),
            _axis("alibi", "Alibi", "alibi", "claims", "the dentist", "a long bath",
                  "choir practice", "a bus replacement service",
                  "a locked greenhouse", "watching the snooker",
                  "no alibi whatsoever"),
        ),
    ),
    # -----------------------------------------------------------------
    # Research-backed packs.  The vocabulary in these is the real thing --
    # Grandsire Triples is a method, Dabinett is a cider apple, a lunky hole
    # is a sheep gap at the foot of a wall -- because specificity does work
    # that invention cannot: a solver who knows the domain feels the setting
    # is real, and one who does not still feels that somebody knew.
    # -----------------------------------------------------------------
    Theme(
        slug="bellringing",
        title="The Quarter-Peal at St Botolph's",
        entity_noun="ringer",
        entity_noun_plural="ringers",
        blurb=(
            "Six ringers, six rounds of the Tuesday practice, and a tower "
            "captain keeping a ledger of everyone's mistakes."
        ),
        spine=ROUNDS,
        spine_verb="rings in",
        spine_noun="round",
        axes=(
            _actor("ringer", "Ringer", "ringer", "Hesketh", "Prudence", "Osbert",
                   "Lavinia", "Fenwick", "Dorcas", "Ambrose"),
            _axis("method", "Method", "method", "calls", "Grandsire Triples",
                  "Plain Bob Major", "Stedman Caters", "Kent Treble Bob",
                  "Cambridge Surprise Minor", "Grandsire Doubles",
                  "Plain Bob Minor"),
            _axis("bell", "Bell", "bell", "takes", "the treble", "the second",
                  "the third", "the fourth", "the fifth", "the tenor",
                  "the sharp second"),
            _axis("slip", "Slip", "slip", "is blamed for", "a fired shot",
                  "a missed dodge", "going methodless", "a clipped backstroke",
                  "an early snap lead", "a dropped rope", "nothing at all"),
        ),
    ),
    Theme(
        slug="sheepdog",
        title="The Clun Forest Trials",
        entity_noun="handler",
        entity_noun_plural="handlers",
        blurb=(
            "A hillside, six handlers, and a judge who deducts for a wide "
            "outrun with the enthusiasm of a man settling an old score."
        ),
        spine=POINTS,
        spine_verb="scores",
        spine_noun="score",
        axes=(
            _actor("handler", "Handler", "handler", "Eiddwen", "Tarrant",
                   "Marged", "Huw Pryce", "Constance", "Idris", "Nerys"),
            _axis("dog", "Dog", "dog", "runs", "Nell", "Moss", "Gyp", "Craig",
                  "Bute", "Tweed", "Fly"),
            _axis("flock", "Flock", "flock", "gathers", "Swaledales", "Cheviots",
                  "Herdwicks", "Rough Fells", "Dalesbreds", "Lonks", "Beulahs"),
            _axis("fault", "Fault", "fault", "loses points for", "a wide outrun",
                  "a hard lift", "an off-line fetch", "crossing on the drive",
                  "a missed shed", "a refusal at the pen", "a clean run"),
        ),
    ),
    Theme(
        slug="cider",
        title="The Pomace and the Prize",
        entity_noun="maker",
        entity_noun_plural="makers",
        blurb=(
            "Six makers press in six different months and each is privately "
            "certain the others have let theirs go to vinegar."
        ),
        spine=MONTHS,
        spine_verb="presses in",
        spine_noun="pressing month",
        axes=(
            _actor("maker", "Maker", "maker", "Haskell", "Morwenna", "Jethro",
                   "Araminta", "Silas Vane", "Petroc", "Bryony"),
            _axis("apple", "Apple", "apple", "presses", "Kingston Black",
                  "Yarlington Mill", "Dabinett", "Foxwhelp",
                  "Somerset Redstreak", "Harry Masters Jersey", "Browns Apple"),
            _axis("vessel", "Vessel", "vessel", "ferments in", "an oak hogshead",
                  "a plastic barrel", "a glass demijohn", "a rum cask",
                  "a stainless tank", "an earthenware jar", "a sherry butt"),
            _axis("fault", "Fault", "fault", "is accused of", "mousiness",
                  "acetification", "ropiness", "a stuck ferment",
                  "a framboise note", "sulphur", "nothing detectable"),
        ),
    ),
    Theme(
        slug="letterpress",
        title="The Jobbing Shop on Dyer's Row",
        entity_noun="compositor",
        entity_noun_plural="compositors",
        blurb=(
            "A jobbing print shop with six compositors, six quoted prices and "
            "one hell-box filling up faster than anybody will admit to."
        ),
        spine=PRICES,
        spine_verb="quotes",
        spine_noun="quoted price",
        axes=(
            _actor("compositor", "Compositor", "compositor", "Verity Stallard",
                   "Alfred Nunn", "Josiah Peake", "Winifred Oakes",
                   "Cecil Braddock", "Harriet Lisle", "Ned Ashby"),
            _axis("face", "Typeface", "typeface", "sets in", "Caslon",
                  "Baskerville", "Gill Sans", "Bodoni", "Garamond", "Perpetua",
                  "Plantin"),
            _axis("job", "Job", "job", "is setting", "a parish newsletter",
                  "an auction bill", "a wedding order of service",
                  "a seed catalogue", "a funeral card", "a regatta programme",
                  "a hardware invoice"),
            _axis("mishap", "Mishap", "mishap", "owns up to", "a pied forme",
                  "a loose quoin", "an inverted sort", "a slurred impression",
                  "a cracked chase", "type left in the galley", "a clean run"),
        ),
    ),
    Theme(
        slug="rodeo",
        title="The Cutbank County Rodeo",
        entity_noun="rider",
        entity_noun_plural="riders",
        blurb=(
            "Six riders, six entry fees paid in cash at the gate, and a "
            "scoreboard that nobody trusts."
        ),
        spine=ENTRY_FEES,
        spine_verb="pays",
        spine_noun="entry fee",
        axes=(
            _actor("rider", "Rider", "rider", "Dalton Reese", "Marla Hobbs",
                   "Cody Vance", "Earlene Tate", "Buck Jessup", "Roselle Kerr",
                   "Travis Mundy"),
            _axis("event", "Event", "event", "enters", "bull riding",
                  "saddle bronc", "bareback", "steer wrestling", "team roping",
                  "tie-down roping", "barrel racing"),
            _axis("stock", "Stock drawn", "animal", "draws", "Widowmaker",
                  "Little Sister", "Tumbleweed", "Brimstone", "Half Past Three",
                  "Copper Penny", "Sunday Sermon"),
            _axis("outcome", "Outcome", "outcome", "finishes with", "a clean ride",
                  "a no-score", "a broken barrier", "a slap of the free hand",
                  "a blown stirrup", "a re-ride", "a disqualification"),
        ),
    ),
    Theme(
        slug="bonsai",
        title="The Autumn Show at Kiyosumi",
        entity_noun="exhibitor",
        entity_noun_plural="exhibitors",
        blurb=(
            "Six trees on six stands, judged on a hundred-point sheet, and the "
            "wiring marks are what everybody is looking for."
        ),
        spine=POINTS,
        spine_verb="is awarded",
        spine_noun="judged score",
        axes=(
            _actor("exhibitor", "Exhibitor", "exhibitor", "Keiko Tanabe",
                   "Hiroshi Mita", "Sumire Oda", "Takumi Ishii", "Noriko Hase",
                   "Jun Kawabe", "Emi Tsuchida"),
            _axis("style", "Style", "style", "shows", "moyogi", "shakan",
                  "kengai", "han-kengai", "chokkan", "bunjin", "ikadabuki"),
            _axis("species", "Species", "species", "has grown", "a trident maple",
                  "a Japanese black pine", "a satsuki azalea", "a zelkova",
                  "a hinoki cypress", "a Chinese quince", "a winged elm"),
            _axis("flaw", "Flaw noted", "flaw", "is marked down for",
                  "visible wiring scars", "reverse taper", "a bar branch",
                  "an eye-poking branch", "a weak nebari", "a crossing root",
                  "no flaw at all"),
        ),
    ),
    Theme(
        slug="drystone",
        title="The Walling Match at Gunnerside",
        entity_noun="waller",
        entity_noun_plural="wallers",
        blurb=(
            "Six wallers, a measured length of fallen wall each, and a whole "
            "morning in which to rebuild it to the satisfaction of a judge "
            "who will push on every cope."
        ),
        spine=MORNINGS,
        spine_verb="finishes at",
        spine_noun="finishing time",
        axes=(
            _actor("waller", "Waller", "waller", "Ewart Beck", "Hilda Crowther",
                   "Tam Ridley", "Jenny Fawcett", "Ossian Baird", "Mab Teasdale",
                   "Clem Hartley"),
            _axis("stone", "Stone", "stone", "works in", "Dales limestone",
                  "millstone grit", "green slate", "red sandstone",
                  "river cobble", "Cotswold oolite", "Welsh rubble"),
            _axis("feature", "Feature built", "feature", "builds in",
                  "a lunky hole", "a wall head", "a set of throughstones",
                  "a stile", "a cripple hole", "a water smoot",
                  "a plain run of copes"),
            _axis("snag", "Snag", "snag", "is pulled up for", "a running joint",
                  "gravel hearting", "a slipped cope", "too little batter",
                  "a wobbly wall head", "stone left unused", "nothing at all"),
        ),
    ),
    Theme(
        slug="hamradio",
        title="Field Day on Barrow Hill",
        entity_noun="operator",
        entity_noun_plural="operators",
        blurb=(
            "A club field day spread over a week, one operator a night, and a "
            "generator that has its own opinions."
        ),
        spine=WEEKDAYS,
        spine_verb="operates on",
        spine_noun="night",
        axes=(
            _actor("operator", "Operator", "operator", "Ingrid", "Bartholomew",
                   "Nkem", "Rosalind", "Yusuf", "Clementine", "Horace"),
            _axis("band", "Band", "band", "works", "160 metres", "80 metres",
                  "40 metres", "20 metres", "15 metres", "10 metres",
                  "6 metres"),
            _axis("mode", "Mode", "mode", "operates", "CW", "SSB", "FT8",
                  "RTTY", "AM", "PSK31", "slow-scan television"),
            _axis("trouble", "Trouble", "trouble", "is defeated by",
                  "a flat battery", "mains hum", "a snapped dipole leg",
                  "a drifting VFO", "a static crash", "a neighbour's doorbell",
                  "nothing but good propagation"),
        ),
    ),
    Theme(
        slug="shearing",
        title="The Blades Final at Waihopai",
        entity_noun="shearer",
        entity_noun_plural="shearers",
        blurb=(
            "Six shearers down the board, judged on the floor as much as on "
            "the clock, and the wool classer is taking notes."
        ),
        spine=PLACINGS,
        spine_verb="places",
        spine_noun="placing",
        axes=(
            _actor("shearer", "Shearer", "shearer", "Rangi", "Deirdre Pollok",
                   "Tipene", "Wiremu", "Shona Garrick", "Manaia", "Bevan Toft"),
            _axis("breed", "Breed", "breed", "shears", "a Merino",
                  "a Corriedale", "a Romney", "a Perendale", "a Polwarth",
                  "a Coopworth", "a Border Leicester"),
            _axis("handpiece", "Handpiece", "handpiece", "uses",
                  "Lister blades", "a narrow comb", "a wide comb",
                  "a cover comb", "a spare set of blades",
                  "a borrowed handpiece", "an old Sunbeam"),
            _axis("penalty", "Penalty", "penalty", "is docked for",
                  "second cuts", "a skin nick", "a missed belly",
                  "tufts on the britch", "a dropped sheep", "a slow pen",
                  "a faultless board"),
        ),
    ),
    Theme(
        slug="highland",
        title="The Heavies at Kinloch Rannoch",
        entity_noun="thrower",
        entity_noun_plural="throwers",
        blurb=(
            "Six throwers in the heavy events, measured to the foot, in a "
            "field where the wind counts for more than anybody admits."
        ),
        spine=THROWS,
        spine_verb="throws",
        spine_noun="best throw",
        axes=(
            _actor("thrower", "Thrower", "thrower", "Angus Dunbar",
                   "Fiona Strachan", "Lachlan Cree", "Morag Inglis",
                   "Duncan Rait", "Isla Kinnear", "Rab Souter"),
            _axis("event", "Event", "event", "competes in", "the caber toss",
                  "the Braemar stone", "the open stone",
                  "the weight for distance", "the weight over the bar",
                  "the Scottish hammer", "the sheaf toss"),
            _axis("tartan", "Tartan", "tartan", "wears", "Fraser hunting",
                  "Gordon dress", "Cameron of Erracht", "Buchanan",
                  "Mackenzie weathered", "Lamont ancient", "Murray of Atholl"),
            _axis("grumble", "Grumble", "grumble", "complains of",
                  "a soft run-up", "a turned ankle", "a crosswind",
                  "a borrowed caber", "a judge's long measure",
                  "a slipped grip", "no excuse whatsoever"),
        ),
    ),
)

THEMES_BY_SLUG = {t.slug: t for t in THEMES}


def theme(slug: str) -> Theme:
    try:
        return THEMES_BY_SLUG[slug]
    except KeyError:
        raise KeyError(
            f"unknown theme {slug!r}; choose from {sorted(THEMES_BY_SLUG)}"
        ) from None


def themes_for(categories: int, items: int, numeric: bool | None = None) -> list[Theme]:
    """Themes that can supply the requested shape."""
    out = []
    for t in THEMES:
        if t.max_categories() < categories or t.max_items() < items:
            continue
        if numeric is True and t.spine.values is None:
            continue
        if numeric is False and t.spine.values is not None:
            continue
        out.append(t)
    return out
