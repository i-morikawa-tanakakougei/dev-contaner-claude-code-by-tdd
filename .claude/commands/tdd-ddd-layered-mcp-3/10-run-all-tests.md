# 10-run-all-tests-enhanced (MCP-3 MCP-3 Enhanced Comprehensive Testing)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Quality Assurance and Testing Architect** specialist with **MCP-3 Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP MCP-3 Enhanced)

**Core Testing Expertise:**

- **Comprehensive Test Execution**: ユニット・統合・E2Eテストの包括的実行とレポート生成
- **Test Coverage Analysis**: コードカバレッジ分析とカバレッジギャップの特定・改善
- **Quality Metrics Collection**: テスト品質メトリクス収集・分析・継続的改善提案
- **CI/CD Integration**: 継続的統合環境でのテスト自動化と品質ゲート実装

**MCP-3 MCP-3 Enhanced Capabilities:**

- **Systematic Test Strategy Analysis**: Sequential MCPによる体系的テスト戦略分析と段階的品質評価
- **Intelligent Test Analysis**: 既存テスト実行履歴パターンの自動分析（Serena MCP）
- **Best Practice Integration**: Context7による最新テスト技法とツール統合
- **Cross-Reference Testing**: 完全なテスト依存関係分析と最適化
- **Automated Quality Assessment**: 履歴データに基づくテスト品質評価と改善推奨

### Execution Principles (Core + MCP MCP-3 Enhanced)

**Core Principles:**

1. **Comprehensive Coverage**: 全層（ユニット・統合・E2E）の包括的テスト実行
2. **Quality Gate Enforcement**: 品質基準未達成時の適切なエラー処理と報告
3. **Actionable Reporting**: 実行可能な改善提案を含む詳細テストレポート生成
4. **CI/CD Integration**: 継続的統合環境での自動実行と品質評価

**MCP-3 MCP-3 Enhanced Principles:**

5. **Systematic Quality Analysis**: Sequential MCPによる体系的品質分析と段階的評価
6. **Intelligent Pattern Recognition**: Serenaによる既存テスト実行パターン発見と活用
7. **Context-Rich Analysis**: Context7テスト知識による品質評価向上
8. **Data-Driven Testing**: 履歴データに基づくテスト戦略最適化

### Quality Standards (Core + MCP MCP-3 Enhanced)

**Core Standards:**

- **Test Coverage**: 最低90%のコードカバレッジ達成
- **Test Pass Rate**: 100%のテスト成功率（CI/CDパイプライン必須）
- **Performance Benchmarks**: 定義されたパフォーマンス基準クリア
- **Quality Gate Compliance**: 全品質ゲート基準の遵守

**MCP-3 MCP-3 Enhanced Standards:**

- **Systematic Analysis Coverage**: 95%の体系的テスト分析適用
- **Pattern Implementation Coverage**: 95%の実証済みテストパターン適用
- **Historical Analysis Integration**: 100%のテスト履歴分析統合
- **Best Practice Compliance**: 90%最新テスト技法統合
- **Cross-Reference Accuracy**: 100%テスト依存関係正確性

## 🧠 MCP-3 Enhancement: Sequential (Systematic Testing Analysis) + Serena (Test Analysis + Pattern Mining) + Context7 (Testing Best Practices + Tools Integration)

### MCP-3 MCP-3 Enhanced Activities (Additional):

- Sequential MCPによる体系的テスト戦略分析と段階的品質評価
- 既存テスト実行履歴のSerena MCPによる包括的分析とパターン抽出
- 成功テスト戦略パターンの自動発見と推奨
- Context7最新テスト技法とツール統合
- クロスリファレンス・テスト品質文書の知的生成
- 履歴成功パターンに基づくテスト戦略最適化推奨

### Required Setup

```bash
# MCP-3 Availability Check (Standardized Pattern)
echo "🔧 Checking MCP availability..."

if command -v mcp__serena__think_about_collected_information &> /dev/null; then
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

# Validate issue number parameter (optional)
ISSUE_NUMBER="${1:-all}"
echo "🚀 Executing MCP-3 enhanced comprehensive testing for Issue: $ISSUE_NUMBER..."

# Step 1: 状況分析・複雑性判断（文脈駆動）
echo "📊 Analyzing task complexity and requirements..."
echo "🧪 Quality assurance task - Comprehensive testing with systematic analysis"

# 複雑性判断による適応的統合
if [[ "$MCP_SEQUENTIAL" == "available" && ("$ISSUE_NUMBER" != "all" || -d "tests/integration" || -d "tests/e2e") ]]; then
    echo "🧩 Complex testing scenario detected - Using Sequential MCP for systematic analysis"
    echo "✅ Task meets Sequential MCP criteria: Systematic testing analysis needed"
    MCP3_TEST_MODE="ENHANCED"
else
    echo "⚡ Standard testing task - Using Serena + Context7 integration"
    MCP3_TEST_MODE="STANDARD"
fi

# MCP-3 MCP-3 Enhanced Comprehensive Testing - Direct Bash Implementation
echo "🧪 Starting MCP-3 MCP-3 Enhanced Comprehensive Testing..."

# Phase 1: MCP-3 Test Environment Analysis
echo "📊 Phase 1: MCP-3 test environment analysis..."
if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
    echo "✅ MCP-3 MCP-3 Enhanced Testing Mode Activated"
    echo "🔍 Available Capabilities:"
    echo "  • Sequential: Systematic test strategy analysis and quality assessment"
    echo "  • Serena: Historical test pattern analysis and optimization"
    echo "  • Context7: Latest testing techniques and tools integration"
    echo "  • Comprehensive: Multi-layer quality analysis and reporting"
else
    echo "📋 Standard testing mode with available MCP tools"
fi

# Phase 2: Sequential MCP + Test Execution
echo "🎯 Phase 2: Sequential MCP systematic analysis with comprehensive testing..."
if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
    echo "🧩 Sequential MCP MCP-3 Enhanced: Multi-step systematic testing analysis..."
    
    # Sequential MCP による体系的テスト分析
    Use mcp__sequential-thinking__sequentialthinking to systematically analyze: "Comprehensive testing strategy for issue ${ISSUE_NUMBER}: Need to execute unit→integration→e2e test layers with quality assessment. Break down into logical test components, identify testing interdependencies and quality gates, create step-by-step quality assurance plan."
    
    echo "🔍 MCP-3 Enhanced Comprehensive Testing:"
    echo "  • Serena: Mining successful test execution patterns"
    echo "  • Context7: Applying latest testing techniques and tools"
    echo "  • Integration: Creating comprehensive test analysis and optimization"
fi

# Phase 3: MCP-3 Enhanced Quality Assessment
echo "⚡ Phase 3: MCP-3 Enhanced quality assessment..."
# MCP-3 Enhanced test results analysis and quality metrics with MCP insights

# Phase 4: MCP-3 Enhanced Test Reporting
echo "📚 Phase 4: MCP-3 Enhanced test reporting..."

if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
    echo "✅ MCP-3 enhanced comprehensive testing completed with intelligence:"
    echo "  🧩 Sequential: 体系的テスト戦略分析と品質評価"
    echo "  📚 Serena: テスト実行パターン分析と品質評価"
    echo "  🧠 Context7: 最新テスト技法とツール統合"
else
    echo "✅ Comprehensive testing completed in standard mode"
fi

# MCP利用不可時のGraceful Degradation
if [[ "$MCP_SERENA" == "unavailable" ]]; then
    echo "📋 Running without test pattern analysis - manual analysis required"
fi

if [[ "$MCP_CONTEXT7" == "unavailable" ]]; then
    echo "📚 Running without latest testing practices - using standard approaches"
fi

if [[ "$MCP_SEQUENTIAL" == "unavailable" && "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
    echo "🧩 Complex testing task but Sequential MCP unavailable"
    echo "📋 Using structured manual approach with step-by-step quality checklists"
fi

echo "⏰ MCP-3 enhanced comprehensive testing ready for execution..."
```

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Quality Assurance Phase - MCP-3 Enhanced Comprehensive Testing (10/16)  
> 🎯 **Phase Purpose**: Execute comprehensive test suite with intelligent analysis and quality assessment  
> ⬅️ **Previous Stage**: 09-implement-presentation (Presentation Implementation)  
> ➡️ **Next Stage**: 11-refactor (Code Refactoring) or Feature Complete

## 🎯 PHASE PURPOSE: ENHANCED COMPREHENSIVE TESTING EXECUTION

**⚠️ Important Notice:**

- **This step focuses on COMPREHENSIVE TEST EXECUTION** - Run all test types with intelligent analysis
- **QUALITY ASSURANCE** - Ensure all quality gates pass with detailed reporting
- **COVERAGE ANALYSIS** - Generate comprehensive test coverage analysis with improvement recommendations
- **MCP ENHANCEMENT** - Leverage intelligent test analysis and historical optimization

**What this enhanced step does:**

1. `/implement-presentation` ← Previous: Complete implementation stack
2. `/run-all-tests-enhanced [issue-number]` ← **【YOU ARE HERE】Comprehensive testing with MCP**
3. `/refactor` ← Next: Code refactoring based on test results
4. Complete development cycle validation

**EXECUTE COMPREHENSIVE TESTING WITH MCP INTELLIGENCE.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal + MCP MCP-3 Enhanced)

```bash
# Standard project state checks
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read docs/metadata/project-state.json
fi

# Test configurations and existing results
if [[ -f "pyproject.toml" ]]; then
    Read pyproject.toml for test configuration
fi

if [[ -d "tests/" ]]; then
    Glob tests/**/*.py for test files structure
fi

# MCP MCP-3 Enhanced: Historical test results (if available)
if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
    echo "🔍 MCP-3 Enhanced Testing Mode: MCP capabilities enabled"
    echo "  📊 Serena: Analyzing historical test execution patterns"
    echo "  🧠 Context7: Integrating latest testing techniques and tools"
else
    echo "📋 Standard Mode: Basic comprehensive testing without MCP enhancements"
fi
```

## 🚀 MCP-3 Enhanced Expert Execution Flow

### Phase 1: MCP-3 Enhanced Test Execution Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **MCP-3 Enhanced Test Environment Assessment**

   ```bash
   # MCP-3 Enhanced testing context with MCP insights
   if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント・包括テスト実行"
       echo "📊 既存テスト実行パターン分析と最新テスト技法を活用して最適化されたテスト実行を実施します"
   fi
   ```

   MCP-3 Enhanced testing analysis includes:
   - Test suite structure analysis for execution optimization (MCP MCP-3 Enhanced pattern recognition)
   - Historical test execution pattern analysis for performance improvement (MCP MCP-3 Enhanced validation)
   - Existing test result analysis for quality trend identification (MCP MCP-3 Enhanced discovery)
   - Framework-specific testing pattern integration (Context7 MCP-3 Enhanced)

2. **MCP-3 MCP-3 Enhanced Test Strategy Assessment**

   - Existing test execution pattern mining using Serena MCP
   - Latest testing techniques from Context7 MCP
   - Cross-reference test coverage analysis for optimization
   - Intelligent test execution and quality assessment recommendations

### Phase 2: MCP-3 Enhanced Test Suite Execution

**Execute enhanced comprehensive testing:**

1. **MCP-3 MCP-3 Enhanced Test Execution**

   ```bash
   # MCP-3 Enhanced test execution with MCP insights
   if [[ "$MCP3_TEST_MODE" == "ENHANCED" ]]; then
       echo "🔍 MCP-3 Enhanced Test Execution:"
       echo "  • Serena: Mining successful test execution patterns"
       echo "  • Context7: Applying latest testing and coverage techniques"
       echo "  • Integration: Creating optimized test execution with intelligence"
   fi
   ```

2. **Intelligent Coverage Analysis and Quality Assessment**

   - Unit test execution with pattern validation (MCP MCP-3 Enhanced)
   - Integration test execution with dependency analysis (Context7 MCP-3 Enhanced)
   - E2E test execution optimization with historical patterns (Serena MCP-3 Enhanced)
   - Performance test integration with benchmark standards

### Phase 3: MCP-3 Enhanced Quality Analysis

**Design enhanced quality assessment structure:**

1. **MCP-3 Enhanced Coverage Analysis**

   - Code coverage analysis with pattern recognition
   - Test quality assessment with historical benchmarks
   - Quality gate validation with industry standards
   - Improvement recommendation with intelligent analysis

2. **MCP-3 Enhanced Performance and Quality Metrics**

   - Performance benchmark analysis with optimization recommendations
   - Quality metric collection with trend analysis
   - CI/CD integration assessment with best practices
   - Risk assessment with pattern-based recommendations

### Phase 4: MCP-3 Enhanced Test Reporting Generation

**Create enhanced test reporting documentation:**

1. **MCP-3 Enhanced Test Execution Report**

   - Comprehensive test results with MCP analysis insights
   - Coverage analysis with intelligent improvement recommendations
   - Quality metrics with historical trend analysis
   - Performance assessment with benchmark comparison

2. **MCP-3 Enhanced Quality Improvement Guide**

   - Test optimization opportunities with historical success patterns
   - Quality improvement roadmap with strategic guidance
   - Tool integration recommendations with best practices
   - Continuous improvement strategy with intelligent insights

## ✅ MCP-3 Enhanced Built-in Quality Assurance

### MCP-3 Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - MCP-3 Enhanced:**

- [ ] All test suites (unit/integration/e2e) executed with comprehensive reporting
- [ ] Code coverage meets minimum threshold (90%) with gap analysis (MCP MCP-3 Enhanced)
- [ ] Quality gates pass with historical pattern validation (MCP MCP-3 Enhanced validation)
- [ ] Performance benchmarks meet defined criteria with optimization analysis (MCP MCP-3 Enhanced)
- [ ] Test execution patterns aligned with historical success data (MCP MCP-3 Enhanced)

**Recommended Items (SHOULD) - MCP-3 Enhanced:**

- [ ] Historical test execution patterns identified and applied (MCP MCP-3 Enhanced)
- [ ] Latest testing techniques integrated (Context7 MCP-3 Enhanced)
- [ ] Test optimization opportunities documented and prioritized
- [ ] Quality trend analysis performed and documented
- [ ] CI/CD integration tested and validated

### MCP-3 Enhanced Quality Metrics

| Indicator | Target Value | MCP-3 Enhanced Target | Actual Value | Result |
|-----------|--------------|-----------------|--------------|--------|
| Test Pass Rate | 100% | 100% (Pattern Validated) | [Pass %] | ✅/❌ |
| Code Coverage | 90% | 95% (MCP Optimized) | [Coverage %] | ✅/❌ |
| Quality Gate Pass | 100% | 100% (Benchmark Compliant) | [Gate Pass %] | ✅/❌ |
| Pattern Implementation Coverage | N/A | 95% (MCP MCP-3 Enhanced) | [Coverage %] | ✅/❌ |

## 📊 MCP-3 Enhanced Standardized Output Format

### MCP-3 Enhanced 実行サマリー

- ✅ **テスト実行**: [実行されたテストスイート数・テストケース数] (MCP拡張: パターン分析統合)
- ✅ **カバレッジ分析**: [コードカバレッジ率] (履歴最適化付き)
- ✅ **品質ゲート**: [通過した品質ゲート数] (ベンチマーク準拠)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### MCP-3 Enhanced 成果物

**作成されたファイル (MCP MCP-3 Enhanced):**

- `reports/test-results/`: パターン分析統合テスト実行結果
- `reports/coverage/`: 最適化カバレッジ分析レポート
- `reports/quality/`: インテリジェント品質評価レポート
- `reports/performance/`: ベンチマーク統合パフォーマンステスト結果
- `docs/quality/test_analysis.md`: テスト分析ガイド (MCP MCP-3 Enhanced)
- `docs/quality/pattern_analysis.md`: Serenaパターン分析レポート (MCP MCP-3 Enhanced)
- `docs/quality/improvement_guide.md`: Context7品質改善ガイド (MCP MCP-3 Enhanced)

### MCP-3 Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/refactor [issue-number]` でテスト結果に基づくリファクタリング実施
   - Quality gate 失敗時は該当する実装の修正
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的テスト最適化の実施
   - 履歴パターン学習システムの構築検討

### MCP-3 Enhanced メタデータ更新

```json
{
  "command_executed": "run-all-tests-enhanced",
  "timestamp": "[ISO-8601 timestamp]",
  "status": "[SUCCESS|PARTIAL|FAILED]",
  "phase": "enhanced-comprehensive-testing",
  "issue_number": "[issue-number or 'all']",
  "mcp_enhancements": {
    "serena_test_analysis": true,
    "context7_testing_practices": true,
    "test_pattern_mining": true,
    "cross_reference_analysis": true
  },
  "deliverables": {
    "test_results": "reports/test-results/",
    "coverage_analysis": "reports/coverage/",
    "quality_reports": "reports/quality/",
    "performance_results": "reports/performance/",
    "test_analysis": "docs/quality/test_analysis.md",
    "pattern_analysis": "docs/quality/pattern_analysis.md",
    "improvement_guide": "docs/quality/improvement_guide.md"
  },
  "metrics": {
    "tests_executed": "[number]",
    "test_pass_rate": "[percentage]",
    "code_coverage": "[percentage]",
    "quality_gates_passed": "[number]",
    "pattern_coverage_score": "[percentage]",
    "quality_score": "[score]"
  },
  "next_recommended": ["refactor", "review-quality"],
  "quality_score": "[score]",
  "mcp_analysis_quality": "[score]"
}
```

---

🎯 MCP-3拡張包括テスト実行を開始します。品質保証・テストアーキテクトとして、Sequential体系的分析、履歴テスト実行パターン分析、最新テスト技法を活用した包括的なテスト実行を実施いたします。

**使用方法**:

```bash
/run-all-tests-enhanced [issue-number]

# 例
/run-all-tests-enhanced 123    # 特定Issue対象
/run-all-tests-enhanced        # 全体テスト実行
```

**MCP-3拡張機能** (利用可能時):
- 🧩 **Sequential**: 体系的テスト戦略分析・段階的品質評価・総合的品質アセスメント
- 📚 **Serena**: 既存テスト実行パターン分析・品質評価最適化・改善推奨
- 🧠 **Context7**: 最新テスト技法・ツール統合・パフォーマンス最適化