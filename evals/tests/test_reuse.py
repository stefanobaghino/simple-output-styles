"""Tests for the shared reuse freshness tolerance.

The clarity picks carry an aggregate tolerance derived from the
measured cross-judge agreement, and the verdict axes keep exact
per-key equality. The CLI tests of the three judge tools cover the
end-to-end paths; these tests pin the rule itself.
"""

from value.reuse import CLARITY_ALPHA, clarity_tolerance, freshness_block


def reused(key, value, check="clarity"):
    return {
        "type": "call",
        "key": key,
        "check": check,
        "role": "pick",
        "value": value,
        "reused_from": "run",
    }


def live(key, value):
    return {"type": "call", "key": key, "value": value}


def parse(row):
    return row.get("value")


def clarity_calls(live_values):
    """Six clarity comparisons whose reused side always holds 1."""
    calls = []
    for index, value in enumerate(live_values):
        key = f"clarity:p{index}:a:b"
        calls += [reused(key, 1), live(key, value)]
    return calls


def test_the_tolerance_warns_at_five_of_six_picks():
    assert clarity_tolerance(6) == 5
    assert clarity_tolerance(5) == 5
    assert clarity_tolerance(4) == 4


def test_three_picks_or_fewer_have_no_reachable_tolerance():
    for n in (0, 1, 2, 3):
        assert clarity_tolerance(n) is None


def test_clarity_disagreements_under_the_tolerance_stay_silent():
    block, warnings = freshness_block(clarity_calls([2, 2, 2, 2, 1, 1]), parse)
    assert warnings == []
    assert block["clarity"] == {
        "compared": 6,
        "disagreements": 4,
        "tolerance": 5,
        "disagree_rate": 0.4,
        "alpha": CLARITY_ALPHA,
        "source": "runs/2026-08-08",
        "stale": False,
    }


def test_clarity_disagreements_at_the_tolerance_warn_once():
    block, warnings = freshness_block(clarity_calls([2, 2, 2, 2, 2, 1]), parse)
    assert len(warnings) == 1
    assert "5 of 6 clarity picks" in warnings[0]
    assert "tolerance of 5" in warnings[0]
    assert not any("the live verdict differs" in warning for warning in warnings)
    assert block["clarity"]["stale"] is True


def test_an_unusable_clarity_side_still_warns_per_key():
    block, warnings = freshness_block(clarity_calls([1, 1, 1, 1, 1, None]), parse)
    assert warnings == ["reuse freshness: clarity:p5:a:b: a side gave no usable verdict"]
    assert block["clarity"]["compared"] == 5
    assert block["clarity"]["disagreements"] == 0


def test_two_disagreeing_picks_of_two_never_warn():
    block, warnings = freshness_block(clarity_calls([2, 2]), parse)
    assert warnings == []
    assert block["clarity"] == {
        "compared": 2,
        "disagreements": 2,
        "tolerance": None,
        "disagree_rate": 0.4,
        "alpha": CLARITY_ALPHA,
        "source": "runs/2026-08-08",
        "stale": False,
    }


def test_a_verdict_axis_disagreement_still_warns_per_key():
    key = "hedging:check:abc"
    calls = [reused(key, ["certain"], check="hedging"), live(key, ["kept"])]
    block, warnings = freshness_block(calls, parse)
    assert warnings == [f"reuse freshness: {key}: the live verdict differs from the reused one"]
    assert "clarity" not in block
