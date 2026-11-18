"""Calibrate the score -> 1-7 rating thresholds from real generator output.

The difficulty *score* in :mod:`logicgrid.difficulty` is a weighted sum whose
units are arbitrary, so the mapping onto a 1-7 rating has to come from data.
This script samples each generation profile's natural score distribution (band
filtering switched off) and reports the quantiles, plus a suggested threshold
set placed at the boundaries between adjacent profiles.

Run::

    python scripts/calibrate.py --samples 40

then paste the suggested tuple into ``difficulty.THRESHOLDS``.
"""

from __future__ import annotations

import argparse
import statistics
import sys
from pathlib import Path
from random import Random

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from logicgrid.difficulty import PROFILES, THRESHOLDS, rating  # noqa: E402
from logicgrid.generate import PuzzleSpec, attempt_once  # noqa: E402

ORDER = ["gentle", "easy", "moderate", "hard", "expert"]


def sample(name: str, n: int, seed: int) -> list[float]:
    prof = PROFILES[name]
    spec = PuzzleSpec(difficulty=name, seed=seed, strict_band=False)
    rng = Random(seed)
    scores: list[float] = []
    tries = 0
    while len(scores) < n and tries < n * 6:
        tries += 1
        puzzle = attempt_once(spec, prof, rng, tries)
        if puzzle is not None:
            scores.append(puzzle.score)
    return sorted(scores)


def quantile(xs: list[float], q: float) -> float:
    if not xs:
        return float("nan")
    idx = min(len(xs) - 1, max(0, round(q * (len(xs) - 1))))
    return xs[idx]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--samples", type=int, default=30)
    ap.add_argument("--seed", type=int, default=20261118)
    args = ap.parse_args()

    dists: dict[str, list[float]] = {}
    print(f"sampling {args.samples} puzzles per profile...\n")
    for name in ORDER:
        xs = sample(name, args.samples, args.seed)
        dists[name] = xs
        band = PROFILES[name].band
        ratings = [rating(x) for x in xs]
        in_band = sum(1 for r in ratings if band[0] <= r <= band[1])
        print(
            f"{name:9s} n={len(xs):3d} "
            f"min={xs[0]:6.2f} p10={quantile(xs,0.10):6.2f} "
            f"med={statistics.median(xs):6.2f} p90={quantile(xs,0.90):6.2f} "
            f"max={xs[-1]:6.2f} | band={band} in-band={in_band}/{len(xs)}"
        )

    # Place each threshold where two adjacent profiles meet: the midpoint of the
    # upper profile's 10th percentile and the lower profile's 90th.
    print("\nboundaries between adjacent profiles:")
    cuts: list[float] = []
    for lo_name, hi_name in zip(ORDER, ORDER[1:]):
        lo, hi = dists[lo_name], dists[hi_name]
        cut = (quantile(lo, 0.80) + quantile(hi, 0.20)) / 2
        cuts.append(round(cut, 2))
        print(f"  {lo_name:9s} | {hi_name:9s} -> {cut:6.2f}")

    # Ratings wanted: gentle 1-2, easy 2-3, moderate 3-4, hard 5-6, expert 6-7.
    # That needs six thresholds; interpolate the ones the four cuts don't pin.
    if len(cuts) == 4:
        c1, c2, c3, c4 = cuts
        suggested = (
            round(c1 - (c2 - c1) / 2, 2),  # 1|2 below the gentle/easy cut
            round(c1, 2),                  # 2|3 at gentle/easy
            round(c2, 2),                  # 3|4 at easy/moderate
            round(c3, 2),                  # 4|5 at moderate/hard
            round((c3 + c4) / 2, 2),       # 5|6 inside hard
            round(c4, 2),                  # 6|7 at hard/expert
        )
        mono = all(a < b for a, b in zip(suggested, suggested[1:]))
        print(f"\nsuggested THRESHOLDS = {suggested}")
        print(f"current   THRESHOLDS = {THRESHOLDS}")
        if not mono:
            print("WARNING: suggestion is not monotonic; widen the profiles or sample more")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
