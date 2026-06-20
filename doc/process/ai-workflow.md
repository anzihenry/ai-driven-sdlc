# AI Collaboration Workflow

This document describes a simple default workflow for AI-assisted delivery.

## 1. Frame The Work

- Start from a project brief or feature spec
- Make goals, scope, and acceptance criteria explicit
- Identify unknowns before implementation begins

## 2. Ask AI For Structured Output

Good prompts usually include:

- Current context
- Constraints
- Expected output format
- Definition of done
- Files or modules that may be changed

## 3. Review Before Merge

Check the AI output for:

- Requirement drift
- Hidden assumptions
- Security or privacy issues
- Missing edge cases
- Test coverage gaps

## 4. Capture Decisions

If the implementation changes architecture, dependencies, or operating cost, add or update an ADR.

## 5. Close The Loop

After shipping:

- Record what worked
- Record what needed manual correction
- Refine prompts for the next iteration
