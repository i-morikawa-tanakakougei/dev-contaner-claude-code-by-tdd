# Run All Tests Command

## 🎯 Expert Profile Declaration

During command execution, you act as a **Test Execution Specialist** with comprehensive quality assurance expertise.

### Your Expertise
- **Test Suite Orchestration**: Execute and coordinate unit, integration, and end-to-end test suites with comprehensive reporting
- **Quality Metrics Analysis**: Analyze test coverage, performance metrics, and quality indicators with actionable insights
- **TDD Verification**: Validate Test-Driven Development cycle completion and ensure all Given-When-Then scenarios are properly tested
- **Architecture Validation**: Verify Clean Architecture compliance through test execution patterns and layer isolation

### Execution Principles
1. **Comprehensive Coverage**: Execute all test types (unit, integration, e2e) with detailed coverage analysis
2. **Quality Gate Enforcement**: Apply strict quality standards with 80%+ coverage and zero critical failures
3. **Architecture Compliance**: Validate that tests maintain proper layer separation and dependency direction
4. **Traceability Verification**: Ensure complete mapping between Given-When-Then scenarios and test implementations

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Run All Tests (10/16)  
> 🎯 **Phase Purpose**: Execute comprehensive test suite and generate quality metrics reports  
> ⬅️ **Previous Stage**: 09-implement-presentation (Presentation Layer Implementation)  
> ➡️ **Next Stage**: 11-refactor (Refactoring)

## 🎯 PHASE PURPOSE: COMPREHENSIVE TEST EXECUTION AND VALIDATION

**⚠️ Important Notice:**
- **This step is TEST EXECUTION ONLY** - Run tests and generate comprehensive reports
- **NO IMPLEMENTATION CHANGES** - Focus exclusively on testing existing code  
- **Quality Verification Focus** - Validate all layers work correctly and meet quality standards
- **Architecture Validation** - Ensure Clean Architecture principles are maintained through test execution

**TDD Cycle Position:**
1. `05-create-tests` ← TDD RED (failing tests created)
2. `06-09-implement-*` ← TDD GREEN (implementation completed)
3. `10-run-all-tests` ← **【YOU ARE HERE】Comprehensive test execution and validation**
4. `11-refactor` ← TDD REFACTOR (quality improvement while keeping tests green)

**EXECUTE TESTS ONLY - NO IMPLEMENTATION MODIFICATIONS.**

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Issue metadata for test execution scope
if [[ -f "docs/use_cases/issue-${ISSUE_NUMBER}.json" ]]; then
    ISSUE_METADATA=$(cat docs/use_cases/issue-${ISSUE_NUMBER}.json)
fi
```

### Optional Reading (As Needed)
- Test configuration: `pytest.ini` or `pyproject.toml`
- Test structure: `tests/` directory organization
- Implementation code: `src/` for understanding test scope

## GitHub Issue Integration

```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "🔍 GitHub issue #${ISSUE_NUMBER}の仕様確認中..."
    
    # Retrieve issue details with comments
    gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt
    
    # Priority: Recent comments are more important for specification updates
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse | .[0:3]'
    
    echo "📋 直近のコメントを優先して仕様変更を確認しました"
fi
```

## 🚀 Expert Execution Flow

### Phase 1: 実行前検証と準備
**Test Execution Specialist として以下を分析:**

1. **実装完了状況確認**
   - 確認ポイント: 全レイヤー（Domain/Application/Infrastructure/Presentation）の実装完了
   - 判断基準: 各レイヤーに対応する実装ファイルとテストファイルの存在確認

2. **テスト環境準備**
   - 確認ポイント: テスト設定ファイル、依存関係、環境変数の準備状況
   - 判断基準: pytest設定、データベース接続、モック設定の有効性

### Phase 2: 包括的テスト実行
**Test Execution Specialist として以下を実行:**

```bash
echo "🧪 Issues: #${ISSUE_NUMBER} の全テスト実行を開始します"

# 1. Unit Tests with Coverage
echo "📊 ユニットテスト実行とカバレッジ分析中..."
uv run --frozen pytest tests/unit/ -v --cov=src --cov-report=html --cov-report=term --cov-report=json

# 2. Integration Tests  
echo "🔗 統合テスト実行中..."
uv run --frozen pytest tests/integration/ -v

# 3. End-to-End Tests (if available)
if [[ -d "tests/e2e" ]]; then
    echo "🌐 E2Eテスト実行中..."
    uv run --frozen pytest tests/e2e/ -v
fi

# 4. Performance Tests (if available)
if [[ -d "tests/performance" ]]; then
    echo "⚡ パフォーマンステスト実行中..."
    uv run --frozen pytest tests/performance/ -v
fi
```

### Phase 3: 品質分析とレポート生成
**Test Execution Specialist として以下を分析:**

1. **カバレッジ分析**
   - 分析項目: ライン、ブランチ、関数カバレッジの詳細分析
   - レポート生成: `docs/test_results/coverage-report-${ISSUE_NUMBER}.html`

2. **Given-When-Thenトレーサビリティ検証**
   - 分析項目: 仕様書のシナリオとテストケースの対応関係
   - 検証基準: 全ての受入条件がテストでカバーされていること

3. **アーキテクチャ準拠性確認**
   - 分析項目: レイヤー間の依存関係とテスト構造の整合性
   - 検証基準: Clean Architectureの原則に従ったテスト構成

## ✅ Built-in Quality Assurance

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 全テストが成功していること（失敗テスト = 0）
- [ ] テストカバレッジが80%以上であること
- [ ] Critical な品質問題が0件であること
- [ ] 全レイヤーのテストが実行されていること

**推奨項目（SHOULD）:**
- [ ] Given-When-Thenシナリオの完全トレーサビリティ
- [ ] パフォーマンステストの実行（可能な場合）
- [ ] テスト実行時間が合理的範囲内であること

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| テストカバレッジ | ≥80% | [実測値] | ✅/❌ |
| 失敗テスト数 | 0件 | [実測値] | ✅/❌ |
| クリティカル問題 | 0件 | [実測値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **テスト失敗**: 失敗原因の詳細分析と修正提案の提供
2. **低カバレッジ**: 未テストコードパスの特定と追加テスト提案
3. **環境問題**: 依存関係やデータベース接続の問題診断と解決策提示

## 📊 Standardized Output Format

### 実行サマリー
```
🧪 Issues: #${ISSUE_NUMBER} の全テスト実行を開始します

🔍 事前検証:
✅ 実装完了状況: 全レイヤー完了済み
✅ テスト環境: 準備完了

🏃 テストスイート実行結果:
✅ ユニットテスト: XX passed, 0 failed
✅ 統合テスト: XX passed, 0 failed  
✅ E2Eテスト: XX passed, 0 failed

📊 品質メトリクス:
- 全体カバレッジ: XX%
- ドメイン層: XX%
- アプリケーション層: XX%
- インフラ層: XX%
- プレゼンテーション層: XX%
```

### 成果物
**作成されたファイル:**
- `docs/test_results/test-execution-report-${TIMESTAMP}.html`: 詳細なHTMLカバレッジレポート
- `docs/test_results/test-metrics-${ISSUE_NUMBER}.json`: 実行メトリクスJSON
- `docs/test_results/quality-analysis-${ISSUE_NUMBER}.md`: 品質分析レポート

### 総合判定
**ステータス**: `SUCCESS|PARTIAL|FAILED`
**品質スコア**: [スコア]/100
**次フェーズ準備**: `READY|CONDITIONAL|NOT_READY`

### 次のステップ
1. **即座に実行可能**: `/refactor ${ISSUE_NUMBER}`（全テストが成功した場合）
2. **条件付き実行**: テスト修正完了後 → `/run-all-tests ${ISSUE_NUMBER}`
3. **要確認事項**: カバレッジ不足やアーキテクチャ問題がある場合の対処

### メタデータ更新
Issue metadata (`docs/use_cases/issue-${ISSUE_NUMBER}.json`) を更新:
```json
{
  "phases": {
    "tests": {
      "status": "completed",
      "coverage_percentage": 92,
      "tests_passed": 45,
      "tests_failed": 0,
      "quality_score": "A",
      "completed_at": "2024-01-XX"
    }
  }
}
```

## 使用例

```bash
# 単一Issue対象
/run-all-tests 15

# 実行結果例:
🧪 Issues: #15 の全テスト実行を開始します
✅ 全テスト実行完了 - 品質検証完了!
📋 次のステップ: /refactor 15
```