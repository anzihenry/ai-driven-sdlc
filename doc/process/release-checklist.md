# Release Checklist

Use this checklist whenever you are about to publish a versioned release.

## Scope

- [ ] Release goal is clear
- [ ] Included PRs are understood
- [ ] Version number matches the actual impact

## Quality

- [ ] `main` is in a releasable state
- [ ] Required CI checks passed
- [ ] Any manual verification is complete
- [ ] Open risks are documented

## Documentation

- [ ] Relevant specs or ADRs are updated
- [ ] Contributor-facing workflow changes are documented
- [ ] Release notes draft has been reviewed
- [ ] Breaking changes include migration notes

## Labeling

- [ ] Release-relevant PRs have correct labels
- [ ] `major` is present if the release is breaking
- [ ] `skip-changelog` is used only when appropriate

## Publish

- [ ] Correct version was entered into the `Release` workflow
- [ ] Correct target branch or commit was selected
- [ ] Git tag was created successfully
- [ ] GitHub Release entry was published successfully

## Post-Release

- [ ] Release output was spot-checked
- [ ] Follow-up issues were filed if needed
- [ ] Team communication was sent if the release matters operationally
