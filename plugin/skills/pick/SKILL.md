---
name: pick
description: Help the user pick an output style from the simple-output-styles plugin and set it globally. Recommends actionable-clarity, or walks through the full list with the pros and cons of each style.
disable-model-invocation: true
---

# Pick an output style

Get the user from a fresh install to an active style with one decision. You
recommend a style, the user picks, and you set the choice in their global
settings.

## Step 1: recommend actionable-clarity

Open with the recommendation: **actionable-clarity**. In testing it wrote the
answers that were easiest to understand, it kept more details than any other
style, and it says "maybe" when a claim is unsure. Its one trade-off: answers
run a little longer than Claude's normal output.

Ask the user one question: go with the recommendation, or see the other
options? If the user already named a style, skip to step 3.

## Step 2: the full list (only when asked)

Present the six styles, each with one line of spirit and its main pro and con
in plain words:

- **actionable-clarity** (recommended) — answer first, every detail kept,
  honest about uncertainty. Clearest in testing; answers run a little longer.
- **plain-language** — familiar words, short sentences, reader first. Nearly
  as clear, with shorter answers and the best care for "maybe"; can cut
  details you need.
- **developer-docs** — the direct, conversational documentation voice. Clear,
  with answers about normal length; can sound more certain than it should.
- **clarity-flow** — reader-centered sentence craft: actors as subjects,
  actions as verbs. Keeps details very well and shortens answers; mid-pack on
  clarity.
- **classic-concise** — omit needless words. The shortest answers of any
  style; less clear than the leaders, and sometimes drops a "maybe".
- **technical-simplified** — controlled language built for procedure
  documents. In everyday chat it tested hardest to understand and dropped the
  most details; pick it only if you want that philosophy.

Let the user pick one, or none — stopping without a style is a fine outcome.

## Step 3: set the style globally

1. Read `~/.claude/settings.json`. If the file does not exist, create it with
   an empty object first.
2. If `outputStyle` is already set to another style, tell the user what is
   active and confirm the replacement before you write.
3. Set `outputStyle` to the chosen style, in the plugin-qualified form that
   `/config` writes, for example
   `"outputStyle": "simple-output-styles:actionable-clarity"`. Change only
   that key and keep every other setting as it is.
4. Check that the file is still valid JSON after the edit.

If the user asks for the style in this project only, write the same key to
`.claude/settings.local.json` in the project instead.

## Step 4: tell the user how to apply it

The output style is part of the system prompt, which Claude Code reads once
at session start. Tell the user the style takes effect after `/clear` or in
the next session, and name the style you set.
