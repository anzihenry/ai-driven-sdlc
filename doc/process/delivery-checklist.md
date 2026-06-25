# Delivery Checklist

Use this checklist before merging AI-assisted work.

The goal is to confirm that the change is scoped, reviewable, validated, and clear for future adopters or maintainers.

## Spec And Scope

- [ ] Requirement, issue, spec, or ADR is linked
- [ ] Goal is explicit
- [ ] In-scope work is clear
- [ ] Out-of-scope work is clear
- [ ] Acceptance criteria are checkable
- [ ] Success or completion signal is named

## Adopter Or User Impact

- [ ] Affected users, adopters, or maintainers are identified
- [ ] User-facing or adopter-facing behavior changes are documented
- [ ] Documentation updates are included or intentionally deferred
- [ ] Support, onboarding, or workflow impact is understood
- [ ] Release notes are planned if the change affects downstream users

## Migration And Compatibility

- [ ] Migration cost is assessed
- [ ] Backward compatibility impact is documented
- [ ] Removed or renamed files, APIs, docs, or workflows are called out
- [ ] Required upgrade steps are documented when applicable
- [ ] Breaking-change label or version impact is considered

## AI Usage And Human Review Boundary

- [ ] AI assistance used is disclosed
- [ ] Files or areas changed by AI are reviewed by a human
- [ ] AI-generated assumptions are documented or removed
- [ ] Hidden assumptions are named and either verified or accepted explicitly
- [ ] Human reviewer challenged correctness, security, and requirement fit
- [ ] Work that requires human judgment was not delegated blindly to AI

## Implementation Quality

- [ ] Changed files match the requested scope
- [ ] Existing behavior is preserved unless the spec changes it
- [ ] Error handling or failure behavior is considered
- [ ] Security, privacy, and permissions are considered
- [ ] Observability or audit needs are considered
- [ ] No speculative abstraction or unrelated refactor was introduced

## Validation Evidence

- [ ] Automated checks were run and results are recorded
- [ ] Manual verification was completed when needed
- [ ] Automated and manual validation boundaries are clear
- [ ] Documentation was reviewed for consistency
- [ ] Examples, prompts, or templates were exercised when relevant
- [ ] Validation claims include evidence, not only assertions
- [ ] Known validation gaps are explicitly documented
- [ ] Residual risk is acceptable to the reviewer

## Rollout, Rollback, And Follow-Up

- [ ] Rollout path is clear
- [ ] Rollback or recovery path is clear when applicable
- [ ] Follow-up work is captured with owner or tracking location
- [ ] Deferred work is intentional and visible
- [ ] Release or migration notes are prepared when needed
- [ ] Retrospective learning notes are planned if AI assistance revealed reusable workflow lessons

## Final Review

- [ ] Pull request summary explains what changed and why
- [ ] Reviewer can trace the change back to the spec, ADR, or issue
- [ ] Reviewer can trace validation evidence back to acceptance criteria
- [ ] Maintainer impact is clear
- [ ] The change is ready to merge
