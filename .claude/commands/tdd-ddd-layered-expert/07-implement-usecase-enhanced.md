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

## 🧠 MCP Enhancement: Serena (Architecture Analysis + Service Mining) + Context7 (Application Patterns + Framework Integration)

### MCP-Enhanced Activities (Additional):

- 既存アプリケーション層実装のSerena MCPによる包括的分析とパターン抽出
- 成功サービス設計パターンの自動発見と推奨
- Context7最新アプリケーションアーキテクチャとフレームワーク統合技術
- クロスリファレンス・サービス設計文書の知的生成
- 履歴成功パターンに基づくアプリケーション層最適化推奨

### Required Setup

```bash
# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced application architecture analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: 既存アプリケーション層パターン分析と最適化"
    echo "  • Context7: 最新アプリケーションアーキテクチャとフレームワーク統合"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • 既存サービス設計パターン発見と適用"
    echo "  • アプリケーションアーキテクチャベストプラクティス統合"
    echo "  • クロスリファレンス分析と最適化"
    echo "  • インテリジェント・サービス設計推奨"
    MCP_AVAILABLE="false"
fi

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /implement-usecase-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Executing enhanced use case implementation for Issue #$ISSUE_NUMBER..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/07-implement-usecase-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced use case implementation completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Use case implementation enhanced with MCP analysis:"
            echo "  📚 Serena: アプリケーション層パターン分析と最適化適用"
            echo "  🧠 Context7: 最新アーキテクチャ技法とフレームワーク統合"
        else
            echo "🎯 Use case implementation completed in standard mode"
        fi
    else
        echo "❌ Enhanced use case implementation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis for use case implementation..."
    echo ""
    echo "🚀 Starting enhanced use case implementation with comprehensive analysis..."
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced application layer implementation..."
fi
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

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Use case specifications for implementation guidance
if [[ -f "docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md" ]]; then
    Read docs/use_cases/sprints/*/issue-${ISSUE_NUMBER}/specification.md
fi

# Domain implementation for orchestration understanding
if [[ -d "src/domain/" ]]; then
    Glob src/domain/**/*.py for domain implementation files
fi

# MCP Enhanced: Existing application implementations (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Implementation Mode: MCP capabilities enabled"
    echo "  📊 Serena: Analyzing existing application layer patterns"
    echo "  🧠 Context7: Integrating latest application architecture techniques"
else
    echo "📋 Standard Mode: Basic application implementation without MCP enhancements"
fi
```

## 🚀 Enhanced Expert Execution Flow

### Phase 1: Enhanced Application Implementation Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **Enhanced Implementation Context Assessment**

   ```bash
   # Enhanced implementation context with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント・アプリケーション層実装"
       echo "📊 既存アーキテクチャパターン分析と最新フレームワーク技法を活用して最適化されたアプリケーション層を実装します"
   fi
   ```

   Enhanced implementation analysis includes:
   - Use case specifications analysis for orchestration design (MCP Enhanced pattern recognition)
   - Domain layer integration planning with dependency analysis (MCP Enhanced validation)
   - Existing application service analysis for consistency and patterns (MCP Enhanced discovery)
   - Framework-specific implementation pattern integration (Context7 Enhanced)

2. **MCP-Enhanced Application Architecture Strategy**

   - Existing service pattern mining using Serena MCP
   - Latest application architecture techniques from Context7 MCP
   - Cross-reference service design analysis for optimization
   - Intelligent orchestration and dependency management recommendations

### Phase 2: Enhanced Use Case Service Implementation

**Execute enhanced application implementation:**

1. **MCP-Enhanced Use Case Service Implementation**

   ```bash
   # Enhanced service implementation with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🔍 Enhanced Service Implementation:"
       echo "  • Serena: Mining successful service orchestration patterns"
       echo "  • Context7: Applying latest service design and architecture techniques"
       echo "  • Integration: Creating optimized service implementations with intelligence"
   fi
   ```

2. **Intelligent DTO and Interface Design**

   - DTO implementation with pattern validation (MCP Enhanced)
   - Interface design with dependency inversion best practices (Context7 Enhanced)
   - Data mapping optimization with historical patterns (Serena Enhanced)
   - Transaction boundary optimization with architectural guidance

### Phase 3: Enhanced Orchestration Implementation

**Design enhanced orchestration structure:**

1. **Enhanced Use Case Orchestration**

   - Business scenario orchestration with pattern recognition
   - Domain service coordination with architectural best practices
   - Transaction management with industry standard practices
   - Error handling optimization with resilience patterns

2. **Enhanced Dependency Management and Integration**

   - Repository interface design with abstraction optimization
   - External service integration with pattern-based recommendations
   - Cross-cutting concern integration with best practices
   - Performance optimization with architectural benchmarks

### Phase 4: Enhanced Implementation Documentation Generation

**Create enhanced implementation documentation:**

1. **Enhanced Application Architecture Document**

   - Service architecture with MCP analysis results
   - Orchestration pattern explanations and rationale
   - Dependency mapping with traceability analysis
   - Performance and scalability considerations

2. **Enhanced Integration and Testing Guide**

   - Service integration testing strategy with intelligent recommendations
   - Mock and stub configuration with pattern guidance
   - Performance testing with benchmark integration
   - Deployment readiness with operational excellence

## ✅ Enhanced Built-in Quality Assurance

### Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - Enhanced:**

- [ ] All Given-When-Then scenarios implemented in use case services with pattern validation
- [ ] Domain orchestration properly implemented with clean architecture compliance (MCP Enhanced)
- [ ] Repository interfaces defined with dependency inversion principles (MCP Enhanced validation)
- [ ] DTO classes created with proper data mapping and validation (MCP Enhanced analysis)
- [ ] Service patterns aligned with historical success data (MCP Enhanced)

**Recommended Items (SHOULD) - Enhanced:**

- [ ] Existing application service patterns identified and applied (MCP Enhanced)
- [ ] Latest application architecture techniques integrated (Context7 Enhanced)
- [ ] Cross-cutting concerns properly implemented with industry standards
- [ ] Performance implications analyzed and documented
- [ ] Integration testing strategy developed and documented

### Enhanced Quality Metrics

| Indicator | Target Value | Enhanced Target | Actual Value | Result |
|-----------|--------------|-----------------|--------------|--------|
| Use Case Coverage | 100% | 100% (Pattern Validated) | [Coverage %] | ✅/❌ |
| Clean Architecture Compliance | 95% | 98% (MCP Verified) | [Compliance %] | ✅/❌ |
| Service Design Quality | 85% | 92% (Architecture Optimized) | [Quality %] | ✅/❌ |
| Pattern Implementation Coverage | N/A | 90% (MCP Enhanced) | [Coverage %] | ✅/❌ |

## 📊 Enhanced Standardized Output Format

### Enhanced 実行サマリー

- ✅ **ユースケース実装**: [実装されたサービス・DTO数] (MCP拡張: パターン分析統合)
- ✅ **オーケストレーション実装**: [実装されたオーケストレーション数] (履歴検証付き)
- ✅ **インターフェース定義**: [定義されたリポジトリ・サービスインターフェース数] (品質検証済み)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### Enhanced 成果物

**作成されたファイル (MCP Enhanced):**

- `src/application/use_cases/`: パターン分析統合ユースケースサービス実装
- `src/application/dtos/`: 最適化データ転送オブジェクト実装
- `src/application/interfaces/`: インテリジェント・インターフェース設計
- `src/application/services/`: ベストプラクティス統合アプリケーションサービス
- `docs/application/issue-<number>/architecture_guide.md`: アーキテクチャガイド (MCP Enhanced)
- `docs/application/issue-<number>/service_analysis.md`: Serenaサービス分析レポート (MCP Enhanced)
- `docs/application/issue-<number>/integration_guide.md`: Context7統合ガイド (MCP Enhanced)

### Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/implement-infra-enhanced <issue-number>` でパターン分析統合インフラストラクチャ層実装
   - `/run-all-tests-enhanced` でインテリジェント統合テスト実行
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的アプリケーション層最適化の実施
   - 履歴パターン学習システムの構築検討

### Enhanced メタデータ更新

```json
{
  "command_executed": "implement-usecase-enhanced",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "enhanced-application-implementation",
  "issue_number": "[issue-number]",
  "mcp_enhancements": {
    "serena_service_analysis": true,
    "context7_architecture_practices": true,
    "service_pattern_mining": true,
    "cross_reference_analysis": true
  },
  "deliverables": {
    "use_case_services": "src/application/use_cases/",
    "dtos": "src/application/dtos/",
    "interfaces": "src/application/interfaces/",
    "application_services": "src/application/services/",
    "architecture_guide": "docs/application/issue-<number>/architecture_guide.md",
    "service_analysis": "docs/application/issue-<number>/service_analysis.md",
    "integration_guide": "docs/application/issue-<number>/integration_guide.md"
  },
  "metrics": {
    "use_cases_implemented": "[number]",
    "dtos_implemented": "[number]",
    "interfaces_defined": "[number]",
    "services_implemented": "[number]",
    "pattern_coverage_score": "[percentage]",
    "architecture_quality_score": "[score]"
  },
  "next_recommended": ["implement-infra-enhanced", "run-all-tests-enhanced"],
  "quality_score": "[score]",
  "mcp_analysis_quality": "[score]"
}
```

---

🎯 MCP拡張アプリケーション層実装を開始します。アプリケーション層アーキテクトとして、履歴サービスパターン分析と最新アーキテクチャ技法を活用した包括的なアプリケーション層実装を実施いたします。

**使用方法**:

```bash
/implement-usecase-enhanced <issue-number>

# 例
/implement-usecase-enhanced 123
```

**MCP拡張機能** (利用可能時):
- 📚 **Serena**: 既存アプリケーション層パターン分析・サービス設計最適化・アーキテクチャ改善推奨
- 🧠 **Context7**: 最新アプリケーションアーキテクチャ・フレームワーク統合・パフォーマンス最適化