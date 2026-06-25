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

Human release decisions are documented in:

- `doc/process/versioning-and-releases.md`
- `doc/process/release-checklist.md`

## Next Upgrade

Once downstream adoption patterns are clear, extend `workflows/ci.yml` with the checks your adopters actually need, such as:

- Lint
- Test
- Build
- Security scanning

Also extend `.github/dependabot.yml` with stack-specific ecosystems such as `npm`, `pip`, or `docker` only when those ecosystems are part of the supported adoption surface.
