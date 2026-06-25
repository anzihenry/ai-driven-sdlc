# Good Feature Spec Example

This example shows a focused feature spec for a template repository.

## Title

Add example reference validation to the template contract checker

## Status

- Status: Proposed
- Owner: Template maintainer
- Reviewers: Documentation maintainer, CI maintainer
- Related issue or discussion: Phase 3 example validation
- Target release or milestone: Phase 3

## Context

- Current state: Example adoption documents can be added, but local file references inside those examples are not checked.
- Pain or limitation: An example can mention a path that no longer exists, causing adopters to follow stale guidance.
- Why now: Phase 3 introduces documented example adoption paths.
- Relevant project brief section: Template quality and adopter confidence.

## Goal

- Primary goal: Fail CI when example documents reference local paths that do not exist.
- Secondary goal: Keep example validation lightweight and stack-agnostic.
- How this improves the user, adopter, or maintainer experience: Maintainers can trust that example walkthroughs point to real repository artifacts.

## Scope

### In Scope

- Add an `example_docs` list to `.github/template-contract.json`
- Extend `.github/scripts/validate_template_contract.py` to check local path references in those docs
- Update validation output so maintainers know example references are checked

### Out Of Scope

- Full markdown linting
- External URL validation
- Building runnable sample applications

## Users And Scenarios

1. As a template maintainer, when I add an example adoption path, I want CI to catch broken local references, so that adopters do not follow stale docs.
2. As a downstream adopter, when I read an example path, I want referenced files to exist, so that I can apply the template confidently.

## Requirements

### Functional Requirements

- The validator must read `example_docs` from `.github/template-contract.json`.
- The validator must scan inline code references in listed example docs.
- The validator must fail when a local path reference does not exist.

### Non-Functional Requirements

- Performance: Validation should remain fast for small documentation sets.
- Reliability: The check should avoid false positives for prose, commands, and external URLs.
- Portability: The check should use Python standard library only.

## AI-Assisted Delivery Notes

- AI may change the validator, manifest, and example docs.
- AI should not add markdown lint dependencies or external URL checks without approval.
- Human review focus: false positives, skipped references, and contract drift.
- Known risks for AI output: over-scoping validation into a full documentation linter.

## Acceptance Criteria

- [ ] Contract validator passes with current example docs.
- [ ] A missing local path in an example doc causes validation failure.
- [ ] The validator output names the example doc and missing path.
- [ ] No external dependencies are introduced.

## Validation Plan

- Automated checks: `python3 .github/scripts/validate_template_contract.py`
- Manual checks: inspect validator logic for local path detection and ignored command snippets
- Documentation review: confirm example docs are listed in the contract manifest
- Rollback or recovery check: remove `example_docs` validation if it creates unacceptable false positives

## Risks And Follow-Ups

- Risk 1: Inline code that is not a path may be misread as a path.
- Risk 2: Future examples may need explicit ignore rules.
- Deferred follow-up 1: Consider markdown link validation if examples grow.

## Implementation Log

- AI assistance used:
- Key implementation decisions:
- Validation completed:
- Human reviewer:
- Final notes:
