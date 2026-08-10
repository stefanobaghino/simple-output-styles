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

Each section below describes the spirit of one style, then what testing with the [evaluation harness](evals/) found: what the style does well, and where it falls short. The style texts live in [plugin/output-styles/](plugin/output-styles/).

### actionable-clarity

The style aims at answers a reader understands on first read and can act on at once: the answer first, every needed fact stated outright, and no more certainty than the evidence supports. It combines the organization of plain-language, the directness of developer-docs, and the information-flow principles of clarity-flow, and adds content-preservation and uncertainty rules of its own.

In testing, its answers were the easiest to understand of all the styles, it kept more details than any other style, and its writing stayed steady even in very long sessions. On the downside: its answers run longer than Claude's normal output; on a fresh set of questions it came in a close second behind plain-language; where a careful answer would say "maybe", this style sometimes sounds more certain than it should; and most of its scores come from an AI judge — the one human check agreed with that judge only half of the time.

#### Sources and disclaimers

The style is a synthesis. It combines principles from the Federal Plain Language Guidelines (public domain), the [Google developer documentation style guide](https://developers.google.com/style) ([CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)), and the clarity principles taught in Style: Toward Clarity and Grace, restated in its own words. The affiliation notes and disclaimers of the clarity-flow, developer-docs, and plain-language sections below apply here as well. The wording was tuned against the measurements of the evaluation harness rather than adapted from a single published guide.

### classic-concise

The style pursues classic prescriptive concision, the archetypal "omit needless words" doctrine: make every word tell, and cut the rest.

In testing, it wrote the shortest answers of any style and still kept the details well. But its answers were harder to understand than those of the leading styles, and it sometimes drops the "maybe" from a claim that deserves one.

#### Source and disclaimers

The style adapts the composition principles of The Elements of Style (William Strunk Jr., 1918), a work in the public domain. It restates the principles in its own words and covers only the 1918 text, not the later editions.

### clarity-flow

The style pursues reader-centered clarity grounded in reading psychology: make the actors of a sentence its subjects, put the actions in verbs, and place old information before new.

In testing, it was second only to actionable-clarity at keeping details, and it makes answers shorter on average. But it landed mid-pack on clarity, it sometimes drops the "maybe" from a claim that deserves one, and its answer length varies a lot from one test to the next.

#### Source and disclaimers

The style is an independent adaptation of the clarity principles taught in Style: Toward Clarity and Grace by Joseph M. Williams. It restates the principles in its own words. It does not reproduce the text, the examples, or the exercises of the book. The author and the publisher are not affiliated with this project, and they do not endorse it.

### developer-docs

The style speaks in the modern industry documentation voice: direct, conversational, and written for a global audience.

In testing, it was among the clearest styles, its answers stay about as long as normal, and it keeps details well. But its direct tone sometimes turns a "maybe" into a certainty, and it gets a little wordier as a session drags on.

#### Source and disclaimers

The style adapts the [Google developer documentation style guide](https://developers.google.com/style), whose text is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/). This project is not affiliated with Google, and Google does not endorse it; the name refers only to the source guide.

### plain-language

The style follows government plain language: familiar words, active voice, short sentences, and the reader addressed directly.

In testing, only actionable-clarity read as clearer, and on a fresh set of questions plain-language won outright. It makes answers shorter, and it is the best of all the styles at keeping "maybe" where it belongs. Its one weakness: the push to shorten can cut details you need.

#### Source and disclaimers

The style adapts the [Federal Plain Language Guidelines](https://digital.gov/guides/plain-language), a work of the United States government in the public domain. This project is not affiliated with the US government.

### technical-simplified

The style applies controlled technical language: a restricted vocabulary, short sentences, and one instruction per sentence, built for procedural documents read worldwide.

Testing found nothing it does better than the other styles in everyday conversation: its answers were the hardest to understand, it dropped the most details and the most "maybes", and it got much wordier as a session dragged on. It is built for procedure documents, not chat, and it stays in the collection for that different philosophy.

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
