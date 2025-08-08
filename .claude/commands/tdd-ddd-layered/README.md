# TDD/DDD/Layered Architecture Commands

This directory contains custom commands for implementing features using Test-Driven Development (TDD), Domain-Driven Design (DDD), and Layered Architecture.

## Development Process: Vision to Ticket Flow (Option 3)

This project adopts the **"Create core scenarios upfront, add and extend during sprints"** approach.

### Overall Flow

- Initial Phase
  - 00: Vision definition and core scenario creation
  - 01: Project structure initialization
  - 02: Sprint planning and ticket creation
- Sprint Execution Phase
  - 03-09: Use case specification → Domain design → TDD implementation (RED→GREEN) → Each layer implementation
  - 10: Run all tests
  - 11: Refactoring (REFACTOR)
- Scenario Evolution & Review Phase
  - 12: Scenario evolution (based on sprint feedback)
  - 13: Issue review implementation
  - 14: Feedback reflection
  - 15: PR creation and issue closing

### Initial Phase Commands

1. **`/create-vision`** - Define project vision and core scenarios (80% coverage)
2. **`/sprint-planning <sprint-number>`** - Plan sprint and create tickets from core scenarios
3. **`/init-project-structure`** - Initialize project structure

### Sprint Execution Commands

4. **`/create-use-case <issue-number>`** - Create Given-When-Then specification from issue
5. **`/domain-modeling <issue-number>`** - Design domain model
6. **`/create-tests <issue-number>`** - Create TDD tests (RED phase)
7. **`/implement-domain <issue-number>`** - Implement domain layer (GREEN phase)
8. **`/implement-usecase <issue-number>`** - Implement application layer
9. **`/implement-infra <issue-number>`** - Implement infrastructure layer
10. **`/implement-presentation <issue-number>`** - Implement presentation layer
11. **`/refactor <issue-number>`** - Refactor code (REFACTOR phase)

### Scenario Evolution Commands

12. **`/evolve-scenarios <feature-name>`** - Add/extend scenarios based on sprint feedback
13. **`/run-all-tests <issue-number>`** - Run all tests and generate report

## Common Guidelines

### When referencing GitHub issues:

- Always prioritize the most recent comments over older ones and the original issue description
- If there are conflicts between the issue content and newer comments, prioritize the newer comments
- Use `gh issue view <issue-number>` to get complete issue details including all comments

### Output language:

- Command instructions are in English
- User-facing output (specifications, design documents, error messages) must be in Japanese

### File organization:

- Vision document: `docs/vision/`
- Core scenarios: `docs/use_cases/core/`
- Use case specifications: `docs/use_cases/`
- Evolved scenarios: `docs/use_cases/evolved/`
- Sprint plans: `docs/sprints/`
- Domain models: `docs/domain/`
- Test plans: `docs/test_plan/`
- Test reports: `docs/test_report/`

## Usage Examples

### Project Initialization

```bash
# Define vision and core scenarios
/create-vision

# Plan first sprint
/sprint-planning 1

# Initialize project structure
/init-project-structure
```

### Sprint Execution

```bash
# Start with a GitHub issue from sprint planning
/create-use-case 123

# Follow the TDD/DDD workflow
/domain-modeling 123
/create-tests 123
/implement-domain 123
/implement-usecase 123
/implement-infra 123
/implement-presentation 123
/refactor 123
/run-all-tests 123
```

### Scenario Evolution (During Sprint)

```bash
# When new requirements emerge
/evolve-scenarios cart-management

# Continue with new issue
/create-tests 456
# ... continue implementation
```

## Key Principles

- **Vision Maintenance**: Always keep the overall vision in mind
- **Core Scenario Selection**: Focus on 80% coverage of main use cases
- **Gradual Extension**: Add edge cases in later sprints
- **Ticket Granularity**: 1 scenario = 1 ticket (as baseline)
- **Continuous Improvement**: Review specifications each sprint
