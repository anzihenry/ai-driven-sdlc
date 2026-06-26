# Adoption Decision Tree

Use this decision tree to choose the right adoption path before copying or rewriting template files.

The goal is not to classify every repository perfectly. The goal is to avoid adopting too much or too little template surface by accident.

## Start Here

### Are You Starting A New Repository?

If yes:

- Start with `doc/process/adopter-quickstart.md`.
- Use Level 2 adoption unless the team explicitly wants a smaller process surface.
- Keep `src/README.md` until the real source layout is chosen.
- Use `doc/process/multi-stack-adoption.md` to decide how `src/`, CI, Dependabot, and prompts should adapt.

If no, continue to the existing repository path.

### Are You Adopting Into An Existing Repository?

If yes:

- Start with `doc/process/adoption-walkthrough.md`.
- Use Level 1 adoption first unless the existing repository already has room for the full governance surface.
- Add docs and prompts before replacing automation.
- Treat `.github/` changes as a separate migration so existing CI and review habits are not disrupted.

If no, continue to the repository type choices below.

## Repository Type Choices

| Repository Type | Recommended Path | First Files To Customize | Extra Guidance |
| --- | --- | --- | --- |
| Documentation or template repository | Level 2 adoption | `README.md`, `doc/specs/project-brief.md`, `doc/process/adoption-walkthrough.md` | Use `doc/examples/template-repository-adoption.md` as the closest example. |
| Product application repository | Level 2 adoption with stack-specific extensions | `README.md`, `CONTRIBUTING.md`, `doc/specs/project-brief.md`, `src/README.md` | Use `doc/process/multi-stack-adoption.md` before changing CI. |
| Library or package repository | Level 1 first, then Level 2 governance | `README.md`, `doc/specs/project-brief.md`, `doc/process/delivery-checklist.md` | Keep release docs if public consumers depend on versions. |
| Internal tooling repository | Level 1 or Level 2 depending on team size | `README.md`, `CONTRIBUTING.md`, `prompts/README.md` | Focus prompts on maintenance, review, and validation evidence. |
| Research or prototype repository | Level 1 adoption | `README.md`, `doc/specs/project-brief.md`, `prompts/planning.md` | Defer release automation until the work has stable consumers. |

## Adoption Level Decision

Choose Level 1 if:

- you only need the minimum AI-assisted delivery workflow
- the repository already has its own governance and automation
- the team wants to test the template before committing to a broader process

Choose Level 2 if:

- you want the recommended template experience
- the team wants examples, operating guidance, release notes, and retrospective learning
- the repository will be used by multiple contributors

Choose Level 3 if:

- you want the full GitHub automation surface
- the team accepts the included label, release-drafter, and workflow conventions
- maintainers will actively keep automation aligned with real usage

## When To Use Each Guide

- Use `doc/process/adopter-quickstart.md` when you need the shortest safe path.
- Use `doc/process/adoption-walkthrough.md` when you are applying the template step by step.
- Use `doc/process/multi-stack-adoption.md` when source layout, CI, dependencies, or prompts need stack-specific choices.
- Use `doc/process/minimum-template-contract.md` when deciding what to keep, customize, or remove.

## Decision Record

Before calling adoption complete, record these choices in the repository or PR:

- chosen adoption level
- repository type
- `src/` treatment
- retained GitHub automation
- intentional deviations from the template contract
- first prompt or workflow the team will actually use
