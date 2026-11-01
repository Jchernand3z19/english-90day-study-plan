# Anki — Existing Deck Audit and Study Order

**Status:** Inspected and reorganized copy prepared on 2026-10-29. The original file is preserved; the ordered package is a separate output. No learner review history or mastery is claimed.

## Inspected deck

| Metric | Result |
|---|---:|
| Notes / phrases | 1,000 |
| Cards | 1,000 |
| Categories | 41 |
| Audio references | 1,000 |
| Missing referenced audio files | 0 |
| Review history in source deck | 0 entries |
| Phrase groups with repeated normalized wording | 10; retained for context review |

All source cards were new and unscheduled at inspection. The audit confirms that the deck has audio references for every phrase and that each referenced audio filename exists in the package media map. This does not assess pronunciation quality or certify that every English phrase/Spanish translation is ideal.

## Ordered study copy

A separate copy was reorganized to follow the broad progression of the 90-day plan. Original phrases, translations, category fields, audio, and card template were preserved. Existing tags were retained and a phase tag was added to each note.

| Phase tag | Phrase count | Focus |
|---|---:|---|
| `plan_fase_01_fundamentos` | 340 | Greetings, personal information, clarification, daily needs, and familiar situations |
| `plan_fase_02_comunicacion_practica` | 355 | Travel, work, health, past events, plans, documents, and practical communication |
| `plan_fase_03_opiniones_y_matices` | 305 | Opinions, uncertainty, discussion, phrasal verbs, idioms, and nuanced conversation |

Cards are positioned sequentially by phase and category, preserving the original order within each category. The study copy is configured for **13 new phrases per active study day**; with one weekly rest/review day, this is a planning pace rather than a guarantee of mastery or completion. Reviews may increase daily workload.

## Files prepared

- Ordered deck: `1000_frases_ingles_ordenado_90_dias.apkg` (created as a separate download; the learner reports importing it and says the initial check looks correct).
- Order manifest: `guia_orden_anki_90_dias.csv`, with position, phase, category, English phrase, Spanish translation, and audio reference.
- Audit report: `auditoria_anki_1000_frases.md`.

## Mastery tracking

Do not mark a phrase as mastered simply because it was answered correctly once in Anki. Count it as mastered only when the learner can:

1. Understand it without translating every word individually.
2. Recall or produce it without seeing the answer.
3. Use it in a new, appropriate spoken sentence or short dialogue.
4. Retrieve it again during a later review.

| Date | Cards reviewed | New cards | Phrases recalled | Phrases used in speech | Notes |
|---|---:|---:|---:|---:|---|
| 2026-10-29 | Not measured | Not measured | Not measured | Not measured | Learner reports importing the ordered deck and says it appears correct; workload and review outcomes not yet measured |

## Remaining decisions

- **Import status:** the learner reports that the ordered copy is imported and appears to work; this is an initial user-reported check, not an independent verification of the Anki collection.
- After several study sessions, review the new-card pace and accumulated reviews; adjust if the workload feels too heavy.
- Duplicate wording was not automatically deleted because repeated phrases may have different translations or contexts.
- No reverse Spanish-to-English card type was added, to avoid doubling the card count before the workload is piloted.
- This is a thematic phase mapping, not a claim that each card is assigned to an exact lesson/day or that the learner has mastered any phrase.

## Manifest validation and thematic lesson map — 2026-10-31

Re-read the available `guia_orden_anki_90_dias.csv` manifest programmatically. It contains 1,000 records, with 340 / 355 / 305 phrases across the three phase tags and 41 categories. All eight columns are populated; note IDs are unique; 1,000 audio references are listed. Ten English phrase pairs (20 rows) repeat across different categories/phases and remain intentionally preserved pending context review. This verifies the CSV manifest, not the live Anki collection or the audio content/quality. Created [Anki-to-lesson thematic map](anki-lesson-map.md), which associates every category with relevant lesson topics. It is thematic, not an exact card-per-day assignment. Audio listening/quality review and exact card-to-lesson selection remain open.

## Full APKG package integrity check — 2026-11-01

Both the preserved original package and the separate ordered package were available and inspected directly. Each contains 1,000 notes, 1,000 cards, and 1,000 MP3 media files; every note has one audio reference, all references resolve, and there are no orphaned media files or zero-byte assets. All 1,000 MP3s in each package have readable metadata (24 kHz, 48 kbps; durations 0.912–3.096 seconds), and the ordered package's 1,000 media files decoded in a full FFmpeg pass with no reported errors. Comparing original and ordered packages by note ID found no changes to English phrase, Spanish translation, or audio reference; all audio filenames and binary contents match. The ordered package adds the phase tags and places the 1,000 cards in unique due positions 1–1,000, one card per note. This verifies package structure and technical audio integrity, **not** whether the recordings sound natural, are correctly pronounced, or are pedagogically appropriate; human listening review remains open. See [full technical audit](../assessments/anki-package-integrity-audit-2026-11-01.md).

## Preliminary linguistic review — 2026-11-01

Completed a first-pass review of the 340 Phase 1 phrases and a structural placeholder scan of the other phases. Ten Phase 1 entries are recorded as candidates for editorial review; no APKG or manifest fields were changed. The cross-phase scan also identified Spanish placeholders in English target phrases at orders 396 and 398. This is not a full linguistic audit of the 1,000 cards. See [preliminary Anki linguistic review](anki-linguistic-review-phase-1-2026-11-01.md).
