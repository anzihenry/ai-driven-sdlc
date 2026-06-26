# Distribution Channels

Use this guide to decide how this template should be distributed to downstream adopters.

The right channel depends on how much upgrade continuity, repository independence, and release traceability the adopter needs.

## Channel Summary

| Channel | Best For | Tradeoff |
| --- | --- | --- |
| GitHub template repository | New repositories that want a clean starting point | Easy start, but no automatic upgrade relationship |
| Fork | Teams that want visible upstream history | Keeps lineage, but may inherit repository noise |
| Release archive | Teams that need a stable snapshot | Easy to pin, but upgrades are manual |
| Tag-based adoption | Teams that want repeatable version references | Requires adopters to track template version and diffs |
| Manual sync | Existing repositories adopting selected surfaces | Flexible, but easiest to drift without notes |

## GitHub Template Repository

Use this when:

- the adopter is starting a new repository
- the team wants a clean history
- the template is used as a starting point, not a tracked dependency

Adopter responsibilities:

- record the source template version or tag in the adoption PR
- run the contract validator after copying
- customize project identity files immediately
- decide whether future upgrades will be manual or tag-based

## Fork

Use this when:

- the adopter wants visible upstream relationship
- template updates may be merged or compared over time
- the downstream repository can tolerate upstream history

Adopter responsibilities:

- document which upstream branch or tag was used
- decide how upstream changes will be reviewed before merging
- avoid accepting template changes that conflict with local project decisions

## Release Archive

Use this when:

- an organization needs a stable downloadable snapshot
- adoption happens outside GitHub template workflows
- a release artifact needs to be attached to internal process or approval

Adopter responsibilities:

- keep the release tag with adoption records
- review migration notes before applying a newer archive
- preserve or replace the minimum template contract intentionally

## Tag-Based Adoption

Use this when:

- downstream teams need to pin a known template version
- maintainers publish meaningful release notes and migration guidance
- upgrades are reviewed as explicit changes

Adopter responsibilities:

- record the adopted tag
- compare the current repository against the target tag before upgrading
- apply migration notes and run validation after upgrade

## Manual Sync

Use this when:

- the target repository already exists
- only selected docs, prompts, or process assets are needed
- adopting all automation would disrupt existing workflows

Adopter responsibilities:

- list copied files and intentionally skipped surfaces
- preserve equivalent Level 1 workflow coverage
- document any contract deviations
- repeat the decision tree when considering future template updates

## Maintainer Recommendations

- Publish every meaningful template version with a tag and release notes.
- Prefer tag-based references for teams that expect upgrades.
- Treat GitHub template creation as a starting path, not an upgrade mechanism.
- Use migration notes when a release changes adopter-facing behavior.
- Keep distribution guidance stack-agnostic; stack-specific commands belong in adopting repositories.
