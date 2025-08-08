Create TDD tests based on Given-When-Then specifications and domain model.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Check Prerequisites**:
   - Verify use case specification exists in `docs/use_cases/`
   - Verify domain model exists in `docs/domain/`
   - If missing, prompt user in Japanese to complete previous steps

3. **Analyze Specifications**:
   - Read Given-When-Then scenarios
   - Read domain model design
   - Map scenarios to test cases

4. **Create Test Structure**:
   - Create test directories if they don't exist:
   ```
   tests/
   ├── unit/
   │   ├── domain/
   │   │   ├── entities/
   │   │   └── value_objects/
   │   └── application/
   │       └── use_cases/
   ├── integration/
   │   └── repositories/
   └── e2e/
       └── api/
   ```

5. **Write Unit Tests (RED phase)**:
   - Start with domain entity tests
   - For each Given-When-Then scenario, create corresponding test
   - Tests should FAIL initially (no implementation yet)
   - Use clear test names that reflect the scenario
   - Include comments linking to specification

   Example structure:
   ```python
   def test_<scenario_description>():
       # Given: <前提条件>
       # When: <実行アクション>
       # Then: <期待される結果>
       assert False  # RED: Not implemented yet
   ```

6. **Create Test Files**:
   - Domain entity tests: `tests/unit/domain/entities/test_<entity_name>.py`
   - Value object tests: `tests/unit/domain/value_objects/test_<vo_name>.py`
   - Use case tests: `tests/unit/application/use_cases/test_<use_case>.py`

7. **Define Test Data Builders**:
   - Create test fixtures and builders for consistent test data
   - Place in `tests/fixtures/` or `tests/builders/`

8. **Document Test Plan**:
   - Create `docs/test_plan/issue-$ARGUMENTS-test-plan.md` in JAPANESE:
   ```markdown
   # テスト計画: <機能名>

   Issue: #$ARGUMENTS

   ## テストカバレッジ

   ### ユニットテスト
   - [ ] <Entity>: <テスト内容>
   - [ ] <ValueObject>: <テスト内容>
   - [ ] <UseCase>: <テスト内容>

   ### 統合テスト
   - [ ] <Repository>: <テスト内容>

   ### E2Eテスト
   - [ ] <API Endpoint>: <テスト内容>

   ## テスト実行方法
   ```
   # Run all tests
   pytest

   # Run specific test file
   pytest tests/unit/domain/entities/test_<entity>.py

   # Run with coverage
   pytest --cov=domain --cov=application
   ```
   ```

9. **Verify Test Setup**:
   - Run tests to confirm they fail (RED phase)
   - Check that all scenarios are covered
   - Ensure test names are descriptive

10. **Update Issue**:
   - Comment: `gh issue comment $ARGUMENTS --body "TDDテストを作成しました（RED phase）。実装前のため、すべてのテストは失敗します。"`

11. **Guide Next Steps**:
    - Prompt user in Japanese to implement domain layer (`/implement-domain`)
    - Remind about RED-GREEN-REFACTOR cycle

Important Notes:
- Tests must fail initially (TDD RED phase)
- Each test should test ONE thing only
- Use descriptive test names in snake_case
- Include Given-When-Then comments in tests
- Mock external dependencies appropriately
- All user-facing output must be in JAPANESE