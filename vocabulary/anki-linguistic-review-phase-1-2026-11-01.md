# Anki linguistic review — first pass (Phase 1) — 2026-11-01

**Scope:** first-pass human review of the 340 Phase 1 manifest entries (English phrase, Spanish equivalent, category/context, and learner-level suitability).
**Source:** the order manifest cross-checked against the original and ordered APKG packages.
**Status:** preliminary editorial review. No card content or APKG was modified.

## Review principle

A translation can be understandable and still be less natural, ambiguous, or mismatched in register. The notes below are candidates for a later correction decision, not automatic proof that a card is wrong. Keep the original package untouched. If corrections are approved, apply them only to a separate working copy, update the manifest, and rerun the package-integrity audit.

## Candidate items to review

| Order | English phrase | Current Spanish | Review note |
|---:|---|---|---|
| 41 | How do you say [palabra] in English? | ¿Cómo se dice [palabra] en inglés? | The placeholder is Spanish inside the English target. Consider using [word] in the English field while retaining [palabra] in Spanish, or explain that the learner substitutes a Spanish word. |
| 54 | I am from [país]. | Soy de [país]. | The placeholder is Spanish inside the English target. Consider [country] in the English field. |
| 126 | Where is the cashier? | ¿Dónde está el cajero? | In Central American Spanish, cajero can mean an ATM or a cashier. Consider ¿Dónde está la caja? or ¿Dónde está el/la cajero/a? depending on intended context. |
| 146 | I’ll have the same. | Comeré lo mismo. | Understandable, but in a restaurant order Voy a pedir lo mismo or Quisiera lo mismo is more natural. |
| 163 | Is service included? | ¿La propina está incluida? | The English can refer to a service charge; the Spanish currently narrows it to a tip. Clarify whether the intended meaning is service charge or gratuity. |
| 174 | I’m hungry as a wolf. | Tengo un hambre de lobo. | The English is idiomatic but less useful as a core beginner chunk than I'm very hungry / I'm starving. Check whether this is a deliberate idiom target or should be moved to a later stage. |
| 214 | You can’t miss it. | No tiene pérdida (no puede no verlo). | The first equivalent No tiene pérdida is natural; the parenthetical literal gloss is awkward and can be removed. |
| 279 | I’m a big fan of... | Soy un gran fan de... | Understandable, but the Spanish is gendered and may sound less natural in some contexts. Consider Me encanta... or Soy muy aficionado/a a... depending on the target structure. |
| 292 | I enjoy gardening. | Disfruto la jardinería. | Understandable but slightly translated. Me gusta la jardinería is more conversational for an early-level learner. |
| 335 | They are old. | Ellos son viejos. | Viejos can sound blunt or pejorative when referring to people. Son mayores is a more neutral alternative when age is intended. |

## Other observations

- The phrase Cheers! appears in two categories with context-specific Spanish translations (toast / UK thanks versus toast). Preserve the duplicate until the intended use is checked; do not deduplicate by wording alone.
- Take it easy appears in two categories with two possible meanings (relax / goodbye). This is a meaningful contextual duplicate, not necessarily an error.
- Some entries contain HTML character references such as Let&#x27;s. These are expected to render as apostrophes in the Anki HTML card; do not replace them blindly without checking the rendered card.
- The Phase 1 set contains useful beginner chunks but also a few idioms, social/personal questions, and imperative expressions. Do not require every Phase 1 card in a beginner conversation. Select only what matches the lesson objective and the learner's readiness.

## What this pass does not certify

- It is not a complete copy-edit of all 340 Phase 1 entries or the 1,000-card deck.
- It does not verify audio pronunciation or naturalness.
- It does not determine the learner's personal answers to generic phrases such as I'm a student, I'm single, or I go to the gym every day. Those are generic language examples, not facts about the learner.
- It does not change the APKG, the CSV manifest, or the learner's imported Anki collection.

## Next steps

1. Resolve or intentionally retain the candidate items above after contextual review.
2. Review Phase 2 and Phase 3 entries with the same standard.
3. Check that the final deck sequence introduces useful language progressively without forcing advanced or irrelevant phrases into early conversation.
4. Only then decide whether to produce a corrected ordered package. Preserve the original and avoid requiring a re-import unless the learner explicitly chooses to replace the current study copy.


## Cross-phase placeholder scan — 2026-11-01

A structural scan of Phase 2 and Phase 3 found two additional Spanish placeholders embedded in English target phrases: order 396, *Hello, this is [nombre] speaking*, and order 398, *Can I speak to [nombre]?*. Consider changing the English-side placeholder to `[name]` in a future corrected copy while retaining `[nombre]` in the Spanish translation. This is a targeted placeholder scan, not a full linguistic review of the 660 Phase 2/3 entries.
