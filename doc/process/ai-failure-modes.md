# AI Failure Modes

Use this guide during planning, implementation, review, and retrospectives.

The goal is to help reviewers catch common AI-assisted delivery failures before they become merged work.

## Failure Mode Index

| Failure Mode | What It Looks Like | Reviewer Response | Prompt Prevention |
| --- | --- | --- | --- |
| Hidden assumptions | The change depends on facts, users, commands, or constraints that were never confirmed. | Ask for the assumption to be named, verified, or removed. | Require the AI to separate confirmed facts from assumptions. |
| Requirement drift | The output solves a different problem than the spec. | Compare the change to the goal, scope, and acceptance criteria. | Include the spec and out-of-scope list in the prompt. |
| Over-scaffolding | The AI adds broad abstractions, directories, helpers, or workflows that are not needed for the slice. | Remove speculative structure or defer it to a follow-up spec. | Ask for the smallest complete change and ban speculative abstractions. |
| Fake validation | The response claims validation happened without commands, evidence, or check results. | Require exact commands, manual checks, or an explicit validation gap. | Ask for validation performed, validation not performed, and why. |
| Stale documentation | Docs are updated inconsistently or still describe older behavior. | Check README, contracts, prompts, specs, and examples together. | Ask the AI to list docs that might need synchronized updates. |
| Stack overfitting | A stack-specific rule becomes implied as a universal template requirement. | Move stack-specific guidance into the appropriate adoption section. | Remind the AI that this repository is stack-agnostic. |
| Migration impact missed | Renames, removals, or contract changes lack upgrade guidance. | Require migration notes, release impact, or rollback path. | Ask for adopter impact and migration cost explicitly. |
| Contract drift | Written guidance and `.github/template-contract.json` disagree. | Run the contract validator and inspect Level 1/2/3 changes. | Tell the AI to update docs and manifest together. |
| Review theater | The review summarizes the change but does not identify risks or evidence gaps. | Request findings first, ordered by severity. | Use `prompts/code-review.md` and require file or line references. |
| Unowned follow-up | Risks are acknowledged but no owner or tracking location exists. | Require owner, issue, milestone, or explicit acceptance of residual risk. | Ask for deferred work and tracking location. |

## Human Review Checkpoints

Reviewers should pause when:

- the AI output changes files outside the requested scope
- a validation claim lacks evidence
- the implementation contradicts a spec, ADR, or contract level
- adopter impact is not discussed for template-facing changes
- the change introduces a new stack assumption
- rollback, migration, or release impact is unclear

## Prompt Hardening Checklist

Before using an AI prompt, include:

- repository purpose
- relevant spec, ADR, issue, or roadmap section
- in-scope and out-of-scope work
- files AI may change
- files AI should not change without approval
- validation commands
- expected manual checks
- known risks and non-goals

## Retrospective Questions

After an AI-assisted change, ask:

- What did the AI assume incorrectly
- Which prompt instruction prevented a problem
- Which prompt instruction was missing
- Which review step caught the most important issue
- Which template or checklist should be updated
- Which validation gap should become automated
