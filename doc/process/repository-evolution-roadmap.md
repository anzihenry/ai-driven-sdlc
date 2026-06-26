# Repository Evolution Roadmap

This roadmap evolves the repository as a reusable, stack-agnostic template for AI-driven software delivery.

It is based on the current repository state as of 2026-06-22:

- The repository structure is clean and consistent
- Documentation, prompts, and GitHub workflow templates are present
- `src/` is still a placeholder area, not a required product codebase
- CI currently validates template completeness and repository hygiene
- The repository is intended to support many downstream stacks rather than one canonical implementation

## Decisions Locked By This Roadmap

The roadmap makes the following repository-level decisions explicit:

- This repository is a template product, not a single application codebase
- `src/` is an adoption surface for downstream projects, not a mandatory canonical architecture
- Stack-specific implementation examples may be used for validation, but they do not become the repository's primary identity
- CI should primarily protect template integrity, documentation quality, and adopter usability
- Release decisions should be based on downstream adopter impact, not only internal maintainer convenience

## Roadmap Goal

Move the repository through six stages:

1. Template baseline
2. Template capability expansion
3. Multi-stack adoption design
4. Example and validation coverage
5. Governance and release maturity
6. Self-service adoption kit

The outcome should be a repository that is useful as:

- a reusable AI-driven project template
- a documentation and workflow standard for new teams
- a governed repository that can evolve without losing portability

## Current Progress

- Phase 0 is complete: template positioning, placeholder cleanup, minimum template contract, and contract-aware CI are in place.
- Phase 1 is complete: core specs, ADRs, delivery checklist, prompt pack, adoption walkthrough, rollout notes, and learning notes are available and covered by the template contract.
- Phase 2 is complete: `doc/process/multi-stack-adoption.md` defines repository patterns, universal versus stack-variable conventions, `src` usage, CI extensions, Dependabot extensions, prompt adjustments, and migration guidance.
- Phase 3 is complete: `doc/examples/` contains a documented template-repository adoption path, paired validation notes, and CI checks for local example references.
- Phase 4 is complete: AI delivery operating guidance, failure modes, good examples, prompt hardening, and checklist updates are available and covered by the template contract.
- Phase 5 is complete: template-aware versioning examples, migration notes, release checklist upgrades, dry-run release practice, and release automation boundaries are available and covered by the template contract.
- Phase 6 is next: package the adoption flow so downstream teams can choose a path, customize required files, ask AI for help, and validate adoption without maintainer hand-holding.

## Guiding Principles

- Preserve stack agnosticism unless a convention clearly improves reuse
- Prefer reusable patterns over one-off project assumptions
- Keep documentation and prompts grounded in real delivery behavior
- Validate the template through examples and adoption paths, not through one mandatory app implementation
- Treat repository automation as support for template consumers, not only template maintainers

## Phase 0: Stabilize The Template Baseline

### Goal

Make the template internally consistent, easy to adopt, and free of misleading placeholders.

### Scope

- Review all placeholder values and example text
- Remove or rewrite instructions that assume a specific company, repository, or stack
- Clarify which files are required for all adopters versus optional starting points
- Confirm repository ownership, contribution, and release expectations

### Detailed Work

- Audit root docs for language that implies one fixed application layout
- Audit `.github/` for placeholder usernames, URLs, labels, and release assumptions
- Mark which files are part of the minimum template contract
- Mark which files are examples, optional references, or future extension points

### Deliverables

- Updated `README.md` with clear template positioning and adoption guidance
- Updated `CONTRIBUTING.md` with the intended maintenance model
- Reviewed `.github/CODEOWNERS` and placeholder GitHub references
- Documented minimum template contract for downstream adopters
- Clear customization guidance for first-time adopters

### Exit Criteria

- No misleading organization, repository, or workflow placeholders remain
- A new user can understand how to adopt the template in under 5 minutes
- Template validation still passes after cleanup

## Phase 1: Expand Core Template Capabilities

### Goal

Make the repository more useful across common AI-assisted delivery scenarios.

### Scope

- Strengthen the existing spec, ADR, review, and release templates
- Add missing template types if repeated delivery workflows need them
- Improve prompt quality for implementation, review, and planning tasks
- Define what a "minimum viable adoption" of this template looks like

### Detailed Work

- Tighten the project brief so teams can express product, scope, and constraints without excess boilerplate
- Tighten the feature spec so it supports AI implementation and human review equally well
- Tighten the ADR template so downstream teams can record meaningful decisions without over-documenting
- Define a minimum-adoption checklist for teams that only want the essential process surface
- Decide which additional template types are core enough to ship by default

### Deliverables

- Refined project brief, feature spec, and ADR templates
- Improved prompt templates for implementation and review
- Optional new templates for recurring use cases such as planning, retrospectives, or rollout notes
- A documented minimum-adoption path for downstream teams

### Minimum-Adoption Path

The minimum-adoption path should answer:

- Which files a new team must customize on day one
- Which files a new team can defer safely
- What the smallest acceptable AI-assisted workflow looks like
- What checks a team should run before calling its adoption complete

### Exit Criteria

- The template covers the core documentation and collaboration needs of a new AI-assisted project
- Teams can start from the repository without inventing missing foundational artifacts
- Prompt templates are specific enough to be useful but generic enough to stay portable

## Phase 2: Design For Multi-Stack Adoption

### Goal

Ensure the template can be adopted cleanly by projects using different technology stacks.

### Scope

- Define how downstream projects should structure `src/` based on their stack
- Document stack-specific extension points in CI, Dependabot, and prompts
- Decide which repository conventions must stay universal and which can vary by stack
- Add guidance for both new projects and existing-project migrations

### `src/` Positioning

This roadmap treats `src/` as a flexible adoption surface with three acceptable patterns:

1. Teams place their real code inside `src/`
2. Teams keep code elsewhere and use `src/` as an example or reserved convention area
3. Teams replace `src/README.md` with stack-specific guidance during adoption

The template should support all three without implying that only one is correct.

### Detailed Work

- Define recommended adoption patterns for common repository types
- Clarify what parts of the template should be copied as-is versus adapted
- Document where stack-specific CI, dependency, and prompt customizations belong
- Document migration guidance for teams adopting this template into an existing repository

### Deliverables

- Adoption guidance for common patterns such as frontend, backend, full-stack, mobile, or library repositories
- Extension guidance for `.github/workflows/ci.yml` and `.github/dependabot.yml`
- Clear rules for what downstream adopters should customize immediately
- Recommended directory conventions without forcing one canonical application layout

### Expected Output Format

Phase 2 should ideally produce a short, explicit compatibility matrix covering:

- repository type
- likely `src/` treatment
- CI extensions to add
- Dependabot extensions to add
- prompt or doc adjustments to make first

### Exit Criteria

- A team can tell how to adapt the template to its own stack without guessing
- The repository stays stack-agnostic while still giving concrete extension guidance
- `src/` is explained as an adoption surface, not as a mandatory predefined product architecture

## Phase 3: Add Example And Validation Coverage

### Goal

Prove that the template works in practice by validating it through representative examples.

### Scope

- Add one or more small example adoption paths
- Validate that template docs, prompts, and workflow guidance are sufficient for those examples
- Expand CI where useful to check template integrity, documentation quality, and example consistency
- Confirm that stack-specific guidance can be followed without hidden assumptions

### Example Model

This roadmap assumes examples should stay lightweight and should not turn the repository into a monorepo of production applications.

Chosen Phase 3 model:

- Primary model: documented walkthrough plus validation notes
- First representative scenario: documentation or template repository adoption
- Reason: this scenario validates the template's own adoption path without coupling the repository to one application stack

Preferred example order:

1. Documented walkthroughs that explain adoption steps
2. Small in-repo examples only when they validate an important template claim
3. External sample repositories only if in-repo examples become too heavy to maintain

Any example added should justify why it belongs in this repository instead of in external documentation.

### Validation Model

"Validation" in this phase should mean checks that are specific enough to fail on meaningful regressions. Good validation targets include:

- required template files exist and remain non-empty
- placeholder values have been intentionally removed or isolated
- internal documentation links resolve
- required process docs and prompts remain aligned
- example walkthroughs still match the repository structure they describe
- any in-repo sample assets still conform to their documented adoption path

Avoid vague validation goals such as "better documentation quality" unless they are translated into explicit review or automation rules.

### Detailed Work

- Choose one primary example model and document why it was chosen
- Add the smallest example set that can prove adoption guidance is real
- Define which validation checks belong in CI versus manual maintainer review
- Record any gaps discovered when walking through the example adoption flow

### Deliverables

- One or more example structures, walkthroughs, or sample integrations
- Validation guidance showing how an adopter should verify successful setup
- CI updates that protect template quality without coupling the repository to one stack
- Documented gaps discovered during example-driven validation

### Exit Standard

Phase 3 is only complete when a maintainer can follow the chosen example path from the repository docs alone and identify no hidden assumptions that would block a new adopter.

### Exit Criteria

- The template has at least one proven adoption path
- Maintainers can explain how the template was validated in a realistic scenario
- CI can catch meaningful template regressions, not just missing files

## Phase 4: Operationalize AI-Assisted Delivery Patterns

### Goal

Turn the repository from a static template pack into a practical operating model for AI-assisted teams.

### Scope

- Refine prompts using real usage feedback
- Capture common AI failure modes and required human review checkpoints
- Align PR, issue, and delivery checklists with actual collaboration behavior
- Add examples of good specs, good task framing, and good review requests

### Detailed Work

- Record the most common prompt rewrites maintainers keep making by hand
- Capture examples of vague requests that lead to weak AI output
- Add reviewer guidance for common failure classes such as hidden assumptions, over-scaffolding, and unverifiable claims
- Align delivery checklists with the actual validation model defined in Phase 3

### Deliverables

- Updated prompts shaped by real template use
- Refined delivery checklist based on real review and implementation patterns
- Contributor guidance for safe AI-assisted change management
- Example artifacts that show the expected quality bar

### Exit Criteria

- Team members can use the prompts with minimal rewriting
- Reviewers know what to challenge in AI-generated output
- The repository reflects a repeatable AI-assisted workflow, not just generic advice

## Phase 5: Mature Governance And Releases

### Goal

Make the template maintainable and releasable as a reusable product in its own right.

### Scope

- Confirm semantic versioning policy for template changes
- Define how breaking template changes should be communicated
- Validate release labels, release drafter behavior, and manual release workflow
- Add upgrade guidance for downstream adopters when the template evolves

### Breaking Change Definition

For this template repository, a change should normally be considered breaking if it forces downstream adopters to do meaningful migration work. Examples include:

- renaming or removing core template files that adopters are expected to keep
- changing required workflow expectations in a way that invalidates current team usage
- changing repository structure assumptions that affect documented adoption paths
- changing release, review, or documentation contracts that downstream teams rely on

The following are usually not breaking on their own:

- typo fixes
- wording improvements that do not change expected usage
- additive templates or prompts that are optional
- non-behavioral CI cleanup for maintainers only

### Detailed Work

- Define versioning examples for patch, minor, and major template releases
- Align release labels with adopter-facing impact
- Document what upgrade notes must exist for major template releases
- Add a lightweight migration note format for downstream teams

### Deliverables

- Release policy aligned to template maintenance reality
- Updated release checklist for template releases
- Upgrade and migration guidance for adopters when needed
- A tested dry-run release path for the next version

### Exit Criteria

- Maintainers can publish a new template version without improvising process
- Release notes explain impact on adopters, not just internal repository changes
- Breaking template changes include clear migration guidance

## Phase 6: Build A Self-Service Adoption Kit

### Goal

Make the template easy for a new downstream team to adopt, customize, and validate without needing maintainer walkthroughs.

### Scope

- Provide a short adopter quickstart for different time budgets
- Add a decision path for choosing the right adoption route
- Turn customization guidance into a practical checklist
- Add a prompt that helps AI generate a repository-specific adoption plan
- Explain contract validation in adopter-facing language

### Detailed Work

- Create a quickstart that covers the first 5 minutes, 30 minutes, and half day of adoption
- Create a decision tree for new projects, existing projects, documentation repositories, tool or library repositories, and product repositories
- Create a customization checklist for files adopters must update, may remove, or should preserve
- Add an adoption prompt that asks AI to inspect a repository and produce an adoption plan, file changes, risks, and validation steps
- Update docs and contract metadata so the self-service assets are discoverable and protected from drift

### Deliverables

- Adopter quickstart
- Adoption decision tree
- Template customization checklist
- Template adoption prompt
- Updated documentation index and contract registration

### Exit Criteria

- A new adopter can identify the correct adoption path without reading the entire repository
- A new adopter can see which files to customize, keep, defer, or remove
- AI can be prompted to produce a concrete adoption plan from repository context
- Contract validation errors are understandable to adopters, not only maintainers

## Recommended Execution Order

1. Finish Phase 0 before broadening template scope
2. Complete Phase 1 before adding many new workflow surfaces
3. Use Phase 2 to define adoption rules before multiplying examples
4. Use Phase 3 to validate the template through realistic usage
5. Run Phase 4 alongside actual maintenance and adoption feedback
6. Use Phase 5 to support sustainable versioned releases
7. Use Phase 6 to make adoption self-service for downstream teams

## Practical First Sprint

If the goal is to improve the repository quickly without losing focus, the first sprint should prioritize:

1. Cleaning placeholder repository metadata
2. Tightening the template positioning in `README.md`
3. Defining the minimum-adoption path for downstream users
4. Clarifying multi-stack extension points in docs and CI guidance
5. Adding one validated example adoption path

## Suggested Milestones

### Milestone A: Template Contract

- Phase 0 complete
- Minimum-adoption path drafted
- Core template files identified

### Milestone B: Adoption Design

- Phase 1 complete
- Phase 2 compatibility guidance drafted
- `src/` positioning documented clearly

### Milestone C: Proven Usability

- Phase 3 complete
- One validated example path exists
- CI protects more than file presence

### Milestone D: Maintained Product

- Phase 4 and Phase 5 complete
- Prompt refinements are based on real usage
- Releases communicate impact to adopters clearly

### Milestone E: Self-Service Adoption

- Phase 6 complete
- Adopters can choose an adoption path without maintainer guidance
- Adoption prompts and checklists produce concrete next actions

## Risks To Avoid

- Drifting from stack-agnostic guidance into one preferred implementation
- Keeping examples so abstract that adopters still need to invent the workflow
- Expanding prompts without validating whether teams can actually use them
- Overfitting CI to template internals while ignoring real adopter experience
- Shipping template changes without documenting downstream impact

## Definition Of Success

This roadmap succeeds when the repository is clearly usable as a reusable AI-driven template with:

- portable documentation and workflow patterns
- prompts that support real delivery work
- adoption guidance for multiple stacks
- validation paths that prove the template works
- release and governance rules that help downstream teams upgrade safely
- self-service adoption guidance that turns the template into a practical starting point
