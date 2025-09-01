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
# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /review-issue <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🔍 Executing review-issue with automated Python implementation..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/13-review-issue.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    python3 "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Implementation quality review completed successfully"
    else
        echo "❌ Implementation quality review failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi
```

### Optional Reading (As Needed)
- Implementation specifications: `docs/use_cases/sprints/sprint-*/issue-${ISSUE_NUMBER}/specification.md`
- Domain model design: `docs/domain/issue-${ISSUE_NUMBER}-domain-model.md`
- All implementation code: `src/` directory structure

## GitHub Issue Integration

#### Issue Comment Retrieval and Analysis
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments for implementation review..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)
    
    # Extract and prioritize recent comments
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
    echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
    echo "Prioritizing latest 5 comments for implementation review"
    
    # Check for review feedback and requirement evolution through comments
    if [[ $COMMENT_COUNT -gt 0 ]]; then
        echo "Analyzing comment timeline for review feedback..."
        # Recent comments take precedence for review context
        LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
        if [[ -n "$LATEST_COMMENT_DATE" ]]; then
            echo "Latest review update: $LATEST_COMMENT_DATE"
        fi
        
        # Extract review and feedback related comments
        echo "Extracting review feedback context..."
        echo "$RECENT_COMMENTS" | jq -r '.[] | select(.body | contains("review") or contains("feedback") or contains("quality") or contains("architecture") or contains("improvement")) | .body' | head -3
    fi
fi
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Implementation Completeness Verification
**As Implementation Quality Auditor, verify the following:**

1. **All Layer Implementation Confirmation**
   - Verification Point: Domain/Application/Infrastructure/Presentation implementation completion
   - Criteria: Verify file existence and functional implementation for each layer

2. **Given-When-Then Traceability Verification**
   - Verification Point: Correspondence between specification scenarios and implementation/tests
   - Criteria: Whether all acceptance criteria are covered by implementation and tests

### Phase 2: Architecture Compliance Review
**As Implementation Quality Auditor, analyze the following:**

```bash
echo "🔍 Starting implementation review for Issue: #${ISSUE_NUMBER}"

# 1. Architecture Compliance Analysis
echo "🏗️ Analyzing architecture compliance..."

# Check layer dependency directions
echo "📊 Checking layer dependencies..."
find src/domain/ -name "*.py" -exec grep -l "from.*application\|from.*infrastructure\|from.*presentation" {} \;
if [[ $? -eq 0 ]]; then
    echo "❌ Warning: Domain layer depends on external layers"
fi

# 2. Code Quality Analysis
echo "📊 Analyzing code quality..."
uv run --frozen ruff check src/ --output-format=json > /tmp/quality_review.json
uv run --frozen pyright src/ --outputjson > /tmp/type_review.json

# 3. Test Coverage Analysis
echo "🧪 Analyzing test coverage..."
uv run --frozen pytest --cov=src --cov-report=json --cov-report=html tests/
```

### Phase 3: Comprehensive Quality Assessment
**As Implementation Quality Auditor, evaluate the following:**

1. **DDD Design Quality Assessment**
   - Entity design appropriateness
   - Value object immutability and equality
   - Domain service responsibility separation
   - Aggregate boundary validity

2. **Clean Architecture Compliance Assessment**  
   - Dependency direction (inward dependencies)
   - Interface segregation implementation
   - Responsibility separation between layers

3. **Test Quality Assessment**
   - Given-When-Then pattern implementation
   - Test independence and reproducibility
   - Edge case coverage

### Phase 4: Business Value Verification
**As Implementation Quality Auditor, confirm the following:**

1. **Requirements Fulfillment Confirmation**
   - Complete implementation of acceptance criteria
   - Accurate implementation of business rules
   - User story value realization

2. **Performance and Security Assessment**
   - Response performance adequacy
   - Security requirement implementation
   - Appropriate error handling

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist
**Required Items (MUST):**
- [ ] All layer implementations are complete
- [ ] Clean Architecture dependencies are in correct direction
- [ ] All Given-When-Then scenarios are implemented
- [ ] Test coverage is 80% or higher

**Recommended Items (SHOULD):**
- [ ] DDD design principles are properly applied
- [ ] Code quality metrics meet baseline standards
- [ ] Security and performance requirements are satisfied

### Quality Metrics
| Metric | Baseline | Actual | Result |
|--------|----------|--------|--------|
| Test Coverage | ≥80% | [Actual Value]% | ✅/❌ |
| Architecture Compliance | 100% | [Actual Value]% | ✅/❌ |
| Given-When-Then Coverage | 100% | [Actual Value]% | ✅/❌ |
| Code Quality Score | ≥80 | [Actual Value] | ✅/❌ |

### Error Handling
**Expected Errors and Actions:**
1. **Architecture Violations**: Layer dependency issues and correction guidance
2. **Insufficient Test Coverage**: Identification of untested areas and additional test proposals
3. **Unimplemented Requirements**: Identification of implementation gaps and additional implementation proposals

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
Issue metadata (`docs/use_cases/sprints/sprint-*/issue-${ISSUE_NUMBER}/metadata.json`) を更新:
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

## Important Notes

1. **Response to New Requirements Discovery**: When new issues, improvements, or requirement changes are discovered during review, interrupt the work and execute `/evolve-scenarios <feature-name>`

2. **Strict Application of Quality Standards**: Provide clear improvement guidance when values fall below baseline standards

3. **Emphasis on Traceability**: Ensure complete traceability from Given-When-Then scenarios to implementation and tests

4. **Business Value Verification**: Evaluate not only technical quality but also business value realization