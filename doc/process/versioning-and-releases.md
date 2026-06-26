# Versioning And Releases

This document defines how this repository should version and publish changes.

## Goals

- Make release decisions predictable
- Keep version numbers aligned with user impact
- Ensure GitHub automation and human review work together
- Avoid undocumented or surprise releases

## Versioning Standard

Use semantic versioning with a leading `v` in Git tags and GitHub Releases.

Examples:

- `v0.1.0`
- `v0.2.3`
- `v1.0.0`

## How To Choose The Next Version

Choose the version based on downstream adopter impact, not only maintainer effort.

### Patch release

Use a patch release when the change is small and backward-compatible.

Typical examples:

- Bug fixes
- Documentation improvements
- CI or tooling fixes
- Template polish that does not change expected usage
- Dependency updates with no breaking behavior
- Clarifying wording in existing templates
- Non-behavioral cleanup in release or validation workflows
- Fixing examples without changing the adoption contract

### Minor release

Use a minor release when the change adds backward-compatible capability.

Typical examples:

- New template modules
- New prompt packs
- New automation workflows
- New reusable documentation patterns
- New optional example adoption paths
- New optional validation checks
- New recommended guidance that does not invalidate current adoption

### Major release

Use a major release when the change breaks existing expectations.

Typical examples:

- Repository structure changes that require migration
- Removing or renaming core templates
- Workflow changes that alter how contributors must work
- Breaking automation or release policy changes
- Changing Level 1, Level 2, or Level 3 adoption expectations in a way that forces downstream work
- Renaming or removing contract-governed files
- Changing `.github/template-contract.json` semantics in a way that invalidates current adopters
- Replacing the prompt flow, delivery checklist, or review expectations with incompatible guidance

## Template-Specific Version Examples

| Change | Likely Version | Why |
| --- | --- | --- |
| Fix typos in `doc/specs/feature-spec-template.md` | Patch | No expected adopter workflow changes. |
| Clarify wording in `prompts/code-review.md` without changing expected inputs or outputs | Patch | Improves existing guidance without migration. |
| Add a new optional prompt under `prompts/` and register it as Level 2 recommended | Minor | Adds capability while preserving existing adopters. |
| Add a new example adoption path under `doc/examples/` | Minor | Adds reusable guidance without breaking current usage. |
| Add a new optional CI validation rule that only checks retained files | Minor | Adds template quality protection without forcing all adopters to change. |
| Rename `doc/specs/feature-spec-template.md` | Major | Breaks documented paths and downstream references. |
| Remove `prompts/feature-implementation.md` from Level 1 | Major | Changes the minimum supported adoption shape. |
| Change the meaning of Level 2 adoption | Major | Forces downstream teams to reassess retained surfaces. |

## Breaking Change Test

Before choosing a major version, ask:

- Does this force downstream adopters to rename, move, or recreate files
- Does this invalidate a documented adoption path
- Does this change the minimum template contract
- Does this change required review, validation, or release behavior
- Does this require migration notes for a team already using the template

If any answer is yes, treat the change as major unless there is a clearly documented compatibility path.

## Label-To-Version Rules

The repository uses labels to support release decisions.

- `major`: indicates a breaking or version-major change
- `enhancement` or `feature`: usually implies a minor release
- `bug`, `documentation`, `tooling`, `template`, `ci`, `task`, `dependencies`, `security`: usually imply a patch release
- `skip-changelog`: excludes the pull request from release notes

If multiple labels exist across merged pull requests, release impact should be decided by the highest-impact change:

- Major beats minor
- Minor beats patch

## Release Cadence

Use a lightweight cadence unless the project later needs something stricter.

Suggested default:

- Patch: release when enough useful fixes accumulate
- Minor: release after a coherent set of improvements is merged
- Major: release intentionally, with migration notes

## Release Sources Of Truth

Use these artifacts together:

- Specs in `doc/specs/` for what changed
- PR labels for release categorization
- Release Drafter for draft release notes
- GitHub Release entries for published versions

## Before Releasing

- Make sure `main` is stable
- Review the draft release notes
- Confirm the target version number
- Confirm no breaking changes are unlabeled
- Confirm docs reflect any workflow or structure changes
- Confirm release notes explain adopter-facing impact
- Confirm migration notes exist when downstream action is required

## Publishing A Release

The repository uses a manual GitHub Actions workflow for publishing releases.

1. Open the repository Actions tab
2. Select the `Release` workflow
3. Run the workflow manually
4. Enter a version without the `v` prefix, such as `0.2.0`
5. Confirm the target branch or commit, usually `main`
6. Publish the generated GitHub Release

The workflow will create:

- A Git tag such as `v0.2.0`
- A GitHub Release using generated release notes

## After Releasing

- Verify the tag and release were created correctly
- Share release notes with the team if needed
- Capture any follow-up work as issues
- Update roadmap or planning docs if the release changes priorities

## Exceptions

If a release does not fit the rules above, document the exception in the release notes or PR summary so future maintainers understand why.
