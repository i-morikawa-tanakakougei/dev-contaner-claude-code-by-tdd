# 08-implement-infra-enhanced (MCP-Enhanced Infrastructure Implementation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Infrastructure Architecture & Integration Specialist** with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Infrastructure Expertise:**

- **Repository Implementation**: Concrete implementation of domain repository interfaces with performance optimization
- **Data Persistence**: Advanced database connections, transaction management, and data mapping strategies
- **External Service Integration**: API integration, file systems, message queues, and third-party service orchestration
- **Infrastructure Configuration**: Connection pools, environment variables, performance tuning, and scalability optimization

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: Automated infrastructure pattern discovery using Serena MCP
- **Best Practice Integration**: Context7-based latest infrastructure patterns and performance optimizations
- **Cross-Reference Architecture**: Complete infrastructure dependency analysis and optimization
- **Performance Pattern Mining**: Infrastructure bottleneck identification and optimization recommendations

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Technical Implementation Focus**: Pure technical implementation without business logic contamination
2. **Dependency Inversion**: Depend on domain interfaces and provide robust concrete implementations
3. **External System Isolation**: Complete abstraction of database and API details from domain layer
4. **Quality Assurance**: Proper connection pools, transactions, error handling, and performance optimization

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Leverage Serena for infrastructure pattern discovery and optimization
6. **Context-Rich Architecture**: Enhance infrastructure with Context7 best practice patterns
7. **Data-Driven Optimization**: Base infrastructure decisions on historical performance data and industry standards

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Repository Interface Compliance**: All domain repository interfaces fully implemented
- **Transaction Management**: Proper ACID compliance and transaction boundary management
- **Performance Standards**: Connection pooling, caching, and query optimization implemented
- **Error Handling**: Comprehensive error handling with proper exception translation

**MCP-Enhanced Standards:**

- **Pattern Discovery Coverage**: 95% of infrastructure patterns identified and optimized
- **Performance Optimization**: 90% of historical bottlenecks identified and resolved
- **Best Practice Integration**: 85% industry standard practices integrated from Context7
- **Cross-Reference Accuracy**: 100% infrastructure dependency mapping with optimization

## 🧠 MCP-3 Integration: Intelligent Infrastructure Implementation

### Context-Driven MCP Integration

このコマンドは**Infrastructure Layer Implementation**に特化しており、複雑性レベルに応じて適切なMCPツールを選択します：

- **基本実装**: Serena + Context7による効率的なリポジトリ実装
- **複雑な統合**: Sequential MCPによる体系的分析が必要な場合（3+ interconnected components）

### Intelligent MCP Setup

```bash
echo "🚀 Infrastructure Implementation with Intelligent MCP Integration..."

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /implement-infra-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "📊 Analyzing infrastructure implementation complexity for Issue #$ISSUE_NUMBER..."

# MCP availability check
echo "🔧 Checking MCP availability..."

if command -v mcp__serena__get_symbols_overview &> /dev/null; then
    echo "✅ Serena MCP available"
    MCP_SERENA="available"
else
    echo "ℹ️ Serena MCP not found - standard mode"
    MCP_SERENA="unavailable" 
fi

if command -v mcp__context7__resolve-library-id &> /dev/null; then
    echo "✅ Context7 MCP available"  
    MCP_CONTEXT7="available"
else
    echo "ℹ️ Context7 MCP not found - standard mode"
    MCP_CONTEXT7="unavailable"
fi

if command -v mcp__sequential-thinking__sequentialthinking &> /dev/null; then
    echo "✅ Sequential MCP available"
    MCP_SEQUENTIAL="available"
else  
    echo "ℹ️ Sequential MCP not found - standard logic mode"
    MCP_SEQUENTIAL="unavailable"
fi

# Context-driven complexity assessment
echo "📋 Evaluating infrastructure layer complexity..."

# Infrastructure implementation is typically standard execution
# unless it involves complex multi-system integration issues
echo "⚡ Standard infrastructure implementation - Using Serena + Context7 integration"

if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual pattern analysis required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard approaches"
fi

echo "🏗️ Starting Infrastructure Layer Implementation..."

# GitHub Issue Requirements Loading (Simple & Comment-Focused)
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

echo "🎯 Proceeding with implementation based on latest requirements..."
```

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → **Infra(08)** → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Enhanced Infrastructure Implementation - Repository & External Integration (08/16)  
> 🎯 **Phase Purpose**: Implement infrastructure layer with MCP-enhanced performance optimization and pattern recognition  
> ⬅️ **Previous Stage**: /07-implement-usecase-enhanced for application layer implementation  
> ➡️ **Next Stage**: /09-implement-presentation-enhanced for UI/API layer implementation

## 🎯 PHASE PURPOSE: ENHANCED INFRASTRUCTURE LAYER WITH MCP INTELLIGENCE

**⚠️ Important Notice:**

- **This step focuses on ENHANCED INFRASTRUCTURE IMPLEMENTATION** - Implement repositories and external integrations with MCP-enhanced performance patterns and optimization
- **NO BUSINESS LOGIC** - Focus only on technical implementation without domain concerns
- **INFRASTRUCTURE LAYER ONLY** - Repository implementations, database access, external service integrations
- **MCP ENHANCEMENT** - Performance pattern analysis and best practice integration

**What this enhanced step does:**

1. `/07-implement-usecase-enhanced` ← Application layer with intelligent orchestration
2. `/08-implement-infra-enhanced` ← **【YOU ARE HERE】MCP-enhanced infrastructure with performance optimization**
3. `/09-implement-presentation-enhanced` ← Enhanced UI/API layer implementation
4. Then proceed with enhanced testing and quality assurance

**IMPLEMENT INFRASTRUCTURE LAYER WITH MCP PERFORMANCE INTELLIGENCE. FOCUS ON TECHNICAL IMPLEMENTATION ONLY.**

## 📋 Context-Driven Analysis

### Intelligent Context Reading

```bash
# Standard project state assessment
echo "📋 Reading project context for infrastructure implementation..."

# Essential project state
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Issue specifications for implementation guidance
echo "📋 Loading issue specifications..."
if [[ -f "docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md" ]]; then
    Read docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md
fi

# Domain interfaces for repository implementation
echo "📋 Analyzing domain interfaces..."
if [[ -d "src/domain/" ]]; then
    Glob src/domain/**/*.py to understand repository interfaces
fi

# Application services for integration understanding
echo "📋 Analyzing application services..."
if [[ -d "src/application/" ]]; then
    Glob src/application/**/*.py to understand service interfaces
fi

# MCP-Enhanced context analysis (when available)
if [[ "$MCP_SERENA" == "available" ]]; then
    echo "🧠 Serena MCP: Analyzing existing infrastructure patterns..."
    Use mcp__serena__get_symbols_overview to analyze infrastructure structure
    Use mcp__serena__search_for_pattern "repository|database|external" to find existing patterns
fi

if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "📚 Context7 MCP: Loading latest infrastructure best practices..."
    Use mcp__context7__resolve-library-id for framework-specific infrastructure patterns
fi
```

## 🚀 Intelligent Expert Execution Flow

### Phase 1: Context-Driven Infrastructure Analysis

**Analyze infrastructure requirements (user interactions in Japanese):**

1. **Smart Infrastructure Context Assessment**

   ```bash
   echo "🎯 Starting infrastructure layer implementation analysis..."
   
   # Repository interface complexity evaluation  
   echo "📋 Evaluating repository implementation requirements..."
   
   # Standard implementation approach for infrastructure layer
   echo "⚡ Infrastructure layer implementation - Standard execution with MCP support"
   ```

   Implementation analysis includes:
   - Repository interface requirements analysis
   - External service integration needs assessment
   - Data persistence strategy planning
   - Performance and scalability considerations

2. **MCP-Supported Infrastructure Strategy**

   - Pattern recognition using Serena MCP (when available)
   - Best practice integration using Context7 MCP (when available)
   - Infrastructure design optimization based on existing patterns
   - Performance optimization with industry standards

### Phase 2: Implementation Execution

**Execute infrastructure implementation:**

1. **Repository Implementation**

   ```bash
   echo "🏗️ Implementing repositories..."
   
   if [[ "$MCP_SERENA" == "available" ]]; then
       echo "🧠 Using Serena MCP for infrastructure pattern analysis"
       Use mcp__serena__find_symbol to locate existing repository patterns
       Use mcp__serena__write_memory to record infrastructure patterns
   fi
   
   if [[ "$MCP_CONTEXT7" == "available" ]]; then
       echo "📚 Using Context7 MCP for infrastructure best practices"
       Use mcp__context7__get-library-docs for framework-specific implementation
   fi
   ```

2. **Data Access and External Service Integration**

   - Repository interface implementation with clean architecture principles
   - Database connection and transaction management
   - External API integration with resilience patterns
   - Caching and performance optimization

### Phase 3: Performance and Integration

**Design performance and integration structure:**

1. **Performance Optimization**

   - Connection pooling and resource management
   - Query optimization and caching strategies
   - Performance monitoring implementation
   - Scalability considerations

2. **External Service Integration**

   - API client implementation with error handling
   - Message queue integration (if needed)
   - File system operations optimization
   - Third-party service integration patterns

### Phase 4: Quality Assurance and Documentation

**Generate infrastructure artifacts:**

1. **Infrastructure Documentation**

   ```bash
   echo "📚 Generating infrastructure documentation..."
   
   if [[ "$MCP_SERENA" == "available" ]]; then
       Use mcp__serena__think_about_collected_information
   fi
   ```

2. **Deployment and Configuration**

   - Environment configuration management
   - Connection string and secrets handling
   - Performance monitoring setup
   - Deployment readiness checklist

## ✅ Quality Assurance with MCP Support

### Smart Self-Diagnostic Checklist

**Mandatory Items (MUST):**

- [ ] All domain repository interfaces fully implemented
- [ ] External service integrations completed with proper error handling
- [ ] Database connections and transaction management implemented
- [ ] Performance considerations documented and implemented
- [ ] Infrastructure patterns follow clean architecture principles

**MCP-Enhanced Items (SHOULD - when available):**

- [ ] Existing infrastructure patterns analyzed and applied (Serena MCP)
- [ ] Latest infrastructure best practices integrated (Context7 MCP)
- [ ] Caching strategies optimized based on performance patterns
- [ ] Connection pooling configured for scalability
- [ ] Monitoring and metrics integrated for operational excellence

### Quality Metrics

| Indicator | Target Value | MCP-Enhanced Target | Actual Value | Result |
|-----------|--------------|---------------------|--------------|--------|
| Repository Implementation Rate | 100% | 100% (Pattern Optimized) | [Completion %] | ✅/❌ |
| Performance Optimization | 80% | 90% (MCP Enhanced) | [Coverage %] | ✅/❌ |
| Best Practice Integration | 75% | 85% (Context7) | [Integration %] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー

- ✅ **Repository実装**: [実装されたRepository数]
- ✅ **外部サービス統合**: [統合されたサービス数]  
- ✅ **パフォーマンス最適化**: [最適化項目数]
- ✅ **MCP支援**: [利用されたMCPツール数]

### 成果物

**作成されたファイル:**

- `src/infrastructure/repositories/`: Repository実装群
- `src/infrastructure/services/`: 外部サービス統合
- `src/infrastructure/config/`: 設定管理
- `src/infrastructure/database/`: データベース管理実装
- `docs/infrastructure/issue-<number>/implementation_guide.md`: 実装ガイド
- `docs/infrastructure/issue-<number>/performance_notes.md`: パフォーマンス・ノート (MCP利用時)

### 次のステップ

1. **即座に実行可能**: 
   - `/implement-presentation-enhanced <issue-number>` でUI/API層実装
   - `/run-all-tests-enhanced` で統合テスト実行
2. **戦略的推奨**: 
   - インフラストラクチャ層の継続的品質向上
   - パフォーマンス監視システムの構築検討

### メタデータ更新

```bash
# Record implementation completion and learning insights
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__write_memory "infrastructure-implementation-$(date +%Y%m%d)" "{
      \"command\": \"implement-infra-enhanced\",
      \"timestamp\": \"$(date -Iseconds)\",
      \"status\": \"[SUCCESS|PARTIAL|FAILED]\",
      \"phase\": \"infrastructure-implementation\", 
      \"issue_number\": \"${ISSUE_NUMBER}\",
      \"mcp_tools_used\": [\"serena\", \"context7\"],
      \"infrastructure_patterns\": [\"discovered_patterns\"],
      \"quality_metrics\": {
        \"repositories_implemented\": \"[number]\",
        \"external_services_integrated\": \"[number]\", 
        \"performance_optimizations\": \"[number]\",
        \"patterns_applied\": \"[number]\"
      },
      \"next_recommended\": [\"implement-presentation-enhanced\", \"run-all-tests-enhanced\"]
    }"
fi

# Update project state
echo "💾 Recording infrastructure implementation completion..."
```

---

🎯 インテリジェントなインフラストラクチャ層実装を開始します。インフラストラクチャ・アーキテクチャ専門家として、MCPツールを活用した効率的で品質の高いインフラ実装を実施いたします。

**使用方法**:

```bash
/implement-infra-enhanced <issue-number>

# 例
/implement-infra-enhanced 123
```

**MCP統合機能** (利用可能時):
- 📚 **Serena**: 既存インフラパターン分析・パフォーマンス最適化
- 🧠 **Context7**: 最新インフラ手法・スケーラビリティパターン・運用ベストプラクティス
- 🤔 **Sequential**: 複雑なマルチシステム統合問題での体系的分析 (必要時)