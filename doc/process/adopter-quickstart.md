# Adopter Quickstart

Use this quickstart when you are adopting this template into a new or existing repository and want the shortest safe path to first use.

This guide does not replace the full adoption walkthrough. It helps you decide what to read and change first.

## Choose Your Time Budget

### First 5 Minutes

Use this path when you are evaluating whether the template fits.

1. Read `README.md` to understand the template's purpose.
2. Read `doc/process/minimum-template-contract.md` to understand Level 1, Level 2, and Level 3 adoption.
3. Open `doc/specs/project-brief.md` and check whether your team can answer the project context questions.
4. Open `prompts/README.md` and identify which prompt you would use first.
5. Run the contract validator if this repository has already been copied:

```sh
python3 .github/scripts/validate_template_contract.py
```

If you cannot answer the project brief or choose a first prompt, pause adoption and clarify the project goal before copying more files.

### First 30 Minutes

Use this path when you want a working initial adoption.

1. Choose an adoption level from `doc/process/minimum-template-contract.md`.
2. Choose a repository type from `doc/process/multi-stack-adoption.md`.
3. Customize these files first:
   - `README.md`
   - `CONTRIBUTING.md`
   - `doc/specs/project-brief.md`
4. Decide whether `src/` is real source code, examples only, or unused.
5. Keep only the GitHub automation that matches your team's actual workflow.
6. Run the contract validator and record any intentional deviations.

At the end of this path, your repository should explain what it is, how people contribute, and which template surfaces are intentionally kept.

### First Half Day

Use this path when adoption should be ready for team use.

1. Complete the 30-minute path.
2. Create or adapt one feature spec using `doc/specs/feature-spec-template.md`.
3. Record one meaningful decision using `doc/decisions/ADR-template.md` if adoption changes workflow, architecture, or governance.
4. Use `prompts/planning.md` if the work is still ambiguous.
5. Use `prompts/feature-implementation.md` only after a spec or scoped task exists.
6. Use `prompts/acceptance-qa.md` to turn the spec into an acceptance checklist.
7. Complete `doc/process/delivery-checklist.md` for the first adopted change.
8. Run the contract validator again.

At the end of this path, the repository should be ready for a real AI-assisted delivery cycle.

## Minimum Safe Adoption

A minimum safe adoption has:

- a customized project brief
- contributor guidance that matches the real team
- at least one usable prompt path
- a clear decision about `src/`
- known contract deviations documented as intentional choices
- validation evidence from the contract validator or an explicit reason it cannot run

## When To Read The Full Guides

- Use `doc/process/adoption-walkthrough.md` when you want the full step-by-step adoption flow.
- Use `doc/process/multi-stack-adoption.md` when you need stack-specific adaptation guidance.
- Use `doc/process/ai-delivery-operating-guide.md` when your team is ready to run repeated AI-assisted delivery.
- Use `doc/process/versioning-and-releases.md` when you will maintain this template as a reusable product.

## Stop Conditions

Pause adoption before adding more files if:

- the project goal is unclear
- the team cannot choose an adoption level
- the repository type is unclear
- the contract validator fails and no one can explain why
- retained automation does not match the team's real workflow

These are not failures. They are signals that the adoption needs a small planning pass before more template surface is copied.
