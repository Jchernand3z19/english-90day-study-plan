# Repository reconciliation — 2026-11-01

**Audited branch:** `main`  
**Baseline audited HEAD:** `097b8d81f363c546cad482793353904a6e7979e5`  
**Subsequent documentation and sync-test changes:** see the latest commits on `main` and the CI runs linked below. The expanded Anki tests and documentation reconciliation have since passed their respective workflows.  
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
| Anki → local Python → GitHub sync | Draft implementation and unit tests committed; not installed or end-to-end tested on the learner's Mac | `integrations/anki-github/README.md`, script, tests, and workflow. Unit tests now cover event flattening, daily aggregate calculations, local-date boundaries, missing IDs, and history merging. CI still does not test a live AnkiConnect session or an actual GitHub upload from the Mac. |
| Google Calendar | Not implemented, configured, or verified | `integrations/google-calendar/README.md`; no Calendar workflow or sync script exists. Proposed study window is not a confirmed schedule. |
| Repository CI | Latest content validation and Anki sync unit-test workflow pass | Content run [41346351700](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346351700) passed after the documentation reconciliation; earlier documentation runs [41346296827](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346296827), [41346082938](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346082938), [41346079230](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346079230), and [41346075860](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346075860) also passed. The expanded Anki sync test workflow [41346644660](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346644660) passed compilation and all 13 unit tests. During test expansion, an import typo was caught by [41346145773](https://github.com/Jchernand3z19/english-90day-study-plan/actions/runs/41346145773), corrected, and followed by a successful run. |
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

### Assistant-side work completed during this reconciliation

- Compared the repository tree, recent commit history, source-of-truth documents, and Actions results.
- Reconciled the README, project status, consolidated review, content-audit log, learning architecture, and Anki mapping date.
- Added this evidence-based reconciliation report and documented which existing commits already contain the work.
- Reviewed the two validation scripts and both workflows, including their limits.
- Reviewed the Anki sync implementation and expanded its pure-function unit tests to cover event flattening, daily aggregates, local-date boundaries, missing review IDs, and historical merge behavior.
- Re-ran the content and Anki workflows; the latest documented runs passed.

### Assistant-side work still open

1. Inspect the remaining curriculum and assessment references for any stale or contradictory instructions not covered by the current status reconciliation.
2. The external URL inventory check is complete for the current retrieval environment: 31 distinct URLs were found; 30 opened successfully and the BBC Learning English URL remained inaccessible, so it is unverified rather than marked broken. This does not certify local audio playback or future availability.
3. Perform a browser/rendered-page review of key GitHub Markdown pages.
4. Build a practical sampling plan for human review of Anki audio and lesson-to-phrase traceability; technical media decoding is not audio-quality review.
5. Continue targeted proofreading only where a concrete issue is identified; do not reopen or rewrite the full curriculum without evidence.
6. Keep Calendar automation deferred until the learner confirms schedule, destination calendar, and notification channel.

### Learner participation required later

1. Finish only the missing Day 1 tasks: the lesson's actual listening activity, remaining supported speaking/self-check, and a genuine audio sample only if pronunciation is to be assessed. Do not repeat the already completed written baseline or the separate external listening diagnostic.
2. After several Anki sessions, report actual review burden and phrase retrieval so the proposed new-card pace can be judged.
3. Participate in a manual AnkiConnect test on the Mac only after code review and explicit approval of the data scope. This is the only step that requires access to the learner's running Anki installation and a securely supplied GitHub token.
4. Confirm Calendar details and authorize any required account connection before Calendar automation is built or tested.

## Preservation rules

- Do not recreate the 90 lessons or repeat completed diagnostics.
- Do not overwrite, replace, or re-import the original or ordered Anki package.
- Do not apply linguistic candidate edits to the deck without explicit approval and a new versioned package.
- Do not mark Day 1 or any other lesson approved without real evidence.
- Do not claim Calendar or local Anki sync is operational until end-to-end tests succeed.
- Keep proposed, implemented, tested, and learner-verified states separate.

