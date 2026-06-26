# Release Dry Run

Use this guide before publishing a versioned template release.

The goal is to confirm release readiness without creating a Git tag or GitHub Release.

## When To Run A Dry Run

Run a release dry run before:

- the first public release
- any major release
- any release that changes adoption levels or contract-governed files
- any release that requires migration notes
- any release where version impact is unclear

## Dry Run Inputs

Gather:

- candidate version:
- target branch or commit:
- included PRs or commits:
- draft release notes:
- related specs, ADRs, or rollout notes:
- migration notes, if required:

## Step 1: Confirm Repository State

Run:

```sh
git status --short --branch
python3 .github/scripts/validate_template_contract.py
```

Confirm:

- `main` or the target branch is stable
- contract validation passes
- no unrelated local changes are included
- example docs still reference real local paths

## Step 2: Choose Version Impact

Use `doc/process/versioning-and-releases.md`.

Confirm:

- patch, minor, or major impact
- adopter-facing impact
- contract level changes
- breaking change test result
- labels match the selected version bump

## Step 3: Review Release Notes

Release notes should explain:

- what changed
- why it matters
- who is affected
- whether migration is required
- which docs, prompts, examples, or workflows changed
- any known risks or deferred follow-ups

Avoid release notes that only describe maintainer-internal file changes.

## Step 4: Check Migration Notes

If downstream action is required, use `doc/process/migration-notes-template.md`.

Confirm:

- affected adoption levels are named
- old and new paths or workflows are clear
- migration steps are actionable
- validation after migration is documented
- rollback or compatibility notes are present

## Step 5: Review GitHub Release Workflow Inputs

The manual release workflow expects:

- version without leading `v`
- target branch or commit

Confirm:

- the intended tag does not already exist
- the target branch or commit is correct
- the version matches the release impact
- release notes are ready for review

## Step 6: Decide Go Or No-Go

Go only if:

- release checklist is complete
- version impact is clear
- CI and manual validation evidence are available
- migration notes exist when needed
- release notes explain downstream impact
- maintainers agree the target is releasable

If no-go, record:

- blocker:
- owner:
- follow-up:
- next dry-run date:

## Dry Run Result

- Result: Go / No-go
- Reviewed by:
- Date:
- Notes:
