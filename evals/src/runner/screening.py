"""The screening mode: one reduced run for a candidate style.

The style-design loop screens many candidate styles cheaply, and only
the best candidate gets a full campaign. A screening run covers a
fixed prompt subset, all measurement axes, and one run instead of
three. The subset draw stratifies over the hedge-rich mark below, so
the subset mirrors the hedge-rich share of the full prompt set
instead of drawing one class only (#111). The subset rule of this
module — the count, the seed, the stratification, and the mark — is
a condition of a screening run: a change makes old screening runs
incomparable with new ones, like a comparability-era change does for
full runs.
"""

from __future__ import annotations

import random

PROMPTS_PER_TYPE = 2
"""The prompts that the subset draws per task type."""

SEED = 0
"""The fixed seed of the subset draw, so the subset is deterministic."""

HEDGE_RICH_IDS = frozenset(
    {
        "code-review-07",
        "code-review-08",
        "debugging-07",
        "debugging-08",
        "explanation-07",
        "explanation-08",
        "summarization-07",
        "summarization-08",
    }
)
"""The hedge-rich prompts of the full set, part of the subset rule.

The mark lives here and not in prompts.yaml, because the provenance
hashes that file whole: a mark inside it would open a comparability
era for every run. A new hedge-rich prompt must be added here, as
the prompt-addition steps of the README state."""

FULL_CAMPAIGN_RUNS = 3
"""The run count of a full campaign, the base of the cost fraction."""

MEASURED_CALL_PERCENT = 25
"""The measured share of the calls of one full run, rounded.

Measured offline against the baseline campaign (runs/2026-08-08 and
runs/2026-08-08b): restrict every stored call row to the stratified
seed-0 subset ids and divide by the run total, with the 18
cost-probe arms whole on both sides, because the probe is per style
and repeat and does not shrink with the subset. Per run: 25.5% and
24.4%. The number is era-scoped: a prompt-set change redraws the
subset and stales it, while the design fractions in the note
recompute.
"""

MEASURED_INPUT_PERCENT = 25
"""The measured share of the input tokens of one full run, rounded.

The same restriction as MEASURED_CALL_PERCENT, in uncached-token
equivalents (an uncached token weighs 1, a cache write 1.25, a cache
read 0.1). Per run: 25.3% and 24.4%. The token share tracks the
call share because the stratified subset mirrors the answer-length
mix of the full set. The same era scoping applies.
"""


def select_screening_prompts(prompts: list[dict]) -> list[dict]:
    """The deterministic prompt subset of a screening run.

    The draw groups the prompt ids per type and samples
    PROMPTS_PER_TYPE ids per type, stratified over HEDGE_RICH_IDS:
    the hedge-rich quota of the subset is the hedge-rich share of
    the full set, rounded, and one shared seeded generator draws
    which types contribute a hedge-rich prompt and which ids fill
    the rest from the confident pool. One generator across the
    types, instead of a re-seeded one per type, so equal-length id
    lists do not repeat the same positions (#111). Every screening
    run over one prompt set uses the same balanced subset. A type
    with fewer prompts contributes all of its prompts, and a set
    without the mark draws from the confident pool alone. The
    result keeps the file order of the prompt set.
    """
    if not prompts:
        return []
    ids_by_type: dict[str, list[str]] = {}
    for prompt in prompts:
        ids_by_type.setdefault(prompt["type"], []).append(prompt["id"])
    rng = random.Random(SEED)
    subset_size = sum(min(PROMPTS_PER_TYPE, len(ids)) for ids in ids_by_type.values())
    hedge_count = sum(1 for prompt in prompts if prompt["id"] in HEDGE_RICH_IDS)
    hedge_types = sorted(
        task_type
        for task_type, ids in ids_by_type.items()
        if any(id_ in HEDGE_RICH_IDS for id_ in ids)
    )
    quota = min(round(subset_size * hedge_count / len(prompts)), len(hedge_types))
    contributing = set(rng.sample(hedge_types, quota))
    chosen: set[str] = set()
    for task_type in sorted(ids_by_type):
        ids = ids_by_type[task_type]
        count = min(PROMPTS_PER_TYPE, len(ids))
        picks: list[str] = []
        if task_type in contributing:
            picks.extend(rng.sample(sorted(id_ for id_ in ids if id_ in HEDGE_RICH_IDS), 1))
        confident = sorted(id_ for id_ in ids if id_ not in HEDGE_RICH_IDS)
        if len(confident) < count - len(picks):
            confident = sorted(id_ for id_ in ids if id_ not in picks)
        picks.extend(rng.sample(confident, count - len(picks)))
        chosen.update(picks)
    return [prompt for prompt in prompts if prompt["id"] in chosen]


def screening_provenance(subset: list[dict], full_count: int) -> dict:
    """The screening block of provenance.json."""
    return {
        "prompts_per_type": PROMPTS_PER_TYPE,
        "seed": SEED,
        "prompt_ids": sorted(prompt["id"] for prompt in subset),
        "hedge_rich_prompt_ids": sorted(
            prompt["id"] for prompt in subset if prompt["id"] in HEDGE_RICH_IDS
        ),
        "full_prompt_count": full_count,
    }


def screening_section(provenance: dict | None) -> list[str]:
    """The screening note of a report, or an empty list.

    The note tells the reader what a screening verdict is worth. The
    design fractions recompute from the subset and prompt counts, so
    they follow a prompt-set change; the measured constants above
    calibrate them against the baseline campaign and hold only for
    the era of that campaign.
    """
    block = (provenance or {}).get("screening")
    if not block:
        return []
    count = len(block["prompt_ids"])
    total = block["full_prompt_count"]
    generation = round(100 * count / (total * FULL_CAMPAIGN_RUNS))
    judged = round(100 * count / total)
    lines = [
        f"**Screening run.** This run covers {count} of {total} prompts, as one",
        f"run instead of {FULL_CAMPAIGN_RUNS}. By design, the generation calls are about",
        f"{generation}% of a full campaign, and the judge calls are about {judged}%",
        "of one full run.",
    ]
    hedge_ids = block.get("hedge_rich_prompt_ids")
    if hedge_ids is not None:
        lines += [
            f"The subset holds {len(hedge_ids)} hedge-rich prompts, mirroring the",
            "hedge-rich share of the full set.",
        ]
    return lines + [
        "Measured against the baseline campaign",
        "(runs/2026-08-08 and runs/2026-08-08b), a screening run holds about",
        f"{MEASURED_CALL_PERCENT}% of the calls and about {MEASURED_INPUT_PERCENT}% of the",
        "weighted input tokens of one full run, plus the full cost",
        "probe, which is per style and does not shrink.",
        "The error bars are wider than in a full run,",
        "because fewer contests feed the bootstrap intervals.",
        "`style-compare` rejects a comparison of this run with a full run.",
        "",
    ]
