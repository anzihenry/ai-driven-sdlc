# Good Review Request Example

This example shows how to ask an AI assistant to review a template validation change.

```text
Review this change with a production-minded code review lens.

Repository context:
- Repository purpose: reusable, stack-agnostic AI-driven SDLC template
- Relevant spec or roadmap context:
  - Phase 3 validates example adoption paths
  - example walkthroughs should match the repository structure they describe
- Expected validation:
  - python3 .github/scripts/validate_template_contract.py
  - PYTHONPYCACHEPREFIX=/private/tmp/python-pyc-cache python3 -m py_compile .github/scripts/validate_template_contract.py

Change under review:
The change adds example_docs to .github/template-contract.json and extends .github/scripts/validate_template_contract.py so local path references in example docs must exist.

Focus on:
- Bugs or incorrect behavior
- False positives in local path detection
- False negatives for missing example references
- Portability or adopter-impact risks
- Missing tests, docs, examples, or validation
- Requirement drift from Phase 3 validation goals
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
