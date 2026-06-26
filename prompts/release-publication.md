# Release Publication Prompt

Use this prompt when preparing a versioned release of this template.

The prompt helps draft release notes, migration summaries, announcement text, and publication checklists. It does not replace maintainer approval.

## When To Use

Use this prompt when:

- a release scope has been drafted
- changed files or commits are available for review
- maintainers need adopter-facing release notes
- migration or upgrade impact is uncertain
- publication evidence needs to be organized

Do not use this prompt to decide a version without human review.

## Inputs To Provide

Provide:

- proposed version
- commit range, PR list, or changed-file summary
- release goal
- known breaking changes or migration notes
- contract changes, if any
- validation already run
- intended distribution channel
- target audience for announcement

## Prompt

```text
You are helping prepare a release publication package for a reusable, stack-agnostic AI-driven SDLC template.

Release context:
- Proposed version:
- Commit range or PR list:
- Release goal:
- Intended distribution channel:
- Known breaking changes:
- Known migration notes:
- Contract changes:
- Validation already run:
- Target announcement audience:

Relevant changed files or summaries:
[paste changed-file list, release draft, or important diffs]

Please produce:
1. Recommended SemVer classification and reasoning
2. Adopter-facing release summary
3. Change categories grouped by adopter impact
4. Required migration notes
5. Optional upgrade guidance
6. Contract impact summary for Level 1, Level 2, and Level 3 adopters
7. Validation evidence summary and missing evidence
8. Release announcement draft
9. Publication checklist with pre-publish, publish, and post-publish steps
10. Human approval questions that must be answered before release

Use these repository references:
- `doc/process/versioning-and-releases.md`
- `doc/process/release-checklist.md`
- `doc/process/release-publication-guide.md`
- `doc/process/distribution-channels.md`
- `doc/process/adopter-upgrade-path.md`
- `doc/process/release-announcement-template.md`
- `doc/process/release-dry-run.md`

Separate confirmed facts from assumptions.
Do not claim validation was run unless evidence is provided.
Do not approve publication; state what humans must confirm.
```

## Expected Output

The response should include:

- version reasoning
- adopter impact summary
- migration summary
- validation evidence
- release announcement draft
- publication checklist
- human approval boundary

## Human Review Boundary

Humans must approve:

- final version
- release scope
- migration requirements
- release notes and announcement text
- publication timing
- whether validation evidence is sufficient
- whether adopters should be advised to upgrade immediately or defer
