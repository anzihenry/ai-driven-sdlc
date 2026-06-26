# GitHub Configuration

This directory contains repository-level collaboration and automation defaults.

## Included

- A stack-agnostic CI workflow
- Dependabot configuration for repository automation
- Repository label catalog and PR auto-labeling
- Pull request template
- Issue templates
- CODEOWNERS
- Release drafting and manual release workflows

## Release Policy

This template is released like a reusable product, not like a single application
deployment. Human release decisions are documented in:

- `doc/process/versioning-and-releases.md`
- `doc/process/release-checklist.md`
- `doc/process/release-dry-run.md`
- `doc/process/release-publication-guide.md`
- `doc/process/distribution-channels.md`
- `doc/process/release-announcement-template.md`
- `doc/process/migration-notes-template.md`

## Template Release Governance

Before running the manual release workflow:

- Choose the version from downstream adopter impact, not from commit volume.
- Run the template contract validator and fix any required surface drift.
- Complete a release dry run against a realistic adoption path.
- Confirm the intended distribution channel and adopter upgrade path.
- Add migration notes when an adopter needs to change files, workflows, prompts,
  contracts, or release practices after upgrading.
- Prepare an announcement when adopters need to understand impact, validation,
  migration, or safe deferral.
- Review generated release notes for adopter-facing impact, migration cost, and
  follow-up decisions.

## Automation Boundaries

- `release-drafter.yml` helps group changes and suggest version categories, but
  it does not make the final SemVer decision.
- `workflows/release.yml` publishes a tag and GitHub Release after a human has
  completed the release checklist and dry run.
- The release workflow does not approve announcement text, decide upgrade
  urgency, or determine whether migration notes are sufficient.
- Label automation supports changelog hygiene; humans still confirm whether a
  change is core-template, optional-extension, or stack-specific.

## Post-Release Human Steps

After the workflow creates the release:

- Review generated release notes before treating them as final.
- Link migration notes, upgrade guidance, and validation evidence when relevant.
- Publish or share the release announcement through the chosen distribution
  channel.
- Record follow-up issues for adopter questions, release note corrections, or
  migration gaps.

## Next Upgrade

Once downstream adoption patterns are clear, extend `workflows/ci.yml` with the checks your adopters actually need, such as:

- Lint
- Test
- Build
- Security scanning

Also extend `.github/dependabot.yml` with stack-specific ecosystems such as `npm`, `pip`, or `docker` only when those ecosystems are part of the supported adoption surface.
