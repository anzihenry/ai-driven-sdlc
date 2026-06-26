# Prompt Pack Guide

This folder contains reusable prompts for AI-assisted planning, implementation, review, and acceptance.

Use these prompts as working templates. Downstream teams should adapt repository context, validation commands, risk areas, and expected output before using them.

## Prompt Flow

Use the prompts in this order for a typical delivery cycle:

1. `planning.md`
2. `feature-implementation.md`
3. `code-review.md`
4. `acceptance-qa.md`

For template adoption work, use `template-adoption.md` before the delivery cycle to choose an adoption level, file plan, and validation path.

The flow is not mandatory. Choose the prompt that matches the current state of the work.

## Prompt Index

| Prompt | Use When | Required Input | Expected Output |
| --- | --- | --- | --- |
| `template-adoption.md` | A new or existing repository needs a concrete plan for adopting this template. | Repository purpose, current tree or relevant files, desired adoption level if known, constraints, existing CI or release process. | Adoption level recommendation, file action plan, stack-variable decisions, risks, validation plan, completion checklist. |
| `planning.md` | The request is still ambiguous and needs to become specs, roadmap items, or implementation tasks. | Rough request, repository context, known constraints, existing decisions. | Problem framing, scope recommendation, proposed specs or tasks, first useful slice, open decisions, validation strategy. |
| `feature-implementation.md` | A spec or clear task exists and an AI coding agent should implement a scoped change. | Goal, relevant files, spec context, in/out scope, validation expectations, definition of done. | Implemented change summary, validation performed, assumptions, risks, follow-ups. |
| `code-review.md` | A diff, PR, commit range, or changed-file summary is ready for review. | Repository context, relevant spec or ADR, expected validation, change under review. | Findings ordered by severity, open questions, validation gaps, concise review summary. |
| `acceptance-qa.md` | A spec and implementation exist and the team needs acceptance or QA confidence. | Spec context, changed files or PR, validation already run, known risks. | Acceptance checklist, QA scenarios, required automated/manual checks, missing evidence, acceptance recommendation. |

## Boundary Rules

- Use `planning.md` before implementation when scope, users, acceptance, or ownership is unclear.
- Use `template-adoption.md` before planning when the question is how to adopt this template into a repository.
- Use `feature-implementation.md` only after the desired change can be stated as a small complete slice.
- Use `code-review.md` when there is concrete output to review, such as a diff or changed-file summary.
- Use `acceptance-qa.md` when the question is whether the implementation satisfies the spec.
- Do not use prompts as policy by themselves. The project brief, feature spec, ADRs, and delivery checklist remain the source of truth.

## Inputs To Prepare

Before using any prompt, gather the smallest useful context:

- repository purpose
- relevant spec, ADR, issue, or roadmap section
- files or directories likely to change
- validation commands or manual checks
- constraints, risks, and known non-goals

If this information is missing, use `planning.md` first.

## Output Quality Bar

A good AI response should:

- distinguish facts from assumptions
- keep scope small and reviewable
- name validation evidence
- call out human decisions
- avoid unrelated refactors or speculative abstractions
- preserve adopter-facing compatibility unless a spec says otherwise

## Maintenance Notes

Update this guide when adding, renaming, or changing prompts.

When a prompt becomes part of the recommended adoption surface, update `.github/template-contract.json` and `doc/process/minimum-template-contract.md` in the same change.
