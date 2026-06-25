# AI-Driven SDLC Template

This repository is a stack-agnostic template for starting projects that use AI as a first-class part of the software delivery lifecycle.

It is designed to help teams keep requirements, implementation, review, and decision-making structured and auditable while still moving fast with AI tools.

The repository itself is a reusable template product. It is not tied to one application architecture or one required source layout.

## Goals

- Turn ambiguous ideas into written specs before coding
- Keep architecture decisions lightweight but explicit
- Make AI-assisted implementation repeatable
- Reduce rework by standardizing review and acceptance steps
- Provide a reusable adoption surface for future teams and products

## Repository Structure

```text
.
|-- doc/
|   |-- decisions/          # ADRs and decision records
|   |-- process/            # Team workflow and AI collaboration guides
|   `-- specs/              # Product briefs and feature specs
|-- prompts/                # Reusable AI prompt templates
|-- src/                    # Optional code convention or example area for adopters
|-- .editorconfig
|-- .gitignore
`-- README.md
```

## Recommended Workflow

1. Create or update `doc/specs/project-brief.md`
2. Add a feature spec from `doc/specs/feature-spec-template.md`
3. Record major technical tradeoffs in `doc/decisions/`
4. Use the prompt templates in `prompts/` to drive implementation and review
5. Adapt the repository structure to your stack and team workflow
6. Capture acceptance notes back into the relevant spec
7. Use `doc/process/versioning-and-releases.md` before publishing a release

## How To Use This Template

### For a new project

1. Rename the repository
2. Replace the project brief with your actual context
3. Decide how your stack should use this repository's structure, including whether `src/` will contain real code, examples, or only guidance
4. Keep specs, prompts, and ADRs aligned with the way your team actually works

### For an existing project

1. Decide whether to adopt this template in place or copy selected parts into your current repository
2. Backfill the project brief and one ADR for the current architecture
3. Start using feature specs and prompts for all new work

## Minimum Recommended Adoption

The smallest useful adoption of this template usually includes:

- a completed `doc/specs/project-brief.md`
- at least one real feature spec
- a review flow that uses the prompt templates as a starting point
- contributor guidance that reflects your actual team process
- CI or manual checks that verify the parts of the template you decide to keep

For the formal keep/customize/remove contract, see `doc/process/minimum-template-contract.md`.
For a step-by-step adoption path, see `doc/process/adoption-walkthrough.md`.
For prompt selection guidance, see `prompts/README.md`.

## Suggested Conventions

- Keep specs short enough to be reviewed quickly
- Prefer one feature per spec
- Write ADRs only for decisions that affect future work
- Treat AI outputs as drafts until reviewed by a human
- Store reusable prompts in version control
- Use labels consistently so release automation stays reliable

## Next Steps

- Remove placeholder ownership and repository references before wider adoption
- Decide the minimum template contract your downstream teams should keep
- Add stack-specific CI, dependency, and deployment guidance only where your adopters need it
- Validate the template through one or more documented adoption paths
- Use the GitHub Release workflow for versioned template releases
