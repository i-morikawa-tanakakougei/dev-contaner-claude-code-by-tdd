Show use case development status and progress with comprehensive analytics and intelligent recommendations.

## Metadata
- **Prerequisites**: Use case development in progress or completed
- **Input**: Issue number(s) (optional - shows all if not specified)
- **Output**: 
  - Comprehensive status report
  - Progress analytics and metrics
  - Development recommendations
- **Dependencies**: Metadata files, Git history, implementation files
- **Execution Timing**: Any time during development for progress monitoring

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Progress Tracking - Development Status Check (16/16)  
> 🎯 **Phase Purpose**: Visualize development progress and suggest next actions  
> 🔄 **Execution Timing**: Can be run from any phase  
> 📊 **Features**: Metadata analysis, visual progress display, next step guidance
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Read project overview)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Display implementation status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Analyze detailed progress)

## 📊 **STATUS REPORTING: ANALYSIS ONLY**

**⚠️ Important Notice:**
- **This step is STATUS REPORTING ONLY** - Display progress and analyze current state
- **NO IMPLEMENTATION** - Focus on reading and reporting status  
- **Progress visualization** - Show development progress across all phases
- **Next action recommendations** - Suggest optimal next steps

**Status Check Functions:**
- ✅ Read and analyze metadata files
- ✅ Display visual progress indicators
- ✅ Show completion percentages
- ✅ Recommend next actions
- ✅ Identify bottlenecks and issues
- ❌ Do not make any implementation changes
- ❌ Do not modify any files

## 📋 **PROJECT STATUS ANALYSIS TASK CHECKLIST**

**Use this checklist for comprehensive project status visualization and analysis:**

### 🔴 Required Tasks

#### **📊 Metadata Discovery and Analysis**
- [ ] **Scan project structure**: Discover all issue-X-Y.json metadata files in docs/use_cases/
- [ ] **Parse metadata files**: Extract progress information from each metadata file
- [ ] **Validate metadata integrity**: Check for corrupted or incomplete metadata files
- [ ] **Aggregate project data**: Combine data from all issues and features

#### **🎯 Feature and Issue Progress Analysis**
- [ ] **Calculate completion percentages**: Determine completion rate for each feature/issue
- [ ] **Analyze phase distribution**: Show how many issues are in each development phase
- [ ] **Identify blocked items**: Find issues that are stuck or haven't progressed
- [ ] **Track velocity metrics**: Calculate development velocity and trend analysis

#### **📈 Progress Visualization Creation**
- [ ] **Create progress dashboard**: Generate visual representation of overall project progress
- [ ] **Build feature status matrix**: Show status of each feature across all development phases

### 🟡 Recommended Tasks

#### **🏗️ Architecture and Quality Metrics**
- [ ] **Analyze layer implementation**: Show completion status for domain/application/infrastructure/presentation layers
- [ ] **Check architecture compliance**: Verify adherence to TDD/DDD/Clean Architecture principles
- [ ] **Review test coverage**: Aggregate test coverage across all implemented features
- [ ] **Assess code quality**: Show quality metrics and trends across the project
- [ ] **Validate Given-When-Then coverage**: Check scenario implementation completeness
- [ ] **Review documentation coverage**: Assess documentation completeness and quality

### 🟢 Optional Tasks

#### **🔍 Advanced Analysis**
- [ ] **Identify data inconsistencies**: Flag any metadata that appears incorrect or outdated
- [ ] **Map issue relationships**: Understand dependencies and relationships between issues
- [ ] **Assess scope changes**: Identify features with evolved or changed requirements
- [ ] **Map implementation coverage**: Show which parts of the system have been implemented
- [ ] **Generate completion timeline**: Display projected completion dates based on current velocity
- [ ] **Create quality metrics charts**: Visualize test coverage, code quality, and performance trends
- [ ] **Show bottleneck analysis**: Identify phases or features that are causing delays
- [ ] **Display sprint progress**: Show current sprint status and upcoming work

### **🚀 Next Action Recommendations**
- [ ] **Identify immediate priorities**: Recommend the most important next steps
- [ ] **Suggest optimal command sequence**: Provide specific commands to run for next actions
- [ ] **Flag urgent issues**: Highlight issues that need immediate attention
- [ ] **Recommend resource allocation**: Suggest where to focus development effort
- [ ] **Identify quick wins**: Point out features that can be completed quickly
- [ ] **Suggest refactoring opportunities**: Recommend areas that would benefit from improvement

### **🎯 Stakeholder Communication Preparation**
- [ ] **Create executive summary**: Generate high-level progress summary for stakeholders
- [ ] **Prepare business value report**: Show delivered business value and upcoming deliverables
- [ ] **Generate risk assessment**: Identify and communicate project risks and mitigation strategies
- [ ] **Create timeline projections**: Provide realistic completion estimates for remaining work
- [ ] **Prepare feature demos**: Identify completed features ready for demonstration
- [ ] **Document milestone achievements**: Highlight major milestones reached and upcoming

### **🔍 Quality and Health Assessment**
- [ ] **Assess project health**: Evaluate overall project health and sustainability
- [ ] **Check technical debt**: Identify areas of technical debt that need attention
- [ ] **Review team velocity**: Analyze team productivity and capacity
- [ ] **Evaluate process effectiveness**: Assess how well the TDD/DDD process is working
- [ ] **Check documentation health**: Ensure documentation is up-to-date and comprehensive
- [ ] **Assess maintainability**: Evaluate long-term maintainability of the codebase

### **🔄 Process and Workflow Analysis**
- [ ] **Analyze command usage patterns**: Show which commands are used most frequently
- [ ] **Identify process bottlenecks**: Find steps in the workflow that cause delays
- [ ] **Review feedback cycles**: Assess effectiveness of review and feedback processes
- [ ] **Check scenario evolution patterns**: Analyze how requirements evolve during development
- [ ] **Evaluate testing effectiveness**: Assess test quality and coverage trends
- [ ] **Review integration patterns**: Analyze cross-feature integration challenges

### **📊 Performance and Scalability Insights**
- [ ] **Analyze system performance**: Review performance metrics across implemented features
- [ ] **Check scalability readiness**: Assess system's readiness for scaling
- [ ] **Review resource utilization**: Analyze system resource usage patterns
- [ ] **Identify optimization opportunities**: Find areas where performance can be improved
- [ ] **Check integration performance**: Assess performance of cross-system integrations
- [ ] **Validate load handling**: Review system behavior under various load conditions

### **🎨 Customizable Reporting Options**
- [ ] **Generate detailed reports**: Create comprehensive reports for different audiences
- [ ] **Create summary dashboards**: Generate high-level overview dashboards
- [ ] **Provide drill-down capability**: Allow detailed exploration of specific areas
- [ ] **Export progress data**: Enable data export for external reporting tools
- [ ] **Create historical comparisons**: Show progress trends over time
- [ ] **Generate actionable insights**: Provide specific, actionable recommendations

### **🔮 Predictive Analysis and Planning**
- [ ] **Project completion forecasting**: Predict project completion based on current trends
- [ ] **Resource planning recommendations**: Suggest resource allocation for optimal progress
- [ ] **Risk mitigation planning**: Identify potential risks and suggest mitigation strategies
- [ ] **Capacity planning analysis**: Assess team capacity and workload distribution
- [ ] **Dependency impact analysis**: Show how delays in one area affect other areas
- [ ] **Quality trend prediction**: Forecast quality metrics based on current trends

### **📚 Status Documentation and Communication**
- [ ] **Generate status report**: Create comprehensive status document
- [ ] **Prepare team communications**: Draft status updates for development team
- [ ] **Create stakeholder briefings**: Prepare executive-level status presentations
- [ ] **Document recommendations**: Record all recommendations and their rationale
- [ ] **Archive status snapshots**: Store status information for historical tracking
- [ ] **Prepare follow-up actions**: Document specific next steps and responsibilities

**💡 Pro Tip: Use this status analysis regularly to maintain project visibility and make data-driven decisions about priorities and resource allocation!

**Multi-Phase Usage:**
- Can be run from any development phase
- Provides real-time progress visibility
- Helps track TDD/DDD cycle completion
- Supports project management decisions

**REPORT STATUS ONLY - NO MODIFICATIONS.**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **進捗可視化の不備**: 多層的・時系列進捗分析とリアルタイム更新
- **次アクション不明確**: AI ベース推奨とコンテキスト依存提案
- **品質状況不透明**: 包括的品質メトリクスとトレンド分析
- **チーム連携不足**: GitHub 連携とステークホルダー向け報告
- **問題早期発見の欠如**: 予測的問題検出とアラート機能

### **🆕 新機能**

1. **🧠 インテリジェント分析**: AI ベースの進捗パターン分析と予測
2. **📊 多次元可視化**: 時系列・品質・リスク・効率性の統合ダッシュボード
3. **🔍 予測アラート**: 潜在的ブロッカーと期限遅延の早期警告
4. **🤝 チーム連携強化**: ステークホルダー別カスタマイズ報告
5. **📈 パフォーマンス最適化**: 開発効率とボトルネック分析

## Common Errors and Solutions

### ❌ Error Case 1: No use cases found
**Cause**: Status check attempted before any use case creation  
**Solution**: Create use cases first with `/create-use-case <issue-number>`

### ❌ Error Case 2: Metadata files corrupted
**Cause**: JSON metadata files have invalid format  
**Solution**: Validate and fix JSON files or regenerate with use case commands

### ❌ Error Case 3: Git history incomplete
**Cause**: Status analysis requires Git history for accurate reporting  
**Solution**: Ensure Git repository is properly initialized and commits exist

## Execution Examples

### ✅ Success Example
```bash
$ /use-case-status 15
📊 Issues: #15 のステータス分析を開始します
📊 メタデータ分析中...
✅ ユースケース仕様: 完了
✅ ドメインモデル: 完了
✅ TDDテスト: 完了
✅ 全層実装: 完了
✅ リファクタリング: 完了
📊 進捗率: 95% (PR作成準備完了)
🎉 ステータス分析完了!
```

### ❌ Failure Example and Fix
```bash
$ /use-case-status 999
❌ Issue #999 のメタデータが見つかりません
💡 有効なイシュー番号を指定してください

# Fix: Use valid issue number or no arguments for all
$ /use-case-status
```

## Command Implementation

### 1. Pre-execution Validation

```bash
# Load shared environment and validate arguments
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "16-use-case-status" "$ARGUMENTS"

# Validate issue numbers provided
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "❌ エラー: イシュー番号が必要です"
    show_usage_example "use-case-status" "1,15" "イシュー1と15の状況確認"
    exit 1
fi

# Check for metadata files existence
echo "🔍 メタデータファイルの存在確認中..."
for issue_num in "${issue_numbers[@]}"; do
    if ! find docs/use_cases -name "issue-*${issue_num}*.json" -type f | grep -q .; then
        echo "❌ Issue #${issue_num} のメタデータファイルが見つかりません"
        echo "💡 まず /create-use-case ${issue_num} を実行してください"
        exit 1
    fi
done

echo "✅ 前提条件の確認が完了しました"
```

### 2. Execute Specialized Agent

```bash
# Execute the 16-use-case-status agent with comprehensive analysis
echo "🤖 ステータス分析エージェントを実行中..."
echo "📊 Issues: #$(IFS=','; echo "${issue_numbers[*]}") の包括的ステータス分析を開始します"

use_task_tool "
Please perform comprehensive use case development status analysis for issues: $(IFS=','; echo "${issue_numbers[*]}")

Execute the following analysis:

**Core Analysis Tasks:**
1. **Metadata Discovery**: Scan and parse all related metadata files in docs/use_cases/
2. **Progress Calculation**: Calculate completion percentages and phase distribution
3. **File Inventory**: Discover implementation files across all layers (domain/application/infrastructure/presentation)
4. **Quality Assessment**: Evaluate test coverage, code quality metrics (Ruff/Pyright), and architecture compliance
5. **GitHub Integration**: Sync with GitHub issues for current state and activity analysis
6. **Timeline Analysis**: Calculate development velocity and project timeline

**Reporting Requirements:**
1. **Progress Dashboard**: Visual progress indicators with completion percentages
2. **Phase Status Matrix**: Detailed status for each development phase (use_case_creation, domain_modeling, test_creation, etc.)
3. **Quality Metrics**: Test coverage, linting errors, type checking results
4. **File Inventory**: Complete listing of documents, implementation files, and tests
5. **GitHub Status**: Issue states, assignees, comments, and activity
6. **Next Action Recommendations**: Intelligent suggestions for immediate next steps
7. **Risk Assessment**: Identify potential blockers and stale issues

**Output Format:**
- Beautiful console progress display with visual progress bars
- Comprehensive markdown status report
- Actionable next steps with specific command recommendations
- Quality metrics dashboard
- Timeline and velocity analysis

**Key Principles:**
- READ-ONLY analysis (no file modifications)
- Multi-dimensional analysis (metadata + files + GitHub + quality)
- Intelligent recommendations based on current phase
- Stakeholder-ready reporting
- Predictive insights and trend analysis

This is a status reporting command - focus on comprehensive analysis and beautiful visualization of current project state.
" "16-use-case-status"

if [[ $? -ne 0 ]]; then
    echo "❌ ステータス分析エージェントの実行に失敗しました"
    exit 1
fi
```

### 3. Agent Result Verification

```bash
# Verify comprehensive status analysis completion
echo "🔍 ステータス分析結果を検証中..."

# Check if analysis generated expected outputs
verification_passed=true

# Verify progress analysis was completed
if ! echo "$TASK_RESULT" | grep -q "進捗"; then
    echo "⚠️ 警告: 進捗分析が不完全な可能性があります"
    verification_passed=false
fi

# Verify quality metrics were assessed
if ! echo "$TASK_RESULT" | grep -q "品質"; then
    echo "⚠️ 警告: 品質メトリクス分析が不完全な可能性があります"
    verification_passed=false
fi

# Verify next actions were provided
if ! echo "$TASK_RESULT" | grep -q "次の"; then
    echo "⚠️ 警告: 次のアクション推奨が不完全な可能性があります"
    verification_passed=false
fi

if [[ "$verification_passed" == "true" ]]; then
    echo "✅ ステータス分析の検証が完了しました"
else
    echo "⚠️ 一部の分析が不完全ですが、利用可能な結果を表示します"
fi
```

### 4. Display Success Summary

```bash
# Display beautiful success summary
echo ""
echo "🎉 ユースケース開発ステータス分析完了"
echo "========================================"
echo ""
echo "📊 **分析対象**: Issues #$(IFS=', #'; echo "${issue_numbers[*]}")"
echo "📈 **実行内容**: 包括的ステータス分析とレポート生成"
echo "🔍 **分析領域**: メタデータ、ファイル、品質、GitHub連携"
echo "🎯 **成果物**: 進捗ダッシュボード、詳細レポート、推奨アクション"
echo ""
echo "✅ **ステータス分析が正常に完了しました**"
echo ""
echo "📋 詳細な分析結果は上記のレポートをご確認ください"
echo "🔄 定期的な進捗確認により、プロジェクトの可視性を維持してください"
echo ""
echo "💡 次回実行: /use-case-status $(IFS=','; echo "${issue_numbers[*]}") で最新状況を確認"
```

## Important Implementation Notes

### **Comprehensive Status Analysis**

This command provides comprehensive, read-only analysis of use case development status with intelligent insights and actionable recommendations.

**Key Capabilities:**
- Multi-dimensional analysis (metadata + files + GitHub + quality)
- Real-time progress calculation and visualization
- Intelligent next action recommendations
- Stakeholder-ready reporting and documentation

**Read-Only Operations:**
- No file modifications or implementation changes
- Safe execution with timeout controls
- Beautiful console display and detailed reports
- Specific command suggestions for next actions

## 📍 **AGENT INTEGRATION IMPLEMENTATION**

This command follows the established 4-step agent integration pattern for consistent execution:

### **Step 1: Pre-execution Validation** 🔍

```bash
# Load shared environment and validate arguments
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "16-use-case-status" "$ARGUMENTS"

# Validate issue numbers provided
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "❌ エラー: イシュー番号が必要です"
    show_usage_example "use-case-status" "1,15" "イシュー1と15の状況確認"
    show_usage_example "use-case-status" "7" "イシュー7の状況確認"
    show_usage_example "use-case-status" "1,feature-name" "イシュー1の特定フィーチャー確認"
    exit 1
fi

# Validate project structure
if [[ ! -d "docs/use_cases" ]]; then
    echo "❌ エラー: プロジェクト構造が見つかりません"
    echo "💡 ヒント: /init-project-structure を実行してください"
    exit 1
fi

echo "🔍 プロジェクト状況分析を開始します..."
echo "📋 対象イシュー: $(IFS=', #'; echo "#${issue_numbers[*]}")"
```

### **Step 2: Execute Specialized Agent** 🤖

```bash
# Execute the 16-use-case-status agent with comprehensive analysis
use_task_tool "
Please perform comprehensive use case development status analysis for issues: $(IFS=','; echo "${issue_numbers[*]}")

## Agent Tasks:
1. **Project Metadata Discovery**:
   - Locate metadata files for specified issues
   - Extract feature information and current phase
   - Validate project structure and documentation
   - Build comprehensive project inventory

2. **Multi-Dimensional Status Analysis**:
   - Analyze development phase completion across all layers
   - Calculate progress percentages and completion metrics
   - Review file inventory and artifact status
   - Assess quality metrics (test coverage, Ruff, Pyright)
   - Analyze GitHub issue status and synchronization
   - Generate timeline analysis and phase transitions

3. **Progress Analytics and Visualization**:
   - Calculate completion percentages with intelligent weighting
   - Generate progress bars and visual indicators
   - Identify bottlenecks and blocked phases
   - Provide phase-by-phase completion status
   - Map dependencies and critical path analysis

4. **Quality Assessment**:
   - Comprehensive test coverage analysis
   - Code quality metrics (complexity, duplication)
   - Architecture compliance validation
   - Given-When-Then scenario coverage
   - Security and performance considerations

5. **Intelligent Recommendations**:
   - Suggest next optimal actions based on current state
   - Identify blocking issues and dependencies
   - Recommend priority optimizations
   - Provide timeline estimates for completion
   - Flag risks and potential issues

6. **Stakeholder Reporting**:
   - Generate detailed status reports for different audiences
   - Create executive summaries and technical details
   - Provide actionable insights and decisions points
   - Generate progress dashboards and metrics

## Success Criteria:
- Complete project metadata discovery and inventory
- Accurate progress calculation across all dimensions
- Quality metrics analyzed and reported
- Clear next action recommendations provided
- Comprehensive status report generated
- All analysis completed safely (read-only operations)

## TDD/DDD/Layered Architecture Focus:
- Validate architectural layer separation and compliance
- Assess domain model richness and business logic placement
- Review test pyramid and Given-When-Then coverage
- Analyze cross-layer integration and boundaries
- Verify clean architecture dependency directions
" "16-use-case-status"
```

### **Step 3: Agent Result Verification** ✅

```bash
# Verify agent execution results
echo "🔍 Verifying 16-use-case-status agent results..."

# Check if status analysis was completed
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
status_patterns=(
    "docs/status/issue-${issue_list}-*.json"
    "docs/analysis/status-${issue_list}-*.json"
    "docs/reports/*status*${issue_list}*.json"
)

status_file=""
for pattern in "${status_patterns[@]}"; do
    if ls $pattern 2>/dev/null >/dev/null; then
        status_file=$(ls $pattern 2>/dev/null | head -1)
        break
    fi
done

if [[ -z "$status_file" ]]; then
    echo "❌ Status analysis file not found"
    exit 1
fi

# Validate analysis completeness
if [[ -f "$status_file" ]] && command -v jq >/dev/null 2>&1; then
    analysis_complete=$(jq -r '.analysis_complete // false' "$status_file" 2>/dev/null)
    progress_calculated=$(jq -r '.progress.calculated // false' "$status_file" 2>/dev/null)
    recommendations_count=$(jq -r '.recommendations | length // 0' "$status_file" 2>/dev/null)
    
    if [[ "$analysis_complete" != "true" ]]; then
        echo "❌ Analysis not completed properly"
        exit 1
    fi
    
    if [[ "$progress_calculated" != "true" ]]; then
        echo "❌ Progress calculation not completed"
        exit 1
    fi
    
    if [[ "$recommendations_count" == "0" ]]; then
        echo "⚠️ No recommendations generated"
    fi
fi

echo "✅ 16-use-case-status agent results verified successfully"
echo "   📊 Status file: $status_file"
echo "   📈 Analysis complete: $analysis_complete"
echo "   📋 Recommendations: $recommendations_count items"
```

### **Step 4: Display Success Summary** 🎉

```bash
# Display comprehensive status summary
echo ""
echo "🎉 プロジェクト状況分析完了!"
echo "=================================="

# Extract and display key metrics
if [[ -f "$status_file" ]] && command -v jq >/dev/null 2>&1; then
    overall_progress=$(jq -r '.progress.overall_percentage // 0' "$status_file" 2>/dev/null)
    current_phase=$(jq -r '.current_phase // "unknown"' "$status_file" 2>/dev/null)
    feature_name=$(jq -r '.feature_name // "unknown"' "$status_file" 2>/dev/null)
    total_issues=$(jq -r '.issues | length // 0' "$status_file" 2>/dev/null)
    
    echo "📊 基本情報:"
    echo "   🏷️  フィーチャー: $feature_name"
    echo "   🔢 対象イシュー: $total_issues 件 ($(IFS=', #'; echo "#${issue_numbers[*]}"))"
    echo "   📈 全体進捗: ${overall_progress}%"
    echo "   📍 現在フェーズ: $current_phase"
    echo ""
    
    # Display progress indicator
    progress_bar=""
    for ((i=1; i<=20; i++)); do
        if (( $(echo "$overall_progress >= $i * 5" | bc -l) )); then
            progress_bar+="█"
        else
            progress_bar+="░"
        fi
    done
    
    echo "📊 進捗状況:"
    echo "   [$progress_bar] ${overall_progress}%"
    echo ""
    
    # Display quality metrics if available
    test_coverage=$(jq -r '.quality.test_coverage // "N/A"' "$status_file" 2>/dev/null)
    ruff_errors=$(jq -r '.quality.ruff_errors // "N/A"' "$status_file" 2>/dev/null)
    pyright_errors=$(jq -r '.quality.pyright_errors // "N/A"' "$status_file" 2>/dev/null)
    
    if [[ "$test_coverage" != "N/A" ]]; then
        echo "🔍 品質メトリクス:"
        echo "   📊 テストカバレッジ: ${test_coverage}%"
        echo "   🔧 Ruffエラー: $ruff_errors 件"
        echo "   🔍 Pyrightエラー: $pyright_errors 件"
        echo ""
    fi
    
    # Display next recommended actions
    recommendations=$(jq -r '.recommendations[]?.action // empty' "$status_file" 2>/dev/null)
    if [[ -n "$recommendations" ]]; then
        echo "📋 推奨アクション:"
        echo "$recommendations" | head -3 | sed 's/^/   /'
        echo ""
    fi
    
    # Progress assessment
    if (( $(echo "$overall_progress >= 100" | bc -l) )); then
        echo "✅ 状態: 完了 - 全開発フェーズが完了しました！"
    elif (( $(echo "$overall_progress >= 80" | bc -l) )); then
        echo "🏁 状態: 最終段階 - もうすぐ完了です"
    elif (( $(echo "$overall_progress >= 60" | bc -l) )); then
        echo "🚀 状態: 順調 - 開発が順調に進んでいます"
    elif (( $(echo "$overall_progress >= 40" | bc -l) )); then
        echo "⚡ 状態: 中盤 - 実装の中盤です"
    elif (( $(echo "$overall_progress >= 20" | bc -l) )); then
        echo "🌱 状態: 初期段階 - 基礎から実装への移行期"
    else
        echo "🚀 状態: 開始 - プロジェクトの初期段階"
    fi
    echo ""
    
    # Show detailed report location
    echo "📋 詳細レポート: $status_file"
    echo "🔄 更新: /use-case-status $(IFS=','; echo "${issue_numbers[*]}") で最新状況確認"
    echo ""
fi

echo "✅ ステータス確認が完了しました"
```
```

## Common Errors and Solutions

### ❌ Error Case 1: Missing issue numbers
**Cause**: Command executed without required issue numbers  
**Solution**: Provide issue numbers: `/use-case-status 1,7`

### ❌ Error Case 2: Project structure not found
**Cause**: Command executed outside of TDD/DDD project  
**Solution**: Initialize project structure: `/init-project-structure`

### ❌ Error Case 3: Metadata files not found
**Cause**: Use cases not created for specified issues  
**Solution**: Create use cases first: `/create-use-case <issue-numbers>,<feature-name>`

## Execution Examples

### ✅ Success Example
```bash
$ /use-case-status 15
🔍 プロジェクト状況分析を開始します...
📋 対象イシュー: #15
🤖 16-use-case-status エージェント実行中...
✅ 分析完了
📊 進捗状況: [████████████████░░░░] 80%
🏁 状態: 最終段階 - もうすぐ完了です
✅ ステータス確認が完了しました
```

### ❌ Failure Example and Fix
```bash
$ /use-case-status
❌ エラー: イシュー番号が必要です
💡 使用例: /use-case-status 1,15

# Fix: Provide issue numbers
$ /use-case-status 1,15
```

## 重要な注意事項

### **包括的状況把握**

- メタデータ・ファイル・GitHub・品質の多角的分析
- リアルタイム進捗計算と可視化
- インテリジェントな次アクション推奨
- ステークホルダー向けレポート生成

### **チーム協力支援**

- GitHub イシューとの完全同期
- 品質メトリクスの透明性確保
- プロジェクト健全性の継続監視
- 具体的なコマンド提案と実行可能性

### **使いやすさと効率性**

- 読み取り専用での安全な実行
- 高速な情報収集とタイムアウト制御
- 美しいコンソール表示と詳細レポート
- エージェント統合による一貫した処理

**統合版ステータス確認コマンドにより、プロジェクトの完全な可視性と効率的な意思決定支援が実現されます！**

## 🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK

ステータス確認中に新課題・ギャップ・改善点発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: ステータス確認は問題発見と進化の重要な機会です
