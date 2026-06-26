# Template Adoption Prompt

Use this prompt when you want an AI coding agent or planning assistant to help adopt this template into a new or existing repository.

## When To Use

Use this prompt when:

- a team has copied, forked, or is considering this template
- an existing repository needs an adoption plan
- the team is unsure which adoption level to choose
- template files need to be customized without losing the minimum contract

Do not use this prompt as a substitute for human ownership of project goals, contribution rules, or release policy.

## Inputs To Provide

Provide as much of the following as possible:

- repository purpose and audience
- whether this is a new or existing repository
- current repository tree or relevant file list
- current README, contribution guide, and CI workflow if they exist
- intended technology stack, if known
- desired adoption level if already chosen
- constraints, such as existing CI, release process, compliance, or team workflow
- what the team wants AI assistance to produce

## Prompt

```text
You are helping adopt a stack-agnostic AI-driven SDLC template into this repository.

Repository context:
- Purpose:
- Audience:
- New or existing repository:
- Repository type:
- Known technology stack:
- Existing CI or release process:
- Constraints:

Relevant files or tree:
[paste file list, tree, or important file contents]

Adoption goal:
[describe whether we want Level 1, Level 2, Level 3, or need help choosing]

Please produce:
1. Recommended adoption level and why
2. Recommended repository type and `src/` treatment
3. Files to keep as-is
4. Files to customize immediately
5. Files to defer or remove intentionally
6. Suggested edits to README, contribution guidance, project brief, prompts, and CI
7. Risks, hidden assumptions, and human decisions required
8. Validation commands or manual checks to run
9. A short adoption completion checklist

Use these template references when forming the plan:
- `doc/process/adopter-quickstart.md`
- `doc/process/adoption-decision-tree.md`
- `doc/process/minimum-template-contract.md`
- `doc/process/multi-stack-adoption.md`
- `doc/process/template-customization-checklist.md`
- `prompts/README.md`

Do not invent stack-specific commands unless the repository context supports them.
Separate universal template requirements from stack-variable choices.
If information is missing, state the smallest set of questions or assumptions needed to proceed.
```

## Expected Output

The AI response should include:

- adoption level recommendation
- file-by-file action plan
- stack-variable decisions
- validation plan
- human review boundaries
- adoption completion checklist

## Human Review Boundary

Humans must confirm:

- project purpose and audience
- adoption level
- source layout and stack conventions
- retained automation
- release and review expectations
- any accepted contract deviations

AI may suggest these decisions, but should not silently decide them.
