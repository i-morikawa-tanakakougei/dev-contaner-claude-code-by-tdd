Implement domain layer to make tests pass (TDD GREEN phase).

Follow these steps:

1. **Check Arguments**:

   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Check Prerequisites**:

   - Verify tests exist in `tests/unit/domain/`
   - Run tests to confirm they are failing (RED phase)
   - If no tests found, prompt user in Japanese to run `/create-tests` first

3. **Run Failing Tests**:

   - Execute: `pytest tests/unit/domain/ -v`
   - Capture failing test output
   - Identify which domain objects need implementation

4. **Implement Entities**:

   - Create entity files in `domain/entities/`
   - Implement ONLY enough code to make tests pass
   - Follow domain model design from `docs/domain/`
   - Ensure business rules and invariants are enforced

   Example structure:

   ```python
   # domain/entities/<entity_name>.py
   class <EntityName>:
       def __init__(self, id, ...):
           self._validate_invariants()
           self.id = id
           # other attributes

       def _validate_invariants(self):
           # Business rule validation
           pass

       # Business methods from domain model
   ```

5. **Implement Value Objects**:

   - Create value object files in `domain/value_objects/`
   - Ensure immutability
   - Implement equality based on values
   - Add validation in constructor

   Example structure:

   ```python
   # domain/value_objects/<vo_name>.py
   @dataclass(frozen=True)
   class <ValueObjectName>:
       value: <type>

       def __post_init__(self):
           # Validation logic
           pass
   ```

6. **Implement Domain Services** (if needed):

   - Create service files in `domain/services/`
   - Implement stateless operations
   - Use only domain objects, no infrastructure

7. **Define Repository Interfaces**:

   - Create abstract interfaces in `domain/repositories/`
   - Define only methods needed by domain
   - No implementation details

   Example:

   ```python
   # domain/repositories/<repository_name>.py
   from abc import ABC, abstractmethod

   class <RepositoryName>(ABC):
       @abstractmethod
       def save(self, entity):
           pass

       @abstractmethod
       def find_by_id(self, id):
           pass
   ```

8. **Run Tests Again**:

   - Execute: `pytest tests/unit/domain/ -v`
   - Ensure all domain tests are now GREEN
   - If any fail, iterate on implementation

9. **Check Code Quality**:

   - Run linter: `ruff check domain/`
   - Run type checker: `pyright domain/`
   - Fix any issues found

10. **Document Implementation**:

- Update `docs/domain/issue-$ARGUMENTS-domain-model.md` with any changes
- Add implementation notes if design evolved

11. **Update Issue**:

    - Comment: `gh issue comment $ARGUMENTS --body "ドメイン層の実装を完了しました（GREEN phase）。すべてのドメインテストが成功しています。"`

12. **Guide Next Steps**:
    - Suggest implementing use cases (`/implement-usecase`) in Japanese
    - Or suggest refactoring if needed

Important Notes:

- Implement ONLY what's needed to pass tests
- Focus on domain logic, not technical concerns
- Keep entities and value objects pure (no I/O)
- Enforce invariants and business rules
- Use type hints for all code
- All user-facing output must be in JAPANESE
