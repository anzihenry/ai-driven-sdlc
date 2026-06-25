# Template Repository Adoption Example

This example shows how a downstream documentation or template repository can adopt the AI-Driven SDLC Template.

It is a documented walkthrough, not a runnable sample project.

## Example Context

- Repository type: Documentation or template repository
- Adoption level: Level 2 recommended team adoption
- Primary users: maintainers who write specs, prompts, and workflow guidance
- Secondary users: downstream teams adopting the template
- Main goal: make the repository understandable, reviewable, and safe to evolve with AI assistance

## Why This Example Exists

This example validates the template's own adoption path without requiring a specific application stack.

It is useful because documentation and template repositories still need:

- clear project context
- scoped feature specs
- ADRs for governance decisions
- AI implementation and review prompts
- release and migration notes
- validation checks for retained template surfaces

## Step 1: Choose Adoption Level

The example chooses Level 2 from `doc/process/minimum-template-contract.md`.

Level 2 is appropriate because the repository wants:

- the core AI-assisted workflow from Level 1
- issue and pull request templates
- Dependabot and label configuration
- release and review habits
- prompt and rollout support

Level 3 is not required unless the repository also wants to preserve the full release, label, and workflow automation surface.

## Step 2: Choose Repository Type

The example uses the `Documentation or template repository` row from `doc/process/multi-stack-adoption.md`.

Implications:

- `src/` is optional and should not be treated as a required application root
- CI should prioritize template contract checks, link checks, markdown checks, and example consistency checks
- Dependabot may only need the `github-actions` ecosystem unless examples add real dependencies
- prompts should emphasize adopter impact, docs consistency, contract levels, and release notes

## Step 3: Decide How To Use `src/`

This example keeps `src/README.md` as optional adoption guidance.

The downstream repository may:

- keep `src/README.md` if it wants to show possible source layout conventions
- remove practical use of `src/` if it is purely documentation-focused
- replace `src/README.md` with example-specific guidance if examples are added later

The selected choice should be documented in the downstream `README.md`.

## Step 4: Fill The Project Brief

The downstream repository should customize `doc/specs/project-brief.md`.

Minimum content:

- what template or documentation system the repository provides
- who adopts or maintains it
- which workflow problems it solves
- what the first useful adoption slice should be
- what success looks like for maintainers and adopters

For this example, a good first useful slice is:

- publish a clear minimum template contract
- validate it in CI
- provide one adoption walkthrough

## Step 5: Create The First Feature Spec

The first feature spec should focus on a small, reviewable improvement.

Example feature:

- Title: Add contract-aware template validation
- Goal: ensure required template files exist and recommended surfaces stay synchronized with written contract guidance
- Acceptance criteria:
  - contract manifest exists
  - contract validator passes locally
  - contract documentation and manifest stay synchronized
  - CI runs the validator

## Step 6: Adapt Prompts

The downstream repository should update prompt context before using AI agents.

For a documentation or template repository, prompts should mention:

- docs and templates are the main deliverables
- adopter impact matters more than app runtime behavior
- validation should include template contract checks
- AI should avoid inventing unsupported stack-specific requirements
- release notes should explain downstream adoption impact

Recommended prompt flow:

1. Use `prompts/planning.md` to break broad template ideas into specs or roadmap items
2. Use `prompts/feature-implementation.md` to update docs, prompts, or CI checks
3. Use `prompts/code-review.md` to check adopter impact and drift from the spec
4. Use `prompts/acceptance-qa.md` to turn acceptance criteria into verification evidence

## Step 7: Align GitHub Automation

For this repository type, retain or add automation only when it supports template maintainability.

Recommended checks:

- run `python3 .github/scripts/validate_template_contract.py`
- check that retained docs and prompts are non-empty
- check that contract documentation and manifest stay synchronized
- add link or example consistency checks if examples grow

Dependabot:

- keep `github-actions` updates for workflow dependencies
- add package ecosystems only if examples or tooling introduce real manifests

## Step 8: Complete Adoption Checks

Before adoption is considered complete, confirm:

- `README.md` explains that the repository is a documentation or template repository
- `doc/specs/project-brief.md` is customized
- the first feature spec exists or is ready to be written
- `doc/process/minimum-template-contract.md` matches `.github/template-contract.json`
- `prompts/README.md` explains when each prompt should be used
- retained GitHub automation reflects actual maintainer workflow
- removed template surfaces are documented as intentional exclusions

## Example Result

This example is successful when a maintainer can follow the repository docs alone and understand:

- which adoption level was chosen
- why the repository type is documentation or template repository
- how `src/` should be treated
- which CI and Dependabot surfaces are relevant
- which prompts support planning, implementation, review, and acceptance
- what evidence is needed before changes merge
