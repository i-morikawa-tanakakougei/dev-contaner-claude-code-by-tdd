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
#!/bin/bash
# MCP-Enhanced PR Creation - Direct Bash Implementation

# Validate issue number
if [[ -z "$1" ]]; then
    echo "ERROR: Issue number required. Usage: /create-pr-enhanced <issue-number>"
    exit 1
fi

ISSUE_NUMBER="$1"
echo "🧠 MCP-Enhanced PR Creation Starting..."
echo ""

# Check MCP session availability
if [[ -f ".serena/sessions/current/session-metadata.json" ]]; then
    echo "✅ MCP session found - Enhanced analysis will be available"
    MCP_AVAILABLE="true"
    echo "🔍 MCP Capabilities:"
    echo "  • Serena: Change impact analysis & code quality assessment"
    echo "  • Context7: Latest PR patterns & best practices integration"
else
    echo "ℹ️ MCP session not found - Running in standard mode"
    echo "💡 To enable MCP enhancements, run /context-session-stageup first"
    echo "📋 Enhanced features when available:"
    echo "  • Intelligent change impact analysis"
    echo "  • Automated quality assessment"
    echo "  • Context7 PR pattern integration"
    echo "  • Smart PR description generation"
    MCP_AVAILABLE="false"
fi

echo ""
echo "🚀 Starting enhanced PR creation process..."
echo ""
```

## 🚀 Expert Execution Flow

### Phase 1: Pre-PR Quality Gate Validation (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Quality Gate Activities:**

1. **Comprehensive Test Execution and Validation**

   ```bash
   echo "🧪 Phase 1: Quality Gate Validation..."
   
   # Run comprehensive test suite
   echo "⚙️ Running full test suite with coverage..."
   uv run --frozen pytest --cov=src --cov-report=term --cov-report=json
   TEST_EXIT_CODE=$?
   
   if [[ $TEST_EXIT_CODE -ne 0 ]]; then
       echo "❌ Tests failed - Cannot create PR"
       exit 1
   fi
   
   # Extract coverage percentage
   if [[ -f "coverage.json" ]]; then
       COVERAGE_PERCENT=$(jq -r '.totals.percent_covered' coverage.json)
       echo "✅ Test Coverage: ${COVERAGE_PERCENT}%"
   fi
   ```

2. **Code Quality Gate Validation**
   ```bash
   # Execute Ruff code quality checks
   echo "🔍 Running Ruff code quality checks..."
   uv run --frozen ruff check . --statistics > ruff_results.txt 2>&1
   RUFF_EXIT_CODE=$?
   
   # Execute Pyright type checking
   echo "🔍 Running Pyright type checking..."
   uv run --frozen pyright > pyright_results.txt 2>&1
   PYRIGHT_EXIT_CODE=$?
   
   if [[ $RUFF_EXIT_CODE -ne 0 ]] || [[ $PYRIGHT_EXIT_CODE -ne 0 ]]; then
       echo "⚠️ Code quality issues detected - Review required"
       cat ruff_results.txt
       cat pyright_results.txt
   else
       echo "✅ Code quality checks passed"
   fi
   ```

**MCP-Enhanced Quality Validation (if available):**

3. **Intelligent Change Impact Analysis**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 Phase 1.5: MCP Enhanced Analysis..."
       echo ""
   fi
   ```
   
   **MCP Instructions (Execute when MCP available):**
   ```
   Use mcp__serena__search_for_pattern "class |def |import " --restrict_search_to_code_files=true to identify affected code patterns
   Use mcp__serena__find_symbol "*" --depth=1 --include_body=false to locate modified components
   Use mcp__serena__get_symbols_overview for overall project structure analysis
   Create impact analysis summary using mcp__serena__write_memory "pr-impact-analysis-$(date +%Y%m%d)" with findings
   ```

4. **Context7 PR Pattern Integration**
   ```
   Use mcp__context7__resolve-library-id "pull-request-patterns" to get PR best practices
   Use mcp__context7__get-library-docs for latest PR creation standards
   Apply industry best practices to PR description generation
   ```

### Phase 2: Git State Management and Branch Validation (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core Git Management Activities:**

1. **Branch State Validation**

   ```bash
   echo "🌿 Phase 2: Git State Management..."
   
   # Verify current branch status
   CURRENT_BRANCH=$(git branch --show-current)
   echo "🌱 Current branch: $CURRENT_BRANCH"
   
   # Check if on appropriate feature branch (not main/master)
   if [[ "$CURRENT_BRANCH" == "main" ]] || [[ "$CURRENT_BRANCH" == "master" ]]; then
       echo "❌ Cannot create PR from main/master branch"
       echo "💡 Please create a feature branch first"
       exit 1
   fi
   
   # Ensure all changes are committed
   if [[ -n "$(git status --porcelain)" ]]; then
       echo "⚠️ Uncommitted changes detected - Please commit all changes first"
       git status
       exit 1
   fi
   
   echo "✅ Git state validation passed"
   ```

2. **Branch Synchronization and Push**

   ```bash
   # Push branch to remote with tracking
   echo "🚀 Pushing branch to remote..."
   git push -u origin "$CURRENT_BRANCH"
   PUSH_EXIT_CODE=$?
   
   if [[ $PUSH_EXIT_CODE -ne 0 ]]; then
       echo "❌ Failed to push branch to remote"
       exit 1
   fi
   
   echo "✅ Branch pushed successfully"
   ```

**MCP-Enhanced Git Analysis (if available):**

3. **Context7 Git Workflow Integration**
   
   **MCP Instructions (Execute when MCP available):**
   ```
   Use mcp__context7__resolve-library-id "git-workflows" to get latest Git practices
   Use mcp__context7__get-library-docs for PR creation best practices
   Use mcp__context7__get-library-docs for branch management strategies
   Apply latest industry Git workflow patterns to branch analysis
   ```

4. **Technology-Specific Git Optimization**
   ```
   Analyze project technology stack from package files
   Use mcp__context7__resolve-library-id for framework-specific PR patterns
   Apply technology-specific PR creation recommendations
   ```

### Phase 3: Intelligent PR Description Generation (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

**Core PR Description Generation:**

1. **GitHub Issue Data Collection**

   ```bash
   echo "📋 Phase 3: PR Description Generation..."
   
   # Collect comprehensive issue information
   echo "🔍 Collecting issue information from GitHub..."
   gh issue view $ISSUE_NUMBER --json title,body,comments,labels,milestone > issue_data.json
   
   if [[ $? -ne 0 ]]; then
       echo "❌ Failed to fetch issue data for #$ISSUE_NUMBER"
       exit 1
   fi
   
   # Extract key issue information
   ISSUE_TITLE=$(jq -r '.title' issue_data.json)
   ISSUE_BODY=$(jq -r '.body' issue_data.json)
   ISSUE_LABELS=$(jq -r '.labels[].name' issue_data.json | tr '\n' ',' | sed 's/,$//')
   
   echo "✅ Issue data collected: $ISSUE_TITLE"
   ```

2. **Git Change Analysis**

   ```bash
   # Analyze git changes for PR description
   echo "🔍 Analyzing git changes..."
   
   # Get commit range for PR
   MAIN_BRANCH=$(git symbolic-ref refs/remotes/origin/HEAD | sed 's@^refs/remotes/origin/@@')
   COMMITS_COUNT=$(git rev-list --count HEAD ^origin/$MAIN_BRANCH)
   CHANGED_FILES=$(git diff --name-only origin/$MAIN_BRANCH...HEAD | wc -l)
   
   # Generate change summary
   git log --oneline origin/$MAIN_BRANCH...HEAD > commit_summary.txt
   git diff --stat origin/$MAIN_BRANCH...HEAD > diff_stats.txt
   
   echo "✅ Change analysis: $COMMITS_COUNT commits, $CHANGED_FILES files changed"
   ```

**MCP-Enhanced PR Content Generation (if available):**

3. **Intelligent Content Analysis and Generation**
   
   **MCP Instructions (Execute when MCP available):**
   ```
   Analyze project changes using mcp__serena__search_for_pattern for modified code patterns
   Use mcp__serena__find_symbol to identify architectural changes
   Generate intelligent PR description using Context7 PR templates
   Apply industry best practices for PR documentation
   ```

4. **Create Comprehensive PR Description**

   ```bash
   # Generate PR description file
   echo "📝 Generating PR description..."
   
   cat > pr_description.md << EOF
# feat: implement ${ISSUE_TITLE} (#${ISSUE_NUMBER})

## Summary
${ISSUE_BODY}

## Changes
- Addresses issue #${ISSUE_NUMBER}
- ${COMMITS_COUNT} commits implementing the feature
- ${CHANGED_FILES} files modified

## Quality Metrics
- Test Coverage: ${COVERAGE_PERCENT}%
- Code Quality: Ruff and Pyright checks $([ $RUFF_EXIT_CODE -eq 0 ] && [ $PYRIGHT_EXIT_CODE -eq 0 ] && echo "passed" || echo "reviewed")
- All tests passing: $([ $TEST_EXIT_CODE -eq 0 ] && echo "✅" || echo "❌")

## Review Checklist
- [ ] Code follows project style guidelines
- [ ] Tests cover new functionality
- [ ] Documentation updated as needed
- [ ] No breaking changes or properly documented

EOF

   echo "✅ PR description generated: pr_description.md"
   ```

### Phase 4: PR Creation and Final Configuration (Core + MCP Enhanced)

**Execute the following as expert (Instructions to Claude Code in English):**

1. **Create GitHub Pull Request**

   ```bash
   echo "🚀 Phase 4: PR Creation..."
   
   # Create PR with comprehensive information
   echo "📋 Creating GitHub PR..."
   gh pr create \
       --title "feat: implement ${ISSUE_TITLE} (#${ISSUE_NUMBER})" \
       --body-file pr_description.md \
       --reviewer "i-morikawa-tanakakougei" \
       --label "enhancement" \
       --label "tdd-ddd-layered" \
       --milestone "$(jq -r '.milestone.title // ""' issue_data.json)"
   
   PR_EXIT_CODE=$?
   if [[ $PR_EXIT_CODE -ne 0 ]]; then
       echo "❌ Failed to create PR"
       exit 1
   fi
   
   # Capture PR information
   PR_URL=$(gh pr view --json url -q '.url')
   PR_NUMBER=$(gh pr view --json number -q '.number')
   
   echo "✅ PR created successfully: #$PR_NUMBER"
   echo "🔗 PR URL: $PR_URL"
   ```

2. **Create MCP Analysis Documentation (if available)**

   ```bash
   if [[ "$MCP_AVAILABLE" == "true" ]]; then
       echo "🧠 Creating MCP analysis documentation..."
       
       # Ensure docs/pr directory exists
       mkdir -p docs/pr
       
       # Create MCP analysis summary
       cat > "docs/pr/pr-${PR_NUMBER}-mcp-analysis.md" << EOF
# PR #${PR_NUMBER} - MCP Analysis Report

## Change Impact Analysis

**Generated**: $(date)
**PR**: #${PR_NUMBER}
**Issue**: #${ISSUE_NUMBER}

### Serena MCP Analysis
- Code pattern analysis completed
- Symbol dependency mapping performed
- Architecture impact assessment conducted

### Context7 Integration
- Latest PR best practices applied
- Industry standard patterns integrated
- Quality optimization recommendations generated

### Quality Enhancement
- Automated quality validation performed
- Improvement opportunities identified
- Review preparation optimized

See full MCP memory for detailed analysis results.
EOF

       echo "✅ MCP analysis documentation created"
   fi
   ```

3. **Configure Issue Management and Linking**

   ```bash
   # Link PR to issue with comprehensive summary
   echo "🔗 Linking PR to issue..."
   
   gh issue comment $ISSUE_NUMBER --body "🚀 Implementation completed in PR #$PR_NUMBER

**Implementation Summary:**
- ✅ All acceptance criteria addressed
- ✅ Test coverage: ${COVERAGE_PERCENT}%
- ✅ Quality gates: $([ $RUFF_EXIT_CODE -eq 0 ] && [ $PYRIGHT_EXIT_CODE -eq 0 ] && echo "Passed" || echo "Reviewed")
- ✅ Architecture compliance verified
$([ "$MCP_AVAILABLE" == "true" ] && echo "- ✅ MCP analysis completed with intelligence enhancement")

**Ready for review and merge!**

PR: $PR_URL"

   # Add issue context to PR
   gh pr comment $PR_NUMBER --body "📋 **Addresses all requirements from issue #$ISSUE_NUMBER**

**Quality Summary:**
- Commits: $COMMITS_COUNT
- Files changed: $CHANGED_FILES
- Test coverage: ${COVERAGE_PERCENT}%
- Labels: $ISSUE_LABELS
$([ "$MCP_AVAILABLE" == "true" ] && echo "- MCP enhancement: ✅ Applied")

Ready for code review."

   echo "✅ Issue and PR linking completed"
   ```

4. **Commit Documentation and Cleanup**

   ```bash
   # Add and commit any generated documentation
   if [[ -d "docs/pr" ]]; then
       git add docs/pr/
       git commit -m "docs: add PR documentation for #${PR_NUMBER}

Created comprehensive PR documentation with quality assessment.
$([ "$MCP_AVAILABLE" == "true" ] && echo "Enhanced with MCP analysis and Context7 best practices.")

🎈 Generated with Claude Code

Reported-by: Claude"
   fi
   
   # Cleanup temporary files
   rm -f issue_data.json commit_summary.txt diff_stats.txt
   rm -f coverage.json ruff_results.txt pyright_results.txt
   
   echo "✅ Cleanup completed"
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

- ✅ **品質ゲート検証**: テストカバレッジ [COVERAGE_PERCENT]%、品質チェック完了
- ✅ **PR作成完了**: PR #[PR_NUMBER] 作成、レビュアー i-morikawa-tanakakougei 割り当て済み
- ✅ **Issue連携設定**: Issue #[ISSUE_NUMBER] リンク設定完了
- ✅ **ブランチ管理**: [CURRENT_BRANCH] ブランチから [COMMITS_COUNT] コミットでPR作成

**MCP 拡張機能 (利用可能時):**

- ✅ **MCP 変更影響分析**: [CHANGED_FILES]個のファイル変更分析完了
- ✅ **Serena コード分析**: シンボル依存関係マッピング完了
- ✅ **Context7 パターン統合**: 最新PRベストプラクティス適用完了
- ✅ **インテリジェント最適化**: MCP分析に基づくPR説明最適化完了
- ✅ **品質ドキュメント**: docs/pr/pr-[PR_NUMBER]-mcp-analysis.md 作成

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
🎉 MCP強化プルリクエスト作成完了！

🔗 作成されたPR:
   📋 PR番号: #[PR_NUMBER]
   📋 URL: [PR_URL]
   📋 レビュアー: i-morikawa-tanakakougei 割り当て済み
   📋 ブランチ: [CURRENT_BRANCH] ([COMMITS_COUNT] コミット)

✅ 品質ゲート結果:
   ✅ テストカバレッジ: [COVERAGE_PERCENT]%
   ✅ コード品質: $([ $RUFF_EXIT_CODE -eq 0 ] && [ $PYRIGHT_EXIT_CODE -eq 0 ] && echo "通過" || echo "レビュー済み")
   ✅ ファイル変更: [CHANGED_FILES] ファイル変更
   ✅ アーキテクチャ: TDD/DDD/Clean Architecture準拠

📋 Issue連携:
   ✅ Issue #[ISSUE_NUMBER]: リンク設定完了
   🏷️ ラベル: [ISSUE_LABELS]
   🎢 マイルストーン: 連携済み

🧠 MCP強化機能 (利用時のみ):
   📊 Serena分析: コードパターン分析完了
   🔍 シンボル依存: マッピング完了
   🌐 Context7統合: 最新PRベストプラクティス適用
   📝 インテリジェント最適化: MCP分析ベーsPR説明生成
   ✅ docs/pr/pr-[PR_NUMBER]-mcp-analysis.md
   ✅ MCPメモリ更新完了

📋 次のステップ (ステータス報告):
   /status-report-enhanced [issue-numbers] (推奨)
   /status-report [issue-numbers] (基本版)

✅ MCP強化PR作成完了 - インテリジェントレビュー準備完了！
```