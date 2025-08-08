Refactor code after all tests are GREEN (TDD REFACTOR phase).

Follow these steps:

1. **Check Arguments**:

   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Verify All Tests Pass**:

   - Run full test suite: `pytest`
   - Ensure 100% of tests are GREEN
   - If any fail, fix them before refactoring

3. **Analyze Code Quality**:

   - Run linter: `ruff check . --show-source`
   - Run type checker: `pyright`
   - Check test coverage: `pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation`
   - Identify areas needing improvement

4. **Domain Layer Refactoring**:

   - Remove duplication in entities and value objects
   - Extract common behavior to base classes
   - Simplify complex methods
   - Ensure ubiquitous language is used consistently

   Common refactorings:

   - Extract method
   - Extract class
   - Replace magic numbers with constants
   - Simplify conditional expressions

5. **Application Layer Refactoring**:

   - Reduce use case complexity
   - Extract common validation logic
   - Improve error handling consistency
   - Optimize DTO conversions

6. **Infrastructure Layer Refactoring**:

   - Optimize database queries
   - Improve connection handling
   - Extract common mapping logic
   - Add caching where appropriate

7. **Presentation Layer Refactoring**:

   - Standardize error responses
   - Extract common validation patterns
   - Improve API consistency
   - Reduce controller complexity

8. **Test Refactoring**:

   - Remove test duplication
   - Extract test fixtures and builders
   - Improve test names and organization
   - Add missing edge case tests

9. **Cross-Cutting Concerns**:

   - Standardize logging patterns
   - Improve error messages
   - Add performance monitoring hooks
   - Ensure consistent naming conventions

10. **Run Tests After Each Change**:

- Make small, incremental changes
- Run relevant tests after each refactoring
- Commit working state frequently

11. **Update Documentation**:

    - Update design docs if architecture changed
    - Improve code comments where needed
    - Update API documentation

12. **Performance Optimization** (if needed):

    - Profile slow operations
    - Optimize database queries
    - Add appropriate indexes
    - Consider async operations

13. **Final Validation**:

    - Run full test suite again
    - Check linting and type checking
    - Review test coverage report
    - Ensure no functionality was broken

14. **Create Refactoring Summary**:

    - Document major changes made
    - Note performance improvements
    - List any breaking changes

15. **Update Issue**:
    - Comment: `gh issue comment $ARGUMENTS --body "リファクタリングを完了しました。すべてのテストは成功し、コード品質が向上しました。"`

Important Notes:

- Never refactor without GREEN tests
- Make one type of change at a time
- Keep commits small and focused
- Refactoring should not change behavior
- All user-facing output must be in JAPANESE
