Run all tests and generate comprehensive test report.

Follow these steps:

1. **Check Arguments**:

   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Clean Test Environment**:

   - Clear test cache: `pytest --cache-clear`
   - Remove old coverage data: `rm -f .coverage`

3. **Run Unit Tests**:

   ```bash
   pytest tests/unit/ -v --tb=short
   ```

   - Verify all domain logic tests pass
   - Check use case tests
   - Ensure fast execution (< 1 second per test)

4. **Run Integration Tests**:

   ```bash
   pytest tests/integration/ -v --tb=short
   ```

   - Test repository implementations
   - Verify database operations
   - Check external service integrations

5. **Run E2E Tests**:

   ```bash
   pytest tests/e2e/ -v --tb=short
   ```

   - Test complete user scenarios
   - Verify API endpoints
   - Check error handling

6. **Generate Coverage Report**:

   ```bash
   pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
          --cov-report=html --cov-report=term-missing \
          --cov-fail-under=80
   ```

   - Review coverage percentages
   - Identify untested code paths
   - Open HTML report: `open htmlcov/index.html`

7. **Run Performance Tests** (if available):

   ```bash
   pytest tests/performance/ -v --benchmark-only
   ```

   - Check response times
   - Identify bottlenecks

8. **Static Code Analysis**:

   ```bash
   # Linting
   ruff check . --statistics

   # Type checking
   pyright --stats

   # Security scanning (if bandit installed)
   bandit -r domain/ application/ infrastructure/ presentation/
   ```

9. **Generate Test Summary Report**:
   Create report in `docs/test_report/issue-$ARGUMENTS-test-report.md`:

   ```markdown
   # テストレポート: <機能名>

   Issue: #$ARGUMENTS
   実行日時: <timestamp>

   ## テスト結果サマリー

   ### ユニットテスト

   - 実行数: X
   - 成功: X
   - 失敗: X
   - スキップ: X
   - 実行時間: X 秒

   ### 統合テスト

   - 実行数: X
   - 成功: X
   - 失敗: X
   - 実行時間: X 秒

   ### E2E テスト

   - 実行数: X
   - 成功: X
   - 失敗: X
   - 実行時間: X 秒

   ## カバレッジ

   - 全体: X%
   - ドメイン層: X%
   - アプリケーション層: X%
   - インフラ層: X%
   - プレゼンテーション層: X%

   ## 品質メトリクス

   - Ruff エラー: X
   - Pyright エラー: X
   - 循環的複雑度: 最大 X

   ## 推奨事項

   - <改善点 1>
   - <改善点 2>
   ```

10. **Check Test Quality**:

- Ensure tests are independent
- Verify no hardcoded test data
- Check for proper mocking
- Validate assertion messages

11. **Performance Baseline**:

    - Record current performance metrics
    - Set benchmarks for future comparison

12. **Update Issue**:

    - Comment with test summary
    - Include coverage percentage
    - Note any concerns

13. **Next Steps Guidance**:
    Display in JAPANESE:

    ```
    テスト実行完了！

    結果:
    - ユニットテスト: X/X 成功
    - 統合テスト: X/X 成功
    - E2Eテスト: X/X 成功
    - カバレッジ: X%

    詳細レポート: docs/test_report/issue-X-test-report.md
    ```

Important Notes:

- Run tests in isolation (not in parallel initially)
- Fix any flaky tests immediately
- Aim for >80% code coverage
- Performance tests are optional
- All user-facing output must be in JAPANESE
