# Anki package integrity audit — 2026-11-01

**Scope:** direct inspection of the original Anki package, the separate ordered package, and the 1,000-row order manifest.  
**Purpose:** verify that the ordered copy preserves source learning content and that card/audio references are technically intact.  
**Result:** package integrity checks passed. This is not a linguistic or human listening-quality certification.

## Package inventory

| Check | Original package | Ordered package |
|---|---:|---:|
| Notes | 1,000 | 1,000 |
| Cards | 1,000 | 1,000 |
| MP3 media files | 1,000 | 1,000 |
| Audio references in notes | 1,000 | 1,000 |
| Missing referenced media | 0 | 0 |
| Orphan media files | 0 | 0 |
| Zero-byte media files | 0 | 0 |
| MP3 metadata readable | 1,000 | 1,000 |
| MP3 metadata errors | 0 | 0 |

All audio files report MP3, 24 kHz, 48 kbps, with durations from 0.912 to 3.096 seconds. A full FFmpeg decode pass over all 1,000 files in the ordered package completed with exit code 0 and no reported decoding errors.

## Original-versus-ordered comparison

The comparison used each note's stable note ID:

- The 1,000 note IDs match between packages.
- English phrase, Spanish translation, and audio-reference fields match for every note (0 mismatches).
- All 1,000 media filenames match.
- All 1,000 audio binaries match byte-for-byte (SHA-256 comparison).
- The ordered package adds the intended phase tag to every note.
- The ordered package contains one card per note, all in one deck, with unique due positions 1–1,000.

The ordered copy therefore preserves the original phrase, translation, and audio assets. The original package remains separate and unchanged.

## Manifest-to-package check

The CSV order manifest was cross-checked against the ordered APKG using note IDs. All 1,000 manifest rows resolve to a package note, and English phrase, Spanish translation, and audio reference match exactly. No row-level mismatches were found.

The package retains the existing 340 / 355 / 305 phase distribution and 41 thematic categories. The card sequence is ordered by the intended phase/category progression. The current lesson association remains thematic; it is not a one-card-per-day assignment.

## What the technical checks do not prove

- The recordings have not been listened to by a human reviewer as part of this audit.
- Successful decoding and readable metadata do not establish natural pronunciation, intelligibility, accent consistency, appropriate intonation, or suitability for beginner shadowing.
- The audit does not certify that every Spanish translation is the best contextual equivalent or that every phrase belongs at its assigned CEFR stage.
- It does not verify the user's live Anki collection, review history, retention, or actual daily workload.

## Next independent quality work

1. Conduct a human listening review of a representative, phase-stratified sample, checking text/audio correspondence, clarity, pronunciation, and naturalness.
2. Review phrase/translation pairs for context, register, ambiguity, and beginner suitability; preserve intentional contextual duplicates unless a clear error is found.
3. Keep the original APKG unchanged. Any future edits must be made to a separate working copy and revalidated against the manifest.
4. Measure the learner's actual new-card and review burden only after a real study pilot; do not assume 13 new cards per day is sustainable.

## Reproducibility

The audit used the original APKG, ordered APKG, and `guia_orden_anki_90_dias.csv` available in the conversation's attached files. Package internals were inspected using SQLite/ZIP, audio metadata using Mutagen, binary comparison using SHA-256, and full media decoding using FFmpeg. No edits were made to either APKG.
