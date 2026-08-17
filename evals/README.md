# Evaluation harness

This directory holds the evaluation harness for the output styles in
`plugin/output-styles/`: the tooling that measures each style against
an unstyled baseline and stores the evidence in `runs/`. This file is
the entry point; the [Documentation](#documentation) section maps the
full set.

## What the harness measures

Per prompt, the harness produces one answer per style and one shared
unstyled answer through the Claude Code CLI, and scores what each
style changes:

- **Fidelity** — whether an answer follows the writing rules of its
  style. A deterministic linter counts violations, and a gate marks
  each pair pass or fail, because a non-compliant answer does not
  represent its style.
- **Token cost** — the fixed input overhead of the style block and
  the styled-to-unstyled answer-length ratio.
- **Reader value** — whether a reader gains anything, through
  comprehension, paraphrase, and translation round-trip checks.
- **Content loss** — the facts that survive the styled rewrite, the
  facts only the rewrite states, and the hedged claims that survive,
  harden, or drop.
- **Clarity ranking** — blind head-to-head contests, fitted to one
  Bradley-Terry strength per style.
- **Drift** — whether rule obedience degrades across long sessions,
  including sessions driven into deep context.

Supporting machinery runs the measurements at scale: a campaign
driver, a cross-run comparison (the error bar of the harness), a
regression-targets check, a second-judge agreement sample, and a
provisioning tool for the pinned CLI binary.
[ARCHITECTURE.md](ARCHITECTURE.md) describes every component.

The harness stays outside `plugin/` on purpose: the marketplace
serves only the `plugin/` directory, so installers never receive the
harness.

## Quick start

The harness uses [uv](https://docs.astral.sh/uv/). Run every command
from this directory. The live tools call the Claude Code CLI on the
account of the person who runs them; the
[prerequisites](OPERATIONS.md#prerequisites) describe the credential
routes and the billing.

The command index:

```
uv run pytest
uv run style-lint FILE.md --rules rules/technical-simplified.rules.yaml
uv run style-pairs [--parallel N] [--screening] [--holdout] [--reuse-from RUN] [--accept-cli-version]
uv run style-gate runs/<date>
uv run style-cost runs/<date> [--probe] [--repeats N] [--reuse-from RUN] [--accept-cli-version]
uv run style-value runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
uv run style-loss runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
uv run style-rank runs/<date> [--judge] [--parallel N] [--reuse-from RUN] [--accept-cli-version]
uv run style-agreement runs/<date> [--judge] [--model M] [--sample N] [--parallel N] [--accept-cli-version]
uv run style-provision [--status]
uv run style-campaign [--runs N] [--budget W] [--probe-repeats N] [--screening] [--holdout] [--reuse-from RUN] [--accept-cli-version]
uv run style-drift [--generate] [--scripts prompts/sessions/*.yaml] [--estimate] [--context-window N] [--depth-target F] [--out runs/<date>-drift] [--accept-cli-version]
uv run style-compare runs/<a> runs/<b> [...] [--out runs/<date>-compare]
uv run style-targets runs/<date> [--targets rules/targets.yaml] [--drift runs/<date>-drift]
```

To produce a full measurement campaign:

1. Provision the pinned CLI binary: `uv run style-provision`.
2. Run the campaign: `uv run style-campaign`. Three full runs land
   under `runs/`.
3. Compare the runs: `uv run style-compare runs/<a> runs/<b> runs/<c>`.
4. Check the regression targets: `uv run style-targets runs/<a>`.

Every stage exits 0 when it is clean; exit 1 means failures or
warnings recorded in the reports, and exit 2 means the tool could
not run. The flags, behaviors, and per-tool exit codes live in the
[tool reference](OPERATIONS.md#tool-reference).

## Documentation

| Document | Read it for |
|---|---|
| [ARCHITECTURE.md](ARCHITECTURE.md) | How the harness is built and why: the components, the measurement pipeline, hermetic isolation, pins and comparability eras, campaign scheduling |
| [OPERATIONS.md](OPERATIONS.md) | How to run and read every tool: flags, behaviors, exit codes, reuse across runs, and the run-data tree |
| [CONTRIBUTING.md](CONTRIBUTING.md) | The procedures: how to add a style, how to add a prompt, the screening threshold, the human spot check protocol, pin updates, and the documentation ownership map |
| [RESULTS.md](RESULTS.md) | The latest measured findings per style, with the numbers and their caveats |
| [Top-level README](../README.md) | The user-facing plugin guide and the styles at a glance |

## License

The Apache License 2.0 covers this directory. See [LICENSE](LICENSE). One
exception exists: the Zero-Clause BSD license of the repository root covers
the rule files in `rules/`, because a rule file pairs with a style text, and
a fork of a style needs the matched rule file. The License section of the
top-level `README.md` states the full split.

## Keep this document current

This file owns the quick start and the documentation map; a change
to either updates it in the same PR. The ownership map of the whole
documentation set lives in
[CONTRIBUTING.md](CONTRIBUTING.md#keep-the-documentation-current).
