---
name: feedback
description: Guide the user to open a feedback issue for the simple-output-styles plugin. Use when the user wants to report feedback on an output style, the evals, the documentation, the installation, licensing, or wants to request a new style. Gathers the Claude Code version and the active style, then prepares a prefilled GitHub issue link.
disable-model-invocation: true
---

# Provide feedback on simple-output-styles

Help the user open the right issue on the
[simple-output-styles repository](https://github.com/stefanobaghino/simple-output-styles)
with as little typing as possible. You gather the facts; the user reviews a
prefilled form and submits it.

Do not open the issue for the user with `gh` or the API. The repository closes
issues that bypass the forms. Always hand the user a prefilled form link.

## Step 1: pick the form

Ask the user one question: is the feedback about an existing style
(actionable-clarity, clarity-flow, classic-concise, developer-docs,
plain-language, technical-simplified), or about something else (evals and
methodology, documentation, installation, licensing and attribution, a new
style request, or anything else)? Skip the question if the request already
makes the answer clear.

## Step 2a: style feedback

Gather each field, asking the user only for what you cannot find yourself:

1. **Version**: run `claude --version` and use the output.
2. **Styles**: find the active output style: check `outputStyle` in
   `.claude/settings.local.json` and `.claude/settings.json` in the project,
   then `~/.claude/settings.json`. Confirm it with the user, since the
   feedback may be about a style other than the active one. If you find
   nothing and the user does not know, use `I don't know`.
3. **Sentiment**: ask whether the feedback is overall positive, mixed, or
   negative, unless the conversation already makes it obvious.
4. **Feedback**: ask for a short description if the user has not given one.
   If the feedback is about output produced in this conversation, offer to
   include the relevant excerpt.

Build the link (URL-encode every value; join multiple styles with commas):

```
https://github.com/stefanobaghino/simple-output-styles/issues/new?template=style-feedback.yml&styles=<styles>&version=<version>&sentiment=<Positive|Mixed|Negative>&feedback=<text>
```

## Step 2b: general feedback

Ask for the area if it is not clear — one of `Evals and methodology`,
`Documentation`, `Installation`, `New style request`,
`Licensing and attribution`, `Other` — plus the sentiment and a short
description, then build the link (URL-encode every value):

```
https://github.com/stefanobaghino/simple-output-styles/issues/new?template=general-feedback.yml&area=<area>&sentiment=<Positive|Mixed|Negative>&feedback=<text>
```

## Step 3: hand over the link

Show the link and tell the user to open it, review the prefilled fields, and
submit. Mention that dropdowns GitHub fails to prefill (this can happen with
multi-select) must be set by hand before the form submits.
