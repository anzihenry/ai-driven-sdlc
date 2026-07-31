# AI Security And Permissions

Use this guide when AI tools can read repository content, suggest code, run commands, call external services, or change files.

The goal is to make security, privacy, and permission boundaries explicit before AI-assisted work begins.

## Boundary Principles

- Treat AI assistance as a delegated workflow, not an independent authority
- Give tools the minimum access needed for the current task
- Keep secrets, credentials, production data, and private customer data out of prompts and generated artifacts
- Require human approval for destructive, privileged, external, or release-affecting actions
- Prefer repository-local evidence over unverified memory or external assumptions
- Record security and permission decisions when they affect future workflow

## Data Handling Boundaries

AI tools should not receive or expose:

- production credentials, API keys, tokens, signing keys, or private certificates
- raw customer data, employee data, payment data, health data, or legal records unless the team has approved the handling path
- private incident details that are not needed for the task
- proprietary third-party code or content that the team is not allowed to process with the chosen tool
- environment files, logs, screenshots, or exports that may contain secrets

When sensitive data is relevant, use the smallest safe substitute:

- describe the shape of the data instead of pasting real records
- redact secrets before sharing logs
- use synthetic fixtures for examples and tests
- link to an internal approved source instead of copying restricted content into prompts
- ask a human owner before widening the data boundary

## Tool Permission Levels

Use the narrowest level that supports the work.

| Level | Access | Suitable For | Human Approval Needed |
| --- | --- | --- | --- |
| Read-only | Inspect files, docs, diffs, logs, and command output. | Planning, review, summarization, impact analysis. | When reading private or regulated data. |
| Workspace write | Edit files inside the repository or approved working directory. | Specs, docs, tests, implementation, examples. | When touching security-sensitive files, generated credentials, or release assets. |
| Command execution | Run local checks, tests, formatters, builds, or scripts. | Validation and repeatable local workflows. | When commands are destructive, privileged, networked, or unclear. |
| External service access | Use package registries, hosted APIs, issue trackers, cloud tools, or production-like systems. | Dependency work, CI triage, release publishing, incident review. | Before network access, writes, publishes, deletes, or permission changes. |
| Release authority | Tag, publish, deploy, merge, or announce. | Versioned releases and production delivery. | Always. |

## Command Execution Rules

Before running a command, identify:

- what the command reads
- what the command writes
- whether it can delete, overwrite, publish, install, or deploy
- whether it uses the network
- whether it depends on secrets or local user state
- how to verify the result

Safe default commands usually include:

- repository-local searches and file inspection
- lint, test, and validation commands documented by the repository
- dry-run commands that do not write outside the workspace
- formatting commands when the affected files are already in scope

Require explicit human approval before:

- deleting files or history
- resetting, force-pushing, rewriting tags, or changing protected branches
- installing dependencies from the network
- running scripts with unclear side effects
- changing permissions, ownership, signing, deployment, or release configuration
- accessing production systems or customer data

## File Change Boundaries

AI-assisted changes should stay inside the agreed scope.

Before editing, confirm:

- which files or directories are in scope
- which generated files should be left alone
- whether docs, prompts, examples, tests, contracts, or release notes must be updated together
- whether changes affect adopters, migration, release behavior, or security posture

Escalate to human review when a change touches:

- authentication, authorization, encryption, secrets, signing, or sandboxing
- CI/CD credentials, deployment workflows, release automation, or package publishing
- dependency manifests or lockfiles
- license, compliance, privacy, or data retention guidance
- the minimum template contract or adopter-facing migration paths

## External Service Boundaries

AI tools should treat external systems as higher-risk than local files.

Before using an external service, define:

- the service being accessed
- whether the action is read-only or write-capable
- the identity or account being used
- the data that will be sent or retrieved
- the rollback or recovery path for write actions

Do not let AI tools publish, deploy, notify users, change access control, or mutate production-like systems without explicit human approval.

## Review Checklist

Before accepting AI-assisted work, reviewers should answer:

- Did the AI use only approved files, data, tools, and services
- Were secrets or sensitive data excluded or redacted
- Were privileged commands approved before execution
- Are security-sensitive changes linked to a spec, ADR, issue, or checklist
- Is validation evidence present and specific
- Are residual risks documented with an owner or explicit acceptance
- Do release, migration, rollback, or adopter-impact notes need updates

## Incident Response

If sensitive data or excessive permission was exposed to an AI tool:

1. Stop the workflow.
2. Preserve the relevant prompt, command, output, or diff for review if safe to do so.
3. Notify the repository owner or security contact.
4. Rotate exposed credentials or invalidate tokens when needed.
5. Remove leaked material from committed files, generated artifacts, logs, and issue or PR text.
6. Record the lesson in `doc/process/retrospective-learning-notes-template.md` or the team's incident process.
7. Update prompts, checklists, or tool permissions so the same failure is harder to repeat.

## Related Guidance

- Use `doc/process/ai-failure-modes.md` to catch common AI-assisted delivery mistakes.
- Use `doc/process/delivery-checklist.md` to confirm validation and review evidence.
- Use `doc/process/ai-delivery-operating-guide.md` to place this guidance inside the full delivery cycle.
- Use `doc/decisions/ADR-template.md` when a security or permission policy affects future work.
