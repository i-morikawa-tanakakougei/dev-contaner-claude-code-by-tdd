# 03-create-use-case-enhanced (MCP-Enhanced Use Case Creation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Requirements Analysis and Use Case Design Expert** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Requirements Engineering Expertise:**

- **Requirements Engineering**: Comprehensive requirement extraction from GitHub issues with specification conflict resolution and stakeholder alignment
- **Use Case Architecture**: Detailed use case specification design with Given-When-Then scenario modeling and acceptance test creation
- **Domain Analysis**: Domain concept identification with ubiquitous language integration and boundary context alignment
- **Test Design**: Acceptance test case creation with comprehensive edge case coverage and automated testing preparation

**MCP-Enhanced Capabilities:**

- **Intelligent Pattern Discovery**: Automated use case pattern analysis using Serena MCP
- **Context-Rich Requirements**: Context7-enhanced requirements gathering with industry best practices
- **Cross-Reference Analysis**: Complete use case dependency mapping and optimization using Serena MCP
- **Best Practice Integration**: Latest requirements engineering techniques from Context7 MCP

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Issue-Driven Analysis**: Extract comprehensive requirements from GitHub issues including comment history and specification evolution
2. **Scenario Completeness**: Create main scenarios, alternative flows, edge cases, and exception handling with full test coverage
3. **Domain Consistency**: Ensure all domain concepts align with established ubiquitous language and bounded context
4. **Implementation Readiness**: Produce specifications that enable direct TDD implementation without ambiguity

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Leverage Serena for historical use case pattern discovery and optimization
6. **Context-Rich Analysis**: Enhance requirements with Context7 industry standards and best practices
7. **Data-Driven Decisions**: Base use case design on historical success patterns and market intelligence

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Requirement Coverage**: All GitHub issue requirements converted to Given-When-Then scenarios
- **Comment Integration**: Comment history properly analyzed with latest specifications reflected
- **Scenario Completeness**: Main flow, alternative flows, and exception handling all defined
- **Domain Consistency**: All concepts consistent with ubiquitous language

**MCP-Enhanced Standards:**

- **Pattern Discovery Coverage**: 95% of relevant use case patterns identified and applied
- **Requirements Intelligence**: 100% requirements analyzed with Context7 industry best practices
- **Cross-Reference Accuracy**: 100% use case dependency mapping with comprehensive analysis
- **Implementation Readiness**: 95% specifications ready for direct TDD implementation

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Pattern Discovery + Requirements Analysis) + Context7 (Requirements Best Practices + Industry Standards)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Enhanced Use Case Specification (03/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Convert GitHub issues into detailed implementable specifications with MCP intelligence  
> ⬅️ **Previous Stage**: 02-sprint-planning or 02-sprint-planning-enhanced  
> ➡️ **Next Stage**: 04-domain-modeling or 04-domain-modeling-enhanced

## 🎯 PHASE PURPOSE: ENHANCED USE CASE SPECIFICATION WITH MCP INTELLIGENCE

**⚠️ Important Notice:**

- **This step focuses on INTELLIGENT SPECIFICATION CREATION** - Convert GitHub issues into comprehensive Given-When-Then specifications with MCP-enhanced analysis
- **NO IMPLEMENTATION** - Focus only on requirements analysis and specification design with intelligence
- **GITHUB ISSUE INTEGRATION with MCP** - Prioritize recent comments and track specification evolution with intelligent pattern analysis

**What this enhanced step does:**

1. `02-sprint-planning-enhanced` ← Previous: Sprint tickets already created
2. `03-create-use-case-enhanced <issue-number>` ← **【YOU ARE HERE】Enhanced specification creation with MCP intelligence**
3. `04-domain-modeling-enhanced <issue-number>` ← Next: Design domain model from enhanced use cases
4. Then proceed with TDD implementation workflow

**Core Activities (Traditional):**

- Extract comprehensive requirements from GitHub issues and comments
- Create detailed Given-When-Then scenarios with full test coverage
- Analyze domain concepts and ensure ubiquitous language consistency
- Design acceptance test cases with edge case coverage

**MCP-Enhanced Activities (Additional):**

- Analyze similar use case patterns using Serena MCP for optimization and best practices
- Apply Context7 requirements engineering best practices for comprehensive specification
- Extract intelligent insights from issue comment history and stakeholder feedback
- Create cross-referenced requirements with dependency analysis and risk assessment
- Generate intelligent test scenario recommendations based on industry patterns

**ANALYZE GITHUB ISSUES WITH MCP INTELLIGENCE. DO NOT IMPLEMENT CODE.**

## 📋 Intelligent MCP Integration Setup

### Use Case Creation with MCP Integration

```bash
#!/bin/bash
# Use Case Creation with Intelligent MCP Integration

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /create-use-case-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Use Case Creation with Intelligent MCP Integration for Issue #$ISSUE_NUMBER"

# Step 1: Analyzing task complexity and requirements
echo "📊 Analyzing task complexity and requirements..."
echo "🎯 Task Type: Implementation Task (Use case specification creation)"
echo "📋 Components: GitHub Issue Analysis + Given-When-Then Creation + Documentation"

# Step 2: Checking MCP availability  
echo "🔧 Checking MCP availability..."

# Check Serena MCP availability
if command -v mcp__serena__get_symbols_overview &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - standard mode"
    MCP_SERENA="unavailable" 
fi

# Check Context7 MCP availability
if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"  
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - standard mode"
    MCP_CONTEXT7="unavailable"
fi

# Step 3: Standard task - Using Serena + Context7 integration
echo "⚡ Standard task - Using Serena + Context7 integration"
echo "📋 Use case creation is an implementation task suitable for standard execution:"
echo "  • GitHub Issue analysis and requirements extraction"
echo "  • Given-When-Then scenario creation from requirements"  
echo "  • Documentation generation and specification writing"

# Graceful Degradation
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without pattern analysis - manual specification creation"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard approaches"
fi

# Step 4: GitHub Issue Requirements Loading (Simple & Comment-Focused)
echo "📋 Loading GitHub issue requirements..."

# Basic issue data retrieval
if command -v gh &> /dev/null; then
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt 2>/dev/null)
    
    if [[ $? -eq 0 ]]; then
        echo "✅ GitHub issue #$ISSUE_NUMBER loaded"
        
        # Simple comment analysis with recency priority
        COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
        
        if [[ $COMMENT_COUNT -gt 0 ]]; then
            echo "📊 Found $COMMENT_COUNT comments"
            echo "⚠️ PRIORITY: Recent comments contain the most current requirements"
            echo "📅 Implementation should prioritize latest comment content over original description"
            
            # Display recent comments summary (simple)
            echo "📋 Latest Comments (most recent first):"
            echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.updatedAt) | reverse | .[0:3] | .[] | "  💬 [\(.updatedAt)] @\(.author.login): \(.body | split("\n")[0] | .[0:100])..."'
        else
            echo "📝 No comments found - using original issue description"
        fi
        
        # Display issue summary
        echo "📄 Issue: $(echo "$ISSUE_DATA" | jq -r '.title')"
        echo "📅 Last Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
        
    else
        echo "⚠️ GitHub CLI failed - falling back to specification files"
    fi
else
    echo "ℹ️ GitHub CLI not available - using specification files"
fi

echo "🎯 Proceeding with use case creation based on latest requirements..."
echo "⏰ Ready for use case specification creation..."
```

## 🚀 Expert Execution Flow

### Phase 1: GitHub Issue Analysis with MCP Support

**Execute comprehensive issue analysis (Instructions to Claude Code in English):**

1. **GitHub Issue Data Processing**

   ```
   Parse GitHub issue data retrieved from setup phase:
   - Extract issue title, body, and metadata for requirements analysis
   - Analyze recent comments with priority on latest specifications
   - Identify acceptance criteria hints and validation requirements
   - Document edge cases and exception scenarios mentioned
   - Extract integration and dependency requirements from discussion
   ```

2. **MCP-Enhanced Issue Analysis (if available)**

   ```
   If MCP_SERENA is available:
   - Use mcp__serena__search_for_pattern to find similar use cases
   - Use mcp__serena__list_memories for use case pattern templates
   - Use mcp__serena__get_symbols_overview to understand project structure

   If MCP_CONTEXT7 is available:
   - Use mcp__context7__resolve-library-id for "requirements-engineering"
   - Use mcp__context7__get-library-docs for use case specification best practices
   - Apply industry-standard Given-When-Then patterns and methodologies
   ```

3. **Project Context Analysis**

   ```
   Read project context documents for alignment:
   - Use Read tool for docs/vision/project-vision.md (if exists)
   - Use Read tool for docs/vision/bounded_context.md (if exists) 
   - Use Read tool for docs/vision/ubiquitous_language.md (if exists)
   - Ensure domain concept consistency with established terminology
   ```

### Phase 2: Use Case Specification Creation with MCP Intelligence

**Execute use case specification development (Instructions to Claude Code in English):**

1. **Requirements Analysis and Extraction**

   ```
   Comprehensive requirements extraction from GitHub issue:
   - Core functional requirements from issue title and description
   - Additional requirements from recent comments with priority analysis
   - Acceptance criteria hints and validation requirements
   - Edge cases and exception scenarios mentioned in discussion
   - Integration and dependency requirements
   - Performance and quality requirements if specified
   ```

2. **Given-When-Then Scenario Creation**

   ```
   Create comprehensive use case scenarios:
   - Main Scenario (Happy Path): Primary user flow with success conditions
   - Alternative Scenarios: Alternate valid paths and workflow variations
   - Exception Scenarios: Error handling, validation failures, edge cases
   - Integration Scenarios: External system interactions if applicable
   
   Enhanced with MCP pattern analysis and Context7 best practices if available
   ```

3. **Domain Concept Identification**

   ```
   Identify and define domain concepts with MCP intelligence:
   - Extract domain entities, value objects, and services from requirements
   - Align terminology with project ubiquitous language
   - Apply Context7 domain modeling patterns if available
   - Use Serena pattern matching for similar domain concepts if available
   ```

### Phase 3: Documentation and Quality Assurance

**Execute comprehensive documentation with MCP learning integration (Instructions to Claude Code in English):**

1. **Create use case documentation structure**

   ```
   Generate use case directory and documentation:
   Create directory: docs/use_cases/issue-${ISSUE_NUMBER}/
   
   Write "docs/use_cases/issue-${ISSUE_NUMBER}/use-case-specification.md" including:
   - Issue reference and context information
   - Comprehensive Given-When-Then scenarios with clear conditions
   - Domain concept definitions aligned with ubiquitous language
   - Acceptance criteria with test case references
   - Dependencies and integration requirements
   - Quality attributes and non-functional requirements
   ```

2. **Create supporting documentation**

   ```
   Generate acceptance test cases and traceability:
   Write "docs/use_cases/issue-${ISSUE_NUMBER}/acceptance-test-cases.md" including:
   - Test scenarios mapped to Given-When-Then specifications
   - Test data requirements and fixture specifications  
   - Expected outcomes with validation criteria
   - Edge case and exception handling test cases

   Write "docs/use_cases/issue-${ISSUE_NUMBER}/requirements-traceability.md" including:
   - GitHub issue requirements mapped to scenarios
   - Comment evolution tracking with specification changes
   - Domain concept usage and consistency tracking
   - Test case coverage matrix
   ```

3. **MCP-enhanced documentation (if available)**

   ```
   If MCPs were used, create additional analysis documentation:
   Write "docs/use_cases/issue-${ISSUE_NUMBER}/mcp-analysis.md" including:
   - Serena pattern analysis results and similar use case insights
   - Context7 requirements engineering best practice integration
   - Cross-reference dependency analysis and recommendations
   - Gap analysis and specification completeness assessment
   ```

4. **MCP learning and memory storage**

   ```
   If MCP_SERENA is available, store learning insights:
   Use mcp__serena__write_memory to record:
   - Use case creation insights for "use-case-patterns-$(date +%Y%m%d)"
   - Requirements analysis learnings for "requirements-templates-$(date +%Y%m%d)" 
   - Domain concept patterns for "domain-concepts-$(date +%Y%m%d)"
   ```

5. **Git commit documentation**

   ```
   Bash git add docs/use_cases/issue-${ISSUE_NUMBER}/
   Bash git commit -m "feat: create use case specification for issue ${ISSUE_NUMBER}

   Comprehensive Given-When-Then scenarios from GitHub issue analysis.
   Includes acceptance test cases and requirements traceability.

   🎯 Generated with Claude Code
   "
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Use Case Analysis Completion (MUST):**

- [ ] GitHub issue requirements fully analyzed and converted to scenarios
- [ ] All Given-When-Then scenarios created with comprehensive coverage
- [ ] Domain concepts identified and aligned with ubiquitous language
- [ ] Acceptance test cases created with clear validation criteria
- [ ] Requirements traceability matrix completed
- [ ] Documentation structure properly created

**MCP Integration Quality (if available):**

- [ ] Serena MCP use case pattern analysis utilized (if available)
- [ ] Context7 requirements engineering best practices integrated (if available)
- [ ] Cross-reference analysis and gap assessment performed (if available)
- [ ] MCP learning insights stored for future reference (if available)

**Documentation Quality (MUST):**

- [ ] Use case specification document created with clear scenarios
- [ ] Acceptance test cases documented with validation criteria
- [ ] Requirements traceability established and documented
- [ ] All documentation committed to version control

**Implementation Readiness (SHOULD):**

- [ ] Domain concepts clearly defined and consistent
- [ ] Test scenarios cover main flow, alternatives, and exceptions
- [ ] Integration requirements identified where applicable
- [ ] Specification ready for domain modeling phase

### Quality Assessment

| Quality Area | Assessment Criteria | Status |
|--------------|-------------------|--------|
| **Requirements Coverage** | All issue requirements converted to scenarios | ✅/❌ |
| **Scenario Completeness** | Main, alternative, and exception flows covered | ✅/❌ |
| **Domain Alignment** | Concepts consistent with ubiquitous language | ✅/❌ |
| **Test Readiness** | Clear acceptance criteria and test cases | ✅/❌ |
| **MCP Integration** | Available MCPs effectively utilized | ✅/❌/N/A |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本分析完了:**

- ✅ **GitHub Issue分析**: Issue詳細、コメント履歴、要求の包括的分析完了
- ✅ **要求抽出**: 機能要求、受け入れ基準、制約条件の体系的抽出完了
- ✅ **シナリオ作成**: Given-When-Then形式での完全なユースケース仕様作成完了
- ✅ **テスト仕様**: 受け入れテストケースと検証基準の詳細化完了

**MCP 拡張分析 (利用可能時):**

- ✅ **Serena パターン分析**: 類似ユースケースパターンの発見と適用
- ✅ **Context7 統合**: 最新要求工学手法とベストプラクティス適用
- ✅ **相互参照分析**: 依存関係マッピングと統合要件分析
- ✅ **学習記録**: 今回の分析結果をMCPメモリに永続化

### 成果物

**必須ドキュメント:**

- `docs/use_cases/issue-${ISSUE_NUMBER}/use-case-specification.md`: 詳細ユースケース仕様書
- `docs/use_cases/issue-${ISSUE_NUMBER}/acceptance-test-cases.md`: 受け入れテストケース仕様
- `docs/use_cases/issue-${ISSUE_NUMBER}/requirements-traceability.md`: 要求トレーサビリティ

**MCP 拡張ドキュメント (利用可能時):**

- `docs/use_cases/issue-${ISSUE_NUMBER}/mcp-analysis.md`: MCP分析結果とインサイト
- Serena MCPメモリファイル: 学習結果の永続化とパターン蓄積

### 総合判定

**実装準備状況**: `READY` / `CONDITIONAL` / `REVISION_REQUIRED`
**主要成果**: [作成されたシナリオ数とドメイン概念の要約]  
**推奨次ステップ**: [ドメインモデリングフェーズへの移行推奨]

### 次のステップ (日本語でユーザーに案内)

1. **仕様承認時**: `/domain-modeling-enhanced ${ISSUE_NUMBER}` でドメインモデル設計開始
2. **仕様調整時**: 関係者レビュー後、必要に応じて仕様を調整
3. **確認推奨**: ドメイン概念とユビキタス言語の整合性確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 ユースケース仕様作成完了！

📊 ユースケース分析結果:
   ✅ 実装準備状況: [READY/CONDITIONAL/REVISION_REQUIRED]
   📋 シナリオ作成: [メイン・代替・例外シナリオの要約]
   🎯 ドメイン概念: [特定されたドメイン概念]
   📝 テスト仕様: [作成されたテストケース数]

💡 仕様分析結果:
   🎯 強み: [仕様の優位性]
   ⚡ 注意点: [実装時の留意事項]
   🔄 依存関係: [特定された依存関係]

🧠 MCP分析強化 (利用時):
   📊 Serena分析: ユースケースパターンと類似事例の発見
   🔍 Context7 統合: 最新要求工学手法を適用
   🌐 学習記録: 今回の知見をパターンライブラリに蓄積

📁 生成ドキュメント:
   ✅ docs/use_cases/issue-${ISSUE_NUMBER}/use-case-specification.md
   ✅ docs/use_cases/issue-${ISSUE_NUMBER}/acceptance-test-cases.md  
   ✅ docs/use_cases/issue-${ISSUE_NUMBER}/requirements-traceability.md

🚀 次のアクション:
   📋 `/domain-modeling-enhanced ${ISSUE_NUMBER}` でドメインモデル設計開始

✅ ユースケース仕様作成完了 - ドメインモデリング準備完了！
```

## Common Errors and Solutions

### ❌ Error Case 1: GitHub issue not found or inaccessible
**Cause**: Invalid issue number or authentication problems  
**Solution**: 
- Verify issue number exists in the repository
- Check GitHub CLI authentication: `gh auth status`
- Ensure repository access permissions

### ❌ Error Case 2: Insufficient requirements in issue description
**Cause**: Issue lacks detailed requirements or acceptance criteria  
**Solution**: 
- Engage with issue reporter for clarification
- Review issue comments for additional context
- Document assumptions and seek validation

### ❌ Error Case 3: Domain concept conflicts with existing terminology
**Cause**: New requirements conflict with established ubiquitous language  
**Solution**: 
```bash
# Review existing domain concepts
/review-domain-concepts --compare-with issue-${ISSUE_NUMBER}
# Align terminology with domain experts
```

## Execution Examples

### ✅ Success Example - Full Use Case Creation with MCP
```bash
$ /create-use-case-enhanced 123

🚀 Use Case Creation with Intelligent MCP Integration for Issue #123

📊 GitHub Issue分析:
  📋 Issue: "Add user profile management functionality"
  💬 コメント: 5件の仕様更新を発見
  📅 最新更新: 2023-12-01

⚡ MCP分析結果:
  📊 Serena: 3件の類似ユースケースパターンを発見
  🌐 Context7: 最新のユーザー管理ベストプラクティスを適用

✅ ユースケース仕様作成完了:
  📋 メインシナリオ: ユーザープロフィール作成・更新・削除
  🔄 代替シナリオ: バリデーション失敗時の処理
  ⚠️ 例外シナリオ: 権限不足・重複データ処理
  ✅ テストケース: 15個の受け入れテスト仕様

📁 成果物:
  ✅ docs/use_cases/issue-123/use-case-specification.md
  ✅ docs/use_cases/issue-123/acceptance-test-cases.md
  ✅ docs/use_cases/issue-123/requirements-traceability.md

🚀 次のステップ: `/domain-modeling-enhanced 123`
```