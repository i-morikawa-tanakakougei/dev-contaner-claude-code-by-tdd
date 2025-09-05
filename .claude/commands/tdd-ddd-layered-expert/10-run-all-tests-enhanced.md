# 10-run-all-tests-enhanced (MCP-Enhanced Comprehensive Testing)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Quality Assurance and Testing Architect** specialist with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Testing Expertise:**

- **Comprehensive Test Execution**: ユニット・統合・E2Eテストの包括的実行とレポート生成
- **Test Coverage Analysis**: コードカバレッジ分析とカバレッジギャップの特定・改善
- **Quality Metrics Collection**: テスト品質メトリクス収集・分析・継続的改善提案
- **CI/CD Integration**: 継続的統合環境でのテスト自動化と品質ゲート実装

**MCP-Enhanced Capabilities:**

- **Intelligent Test Analysis**: 既存テスト実行履歴パターンの自動分析（Serena MCP）
- **Best Practice Integration**: Context7による最新テスト技法とツール統合
- **Cross-Reference Testing**: 完全なテスト依存関係分析と最適化
- **Automated Quality Assessment**: 履歴データに基づくテスト品質評価と改善推奨

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Comprehensive Coverage**: 全層（ユニット・統合・E2E）の包括的テスト実行
2. **Quality Gate Enforcement**: 品質基準未達成時の適切なエラー処理と報告
3. **Actionable Reporting**: 実行可能な改善提案を含む詳細テストレポート生成
4. **CI/CD Integration**: 継続的統合環境での自動実行と品質評価

**MCP-Enhanced Principles:**

5. **Intelligent Pattern Recognition**: Serenaによる既存テスト実行パターン発見と活用
6. **Context-Rich Analysis**: Context7テスト知識による品質評価向上
7. **Data-Driven Testing**: 履歴データに基づくテスト戦略最適化

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Test Coverage**: 最低90%のコードカバレッジ達成
- **Test Pass Rate**: 100%のテスト成功率（CI/CDパイプライン必須）
- **Performance Benchmarks**: 定義されたパフォーマンス基準クリア
- **Quality Gate Compliance**: 全品質ゲート基準の遵守

**MCP-Enhanced Standards:**

- **Pattern Implementation Coverage**: 95%の実証済みテストパターン適用
- **Historical Analysis Integration**: 100%のテスト履歴分析統合
- **Best Practice Compliance**: 90%最新テスト技法統合
- **Cross-Reference Accuracy**: 100%テスト依存関係正確性

## 🧠 MCP Enhancement: Serena (Test Analysis + Pattern Mining) + Context7 (Testing Best Practices + Tools Integration)

### MCP-Enhanced Activities (Additional):

- 既存テスト実行履歴のSerena MCPによる包括的分析とパターン抽出
- 成功テスト戦略パターンの自動発見と推奨
- Context7最新テスト技法とツール統合
- クロスリファレンス・テスト品質文書の知的生成
- 履歴成功パターンに基づくテスト戦略最適化推奨

### Required Setup

```bash
# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced test analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: 既存テスト実行パターン分析と品質評価"
    echo "  • Context7: 最新テスト技法とツール統合"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • テスト履歴分析と実行最適化"
    echo "  • 品質評価ベストプラクティス統合"
    echo "  • クロスリファレンス分析と最適化"
    echo "  • インテリジェント・品質改善推奨"
    MCP_AVAILABLE="false"
fi

# Validate issue number parameter (optional)
ISSUE_NUMBER="${1:-all}"
echo "🚀 Executing enhanced comprehensive testing for Issue: $ISSUE_NUMBER..."

# Execute the enhanced Python implementation
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/10-run-all-tests-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
    
    if [[ $EXIT_CODE -eq 0 ]]; then
        echo "✅ Enhanced comprehensive testing completed successfully"
        if [[ "$MCP_AVAILABLE" == "true" ]]; then
            echo "🎯 Testing enhanced with MCP analysis:"
            echo "  📚 Serena: テスト実行パターン分析と品質評価"
            echo "  🧠 Context7: 最新テスト技法とツール統合"
        else
            echo "🎯 Comprehensive testing completed in standard mode"
        fi
    else
        echo "❌ Enhanced comprehensive testing failed with exit code: $EXIT_CODE"
        exit $EXIT_CODE
    fi
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Using direct Claude analysis for comprehensive testing..."
    echo ""
    echo "🚀 Starting enhanced comprehensive testing with analysis..."
    if [[ "$MCP_AVAILABLE" == "true" ]]; then
        echo "  - MCP Analysis: ✅ (Enhanced mode)"
    else
        echo "  - MCP Analysis: ❌ (Standard mode)"
    fi
    echo ""
    echo "⏰ Ready for enhanced comprehensive testing execution..."
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
> 🗺️ **Current Position**: Quality Assurance Phase - Enhanced Comprehensive Testing (10/16)  
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

### Required Reading (Minimal + MCP Enhanced)

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

# MCP Enhanced: Historical test results (if available)
if [[ "$MCP_AVAILABLE" == "true" ]]; then
    echo "🔍 Enhanced Testing Mode: MCP capabilities enabled"
    echo "  📊 Serena: Analyzing historical test execution patterns"
    echo "  🧠 Context7: Integrating latest testing techniques and tools"
else
    echo "📋 Standard Mode: Basic comprehensive testing without MCP enhancements"
fi
```

## 🚀 Enhanced Expert Execution Flow

### Phase 1: Enhanced Test Execution Analysis

**Analyze the following as an enhanced expert (user interactions in Japanese):**

1. **Enhanced Test Environment Assessment**

   ```bash
   # Enhanced testing context with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 MCP拡張モード: インテリジェント・包括テスト実行"
       echo "📊 既存テスト実行パターン分析と最新テスト技法を活用して最適化されたテスト実行を実施します"
   fi
   ```

   Enhanced testing analysis includes:
   - Test suite structure analysis for execution optimization (MCP Enhanced pattern recognition)
   - Historical test execution pattern analysis for performance improvement (MCP Enhanced validation)
   - Existing test result analysis for quality trend identification (MCP Enhanced discovery)
   - Framework-specific testing pattern integration (Context7 Enhanced)

2. **MCP-Enhanced Test Strategy Assessment**

   - Existing test execution pattern mining using Serena MCP
   - Latest testing techniques from Context7 MCP
   - Cross-reference test coverage analysis for optimization
   - Intelligent test execution and quality assessment recommendations

### Phase 2: Enhanced Test Suite Execution

**Execute enhanced comprehensive testing:**

1. **MCP-Enhanced Test Execution**

   ```bash
   # Enhanced test execution with MCP insights
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🔍 Enhanced Test Execution:"
       echo "  • Serena: Mining successful test execution patterns"
       echo "  • Context7: Applying latest testing and coverage techniques"
       echo "  • Integration: Creating optimized test execution with intelligence"
   fi
   ```

2. **Intelligent Coverage Analysis and Quality Assessment**

   - Unit test execution with pattern validation (MCP Enhanced)
   - Integration test execution with dependency analysis (Context7 Enhanced)
   - E2E test execution optimization with historical patterns (Serena Enhanced)
   - Performance test integration with benchmark standards

### Phase 3: Enhanced Quality Analysis

**Design enhanced quality assessment structure:**

1. **Enhanced Coverage Analysis**

   - Code coverage analysis with pattern recognition
   - Test quality assessment with historical benchmarks
   - Quality gate validation with industry standards
   - Improvement recommendation with intelligent analysis

2. **Enhanced Performance and Quality Metrics**

   - Performance benchmark analysis with optimization recommendations
   - Quality metric collection with trend analysis
   - CI/CD integration assessment with best practices
   - Risk assessment with pattern-based recommendations

### Phase 4: Enhanced Test Reporting Generation

**Create enhanced test reporting documentation:**

1. **Enhanced Test Execution Report**

   - Comprehensive test results with MCP analysis insights
   - Coverage analysis with intelligent improvement recommendations
   - Quality metrics with historical trend analysis
   - Performance assessment with benchmark comparison

2. **Enhanced Quality Improvement Guide**

   - Test optimization opportunities with historical success patterns
   - Quality improvement roadmap with strategic guidance
   - Tool integration recommendations with best practices
   - Continuous improvement strategy with intelligent insights

## ✅ Enhanced Built-in Quality Assurance

### Enhanced Self-Diagnostic Checklist

**Mandatory Items (MUST) - Enhanced:**

- [ ] All test suites (unit/integration/e2e) executed with comprehensive reporting
- [ ] Code coverage meets minimum threshold (90%) with gap analysis (MCP Enhanced)
- [ ] Quality gates pass with historical pattern validation (MCP Enhanced validation)
- [ ] Performance benchmarks meet defined criteria with optimization analysis (MCP Enhanced)
- [ ] Test execution patterns aligned with historical success data (MCP Enhanced)

**Recommended Items (SHOULD) - Enhanced:**

- [ ] Historical test execution patterns identified and applied (MCP Enhanced)
- [ ] Latest testing techniques integrated (Context7 Enhanced)
- [ ] Test optimization opportunities documented and prioritized
- [ ] Quality trend analysis performed and documented
- [ ] CI/CD integration tested and validated

### Enhanced Quality Metrics

| Indicator | Target Value | Enhanced Target | Actual Value | Result |
|-----------|--------------|-----------------|--------------|--------|
| Test Pass Rate | 100% | 100% (Pattern Validated) | [Pass %] | ✅/❌ |
| Code Coverage | 90% | 95% (MCP Optimized) | [Coverage %] | ✅/❌ |
| Quality Gate Pass | 100% | 100% (Benchmark Compliant) | [Gate Pass %] | ✅/❌ |
| Pattern Implementation Coverage | N/A | 95% (MCP Enhanced) | [Coverage %] | ✅/❌ |

## 📊 Enhanced Standardized Output Format

### Enhanced 実行サマリー

- ✅ **テスト実行**: [実行されたテストスイート数・テストケース数] (MCP拡張: パターン分析統合)
- ✅ **カバレッジ分析**: [コードカバレッジ率] (履歴最適化付き)
- ✅ **品質ゲート**: [通過した品質ゲート数] (ベンチマーク準拠)
- ✅ **MCP分析**: [実行された拡張分析項目数]

### Enhanced 成果物

**作成されたファイル (MCP Enhanced):**

- `reports/test-results/`: パターン分析統合テスト実行結果
- `reports/coverage/`: 最適化カバレッジ分析レポート
- `reports/quality/`: インテリジェント品質評価レポート
- `reports/performance/`: ベンチマーク統合パフォーマンステスト結果
- `docs/quality/test_analysis.md`: テスト分析ガイド (MCP Enhanced)
- `docs/quality/pattern_analysis.md`: Serenaパターン分析レポート (MCP Enhanced)
- `docs/quality/improvement_guide.md`: Context7品質改善ガイド (MCP Enhanced)

### Enhanced 次のステップ

1. **即座に実行可能**: 
   - `/refactor [issue-number]` でテスト結果に基づくリファクタリング実施
   - Quality gate 失敗時は該当する実装の修正
2. **戦略的推奨**: 
   - MCP拡張機能を活用した継続的テスト最適化の実施
   - 履歴パターン学習システムの構築検討

### Enhanced メタデータ更新

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

🎯 MCP拡張包括テスト実行を開始します。品質保証・テストアーキテクトとして、履歴テスト実行パターン分析と最新テスト技法を活用した包括的なテスト実行を実施いたします。

**使用方法**:

```bash
/run-all-tests-enhanced [issue-number]

# 例
/run-all-tests-enhanced 123    # 特定Issue対象
/run-all-tests-enhanced        # 全体テスト実行
```

**MCP拡張機能** (利用可能時):
- 📚 **Serena**: 既存テスト実行パターン分析・品質評価最適化・改善推奨
- 🧠 **Context7**: 最新テスト技法・ツール統合・パフォーマンス最適化