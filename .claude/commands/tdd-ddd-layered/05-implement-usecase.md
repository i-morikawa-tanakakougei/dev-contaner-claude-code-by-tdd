Implement application layer use cases to orchestrate domain logic.

Follow these steps:

1. **Check Prerequisites**:
   - Verify domain implementation exists and tests pass
   - Verify use case tests exist in `tests/unit/application/use_cases/`
   - Run use case tests to confirm they are failing

2. **Create Application Layer Structure**:
   - Create directories:
   ```
   application/
   ├── use_cases/
   ├── dtos/
   └── exceptions/
   ```

3. **Implement Use Cases**:
   - Create use case files in `application/use_cases/`
   - Each use case should orchestrate domain objects
   - Handle application-level concerns (transactions, authorization)
   - Use dependency injection for repositories

   Example structure:
   ```python
   # application/use_cases/<use_case_name>.py
   class <UseCaseName>:
       def __init__(self, repository: <RepositoryInterface>):
           self._repository = repository
       
       def execute(self, request: <RequestDTO>) -> <ResponseDTO>:
           # 1. Validate request
           # 2. Load domain objects
           # 3. Execute domain logic
           # 4. Persist changes
           # 5. Return response
           pass
   ```

4. **Create DTOs (Data Transfer Objects)**:
   - Create request/response DTOs in `application/dtos/`
   - Keep DTOs simple and focused on data transfer
   - Include validation for request DTOs

   Example:
   ```python
   # application/dtos/<feature>_dtos.py
   @dataclass
   class <Feature>Request:
       # Request fields
       
       def validate(self):
           # Validation logic
           pass
   
   @dataclass
   class <Feature>Response:
       # Response fields
   ```

5. **Define Application Exceptions**:
   - Create custom exceptions in `application/exceptions/`
   - Distinguish between business rule violations and technical errors

6. **Implement Mock Repositories**:
   - Create in-memory implementations in `infrastructure/repositories/`
   - Use for testing without database

   Example:
   ```python
   # infrastructure/repositories/mock_<repository>.py
   class Mock<Repository>(<RepositoryInterface>):
       def __init__(self):
           self._storage = {}
       
       def save(self, entity):
           self._storage[entity.id] = entity
       
       def find_by_id(self, id):
           return self._storage.get(id)
   ```

7. **Run Use Case Tests**:
   - Execute: `pytest tests/unit/application/use_cases/ -v`
   - Ensure all use case tests are GREEN
   - Fix any failing tests

8. **Integration Testing**:
   - Write integration tests for use cases with mock repositories
   - Test transaction boundaries and error handling

9. **Check Code Quality**:
   - Run: `ruff check application/`
   - Run: `pyright application/`
   - Fix any issues

10. **Update Documentation**:
    - Document use case flow in `docs/application/`
    - Include sequence diagrams if complex

11. **Update Issue**:
    - Comment: `gh issue comment $ARGUMENTS --body "アプリケーション層（ユースケース）の実装を完了しました。"`

12. **Guide Next Steps**:
    - Suggest implementing infrastructure (`/implement-infra`) in Japanese
    - Or presentation layer if infrastructure is simple

Important Notes:
- Use cases orchestrate, don't contain business logic
- Keep use cases thin and focused
- Use DTOs for input/output, not domain objects
- Handle cross-cutting concerns (logging, auth)
- Mock repositories for testing
- All user-facing output must be in JAPANESE