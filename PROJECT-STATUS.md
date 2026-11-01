# Project status — English 90-Day Study Plan

**Last updated:** 2026-11-01  
**Repository:** Jchernand3z19/english-90day-study-plan  
**Overall status:** Active; consolidated review of all 90 lessons and all 1,000 Anki text pairs completed; targeted corrections and editorial candidates documented. Day 1 conversational pilot partially completed and recorded; lesson remains in progress. Local Anki → Python → GitHub integration draft added but not installed or end-to-end tested.

## Executive summary

The repository's 90-day curriculum has received targeted progression and workload corrections. The beginner lessons were adjusted to teach and model language before expecting independent production. Phase 2 speaking tasks and its checkpoint were reduced to a more gradual progression. Phase 3 was reviewed for its higher-level objectives and remains conditional on demonstrated readiness. Documentation now distinguishes completed baseline diagnostics, an invalid voice exercise, unmeasured learning outcomes, automated checks, and remaining manual review.

**No daily lesson has been approved yet.** The tracker remains at 0/90. The corrected Day 1 conversational pilot took place on 2026-11-01 and is recorded as partial evidence, not lesson completion. Listening comprehension and pronunciation remain unassessed. The calendar integration is deliberately deferred.

## Current priorities

| Priority | Workstream | Status | Next action |
|---:|---|---|---|
| 1 | 90-lesson content review | Text and curriculum review complete; targeted inconsistencies corrected; automated checks pass | No further text edits block the pilot. External links received a documented spot-check; GitHub-rendered visual review could not be independently retrieved in this environment. |
| 2 | Anki language quality | Phase 1 first-pass review and Phase 2–3 review completed; candidate edits documented | Keep both APKGs unchanged until the learner explicitly approves a new edited copy. |
| 3 | Audio quality | Package integrity and full technical decode passed | Human listening for pronunciation, naturalness, and accent remains unverified; do not claim it passed. |
| 4 | Corrected Day 1 pilot | Partially completed 2026-11-01; not approved | Finish the lesson's listening task, comprehension questions, and final self-check; preserve separate evidence for listening, pronunciation, and text/transcribed production. [Pilot log](daily-logs/day-001-pilot-2026-11-01.md). |
| 5 | Anki workload and transfer | Import reported by learner; real usage not measured | After several sessions, evaluate review burden, recall, and spoken transfer. |
| 6 | Anki → Python → GitHub sync | Draft script, setup guide, unit tests, and CI validation workflow committed; not installed or end-to-end tested | Learner-side AnkiConnect and narrowly scoped GitHub token are required for a manual end-to-end test. No secret or collection data is present in the repo. |
| 7 | Calendar and notifications | Deferred; placeholder documentation only, no calendar workflow or sync script | After the learning workflow is validated, confirm schedule, target calendar, and notification channel before implementing a separate workflow. |
| 8 | Repository validation | Previous content validation passed; new integration files need validation | The new CI workflow now compiles the Python script and runs parser unit tests; inspect its first result, then validate tracker and status links. |

**What requires the learner:** the corrected Day 1 practice and real listening/speaking evidence; later, a report of actual Anki workload; and any Google account authorization or confirmation needed to test Calendar. Lesson editing, Anki text review, documentation, and technical validation are assistant-side work.

## Diagnostic evidence already completed

Do not repeat these as initial diagnostics:

- **Written baseline (2026-10-28):** reading 3/3; grammar/vocabulary 4/5 (80%); one recorded present-simple error (“She doesn't work here”); spontaneous writing and corrections preserved in assessments/initial-written-evidence.md.
- **External listening baseline (2026-10-28):** British Council A1 “Meeting other students”; learner listened twice without transcript. Exact answers and limitations are in assessments/initial-listening-evidence.md. It is limited evidence, not an overall level certification.
- **Spoken introduction (2026-10-28):** two duplicate WAV attachments were submitted; transcript and later text additions are documented in assessments/initial-speaking-text-evidence.md. The two extra ideas were provided in text, not confirmed spoken. No reliable pronunciation/fluency score was assigned.
- **Starting level:** approximately A1/A2 as a working estimate only, not an official CEFR result.

## Voice pilot incident and correction

On 2026-10-29, an improvised job-search dialogue about Alex was used instead of the assigned Day 1 lesson. The task was too difficult and stopped after three items. It is **not** valid Day 1 completion, lesson listening evidence, a diagnostic score, or proof of failure on the actual lesson.

The incident is documented in assessments/voice-pilot-incident-2026-10-29.md. Day 1 was rewritten as a beginner lesson with three personal sentence frames, a short four-sentence listening text, three simple comprehension questions, and supported speaking. The learner completed part of the corrected lesson in a conversational pilot on 2026-11-01: the three core sentence frames were produced correctly in text/transcription. The lesson's listening script and comprehension questions were not completed; pronunciation was not acoustically assessed; the final self-check was not completed. Day 1 is In progress, not approved. See [pilot record](daily-logs/day-001-pilot-2026-11-01.md).

## Curriculum work completed

### Phase 1 — Days 1–30

- Days 1–7 rebuilt or simplified to progress from basic sentence frames and greetings toward a supported short exchange.
- Days 8–13 simplified: smaller phrase-retrieval load; shopping, clothing, café, restaurant, and service requests broken into modelled steps.
- Days 15–20 simplified: directions and transport introduced in short instructions and one-question exchanges rather than multi-step routes and complex role switching.
- Days 22–27 simplified: routines, frequency, interests, and daily activities progress from one or two model sentences toward short connected output.
- Review days 14, 21, and 28 use a smaller, more realistic retrieval load.
- Day 29 checkpoint speaking demand reduced to a supported 20–30 second introduction with sentence frames and thinking pauses.
- The 2026-11-01 consolidated editorial pass reviewed all 90 lesson files for objective/activity alignment, task load, progression, language consistency, timing, listening instructions, and checkpoint demands. It is not a line-by-line certification of every grammar explanation, translation, answer key, or audio recording; those remain subject to targeted proofreading and learner evidence.

### Phase 2 — Days 31–60

- Days 31–36: travel planning, hotel, airport, booking, and directions tasks now begin with one or two modelled requests; longer multi-detail role-plays and role switching are optional extensions.
- Days 38–43: past-event narration builds from one or two past actions toward a short connected story.
- Days 45–50: problem-solving and service requests are broken into one problem/request/solution at a time.
- Days 52–58: social conversation practice uses shorter exchanges and fewer mandatory follow-up questions.
- Day 59 checkpoint and Phase 2 rubric aligned to a 45–60 second story and an approximately two-minute guided conversation with two follow-up questions.
- The consolidated editorial pass also covers Phase 2. Targeted corrections are documented; every individual phrase, answer key, and external resource has not been independently certified.

### Phase 3 — Days 61–90

- Objectives and speaking demands were reviewed across the phase.
- It intentionally introduces opinions, reasons, disagreement, longer conversations, professional communication, networking, interviews, summaries, and repair strategies.
- It is conditional on passing the Phase 2 mastery checkpoint. If prerequisites are not secure, remain in Phase 2 review.
- Some 3–5 minute or extended professional tasks are advanced targets, not a promise of reaching that ability within 90 calendar days.
- The consolidated editorial pass covers Phase 3 as well; earlier targeted corrections and sampled direct reviews remain recorded in assessments/content-audit.md. A complete line-by-line certification of every language item is not claimed.

## Anki status

- Source deck inspected: 1,000 notes/phrases, 1,000 cards, 41 categories, 1,000 audio references, no missing referenced media in the package map.
- A separate ordered copy was prepared: 340 Phase 1, 355 Phase 2, 305 Phase 3 phrases; 13 new cards per active study day is the configured starting pace.
- The learner reports importing the ordered copy and says the initial check looked correct. This is not independent access to the live Anki collection.
- Daily reviews, review burden, recall, and spoken transfer remain unmeasured. Anki is optional and does not replace lesson listening or speaking.
- Do not re-import, overwrite the original, or claim mastery based on a card viewed once.

## Anki progress sync — implementation draft

The local Anki → Python → GitHub script and CI workflow are committed but not installed or end-to-end tested on the learner's Mac. The script exports aggregate review statistics only; it does not upload card text, translations, audio, or raw review events. Unit tests cover event flattening, daily aggregate counts, local-date boundaries, missing review IDs, and historical-day merging. The expanded test workflow passed in [run 41346214358](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346214358). A real manual test still requires AnkiConnect on the Mac and explicit approval of the data scope. See [integration instructions](integrations/anki-github/README.md).

## Calendar and notification plan (deferred)

The English repository currently contains only a placeholder README in integrations/google-calendar/; there is no calendar workflow or sync script, and no event creation or reminder delivery is active. Monday–Saturday, 19:00–20:00 Honduras time is only a proposed study window, not a confirmed calendar configuration. The notification channel and destination calendar have not been confirmed for this English plan. The previously cited failed runs 40702109512 and 40702400684 belong to the separate cyber-data-analyst-study-plan repository; they are not failures of this English repository's calendar integration. After the corrected Day 1 pilot, confirm the calendar details with the learner before implementing and testing a dedicated workflow. A missed session must remain pending; never skip or auto-approve.

## Repository reconciliation — 2026-11-01

A read-only audit of the repository tree, recent commits, documentation, and CI results was recorded in [the repository reconciliation report](assessments/repository-reconciliation-2026-11-01.md). The audit found documentation drift, not missing core curriculum work. It distinguishes completed, implemented-but-not-end-to-end-tested, proposed, and learner-dependent items. No lessons or Anki packages were rebuilt or replaced.

## Repository validation and remaining limits

- GitHub Actions validation checks lesson/tracker coverage, internal relative Markdown links, lesson structure, listening evidence cues, and checkpoint weights.
- The latest verified content validation after the documentation reconciliation is [run 41346351700](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346351700) — success on 2026-11-01 20:02 UTC, against the current audited HEAD. Both checks passed: (1) exactly 90 lesson files, one tracker link per day, and all relative Markdown links; (2) lesson structure, listening-evidence cues, legacy Anki rules, and checkpoint weights. The preceding run failed because `PROJECT-STATUS.md` linked to `learning-data/` before that directory had a README/index. Added `learning-data/README.md` and reran the workflow successfully. The Anki sync workflow [run 41272247896](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41272247896) also passed compilation and unit tests.
- Automated structural checks do not prove that every lesson is pedagogically sound, every translation/answer key is correct, every external link is live, or GitHub renders every page correctly.
- A full rendered-page review and exhaustive external URL check remain open.
- All 90 lesson files and tracker links exist; this is coverage, not quality approval.

## Rules that must remain in force

1. Follow the exact current lesson file; never substitute an improvised dialogue.
2. Ask one question at a time and wait for the learner.
3. Teach and model target language before expecting independent production.
4. Explain difficult points and corrections in Spanish; increase English gradually.
5. Distinguish actual audio listening from reading a transcript. If audio was not heard, mark Not assessed.
6. Do not repeat the completed baseline diagnostics.
7. Do not mark a lesson approved without its required evidence and criteria.
8. A missed lesson remains pending; do not auto-skip or auto-approve.
9. Anki is optional; do not equate card exposure with spoken mastery.
10. Do not activate calendar automation until the corrected learning process has been piloted and accepted.

## Source-of-truth documents

- [README](README.md)
- [Progress tracker](tracker.md)
- [Study method and tutor rules](study-method.md)
- [Content audit and correction log](assessments/content-audit.md)
- [Voice pilot incident](assessments/voice-pilot-incident-2026-10-29.md)
- [Initial written diagnostic](assessments/initial-written-evidence.md)
- [Initial listening diagnostic](assessments/initial-listening-evidence.md)
- [Initial speaking evidence](assessments/initial-speaking-text-evidence.md)
- [Phase assessments](assessments/phase-assessments.md)
- [Anki audit and study order](vocabulary/anki-tracker.md)
- [Daily resource index](resources/daily-resource-index.md)


## Integrated spoken-English architecture — 2026-10-31

A new [integrated learning architecture](learning-architecture.md) defines how the 90-day lessons, Anki, audio, speaking practice, assessments, and tracker must work as one cumulative system. It expands the listening/speaking scope beyond contractions to connected speech, word boundaries, weak forms, reductions, stress, rhythm, intonation, sound contrasts, speech rate, chunking, automatic retrieval, conversational turn-taking, clarification, and repair.

**This is a requirements/design update, not a claim that implementation is complete.** The ordered Anki deck remains unchanged. The existence of 1,000 audio references does not establish that every recording has been checked or mapped to lessons.

### What remains
1. Audit all 90 lesson files against the architecture's per-lesson traceability checklist.
2. Map relevant Anki phrases/cards to lesson objectives and earlier-language retrieval.
3. Sample and quality-check Anki audio and lesson audio for exact phrase match, clarity, accent, naturalness, and level.
4. Identify missing links between listening, pronunciation, guided speaking, and new-context transfer.
5. Make targeted corrections only where evidence shows a gap.
6. Pilot corrected Day 1 and record listening, pronunciation, and spontaneous speaking separately.
7. Update tracking/validation so lesson completion is distinct from phrase/skill mastery.

The Day 1 conversational pilot is partially complete and documented; the required listening and final self-check remain open, so no lesson is approved. Calendar automation remains deferred.
## Conversational design rule — 2026-10-31

The learning method now explicitly distinguishes Anki retrieval from real conversation. Anki phrases are a starting resource, not a vocabulary ceiling or dialogue script. Conversation activities must have a communicative purpose and natural progression, intentionally reuse a small relevant subset of deck phrases, and add the connectors, reactions, follow-up questions, clarification, and context-specific language needed for a coherent exchange.

The tutor must respond to the meaning of the learner's answers rather than mechanically reciting a fixed phrase sequence. New language must remain appropriate to the learner's demonstrated level, be modelled before independent use, and be introduced in manageable amounts. New expressions can be noted as candidates for later Anki inclusion, but should be added only when reusable and nonredundant; do not turn every incidental word into a card.

This is a design requirement added to the architecture and study method. It does not mean all 90 lessons have already been revised or audited for natural conversation. The lesson-by-lesson implementation check remains open.

## Conversational design rule — 2026-10-31

The learning method now distinguishes Anki retrieval from real conversation. Anki phrases are a starting resource, not a vocabulary ceiling or dialogue script. Conversation activities must have a communicative purpose and natural progression, intentionally reuse a small relevant subset of deck phrases, and add the connectors, reactions, follow-up questions, clarification, and context-specific language needed for a coherent exchange.

The tutor must respond to the meaning of the learner's answers rather than mechanically reciting a fixed phrase sequence. New language must remain appropriate to demonstrated ability, be modelled before independent use, and be introduced in manageable amounts. New expressions can be noted as candidates for later Anki inclusion, but should be added only when reusable and nonredundant; do not turn every incidental word into a card.

This is a design requirement added to the architecture and study method. It does not mean all 90 lessons have already been revised or audited for natural conversation. The lesson-by-lesson implementation check remains open.

## Natural conversation audit — 2026-10-31

Opened the core interaction sections of all 90 lesson files to assess progression from controlled phrase practice to natural conversation. The review found that Phases 2 and 3 already contain relevant follow-ups, reactions, clarification, social conversation, professional interaction, and guided free conversation. Phase 1 appropriately starts with short scripted exchanges, but tutor-led practice should add one natural follow-up only when the base exchange is comfortable. Day 17's production task was too demanding for the beginner level (four information questions plus mandatory role switching); it has been corrected to one core bus question, one natural follow-up, and optional extensions. At the time of this 2026-10-31 entry, full line-by-line language/translation/audio/answer-key review remained open. It is superseded by the 2026-11-01 consolidated content review below, which records the completed text review and the remaining limits (human audio quality and visual rendering). See [natural conversation audit](assessments/natural-conversation-audit-2026-10-31.md).

## Anki manifest validation — 2026-10-31

Revalidated the available 1,000-row Anki order manifest: 340 / 355 / 305 phrases across phases, 41 categories, all eight fields populated, unique note IDs, and 1,000 audio references. Ten repeated English phrase pairs across categories/phases were retained rather than deleted automatically. Added [Anki-to-lesson thematic map](vocabulary/anki-lesson-map.md) covering all 41 categories and relevant lesson topics. This is a category-level map, not an exact daily card assignment. The actual recordings have not been quality-reviewed; manifest references do not prove pronunciation/audio quality. Live Anki review burden and spoken transfer remain unmeasured.

## APKG package integrity verification — 2026-11-01

The original and ordered Anki packages were inspected directly. Each has 1,000 notes, 1,000 cards, and 1,000 referenced MP3s, with no missing/orphaned/zero-byte media. All 1,000 MP3 files in both packages have valid readable metadata; a full FFmpeg decode of the ordered package reported no errors. Comparing packages by note ID found identical English phrases, Spanish translations, audio references, filenames, and audio bytes. The ordered copy adds phase tags and unique card due positions 1–1,000. This confirms package integrity, not human listening quality or pronunciation suitability. Day 1's location example is now a placeholder rather than assuming a city, and the Phase 1 outline has been aligned with the actual Day 1 and Day 29 lesson demands. Details: [APKG integrity audit](assessments/anki-package-integrity-audit-2026-11-01.md).

## Remaining independent work

- Review the phrase/translation pairs for linguistic accuracy and level appropriateness; package integrity does not certify translation quality.
- Listen to a representative set of recordings for naturalness, pronunciation, and text/audio match. Automated decoding cannot replace listening.
- Continue exact lesson-to-card selection only where it supports the lesson objective; the current map remains thematic.
- Continue detailed review of lesson answer keys, translations, and pedagogical load beyond the focused audits already documented.
- Day 1 listening/self-check, Anki workload measurement, and Calendar setup still require learner participation or approval.

## Preliminary Anki linguistic review — 2026-11-01

A first-pass review of the 340 Phase 1 cards identified ten candidate entries for context, naturalness, placeholder, or register review. A structural scan of Phase 2/3 also found two Spanish placeholders in English target phrases (orders 396 and 398). These are candidates, not approved corrections; no APKG or manifest content was changed. The first-pass linguistic review now covers all 1,000 text pairs across the three phases; proposed edits are documented separately and no APKG or manifest content was changed. See [preliminary review notes](vocabulary/anki-linguistic-review-phase-1-2026-11-01.md).

## Repository validation — 2026-11-01

The latest GitHub Actions validation after the documentation and Day 1 updates passed both jobs: (1) 90-lesson coverage, tracker links, and internal Markdown links; (2) lesson structure, listening-evidence cues, and checkpoint weights. [Run 41269322359 — success](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41269322359). Earlier failed runs in the same update sequence were caused by commits that referenced the new audit file before that file had been created; the latest run on the final repository state is green.


## Consolidated review — 2026-11-01

- Completed a consolidated review of all 90 daily lesson files, incorporating the earlier direct review of Days 77–90. Targeted inconsistencies in Days 19, 26, 29–30, 40, 42, 52, 54–55, 57, and 71 were corrected. Details: [consolidated content review](assessments/consolidated-content-review-2026-11-01.md).
- Reviewed all 660 Anki text pairs in Phases 2 and 3. Phase 1 has a separate first-pass review. Candidate edits are documented; neither APKG nor the CSV manifest was modified. See [Phase 2–3 linguistic review](vocabulary/anki-linguistic-review-phases-2-3-2026-11-01.md).
- Remaining non-learner work: final rendered Markdown checks and retry the five external pages that timed out; no URL is marked broken solely due to a timeout. Calendar implementation is intentionally deferred until the pilot and confirmation of settings. Human audio-quality review and learner practice cannot be inferred from technical file checks.
- Latest automated repository validation: [run 41270932768](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41270932768) — success; both lesson/tracker/link checks and lesson-quality/checkpoint checks passed. The final run after the current content/resource/Anki-policy edits is [41270932768](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41270932768).


## External resource spot-check — 2026-11-01

A set of core British Council and Cambridge resources loaded and matched their visible title/level/topic. On recheck, “Changing plans” and “Changing a meeting time” loaded; “Transport announcements” and “Showing interest” still timed out but appear in their catalogues. “An invitation to a party” remains unverified and has a title/description mismatch in the A2 catalogue, so the resource index now prioritises the lesson's own dialogue. BBC Learning English blocked automated retrieval, so its availability was not assessed. Details are in assessments/content-audit.md. Automated repository validation does not fetch external URLs.


## Curriculum map alignment — 2026-11-01

The three phase curriculum maps and fixed phase assessment were compared against the daily lesson requirements. Additional mismatches in Phase 1 Days 3, 4, 5, 7, 8, 13, 18, 19, 22, 23, 25, 27; Phase 2 Days 39, 43, 52, 57; and Phase 3 Day 65 were corrected. Day 29's assessment requirement was also aligned with the taught sentence frames. See assessments/consolidated-content-review-2026-11-01.md for details.


## Anki-to-lesson selection policy — 2026-11-01

The category-level Anki map is sufficient for dynamic lesson selection. A fixed card-by-day assignment is intentionally not required, because it could force unrelated phrases into conversations and create a parallel curriculum. During each session, the tutor may select one to three relevant familiar cards from the matching category when useful; conversation can also include natural supporting language outside Anki. No deck file was modified.


## Ready-for-pilot boundary — 2026-11-01 (pre-pilot snapshot)

This section records the state immediately before the learner pilot; the next section supersedes its statement that the pilot is still the next required action.

The assistant-side text, curriculum, Anki text review, resource-index corrections, documentation, and automated structural validation were complete to the level needed to begin the corrected Day 1 pilot. Remaining limits are explicit: the 1,000-card audio has passed technical decoding but not human naturalness/pronunciation review; a few external pages time out in the retrieval environment; and GitHub's rendered HTML could not be independently fetched here. None of these blocks the corrected Day 1 lesson, which uses its own short listening script. The corrected Day 1 pilot subsequently took place partially; see the following section and the dedicated pilot log. Calendar settings and automation remain deferred until after that pilot and confirmation of the schedule, destination calendar, and notification channel.


## Day 1 pilot and integration preparation — 2026-11-01

The learner completed a guided conversational practice covering the three core Day 1 sentence frames plus optional extensions (age, music, walking in the park, and dominoes). The core frames were correct in the visible text/transcription. Some optional language required modelling and correction before the learner reproduced it. This is useful preliminary evidence that short prompts, modelling, and Spanish explanations support participation, but it is not evidence of pronunciation quality or listening comprehension. The tutor also introduced extra questions before completing the lesson's prescribed listening and final self-check; this is recorded as a process deviation to correct. Full details: [Day 1 pilot record](daily-logs/day-001-pilot-2026-11-01.md). Day 1 is **In progress**, not approved.

A first local Anki integration draft has been committed:
- [Integration guide](integrations/anki-github/README.md)
- [Local Python sync script](integrations/anki-github/sync_anki_progress.py)
- [GitHub data destination](learning-data/)

The intended flow is Anki Desktop + AnkiConnect on the learner's Mac → local Python aggregation → GitHub Contents API. The initial export is restricted to aggregate deck counts and daily review statistics; it must not upload card text, translations, audio, notes, or raw review events. The script is a draft and has **not** been executed against the learner's Anki installation. End-to-end validation requires AnkiConnect to be installed/enabled, Anki Desktop to be open, and a narrowly scoped GitHub token supplied securely at runtime. Do not schedule it or claim it is operational until a successful manual sync has been inspected.

### Revised immediate next actions

1. Complete the remaining Day 1 listening task and final self-check in a later learner session; keep pronunciation unassessed unless an actual audio sample can be reviewed.
2. Code review and unit-test coverage for the Python script have been expanded; live AnkiConnect compatibility and safe GitHub update behaviour still require a manual end-to-end test.
3. Run one manual local sync after the learner-side prerequisites are available; inspect the exact JSON written to GitHub.
4. Only after manual validation, decide whether to schedule the local sync with macOS launchd.
5. Keep Calendar deferred; it is separate from Anki sync and requires its own explicit settings and authorization.
