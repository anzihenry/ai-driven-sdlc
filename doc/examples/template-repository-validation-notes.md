# Template Repository Validation Notes

These notes validate the example adoption path in `doc/examples/template-repository-adoption.md`.

The goal is to confirm whether a maintainer can follow the documented path without hidden assumptions.

## Validation Context

- Example path: `doc/examples/template-repository-adoption.md`
- Repository type: Documentation or template repository
- Adoption level: Level 2 recommended team adoption
- Validation method: Manual walkthrough against current repository docs and contract validator
- Validation date: YYYY-MM-DD

## What Was Clear

- The adoption level can be chosen from `doc/process/minimum-template-contract.md`
- The repository type can be chosen from `doc/process/multi-stack-adoption.md`
- The `src/` guidance is flexible enough for documentation or template repositories
- The prompt flow is discoverable through `prompts/README.md`
- The contract validator provides a concrete automated check for retained template surfaces

## What Required Human Judgment

- Whether a downstream team should choose Level 2 or Level 3 adoption
- Whether `src/README.md` should be retained, rewritten, or removed
- Which release automation surfaces should be kept by a specific downstream repository
- Which prompt risks matter most for a downstream team's workflow
- Whether a change is adopter-facing enough to require rollout notes

## Checks That Can Be Automated

- Contract validator passes:

```sh
python3 .github/scripts/validate_template_contract.py
```

- Example documents are present and non-empty
- Local file references in example documents resolve
- `doc/process/minimum-template-contract.md` and `.github/template-contract.json` stay synchronized
- Retained prompts and process docs remain listed in the contract manifest

## Checks That Should Stay Manual

- Whether the example scenario is still representative
- Whether the walkthrough gives enough context for a real adopter
- Whether prompt guidance is too generic or too stack-specific
- Whether rollout and migration guidance matches downstream adoption impact
- Whether deferred template surfaces are intentionally excluded

## Hidden Assumptions Found

- The example assumes the downstream repository retains `.github/scripts/validate_template_contract.py`
- The example assumes maintainers can decide adoption level before choosing repository type
- The example assumes documentation or template repositories still need release and migration notes

These assumptions are acceptable for the first example, but future examples should test different adoption levels and repository types.

## Gaps To Consider Later

- Add automated local-path validation for example documents
- Add a second example for a frontend or backend repository if Phase 3 needs broader stack coverage
- Add a checklist version of the example if adopters need a shorter execution artifact

## Phase 3 Exit Standard Check

- Can a maintainer follow the chosen example path from repository docs alone: Yes
- Are hidden assumptions identified: Yes
- Does the example avoid turning the repository into a sample app monorepo: Yes
- Does the example prove at least one adoption path: Partially, pending automated example consistency checks

## Validation Result

The documentation or template repository adoption path is usable as the first Phase 3 example.

Phase 3 should continue by adding lightweight CI checks that protect example consistency without coupling the repository to a specific application stack.
