# AI Delivery Operating Guide

Use this guide to run a complete AI-assisted delivery cycle with this template.

The goal is to make AI collaboration repeatable, reviewable, and grounded in repository evidence.

## Operating Principles

- Start with context before implementation
- Keep each change tied to a spec, ADR, issue, or checklist
- Use AI for drafting, implementation support, review support, and validation planning
- Keep human judgment responsible for scope, correctness, security, release impact, and merge decisions
- Record validation evidence before merge
- Feed lessons back into prompts, templates, and checklists

## Delivery Flow

### 1. Frame The Work

Use `prompts/planning.md` when the request is ambiguous.

Inputs:

- rough request, idea, or problem
- repository purpose
- relevant project brief, roadmap, issue, or prior decision
- known constraints and non-goals

Expected output:

- clarified problem
- suggested spec or ADR updates
- first useful delivery slice
- open decisions
- validation strategy

Human checkpoint:

- approve scope before implementation starts
- decide whether a spec or ADR is required

### 2. Write Or Update The Spec

Use `doc/specs/feature-spec-template.md` when the change affects user behavior, adopter workflow, repository governance, or delivery process.

The spec should define:

- context and goal
- in-scope and out-of-scope work
- user or maintainer scenarios
- AI usage boundaries
- acceptance criteria
- validation plan
- rollout and migration impact

Human checkpoint:

- confirm the acceptance criteria are checkable
- confirm the validation plan is realistic

### 3. Implement The Smallest Complete Change

Use `prompts/feature-implementation.md` after scope is clear.

AI may help with:

- inspecting relevant files
- proposing focused edits
- updating docs, prompts, templates, or code
- suggesting tests or validation commands
- summarizing risks and assumptions

AI should not decide:

- whether hidden scope should be added
- whether security or migration risk is acceptable
- whether validation evidence is sufficient
- whether a release is safe

Human checkpoint:

- review changed files before trusting the output
- remove speculative abstractions or unrelated changes

### 4. Review The Change

Use `prompts/code-review.md` when a diff, PR, commit range, or changed-file summary exists.

Review should check:

- correctness
- requirement fit
- adopter impact
- contract drift
- missing validation
- hidden assumptions
- migration or release risk

Human checkpoint:

- decide whether findings block merge
- confirm any deferred work is tracked

### 5. Verify Acceptance

Use `prompts/acceptance-qa.md` when implementation exists and the team needs acceptance confidence.

Validation evidence may include:

- automated checks
- manual walkthroughs
- documentation review
- example consistency checks
- release or rollback review

Human checkpoint:

- separate must-pass checks from nice-to-have checks
- record residual risk if accepting with follow-ups

### 6. Prepare Rollout Notes When Needed

Use `doc/process/rollout-notes-template.md` when the change affects adopters, users, maintainers, migration, release behavior, or operational risk.

Rollout notes should answer:

- who is affected
- what changes
- whether migration is required
- what validation happened
- how rollback or recovery works

Human checkpoint:

- decide release impact
- confirm migration guidance is clear

### 7. Capture Learning

Use `doc/process/retrospective-learning-notes-template.md` after meaningful delivery cycles or AI-assisted reviews.

Capture:

- what worked
- what did not work
- what AI handled well
- what needed human correction
- which prompts or templates should change

Human checkpoint:

- decide which lessons should update repository assets

## When To Use Each Prompt

| Situation | Prompt |
| --- | --- |
| Request is vague or too broad | `prompts/planning.md` |
| Scope is clear and implementation can start | `prompts/feature-implementation.md` |
| Diff or PR is ready for review | `prompts/code-review.md` |
| Implementation needs acceptance or QA evidence | `prompts/acceptance-qa.md` |

## Minimum Evidence Before Merge

Before merge, the reviewer should be able to answer:

- What spec, ADR, issue, or checklist justified this change
- What AI assistance was used
- What files changed and why
- What validation was run
- What remains unvalidated
- Whether the change affects adopters, migration, release notes, or rollback
- Whether follow-up work is tracked

## Escalation Points

Pause for explicit human decision when:

- scope expands beyond the spec
- migration cost appears
- security, privacy, or permission risk appears
- validation cannot be completed
- AI output conflicts with repository guidance
- release impact is unclear
- a change may alter the minimum template contract
