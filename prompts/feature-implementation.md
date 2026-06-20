# Feature Implementation Prompt

Use this prompt as a starting point when asking an AI coding agent to implement a feature.

```text
You are working in an existing repository.

Goal:
<describe the feature>

Context:
<link or paste the relevant feature spec>

Constraints:
- Keep changes scoped
- Do not break existing behavior
- Explain assumptions clearly

Tasks:
1. Inspect the current codebase before changing anything
2. Implement the smallest complete solution
3. Add or update tests when appropriate
4. Summarize changed files and remaining risks

Definition of done:
<list concrete acceptance criteria>
```
