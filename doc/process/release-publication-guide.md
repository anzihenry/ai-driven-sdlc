# Release Publication Guide

Use this guide when publishing a versioned release of this template.

This guide starts after the release scope is already understood. Use `doc/process/versioning-and-releases.md` first when choosing the version.

## Publication Principles

- Publish for downstream adopters, not only maintainers.
- Release notes should explain impact, migration, validation, and upgrade path.
- Automation may create tags and GitHub Releases, but humans approve version, content, and adopter messaging.
- Every release should be traceable to a validated repository state.

## Before Publishing

Complete these checks before creating a tag or GitHub Release:

- [ ] Version is selected using `doc/process/versioning-and-releases.md`
- [ ] Release checklist is complete
- [ ] Release dry run is complete or explicitly waived
- [ ] Template contract validator passes
- [ ] Migration notes exist if adopters must take action
- [ ] Release announcement draft exists for adopter-facing communication
- [ ] Distribution channel is chosen
- [ ] Known risks and rollback or follow-up decisions are documented

Suggested validation command:

```sh
python3 .github/scripts/validate_template_contract.py
```

## Publishing

Use the repository's manual release workflow only after the pre-publish checks are complete.

The manual workflow should:

- create the version tag
- create the GitHub Release
- generate initial release notes when supported

The manual workflow should not:

- choose the version
- approve release content
- decide migration impact
- decide whether adopters should upgrade

After the release is created:

- review generated release notes
- replace vague internal change descriptions with adopter-facing impact
- link migration notes when applicable
- link validation evidence or dry-run notes
- confirm the tag points to the intended commit

## After Publishing

Complete these steps after the GitHub Release exists:

- [ ] Publish or share the release announcement
- [ ] Confirm release notes include adopter impact
- [ ] Confirm migration notes are linked when needed
- [ ] Confirm distribution guidance matches the release
- [ ] Record any post-release issues or follow-up work
- [ ] If the release is breaking, verify upgrade guidance is clear enough for a downstream maintainer

## Publication Evidence

Each release should leave behind:

- version tag
- GitHub Release
- release notes
- validation command and result
- dry-run result or waiver
- migration notes if required
- announcement text or link
- follow-up tracking if needed

## Stop Conditions

Do not publish yet if:

- the version decision is unclear
- contract validation fails
- migration impact is unknown
- release notes only describe internal edits
- no one has reviewed adopter-facing impact
- the target commit is not the intended release state

Pausing before publication is cheaper than publishing a release that adopters cannot interpret.
