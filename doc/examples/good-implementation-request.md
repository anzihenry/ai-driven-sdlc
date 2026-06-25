# Good Implementation Request Example

This example shows how to ask an AI coding agent to implement a scoped template change.

```text
You are working in the AI-Driven SDLC Template repository.

Goal:
Add lightweight validation that catches broken local file references in example adoption documents.

Repository context:
- Repository purpose: reusable, stack-agnostic AI-driven SDLC template
- Relevant files:
  - .github/template-contract.json
  - .github/scripts/validate_template_contract.py
  - doc/examples/template-repository-adoption.md
  - doc/examples/template-repository-validation-notes.md
- Existing conventions to preserve:
  - use Python standard library only
  - keep CI stack-agnostic
  - keep examples lightweight and documentation-first

Spec context:
Use the Phase 3 validation goal: example walkthroughs should match the repository structure they describe.

Scope:
- In scope:
  - add an example_docs list to .github/template-contract.json
  - update validate_template_contract.py to check local path references in example docs
  - update validator success output to mention example references
- Out of scope:
  - markdown linting
  - external URL checks
  - adding sample applications

Implementation constraints:
- Keep changes scoped to example consistency validation.
- Do not add third-party dependencies.
- Do not change adoption levels unless required.
- Explain any assumption about what counts as a local path.

Tasks:
1. Inspect current contract validation logic.
2. Implement the smallest local-path reference check.
3. Run the validator.
4. Run Python syntax validation.
5. Summarize changed files, validation results, assumptions, and remaining risks.

Validation expected:
- Automated checks:
  - python3 .github/scripts/validate_template_contract.py
  - PYTHONPYCACHEPREFIX=/private/tmp/python-pyc-cache python3 -m py_compile .github/scripts/validate_template_contract.py
- Manual checks:
  - confirm command snippets are not treated as file paths
  - confirm local path references in example docs resolve

Definition of done:
- Current example docs pass validation.
- Missing example path references would fail validation.
- No stack-specific dependencies are introduced.

Response format:
- Summary of what changed
- Validation performed
- Risks or follow-ups
```
