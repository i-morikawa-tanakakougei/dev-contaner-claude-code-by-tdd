Apply review feedback to TDD/DDD/Layered Architecture implementation.

Follow these steps:

1. **Check Arguments**:
   - Verify that `$ARGUMENTS` is provided
   - If not provided, terminate immediately and prompt the user to pass the issue number argument in Japanese

2. **Load Review Report**:
   - Read review report from `docs/review/issue-$ARGUMENTS-review.md`
   - If not found, prompt user to run `/review-issue` first
   - Extract improvement items by priority

3. **Verify Current Test Status**:
   ```bash
   pytest --tb=short
   ```
   - Ensure all tests are GREEN before starting changes
   - Record current coverage percentage

4. **Process Required Improvements (必須対応項目)**:
   
   For each required improvement:
   
   a. **Create Focused Test**:
      - Write specific test for the improvement
      - Ensure test fails initially (RED)
   
   b. **Implement Fix**:
      - Make minimal change to pass test (GREEN)
      - Keep changes focused on single issue
   
   c. **Verify Tests**:
      - Run related test suite
      - Ensure no regression

5. **Process Recommended Improvements (推奨改善項目)**:
   
   For each recommended improvement:
   
   a. **Assess Impact**:
      - Evaluate effort vs benefit
      - Check if it affects public APIs
   
   b. **Apply Improvement**:
      - Follow TDD cycle if adding functionality
      - Refactor if improving existing code
   
   c. **Update Documentation**:
      - Update affected design docs
      - Add comments if complexity increased

6. **Architecture Compliance Fixes**:

   **DDD Principles**:
   - Fix ubiquitous language inconsistencies
   - Adjust aggregate boundaries if needed
   - Ensure domain purity (remove I/O from domain)
   - Make value objects truly immutable

   **Layered Architecture**:
   - Fix dependency direction violations
   - Remove circular dependencies
   - Ensure proper separation of concerns
   - Apply dependency injection where missing

   **TDD Practices**:
   - Add missing test scenarios
   - Improve test names and structure
   - Increase coverage for critical paths

7. **Code Quality Improvements**:
   
   ```bash
   # Fix linting issues
   ruff check . --fix
   
   # Address type checking errors
   pyright
   
   # Format code
   ruff format .
   ```

8. **Performance Optimizations** (if mentioned):
   - Profile before optimization
   - Apply improvements
   - Measure impact
   - Document changes

9. **Update Tests**:
   - Add tests for edge cases found in review
   - Improve test data builders
   - Remove test duplication
   - Ensure Given-When-Then structure

10. **Create New Tickets for Additional Requirements** (if any):
    - If new requirements were discovered during review:
    
    a. **Determine Sprint Allocation**:
       - Check current sprint capacity
       - Prioritize based on urgency and dependencies
    
    b. **Create GitHub Issues**:
       ```bash
       # For new scenarios discovered during review
       gh issue create \
         --title "実装: <New requirement>" \
         --body "## 概要\n<Description>\n\n## 発見経緯\nIssue #$ARGUMENTS のレビュー中に発見\n\n## シナリオ\n- Given: <condition>\n- When: <action>\n- Then: <result>\n\n## 関連\n- 元Issue: #$ARGUMENTS\n- レビューレポート: docs/review/issue-$ARGUMENTS-review.md" \
         --label "enhancement,from-review"
       ```
    
    c. **Update Sprint Backlog**:
       - If for current sprint: Update `docs/sprints/sprint-<current>-backlog.md`
       - If for next sprint: Update `docs/sprints/sprint-<next>-backlog.md`
    
    d. **Create Scenario Document**:
       - File: `docs/use_cases/evolved/from-review-$ARGUMENTS-<aspect>.md`
       - Link to original issue and review report

11. **Run Full Validation**:
    ```bash
    # Run all tests
    pytest
    
    # Check coverage improvement
    pytest --cov=domain --cov=application --cov=infrastructure --cov=presentation \
           --cov-report=term-missing
    
    # Verify code quality
    ruff check .
    pyright
    ```

12. **Create Feedback Application Report**:
    Create `docs/review/issue-$ARGUMENTS-feedback-applied.md` in Japanese:

```markdown
# フィードバック反映レポート: <機能名>

Issue: #$ARGUMENTS
反映日時: <timestamp>
元レビュー: docs/review/issue-$ARGUMENTS-review.md

## 反映結果サマリー

### 必須対応項目
| 項目 | 対応状況 | 変更内容 |
|------|---------|----------|
| <改善点1> | ✅ 完了 | <具体的な変更> |
| <改善点2> | ✅ 完了 | <具体的な変更> |

### 推奨改善項目
| 項目 | 対応状況 | 変更内容/未対応理由 |
|------|---------|-------------------|
| <改善点1> | ✅ 完了 | <具体的な変更> |
| <改善点2> | ⏸️ 保留 | <未対応の理由> |

## メトリクス改善

| メトリクス | 改善前 | 改善後 | 変化 |
|-----------|--------|--------|------|
| テストカバレッジ | X% | Y% | +Z% |
| テスト数 | X | Y | +Z |
| 循環的複雑度（最大） | X | Y | -Z |
| Ruffエラー | X | 0 | -X |
| Pyrightエラー | X | 0 | -X |

## 主な変更点

### ドメイン層
- <変更内容1>
- <変更内容2>

### アプリケーション層
- <変更内容1>
- <変更内容2>

### インフラストラクチャ層
- <変更内容1>
- <変更内容2>

### プレゼンテーション層
- <変更内容1>
- <変更内容2>

## 追加されたテスト
- <テストケース1>: <カバーするシナリオ>
- <テストケース2>: <カバーするシナリオ>

## リファクタリング
- <リファクタリング1>: <改善内容>
- <リファクタリング2>: <改善内容>

## 新規作成チケット
| Issue # | タイトル | スプリント | 優先度 |
|---------|----------|------------|--------|
| #<new1> | <Title> | Sprint X | High |
| #<new2> | <Title> | Sprint Y | Medium |

## 残課題
- <将来的な改善案1>
- <将来的な改善案2>

## 最終確認
- [x] すべてのテストがGREEN
- [x] カバレッジ80%以上
- [x] Ruffエラーなし
- [x] Pyrightエラーなし
- [x] Given-When-Thenシナリオ完全実装
```

13. **Update Issue**:
    ```bash
    gh issue comment $ARGUMENTS --body "レビューフィードバックを反映しました。

    反映結果:
    - 必須項目: X/X 完了
    - 推奨項目: Y/Z 完了
    - テストカバレッジ: X% → Y%
    
    詳細: docs/review/issue-$ARGUMENTS-feedback-applied.md
    
    すべてのテストがGREENで、品質基準を満たしています。"
    ```

14. **Commit Changes**:
    ```bash
    git add .
    git commit -m "refactor: レビューフィードバックを反映 (#$ARGUMENTS)

    - 必須改善項目をすべて対応
    - テストカバレッジを X% から Y% に改善
    - コード品質基準を達成
    
    詳細は docs/review/issue-$ARGUMENTS-feedback-applied.md を参照"
    ```

15. **Display Summary**:
    Show summary in Japanese:
    ```
    フィードバック反映完了！
    
    Issue: #$ARGUMENTS
    
    改善結果:
    - 必須項目: X/X ✅
    - 推奨項目: Y/Z ✅
    - 保留項目: Z件
    - 新規チケット作成: N件
    
    品質メトリクス:
    - カバレッジ: X% → Y% (↑Z%)
    - エラー: すべて解消 ✅
    
    次のステップ:
    - /run-all-tests $ARGUMENTS - 最終テスト実行
    - /create-pr $ARGUMENTS - プルリクエスト作成
    ```

Important Notes:
- Always maintain GREEN tests during changes
- Apply one improvement at a time
- Document why certain recommendations were not applied
- Focus on maintaining TDD/DDD/Layered Architecture principles
- All output and documentation must be in JAPANESE