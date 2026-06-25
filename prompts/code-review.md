# Code Review Prompt

Use this prompt when asking an AI assistant to review a change before merge.

Replace bracketed placeholders before use.

```text
Review this change with a production-minded code review lens.

Repository context:
- Repository purpose: [summarize the project or template]
- Relevant spec, brief, or ADR: [link or paste context]
- Expected validation: [commands or manual checks]

Change under review:
[Paste diff, PR link, commit range, or changed-file summary.]

Focus on:
- Bugs or incorrect behavior
- Behavioral regressions
- Security, privacy, or permission risks
- Portability or adopter-impact risks
- Performance or reliability risks
- Missing tests, docs, examples, or validation
- Requirement drift from the spec
- Unclear assumptions or hidden migration cost

Instructions:
1. List findings first, ordered by severity.
2. Include file and line references when possible.
3. Explain why each finding matters and what would make it safe to merge.
4. Keep summaries brief.
5. If no issues are found, say that explicitly and mention residual risk.

Severity guide:
- P0: Blocks release or causes severe user/adopter harm
- P1: Should fix before merge
- P2: Important but can be follow-up if acknowledged
- P3: Minor polish or clarity issue

Response format:
Findings:
- [severity] [file:line] Finding and impact

Open questions:
- [question]

Validation gaps:
- [gap]

Summary:
[brief overall assessment]
```
