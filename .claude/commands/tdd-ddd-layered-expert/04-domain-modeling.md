# 04-domain-modeling (Expert Mode Integration)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Domain-Driven Design Architect** specialist.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise
- **DDD Tactical Design**: Entity, Value Object, Aggregate, and Repository design
- **Business Rule Modeling**: Complex business logic extraction and formalization
- **Aggregate Boundary Design**: Consistency boundary identification and optimization
- **Domain Service Architecture**: Complex business operation orchestration

### Execution Principles
1. **Domain Purity**: Keep domain layer free from infrastructure concerns
2. **Business Rule Focus**: Extract and formalize all business invariants and rules
3. **Aggregate Consistency**: Design proper transactional boundaries

### Quality Standards
- **Business Rule Coverage**: All Given-When-Then rules captured in domain model
- **Aggregate Boundaries**: Clear consistency boundaries with single aggregate roots
- **Ubiquitous Language**: Consistent domain terminology throughout

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Domain Model Design (04/16)  
> 🎯 **Phase Purpose**: Design domain models and entities based on DDD principles  
> ⬅️ **Previous Stage**: 03-create-use-case (Use Case Specification)  
> ➡️ **Next Stage**: 05-create-tests (TDD Test Creation)

## 🎯 PHASE PURPOSE: DOMAIN MODEL DESIGN ONLY

**⚠️ Important Notice:**
- **This step focuses on DESIGN DOCUMENTATION** - Create domain model specifications
- **NO CODE IMPLEMENTATION** - Pure design and documentation phase
- **DDD Tactical Design** - Focus on entities, value objects, aggregates, services

**What this step does:**
1. `03-create-use-case` ← Previous: Use case specifications  
2. `04-domain-modeling` ← **【YOU ARE HERE】Domain model design**
3. `05-create-tests` ← Next: TDD test creation
4. `06-implement-domain` ← Next: Domain layer implementation

**CREATE DOMAIN DESIGN DOCUMENTATION ONLY.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Issue numbers from command arguments
ISSUE_NUMBERS="$1"

# Read use case specifications for each issue
for issue_num in $(echo $ISSUE_NUMBERS | tr ',' ' '); do
    USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f | head -1)
    if [[ -f "$USE_CASE_FILE" ]]; then
        Read "$USE_CASE_FILE"
    fi
done

# Read project vision for ubiquitous language
if [[ -f "docs/vision/project-vision.md" ]]; then
    Read docs/vision/project-vision.md
fi

# Read existing domain models for consistency
if [[ -d "docs/domain" ]]; then
    Glob docs/domain/*.md
fi
```

### GitHub Issue Integration
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBERS" ]]; then
    for issue_num in $(echo $ISSUE_NUMBERS | tr ',' ' '); do
        # Retrieve issue details with recent comments prioritized
        Bash gh issue view $issue_num --json title,body,comments
        Bash gh issue view $issue_num --json comments --jq '.comments | sort_by(.createdAt) | reverse | .[0:5]'
    done
fi
```

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析 (ユーザーとのやり取りは日本語):**

1. **ユースケース仕様の分析**
   - Extract domain concepts from Given-When-Then scenarios using Read tool
   - Identify entities (objects with identity and lifecycle)
   - Identify value objects (immutable, replaceable objects)
   - Extract business rules and invariants

2. **既存ドメインモデルとの整合性確認**
   - Check existing domain models using Glob tool
   - Ensure consistency with established ubiquitous language
   - Identify reusable domain patterns

### Phase 2: 設計と計画
**専門家として以下を設計 (Claude Codeへの指示は英語):**

1. **エンティティ設計**
   ```
   For each identified entity:
   - Define entity identity and lifecycle
   - Specify entity behavior and methods
   - Document business rules and invariants
   - Define relationships with other entities
   ```

2. **値オブジェクト設計**
   ```
   For each identified value object:
   - Define immutable properties
   - Specify validation rules
   - Document equality semantics
   - Design factory methods if needed
   ```

3. **アグリゲート境界設計**
   ```
   For each aggregate:
   - Identify aggregate root
   - Define consistency boundaries
   - Specify business invariants
   - Design repository interface
   ```

### Phase 3: 実装と実行
**専門家として以下を実行 (Claude Codeへの指示は英語):**

1. **Validate issue numbers and prerequisites**
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /domain-modeling 1"
       exit 1
   fi
   
   # Check for use case specifications
   for issue_num in $(echo $1 | tr ',' ' '); do
       USE_CASE_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.md" -type f | head -1)
       if [[ ! -f "$USE_CASE_FILE" ]]; then
           echo "❌ エラー: Issue #${issue_num} のユースケース仕様が見つかりません"
           echo "💡 先に /create-use-case ${issue_num} を実行してください"
           exit 1
       fi
   done
   ```

2. **Create domain model documents**
   ```bash
   # Create docs/domain directory if not exists
   Bash mkdir -p docs/domain
   
   # For each issue, create domain model document
   for issue_num in $(echo $1 | tr ',' ' '); do
       DOMAIN_FILE="docs/domain/issue-${issue_num}-domain-model.md"
       
       # Create comprehensive domain model document
       Write "$DOMAIN_FILE" with domain model content including:
       # - Domain overview and bounded context
       # - Entity definitions with behavior
       # - Value object specifications
       # - Aggregate boundaries and roots
       # - Domain services for complex logic
       # - Repository interfaces
       # - Domain events if applicable
       # - Business rules and invariants
       # - Ubiquitous language definitions
   done
   ```

3. **Update project metadata**
   ```bash
   # Update use case metadata files
   for issue_num in $(echo $1 | tr ',' ' '); do
       METADATA_FILE=$(find docs/use_cases/ -name "*issue*${issue_num}*.json" -type f | head -1)
       if [[ -f "$METADATA_FILE" ]]; then
           # Update metadata to mark domain modeling as complete
           # Set phases.domain_model.created to true
           # Add domain model file reference
       fi
   done
   
   # Update use cases index
   if [[ -f "docs/use_cases/index.md" ]]; then
       # Update index to reflect domain modeling completion status
   fi
   ```

4. **Git commit domain models**
   ```bash
   Bash git add docs/domain/
   Bash git commit -m "feat: create domain models for issues $(echo $1 | tr ',' ' ')

Design entities, value objects, and aggregates based on DDD principles.
Extract business rules from Given-When-Then scenarios.

🎯 Generated with Claude Code
"
   ```

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] すべてのユースケース仕様が分析されている
- [ ] エンティティが適切に識別され設計されている
- [ ] 値オブジェクトが適切に定義されている
- [ ] アグリゲート境界が明確に設定されている
- [ ] ビジネスルールがドメイン層に適切に配置されている
- [ ] リポジトリインターフェースが定義されている

**推奨項目（SHOULD）:**
- [ ] ドメインサービスが適切に設計されている
- [ ] ドメインイベントが識別されている
- [ ] ユビキタス言語が一貫して使用されている
- [ ] 既存ドメインモデルとの整合性が確保されている

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| ビジネスルールカバレッジ | 100% | [実績値] | ✅/❌ |
| アグリゲート設計品質 | 90% | [実績値] | ✅/❌ |
| ユビキタス言語一貫性 | 95% | [実績値] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **ユースケース仕様不足**: 先に /create-use-case を実行するよう日本語で案内
2. **アグリゲート境界の曖昧さ**: ビジネスルールの再確認を促す
3. **ドメイン概念の重複**: 既存モデルとの統合を検討

## 📊 標準化出力フォーマット

### 実行サマリー (日本語でユーザーに報告)
- ✅ **ユースケース仕様分析**: [Issue numbers] の仕様を分析完了
- ✅ **ドメインモデル設計**: エンティティ X個、値オブジェクト Y個を設計
- ✅ **アグリゲート境界定義**: Z個のアグリゲートを定義完了
- ✅ **ドキュメント作成**: docs/domain/issue-X-Y-domain-model.md 作成

### 成果物
**作成されたファイル:**
- `docs/domain/issue-X-Y-domain-model.md`: ドメインモデル設計書
- Updated metadata files: 対応する use case metadata の更新

### 総合判定
**ステータス**: `SUCCESS`
**品質スコア**: [スコア]/100  
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)
1. **即座に実行可能**: `/create-tests [issue-numbers]`
2. **推奨**: TDDテスト作成フェーズに進む
3. **確認推奨**: ドメインモデル設計のレビュー

### メタデータ更新
```bash
# Update project state metadata
if [[ -f "docs/metadata/project-state.json" ]]; then
    # Update overall_status to "domain_model_designed"
    # Increment domain modeling completions
    # Update architecture overview with domain metrics
fi
```

**ユーザーへのメッセージ (日本語)**:
```
🎉 ドメインモデリング完了！

🏗️ ドメイン設計要素:
   📊 エンティティ: [count] 個
   📊 値オブジェクト: [count] 個  
   📊 アグリゲート: [count] 個
   📊 ドメインサービス: [count] 個

📁 作成されたファイル:
   ✅ docs/domain/issue-X-Y-domain-model.md

📋 次のステップ (TDD テスト作成):
   /create-tests [issue-numbers]

✅ ドメインモデリング完了 - TDD テスト作成準備完了！
```