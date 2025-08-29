# Refactor Command

## 🎯 Expert Profile Declaration

During command execution, you act as a **Code Quality Improvement Specialist** with advanced refactoring expertise.

### Your Expertise
- **Code Structure Optimization**: Improve code organization, eliminate duplication, and enhance maintainability without changing functionality
- **Design Pattern Implementation**: Apply appropriate design patterns (Strategy, Factory, Observer) to improve code flexibility and extensibility
- **Performance Optimization**: Identify and resolve performance bottlenecks while maintaining code readability and testability
- **Architecture Refinement**: Ensure Clean Architecture compliance and optimize layer separation for better maintainability

### Execution Principles
1. **Functionality Preservation**: All tests must remain GREEN throughout the refactoring process
2. **Incremental Improvement**: Make small, safe changes with continuous test validation
3. **Quality Focus**: Prioritize code readability, maintainability, and architectural consistency
4. **Test-Driven Safety**: Use existing tests as safety net and add tests for refactored components when needed

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
> 🗺️ **Current Position**: Sprint Execution Phase - Refactoring (11/16)  
> 🎯 **Phase Purpose**: Improve code quality while maintaining all functionality  
> ⬅️ **Previous Stage**: 10-run-all-tests (Test Execution)  
> ➡️ **Next Stage**: 12-evolve-scenarios (Scenario Evolution) or 13-review-issue (Review)

## 🎯 PHASE PURPOSE: TDD REFACTOR - CODE QUALITY IMPROVEMENT ONLY

**⚠️ Important Notice:**
- **This step is TDD REFACTOR PHASE** - Improve code quality while maintaining functionality
- **ALL TESTS MUST REMAIN GREEN** - Do not break existing functionality  
- **Quality Improvement Focus** - Remove duplication, improve readability, optimize performance
- **No New Features** - Only improve existing implementation structure and quality

**TDD Cycle Completion:**
1. `05-create-tests` ← TDD RED (failing tests created)
2. `06-09-implement-*` ← TDD GREEN (implementation completed)
3. `10-run-all-tests` ← All tests passing verification
4. `11-refactor` ← **【YOU ARE HERE】TDD REFACTOR (quality improvement)**

**Refactoring Rules:**
- ✅ Improve code structure and readability
- ✅ All tests must remain GREEN throughout refactoring
- ❌ No new features or functionality

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Issue metadata and test results
if [[ -f "docs/use_cases/issue-${ISSUE_NUMBER}.json" ]]; then
    ISSUE_METADATA=$(cat docs/use_cases/issue-${ISSUE_NUMBER}.json)
fi

# Latest test results to ensure GREEN state
LATEST_TEST_REPORT=$(find docs/test_results/ -name "*issue*${ISSUE_NUMBER}*" -type f | sort | tail -1)
```

### Optional Reading (As Needed)
- Implementation code: `src/` for refactoring analysis
- Test files: `tests/` for understanding coverage and structure
- Code quality reports: Previous analysis results

## GitHub Issue Integration

```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "🔍 GitHub issue #${ISSUE_NUMBER}の実装レビュー中..."
    
    # Retrieve issue details with recent comments
    gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt
    
    # Check for any code quality feedback in recent comments
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse | .[0:3]'
    
    echo "📋 コード品質に関するフィードバックを確認しました"
fi
```

## 🚀 Expert Execution Flow

### Phase 1: コード品質分析
**Code Quality Improvement Specialist として以下を分析:**

1. **コード構造分析**
   - 確認ポイント: 重複コード、長いメソッド、複雑な条件分岐の特定
   - 判断基準: コード複雑度メトリクス、重複率、メソッド長の評価

2. **アーキテクチャ準拠性確認**
   - 確認ポイント: レイヤー間の依存関係、単一責任原則の遵守
   - 判断基準: Clean Architecture の原則に従った構造になっているか

### Phase 2: 安全なリファクタリング実行
**Code Quality Improvement Specialist として以下を実行:**

```bash
echo "🔧 Issues: #${ISSUE_NUMBER} のリファクタリングを開始します"

# 1. Pre-refactoring Test Validation
echo "🟢 リファクタリング前テスト状態確認..."
uv run --frozen pytest --tb=short -q

if [[ $? -ne 0 ]]; then
    echo "❌ エラー: テストが失敗しています。先に /run-all-tests で修正してください"
    exit 1
fi

echo "✅ 全テストがGREEN状態です。安全にリファクタリングを開始できます"

# 2. Code Quality Analysis
echo "📊 コード品質分析中..."
uv run --frozen ruff check src/ --output-format=json > /tmp/quality_analysis.json
```

### Phase 3: 段階的品質改善
**Code Quality Improvement Specialist として以下を段階的に実行:**

1. **重複コード除去**
   - アクション: 共通処理の抽出、ユーティリティメソッドの作成
   - 期待結果: コード重複率の低下、保守性の向上

2. **メソッド・クラス構造改善**  
   - アクション: 長いメソッドの分割、単一責任原則の適用
   - 期待結果: 可読性向上、テスタビリティ改善

3. **デザインパターン適用**
   - アクション: 適切な設計パターンの導入（Strategy, Factory, etc.）
   - 期待結果: 拡張性とフレキシビリティの向上

4. **パフォーマンス最適化**
   - アクション: アルゴリズムの改善、データ構造の最適化
   - 期待結果: 実行速度向上、リソース使用量削減

**各改善後の継続的検証:**
```bash
# After each refactoring change
echo "🧪 改善後テスト実行中..."
uv run --frozen pytest --tb=short -q

if [[ $? -ne 0 ]]; then
    echo "❌ テストが失敗しました。変更を戻します"
    git checkout HEAD~1
    exit 1
fi

echo "✅ テストGREEN状態維持 - 次の改善に進みます"
```

## ✅ Built-in Quality Assurance

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 全テストがリファクタリング前後で成功していること
- [ ] 機能的な変更が一切加えられていないこと
- [ ] コード品質メトリクスが改善されていること
- [ ] Clean Architectureの原則が維持されていること

**推奨項目（SHOULD）:**
- [ ] コード重複率が削減されていること
- [ ] メソッド複雑度が適切な範囲内であること
- [ ] 適切な設計パターンが適用されていること

### 品質メトリクス
| 指標 | リファクタリング前 | リファクタリング後 | 改善率 |
|------|-------------------|-------------------|--------|
| コード重複率 | [Before]% | [After]% | [Improvement]% |
| 平均メソッド長 | [Before] lines | [After] lines | [Reduction]% |
| 循環的複雑度 | [Before] | [After] | [Improvement]% |

### エラー処理
**想定されるエラーと対処:**
1. **テスト失敗**: 即座に前の状態に戻し、より小さい単位でリファクタリング再実行
2. **パフォーマンス劣化**: ベンチマーク比較で性能低下を検出した場合の巻き戻し
3. **アーキテクチャ違反**: レイヤー間依存関係の問題検出時の修正指導

## 📊 Standardized Output Format

### 実行サマリー
```
🔧 Issues: #${ISSUE_NUMBER} のリファクタリングを開始します

🟢 事前検証:
✅ テスト状態: 全テスト成功（XX passed, 0 failed）
✅ コードベース: リファクタリング準備完了

🎨 リファクタリング実行結果:
✅ 重複コード除去: XX箇所改善
✅ メソッド構造改善: XX個のメソッドを最適化  
✅ デザインパターン適用: XX個のパターン導入
✅ パフォーマンス最適化: XX%の処理速度改善

🧪 継続的テスト検証:
✅ 全段階でテストGREEN維持
✅ 機能的変更なし確認済み
```

### 成果物
**作成されたファイル:**
- `docs/refactoring/refactor-report-${ISSUE_NUMBER}.md`: リファクタリング詳細レポート
- `docs/refactoring/quality-metrics-${ISSUE_NUMBER}.json`: 品質改善メトリクス
- `docs/refactoring/before-after-comparison-${ISSUE_NUMBER}.md`: 改善前後比較

### 総合判定
**ステータス**: `SUCCESS|PARTIAL|FAILED`
**品質改善スコア**: [改善度]/100
**次フェーズ準備**: `READY|CONDITIONAL|NOT_READY`

### 次のステップ
1. **即座に実行可能**: `/evolve-scenarios feature-name`（新しいシナリオ発見時）
2. **即座に実行可能**: `/review-issue ${ISSUE_NUMBER}`（レビューフェーズへ）
3. **要確認事項**: 重大な品質問題が残っている場合の追加改善

### メタデータ更新
Issue metadata (`docs/use_cases/issue-${ISSUE_NUMBER}.json`) を更新:
```json
{
  "phases": {
    "refactor": {
      "status": "completed",
      "code_quality_improvement": "XX%",
      "duplication_reduction": "XX%",
      "complexity_reduction": "XX%",
      "performance_improvement": "XX%",
      "completed_at": "2024-01-XX"
    }
  }
}
```

## 使用例

```bash
# 単一Issue対象
/refactor 15

# 実行結果例:
🔧 Issues: #15 のリファクタリングを開始します
🟢 テスト状態確認: 全テスト成功
🎨 コード品質改善実行中...
✅ リファクタリング完了 - テスト維持
🎉 TDD REFACTORフェーズ完了!
📋 次のステップ: /review-issue 15
```

## 重要な注意事項

1. **テスト駆動の安全性**: 各改善ステップの後に必ずテストを実行し、GREEN状態を維持
2. **機能不変の原則**: リファクタリングは機能を変更せず、構造のみを改善
3. **段階的アプローチ**: 大きな変更を避け、小さな改善を積み重ねる
4. **品質測定**: 改善前後の定量的比較で効果を検証