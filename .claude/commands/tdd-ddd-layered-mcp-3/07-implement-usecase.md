# 07-implement-usecase-enhanced (MCP-Enhanced Use Case Implementation)

## 🎯 Expert Profile Declaration

During command execution, you act as an **Application Layer Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Application Layer Expertise:**

- **Clean Architecture Application Layer**: ユースケース・オーケストレーション、DTO設計、トランザクション管理
- **Use Case Implementation**: Given-When-Thenシナリオの正確なアプリケーションロジック実装
- **Dependency Inversion**: インフラストラクチャ依存性の抽象化とインジェクション設計
- **Cross-Cutting Concerns**: セキュリティ、ロギング、バリデーションの横断的関心事実装

**MCP-Enhanced Capabilities:**

- **Intelligent Architecture Analysis**: 既存アプリケーション層パターンの自動分析（Serena MCP）
- **Pattern Reference Integration**: Context7による最新アーキテクチャパターンとフレームワーク統合
- **Cross-Reference Implementation**: 完全なアプリケーション依存関係分析と最適化
- **Automated Service Design**: 既存サービスパターンからの知的設計推奨

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Use Case Orchestration**: ドメインロジック・オーケストレーションによるビジネス価値実現
2. **Clean Boundaries**: アプリケーション層とドメイン層の明確な分離維持
3. **Dependency Inversion**: 抽象化によるインフラストラクチャ依存性管理
4. **Transaction Management**: 適切なトランザクション境界とデータ整合性確保

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Serenaによる既存実装パターン発見と活用
6. **Context-Rich Architecture**: Context7アーキテクチャ知識による設計品質向上
7. **Data-Driven Service Design**: 履歴データに基づくサービス設計最適化

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Use Case Coverage**: 100%のGiven-When-Thenシナリオ実装
- **Clean Architecture Compliance**: 依存性ルールと境界の遵守
- **Transaction Integrity**: 適切なACID特性とデータ整合性
- **Error Handling**: 包括的なエラー処理と復旧メカニズム

**MCP-Enhanced Standards:**

- **Pattern Implementation Coverage**: 95%の実証済みアーキテクチャパターン適用
- **Service Design Optimization**: 100%のサービス設計最適化機会特定
- **Cross-Reference Accuracy**: 100%アプリケーション依存関係正確性
- **Framework Integration Quality**: 90%最新フレームワーク統合ベストプラクティス

## 🧠 MCP-3 Integration: Intelligent Application Implementation

### Context-Driven MCP Integration

このコマンドは**Application Layer Implementation**に特化しており、複雑性レベルに応じて適切なMCPツールを選択します：

- **基本実装**: Serena + Context7による効率的な実装
- **複雑な統合**: Sequential MCPによる体系的分析が必要な場合（3+ interconnected components）

### Intelligent MCP Setup

```bash
echo "🚀 Application Use Case Implementation with Intelligent MCP Integration..."

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /implement-usecase-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "📊 Analyzing implementation complexity for Issue #$ISSUE_NUMBER..."

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
echo "📋 Evaluating application layer complexity..."

# Application implementation is typically standard execution
# unless it involves complex multi-layer integration issues
echo "⚡ Standard application implementation - Using Serena + Context7 integration"

if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without code analysis - manual analysis required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest patterns - using standard approaches"
fi

echo "🏗️ Starting Application Layer Implementation..."

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

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: TDD Implementation Phase - Enhanced Application Implementation (07/16)  
> 🎯 **Phase Purpose**: Implement application layer use cases and orchestration with MCP intelligence  
> ⬅️ **Previous Stage**: 06-implement-domain-enhanced (Domain Implementation)  
> ➡️ **Next Stage**: 08-implement-infra-enhanced (Infrastructure Implementation)

## 🎯 PHASE PURPOSE: ENHANCED APPLICATION LAYER IMPLEMENTATION

**⚠️ Important Notice:**

- **This step focuses on APPLICATION LAYER CODE IMPLEMENTATION** - Create use case classes, DTOs, and orchestration logic
- **DOMAIN ORCHESTRATION** - Coordinate domain objects to fulfill business scenarios
- **DEPENDENCY INVERSION** - Define interfaces for infrastructure dependencies
- **MCP ENHANCEMENT** - Leverage intelligent architecture analysis and optimization

**What this enhanced step does:**

1. `/implement-domain-enhanced` ← Previous: Domain entities and business logic
2. `/implement-usecase-enhanced <issue-number>` ← **【YOU ARE HERE】Application layer implementation with MCP**
3. `/implement-infra-enhanced` ← Next: Infrastructure layer implementation
4. Continue Clean Architecture implementation cycle

**IMPLEMENT APPLICATION LAYER CODE WITH MCP INTELLIGENCE.**

## 📋 Context-Driven Analysis

### Intelligent Context Reading

```bash
# Standard project state assessment
echo "📋 Reading project context..."

# Essential project state
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Use case specifications for implementation guidance
echo "📋 Loading use case specifications..."
if [[ -f "docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md" ]]; then
    Read docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md
fi

# Domain layer understanding for orchestration
echo "📋 Analyzing domain layer for orchestration..."
if [[ -d "src/domain/" ]]; then
    Glob src/domain/**/*.py to understand domain structure
fi

# MCP-Enhanced context analysis (when available)
if [[ "$MCP_SERENA" == "available" ]]; then
    echo "🧠 Serena MCP: Analyzing existing application patterns..."
    Use mcp__serena__get_symbols_overview to analyze application layer structure
    Use mcp__serena__search_for_pattern "use_case|service|dto" to find existing patterns
fi

if [[ "$MCP_CONTEXT7" == "available" ]]; then
    echo "📚 Context7 MCP: Loading latest application architecture practices..."
    Use mcp__context7__resolve-library-id for framework-specific patterns
fi
```

## 🚀 Intelligent Expert Execution Flow

### Phase 1: Context-Driven Implementation Analysis

**Analyze implementation requirements (user interactions in Japanese):**

1. **Smart Implementation Context Assessment**

   ```bash
   echo "🎯 Starting application layer implementation analysis..."
   
   # Use case orchestration complexity evaluation  
   echo "📋 Evaluating use case orchestration requirements..."
   
   # Standard implementation approach for application layer
   echo "⚡ Application layer implementation - Standard execution with MCP support"
   ```

   Implementation analysis includes:
   - Use case specifications analysis for orchestration design
   - Domain layer integration planning with clean architecture compliance
   - Repository interface requirements analysis
   - DTO and service boundary definition

2. **MCP-Supported Architecture Strategy**

   - Pattern recognition using Serena MCP (when available)
   - Best practice integration using Context7 MCP (when available)
   - Service design optimization based on existing patterns
   - Clean architecture compliance validation

### Phase 2: Implementation Execution

**Execute application implementation:**

1. **Use Case Service Implementation**

   ```bash
   echo "🏗️ Implementing use case services..."
   
   if [[ "$MCP_SERENA" == "available" ]]; then
       echo "🧠 Using Serena MCP for pattern analysis and optimization"
       Use mcp__serena__find_symbol to locate existing service patterns
       Use mcp__serena__write_memory to record implementation patterns
   fi
   
   if [[ "$MCP_CONTEXT7" == "available" ]]; then
       echo "📚 Using Context7 MCP for architecture best practices"
       Use mcp__context7__get-library-docs for framework-specific implementation
   fi
   ```

2. **DTO and Interface Design**

   - DTO implementation following clean architecture principles
   - Repository interface definition with dependency inversion
   - Service interface design for testability
   - Data mapping and validation implementation

### Phase 3: Orchestration and Integration

**Design orchestration structure:**

1. **Use Case Orchestration**

   - Business scenario implementation following Given-When-Then
   - Domain service coordination with proper boundaries
   - Transaction management with appropriate scope
   - Error handling with proper exception propagation

2. **Dependency Management**

   - Repository interface design with clean abstractions
   - External service integration planning
   - Cross-cutting concern integration points
   - Performance considerations documentation

### Phase 4: Quality Assurance and Documentation

**Generate implementation artifacts:**

1. **Application Architecture Documentation**

   ```bash
   echo "📚 Generating application architecture documentation..."
   
   if [[ "$MCP_SERENA" == "available" ]]; then
       Use mcp__serena__think_about_collected_information
   fi
   ```

2. **Integration and Testing Preparation**

   - Service integration testing strategy
   - Mock and stub configuration guidance  
   - Performance testing considerations
   - Deployment readiness checklist

## ✅ Quality Assurance with MCP Support

### Smart Self-Diagnostic Checklist

**Mandatory Items (MUST):**

- [ ] All Given-When-Then scenarios implemented in use case services
- [ ] Domain orchestration properly implemented with clean architecture compliance
- [ ] Repository interfaces defined with dependency inversion principles
- [ ] DTO classes created with proper data mapping and validation
- [ ] Service boundaries clearly defined and maintainable

**MCP-Enhanced Items (SHOULD - when available):**

- [ ] Existing application service patterns analyzed and applied (Serena MCP)
- [ ] Latest application architecture techniques integrated (Context7 MCP)
- [ ] Cross-cutting concerns properly implemented with industry standards
- [ ] Performance implications analyzed and documented
- [ ] Integration testing strategy developed and documented

### Quality Metrics

| Indicator | Target Value | MCP-Enhanced Target | Actual Value | Result |
|-----------|--------------|---------------------|--------------|--------|
| Use Case Coverage | 100% | 100% (Pattern Validated) | [Coverage %] | ✅/❌ |
| Clean Architecture Compliance | 95% | 98% (MCP Verified) | [Compliance %] | ✅/❌ |
| Service Design Quality | 85% | 92% (Optimized) | [Quality %] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー

- ✅ **ユースケース実装**: [実装されたサービス・DTO数]
- ✅ **オーケストレーション実装**: [実装されたオーケストレーション数]  
- ✅ **インターフェース定義**: [定義されたリポジトリ・サービスインターフェース数]
- ✅ **MCP支援**: [利用されたMCPツール数]

### 成果物

**作成されたファイル:**

- `src/application/use_cases/`: ユースケースサービス実装
- `src/application/dtos/`: データ転送オブジェクト実装
- `src/application/interfaces/`: インターフェース設計
- `src/application/services/`: アプリケーションサービス
- `docs/application/issue-<number>/architecture_guide.md`: アーキテクチャガイド
- `docs/application/issue-<number>/implementation_notes.md`: 実装ノート (MCP利用時)

### 次のステップ

1. **即座に実行可能**: 
   - `/implement-infra-enhanced <issue-number>` でインフラストラクチャ層実装
   - `/run-all-tests-enhanced` で統合テスト実行
2. **戦略的推奨**: 
   - アプリケーション層の継続的品質向上
   - インテグレーションテストの拡充検討

### メタデータ更新

```bash
# Record implementation completion and learning insights
if [[ "$MCP_SERENA" == "available" ]]; then
    Use mcp__serena__write_memory "application-implementation-$(date +%Y%m%d)" "{
      \"command\": \"implement-usecase-enhanced\",
      \"timestamp\": \"$(date -Iseconds)\",
      \"status\": \"[SUCCESS|PARTIAL|FAILED]\",
      \"phase\": \"application-implementation\", 
      \"issue_number\": \"${ISSUE_NUMBER}\",
      \"mcp_tools_used\": [\"serena\", \"context7\"],
      \"implementation_patterns\": [\"discovered_patterns\"],
      \"quality_metrics\": {
        \"use_cases_implemented\": \"[number]\",
        \"dtos_implemented\": \"[number]\", 
        \"interfaces_defined\": \"[number]\",
        \"services_implemented\": \"[number]\"
      },
      \"next_recommended\": [\"implement-infra-enhanced\", \"run-all-tests-enhanced\"]
    }"
fi

# Update project state
echo "💾 Recording implementation completion..."
```

---

🎯 インテリジェントなアプリケーション層実装を開始します。アプリケーション層アーキテクトとして、MCPツールを活用した効率的で品質の高いアプリケーション層実装を実施いたします。

**使用方法**:

```bash
/implement-usecase-enhanced <issue-number>

# 例
/implement-usecase-enhanced 123
```

**MCP統合機能** (利用可能時):
- 📚 **Serena**: 既存アプリケーション層パターン分析・コード品質向上
- 🧠 **Context7**: 最新アプリケーションアーキテクチャ・フレームワーク統合
- 🤔 **Sequential**: 複雑な統合問題での体系的分析 (必要時)