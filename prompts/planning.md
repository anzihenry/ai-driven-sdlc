# Planning Prompt

Use this prompt when the request is still ambiguous and needs to become specs, roadmap items, or implementation tasks.

Replace bracketed placeholders before use.

```text
You are helping plan work in an existing repository.

Goal:
[Describe the idea, problem, opportunity, or rough request.]

Repository context:
- Repository purpose: [summarize the project or template]
- Current state: [known files, docs, modules, workflows, or constraints]
- Existing decisions to preserve: [ADRs, roadmap decisions, release policy, team conventions]
- Adoption level and repository type, if known: [Level 1/2/3 and type from multi-stack adoption guide]

Planning constraints:
- Keep the plan grounded in current repository state.
- Separate assumptions from confirmed facts.
- Prefer small, reviewable delivery slices.
- Do not propose implementation work that lacks an acceptance signal.
- Call out decisions that need human approval before coding.
- Call out hidden assumptions and missing validation evidence.

Tasks:
1. Inspect or summarize the current context.
2. Identify the real problem and likely users or stakeholders.
3. Split the work into specs, decisions, tasks, and follow-ups.
4. Recommend the smallest useful first slice.
5. List risks, unknowns, hidden assumptions, and validation needs.
6. Identify whether rollout notes or retrospective learning notes may be needed.
7. Suggest which prompt or template should be used next.

Expected output:
- Problem framing
- Scope recommendation
- Proposed specs or docs to create or update
- Suggested implementation slices
- Open decisions
- Hidden assumptions
- Validation strategy
- Follow-up artifacts to create
- Recommended next step

Context to include:
[Paste rough notes, user request, issue, meeting notes, or existing docs.]
```
