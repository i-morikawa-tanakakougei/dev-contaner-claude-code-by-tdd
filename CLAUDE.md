# Development Guidelines

This document contains critical information about working with this codebase. Follow these guidelines precisely.

## Core Development Rules

1. Package Management

   - ONLY use uv, NEVER pip
   - Installation: `uv add package`
   - Running tools: `uv run tool`
   - Upgrading: `uv add --dev package --upgrade-package package`
   - FORBIDDEN: `uv pip install`, `@latest` syntax

2. Code Quality

   - Type hints required for all code
   - Public APIs must have docstrings
   - Functions must be focused and small
   - Follow existing patterns exactly
   - Line length: 120 chars maximum

3. Testing Requirements
   - Framework: `uv run --frozen pytest`
   - Async testing: use anyio, not asyncio
   - Coverage: test edge cases and errors
   - New features require tests
   - Bug fixes require regression tests

- For commits fixing bugs or adding features based on user reports add:

  ```bash
  git commit --trailer "Reported-by:<name>"
  ```

  Where `<name>` is the name of the user.

- For commits related to a Github issue, add

  ```bash
  git commit --trailer "Github-Issue:#<number>"
  ```

- NEVER ever mention a `co-authored-by` or similar aspects. In particular, never
  mention the tool used to create the commit message or PR.

## Pull Requests

- Create a detailed message of what changed. Focus on the high level description of
  the problem it tries to solve, and how it is solved. Don't go into the specifics of the
  code unless it adds clarity.

- Always add `i-morikawa-tanakakougei` as reviewer.

- NEVER ever mention a `co-authored-by` or similar aspects. In particular, never
  mention the tool used to create the commit message or PR.

## Development Approach: TDD/DDD/Layered Architecture

### Process Design: Vision to Ticket Creation Flow

This project adopts the **"Create core scenarios upfront, add and extend during sprints"** approach.

#### Initial Phase (Project Start)

1. **Vision Definition and Core Scenario Creation**: `/create-vision`

   - Define vision with Bounded Context and main use cases
   - Create Given-When-Then scenarios for core use cases (covering 80% of the whole)
   - Establish ubiquitous language
   - Document in `docs/vision/` and `docs/use_cases/core/`

2. **Sprint Planning**: `/sprint-planning <sprint-number>`
   - Split core scenarios into tickets (1 scenario = 1 ticket as baseline)
   - Set priorities and define sprint goals
   - Include Given-When-Then as acceptance criteria for each ticket
   - Create and manage GitHub issues

#### Sprint Execution Phase

3. **Use Case Specification Creation**: `/create-use-case <issue-number>`

   - Create Given-When-Then scenarios from issues
   - Verify alignment with vision
   - Define domain concepts and ubiquitous language
   - Document in `docs/use_cases/`

4. **Domain Model Design**: `/domain-modeling <issue-number>`

   - Design entities, value objects, and domain services
   - Define aggregate boundaries and repositories
   - Document in `docs/domain/`

5. **Test Creation (RED)**: `/create-tests <issue-number>`

   - Create failing tests based on specifications
   - Cover all Given-When-Then scenarios
   - Execute TDD RED phase

6. **Domain Layer Implementation (GREEN)**: `/implement-domain <issue-number>`

   - Implement minimal code to pass tests
   - Implement business rules and invariants
   - Maintain domain purity (no I/O)

7. **Application Layer Implementation**: `/implement-usecase <issue-number>`

   - Create use cases to orchestrate domain
   - Handle application concerns (transactions, authentication)
   - Use DTOs for input/output

8. **Infrastructure Layer Implementation**: `/implement-infra <issue-number>`

   - Create concrete repository implementations
   - Handle persistence and external services
   - Keep infrastructure details isolated

9. **Presentation Layer Implementation**: `/implement-presentation <issue-number>`

   - Create API endpoints or CLI commands
   - Handle input validation and error responses
   - Keep presentation layer lightweight

10. **Refactoring (REFACTOR)**: `/refactor <issue-number>`
    - Improve code quality after tests pass
    - Remove duplication and simplify
    - Maintain all tests GREEN

#### Scenario Evolution During Sprints

11. **Scenario Addition/Extension**: `/evolve-scenarios <feature-name>`

    - Add new scenarios based on sprint review feedback
    - Document edge cases and new requirements
    - Sync existing scenarios with modifications
    - Simultaneous execution of new scenarios and ticket creation (ensure consistency)

12. **Run All Tests**: `/run-all-tests <issue-number>`
    - Execute complete test suite
    - Verify coverage and quality metrics
    - Generate comprehensive reports

### Key Principles

- **Vision Maintenance**: Always keep the overall vision in mind, avoid missing the forest for the trees
- **Core Scenario Selection**: Focus on main use cases covering 80% of the vision
- **Gradual Extension**: Add edge cases in later sprints
- **Ticket Granularity**: 1 ticket = 1 scenario as baseline, split large scenarios
- **Continuous Improvement**: Review specifications each sprint to prevent obsolescence

### Command List

Initial Phase:

- `/create-vision`: Define vision and core scenarios
- `/sprint-planning <sprint-number>`: Sprint planning and ticket creation

Sprint Execution:

- `/create-use-case <issue-number>`: Create use case specifications
- `/domain-modeling <issue-number>`: Design domain model
- `/create-tests <issue-number>`: Create tests (RED)
- `/implement-domain <issue-number>`: Implement domain layer (GREEN)
- `/implement-usecase <issue-number>`: Implement application layer
- `/implement-infra <issue-number>`: Implement infrastructure layer
- `/implement-presentation <issue-number>`: Implement presentation layer
- `/refactor <issue-number>`: Refactoring (REFACTOR)

Scenario Evolution:

- `/evolve-scenarios <feature-name>`: Add/extend scenarios
- `/run-all-tests <issue-number>`: Run all tests

Others:

- `/init-project-structure`: Initialize project structure
- Custom commands are placed in `.claude/commands/tdd-ddd-layered/`

## Available Tools (MCP)

1. Context7

   - Please ensure you use Context7 in the following situations:
   - **When you need the latest API or library information:** When using Python, other frequently updated libraries and frameworks, or minor packages such as FastHtml, please obtain the latest official documentation and code examples from Context7 to perform accurate code generation.
   - **To ensure code accuracy:** To prevent outdated APIs or "hallucinated" code, please utilize Context7 to reference version-specific information.
   - **To improve development efficiency:** When coding, obtain the latest technical information in real-time from Context7 to provide prompt and accurate suggestions.
   - **For small-scale libraries and niche tech stacks:** When official documentation is limited, please obtain the latest information with Context7 and provide appropriate code.

   When using Context7, please generate an accurate answer that is optimized for the user's request based on the information you have obtained.

## Python Tools

## Code Formatting

1. Ruff

   - Format: `uv run --frozen ruff format .`
   - Check: `uv run --frozen ruff check .`
   - Fix: `uv run --frozen ruff check . --fix`
   - Critical issues:
     - Line length (88 chars)
     - Import sorting (I001)
     - Unused imports
   - Line wrapping:
     - Strings: use parentheses
     - Function calls: multi-line with proper indent
     - Imports: split into multiple lines

2. Type Checking

   - Tool: `uv run --frozen pyright`
   - Requirements:
     - Explicit None checks for Optional
     - Type narrowing for strings
     - Version warnings can be ignored if checks pass

3. Pre-commit
   - Config: `.pre-commit-config.yaml`
   - Runs: on git commit
   - Tools: Prettier (YAML/JSON), Ruff (Python)
   - Ruff updates:
     - Check PyPI versions
     - Update config rev
     - Commit config first

## Error Resolution

1. CI Failures

   - Fix order:
     1. Formatting
     2. Type errors
     3. Linting
   - Type errors:
     - Get full line context
     - Check Optional types
     - Add type narrowing
     - Verify function signatures

2. Common Issues

   - Line length:
     - Break strings with parentheses
     - Multi-line function calls
     - Split imports
   - Types:
     - Add None checks
     - Narrow string types
     - Match existing patterns
   - Pytest:
     - If the tests aren't finding the anyio pytest mark, try adding PYTEST_DISABLE_PLUGIN_AUTOLOAD=""
       to the start of the pytest run command eg:
       `PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest`

3. Best Practices
   - Check git status before commits
   - Run formatters before type checks
   - Keep changes minimal
   - Follow existing patterns
   - Document public APIs
   - Test thoroughly

## Exception Handling

- **Always use `logger.exception()` instead of `logger.error()` when catching exceptions**
  - Don't include the exception in the message: `logger.exception("Failed")` not `logger.exception(f"Failed: {e}")`
- **Catch specific exceptions** where possible:
  - File ops: `except (OSError, PermissionError):`
  - JSON: `except json.JSONDecodeError:`
  - Network: `except (ConnectionError, TimeoutError):`
- **Only catch `Exception` for**:
  - Top-level handlers that must not crash
  - Cleanup blocks (log at debug level)

## Interaction With User

- In principle, chat responses are in Japanese.
