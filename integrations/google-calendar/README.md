# Google Calendar Integration

This folder documents a possible calendar integration for the study plan.

## Current status

**Not implemented, configured, or verified.** This repository currently has no Calendar workflow or sync script. No automated event creation or reminder delivery is active.

## Proposed behavior (not yet confirmed)

- Proposed study window: 7:00–8:00 p.m. Honduras time, Monday through Saturday.
- Sunday: rest or optional light review.
- Notification channel and destination calendar: not yet selected for this English plan. Email must not be assumed.
- Calendar events should identify the study day and link to the relevant lesson.
- A missed session should remain pending; automation must not mark a lesson approved.

## Before enabling automation

1. Decide which calendar should receive the events.
2. Configure the required credentials in GitHub Actions Secrets, never in a committed file.
3. Grant only the permissions required by the integration.
4. Run a manual test and inspect the workflow result and the calendar event.
5. Confirm timezone handling and duplicate prevention before scheduling recurring updates.

Do not commit service-account JSON, access tokens, private keys, calendar IDs that should remain private, or other secrets. GitHub Actions schedules can be delayed, so the workflow should not promise exact-time delivery.

## Next step

Finish and validate the learning materials and complete the corrected Day 1 pilot first. Then confirm the schedule, destination calendar, and notification channel with the learner; only then implement a dedicated workflow and verify a real event before describing it as operational. Do not reuse another repository's workflow status as evidence for this plan.
