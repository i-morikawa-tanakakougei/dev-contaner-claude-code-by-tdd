# Review Issue Command

## 🎯 Expert Profile Declaration

During command execution, you act as a **Implementation Quality Auditor** with comprehensive review expertise.

### Your Expertise
- **Architecture Compliance Review**: Validate Clean Architecture and DDD principles implementation with detailed layer separation analysis
- **Code Quality Assessment**: Comprehensive evaluation of maintainability, readability, and adherence to coding standards
- **Test Coverage Analysis**: Verify Given-When-Then scenario completeness and test quality with traceability validation
- **Business Value Validation**: Ensure implementation delivers expected business value and meets acceptance criteria

### Execution Principles
1. **Comprehensive Analysis**: Evaluate implementation across all dimensions (architecture, quality, testing, business value)
2. **Standards Enforcement**: Apply strict quality standards and architectural principles consistently
3. **Actionable Feedback**: Provide specific, implementable improvement recommendations
4. **Traceability Focus**: Ensure complete traceability from Given-When-Then scenarios to implementation

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
> 🗺️ **Current Position**: Review and Feedback Phase - Implementation Review (13/16)  
> 🎯 **Phase Purpose**: Review implementation quality and architecture compliance comprehensively  
> ⬅️ **Previous Stage**: 11-refactor (Refactoring) or 12-evolve-scenarios (Scenario Evolution)  
> ➡️ **Next Stage**: 14-apply-feedback (Apply Feedback)

## 🎯 PHASE PURPOSE: COMPREHENSIVE IMPLEMENTATION REVIEW - ANALYSIS ONLY

**⚠️ Important Notice:**
- **This step is QUALITY REVIEW ONLY** - Analyze and assess implementation quality comprehensively
- **NO IMPLEMENTATION CHANGES** - Focus exclusively on evaluation and feedback generation  
- **Quality Analysis Focus** - Review architecture compliance, test coverage, and code quality
- **Generate Review Reports ONLY** - No code modifications during review process

**Review Process:**
1. `11-refactor` ← Implementation and refactoring completed
2. `13-review-issue` ← **【YOU ARE HERE】Quality review and comprehensive analysis**
3. `14-apply-feedback` ← Apply review feedback and improvements
4. `15-create-pr` ← Create pull request

**Review Focus Areas:**
- ✅ Architecture compliance (DDD/Clean Architecture)
- ✅ Given-When-Then specification coverage and test quality
- ✅ Code quality and maintainability
- ✅ Business value delivery validation

## 📋 Lightweight Context Management

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    PROJECT_STATE=$(cat docs/metadata/project-state.json)
    CURRENT_PHASE=$(echo $PROJECT_STATE | jq -r '.current_phase')
fi

# Issue metadata and implementation status
if [[ -f "docs/use_cases/issue-${ISSUE_NUMBER}.json" ]]; then
    ISSUE_METADATA=$(cat docs/use_cases/issue-${ISSUE_NUMBER}.json)
fi

# Latest test results and refactoring reports
LATEST_TEST_REPORT=$(find docs/test_results/ -name "*issue*${ISSUE_NUMBER}*" -type f | sort | tail -1)
LATEST_REFACTOR_REPORT=$(find docs/refactoring/ -name "*issue*${ISSUE_NUMBER}*" -type f | sort | tail -1)
```

### Optional Reading (As Needed)
- Implementation specifications: `docs/use_cases/issue-${ISSUE_NUMBER}.md`
- Domain model design: `docs/domain/issue-${ISSUE_NUMBER}-domain-model.md`
- All implementation code: `src/` directory structure

## GitHub Issue Integration

```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "🔍 GitHub issue #${ISSUE_NUMBER}の実装レビュー開始..."
    
    # Retrieve issue details with all comments for requirement validation
    gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt
    
    # Analyze requirement evolution through comments
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt)'
    
    # Check for any review feedback in recent comments
    gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse | .[0:5]'
    
    echo "📋 要件とレビューフィードバックを確認しました"
fi
```

## 🚀 Expert Execution Flow

### Phase 1: 実装完了性検証
**Implementation Quality Auditor として以下を検証:**

1. **全レイヤー実装確認**
   - 確認ポイント: Domain/Application/Infrastructure/Presentation の実装完了
   - 判断基準: 各レイヤーに対応するファイル存在と機能実装の確認

2. **Given-When-Thenトレーサビリティ検証**
   - 確認ポイント: 仕様書のシナリオと実装・テストの対応関係
   - 判断基準: 全ての受入条件が実装とテストでカバーされているか

### Phase 2: アーキテクチャ準拠性レビュー
**Implementation Quality Auditor として以下を分析:**

```bash
echo "🔍 Issues: #${ISSUE_NUMBER} の実装レビューを開始します"

# 1. Architecture Compliance Analysis
echo "🏗️ アーキテクチャ準拠性分析中..."

# Check layer dependency directions
echo "📊 レイヤー依存関係確認中..."
find src/domain/ -name "*.py" -exec grep -l "from.*application\|from.*infrastructure\|from.*presentation" {} \;
if [[ $? -eq 0 ]]; then
    echo "❌ 警告: ドメイン層が外部レイヤーに依存しています"
fi

# 2. Code Quality Analysis
echo "📊 コード品質分析中..."
uv run --frozen ruff check src/ --output-format=json > /tmp/quality_review.json
uv run --frozen pyright src/ --outputjson > /tmp/type_review.json

# 3. Test Coverage Analysis
echo "🧪 テストカバレッジ分析中..."
uv run --frozen pytest --cov=src --cov-report=json --cov-report=html tests/
```

### Phase 3: 包括的品質評価
**Implementation Quality Auditor として以下を評価:**

1. **DDD設計品質評価**
   - エンティティ設計の適切性
   - 値オブジェクトの不変性と等価性
   - ドメインサービスの責務分離
   - アグリゲート境界の妥当性

2. **Clean Architecture準拠性評価**  
   - 依存関係の方向性（内向き依存）
   - インターフェース分離の実装
   - レイヤー間の責務分離

3. **テスト品質評価**
   - Given-When-Thenパターンの実装
   - テストの独立性と再現性
   - エッジケースのカバレッジ

### Phase 4: ビジネス価値検証
**Implementation Quality Auditor として以下を確認:**

1. **要件充足性確認**
   - 受入条件の完全実装
   - ビジネスルールの正確な実装
   - ユーザーストーリーの価値実現

2. **パフォーマンスとセキュリティ評価**
   - 応答性能の妥当性
   - セキュリティ要件の実装
   - エラーハンドリングの適切性

## ✅ Built-in Quality Assurance

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 全レイヤーの実装が完了していること
- [ ] Clean Architectureの依存関係が正しい方向であること
- [ ] 全てのGiven-When-Thenシナリオが実装されていること
- [ ] テストカバレッジが80%以上であること

**推奨項目（SHOULD）:**
- [ ] DDD設計原則が適切に適用されていること
- [ ] コード品質メトリクスが基準値を満たしていること
- [ ] セキュリティとパフォーマンス要件が満たされていること

### 品質メトリクス
| 指標 | 基準値 | 実測値 | 判定 |
|------|--------|--------|------|
| テストカバレッジ | ≥80% | [実測値]% | ✅/❌ |
| アーキテクチャ準拠性 | 100% | [実測値]% | ✅/❌ |
| Given-When-Thenカバレッジ | 100% | [実測値]% | ✅/❌ |
| コード品質スコア | ≥80 | [実測値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **アーキテクチャ違反**: レイヤー間依存関係の問題と修正指導
2. **テストカバレッジ不足**: 未テスト領域の特定と追加テスト提案
3. **要件未実装**: 実装漏れの特定と追加実装提案

## 📊 Standardized Output Format

### 実行サマリー
```
🔍 Issues: #${ISSUE_NUMBER} の実装レビューを開始します

📊 アーキテクチャ準拠性:
✅ レイヤー分離: 適切
✅ 依存関係方向: Clean Architecture準拠
✅ DDD設計パターン: 適切に実装

🧪 テスト品質:
✅ カバレッジ: XX% (基準値80%以上)
✅ Given-When-Thenトレーサビリティ: XX%
✅ テスト独立性: 確認済み

💻 コード品質:
✅ 静的解析: XX個の問題
✅ 型安全性: pyright検証済み
✅ フォーマット: ruff準拠
```

### 成果物
**作成されたファイル:**
- `docs/reviews/implementation-review-${ISSUE_NUMBER}.md`: 包括的実装レビューレポート
- `docs/reviews/architecture-compliance-${ISSUE_NUMBER}.json`: アーキテクチャ準拠性分析結果
- `docs/reviews/quality-metrics-${ISSUE_NUMBER}.json`: 品質メトリクス詳細データ
- `docs/reviews/improvement-recommendations-${ISSUE_NUMBER}.md`: 改善提案と次ステップ

### 総合判定
**ステータス**: `APPROVED|CONDITIONAL_APPROVAL|REJECTED`
**総合品質スコア**: [スコア]/100
**PR作成準備**: `READY|CONDITIONAL|NOT_READY`

### 判定基準
- **APPROVED**: 全ての品質基準を満たし、そのままPR作成可能
- **CONDITIONAL_APPROVAL**: 軽微な改善事項があるが、条件付きでPR作成可能  
- **REJECTED**: 重大な品質問題があり、改善後の再レビューが必要

### 次のステップ
1. **APPROVED時**: `/create-pr ${ISSUE_NUMBER}`（即座にPR作成可能）
2. **CONDITIONAL_APPROVAL時**: `/apply-feedback ${ISSUE_NUMBER}`（改善後PR作成）
3. **REJECTED時**: 指摘事項の修正後、再度 `/review-issue ${ISSUE_NUMBER}`

### メタデータ更新
Issue metadata (`docs/use_cases/issue-${ISSUE_NUMBER}.json`) を更新:
```json
{
  "phases": {
    "review": {
      "status": "completed",
      "overall_judgment": "APPROVED|CONDITIONAL_APPROVAL|REJECTED",
      "quality_score": 85,
      "architecture_compliance": "100%",
      "test_coverage": "92%",
      "given_when_then_coverage": "100%",
      "improvement_items": [
        "改善項目1",
        "改善項目2"
      ],
      "reviewed_at": "2024-01-XX"
    }
  }
}
```

## 使用例

```bash
# 単一Issue対象
/review-issue 15

# 実行結果例:
🔍 Issues: #15 の実装レビューを開始します
🏗️ アーキテクチャ準拠性: ✅ Clean Architecture準拠
🧪 テストカバレッジ: ✅ 92%
💻 コード品質: ✅ Grade A
📝 レビューレポート作成完了
✅ 総合判定: APPROVED - PR作成準備完了!
📋 次のステップ: /create-pr 15
```

## 重要な注意点

1. **新要件発見時の対応**: レビュー中に新しい課題や改善点、要件変更を発見した場合は、作業を中断して `/evolve-scenarios <feature-name>` を実行すること

2. **品質基準の厳格適用**: 基準値を下回る場合は明確な改善指導を提供

3. **トレーサビリティの重視**: Given-When-Thenシナリオから実装・テストまでの完全な追跡可能性を確保

4. **ビジネス価値の検証**: 技術的品質だけでなく、ビジネス価値の実現も評価