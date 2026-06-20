# AI-Driven SDLC Template

This repository is a stack-agnostic template for starting projects that use AI as a first-class part of the software delivery lifecycle.

It is designed to help teams keep requirements, implementation, review, and decision-making structured and auditable while still moving fast with AI tools.

## Goals

- Turn ambiguous ideas into written specs before coding
- Keep architecture decisions lightweight but explicit
- Make AI-assisted implementation repeatable
- Reduce rework by standardizing review and acceptance steps
- Provide a reusable project layout for future teams and products

## Repository Structure

```text
.
|-- doc/
|   |-- decisions/          # ADRs and decision records
|   |-- process/            # Team workflow and AI collaboration guides
|   `-- specs/              # Product briefs and feature specs
|-- prompts/                # Reusable AI prompt templates
|-- src/                    # Product source code
|-- .editorconfig
|-- .gitignore
`-- README.md
```

## Recommended Workflow

1. Create or update `doc/specs/project-brief.md`
2. Add a feature spec from `doc/specs/feature-spec-template.md`
3. Record major technical tradeoffs in `doc/decisions/`
4. Use the prompt templates in `prompts/` to drive implementation and review
5. Build the actual application inside `src/`
6. Capture acceptance notes back into the relevant spec
7. Use `doc/process/versioning-and-releases.md` before publishing a release

## How To Use This Template

### For a new project

1. Rename the repository
2. Replace the project brief with your actual context
3. Add your tech stack files inside `src/`
4. Keep specs and ADRs updated as the project evolves

### For an existing project

1. Move current source code into `src/` if needed
2. Backfill the project brief and one ADR for the current architecture
3. Start using feature specs for all new work

## Suggested Conventions

- Keep specs short enough to be reviewed quickly
- Prefer one feature per spec
- Write ADRs only for decisions that affect future work
- Treat AI outputs as drafts until reviewed by a human
- Store reusable prompts in version control
- Use labels consistently so release automation stays reliable

## Next Steps

- Add the actual application stack inside `src/`
- Add CI checks once the stack is chosen
- Add testing and deployment workflows for the selected platform
- Extend Dependabot for the chosen package ecosystem
- Use the GitHub Release workflow for versioned template releases
