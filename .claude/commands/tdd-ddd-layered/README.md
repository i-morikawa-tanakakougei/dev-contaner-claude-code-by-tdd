# TDD/DDD/Layered Architecture Commands

This directory contains custom commands for implementing features using Test-Driven Development (TDD), Domain-Driven Design (DDD), and Layered Architecture.

## Command Workflow

1. **`/init-project-structure`** - Initialize project structure
2. **`/create-use-case <issue-number>`** - Create Given-When-Then specification
3. **`/domain-modeling <issue-number>`** - Design domain model
4. **`/create-tests <issue-number>`** - Create TDD tests (RED phase)
5. **`/implement-domain <issue-number>`** - Implement domain layer (GREEN phase)
6. **`/implement-usecase <issue-number>`** - Implement application layer
7. **`/implement-infra <issue-number>`** - Implement infrastructure layer
8. **`/implement-presentation <issue-number>`** - Implement presentation layer
9. **`/refactor <issue-number>`** - Refactor code (REFACTOR phase)
10. **`/run-all-tests <issue-number>`** - Run all tests and generate report

## Common Guidelines

### When referencing GitHub issues:
- Always prioritize the most recent comments over older ones and the original issue description
- If there are conflicts between the issue content and newer comments, prioritize the newer comments
- Use `gh issue view <issue-number>` to get complete issue details including all comments

### Output language:
- Command instructions are in English
- User-facing output (specifications, design documents, error messages) must be in Japanese

### File organization:
- Use case specifications: `docs/use_cases/`
- Domain models: `docs/domain/`
- Test plans: `docs/test_plan/`
- Test reports: `docs/test_report/`

## Usage Example

```bash
# Start with a GitHub issue
/create-use-case 123

# Follow the workflow
/domain-modeling 123
/create-tests 123
/implement-domain 123
# ... continue with other steps
```