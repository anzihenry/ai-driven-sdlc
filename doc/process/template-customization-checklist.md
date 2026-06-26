# Template Customization Checklist

Use this checklist after copying or forking the template and before calling adoption complete.

The checklist is written for downstream adopters. Maintainers can also use it during release dry runs.

## Adoption Choice

- [ ] Chosen adoption level is documented: Level 1, Level 2, or Level 3
- [ ] Repository type is documented
- [ ] `src/` treatment is documented: real source, examples only, reserved, or unused
- [ ] Stack-variable conventions are documented in `README.md` or `src/README.md`
- [ ] Intentional deviations from the template contract are listed

## Must Customize

- [ ] `README.md` describes the real project, audience, and usage path
- [ ] `CONTRIBUTING.md` reflects the real team workflow
- [ ] `doc/specs/project-brief.md` describes the actual project context
- [ ] `.github/CODEOWNERS` is updated or removed if CODEOWNERS is retained
- [ ] `.github/ISSUE_TEMPLATE/config.yml` contact links are updated or removed if retained
- [ ] `src/README.md` is updated if `src/` remains part of the repository surface

## Should Preserve Or Replace With Equivalents

- [ ] `doc/specs/feature-spec-template.md` or an equivalent spec format exists
- [ ] `doc/decisions/ADR-template.md` or an equivalent decision format exists
- [ ] `doc/process/ai-workflow.md` or an equivalent AI collaboration flow exists
- [ ] `doc/process/delivery-checklist.md` or an equivalent delivery checklist exists
- [ ] `prompts/feature-implementation.md` or an equivalent implementation prompt exists
- [ ] `prompts/code-review.md` or an equivalent review prompt exists

## May Remove If Unused

- [ ] Release Drafter configuration is removed if the team does not use release drafts
- [ ] Manual release workflow is removed if releases are managed elsewhere
- [ ] Label sync workflow is removed if labels are managed manually
- [ ] Dependabot configuration is removed if dependency automation is out of scope
- [ ] Issue templates are removed or simplified if the team uses another intake system
- [ ] Example docs are removed only if the team has an equivalent onboarding example

## Prompt Pack Setup

- [ ] `prompts/README.md` lists the prompts the team will actually use
- [ ] Planning prompt is available for ambiguous work
- [ ] Implementation prompt is available for scoped specs or tasks
- [ ] Review prompt is available for diffs, PRs, or commit ranges
- [ ] Acceptance or QA prompt is available for validation
- [ ] Prompt usage boundaries are understood by both AI users and human reviewers

## Automation Setup

- [ ] Contract validator runs locally
- [ ] CI runs contract validation if GitHub Actions are retained
- [ ] Retained workflows match the team's real process
- [ ] Stack-specific lint, test, build, or security checks are added only when relevant
- [ ] Removed automation is documented as intentionally excluded

## Validation Evidence

- [ ] Contract validator result is recorded
- [ ] First project brief review is complete
- [ ] First spec or planning artifact is created or intentionally deferred
- [ ] First AI prompt path is tested or ready to test
- [ ] Known gaps have owners or accepted residual risk

## Adoption Complete When

Adoption is complete only when:

- required project identity placeholders are gone
- retained template files are useful in the real repository
- removed template surfaces were removed intentionally
- the team can explain its adoption level
- validation evidence exists
- the next real delivery task has a clear starting prompt or process path
