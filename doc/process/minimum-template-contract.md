# Minimum Template Contract

This document defines the smallest supported shape of this repository when it is adopted by a downstream team.

Its purpose is to answer four questions clearly:

- Which files should normally be kept
- Which files must be customized during adoption
- Which files are optional extensions
- What checks should be run before adoption is considered complete

The machine-readable source of truth for CI is `.github/template-contract.json`. CI validates that the adoption levels in this document stay synchronized with that manifest.

## Contract Principles

- Keep the minimum contract small enough for real teams to adopt
- Protect the files that define the repository's core AI-assisted workflow
- Allow downstream teams to adapt structure, stack, and automation without breaking the template's intent
- Treat optional files as accelerators, not hidden requirements

## Adoption Levels

### Level 1: Minimum Supported Adoption

This is the smallest shape that still counts as adopting this template in a meaningful way.

Teams at this level should keep:

- `README.md`
- `CONTRIBUTING.md`
- `doc/README.md`
- `doc/specs/project-brief.md`
- `doc/specs/feature-spec-template.md`
- `doc/decisions/ADR-template.md`
- `doc/process/ai-workflow.md`
- `doc/process/delivery-checklist.md`
- `prompts/feature-implementation.md`
- `prompts/code-review.md`

Teams at this level may simplify or replace:

- `.github/` automation files
- `src/README.md`
- release automation and release-drafting configuration
- label synchronization and auto-labeling rules

### Level 2: Recommended Team Adoption

This level keeps the minimum workflow surface and also preserves repository governance defaults.

Teams at this level should keep everything in Level 1, plus:

- `.github/PULL_REQUEST_TEMPLATE.md`
- `.github/ISSUE_TEMPLATE/bug_report.md`
- `.github/ISSUE_TEMPLATE/feature_request.md`
- `.github/ISSUE_TEMPLATE/task_request.md`
- `.github/dependabot.yml`
- `.github/labeler.yml`
- `.github/labels.json`
- `doc/examples/good-feature-spec.md`
- `doc/examples/good-implementation-request.md`
- `doc/examples/good-review-request.md`
- `doc/examples/README.md`
- `doc/examples/template-repository-adoption.md`
- `doc/examples/template-repository-validation-notes.md`
- `doc/process/ai-delivery-operating-guide.md`
- `doc/process/ai-failure-modes.md`
- `doc/process/adoption-walkthrough.md`
- `doc/process/multi-stack-adoption.md`
- `doc/process/migration-notes-template.md`
- `doc/process/rollout-notes-template.md`
- `doc/process/retrospective-learning-notes-template.md`
- `doc/process/versioning-and-releases.md`
- `doc/process/release-checklist.md`
- `doc/process/release-dry-run.md`
- `prompts/README.md`
- `prompts/planning.md`
- `prompts/acceptance-qa.md`

This level is the default recommendation for teams that want repeatable review and release habits.

### Level 3: Full Template Adoption

This level keeps the full repository governance surface, including release and label automation.

Teams at this level should keep everything in Level 2, plus:

- `.github/release-drafter.yml`
- `.github/workflows/ci.yml`
- `.github/workflows/labeler.yml`
- `.github/workflows/release-drafter.yml`
- `.github/workflows/release.yml`
- `.github/workflows/sync-labels.yml`
- `.github/README.md`
- `.github/CODEOWNERS`
- `src/README.md`

Teams can still customize behavior heavily at this level, but they should preserve the intent of the template surfaces they keep.

## Files That Must Be Customized During Adoption

The following files should not usually stay unchanged after real adoption:

- `README.md`
- `CONTRIBUTING.md`
- `doc/specs/project-brief.md`
- `.github/CODEOWNERS` if the repository uses CODEOWNERS
- `.github/ISSUE_TEMPLATE/config.yml` if the repository uses contact links
- `src/README.md` if the downstream team wants stack-specific guidance

These files are adopter-facing and should reflect the actual team, workflow, and repository structure.

## Files That May Be Removed If Unused

The following files can be removed if the downstream team is not adopting the related workflow:

- `.github/release-drafter.yml`
- `.github/workflows/release-drafter.yml`
- `.github/workflows/release.yml`
- `.github/workflows/sync-labels.yml`
- `.github/dependabot.yml`
- `.github/labeler.yml`
- `.github/labels.json`
- `.github/ISSUE_TEMPLATE/*`

Before removing them, the adopting team should decide whether the capability is intentionally excluded or just temporarily deferred.

## Files That Should Rarely Be Removed

The following files are part of the template's core identity and should usually stay in some equivalent form:

- `README.md`
- `CONTRIBUTING.md`
- `doc/specs/project-brief.md`
- `doc/specs/feature-spec-template.md`
- `doc/decisions/ADR-template.md`
- `doc/process/ai-workflow.md`
- `doc/process/delivery-checklist.md`
- `prompts/feature-implementation.md`
- `prompts/code-review.md`

Teams may rewrite these heavily, but removing all of them usually means the repository is no longer using this template in a meaningful way.

## `src/` Contract

This template does not require one canonical source-code layout.

Downstream teams may choose any of these approaches:

1. Keep `src/` as the main source root
2. Use `src/` for examples or conventions only
3. Remove practical use of `src/` and replace its guidance during adoption

What matters is that the chosen approach is documented clearly in `README.md` and, if relevant, `src/README.md`.

## Contract Validator For Adopters

If this repository is copied with `.github/scripts/validate_template_contract.py`, run:

```sh
python3 .github/scripts/validate_template_contract.py
```

The validator checks repository hygiene, required template files, adoption-level sync, example references, and optional surfaces that are present.

For adopters, validation results should be interpreted this way:

| Result | Meaning | Adopter Action |
| --- | --- | --- |
| Pass | The copied template surface is internally consistent. | Continue adoption and record validation evidence. |
| Missing Level 1 file | The minimum AI-assisted workflow may be incomplete. | Restore the file or document the equivalent replacement. |
| Level list mismatch | Human docs and machine contract disagree. | Update this document and `.github/template-contract.json` together. |
| Optional file present but empty | A retained optional surface exists but is not usable. | Fill it in or remove it intentionally. |
| Forbidden path found | Repository hygiene failed. | Remove the forbidden file before review or release. |

Validation does not decide whether the template is a good fit for the project. It only confirms that retained template surfaces are coherent.

If an adopter intentionally removes or replaces a contract file, the decision should be recorded in the adopting repository's README, adoption PR, or equivalent planning artifact.

## Adoption Completion Checklist

A downstream team should not consider adoption complete until:

- repository ownership and contact placeholders are removed or replaced
- the project brief reflects the real project
- contributor guidance reflects the real team workflow
- at least one feature spec exists or is ready to be written with the provided template
- prompt templates are still usable in the repository's actual workflow
- any retained GitHub automation matches the team's actual process
- any removed template surface was removed intentionally, not by accident

## Maintainer Notes

When this template evolves, maintainers should evaluate changes against this contract:

- Does the change alter the minimum supported adoption shape
- Does the change force migration work for teams at Level 1, 2, or 3
- Does the change convert an optional surface into a hidden requirement
- Does the change make the template more portable or more opinionated

If the answer materially affects adopters, the roadmap, release notes, or migration guidance should say so explicitly.

When updating the contract levels in this document, update `.github/template-contract.json` in the same change. CI checks the documented Level 1, Level 2, and Level 3 file lists against the manifest so drift is caught before merge.
