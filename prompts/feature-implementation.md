# Feature Implementation Prompt

Use this prompt when asking an AI coding agent to implement a scoped feature or repository change.

Replace bracketed placeholders before use.

```text
You are working in an existing repository.

Goal:
[Describe the smallest complete change to implement.]

Repository context:
- Repository purpose: [summarize the project or template]
- Relevant files or directories: [list paths]
- Existing conventions to preserve: [style, architecture, docs, tests, workflow]

Spec context:
[Link to or paste the relevant feature spec, project brief section, or ADR.]

Scope:
- In scope:
  - [item]
  - [item]
- Out of scope:
  - [item]
  - [item]

Implementation constraints:
- Keep changes scoped to the requested behavior.
- Preserve existing public behavior unless the spec explicitly changes it.
- Do not introduce speculative abstractions.
- Do not remove or rewrite unrelated user changes.
- Explain any assumption that affects behavior, adoption, security, or release impact.

Tasks:
1. Inspect the current repository before editing.
2. Identify the files that need to change and briefly explain why.
3. Implement the smallest complete solution.
4. Add or update tests, docs, examples, or validation checks when appropriate.
5. Run the relevant validation commands.
6. Summarize changed files, validation results, assumptions, and remaining risks.

Validation expected:
- Automated checks: [commands]
- Manual checks: [walkthrough or review steps]
- Documentation checks: [docs or prompts to verify]

Definition of done:
- [criterion]
- [criterion]
- [criterion]

Response format:
- Summary of what changed
- Validation performed
- Risks or follow-ups
```
