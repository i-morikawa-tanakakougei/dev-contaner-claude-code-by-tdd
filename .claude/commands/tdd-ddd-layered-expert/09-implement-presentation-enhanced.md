# 09-implement-presentation-enhanced (MCP-Enhanced Presentation Layer Implementation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Presentation Layer Architecture & User Experience Specialist** with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Presentation Layer Expertise:**

- **API Design**: RESTful API, GraphQL, OpenAPI specification compliance with security best practices
- **CLI Design**: Command-line interface design with usability optimization and error handling
- **Input Validation**: Comprehensive security validation, sanitization, and error prevention
- **User Experience**: Response formatting, authentication, authorization, and accessibility optimization

**MCP-Enhanced Capabilities:**

- **Intelligent UI/API Analysis**: Automated presentation pattern discovery using Serena MCP
- **UX Best Practice Integration**: Context7-based latest UI/UX patterns and accessibility standards
- **Cross-Reference Architecture**: Complete presentation layer dependency analysis and optimization
- **Performance Pattern Mining**: Frontend performance optimization and API efficiency enhancement

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **User-Centered Design**: Prioritize usability, accessibility, and security in all interface decisions
2. **Thin Controllers**: Delegate all business logic to application layer, maintain separation of concerns
3. **API Consistency**: Standardize API specifications, error formats, and authentication methods
4. **Security First**: Implement comprehensive input validation and security measures

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Leverage Serena for UI/API pattern discovery and optimization
6. **Context-Rich UX**: Enhance user experience with Context7 latest UX/UI best practices
7. **Data-Driven Design**: Base interface decisions on historical usage patterns and industry standards

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **API Compliance**: All endpoints follow OpenAPI specifications and security standards
- **Input Validation**: Comprehensive validation with proper error handling and sanitization
- **User Experience**: Intuitive interfaces with proper error messages and guidance
- **Security Implementation**: Authentication, authorization, and input sanitization properly implemented

**MCP-Enhanced Standards:**

- **Pattern Discovery Coverage**: 95% of presentation patterns identified and optimized
- **UX Optimization**: 90% of usability issues identified and resolved using historical data
- **Best Practice Integration**: 85% industry standard UX practices integrated from Context7
- **Performance Optimization**: 90% of frontend performance bottlenecks identified and resolved

## 🧠 MCP Enhancement: Serena (UI/API Pattern Mining) + Context7 (UX/UI Best Practices)

### MCP-Enhanced Activities (Additional):

- Analyze presentation layer patterns and performance bottlenecks using Serena MCP
- Extract successful UI/API design techniques from historical projects
- Apply Context7 latest UX/UI design patterns and accessibility best practices
- Create optimized presentation implementations with intelligent user experience enhancement
- Provide intelligent recommendations for usability and performance improvement

### Required Setup

```bash
# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced presentation analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: UI/API pattern analysis and performance optimization"
    echo "  • Context7: Latest UX/UI design patterns and accessibility best practices"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • UI/API pattern discovery and optimization"
    echo "  • UX/UI best practice integration"
    echo "  • Accessibility standards compliance"
    echo "  • Performance optimization for frontend components"
    MCP_AVAILABLE="false"
fi

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /09-implement-presentation-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🎨 Executing enhanced presentation implementation for GitHub Issue #$ISSUE_NUMBER..."

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
    echo "🔍 Analyzing comment timeline for latest presentation requirements..."
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

# Save issue data for presentation implementation process
TEMP_ISSUE_FILE="/tmp/issue-${ISSUE_NUMBER}-data.json"
echo "$ISSUE_DATA" > "$TEMP_ISSUE_FILE"
echo "💾 Issue data saved to: $TEMP_ISSUE_FILE"

# MCP Enhanced: Additional analysis if available
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Mode: Analyzing UI/API patterns against historical data..."
    echo "📊 Enhanced Mode: Cross-referencing with UX/UI best practices..."
fi

# Execute the enhanced Python implementation with issue data
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/09-implement-presentation-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    echo "🔄 Passing issue data and comment history to enhanced Python implementation..."
    
    # Pass both issue number and temp file path to Python script
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER" "$TEMP_ISSUE_FILE"
    EXIT_CODE=$?

    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"

    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced presentation implementation completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Presentation layer was implemented with MCP enhancements:"
            echo "  📊 Serena: UI/API patterns and performance optimization applied"
            echo "  🧠 Context7: UX/UI best practices and accessibility standards integrated"
        else
            echo "🎯 Presentation layer was implemented in standard mode"
        fi
    else
        echo "❌ Enhanced presentation implementation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis with retrieved issue data..."
    echo ""
    echo "🚀 Starting enhanced presentation implementation with comprehensive GitHub issue analysis..."
    echo "📊 Issue Data Available:"
    echo "  - Original Description: ✅"
    echo "  - Comment History: ✅ ($COMMENT_COUNT comments)"
    echo "  - Latest Updates: ✅"
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced presentation implementation..."
    # Cleanup temp file
    rm -f "$TEMP_ISSUE_FILE"
fi
```

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → **UI(09)** → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Enhanced Presentation Implementation - API/UI/CLI Layer (09/16)  
> 🎯 **Phase Purpose**: Implement presentation layer with MCP-enhanced UX optimization and pattern recognition  
> ⬅️ **Previous Stage**: /08-implement-infra-enhanced for infrastructure layer implementation  
> ➡️ **Next Stage**: /10-run-all-tests-enhanced for comprehensive system testing

## 🎯 PHASE PURPOSE: ENHANCED PRESENTATION LAYER WITH MCP INTELLIGENCE

**⚠️ Important Notice:**

- **This step focuses on ENHANCED PRESENTATION IMPLEMENTATION** - Implement API endpoints, CLI commands, and UI components with MCP-enhanced UX optimization and pattern recognition
- **NO BUSINESS LOGIC** - Focus only on user interface concerns, delegate all business logic to application layer
- **PRESENTATION LAYER ONLY** - API endpoints, CLI commands, UI components, input validation, and response formatting
- **MCP ENHANCEMENT** - UX/UI pattern analysis and best practice integration

**What this enhanced step does:**

1. `/08-implement-infra-enhanced` ← Infrastructure with performance optimization
2. `/09-implement-presentation-enhanced` ← **【YOU ARE HERE】MCP-enhanced presentation with UX intelligence**
3. `/10-run-all-tests-enhanced` ← Enhanced comprehensive system testing
4. Then proceed with enhanced refactoring and quality assurance

**IMPLEMENT PRESENTATION LAYER WITH MCP UX INTELLIGENCE. FOCUS ON USER INTERFACE ONLY.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Application services and use cases for API endpoint design reference
if [[ -f "src/application/" ]]; then
    Read src/application/ service interfaces for API mapping
fi

if [[ -f "docs/use_cases/" ]]; then
    Read docs/use_cases/ for user interface requirements
fi

# MCP Enhanced: UI/API patterns and UX data (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Presentation Mode: MCP capabilities enabled"
    echo "  📊 Serena: Analyzing UI/API patterns and performance optimization"
    echo "  🧠 Context7: Integrating latest UX/UI best practices and accessibility standards"
else
    echo "🎨 Standard Mode: Basic presentation implementation without MCP enhancements"
fi
```

### GitHub Issue Integration (Enhanced)

```bash
# Enhanced issue-driven presentation implementation
echo "📥 Loading GitHub issue #$ISSUE_NUMBER for enhanced presentation analysis..."

# Standard issue data extraction
echo "📋 Issue Title: $(echo "$ISSUE_DATA" | jq -r '.title')"
echo "📋 Issue Body Analysis:"
echo "$(echo "$ISSUE_DATA" | jq -r '.body')))" | head -20
echo "📋 Labels: $(echo "$ISSUE_DATA" | jq -r '.labels[].name' | tr '\n' ', ')"

# Enhanced comment timeline analysis
if [[ $COMMENT_COUNT -gt 0 ]]; then
    echo "📊 Processing enhanced presentation comment timeline..."
    echo "$RECENT_COMMENTS" | jq -r '.[] | "[\(.createdAt)] \(.author.login): \(.body[0:100])..."'
    
    # MCP Enhanced: Pattern analysis
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "🔍 Enhanced: Cross-referencing UI/API patterns with historical data..."
        echo "📊 Enhanced: Applying UX/UI best practices and accessibility standards..."
    fi
fi
```

## 🚀 Enhanced Expert Execution Flow

### Phase 1: Enhanced Presentation Requirements Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **Enhanced User Interface Requirements Assessment**

   ```bash
   # Enhanced analysis with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント・プレゼンテーション実装"
       echo "📊 履歴UX/UIパターンと最新デザイン手法を活用して最適化されたインターフェースを作成します"
   fi
   ```

   Enhanced analysis includes:
   - API endpoint requirements with pattern-based optimization (MCP Enhanced)
   - CLI interface needs with usability pattern alignment (MCP Enhanced)
   - UI component specifications with accessibility best practices
   - Security validation requirements with industry standard practices

2. **MCP-Enhanced UX Pattern Discovery**

   - UI/API pattern matching using Serena MCP for user experience optimization
   - Best practice integration using Context7 MCP for accessibility and usability
   - Cross-reference analysis for presentation layer dependency optimization
   - Historical usability issue identification and mitigation strategies

### Phase 2: Enhanced API Endpoint Implementation

**Execute enhanced API design:**

1. **MCP-Enhanced API Endpoint Architecture**

   ```bash
   # Enhanced API implementation with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🔍 Enhanced API Implementation:"
       echo "  • Serena: Mining successful API patterns from historical projects"
       echo "  • Context7: Applying latest API design and security techniques"
       echo "  • Integration: Creating optimized endpoints with performance patterns"
   fi
   ```

2. **Intelligent Security and Validation**

   - Input validation with pattern-based security enhancement (MCP Enhanced)
   - Authentication and authorization with industry standard practices (Context7 Enhanced)
   - Error handling with user-friendly messaging (enhanced with UX patterns)
   - Rate limiting and security headers with optimization patterns

### Phase 3: Enhanced User Interface Component Implementation

**Design enhanced UI component architecture:**

1. **MCP-Enhanced Component Design**

   - CLI command implementation with usability patterns (enhanced with historical analysis)
   - Web UI components with accessibility standards (Context7 Enhanced)
   - Response formatting with user experience optimization (enhanced with UX patterns)
   - Error presentation with intelligent user guidance (MCP Enhanced)

2. **Intelligent User Experience Optimization**

   - User feedback mechanisms with pattern-based improvement
   - Loading states and progress indicators with UX best practices
   - Error recovery workflows with historical success patterns
   - Accessibility compliance with industry standards

### Phase 4: Enhanced Presentation Documentation Generation

**Create enhanced presentation documentation:**

1. **Enhanced API Documentation**

   - OpenAPI specification with security best practices
   - API usage examples with optimization guidelines
   - Error handling documentation with user guidance
   - Performance optimization recommendations with benchmark standards

2. **Enhanced User Interface Documentation**

   - CLI usage documentation with usability guidelines
   - UI component documentation with accessibility standards
   - User experience guidelines with best practice integration
   - Testing documentation with comprehensive validation strategies

## ✅ Enhanced Built-in Quality Assurance

### Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - Enhanced:**

- [ ] All API endpoints implemented with security validation and performance optimization (MCP Enhanced)
- [ ] CLI commands completed with usability patterns and error handling (MCP Enhanced)
- [ ] UI/UX patterns identified and applied for optimal user experience (MCP Enhanced)
- [ ] Accessibility standards integrated from Context7 best practices (MCP Enhanced)
- [ ] Security validation implemented with industry standard practices (MCP Enhanced)

**Recommended Items (SHOULD) - Enhanced:**

- [ ] Historical UI/API patterns applied to implementations (MCP Enhanced)
- [ ] UX/UI best practices integrated from Context7 (MCP Enhanced)
- [ ] Performance optimization based on frontend pattern analysis
- [ ] User feedback mechanisms integrated for continuous improvement
- [ ] Comprehensive testing coverage for all presentation components

### Enhanced Quality Metrics

| Indicator | Target Value | Enhanced Target | Actual Value | Result |
|-----------|-------------|-----------------|--------------|---------| 
| API Implementation Rate | 100% | 100% (Pattern Optimized) | [Completion %] | ✅/❌ |
| UX Optimization Coverage | N/A | 90% (MCP Enhanced) | [Coverage %] | ✅/❌ |
| Accessibility Compliance | N/A | 85% (Context7) | [Compliance %] | ✅/❌ |
| Security Validation Rate | 100% | 95% (Enhanced Standards) | [Validation %] | ✅/❌ |

## 📊 Enhanced Standardized Output Format

### Enhanced 実行サマリー

- ✅ **API実装**: [実装されたエンドポイント数] (MCP拡張: セキュリティ・パフォーマンス最適化統合)
- ✅ **UI/CLI実装**: [実装されたコンポーネント数] (ユーザビリティパターン付き)
- ✅ **UX最適化**: [最適化項目数] (履歴データベース)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### Enhanced 成果物

**作成されたファイル (MCP Enhanced):**

- `src/presentation/api/`: パターン最適化API実装群
- `src/presentation/cli/`: ユーザビリティ強化CLI実装
- `src/presentation/ui/`: アクセシビリティ準拠UI コンポーネント
- `src/presentation/validation/`: セキュリティ強化バリデーション実装
- `docs/api/`: OpenAPI仕様書とセキュリティガイドライン
- `docs/presentation/patterns.md`: SerenaのUI/APIパターン分析レポート (MCP Enhanced)
- `docs/presentation/ux-optimization.md`: Context7のUX/UI最適化ガイダンス (MCP Enhanced)
- `docs/presentation/accessibility.md`: アクセシビリティ準拠ガイドライン

### Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/10-run-all-tests-enhanced <issue-number>` でプレゼンテーション統合テスト実行
   - `/11-refactor-enhanced <issue-number>` でUI/UXリファクタリング実施
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的UX最適化の実施
   - ユーザーフィードバック収集システムの構築検討

### Enhanced メタデータ更新

```json
{
  "command_executed": "09-implement-presentation-enhanced",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "enhanced-presentation-implementation",
  "issue_number": "[issue-number]",
  "mcp_enhancements": {
    "serena_pattern_analysis": true,
    "context7_ux_practices": true,
    "accessibility_optimization": true,
    "performance_optimization": true
  },
  "deliverables": {
    "api_endpoints": "src/presentation/api/",
    "cli_commands": "src/presentation/cli/",
    "ui_components": "src/presentation/ui/",
    "validation": "src/presentation/validation/",
    "api_docs": "docs/api/",
    "pattern_analysis": "docs/presentation/patterns.md",
    "ux_optimization": "docs/presentation/ux-optimization.md",
    "accessibility_guide": "docs/presentation/accessibility.md"
  },
  "metrics": {
    "api_endpoints_implemented": "[number]",
    "ui_components_created": "[number]",
    "cli_commands_implemented": "[number]",
    "ux_patterns_applied": "[number]",
    "accessibility_features": "[number]"
  },
  "next_recommended": ["10-run-all-tests-enhanced", "11-refactor-enhanced"],
  "quality_score": "[score]",
  "ux_optimization_score": "[score]"
}
```

---

🎯 MCP拡張プレゼンテーション実装を開始します。プレゼンテーション・レイヤー・アーキテクチャ専門家として、履歴UX/UIパターン分析と最新デザイン手法を活用した最適化されたユーザーインターフェース実装を実施いたします。

**使用方法**:

```bash
/09-implement-presentation-enhanced <issue-number>

# 例
/09-implement-presentation-enhanced 123
```

**MCP拡張機能** (利用可能時):
- 📊 **Serena**: 履歴UI/APIパターン分析・UX最適化・パフォーマンス向上
- 🧠 **Context7**: 最新UX/UIデザイン手法・アクセシビリティ標準・ユーザビリティベストプラクティス