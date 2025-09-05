# 06-implement-domain-enhanced (MCP-Enhanced Domain Implementation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Domain Implementation Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Domain Implementation Expertise:**

- **DDD Implementation**: Entity, Value Object, Aggregate実装とビジネスルール実装
- **Clean Architecture**: ドメイン層純粋性の維持とアーキテクチャ境界遵守
- **Test-Driven Development**: ドメインロジックのTDD実装とリファクタリング
- **Business Logic Formalization**: 複雑ビジネスルールの正確なコード化

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: 既存ドメイン実装パターンの自動発見（Serena MCP）
- **Pattern Reference Integration**: Context7による最新DDD実装パターンと技術的ベストプラクティス
- **Cross-Reference Implementation**: 完全なドメイン依存関係分析と実装最適化
- **Automated Refactoring**: 既存ドメインコードの知的改善提案

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Domain Purity**: ドメイン層をインフラストラクチャ関心事から完全に分離
2. **Business Rule Implementation**: すべてのGiven-When-Thenルールをドメインコードで実装
3. **Test-First Approach**: テスト駆動開発でドメインロジックを確実に実装
4. **Aggregate Integrity**: アグリゲート整合性とトランザクション境界を維持

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Serenaによる既存実装パターン発見と活用
6. **Context-Rich Implementation**: Context7技術知識による実装品質向上
7. **Data-Driven Refactoring**: 履歴データに基づく実装最適化決定

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Business Rule Coverage**: 100%のGiven-When-Thenルール実装
- **Domain Purity**: インフラストラクチャ依存なしドメイン層
- **Test Coverage**: ドメインロジック100%テストカバレッジ
- **Aggregate Consistency**: 適切な整合性境界とビジネス不変条件

**MCP-Enhanced Standards:**

- **Pattern Implementation Coverage**: 95%の実証済みパターン適用
- **Automated Refactoring Integration**: 100%の改善機会特定と適用
- **Cross-Reference Accuracy**: 100%ドメイン依存関係正確性
- **Technical Best Practice Integration**: 90%最新実装技法統合

## 🧠 MCP Enhancement: Serena (Code Analysis + Implementation Mining) + Context7 (DDD Implementation + Technical Patterns)

### MCP-Enhanced Activities (Additional):

- 既存ドメイン実装のSerena MCPによる包括的分析とパターン抽出
- 成功実装パターンの自動発見と推奨
- Context7最新DDD実装技法とフレームワーク固有パターン統合
- クロスリファレンス実装文書の知的生成
- 履歴成功パターンに基づく実装最適化推奨

### Required Setup

```bash
# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced implementation analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: 既存ドメイン実装パターン分析と最適化"
    echo "  • Context7: 最新DDD実装技法とテクニカルベストプラクティス"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • 既存実装パターン発見と適用"
    echo "  • DDD実装ベストプラクティス統合"
    echo "  • クロスリファレンス分析と最適化"
    echo "  • インテリジェント・リファクタリング推奨"
    MCP_AVAILABLE="false"
fi

# Validate issue number parameter
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /implement-domain-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🚀 Executing enhanced domain implementation for Issue #$ISSUE_NUMBER..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/06-implement-domain-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced domain implementation completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Domain implementation enhanced with MCP analysis:"
            echo "  📚 Serena: 実装パターン分析と最適化適用"
            echo "  🧠 Context7: 最新DDD技法とベストプラクティス統合"
        else
            echo "🎯 Domain implementation completed in standard mode"
        fi
    else
        echo "❌ Enhanced domain implementation failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis for domain implementation..."
    echo ""
    echo "🚀 Starting enhanced domain implementation with comprehensive analysis..."
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced domain layer implementation..."
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
> 🗺️ **Current Position**: TDD Implementation Phase - Enhanced Domain Implementation (06/16)  
> 🎯 **Phase Purpose**: Implement domain entities and business logic with MCP intelligence  
> ⬅️ **Previous Stage**: 05-create-tests-enhanced (Test Creation)  
> ➡️ **Next Stage**: 07-implement-usecase-enhanced (Application Layer Implementation)

## 🎯 PHASE PURPOSE: ENHANCED DOMAIN LAYER IMPLEMENTATION

**⚠️ Important Notice:**

- **This step focuses on DOMAIN LAYER CODE IMPLEMENTATION** - Create actual domain entities, value objects, and business logic
- **TDD APPROACH** - Implement to pass existing tests (GREEN phase)
- **BUSINESS LOGIC FOCUS** - Implement all Given-When-Then business rules
- **MCP ENHANCEMENT** - Leverage intelligent implementation analysis and optimization

**What this enhanced step does:**

1. `/create-tests-enhanced` ← Previous: Test cases created
2. `/implement-domain-enhanced <issue-number>` ← **【YOU ARE HERE】Domain layer implementation with MCP**
3. `/implement-usecase-enhanced` ← Next: Application layer implementation
4. Continue TDD implementation cycle

**IMPLEMENT DOMAIN LAYER CODE WITH MCP INTELLIGENCE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Domain model specifications for implementation guidance
if [[ -f "docs/domain/issue-${ISSUE_NUMBER}-domain-model.md" ]]; then
    Read docs/domain/issue-${ISSUE_NUMBER}-domain-model.md
fi

# Test specifications for TDD implementation
if [[ -d "tests/" ]]; then
    Glob tests/**/*${ISSUE_NUMBER}* for test files
fi

# MCP Enhanced: Existing domain implementations (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Implementation Mode: MCP capabilities enabled"
    echo "  📊 Serena: Analyzing existing domain implementation patterns"
    echo "  🧠 Context7: Integrating latest DDD implementation techniques"
else
    echo "📋 Standard Mode: Basic domain implementation without MCP enhancements"
fi
```

## 🚀 Enhanced Expert Execution Flow

### Phase 1: Enhanced Domain Implementation Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **Enhanced Implementation Foundation Assessment**

   ```bash
   # Enhanced implementation context with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント・ドメイン実装"
       echo "📊 既存実装パターン分析と最新DDD技法を活用して最適化されたドメイン層を実装します"
   fi
   ```

   Enhanced implementation analysis includes:
   - Test specifications analysis for TDD implementation (MCP Enhanced pattern recognition)
   - Domain model specifications for implementation guidance (MCP Enhanced validation)
   - Existing codebase analysis for consistency and patterns (MCP Enhanced discovery)
   - Framework-specific implementation pattern integration (Context7 Enhanced)

2. **MCP-Enhanced Domain Implementation Strategy**

   - Existing domain pattern mining using Serena MCP
   - Latest DDD implementation techniques from Context7 MCP
   - Cross-reference implementation analysis for consistency
   - Intelligent code generation and refactoring recommendations

### Phase 2: Enhanced Domain Entity Implementation

**Execute enhanced domain implementation:**

1. **MCP-Enhanced Entity Implementation**

   ```bash
   # Enhanced entity implementation with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🔍 Enhanced Entity Implementation:"
       echo "  • Serena: Mining successful entity implementation patterns"
       echo "  • Context7: Applying latest entity design and validation techniques"
       echo "  • Integration: Creating optimized entity implementations with intelligence"
   fi
   ```

2. **Intelligent Value Object Implementation**

   - Value object implementation with pattern validation (MCP Enhanced)
   - Immutable design enforcement with industry standards (Context7 Enhanced)
   - Validation logic optimization with historical patterns (Serena Enhanced)
   - Type safety and performance optimization integration

### Phase 3: Enhanced Business Logic Implementation

**Design enhanced business logic structure:**

1. **Enhanced Domain Service Implementation**

   - Complex business logic implementation with pattern recognition
   - Domain service design with architectural best practices
   - Business rule encoding with validation and testing
   - Performance optimization with industry benchmarks

2. **Enhanced Aggregate Implementation and Validation**

   - Aggregate root implementation with consistency validation
   - Business invariant enforcement with intelligent analysis
   - Transaction boundary optimization with pattern-based recommendations
   - Event-driven architecture integration with best practices

### Phase 4: Enhanced Implementation Documentation Generation

**Create enhanced implementation documentation:**

1. **Enhanced Domain Implementation Document**

   - Implementation architecture with MCP analysis results
   - Code organization and pattern explanations
   - Business logic implementation with traceability
   - Performance and maintainability considerations

2. **Enhanced Refactoring and Optimization Guide**

   - Code quality analysis with intelligent recommendations
   - Refactoring opportunities with historical success patterns
   - Performance optimization with benchmark integration
   - Future enhancement roadmap with strategic guidance

## ✅ Enhanced Built-in Quality Assurance

### Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - Enhanced:**

- [ ] All test cases pass with domain implementation (TDD GREEN phase)
- [ ] Business rules from Given-When-Then scenarios are implemented with pattern validation
- [ ] Domain purity maintained with no infrastructure dependencies (MCP Enhanced validation)
- [ ] Aggregate boundaries and business invariants properly enforced (MCP Enhanced analysis)
- [ ] Implementation patterns aligned with historical success data (MCP Enhanced)

**Recommended Items (SHOULD) - Enhanced:**

- [ ] Existing domain implementation patterns identified and applied (MCP Enhanced)
- [ ] Latest DDD implementation techniques integrated (Context7 Enhanced)
- [ ] Code organization optimized based on pattern analysis
- [ ] Performance implications analyzed and documented
- [ ] Refactoring opportunities identified and prioritized

### Enhanced Quality Metrics

| Indicator | Target Value | Enhanced Target | Actual Value | Result |
|-----------|--------------|-----------------|--------------|--------|
| Test Pass Rate | 100% | 100% (Pattern Validated) | [Pass %] | ✅/❌ |
| Business Rule Implementation | 100% | 100% (MCP Verified) | [Implementation %] | ✅/❌ |
| Domain Purity Score | 100% | 100% (Architecture Compliant) | [Purity %] | ✅/❌ |
| Pattern Implementation Coverage | N/A | 95% (MCP Enhanced) | [Coverage %] | ✅/❌ |

## 📊 Enhanced Standardized Output Format

### Enhanced 実行サマリー

- ✅ **ドメイン実装**: [実装されたエンティティ・値オブジェクト数] (MCP拡張: パターン分析統合)
- ✅ **ビジネスルール実装**: [実装されたルール数] (履歴検証付き)
- ✅ **テスト通過**: [通過テスト数] (品質検証済み)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### Enhanced 成果物

**作成されたファイル (MCP Enhanced):**

- `src/domain/entities/`: パターン分析統合エンティティ実装
- `src/domain/value_objects/`: 最適化値オブジェクト実装
- `src/domain/services/`: インテリジェント・ドメインサービス実装
- `src/domain/aggregates/`: ベストプラクティス統合アグリゲート実装
- `docs/domain/issue-<number>/implementation_guide.md`: 実装ガイド (MCP Enhanced)
- `docs/domain/issue-<number>/pattern_analysis.md`: Serenaパターン分析レポート (MCP Enhanced)
- `docs/domain/issue-<number>/refactoring_guide.md`: Context7最適化ガイド (MCP Enhanced)

### Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/implement-usecase-enhanced <issue-number>` でパターン分析統合アプリケーション層実装
   - `/run-all-tests-enhanced` でインテリジェント統合テスト実行
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的ドメイン実装最適化の実施
   - 履歴パターン学習システムの構築検討

### Enhanced メタデータ更新

```json
{
  "command_executed": "implement-domain-enhanced",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "enhanced-domain-implementation",
  "issue_number": "[issue-number]",
  "mcp_enhancements": {
    "serena_pattern_analysis": true,
    "context7_ddd_practices": true,
    "implementation_pattern_mining": true,
    "cross_reference_analysis": true
  },
  "deliverables": {
    "domain_entities": "src/domain/entities/",
    "value_objects": "src/domain/value_objects/",
    "domain_services": "src/domain/services/",
    "aggregates": "src/domain/aggregates/",
    "implementation_guide": "docs/domain/issue-<number>/implementation_guide.md",
    "pattern_analysis": "docs/domain/issue-<number>/pattern_analysis.md",
    "refactoring_guide": "docs/domain/issue-<number>/refactoring_guide.md"
  },
  "metrics": {
    "entities_implemented": "[number]",
    "value_objects_implemented": "[number]",
    "business_rules_implemented": "[number]",
    "tests_passed": "[number]",
    "pattern_coverage_score": "[percentage]",
    "implementation_quality_score": "[score]"
  },
  "next_recommended": ["implement-usecase-enhanced", "run-all-tests-enhanced"],
  "quality_score": "[score]",
  "mcp_analysis_quality": "[score]"
}
```

---

🎯 MCP拡張ドメイン実装を開始します。ドメイン実装アーキテクトとして、履歴実装パターン分析と最新DDD技法を活用した包括的なドメイン層実装を実施いたします。

**使用方法**:

```bash
/implement-domain-enhanced <issue-number>

# 例
/implement-domain-enhanced 123
```

**MCP拡張機能** (利用可能時):
- 📚 **Serena**: 既存ドメイン実装パターン分析・最適化推奨・リファクタリングガイド
- 🧠 **Context7**: 最新DDD実装技法・フレームワーク固有パターン・パフォーマンス最適化