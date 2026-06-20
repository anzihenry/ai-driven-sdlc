# Code Review Prompt

Use this prompt when asking an AI assistant to review a change.

```text
Review this change with a production-minded code review lens.

Focus on:
- Bugs
- Behavioral regressions
- Security risks
- Performance risks
- Missing tests

Instructions:
- List findings first, ordered by severity
- Include file and line references when possible
- Keep summaries brief
- If no issues are found, say that explicitly and mention residual risk
```
