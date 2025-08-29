# Create Use Case

## 🎯 Expert Profile Declaration

During command execution, you act as a **Requirements Analysis and Use Case Design Expert** specialist.

### Your Expertise
- **Requirements Engineering**: Comprehensive requirement extraction from GitHub issues with specification conflict resolution and stakeholder alignment
- **Use Case Architecture**: Detailed use case specification design with Given-When-Then scenario modeling and acceptance test creation
- **Domain Analysis**: Domain concept identification with ubiquitous language integration and boundary context alignment  
- **Test Design**: Acceptance test case creation with comprehensive edge case coverage and automated testing preparation

### Execution Principles
1. **Issue-Driven Analysis**: Extract comprehensive requirements from GitHub issues including comment history and specification evolution
2. **Scenario Completeness**: Create main scenarios, alternative flows, edge cases, and exception handling with full test coverage
3. **Domain Consistency**: Ensure all domain concepts align with established ubiquitous language and bounded context
4. **Implementation Readiness**: Produce specifications that enable direct TDD implementation without ambiguity

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
> 🗺️ **Current Position**: Use Case Specification - Detailed Requirements (3/16)  
> 🎯 **Phase Purpose**: Convert GitHub issues into detailed implementable specifications  
> ➡️ **Next Stage**: /domain-modeling to design domain model from use cases

## 🎯 PHASE PURPOSE: USE CASE SPECIFICATION FROM GITHUB ISSUES

**⚠️ Important Notice:**
- **This step focuses on DETAILED SPECIFICATION CREATION** - Convert GitHub issues into comprehensive Given-When-Then specifications with full test coverage
- **NO IMPLEMENTATION** - Focus only on requirements analysis and specification design
- **GITHUB ISSUE INTEGRATION** - Prioritize recent comments and track specification evolution through comment history

**What this step does:**
1. `/sprint-planning` ← スプリントチケットを作成済み
2. `/create-use-case <issue-number>` ← **【YOU ARE HERE】GitHub Issueから詳細仕様を作成**
3. `/domain-modeling <issue-number>` ← ユースケースからドメインモデルを設計
4. Then proceed with TDD implementation workflow

**ANALYZE GITHUB ISSUES AND CREATE SPECIFICATIONS. DO NOT IMPLEMENT CODE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-use-case <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "Creating use case specification for Issue #$ISSUE_NUMBER"

# Load project context
if [[ -f "docs/vision/ubiquitous_language.md" ]]; then
    echo "Loading ubiquitous language definitions..."
    UBIQUITOUS_LANGUAGE_EXISTS=true
else
    echo "WARNING: Ubiquitous language not found. May need to update during specification."
    UBIQUITOUS_LANGUAGE_EXISTS=false
fi

# Check for existing use case directory
mkdir -p "docs/use_cases/issue_$ISSUE_NUMBER"
echo "Use case directory prepared: docs/use_cases/issue_$ISSUE_NUMBER"
```

### Optional Reading (As Needed)
- Project vision: `docs/vision/vision.md` (understand overall context)
- Bounded context: `docs/vision/bounded_context.md` (verify domain boundaries)
- Related use cases: `docs/use_cases/issue_*/` (identify patterns and dependencies)

## GitHub Issue Integration

### Issue Comment Retrieval and Analysis
```bash
# Retrieve issue with full comment history
echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments..."

# Get issue details with comments
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)

# Extract and prioritize recent comments
RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')

COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
echo "Prioritizing latest 5 comments for specification analysis"

# Check for specification conflicts
if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "Analyzing comment timeline for requirement evolution..."
    # Recent comments take precedence over original issue description
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "Latest specification update: $LATEST_COMMENT_DATE"
    fi
fi
```

### Specification Evolution Tracking
```markdown
## Comment Analysis Strategy
1. **Latest First**: Recent comments override earlier specifications
2. **Authority Recognition**: Identify specification authors vs. discussants  
3. **Change Tracking**: Monitor requirement evolution through timeline
4. **Conflict Detection**: Flag contradictory requirements between original issue and comments
5. **Specification Completeness**: Identify missing requirements or ambiguous specifications
```

## 🚀 専門家実行フロー

要求分析・ユースケース設計エキスパートとして以下の段階的なアプローチで実行します：

### Phase 1: GitHub Issue詳細分析
**専門家として以下を分析:**

1. **Issue内容の包括的理解**
   ```bash
   # Analyze issue details from retrieved data
   echo "Issue Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
   echo "Issue Body Analysis:"
   echo "$(echo "$ISSUE_DATA" | jq -r '.body')" | head -20
   echo "Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name' | tr '\n' ', ')"
   ```

2. **コメント履歴による仕様進化分析**
   ```bash
   # Process comments chronologically to understand requirement evolution
   if [[ $COMMENT_COUNT -gt 0 ]]; then
     echo "Processing comment timeline..."
     echo "$RECENT_COMMENTS" | jq -r '.[] | "[\(.createdAt)] \(.author.login): \(.body[0:100])..."'
   fi
   ```
   - 確認ポイント: 要求の明確性、制約条件、受け入れ基準の完全性
   - 判断基準: 実装可能性、テスト可能性、ビジネス価値の明確性

### Phase 2: ドメイン概念抽出と言語整合性確認
**専門家として以下を設計:**

1. **新しいドメイン概念の識別**
   ```bash
   # Read existing ubiquitous language
   if [[ $UBIQUITOUS_LANGUAGE_EXISTS == true ]]; then
     Read docs/vision/ubiquitous_language.md
   fi
   
   # Analyze issue for new domain concepts
   # Extract nouns and domain-specific terms from issue description and comments
   ```

2. **既存ユビキタス言語との整合性確認**
   ```markdown
   # 言語整合性チェックテンプレート
   ## 新規概念候補
   - **[概念名]**: [Issue内での使用文脈]
   - **既存用語との関係**: [類似概念の有無、命名の一貫性]
   - **境界コンテキスト内での位置**: [ドメイン境界内での役割]
   ```

### Phase 3: メインシナリオ設計
**専門家として以下を実行:**

1. **主要フローのGiven-When-Then化**
   ```markdown
   # メインシナリオテンプレート
   ## シナリオ: [Issue要件に基づくシナリオ名]
   
   ### 背景と目的
   [Issueから抽出した背景情報とビジネス目的]
   
   ### メインフロー
   **Given** [前提条件 - システム状態とデータ準備]
   **When** [実行アクション - ユーザー操作や外部イベント]  
   **Then** [期待結果 - システム応答と状態変化]
   
   ### 受け入れ基準
   - [ ] [検証可能な条件1]
   - [ ] [検証可能な条件2]
   - [ ] [検証可能な条件3]
   ```

2. **代替シナリオとエラーケース設計**
   ```markdown
   # 代替・例外シナリオテンプレート
   ## Alternative Flow 1: [代替条件]
   **Given** [代替前提条件]
   **When** [代替アクション]
   **Then** [代替結果]
   
   ## Exception Flow 1: [例外条件]  
   **Given** [例外前提条件]
   **When** [例外発生アクション]
   **Then** [例外処理結果とエラーメッセージ]
   ```

### Phase 4: 受け入れテスト設計
**専門家として以下を実行:**

1. **テストケース詳細化**
   ```markdown
   # 受け入れテストケーステンプレート
   ## Test Case 1: [テストケース名]
   
   ### テストデータ準備
   ```json
   {
     "initial_state": {...},
     "test_input": {...},
     "expected_output": {...}
   }
   ```
   
   ### 実行ステップ
   1. [準備ステップ]
   2. [実行ステップ]  
   3. [検証ステップ]
   
   ### 期待結果
   - [具体的な検証ポイント]
   ```

2. **自動化テスト準備**
   - アクション: Design test automation strategy and identify testable components
   - 期待結果: Clear guidance for TDD implementation in subsequent phases

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] GitHub Issueの全要件がGiven-When-Thenシナリオ化されている
- [ ] コメント履歴が適切に分析され最新の仕様が反映されている
- [ ] メインフロー、代替フロー、例外処理が全て定義されている
- [ ] 全シナリオが受け入れテスト可能な形で記述されている
- [ ] ドメイン概念がユビキタス言語と整合している

**推奨項目（SHOULD）:**
- [ ] エッジケースとバウンダリ条件が十分に考慮されている
- [ ] パフォーマンス要件やセキュリティ制約が明記されている  
- [ ] 他のユースケースとの依存関係が明確化されている

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| シナリオ完備率 | 100% | [メイン/代替/例外の完成率] | ✅/❌ |
| 受け入れ基準明確度 | 90%以上 | [明確な基準数/総基準数] | ✅/❌ |
| テストケースカバレッジ | 85%以上 | [カバーされた条件/総条件] | ✅/❌ |
| ドメイン言語整合性 | 100% | [整合概念数/新規概念数] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. Issue存在エラー: Issue番号の確認、アクセス権限の確認
2. 仕様矛盾エラー: ステークホルダーへの確認要求、優先順位の明確化  
3. ドメイン概念競合: 既存言語との調整、新規概念の再定義

## 📊 標準化出力フォーマット

### 実行サマリー
- ✅ **Issue分析**: [分析完了したIssue情報とコメント数]
- ✅ **シナリオ作成**: [作成されたメイン/代替/例外シナリオ数]
- ✅ **受け入れ基準**: [定義された受け入れ基準数とテストケース数]
- ✅ **ドメイン概念**: [新規定義または更新されたドメイン概念数]

### 成果物
**作成されたファイル:**
- `docs/use_cases/issue_<number>/specification.md`: ユースケース仕様書
- `docs/use_cases/issue_<number>/scenarios.md`: Given-When-Thenシナリオ集
- `docs/use_cases/issue_<number>/domain_concepts.md`: 関連ドメイン概念定義
- `docs/use_cases/issue_<number>/acceptance_tests.md`: 受け入れテストケース
- `docs/vision/ubiquitous_language.md`: 更新されたユビキタス言語辞書

### 総合判定
**ステータス**: `[SUCCESS|PARTIAL|FAILED]`
**品質スコア**: [スコア]/100
**次フェーズ準備**: `[READY|CONDITIONAL|NOT_READY]`

### 次のステップ
1. **即座に実行可能**: `/domain-modeling <issue-number>` でドメインモデル設計開始
2. **条件付き実行**: 仕様レビュー完了後 → `/create-tests <issue-number>`
3. **要確認事項**: [不明確な要件、外部システム仕様、パフォーマンス要件詳細]

### メタデータ更新
```json
{
  "command_executed": "create-use-case", 
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "use-case-specification",
  "issue_number": "[issue-number]",
  "deliverables": {
    "specification": "docs/use_cases/issue_<number>/specification.md",
    "scenarios": "docs/use_cases/issue_<number>/scenarios.md", 
    "domain_concepts": "docs/use_cases/issue_<number>/domain_concepts.md",
    "acceptance_tests": "docs/use_cases/issue_<number>/acceptance_tests.md"
  },
  "metrics": {
    "scenarios_created": "[main/alternative/exception count]",
    "acceptance_criteria": "[number]",
    "test_cases": "[number]",
    "domain_concepts_added": "[number]"
  },
  "next_recommended": ["domain-modeling"],
  "quality_score": "[score]"
}
```

---

🎯 GitHub Issueからユースケース仕様作成を開始します。要求分析エキスパートとして、実装可能で包括的な仕様を作成いたします。

**使用方法**: 
```bash
/create-use-case <issue-number>

# 例
/create-use-case 123
```