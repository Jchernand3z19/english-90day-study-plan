# Repository reconciliation — 2026-11-01

**Audited branch:** `main`  
**Audited HEAD:** `097b8d81f363c546cad482793353904a6e7979e5`  
**Method:** read-only inspection of repository tree, current documentation, recent commit history, and GitHub Actions results. This report records the state at the audited HEAD; it does not replace earlier audit logs.

## Executive result

The existing curriculum, assessment records, Anki audits, integration draft, and validation scripts are present. The recent work is not missing: the commit history shows the Day 1 pilot record, Anki sync draft, unit tests, workflow, privacy README, and final status updates already committed.

The main problem found was **documentation drift**, not missing curriculum work. Some status statements were older than the evidence already recorded elsewhere. The corrections in this reconciliation update those statements without rebuilding lessons or changing either Anki package.

## Status by workstream

| Workstream | Reconciled status | Evidence / boundary |
|---|---|---|
| 90 daily lesson files | Present; editorial review and targeted corrections are documented | `assessments/consolidated-content-review-2026-11-01.md`, `assessments/content-audit.md`; existence and structure are also checked by CI. This does not certify every sentence, answer, external URL, or classroom outcome. |
| Curriculum maps and phase assessments | Present; targeted alignment corrections are documented | Consolidated review, phase curriculum files, and `assessments/phase-assessments.md`. |
| Initial learner diagnostic | Completed and preserved; do not repeat the completed baseline tasks | `assessments/initial-written-evidence.md`, `assessments/initial-listening-evidence.md`, `assessments/initial-speaking-text-evidence.md`. |
| Day 1 pilot | Partially completed on 2026-11-01; not approved | `daily-logs/day-001-pilot-2026-11-01.md`. Listening comprehension and pronunciation were not assessed; supported speaking and final self-check still need completion. |
| Original and ordered Anki decks | Preserved; no card/package edits in the repository review | `assessments/anki-package-integrity-audit-2026-11-01.md` and `vocabulary/anki-tracker.md`. The learner reported importing the ordered copy; live collection state is not independently accessible here. |
| Anki linguistic review | Candidate corrections documented, not applied to APKG/CSV | Phase 1 and Phase 2–3 linguistic review files. Any deck revision must be a new version after approval; never overwrite the original. |
| Anki-to-lesson mapping | Thematic map and dynamic-selection policy exist; exact per-card audio/lesson traceability is not complete | `vocabulary/anki-lesson-map.md`, `learning-architecture.md`. No fixed card-per-day assignment is intended. |
| Anki → local Python → GitHub sync | Draft implementation and unit tests committed; not installed or end-to-end tested on the learner's Mac | `integrations/anki-github/README.md`, script, tests, and workflow. CI tests compilation/unit behavior only, not AnkiConnect or an actual GitHub upload from the Mac. |
| Google Calendar | Not implemented, configured, or verified | `integrations/google-calendar/README.md`; no Calendar workflow or sync script exists. Proposed study window is not a confirmed schedule. |
| Repository CI | Latest content validation and Anki sync unit-test workflow pass | Content run [41344766693](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41344766693); Anki sync run [41272247896](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41272247896). |
| Rendered Markdown / external links | Still requires browser-level verification | Current CI checks relative internal links and structural rules, not every external destination or rendered page. |

## Recent history confirms the work is already committed

The inspected history includes these commits on `main`:

- `786f394` and `94399ad`: record the Day 1 pilot evidence and its in-progress status.
- `052c894`, `7af9aea`, `f5077c3`, `cdd2d66`: document and implement the Anki sync draft, data destination, and safer review-history parsing.
- `69a5e09` and `165f51b`: add unit tests and CI validation for the Anki sync.
- `4dbc785`: reinforce lesson-sequence and evidence rules after the pilot.
- `0324338`: document the purpose and privacy of the learning-data directory.
- `097b8d8`: update the project status after the latest repository validation.

These are existing commits, not tasks to redo.

## Documentation drift identified and corrected in this reconciliation

1. The README described the corrected Day 1 as simply pending, without noting the partial pilot on 2026-11-01.
2. The consolidated review still said the corrected pilot had not yet been completed, although a partial pilot record existed.
3. The consolidated review listed the automated validation as still pending, although the validation had passed.
4. `PROJECT-STATUS.md` cited run 41344730250 as latest, while a later successful run 41344766693 existed for the current HEAD.

The reconciled wording now distinguishes a **partial pilot** from a **completed/approved lesson**, and a successful automated check from the checks that remain outside CI.

## Remaining work — in order

### Assistant-side work; no learner action needed yet

1. Continue reconciling status documents and source-of-truth links against actual files and commits.
2. Inspect all lesson and assessment references for stale instructions or duplicated/conflicting rules; make only evidence-backed documentation corrections.
3. Review the validator and workflow coverage, including what is and is not tested.
4. Review the Anki sync script, tests, and data-minimisation behavior; improve only defects confirmed by code inspection.
5. Review the lesson-resource index and external links; record which destinations were actually opened and checked.
6. Review lesson/audio/Anki traceability and identify a manageable sampling method for human audio-quality checks.
7. After these checks, run CI again and update the project status with the exact run IDs.

### Learner participation required later

1. Finish only the missing Day 1 tasks: the lesson's actual listening activity, remaining supported speaking/self-check, and a genuine audio sample only if pronunciation is to be assessed. Do not repeat the already completed written baseline or the separate external listening diagnostic.
2. After several Anki sessions, report actual review burden and phrase retrieval so the proposed new-card pace can be judged.
3. Participate in a manual AnkiConnect test on the Mac only after code review and explicit approval of the data scope.
4. Confirm calendar details and authorize any required account connection before Calendar automation is built or tested.

## Preservation rules

- Do not recreate the 90 lessons or repeat completed diagnostics.
- Do not overwrite, replace, or re-import the original or ordered Anki package.
- Do not apply linguistic candidate edits to the deck without explicit approval and a new versioned package.
- Do not mark Day 1 or any other lesson approved without real evidence.
- Do not claim Calendar or local Anki sync is operational until end-to-end tests succeed.
- Keep proposed, implemented, tested, and learner-verified states separate.

