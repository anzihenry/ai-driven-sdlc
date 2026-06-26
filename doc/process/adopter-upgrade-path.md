# Adopter Upgrade Path

Use this guide when a downstream repository wants to upgrade from one version of this template to another.

Template upgrades should be reviewed like product changes because they may affect process, prompts, automation, release behavior, or documentation contracts.

## Before You Upgrade

Record the current state:

- current adopted template version or source commit
- target template version or tag
- adoption level: Level 1, Level 2, or Level 3
- files copied from the template
- files intentionally replaced with local equivalents
- retained GitHub automation
- known local deviations from the template contract

If the current adopted version is unknown, treat the upgrade as a manual sync and review changes more carefully.

## Choose An Upgrade Strategy

| Strategy | Use When | Review Focus |
| --- | --- | --- |
| Direct tag comparison | Current and target tags are known | Template diff, migration notes, contract changes |
| Manual file sync | Existing repository copied selected files | File-by-file intent and local conflicts |
| Fork merge | Repository is an upstream fork | Merge conflicts, local workflow preservation |
| Fresh adoption review | Current template lineage is unclear | Re-run quickstart, decision tree, and customization checklist |

## Upgrade Steps

1. Read the target release notes.
2. Read migration notes if the release includes adopter-facing changes.
3. Compare current adopted files with the target template version.
4. Identify contract changes:
   - Level 1 files added, renamed, or removed
   - Level 2 recommended files added, renamed, or removed
   - Level 3 automation changes
   - optional files that became required or required files that became optional
5. Apply changes in small reviewable batches.
6. Preserve local project decisions unless the upgrade intentionally changes them.
7. Run the contract validator.
8. Run stack-specific checks owned by the adopting repository.
9. Update local adoption notes with the new template version and deviations.

## Conflict Handling

When template changes conflict with local repository choices:

- keep local project identity over template defaults
- keep local stack-specific CI over generic CI suggestions
- prefer equivalent local processes when they satisfy the same contract intent
- document rejected template changes when they affect future upgrades
- create an ADR if the conflict changes team workflow, release policy, or review expectations

## Validation

Minimum validation:

```sh
python3 .github/scripts/validate_template_contract.py
```

Also run adopter-owned validation, such as:

- documentation link checks
- lint, test, or build commands
- release workflow dry run
- prompt trial on a small real task

## Rollback

Rollback should be possible if the upgrade disrupts adoption.

Before merging the upgrade:

- keep the pre-upgrade branch or commit
- note which files changed
- identify which changes are safe to revert independently
- document any manual edits that would need to be undone

## Upgrade Complete When

The upgrade is complete when:

- target template version is recorded
- migration notes have been applied or explicitly waived
- contract validation passes or deviations are documented
- adopter-specific checks pass
- retained automation still matches the team's workflow
- reviewers understand any changed prompts, docs, or release process
