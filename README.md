# Make Claude write clearly, for everyone

This plugin adds a collection of [output styles](https://code.claude.com/docs/en/output-styles) for Claude Code. An output style replaces part of the system prompt of Claude Code, and thus shapes how Claude writes in every turn. This covers both the chat replies of Claude and the material that Claude writes, such as documentation and commit messages. The styles in this plugin aim at output that is clear, simple, and unambiguous, also for non-native readers.

Each style keeps the default coding instructions of Claude Code.

## How to install the plugin

1. Add the marketplace:

   ```
   /plugin marketplace add stefanobaghino/claude-plugins
   ```

2. Install the plugin:

   ```
   /plugin install simple-output-styles
   ```

3. Open `/config`, then select **Output style** and pick a style.

## How to give feedback

Open an issue through the [feedback forms](https://github.com/stefanobaghino/simple-output-styles/issues/new/choose): one form for feedback on an existing style, one for everything else — evals and methodology, documentation, installation, licensing, and requests for new styles. If you have the plugin installed, run `/simple-output-styles:feedback` and Claude gathers the details and prefills the form for you.

## Styles

Each section below describes the spirit of one style, then the advantages and disadvantages that the [evaluation harness](evals/) measured for it. The style texts live in [plugin/output-styles/](plugin/output-styles/).

### actionable-clarity

The style aims at answers a reader understands on first read and can act on at once: the answer first, every needed fact stated outright, and no more certainty than the evidence supports. It combines the organization of plain-language, the directness of developer-docs, and the information-flow principles of clarity-flow, and adds content-preservation and uncertainty rules of its own.

The harness measured three advantages: the model judge ranked it clearest of the styled field across the confirmation campaign, its rewrites preserve checked facts better than any other style in the collection, and its output stays level across long sessions. It also measured four disadvantages: the style writes longer answers than unstyled Claude, and it is the only style in the collection that does; on the held-out prompt set it came second, behind plain-language, within the accepted statistical tie; against baselines whose unstyled answers hedge heavily, it can drop or harden stated uncertainty more than its target allows; and its clarity results rest on the model judge alone, because the human spot check agreed with the judge only half of the time and the maintainer accepted the style by explicit overrule.

#### Sources and disclaimers

The style is a synthesis. It combines principles from the Federal Plain Language Guidelines (public domain), the [Google developer documentation style guide](https://developers.google.com/style) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), and the clarity principles taught in Style: Toward Clarity and Grace, restated in its own words. The affiliation notes and disclaimers of the clarity-flow, developer-docs, and plain-language sections below apply here as well. The wording was tuned against the measurements of the evaluation harness rather than adapted from a single published guide.

### classic-concise

The style pursues classic prescriptive concision, the archetypal "omit needless words" doctrine: make every word tell, and cut the rest.

The harness measured two advantages: it produces the shortest output in the collection, and its rewrites keep checked facts well despite the cuts. It also measured two disadvantages: the model judge places it in the lower half of the field on clarity, and it loses more stated uncertainty than the leading styles.

#### Source and disclaimers

The style adapts the composition principles of The Elements of Style (William Strunk Jr., 1918), a work in the public domain. It restates the principles in its own words and covers only the 1918 text, not the later editions.

### clarity-flow

The style pursues reader-centered clarity grounded in reading psychology: make the actors of a sentence its subjects, put the actions in verbs, and place old information before new.

The harness measured two advantages: it preserves checked facts best among the five reference styles, and it shortens output on average. It also measured three disadvantages: the model judge ranks it mid-field on clarity, behind plain-language and developer-docs; it loses stated uncertainty more than the leaders; and its output length swings widely from one run to the next.

#### Source and disclaimers

The style is an independent adaptation of the clarity principles taught in Style: Toward Clarity and Grace by Joseph M. Williams. It restates the principles in its own words. It does not reproduce the text, the examples, or the exercises of the book. The author and the publisher are not affiliated with this project, and they do not endorse it.

### developer-docs

The style speaks in the modern industry documentation voice: direct, conversational, and written for a global audience.

The harness measured three advantages: it is one of the two clarity leaders among the reference styles, its output length stays close to unstyled Claude, and it preserves checked facts well. It also measured two disadvantages: it drops or hardens stated uncertainty more than plain-language does, because its directness discourages hedging words, and it grows slightly more verbose as a session gets long.

#### Source and disclaimers

The style adapts the [Google developer documentation style guide](https://developers.google.com/style), whose text is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). This project is not affiliated with Google, and Google does not endorse it; the name refers only to the source guide.

### plain-language

The style follows government plain language: familiar words, active voice, short sentences, and the reader addressed directly.

The harness measured four advantages: the model judge ranks it clearest of the five reference styles, it placed first on the held-out prompt set, it shortens output, and it preserves stated uncertainty best in the whole collection. It also measured one disadvantage: its rewrites lose more checked facts than the other leading styles — the drive to shorten cuts details the reader needs.

#### Source and disclaimers

The style adapts the [Federal Plain Language Guidelines](https://digital.gov/guides/plain-language), a work of the United States government in the public domain. This project is not affiliated with the US government.

### technical-simplified

The style applies controlled technical language: a restricted vocabulary, short sentences, and one instruction per sentence, built for procedural documents read worldwide.

The harness measured no advantage for it on conversational work. It measured three disadvantages: it ranks last on clarity, it loses the most checked facts and the most stated uncertainty in the collection, and it grows markedly more verbose as a session gets long. A controlled language built for procedures fits the conversational prompt set poorly; the style stays in the collection for the diversity of its philosophy.

#### Source and disclaimers

The style is an independent adaptation of the writing rules of ASD-STE100 Issue 9. It restates the rules in its own words. It does not reproduce the text, the examples, or the dictionary of the specification.

"ASD-STE100 Simplified Technical English" is a registered trademark of the Aerospace, Security and Defence Industries Association of Europe (ASD). This project uses the name only to refer to the specification. ASD and the STEMG are not affiliated with this project, and they do not endorse or certify this project.

This plugin does not make the output of Claude compliant with ASD-STE100. Download the full specification free of charge from [asd-ste100.org](https://www.asd-ste100.org/).

## License

Two licenses cover this project:

- The Zero-Clause BSD license (0BSD) covers the plugin, the rule files in `evals/rules/`, and every other file outside `evals/`. See [LICENSE](LICENSE). 0BSD requires no attribution notice, so you can copy a style text into your own setup without a license notice.
- The Apache License 2.0 covers the evaluation harness in `evals/`, except the rule files in `evals/rules/`. See [evals/LICENSE](evals/LICENSE).

The rule files stay under 0BSD because a rule file pairs with a style text. A fork of a style needs the matched rule file to measure the fork.

GitHub reads only the root license file, so the repository page shows 0BSD. This section states the full split.
