# 14-apply-feedback-enhanced (MCP-Enhanced Feedback Application)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Feedback Application Specialist** with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core Feedback Application Expertise:**

- **Feedback Analysis**: Systematic review and prioritization of feedback from code reviews, testing, and stakeholder input
- **Quality Improvement**: Implementation of improvements while maintaining system integrity and test coverage
- **Risk Assessment**: Identification and mitigation of risks when applying changes based on feedback
- **Architecture Compliance**: Ensuring all changes align with TDD/DDD/Layered Architecture principles

**MCP-Enhanced Capabilities:**

- **Intelligent Feedback Mining**: Automated feedback extraction and categorization using Serena MCP
- **Context-Aware Improvements**: Context7-enhanced improvement patterns and best practices
- **Impact Analysis**: Complete change impact analysis and optimization recommendations
- **Quality Pattern Recognition**: Advanced quality improvement pattern identification

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Priority-Based Approach**: Address high-impact, low-risk feedback first
2. **Incremental Implementation**: Apply changes in small, testable increments
3. **Continuous Validation**: Run tests after each change to ensure system stability
4. **Documentation Updates**: Keep documentation synchronized with code changes

**MCP-Enhanced Principles:**
5. **Intelligent Analysis**: Leverage Serena for deep feedback impact analysis and pattern recognition
6. **Context-Rich Improvements**: Enhance implementations with Context7 improvement guidance
7. **Automated Quality Assurance**: Build automated quality validation with intelligent recommendations

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Test Preservation**: All existing tests continue to pass after feedback application
- **Quality Maintenance**: Code quality metrics maintain or improve
- **Architecture Integrity**: Clean Architecture principles preserved throughout changes
- **Documentation Sync**: All changes properly documented and traced

**MCP-Enhanced Standards:**

- **Automated Impact Assessment**: 100% change impact analysis with Serena MCP
- **Pattern Compliance**: 95% adherence to improvement best practices from Context7
- **Quality Enhancement**: 90%+ improvement in targeted quality metrics
- **Intelligent Optimization**: Advanced optimization recommendations applied

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Code Analysis + Feedback Mining) + Context7 (Improvement Patterns + Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Feedback Application Phase (14/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Systematic application of review feedback with MCP intelligence  
> ⬅️ **Previous Stage**: 13-review-issue (Implementation Review) or 13-review-issue-enhanced  
> ➡️ **Next Stage**: 15-create-pr (Pull Request Creation)

## 🎯 PHASE PURPOSE: FEEDBACK APPLICATION WITH MCP ENHANCEMENT

**⚠️ Important Notice:**

- **This step focuses on SYSTEMATIC FEEDBACK APPLICATION** - Apply feedback based on priority and intelligence
- **MCP ENHANCEMENT** - Leverage intelligent analysis and improvement pattern guidance
- **QUALITY IMPROVEMENT FOCUS** - Enhance system quality while maintaining integrity
- **COMPREHENSIVE IMPACT ANALYSIS** - Complete change impact assessment and optimization

**What this step does:**

1. `13-review-issue` ← Previous: Implementation review and feedback collection
2. `14-apply-feedback-enhanced` ← **【YOU ARE HERE】Feedback application with MCP**
3. `15-create-pr` ← Next: Pull request creation
4. `16-status-report` ← Next: Status reporting and completion

**Core Activities (Traditional):**

- Collect and analyze feedback from various sources
- Prioritize feedback based on impact and risk assessment
- Apply changes incrementally with proper testing
- Update documentation and maintain quality metrics

**MCP-Enhanced Activities (Additional):**

- Analyze feedback patterns and improvement opportunities using Serena MCP
- Extract optimization recommendations automatically from code analysis
- Apply Context7 improvement patterns and industry best practices
- Create intelligent quality enhancement plans with automated validation

**APPLY FEEDBACK SYSTEMATICALLY WITH INTELLIGENCE.**

## 📋 MCP-Enhanced Feedback Analysis

### Required Setup

```bash
# Validate issue number and MCP session
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /apply-feedback-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🧠 Executing MCP-enhanced feedback application with intelligent analysis..."

# Check MCP session availability (optional enhancement)
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced analysis will be available"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    MCP_AVAILABLE="false"
fi

# Execute the enhanced Python implementation (inherits + extends existing functionality)
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/14-apply-feedback-enhanced.py"

if [[ -f "$SCRIPT_PATH" ]]; then
    echo "✅ Found enhanced implementation: $SCRIPT_PATH"
    uv run "$SCRIPT_PATH" "$ISSUE_NUMBER"
    EXIT_CODE=$?
else
    echo "❌ Enhanced implementation not found: $SCRIPT_PATH"
    echo "💡 Please ensure the Python implementation is available"
    exit 1
fi

if [[ $EXIT_CODE -eq 0 ]]; then
    echo "✅ Feedback application completed successfully"
else
    echo "❌ Feedback application failed with exit code: $EXIT_CODE"
    exit $EXIT_CODE
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Feedback Collection and Analysis (Core + MCP Enhanced)

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **GitHub Issues and PR Feedback Collection**

   - Use Bash tool to collect feedback from GitHub comments using `gh issue view`
   - Extract feedback from recent PR reviews and comments
   - Identify feedback themes and priority areas
   - Document feedback sources and timestamps

2. **Existing Quality Metrics Assessment**
   - Check current test coverage and code quality metrics using Bash tool
   - Identify areas needing improvement based on metrics
   - Establish baseline for improvement measurement

**MCP-Enhanced Analysis (if available):**
3. **Automated Feedback Pattern Discovery**

   - Use mcp__serena__search_for_pattern to identify code smell patterns
   - Use mcp__serena__find_symbol to locate improvement opportunities
   - Use mcp__serena__find_referencing_symbols to analyze change impact
   - Create memory using mcp__serena__write_memory for feedback analysis

4. **Intelligent Quality Assessment**
   - Use mcp__serena__get_symbols_overview to assess codebase health
   - Identify technical debt patterns and improvement opportunities
   - Extract optimization recommendations from code analysis
   - Document findings in quality assessment memory

### Phase 2: Feedback Prioritization and Planning (Core + MCP Enhanced)

**Design the following as expert (Instructions to Claude Code in English):**

**Core Planning Activities:**

1. **Feedback Prioritization Matrix**

   ```
   Categorize feedback by:
   - Impact level (High/Medium/Low)
   - Risk level (High/Medium/Low)
   - Implementation complexity
   - Dependencies between feedback items
   ```

2. **Implementation Planning**

   ```
   For each priority feedback:
   - Define specific implementation steps
   - Identify test validation requirements
   - Plan incremental application approach
   - Document expected outcomes
   ```

**MCP-Enhanced Planning (if available):**
3. **Context7 Improvement Pattern Integration**

```
Use mcp__context7__resolve-library-id for "code-quality"
Use mcp__context7__get-library-docs for improvement patterns
Use mcp__context7__get-library-docs for refactoring best practices
Integrate latest improvement methodologies into planning
```

4. **Technology-Specific Enhancement Guidance**
   ```
   Identify project tech stack from codebase analysis
   Use mcp__context7__resolve-library-id for framework-specific improvements
   Use mcp__context7__get-library-docs for optimization patterns
   Apply technology-specific improvement recommendations
   ```

### Phase 3: Incremental Feedback Application (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Validate prerequisites and environment**

   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "Error: At least one issue number must be specified"
       echo "Usage example: /apply-feedback-enhanced 1"
       exit 1
   fi

   # Run baseline tests
   echo "Running baseline tests..."
   uv run --frozen pytest
   BASELINE_EXIT_CODE=$?
   
   # Capture baseline metrics
   echo "Capturing baseline quality metrics..."
   uv run --frozen ruff check . --statistics > baseline_ruff.txt
   uv run --frozen pytest --cov=src --cov-report=term | grep TOTAL > baseline_coverage.txt
   ```

2. **Apply feedback incrementally with validation**

   ```bash
   # Apply feedback in priority order
   for feedback_item in high_priority medium_priority low_priority; do
       echo "Applying: $feedback_item"
       
       # Pre-change validation
       echo "Running pre-change tests..."
       uv run --frozen pytest
       
       # Apply specific feedback changes
       # (Implementation logic here)
       
       # Post-change validation
       echo "Running post-change tests..."
       uv run --frozen pytest
       POST_CHANGE_EXIT_CODE=$?
       
       if [[ $POST_CHANGE_EXIT_CODE -ne 0 ]]; then
           echo "❌ Tests failed after applying $feedback_item"
           echo "Rolling back changes..."
           # Rollback logic here
           continue
       fi
       
       echo "✅ Successfully applied: $feedback_item"
   done
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Change Application**

```bash
# Enhanced feedback application with MCP analysis
For each feedback item from Serena analysis:
- Apply change impact analysis before implementation
- Use intelligent refactoring patterns from Context7
- Validate architectural compliance automatically
- Generate optimization recommendations
```

4. **Automated Quality Enhancement**

   ```bash
   # Intelligent quality improvement
   Use Serena MCP to identify code duplication patterns
   Apply Context7 refactoring patterns for improvement
   Generate automated test enhancements
   Create quality metric improvement documentation
   ```

### Phase 4: Quality Validation and Documentation (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create feedback application documentation (always)**

   ```bash
   # Standard feedback application document (always created)
   Write "docs/feedback/issue-${ISSUE_NUMBER}-feedback-application.md" with:
   # - Applied feedback summary and categorization
   # - Implementation approach and rationale
   # - Quality metrics before/after comparison
   # - Risk assessment and mitigation strategies
   # - Next steps and remaining feedback items
   ```

2. **Create MCP analysis documents (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced analysis document
       Write "docs/feedback/issue-${ISSUE_NUMBER}-mcp-feedback-analysis.md" with:
       # - MCP-discovered improvement patterns analysis
       # - Automated quality enhancement recommendations
       # - Change impact analysis and optimization results
       # - Context7-enhanced improvement implementation guide
       # - Future optimization roadmap

       # MCP detailed reports
       Write "docs/feedback/issue-${ISSUE_NUMBER}-quality-improvement-report.md" with:
       # - Serena MCP codebase quality analysis summary
       # - Identified optimization opportunities and recommendations
       # - Applied improvement patterns and results
       # - Quality metrics improvement tracking
       # - Context7 pattern integration outcomes

       # Update MCP memory with findings
       Use mcp__serena__write_memory to store:
       # - Feedback application analysis results
       # - Quality improvement outcomes
       # - Optimization recommendation tracking
       # - Pattern application effectiveness
   fi
   ```

3. **Update quality metrics tracking**

   ```bash
   # Capture final metrics and comparison
   echo "Capturing final quality metrics..."
   uv run --frozen ruff check . --statistics > final_ruff.txt
   uv run --frozen pytest --cov=src --cov-report=term | grep TOTAL > final_coverage.txt
   
   # Generate improvement report
   Write "docs/feedback/issue-${ISSUE_NUMBER}-quality-metrics.md" with:
   # - Baseline vs final metrics comparison
   # - Quality improvement percentage calculations
   # - Remaining improvement opportunities
   # - Recommendations for future sprints
   ```

4. **Git commit feedback applications**
   ```bash
   Bash git add .
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       Bash git commit -m "feat: apply feedback for issue ${ISSUE_NUMBER} with MCP enhancement

   Apply systematic feedback based on priority and impact analysis.
   Implement quality improvements while maintaining test coverage.
   Enhanced with MCP intelligent analysis and improvement patterns.

   🎯 Generated with Claude Code
       "
   else
       Bash git commit -m "feat: apply feedback for issue ${ISSUE_NUMBER}

   Apply systematic feedback based on priority and impact analysis.
   Implement quality improvements while maintaining test coverage.

   🎯 Generated with Claude Code
       "
   fi
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP feedback pattern analysis completed
- [ ] Context7 improvement pattern integration applied
- [ ] Enhanced feedback application with intelligence
- [ ] Quality improvement automatically tracked and documented
- [ ] Change impact analysis completed
- [ ] Implementation guidance updated

**Recommended Items (SHOULD):**

- [ ] Technical debt reduction achieved and documented
- [ ] Performance implications analyzed and optimized
- [ ] Security improvements validated
- [ ] Code maintainability enhancements applied

### Quality Metrics

| Metric                              | Target | Actual         | Assessment |
| ----------------------------------- | ------ | -------------- | ---------- |
| Feedback Application Coverage       | 100%   | [Actual Value] | ✅/❌      |
| Quality Metrics Improvement         | 90%    | [Actual Value] | ✅/❌      |
| Test Coverage Maintenance           | 95%    | [Actual Value] | ✅/❌      |
| Architecture Compliance             | 100%   | [Actual Value] | ✅/❌      |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|-----------|
| Pattern Discovery Coverage | 90% | [Actual Value] | ✅/❌ |
| Automated Improvement Application | 95% | [Actual Value] | ✅/❌ |
| Context7 Integration | 85% | [Actual Value] | ✅/❌ |
| Change Impact Accuracy | 100% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **フィードバック収集分析**: GitHub コメント X 件、PR レビュー Y 件を分析完了
- ✅ **優先度付け実装**: 高優先度 A 項目、中優先度 B 項目、低優先度 C 項目を適用
- ✅ **品質メトリクス改善**: カバレッジ X%→Y%、Ruff問題 A→B に改善
- ✅ **ドキュメント更新**: docs/feedback/issue-X-feedback-application.md 作成

**MCP 拡張機能 (利用可能時):**

- ✅ **MCP フィードバック分析**: [X]個のファイル、[Y]個の改善パターン分析完了
- ✅ **自動改善適用**: [A]個の品質改善、[B]個の最適化を自動適用
- ✅ **変更影響分析**: [C]個のコンポーネント影響分析完了
- ✅ **Context7 パターン統合**: 最新改善パターン適用完了
- ✅ **改善ガイダンス生成**: MCP 分析に基づく改善計画更新

### 成果物

**基本ファイル (常に作成):**

- `docs/feedback/issue-X-feedback-application.md`: フィードバック適用記録
- `docs/feedback/issue-X-quality-metrics.md`: 品質メトリクス改善記録
- Updated test coverage and quality metrics

**MCP 拡張ファイル (利用可能時):**

- `docs/feedback/issue-X-mcp-feedback-analysis.md`: MCP フィードバック分析
- `docs/feedback/issue-X-quality-improvement-report.md`: 品質改善詳細レポート
- Updated MCP memory files: フィードバック適用結果の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP 利用時)
**品質改善スコア**: [スコア]/100
**MCP インテリジェンス品質**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/create-pr [issue-numbers]` または `/create-pr-enhanced [issue-numbers]`
2. **推奨**: プルリクエスト作成フェーズに進む
3. **確認推奨**: フィードバック適用結果のレビュー

**ユーザーへのメッセージ (日本語)**:

```
🎉 フィードバック適用完了！

🔧 適用されたフィードバック:
   📊 高優先度: [count] 項目 (100%完了)
   📊 中優先度: [count] 項目 ([percentage]%完了)
   📊 低優先度: [count] 項目 ([percentage]%完了)

📈 品質メトリクス改善:
   ✅ テストカバレッジ: [before]% → [after]% (+[improvement]%)
   ✅ Ruff問題: [before] → [after] (-[reduction])
   ✅ 複雑度スコア: [before] → [after] (-[improvement]%)

📁 作成されたファイル:
   ✅ docs/feedback/issue-X-feedback-application.md
   ✅ docs/feedback/issue-X-quality-metrics.md

🧠 MCP強化機能 (利用時のみ):
   📊 Serena分析: [X]ファイル、[Y]パターン分析
   🔍 自動改善適用: [A]個の品質改善実装
   📋 変更影響分析: [C]個のコンポーネント分析
   🌐 Context7統合: 最新改善パターン適用
   ✅ docs/feedback/issue-X-mcp-feedback-analysis.md
   ✅ docs/feedback/issue-X-quality-improvement-report.md
   ✅ MCP メモリファイル更新

📋 次のステップ (プルリクエスト作成):
   /create-pr [issue-numbers] または /create-pr-enhanced [issue-numbers]

✅ フィードバック適用完了 - プルリクエスト作成準備完了！
```