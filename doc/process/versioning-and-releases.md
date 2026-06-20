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

### Patch release

Use a patch release when the change is small and backward-compatible.

Typical examples:

- Bug fixes
- Documentation improvements
- CI or tooling fixes
- Template polish that does not change expected usage
- Dependency updates with no breaking behavior

### Minor release

Use a minor release when the change adds backward-compatible capability.

Typical examples:

- New template modules
- New prompt packs
- New automation workflows
- New reusable documentation patterns

### Major release

Use a major release when the change breaks existing expectations.

Typical examples:

- Repository structure changes that require migration
- Removing or renaming core templates
- Workflow changes that alter how contributors must work
- Breaking automation or release policy changes

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
