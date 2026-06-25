# Adoption Walkthrough

This walkthrough shows one realistic path for adopting the AI-Driven SDLC Template in a downstream repository.

It assumes the adopting team wants the recommended team adoption level from `doc/process/minimum-template-contract.md`.

## Outcome

By the end of this walkthrough, the downstream repository should have:

- a clear project brief
- at least one usable feature spec
- AI implementation and review prompts that fit the team workflow
- GitHub issue and PR templates that match the team's process
- CI or manual checks that validate the retained template surfaces

## Step 1: Choose The Adoption Level

Start with the contract in `doc/process/minimum-template-contract.md`.

Recommended default:

- Use Level 1 for lightweight experiments or solo projects
- Use Level 2 for most team repositories
- Use Level 3 when release and label automation should be preserved

Record the chosen level in the downstream repository's `README.md` or contribution guide.

## Step 2: Remove Placeholder Ownership

Before inviting contributors, update or remove repository-specific placeholders:

- configure `.github/CODEOWNERS` or remove it if CODEOWNERS is not used
- update `.github/ISSUE_TEMPLATE/config.yml` only if contact links are needed
- replace generic wording in `README.md` with the downstream project context
- update `CONTRIBUTING.md` so it describes the real review and validation flow

This step is complete when no contributor-facing file implies a fake organization, owner, repository, or support path.

## Step 3: Fill The Project Brief

Use `doc/specs/project-brief.md` to capture the project context before feature work begins.

Minimum acceptable brief:

- the product or system is described in plain language
- target users and primary jobs are named
- at least three desired outcomes are listed
- non-goals and constraints are explicit
- success signals are concrete enough to review later

The brief does not need to be long. It does need to be specific enough that an AI agent and a human reviewer can tell what belongs in the project.

## Step 4: Decide How The Repository Uses `src/`

This template does not require one source layout.

Choose one approach:

- put real product code in `src/`
- reserve `src/` for examples or shared conventions
- replace `src/README.md` with stack-specific guidance

Document the choice in the downstream `README.md`. If the team keeps code outside `src/`, say where the code lives instead.

## Step 5: Create The First Feature Spec

Use `doc/specs/feature-spec-template.md` for the first real feature.

The first spec should include:

- the user or team problem
- in-scope and out-of-scope behavior
- acceptance criteria that can be checked
- validation steps for the expected implementation
- AI usage expectations and review notes

Keep the first feature small. A thin but complete slice is more useful than a broad plan with no verification path.

## Step 6: Adapt The Prompts

Review the prompts in `prompts/` before using them for implementation or review.

At minimum, update prompt usage notes so they mention:

- the repository structure that matters to the task
- the validation commands the team expects
- the files or areas the AI agent may change
- the risks reviewers should pay attention to

Do not treat prompts as static policy. They should improve as the team learns which instructions produce reliable work.

## Step 7: Align GitHub Automation

For Level 2 or Level 3 adoption, check the GitHub configuration:

- confirm issue templates match the team's intake process
- confirm the PR template asks for the right validation evidence
- confirm labels match release and review habits
- extend Dependabot only for package ecosystems the repository actually uses
- extend CI only with checks the team can run consistently

If a workflow is retained but not used, either configure it or remove it intentionally.

## Step 8: Run Adoption Checks

Before declaring adoption complete, run the template contract validator if it is retained:

```sh
python3 .github/scripts/validate_template_contract.py
```

Then manually confirm:

- core docs are no longer generic placeholders
- the first feature spec can guide implementation
- prompts can be used without heavy rewriting
- retained automation reflects the real repository
- removed template surfaces were removed intentionally

## Completion Signal

Adoption is complete when a new contributor can open the repository and understand:

- what the project is
- how feature work is specified
- how AI-assisted implementation should be requested
- how review and validation should happen
- which template surfaces are intentionally retained, customized, or removed
