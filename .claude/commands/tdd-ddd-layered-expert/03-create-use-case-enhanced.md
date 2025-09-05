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

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-use-case-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Executing MCP-enhanced create-use-case for GitHub Issue #$ISSUE_NUMBER..."

# MCP Enhanced: Session availability check
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "🔍 Enhanced Analysis Mode: MCP capabilities enabled"
    echo "  🧠 Serena: Use case pattern analysis and cross-reference mapping"
    echo "  📚 Context7: Requirements engineering best practices"
    MCP_AVAILABLE="true"
else
    echo "📋 Standard Mode: Core use case creation without MCP enhancements"
    MCP_AVAILABLE="false"
fi

# CRITICAL: Retrieve GitHub issue with full comment history first
echo "📥 Retrieving GitHub issue #$ISSUE_NUMBER with complete comment history..."

# Get issue details with comments using gh CLI
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees 2>/dev/null)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "❌ Failed to retrieve issue #$ISSUE_NUMBER. Please check:"
    echo "  - Issue number exists"
    echo "  - GitHub CLI is authenticated"
    echo "  - Repository access permissions"
    exit 1
fi

# Extract and analyze comments (prioritize recent ones)
COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
echo "📊 Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"

if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "🔍 Analyzing comment timeline for latest requirements..."
    # Get latest 5 comments (most recent first)
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "📅 Latest specification update: $LATEST_COMMENT_DATE"
        echo "⚠️  PRIORITY: Recent comments take precedence over original issue description"
    fi
    
    # Display recent comment summary
    echo "📋 Recent Comments Summary:"
    echo "$RECENT_COMMENTS" | jq -r '.[] | "  [" + .createdAt + "] @" + .author.login + ": " + (.body | split("\n")[0] | .[0:80] + (if length > 80 then "..." else "" end))'
else
    echo "📝 No comments found. Using original issue description only."
fi

# Display issue summary
echo "📄 Issue Summary:"
echo "  Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "  Created: $(echo "$ISSUE_DATA" | jq -r '.createdAt')"
echo "  Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')"
echo "  Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name // empty' | tr '\n' ', ' | sed 's/,$//')"

# Save issue data for use case creation process
TEMP_ISSUE_FILE="/tmp/issue-${ISSUE_NUMBER}-data.json"
echo "$ISSUE_DATA" > "$TEMP_ISSUE_FILE"
echo "💾 Issue data saved to: $TEMP_ISSUE_FILE"
```

### Optional Reading (As Needed)
- Project vision: `docs/vision/project-vision.md` (understand overall context)
- Bounded context: `docs/vision/bounded_context.md` (verify domain boundaries)
- Sprint plan: `docs/sprint/sprint_*_plan.md` (understand sprint context)
- Related use cases: `docs/use_cases/*/issue-*/` (identify patterns and dependencies)

## GitHub Issue Integration (Enhanced)

### Enhanced Issue Comment Retrieval and Analysis
```bash
# Enhanced issue analysis with MCP intelligence
echo "Retrieving GitHub issue #$ISSUE_NUMBER with enhanced analysis..."

# Get issue details with comments
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees)

# MCP Enhanced: Pattern-based issue analysis
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced: Analyzing issue patterns and requirements intelligence..."
    echo "📊 Enhanced: Cross-referencing similar use cases and industry patterns..."
fi

# Extract and prioritize recent comments
RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')

COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length')
echo "Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"
echo "Prioritizing latest 5 comments for specification analysis"

# Check for specification conflicts and evolution
if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "Analyzing comment timeline for requirement evolution..."
    # Recent comments take precedence over original issue description
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "Latest specification update: $LATEST_COMMENT_DATE"
    fi
fi
```

### Specification Evolution Tracking with MCP
```markdown
## Enhanced Comment Analysis Strategy

1. **Latest First with Intelligence**: Recent comments override earlier specifications with MCP pattern analysis
2. **Authority Recognition Enhanced**: Identify specification authors vs. discussants with stakeholder analysis
3. **Conflict Resolution with Context**: Resolve specification conflicts using Context7 best practices
4. **Cross-Reference Analysis**: Serena MCP analysis of similar issue patterns and resolutions
```

## 🚀 MCP強化ユースケース作成実行フロー

```bash
#!/bin/bash
# MCP-Enhanced Use Case Creation

echo "📋 MCP-Enhanced Use Case Creation..."

# Phase 1: 引数検証・MCP環境確認
echo "📚 Phase 1: Argument validation and MCP session analysis..."

# Issue番号検証
if [[ -z "$1" ]]; then
    echo "❌ ERROR: Issue number required. Usage: /create-use-case-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🎯 Creating enhanced use case specification for Issue #${ISSUE_NUMBER} with MCP intelligence..."

# MCP利用可能性確認
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced requirements analysis available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Use case pattern discovery and cross-reference analysis"
    echo "  • Context7: Requirements engineering best practices"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Intelligent use case pattern analysis"
    echo "  • Requirements engineering best practice integration"
    echo "  • Cross-reference dependency mapping"
    echo "  • Industry-standard scenario templates"
    MCP_AVAILABLE="false"
fi

# Phase 2: GitHub Issue詳細取得・分析
echo "📥 Phase 2: GitHub issue retrieval and analysis..."

# CRITICAL: Retrieve GitHub issue with full comment history first
echo "📥 Retrieving GitHub issue #$ISSUE_NUMBER with complete comment history..."

# Get issue details with comments using gh CLI
ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt,labels,assignees 2>/dev/null)
EXIT_CODE=$?

if [[ $EXIT_CODE -ne 0 ]]; then
    echo "❌ Failed to retrieve issue #$ISSUE_NUMBER. Please check:"
    echo "  - Issue number exists"
    echo "  - GitHub CLI is authenticated" 
    echo "  - Repository access permissions"
    exit 1
fi

# Extract and analyze comments (prioritize recent ones)
COMMENT_COUNT=$(echo "$ISSUE_DATA" | jq '.comments | length // 0')
echo "📊 Found $COMMENT_COUNT comments on issue #$ISSUE_NUMBER"

if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "🔍 Analyzing comment timeline for latest requirements..."
    # Get latest 5 comments (most recent first)
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    LATEST_COMMENT_DATE=$(echo "$RECENT_COMMENTS" | jq -r '.[0].createdAt // empty')
    
    if [[ -n "$LATEST_COMMENT_DATE" ]]; then
        echo "📅 Latest specification update: $LATEST_COMMENT_DATE"
        echo "⚠️  PRIORITY: Recent comments take precedence over original issue description"
    fi
    
    # Display recent comment summary
    echo "📋 Recent Comments Summary:"
    echo "$RECENT_COMMENTS" | jq -r '.[] | "  [" + .createdAt + "] @" + .author.login + ": " + (.body | split("\n")[0] | .[0:80] + (if length > 80 then "..." else "" end))'
else
    echo "📝 No comments found. Using original issue description only."
fi

# Display issue summary
echo "📄 Issue Summary:"
echo "  Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "  Created: $(echo "$ISSUE_DATA" | jq -r '.createdAt')"
echo "  Updated: $(echo "$ISSUE_DATA" | jq -r '.updatedAt')" 
echo "  Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name // empty' | tr '\n' ', ' | sed 's/,$//')"

# Save issue data for detailed analysis
TEMP_ISSUE_FILE="/tmp/issue-${ISSUE_NUMBER}-data.json"
echo "$ISSUE_DATA" > "$TEMP_ISSUE_FILE"
echo "💾 Issue data saved to: $TEMP_ISSUE_FILE"

# Phase 3: MCP拡張分析（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 3: MCP-enhanced requirements pattern analysis..."
    
    # Serenaユースケース・パターン分析
    echo "📚 Serena: Discovering historical use case patterns and requirements..."
    Use mcp__serena__search_for_pattern "use.*case|scenario|Given.*When.*Then|requirements|specification" --restrict_search_to_code_files=false
    Use mcp__serena__read_memory "use-case-patterns" if available
    Use mcp__serena__read_memory "requirements-templates" if available
    Use mcp__serena__list_memories to find use-case-related patterns
    
    # Context7要求工学・ベストプラクティス統合
    echo "🌐 Context7: Analyzing requirements engineering best practices..."
    Use mcp__context7__resolve-library-id "requirements-engineering"
    Use mcp__context7__resolve-library-id "use-case-modeling"
    Use mcp__context7__get-library-docs "/requirements-engineering" --topic "use-case-specification"
    Use mcp__context7__get-library-docs "/use-case-modeling" --topic "given-when-then"
    Use mcp__context7__get-library-docs "/requirements-engineering" --topic "acceptance-criteria"
    
    # インテリジェント要求分析
    echo "🔍 Intelligent requirements cross-reference analysis..."
    Use mcp__serena__search_for_pattern "acceptance|criteria|test|validation" --context_lines_before=2 --context_lines_after=2
    
else
    echo "📋 Phase 3: Standard mode - Basic requirements analysis"
fi

# Phase 4: プロジェクト・コンテキスト分析  
echo "🔍 Phase 4: Project context and domain analysis..."

# プロジェクト・ビジョン確認
if [[ -f "docs/vision/project-vision.md" ]]; then
    echo "📄 Loading project vision for context alignment..."
    Use Read tool to analyze docs/vision/project-vision.md
fi

# 境界コンテキスト確認
if [[ -f "docs/vision/bounded_context.md" ]]; then
    echo "📋 Loading bounded context for domain alignment..."
    Use Read tool to analyze docs/vision/bounded_context.md
fi

# ユビキタス言語確認
if [[ -f "docs/vision/ubiquitous_language.md" ]]; then
    echo "📚 Loading ubiquitous language for terminology consistency..."
    Use Read tool to analyze docs/vision/ubiquitous_language.md
fi

# 関連スプリント計画確認
SPRINT_PLAN=$(find docs/sprint/ -name "*plan.md" -type f | head -1 2>/dev/null)
if [[ -f "$SPRINT_PLAN" ]]; then
    echo "📊 Loading sprint context for priority alignment..."
    Use Read tool to analyze "$SPRINT_PLAN"
fi

# Phase 5: 要求分析・仕様設計
echo "📝 Phase 5: Enhanced requirements analysis and specification design..."

if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 MCP拡張モード: インテリジェント要求分析"
    echo "📊 履歴パターンと最新要求工学手法を活用して最適化された仕様を作成します"
fi

# GitHub Issue詳細分析
echo "🔍 Analyzing GitHub issue content with MCP enhancement..."
# Parse issue title, body, and recent comments for requirements extraction
Use the issue data from TEMP_ISSUE_FILE to extract:
- Core functional requirements from issue title and description
- Additional requirements from recent comments with priority analysis
- Acceptance criteria hints and validation requirements
- Edge cases and exception scenarios mentioned
- Integration and dependency requirements
- Performance and quality requirements

# Domain concept identification (enhanced with MCP if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🎯 Enhanced domain concept identification with MCP intelligence..."
    # Apply Context7 domain modeling patterns
    # Use Serena pattern matching for similar domain concepts
fi

# Phase 6: Given-When-Then シナリオ作成
echo "📋 Phase 6: Creating comprehensive Given-When-Then scenarios..."

Create detailed use case specifications with:
1. **Main Scenario (Happy Path)**: Primary user flow with success conditions
2. **Alternative Scenarios**: Alternate valid paths and variations
3. **Exception Scenarios**: Error handling and edge cases
4. **Integration Scenarios**: External system interactions if applicable
Enhanced with MCP pattern analysis and Context7 best practices if available

# ユーザーに日本語で仕様確認・追加情報収集
Ask user for the following specification validation in Japanese:
1. 抽出された要求の妥当性確認 (enhanced with pattern analysis if MCP available)
2. 不足している要求・シナリオの特定 (enhanced with gap analysis if MCP available)
3. 受け入れ基準の明確化 (enhanced with industry standards if MCP available)
4. テストケースの網羅性確認 (enhanced with test pattern analysis if MCP available)
5. ドメイン概念の整合性確認 (enhanced with domain pattern validation if MCP available)

# Phase 7: ユースケース・ディレクトリ作成
echo "📁 Phase 7: Creating use case documentation structure..."

# ユースケースディレクトリ作成
USE_CASE_DIR="docs/use_cases/issue-${ISSUE_NUMBER}"
Create directory: $USE_CASE_DIR if not exists

# Phase 8: 詳細仕様書作成
echo "📝 Phase 8: Creating comprehensive use case specification..."

# メインユースケース仕様書作成
USE_CASE_FILE="$USE_CASE_DIR/use-case-specification.md"
Create "$USE_CASE_FILE" with:
- Issue reference and context
- Comprehensive Given-When-Then scenarios with MCP enhancement
- Domain concept definitions aligned with ubiquitous language
- Acceptance criteria with test case references
- Dependencies and integration requirements
- Quality attributes and non-functional requirements

# 受け入れテストケース仕様書作成
ACCEPTANCE_TESTS_FILE="$USE_CASE_DIR/acceptance-test-cases.md"
Create "$ACCEPTANCE_TESTS_FILE" with:
- Test scenarios mapped to Given-When-Then specifications
- Test data requirements and fixture specifications
- Expected outcomes with validation criteria
- Edge case and exception handling test cases
- Performance and quality test requirements if applicable

# 要求トレーサビリティ・マトリックス作成
TRACEABILITY_FILE="$USE_CASE_DIR/requirements-traceability.md"
Create "$TRACEABILITY_FILE" with:
- GitHub issue requirements mapped to scenarios
- Comment evolution tracking with specification changes
- Domain concept usage and consistency tracking
- Test case coverage matrix
- Implementation readiness assessment

# Phase 9: MCP拡張文書作成（利用可能時）
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🧠 Phase 9: Creating MCP-enhanced analysis documents..."
    
    # MCP分析結果文書
    MCP_ANALYSIS_FILE="$USE_CASE_DIR/mcp-requirements-analysis.md"
    Create "$MCP_ANALYSIS_FILE" with:
    - Serena historical pattern analysis results
    - Context7 requirements engineering best practice integration
    - Cross-reference dependency analysis and recommendations
    - Intelligent gap analysis and specification completeness assessment
    
    # 要求パターン分析レポート
    PATTERN_ANALYSIS_FILE="$USE_CASE_DIR/requirements-pattern-analysis.md"
    Create "$PATTERN_ANALYSIS_FILE" with:
    - Similar use case patterns from Serena analysis
    - Industry-standard requirements templates from Context7
    - Best practice recommendations for implementation
    - Risk assessment and mitigation recommendations
    
    # Serena memory への学習内容保存
    Use mcp__serena__write_memory "use-case-creation-$(date +%Y%m%d)-issue-${ISSUE_NUMBER}" "Use case specification completed for issue ${ISSUE_NUMBER} with comprehensive Given-When-Then scenarios, Context7 requirements engineering patterns applied, and full traceability analysis"
fi

# Phase 10: メタデータ・JSON作成
echo "📊 Phase 10: Creating use case metadata and JSON specification..."

# ユースケース・メタデータJSON作成
METADATA_FILE="$USE_CASE_DIR/use-case-metadata.json"
Create "$METADATA_FILE" with comprehensive metadata:
{
  "issue_number": "${ISSUE_NUMBER}",
  "title": "$(echo "$ISSUE_DATA" | jq -r '.title')",
  "created_date": "[current timestamp]",
  "github_issue": {
    "created_at": "$(echo "$ISSUE_DATA" | jq -r '.createdAt')",
    "updated_at": "$(echo "$ISSUE_DATA" | jq -r '.updatedAt')",
    "comment_count": ${COMMENT_COUNT},
    "labels": $(echo "$ISSUE_DATA" | jq '.labels'),
    "latest_comment_date": "${LATEST_COMMENT_DATE:-null}"
  },
  "requirements": {
    "main_scenarios": "[count]",
    "alternative_scenarios": "[count]", 
    "exception_scenarios": "[count]",
    "domain_concepts": "[list]",
    "acceptance_criteria": "[count]"
  },
  "mcp_enhancements": {
    "pattern_analysis": [MCP_AVAILABLE],
    "context7_integration": [MCP_AVAILABLE],
    "cross_reference_analysis": [MCP_AVAILABLE],
    "intelligent_gap_analysis": [MCP_AVAILABLE]
  },
  "status": "SPECIFICATION_COMPLETE",
  "next_recommended": ["domain-modeling-enhanced"]
}

# Phase 11: Gitコミット
echo "📝 Phase 11: Git commit for use case specification..."

Use Bash tool: git add docs/use_cases/issue-${ISSUE_NUMBER}/

if [[ "$MCP_AVAILABLE" == "true" ]]; then
    Use Bash tool: git commit -m "feat: create use case specification for issue ${ISSUE_NUMBER} with MCP enhancement

Comprehensive Given-When-Then scenarios created from GitHub issue analysis.
Enhanced with MCP pattern discovery and Context7 requirements engineering.
Full traceability and acceptance test case specifications included.

🎯 Generated with Claude Code"
else
    Use Bash tool: git commit -m "feat: create use case specification for issue ${ISSUE_NUMBER}

Comprehensive Given-When-Then scenarios created from GitHub issue analysis.
Full traceability and acceptance test case specifications included.

🎯 Generated with Claude Code"
fi

# Phase 12: 品質保証・検証
echo "✅ Phase 12: Quality assurance and specification validation..."

# 品質チェックリスト実行
Verify the following quality standards:

**Required Items (MUST):**
- [ ] GitHub issue requirements fully analyzed and converted to scenarios
- [ ] All Given-When-Then scenarios created with comprehensive coverage
- [ ] Domain concepts identified and aligned with ubiquitous language
- [ ] Acceptance test cases created with clear validation criteria
- [ ] Requirements traceability matrix completed

**Recommended Items (SHOULD) - MCP Enhanced:**
- [ ] Serena MCP pattern analysis completed (if MCP available)
- [ ] Context7 requirements engineering best practices applied (if MCP available)
- [ ] Cross-reference dependency analysis performed (if MCP available)
- [ ] Intelligent gap analysis and completeness assessment (if MCP available)
- [ ] Implementation readiness assessment completed (if MCP available)

# Phase 13: 実行サマリー・次ステップ案内
echo "🎉 Phase 13: Completion summary and next steps..."

Display to user in Japanese:
## ✅ 実行サマリー

**基本機能 (常に実行):**
- ✅ **GitHub Issue分析**: Issue #${ISSUE_NUMBER} の詳細分析・コメント履歴解析完了
- ✅ **要求抽出**: 機能要求・受け入れ基準・制約条件の包括的抽出完了
- ✅ **Given-When-Thenシナリオ作成**: メイン・代替・例外シナリオの完全作成完了
- ✅ **受け入れテスト仕様**: テストケース・検証基準・データ要件の詳細化完了

**MCP拡張機能 (利用可能時):**
- ✅ **MCPパターン分析**: Serenaによる類似ユースケース・パターン発見完了
- ✅ **インテリジェント要求工学**: Context7最新手法・ベストプラクティス適用完了
- ✅ **相互参照分析**: 依存関係マッピング・統合要件分析完了
- ✅ **ギャップ分析**: インテリジェント仕様完全性評価・リスク識別完了

## 📁 成果物

**基本ファイル (常に作成):**
- `docs/use_cases/issue-${ISSUE_NUMBER}/use-case-specification.md`: 詳細ユースケース仕様書
- `docs/use_cases/issue-${ISSUE_NUMBER}/acceptance-test-cases.md`: 受け入れテストケース仕様
- `docs/use_cases/issue-${ISSUE_NUMBER}/requirements-traceability.md`: 要求トレーサビリティ・マトリックス
- `docs/use_cases/issue-${ISSUE_NUMBER}/use-case-metadata.json`: メタデータ・実行履歴JSON

**MCP拡張ファイル (利用可能時):**
- `docs/use_cases/issue-${ISSUE_NUMBER}/mcp-requirements-analysis.md`: MCP要求分析結果
- `docs/use_cases/issue-${ISSUE_NUMBER}/requirements-pattern-analysis.md`: 要求パターン分析レポート
- Enhanced specifications with intelligent insights and industry best practices
- Updated MCP memory files: ユースケース作成結果の永続化

## 🚀 次のステップ

1. **即座に実行可能**: `/domain-modeling-enhanced ${ISSUE_NUMBER}` でドメインモデル設計
2. **推奨**: 作成された仕様書のレビューと関係者による検証
3. **確認推奨**: ドメイン概念とユビキタス言語の整合性確認

**📋 Use Case Specification完了 - 実装準備完了**

# Cleanup
rm -f "$TEMP_ISSUE_FILE"

# メタデータ更新
Create docs/metadata/command-execution-log.json entry with:
{
  "command_executed": "create-use-case-enhanced",
  "timestamp": "[current timestamp]",
  "status": "SUCCESS",
  "phase": "use-case-specification",
  "issue_number": "${ISSUE_NUMBER}",
  "mcp_enhancements": {
    "serena_pattern_analysis": [MCP_AVAILABLE],
    "context7_requirements_engineering": [MCP_AVAILABLE],
    "cross_reference_analysis": [MCP_AVAILABLE],
    "intelligent_gap_analysis": [MCP_AVAILABLE]
  },
  "metrics": {
    "github_comments_analyzed": "${COMMENT_COUNT}",
    "scenarios_created": "[number]",
    "acceptance_tests_created": "[number]",
    "domain_concepts_identified": "[number]"
  },
  "next_recommended": ["domain-modeling-enhanced"]
}

echo "🎯 MCP強化ユースケース仕様作成が完了しました！"
```

---

🎯 **MCP強化ユースケース仕様作成コマンド完成**

**使用方法**:
```bash
/create-use-case-enhanced <issue-number>
```

**MCP拡張機能** (利用可能時):
- 🧠 **Serena**: ユースケースパターン発見・相互参照分析
- 📚 **Context7**: 要求工学・ベストプラクティス統合