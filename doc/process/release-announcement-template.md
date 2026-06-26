# Release Announcement Template

Use this template when announcing a new version of this AI-driven SDLC template.

The announcement should help adopters decide whether to upgrade, what will change, and how to validate the upgrade.

## Announcement

### Title

`[Template Release] vX.Y.Z: Short adopter-facing summary`

### Summary

Describe the release in 2-4 sentences.

Include:

- what changed
- who should care
- whether adopters need to take action
- whether the release is patch, minor, or major

### Adopter Impact

| Area | Impact | Action Required |
| --- | --- | --- |
| Minimum contract | None / changed | Yes / no |
| Recommended docs | None / changed | Yes / no |
| Prompts | None / changed | Yes / no |
| GitHub automation | None / changed | Yes / no |
| Release or migration process | None / changed | Yes / no |

### What's Included

- Change 1:
- Change 2:
- Change 3:

### Migration Notes

Use this section if adopters must update files, workflows, prompts, CI, release behavior, or documentation.

- Required migration:
- Optional migration:
- Files likely to conflict:
- Suggested review order:

If no migration is needed, say:

`No adopter migration is required for this release.`

### Validation Evidence

- Contract validation:
- Release dry run:
- Example or adoption rehearsal:
- Known validation gaps:

### Upgrade Path

Recommended adopter path:

1. Read the release notes.
2. Review migration notes.
3. Compare local adopted files with the release tag.
4. Apply changes in small batches.
5. Run contract validation and local repository checks.

Link to `doc/process/adopter-upgrade-path.md` when publishing inside this repository.

### Rollback Or Deferral

Explain whether adopters can safely defer the upgrade.

- Safe to defer:
- Rollback notes:
- Follow-up release expected:

### Maintainer Notes

Optional internal notes:

- Publication owner:
- Announcement channels:
- Follow-up issue or milestone:
- Support window:

## Quality Bar

A good announcement:

- is understandable without reading every commit
- explains downstream impact before internal implementation detail
- links migration guidance when action is required
- names validation evidence
- separates required action from optional adoption
