# Migration Notes Template

Use this template when a release requires downstream adopters to take action.

Migration notes are required for major releases and recommended for any minor release that changes adoption expectations, file locations, validation behavior, or workflow conventions.

## Summary

- Release:
- Change:
- Owner:
- Date:
- Related spec, ADR, PR, or issue:

## Who Is Affected

- Adoption levels affected: Level 1 / Level 2 / Level 3
- Repository types affected:
- Maintainers affected:
- Downstream teams affected:

## What Changed

Describe the change in adopter-facing language.

- Previous behavior:
- New behavior:
- Why the change was made:

## Migration Required

- Migration required: Yes / No
- Estimated effort:
- Deadline or recommended timing:
- Compatibility window:

## File Or Workflow Changes

| Old Path Or Workflow | New Path Or Workflow | Required Action |
| --- | --- | --- |
| `<old>` | `<new>` | `<action>` |

## Step-By-Step Migration

1. Step:
2. Step:
3. Step:

## Validation After Migration

Run or confirm:

- [ ] `python3 .github/scripts/validate_template_contract.py`
- [ ] Retained docs and prompts are still listed in the contract manifest
- [ ] Release notes explain adopter impact
- [ ] Local workflow or CI checks still pass
- [ ] Any removed surfaces were removed intentionally

## Rollback Or Compatibility

- Rollback available: Yes / No
- Rollback steps:
- Compatibility notes:
- Known limitations:

## Support And Follow-Up

- Owner:
- Tracking issue:
- Follow-up date:
- Notes:
