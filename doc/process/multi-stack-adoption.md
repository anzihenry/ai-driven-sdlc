# Multi-Stack Adoption Guide

Use this guide when adapting the AI-Driven SDLC Template to a downstream repository with a specific technology stack.

The template stays stack-agnostic. Downstream teams should add stack-specific code, checks, dependencies, and prompts only where they match the repository being adopted.

## Adoption Principles

- Keep the template contract stable while adapting implementation details
- Document the chosen repository layout before adding stack-specific automation
- Add CI checks only when the downstream team can run and maintain them
- Add Dependabot ecosystems only for dependencies that exist in the repository
- Tune prompts with stack-specific validation commands and risk areas
- Avoid turning examples into hidden requirements

## Universal And Stack-Variable Conventions

Use this table to decide what should remain consistent across adopters and what may change by stack.

| Area | Universal Convention | Stack-Variable Convention |
| --- | --- | --- |
| Project brief | Every adoption should explain purpose, users, outcomes, constraints, risks, and first useful slice. | Domain language, success signals, users, and constraints vary by project. |
| Feature specs | Specs should define context, goal, scope, scenarios, requirements, AI boundaries, acceptance criteria, validation, rollout, and risks. | Requirement details, UX notes, data model, and validation methods vary by stack. |
| ADRs | Decisions should record context, choice, alternatives, adopter impact, migration cost, AI usage boundary, validation evidence, and follow-up path. | Decision topics and technical alternatives vary by architecture, platform, and ecosystem. |
| Prompt flow | Teams should have prompts for planning, implementation, review, and acceptance. | Prompt context should name stack-specific commands, files, frameworks, and risks. |
| Contract validation | Retained template surfaces should stay aligned with `doc/process/minimum-template-contract.md` and `.github/template-contract.json`. | Downstream teams may choose Level 1, Level 2, or Level 3 adoption and may remove optional surfaces intentionally. |
| Review evidence | Review should connect changes back to a spec, ADR, issue, or checklist and include validation evidence. | Evidence may be unit tests, browser checks, API tests, simulator runs, package builds, docs checks, or manual walkthroughs. |
| Source layout | The chosen source layout should be documented and understandable to new contributors. | Code may live in `src/`, stack-specific subdirectories, framework defaults, or an existing repository layout. |
| Build commands | Local and CI validation commands should be documented. | Commands vary by package manager, language, framework, platform, and deployment target. |
| Dependency ecosystem | Dependency update rules should match real manifests and ownership. | Ecosystems may include GitHub Actions, npm, pip, gomod, cargo, gradle, Docker, or others. |
| Deployment checks | Release and rollout risk should be considered before merge. | Deployment checks vary by hosting platform, app store, package registry, infrastructure, or documentation site. |
| Test strategy | Each change should have an appropriate validation path. | Test mix varies by stack, such as unit, integration, contract, browser, simulator, package, migration, or link checks. |

## Compatibility Matrix

| Repository Type | Likely `src/` Treatment | CI Extensions To Add | Dependabot Extensions To Add | Prompt Or Doc Adjustments |
| --- | --- | --- | --- | --- |
| Frontend app | Use `src/web/` or replace `src/README.md` with the framework layout. | Install dependencies, lint, typecheck, test, build, accessibility or visual checks when used. | `npm` or another package ecosystem for the frontend directory. | Mention framework, routing, state, styling, build command, browser validation, and accessibility risks. |
| Backend API | Use `src/api/` or the service's existing source root. | Lint, unit tests, integration tests, API contract tests, migration checks when relevant. | `npm`, `pip`, `gomod`, `cargo`, `maven`, or another ecosystem for the API directory. | Mention API surface, data contracts, auth, error handling, observability, and migration risks. |
| Full-stack app | Use `src/web/` and `src/api/`, or document the framework's integrated layout. | Frontend checks, backend checks, end-to-end checks, build, migration checks. | Add each package ecosystem in the correct directory. | Mention cross-boundary contracts, shared types, environment variables, deployment order, and rollback risks. |
| Mobile app | Use `src/mobile/` or the platform's conventional app directory. | Lint, unit tests, platform build, simulator or device smoke tests when available. | Ecosystems such as `npm`, `gradle`, `swift`, or platform-specific tooling when supported. | Mention platform targets, simulator/device validation, permissions, release channel, and store review risks. |
| Library or package | Use `src/` as the package root or document the language-specific package layout. | Lint, tests, build/package, compatibility matrix, public API checks. | Package ecosystem for the library root. | Mention public API, semantic versioning, compatibility, generated artifacts, and migration guidance. |
| Documentation or template repository | Use `src/` only for examples or remove practical use of it. | Template contract checks, link checks, markdown checks, example consistency checks. | GitHub Actions only unless examples include dependencies. | Mention adopter impact, docs consistency, examples, contract levels, and release notes. |
| Existing repository adopting selected surfaces | Keep existing source layout and document where the template applies. | Keep existing CI, then add template checks only where useful. | Preserve existing dependency update rules and add missing ecosystems intentionally. | Mention current architecture, adoption level, retained template surfaces, and migration boundaries. |

## `src/` Usage Rules

Downstream teams should choose and document one of these approaches:

1. Use `src/` as the primary source root
2. Use `src/` as a parent for stack-specific roots such as `src/web/`, `src/api/`, or `src/mobile/`
3. Keep existing source roots and use `src/README.md` only as adoption guidance
4. Replace `src/README.md` with stack-specific instructions

Do not move an existing codebase into `src/` unless that improves clarity for the team maintaining it.

## CI Extension Guidance

Start with the template contract validator if the workflow is retained:

```sh
python3 .github/scripts/validate_template_contract.py
```

Then add stack-specific jobs in this order:

1. Formatting or lint checks
2. Unit tests
3. Type checks or static analysis
4. Build or package checks
5. Integration, browser, simulator, or end-to-end checks
6. Security, dependency, or policy checks

Each CI check should have a matching local command in the downstream README or contribution guide.

## Dependabot Extension Guidance

Only add ecosystems that match real dependency manifests.

Common examples:

- `npm` for `package.json`
- `pip` for `requirements.txt`
- `poetry` for `pyproject.toml` with Poetry
- `gomod` for `go.mod`
- `cargo` for `Cargo.toml`
- `gradle` for Gradle projects
- `github-actions` for workflows under `.github/workflows`
- `docker` for Dockerfiles

Set the `directory` to the folder where the manifest actually lives. For multi-package repositories, add one entry per maintained dependency root.

## Prompt Customization Guidance

When adopting prompts, update the repository context before use.

At minimum, specify:

- relevant source directories
- stack-specific validation commands
- framework or language conventions
- files AI may change
- files AI should not change without approval
- common risks for the stack
- expected manual checks

Examples:

- Frontend prompts should mention browser validation, responsive behavior, accessibility, and build commands.
- Backend prompts should mention API contracts, auth, data migration, observability, and integration tests.
- Template prompts should mention adopter impact, contract levels, docs consistency, and release notes.

## New Project Adoption

For a new project:

1. Choose adoption level from `doc/process/minimum-template-contract.md`
2. Fill `doc/specs/project-brief.md`
3. Choose the source layout and document it in `README.md`
4. Create the first feature spec
5. Add minimal stack-specific CI
6. Add dependency update rules for real manifests
7. Update prompts with stack-specific validation commands

## Existing Project Migration

For an existing project:

1. Keep the existing source layout unless there is a strong reason to move it
2. Add the minimum template files first
3. Backfill the project brief and one ADR for current architecture
4. Map existing CI to the template's validation expectations
5. Add prompt guidance that references existing modules and commands
6. Introduce issue, PR, release, and checklist templates gradually
7. Record any deferred template surfaces as intentional exclusions

## Adoption Completion Check

A stack-specific adoption is complete when:

- the chosen repository type is documented
- `src/` usage is clear
- CI checks match the retained template and real stack
- Dependabot entries match real dependency manifests
- prompts include stack-specific context and validation commands
- the first feature spec can guide implementation and review
- removed template surfaces are documented as intentional
