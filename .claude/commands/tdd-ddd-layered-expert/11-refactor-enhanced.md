# /refactor-enhanced [issue-numbers] - MCP統合インテリジェントリファクタリング

## 🎯 Purpose and Scope

Execute TDD REFACTOR phase with MCP-enhanced intelligence for code quality improvement and technical debt reduction. This enhanced command provides automated code analysis, pattern recognition, and intelligent refactoring recommendations.

### Your Expertise (Core + MCP Enhanced)

**Core Refactoring Expertise:**

- **TDD REFACTOR Mastery**: Safe refactoring while maintaining GREEN tests
- **Code Quality Analysis**: Systematic detection of code smells and anti-patterns
- **Performance Optimization**: Identifying and resolving performance bottlenecks
- **Architectural Improvement**: Enhancing code structure and maintainability

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: Automated code quality assessment using Serena MCP
- **Pattern-Based Optimization**: Context7-enhanced refactoring patterns and best practices
- **Technical Debt Discovery**: Comprehensive analysis of refactoring opportunities
- **Performance Intelligence**: Automated performance bottleneck identification

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Test Safety**: Never break existing tests during refactoring
2. **Incremental Changes**: Make small, focused improvements step by step
3. **Behavior Preservation**: Maintain all existing functionality

**MCP-Enhanced Principles:**
4. **Intelligent Analysis**: Leverage Serena for deep code quality analysis
5. **Pattern-Driven Improvement**: Apply Context7 refactoring patterns and industry best practices
6. **Automated Optimization**: Use MCP intelligence for systematic code improvement

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Test Success**: 100% tests remain GREEN throughout refactoring
- **Code Quality Improvement**: Measurable improvement in linting and type checking
- **Documentation Updates**: All affected documentation updated accordingly

**MCP-Enhanced Standards:**

- **Code Smell Elimination**: 95% of identified code smells addressed
- **Pattern Compliance**: 90% adherence to modern refactoring patterns
- **Performance Improvement**: 15%+ improvement in identified bottlenecks
- **Technical Debt Reduction**: 80%+ of technical debt items addressed

---

## 🚀 Commands in Workflow Context

### Position in Development Flow

```
📋 Current Position: /refactor-enhanced
├── 00. create-vision ← Vision and core scenarios
├── 02. sprint-planning ← Sprint planning and tickets
├── 03. create-use-case ← Use case specifications
├── 04. domain-modeling ← Domain model design
├── 05. create-tests ← TDD RED (create failing tests)
├── 06. implement-domain ← Domain layer (GREEN)
├── 07. implement-usecase ← Application layer (GREEN)
├── 08. implement-infra ← Infrastructure layer (GREEN)
├── 09. implement-presentation ← Presentation layer (GREEN)
├── 10. run-all-tests ← Verify tests pass
├── 11. refactor ← **Current: Code quality improvement**
├── 12. next iteration ← Move to next feature
```

4. `10-run-all-tests` ← Previous: Verify all tests pass (required for refactoring)

**Core Activities (Traditional):**

- Improve code quality while maintaining GREEN tests
- Remove duplication and simplify complex methods
- Optimize performance bottlenecks
- Update documentation and ensure consistency

**MCP-Enhanced Activities (Additional):**

- Analyze codebase for refactoring opportunities using Serena MCP
- Extract technical debt patterns automatically
- Apply Context7 refactoring patterns and best practices
- Generate comprehensive improvement recommendations

---

## 🔧 Setup Script

Execute this comprehensive setup to initialize MCP-enhanced refactoring environment:

```bash
#!/bin/bash

# Issue number validation
if [[ $# -eq 0 ]]; then
    echo "❌ Issue number is required"
    echo "Usage: /refactor-enhanced [issue-numbers]"
    exit 1
fi

# MCP availability check
echo "🔍 MCP統合リファクタリングシステム初期化中..."
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ Serena MCP detected - Enhanced refactoring analysis available"
    echo "🎯 Intelligent code quality analysis enabled"
    MCP_AVAILABLE="true"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    MCP_AVAILABLE="false"
fi

# GitHub integration check
if command -v gh &> /dev/null && gh auth status &> /dev/null; then
    echo "✅ GitHub CLI authenticated - Issue integration available"
    GITHUB_AVAILABLE="true"

    # Fetch issue data for better context
    for issue_num in $(echo $1 | tr ',' ' '); do
        if gh issue view "$issue_num" --json title,body,labels > /tmp/gh_issue_${issue_num}.json 2>/dev/null; then
            echo "📋 Issue #${issue_num} data retrieved for refactoring context"
        else
            echo "⚠️ Could not fetch issue #${issue_num} data"
        fi
    done
else
    echo "ℹ️ GitHub CLI not available - Running without issue integration"
    GITHUB_AVAILABLE="false"
fi

# Initialize enhanced refactoring environment
ISSUE_NUMBERS="$1"
echo "🎯 Enhanced Refactoring Target: Issues [$ISSUE_NUMBERS]"
echo "📊 MCP Intelligence: $MCP_AVAILABLE"
echo "🔗 GitHub Integration: $GITHUB_AVAILABLE"

# Create refactoring workspace
mkdir -p docs/refactoring/issue-reports
mkdir -p tests/quality/refactoring-reports

echo "✅ MCP統合リファクタリング環境準備完了"
echo ""
```

---

## 📊 Analysis Phase

**Analyze the following as expert (User interactions in Japanese):**

**Core Analysis Activities:**

1. **Test Status Verification**

   - Run complete test suite using `uv run --frozen pytest` to ensure all tests are GREEN
   - Verify test coverage using `uv run --frozen pytest --cov` 
   - Identify any failing tests that need fixing before refactoring
   - Analyze test structure for potential improvements
   - Ensure no tests are skipped or ignored
   - Document current test baseline for safety

2. **Code Quality Assessment**
   - Run comprehensive linting using `uv run --frozen ruff check . --show-source`
   - Execute type checking with `uv run --frozen pyright`
   - Analyze cyclomatic complexity and code metrics
   - Identify code smells and anti-patterns
   - Review dependency structures and coupling issues
   - Evaluate naming consistency and conventions

**MCP-Enhanced Analysis (if available):**
3. **Automated Code Quality Discovery**

- Use mcp__serena__get_symbols_overview to scan entire codebase for quality issues
- Use mcp__serena__find_symbol to identify complex methods and classes
- Use mcp__serena__search_for_pattern to find code duplication patterns
- Create memory using mcp__serena__write_memory for refactoring opportunities

4. **Intelligent Technical Debt Mining**
   - Use mcp__serena__find_referencing_symbols to analyze coupling complexity
   - Extract performance bottlenecks using pattern analysis
   - Identify architectural inconsistencies automatically
   - Document refactoring priorities in architecture memory

---

## 🎨 Design Phase

**Design the following as expert (Instructions to Claude Code in English):**

**Core Design Activities:**

1. **Refactoring Strategy Design**

   ```
   For each identified improvement area:
   - Plan incremental refactoring steps
   - Define safety checkpoints with tests
   - Prioritize changes by impact and risk
   - Design rollback strategies for safety
   ```

2. **Domain Layer Refactoring Plan**

   ```
   For domain improvements:
   - Extract common entity behaviors to base classes
   - Remove duplication in business logic
   - Simplify complex domain methods
   - Ensure ubiquitous language consistency
   ```

3. **Application Layer Optimization Plan**

   ```
   For application layer improvements:
   - Reduce use case complexity
   - Extract common validation patterns
   - Standardize error handling
   - Optimize DTO conversions
   ```

4. **Infrastructure & Presentation Refactoring Plan**
   ```
   For outer layer improvements:
   - Optimize database queries and connections
   - Standardize API response patterns
   - Extract common validation logic
   - Improve error message consistency
   ```

**MCP-Enhanced Design (if available):**
5. **Context7 Refactoring Pattern Integration**

```
Use mcp__context7__resolve-library-id for "code-refactoring"
Use mcp__context7__get-library-docs for refactoring patterns
Use mcp__context7__get-library-docs for performance optimization techniques
Integrate latest refactoring methodologies into improvement plan
```

6. **Technology-Specific Enhancement**
   ```
   Apply framework-specific refactoring patterns for:
   - FastAPI endpoint optimization
   - SQLAlchemy query optimization
   - Pytest test structure improvements
   - AsyncIO performance enhancements
   ```

---

## ⚡ Implementation Phase

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Implementation Steps:**

1. **Validate prerequisites and safety measures**

   ```bash
   # Ensure all tests pass before refactoring
   if ! uv run --frozen pytest; then
       echo "❌ Tests must be GREEN before refactoring"
       exit 1
   fi
   
   # Create safety branch for rollback
   git checkout -b "refactor-issue-${ISSUE_NUMBER}-backup"
   git checkout -
   
   # Document current state
   git add -A
   git commit -m "checkpoint: pre-refactoring state for issue ${ISSUE_NUMBER}"
   ```

2. **Execute systematic refactoring**

   ```bash
   # Domain layer refactoring (highest priority)
   For each domain improvement:
   - Apply extract method refactoring
   - Remove duplication using template method pattern
   - Simplify complex conditionals
   - Run tests after each change
   
   # Application layer refactoring
   For each use case improvement:
   - Extract common validation logic
   - Improve error handling consistency
   - Optimize DTO mappings
   - Verify tests remain GREEN
   
   # Infrastructure layer refactoring
   For each infrastructure improvement:
   - Optimize database queries
   - Extract connection handling patterns
   - Add appropriate caching
   - Test performance improvements
   ```

**MCP-Enhanced Implementation (if available):**
3. **Intelligent Refactoring Execution**

```bash
# Enhanced refactoring with MCP analysis
For each Serena-identified improvement:
- Apply Context7 refactoring patterns automatically
- Use intelligent code transformation suggestions
- Validate improvements with automated quality metrics
- Document enhancement rationale and impact
```

4. **Automated Quality Verification**

   ```bash
   # Comprehensive quality validation
   After each refactoring step:
   - Run automated test verification
   - Check code quality metrics improvement
   - Validate performance benchmarks
   - Update documentation automatically
   ```

---

## 🎯 Output Generation

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create comprehensive refactoring documentation**

   ```bash
   Write "docs/refactoring/issue-${ISSUE_NUMBER}-refactoring-summary.md" with:
   # - List of all refactoring changes made
   # - Before/after code quality metrics
   # - Performance improvement measurements
   # - Test coverage impact analysis
   ```

2. **Generate quality improvement report**

   ```bash
   Write "docs/refactoring/issue-${ISSUE_NUMBER}-quality-report.md" with:
   # - Code smell elimination summary
   # - Complexity reduction metrics
   # - Maintainability improvements
   # - Technical debt reduction analysis
   ```

3. **Create MCP enhancement report (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced refactoring analysis
       Write "docs/refactoring/issue-${ISSUE_NUMBER}-mcp-analysis.md" with:
       # - Serena MCP code analysis results
       # - Context7 pattern application summary
       # - Intelligent improvement recommendations
       # - Future refactoring opportunities
       
       # Detailed MCP reports
       Write "docs/refactoring/issue-${ISSUE_NUMBER}-mcp-detailed-report.md" with:
       # - Complete Serena analysis findings
       # - Applied Context7 refactoring patterns
       # - Performance optimization results
       # - Architectural improvement analysis
   fi
   ```

4. **Update project quality metadata**

   ```bash
   # Update refactoring history and metrics
   for issue_num in $(echo $1 | tr ',' ' '); do
       # Update issue status with refactoring completion
       if [[ "$GITHUB_AVAILABLE" == "true" ]]; then
           gh issue comment "$issue_num" --body "✅ リファクタリング完了
           
   📊 品質改善メトリクス:
   - コード品質スコア向上
   - パフォーマンス最適化実施
   - テクニカルデブト削減
   - テストカバレッジ維持
           
   🔄 すべてのテストが正常に通過し、機能に変更はありません。"
       fi
   done
   
   # Commit all refactoring improvements
   git add docs/refactoring/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       git commit -m "refactor: improve code quality for issues $(echo $1 | tr ',' ' ') with MCP enhancement
       
   Apply systematic refactoring to improve maintainability and performance.
   Remove code duplication and simplify complex methods.
   Enhanced with MCP intelligent analysis and pattern application.
       
   🎯 Generated with Claude Code
       "
   else
       git commit -m "refactor: improve code quality for issues $(echo $1 | tr ',' ' ')
       
   Apply systematic refactoring to improve maintainability and performance.
   Remove code duplication and simplify complex methods.
       
   🎯 Generated with Claude Code
       "
   fi
   ```

---

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] All tests remain GREEN after refactoring
- [ ] Code quality metrics improved (linting, type checking)
- [ ] No functional behavior changes introduced
- [ ] Refactoring documentation completed
- [ ] Performance benchmarks validated
- [ ] Technical debt reduction measured

**Recommended Items (SHOULD):**

- [ ] Serena MCP code analysis utilized for intelligent improvements
- [ ] Context7 refactoring patterns applied effectively
- [ ] Automated quality verification completed
- [ ] Future refactoring opportunities identified

### Quality Metrics

| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Test Success Rate | 100% | [Actual Value] | ✅/❌ |
| Code Quality Improvement | +15% | [Actual Value] | ✅/❌ |
| Performance Enhancement | +15% | [Actual Value] | ✅/❌ |
| Technical Debt Reduction | 80% | [Actual Value] | ✅/❌ |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|------------|
| Code Smell Elimination | 95% | [Actual Value] | ✅/❌ |
| Pattern Compliance | 90% | [Actual Value] | ✅/❌ |
| Automated Improvement Coverage | 85% | [Actual Value] | ✅/❌ |

---

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **テスト安全性確認**: すべてのテストがGREEN状態を維持
- ✅ **コード品質向上**: リンティング・タイプチェック改善
- ✅ **パフォーマンス最適化**: ボトルネック特定・改善実施
- ✅ **リファクタリング完了**: docs/refactoring/issue-X-refactoring-summary.md 作成

**MCP拡張機能 (利用可能時):**

- ✅ **MCPコード解析**: [X]個のファイル、[Y]個の改善点分析完了
- ✅ **インテリジェント改善**: [Z]個のコード異臭除去、[W]個のパターン適用
- ✅ **自動品質検証**: Context7最新リファクタリングパターン適用完了
- ✅ **技術的負債削減**: [P]%の技術的負債解消、将来改善点特定

### 成果物

**基本ファイル (常に作成):**

- `docs/refactoring/issue-X-refactoring-summary.md`: リファクタリング概要
- `docs/refactoring/issue-X-quality-report.md`: 品質改善レポート
- Updated code files: 改善されたソースコード

**MCP拡張ファイル (利用可能時):**

- `docs/refactoring/issue-X-mcp-analysis.md`: MCP分析結果
- `docs/refactoring/issue-X-mcp-detailed-report.md`: 詳細MCP分析レポート
- Updated MCP memory files: リファクタリング知見の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP利用時)
**品質改善スコア**: [スコア]/100
**MCPインテリジェンス活用**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: 新機能開発や次のスプリント計画
2. **推奨**: 改善されたコードベースでの新機能実装
3. **確認推奨**: リファクタリング成果とパフォーマンス改善の確認

**ユーザーへのメッセージ (日本語)**:

```
🎉 インテリジェントリファクタリング完了！

🔧 基本リファクタリング:
   ✅ テスト安全性: 100%GREEN維持
   ✅ コード品質改善: [品質スコア向上]%
   ✅ パフォーマンス最適化: [性能向上]%
   ✅ 技術的負債削減: [削減率]%

🤖 MCP強化リファクタリング (利用時):
   🧠 Serenaコード解析: [X]ファイル分析
   📊 品質改善発見: [Y]改善点特定
   🎯 Context7パターン適用: 最新手法導入
   ✅ docs/refactoring/issue-X-mcp-analysis.md
   ✅ docs/refactoring/issue-X-mcp-detailed-report.md

📁 生成ファイル:
   ✅ docs/refactoring/issue-X-refactoring-summary.md
   ✅ docs/refactoring/issue-X-quality-report.md

🎯 次のアクション:
   新機能開発または次のスプリント計画

✅ リファクタリング完了 - 高品質なコードベース実現！
```