# Acceptance And QA Prompt

Use this prompt after a spec exists, or after implementation, to produce a focused acceptance and quality review plan.

Replace bracketed placeholders before use.

```text
You are helping verify whether a change satisfies its spec.

Goal:
[Describe the feature, fix, template change, or repository workflow change.]

Spec context:
[Paste or link the relevant feature spec, project brief section, ADR, or release note.]

Implementation context:
- Changed files or PR: [diff, commit range, PR link, or summary]
- Validation already run: [commands and results]
- Known risks or constraints: [list]

Review constraints:
- Derive checks from the spec, not from assumptions.
- Separate must-pass acceptance checks from nice-to-have quality checks.
- Include manual checks only when automation cannot reasonably cover the behavior.
- Call out missing evidence clearly.
- Flag any spec ambiguity that blocks confident acceptance.

Tasks:
1. Extract acceptance criteria from the spec.
2. Turn each criterion into concrete checks.
3. Identify automated tests, manual walkthroughs, documentation checks, and release checks.
4. Compare existing validation evidence with required evidence.
5. List blockers, follow-ups, and residual risks.

Expected output:
- Acceptance checklist
- QA scenarios
- Required automated checks
- Required manual checks
- Documentation and release checks
- Missing evidence
- Acceptance recommendation: accept, accept with follow-ups, or block
```
