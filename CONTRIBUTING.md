# Contributing Guide

## Working Principles

- Start from a spec when the change affects adopter-facing behavior
- Keep changes small and reviewable
- Treat AI-generated output as a draft until verified
- Capture meaningful technical decisions in `doc/decisions/`
- Optimize for reuse across multiple downstream stacks, not one preferred implementation

## Default Delivery Flow

1. Create or update the relevant issue
2. Write or refine the spec in `doc/specs/` or update the relevant process guidance
3. Implement the smallest complete template change
4. Validate the template impact locally
5. Open a pull request using the repository template
6. Record follow-up work before merge if anything is deferred

## AI-Assisted Development Expectations

- State clearly which tool was used
- Review generated content for correctness, clarity, portability, and security
- Remove dead guidance or speculative abstractions
- Document assumptions in the PR if they affect adopters

## Pull Request Expectations

- Link the relevant issue, spec, or ADR
- Summarize risk and validation steps
- Include screenshots or logs when they help review
- Keep unrelated changes out of the PR
- Add labels when they affect release notes, adopter expectations, or version bumps

## Label Guide

- `bug`: defects, regressions, or incorrect behavior
- `enhancement`: new user or engineering capability
- `task`: scoped implementation or maintenance work
- `documentation`: docs, prompts, specs, and written guidance
- `ci`: GitHub Actions and CI workflow changes
- `tooling`: repository automation and developer workflow changes
- `template`: reusable template structure changes
- `dependencies`: dependency or third-party action updates
- `security`: security-sensitive work
- `needs-spec`: change is blocked on better requirements
- `major`: breaking or version-major release impact
- `skip-changelog`: exclude the PR from release notes

## Release Expectations

- Use semantic versioning tags such as `v0.1.0`
- Let the release draft collect merged changes on `main`
- Use the manual GitHub Release workflow to publish a reviewed version
- Use `skip-changelog` on PRs that should stay out of release notes
- Follow `doc/process/versioning-and-releases.md` when choosing the next version
- Run `doc/process/release-checklist.md` before publishing
- Treat downstream migration cost as the primary signal for major releases

## Review Guidelines

- Prioritize correctness, adopter clarity, and downstream impact
- Call out missing validation steps or upgrade guidance
- Prefer concrete suggestions over broad opinions
- Be explicit when something should be deferred to follow-up
