# 15-create-pr-enhanced (MCP-Enhanced Pull Request Creation)

## 🎯 Expert Profile Declaration

During command execution, you act as a **Pull Request Creation Specialist** with **MCP Enhancement** capabilities.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Your Expertise (Core + MCP Enhanced)

**Core PR Creation Expertise:**

- **PR Quality Assurance**: Creation of comprehensive, reviewable pull requests with clear descriptions and proper linking
- **Integration Validation**: Pre-merge validation including tests, builds, and quality gates
- **Issue Management**: Automatic issue closure and milestone management
- **Documentation Standards**: Ensuring PR descriptions follow team conventions and include all necessary context

**MCP-Enhanced Capabilities:**

- **Intelligent Code Analysis**: Automated change impact analysis using Serena MCP
- **Context-Aware PR Generation**: Context7-enhanced PR templates and best practices
- **Quality Pattern Recognition**: Advanced quality metric analysis and reporting
- **Automated PR Optimization**: Intelligent PR description and review preparation

### Execution Principles (Core + MCP Enhanced)

**Core Principles:**

1. **Quality Gates First**: All tests and quality checks must pass before PR creation
2. **Comprehensive Documentation**: PR descriptions should tell the complete story of changes
3. **Automated Linking**: Properly link and close related issues
4. **Reviewability**: Structure changes and descriptions for easy review

**MCP-Enhanced Principles:**
5. **Intelligent Analysis**: Leverage Serena for deep change impact analysis and optimization
6. **Context-Rich Generation**: Enhance PR descriptions with Context7 best practices
7. **Automated Quality Assurance**: Build automated quality validation with intelligent recommendations

### Quality Standards (Core + MCP Enhanced)

**Core Standards:**

- **Quality Gate Compliance**: All tests pass and code quality checks are satisfied
- **Issue Integration**: Proper linking and closure configuration for related issues
- **Documentation Completeness**: Clear, comprehensive PR descriptions with all necessary context
- **Review Readiness**: PRs structured for efficient and effective code review

**MCP-Enhanced Standards:**

- **Automated Impact Analysis**: 100% change impact analysis with Serena MCP
- **Pattern Compliance**: 95% adherence to PR best practices from Context7
- **Quality Enhancement**: 90%+ improvement in PR quality metrics
- **Intelligent Optimization**: Advanced PR optimization recommendations applied

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

**🧠 MCP Enhancement**: Serena (Code Analysis + Change Impact) + Context7 (PR Patterns + Best Practices)

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Pull Request Creation Phase (15/16) **[MCP-Enhanced Version]**  
> 🎯 **Phase Purpose**: Pull request creation with MCP intelligence and optimization  
> ⬅️ **Previous Stage**: 14-apply-feedback (Feedback Application) or 14-apply-feedback-enhanced  
> ➡️ **Next Stage**: 16-status-report (Status Reporting and Completion)

## 🎯 PHASE PURPOSE: PR CREATION WITH MCP ENHANCEMENT

**⚠️ Important Notice:**

- **This step focuses on COMPREHENSIVE PR CREATION** - Create PRs with intelligence and optimization
- **MCP ENHANCEMENT** - Leverage intelligent analysis and PR pattern guidance
- **QUALITY ASSURANCE FOCUS** - Ensure all quality gates pass with automated validation
- **INTELLIGENT OPTIMIZATION** - Complete change impact analysis and PR optimization

**What this step does:**

1. `14-apply-feedback` ← Previous: Feedback application and quality improvement
2. `15-create-pr-enhanced` ← **【YOU ARE HERE】PR creation with MCP intelligence**
3. `16-status-report` ← Next: Status reporting and completion
4. **Integration Ready** ← Final: Ready for merge and deployment

**Core Activities (Traditional):**

- Validate quality gates and run comprehensive tests
- Generate comprehensive PR descriptions with proper linking
- Create PRs with appropriate reviewers and labels
- Configure automatic issue closure and milestone management

**MCP-Enhanced Activities (Additional):**

- Analyze change impact and code quality using Serena MCP
- Generate intelligent PR descriptions with Context7 best practices
- Create automated quality validation with optimization recommendations
- Provide intelligent PR review preparation and merge readiness assessment

**CREATE HIGH-QUALITY PRS WITH INTELLIGENCE.**

## 📋 MCP-Enhanced PR Analysis

### Required Setup

```bash
# Validate issue number and MCP session
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-pr-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🧠 Executing MCP-enhanced PR creation with intelligent analysis..."

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
SCRIPT_PATH=".claude/commands/tdd-ddd-layered-expert/utils/15-create-pr-enhanced.py"

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
    echo "✅ PR creation completed successfully"
else
    echo "❌ PR creation failed with exit code: $EXIT_CODE"
    exit $EXIT_CODE
fi
```

## 🚀 Expert Execution Flow

### Phase 1: Pre-PR Quality Gate Validation (Core + MCP Enhanced)

**Analyze the following as expert (User interactions in Japanese):**

**Core Quality Gate Activities:**

1. **Comprehensive Test Execution**

   - Run full test suite using Bash tool with `uv run --frozen pytest`
   - Capture test coverage metrics and results
   - Validate all tests pass before proceeding
   - Generate test report for PR documentation

2. **Code Quality Validation**
   - Execute Ruff checks using Bash tool with `uv run --frozen ruff check .`
   - Run Pyright type checking using Bash tool with `uv run --frozen pyright`
   - Validate security with Bandit scanning
   - Ensure all quality gates pass

**MCP-Enhanced Quality Validation (if available):**
3. **Automated Change Impact Analysis**

   - Use mcp__serena__search_for_pattern to identify affected code patterns
   - Use mcp__serena__find_symbol to locate modified components
   - Use mcp__serena__find_referencing_symbols to analyze change dependencies
   - Create memory using mcp__serena__write_memory for impact analysis

4. **Intelligent Quality Assessment**
   - Use mcp__serena__get_symbols_overview to assess overall code health
   - Identify potential regression risks from changes
   - Extract quality improvement opportunities from analysis
   - Document findings in quality assessment memory

### Phase 2: Git State Management and Optimization (Core + MCP Enhanced)

**Design the following as expert (Instructions to Claude Code in English):**

**Core Git Management Activities:**

1. **Branch State Validation**

   ```
   Verify current branch status:
   - Check if on appropriate feature branch
   - Validate branch is up-to-date with main
   - Ensure all changes are committed
   - Push branch to remote with proper tracking
   ```

2. **Commit Optimization**

   ```
   Optimize commit structure:
   - Generate meaningful commit messages linked to issues
   - Ensure proper commit message format
   - Add Co-Authored-By information as required
   - Configure automatic issue closure via commit message
   ```

**MCP-Enhanced Git Management (if available):**
3. **Context7 Git Workflow Integration**

```
Use mcp__context7__resolve-library-id for "git-workflows"
Use mcp__context7__get-library-docs for PR best practices
Use mcp__context7__get-library-docs for merge strategies
Integrate latest Git workflow patterns into process
```

4. **Technology-Specific PR Optimization**
   ```
   Identify project tech stack from codebase analysis
   Use mcp__context7__resolve-library-id for framework-specific PR patterns
   Use mcp__context7__get-library-docs for deployment considerations
   Apply technology-specific PR optimization recommendations
   ```

### Phase 3: Intelligent PR Description Generation (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core PR Description Generation:**

1. **Validate prerequisites and collect information**

   ```bash
   # Validate issue number and collect GitHub information
   if [[ $# -eq 0 ]]; then
       echo "Error: At least one issue number must be specified"
       echo "Usage example: /create-pr-enhanced 1"
       exit 1
   fi

   # Collect issue information
   echo "Collecting issue information for comprehensive PR description..."
   gh issue view $ISSUE_NUMBER --json title,body,comments,labels,milestone > issue_data.json
   
   # Capture current quality metrics
   echo "Capturing quality metrics for PR documentation..."
   uv run --frozen pytest --cov=src --cov-report=term > test_results.txt
   uv run --frozen ruff check . --statistics > ruff_results.txt
   ```

2. **Generate comprehensive PR description**

   ```bash
   # Create intelligent PR description based on issue and changes
   Create PR description document including:
   # - Summary of changes with business context
   # - Issue linking with acceptance criteria validation
   # - Architecture layer impact analysis
   # - Test coverage and quality metrics
   # - Security and performance considerations
   # - Review checklist and deployment notes
   # - Migration considerations if applicable
   ```

**MCP-Enhanced PR Description (if available):**
3. **Intelligent PR Content Generation**

```bash
# Enhanced PR description with MCP analysis
For each identified change from Serena analysis:
- Extract architectural impact from code analysis
- Generate intelligent change summaries
- Apply Context7 PR description best practices
- Create optimization recommendations section
```

4. **Automated Quality Documentation**

   ```bash
   # Intelligent quality documentation
   Use Serena MCP to analyze code quality improvements
   Apply Context7 patterns for quality metric presentation
   Generate automated testing strategy documentation
   Create performance impact assessment
   ```

### Phase 4: PR Creation and Configuration (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create standard PR documentation (always)**

   ```bash
   # Standard PR creation (always executed)
   gh pr create \
       --title "feat: implement ${ISSUE_TITLE} (#${ISSUE_NUMBER})" \
       --body-file pr_description.md \
       --reviewer "i-morikawa-tanakakougei" \
       --label "enhancement" \
       --label "tdd-ddd-layered"
   
   # Capture PR information
   PR_URL=$(gh pr view --json url -q '.url')
   PR_NUMBER=$(gh pr view --json number -q '.number')
   ```

2. **Create MCP analysis documents (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       # MCP-enhanced PR analysis document
       Write "docs/pr/pr-${PR_NUMBER}-mcp-analysis.md" with:
       # - MCP-discovered change impact analysis
       # - Automated quality assessment results
       # - Code health improvement tracking
       # - Context7-enhanced PR optimization recommendations
       # - Intelligent review preparation guidance

       # MCP detailed reports
       Write "docs/pr/pr-${PR_NUMBER}-quality-assessment.md" with:
       # - Serena MCP code analysis summary
       # - Discovered improvement opportunities and applications
       # - Quality metrics before/after comparison
       # - Risk assessment and mitigation recommendations
       # - Context7 pattern integration outcomes

       # Update MCP memory with findings
       Use mcp__serena__write_memory to store:
       # - PR creation analysis results
       # - Quality assessment outcomes
       # - Change impact documentation
       # - Review preparation recommendations
   fi
   ```

3. **Configure issue management and automation**

   ```bash
   # Link PR to issues and configure automation
   if [[ -n "$ISSUE_NUMBER" ]] && [[ -n "$PR_NUMBER" ]]; then
       # Add comprehensive PR reference to issue
       gh issue comment $ISSUE_NUMBER --body "🚀 Implementation completed in PR #$PR_NUMBER

   Implementation summary:
   - ✅ All acceptance criteria addressed with MCP analysis
   - ✅ Full test coverage achieved (${COVERAGE_PERCENTAGE}%)
   - ✅ Architecture compliance verified with intelligent analysis
   - ✅ Code quality gates passed with optimization applied

   Ready for review and merge with enhanced quality assurance."

       # Add issue context to PR
       gh pr comment $PR_NUMBER --body "📋 Addresses all requirements from issue #$ISSUE_NUMBER with MCP enhancement"
   fi
   ```

4. **Git commit PR documentation**
   ```bash
   Bash git add docs/pr/
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       Bash git commit -m "docs: add PR documentation with MCP enhancement for #${PR_NUMBER}

   Created comprehensive PR documentation with intelligent analysis.
   Includes change impact assessment and quality optimization reports.
   Enhanced with MCP analysis and Context7 best practices.

   🎯 Generated with Claude Code
       "
   else
       Bash git commit -m "docs: add PR documentation for #${PR_NUMBER}

   Created comprehensive PR documentation with quality assessment.
   Includes change impact analysis and review preparation.

   🎯 Generated with Claude Code
       "
   fi
   ```

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] Serena MCP change impact analysis completed
- [ ] Context7 PR pattern integration applied
- [ ] Enhanced PR creation with intelligence
- [ ] Quality metrics automatically tracked and documented
- [ ] Change impact analysis completed
- [ ] Review preparation guidance updated

**Recommended Items (SHOULD):**

- [ ] Performance impact assessed and documented
- [ ] Security implications analyzed and addressed
- [ ] Architecture compliance verified with automation
- [ ] Documentation completeness validated

### Quality Metrics

| Metric                              | Target | Actual         | Assessment |
| ----------------------------------- | ------ | -------------- | ---------- |
| Quality Gate Pass Rate             | 100%   | [Actual Value] | ✅/❌      |
| PR Description Completeness        | 95%    | [Actual Value] | ✅/❌      |
| Issue Integration Quality           | 100%   | [Actual Value] | ✅/❌      |
| Review Readiness Score              | 90%    | [Actual Value] | ✅/❌      |

**MCP-Enhanced Metrics (if MCP Available):**
| Metric | Target | Actual | Assessment |
|--------|--------|--------|-----------|
| Change Impact Coverage | 95% | [Actual Value] | ✅/❌ |
| Automated Quality Analysis | 90% | [Actual Value] | ✅/❌ |
| Context7 Integration | 85% | [Actual Value] | ✅/❌ |
| Intelligence Enhancement | 100% | [Actual Value] | ✅/❌ |

## 📊 Standardized Output Format

### 実行サマリー (日本語でユーザーに報告)

**基本機能 (常に実行):**

- ✅ **品質ゲート検証**: テスト X 件通過、コード品質チェック完了
- ✅ **PR作成完了**: PR #[NUMBER] 作成、レビュアー割り当て済み
- ✅ **Issue連携設定**: Issue #[NUMBER] 自動クローズ設定完了
- ✅ **ドキュメント生成**: PR説明書および品質レポート作成

**MCP 拡張機能 (利用可能時):**

- ✅ **MCP 変更影響分析**: [X]個のファイル、[Y]個のコンポーネント分析完了
- ✅ **自動品質評価**: [A]個の品質指標、[B]個の改善提案を生成
- ✅ **変更リスク評価**: [C]個のリスク要因分析完了
- ✅ **Context7 パターン統合**: 最新PR作成パターン適用完了
- ✅ **レビュー準備最適化**: MCP 分析に基づくレビュー準備完了

### 成果物

**基本ファイル (常に作成):**

- `GitHub PR #[NUMBER]`: 包括的なPR説明とレビュー準備
- `Issue #[NUMBER]`: 自動クローズ設定とPR連携
- Quality metrics documentation and test reports

**MCP 拡張ファイル (利用可能時):**

- `docs/pr/pr-[NUMBER]-mcp-analysis.md`: MCP 変更影響分析
- `docs/pr/pr-[NUMBER]-quality-assessment.md`: 品質評価詳細レポート
- Updated MCP memory files: PR作成分析結果の永続化

### 総合判定

**ステータス**: `SUCCESS` (基本) / `MCP_ENHANCED_SUCCESS` (MCP 利用時)
**PR品質スコア**: [スコア]/100
**MCP インテリジェンス品質**: [スコア]/100 (利用時のみ)
**次フェーズ準備**: `READY`

### 次のステップ (日本語でユーザーに案内)

1. **即座に実行可能**: `/status-report [issue-numbers]` または `/status-report-enhanced [issue-numbers]`
2. **推奨**: ステータス報告フェーズに進む
3. **確認推奨**: PR作成結果のレビュー

**ユーザーへのメッセージ (日本語)**:

```
🎉 プルリクエスト作成完了！

🔗 作成されたPR:
   📋 PR番号: #[NUMBER]
   📋 URL: [PR_URL]
   📋 レビュアー: i-morikawa-tanakakougei 割り当て済み

✅ 品質ゲート結果:
   ✅ テスト: [X]件通過 (カバレッジ: [XX]%)
   ✅ コード品質: Ruff/Pyright チェック通過
   ✅ セキュリティ: 新規脆弱性なし
   ✅ アーキテクチャ: Clean Architecture準拠確認

📋 Issue連携:
   ✅ Issue #[NUMBER]: 自動クローズ設定完了
   ✅ マイルストーン: [MILESTONE] 連携済み

🧠 MCP強化機能 (利用時のみ):
   📊 Serena分析: [X]ファイル、[Y]コンポーネント分析
   🔍 変更影響評価: [A]個のリスク要因評価完了
   📋 品質最適化: [C]個の改善提案適用
   🌐 Context7統合: 最新PR作成パターン適用
   ✅ docs/pr/pr-[NUMBER]-mcp-analysis.md
   ✅ docs/pr/pr-[NUMBER]-quality-assessment.md
   ✅ MCP メモリファイル更新

📋 次のステップ (ステータス報告):
   /status-report [issue-numbers] または /status-report-enhanced [issue-numbers]

✅ PR作成完了 - レビューおよびマージ準備完了！
```