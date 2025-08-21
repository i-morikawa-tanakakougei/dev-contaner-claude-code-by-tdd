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

## Task Details

**🤖 Agent Integration**: This command uses the specialized `16-use-case-status` agent for comprehensive development status analysis and intelligent recommendations.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Parse arguments (optional issue numbers)
   if [[ $# -gt 0 ]]; then
       IFS=',' read -ra ISSUES <<< "$1"
       echo "📊 Issues: $(printf '#%s ' "${ISSUES[@]}")のステータス分析を開始します"
   else
       echo "📊 全イシューのステータス分析を開始します"
       ISSUES=()
   fi
   
   # Check for metadata files if specific issues provided
   if [[ ${#ISSUES[@]} -gt 0 ]]; then
       for issue_num in "${ISSUES[@]}"; do
           if ! find docs/use_cases -name "*${issue_num}*" -type f 2>/dev/null | head -1 >/dev/null; then
               echo "❌ Issue #${issue_num} のメタデータが見つかりません"
               echo "💡 まず /create-use-case ${issue_num} を実行してください"
               exit 1
           fi
       done
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "📊 コンテキスト準備とエージェント起動..."
   
   # Create context file with status analysis information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for status analysis
   cat > "$context_file" <<EOF
   {
     "command": "use-case-status",
     "timestamp": "$current_time",
     "issue_numbers": [$(if [[ ${#ISSUES[@]} -gt 0 ]]; then IFS=,; printf '%s\n' "${ISSUES[@]}" | paste -sd,; fi)],
     "phase": "status-analysis",
     "context": {
       "expected_outputs": [
         "docs/status/progress-report.json",
         "docs/status/development-metrics.md",
         "docs/status/next-actions.md"
       ],
       "architecture_patterns": ["Progress Tracking", "Metrics Analysis", "Recommendation Engine"]
     },
     "additional_instructions": "開発進捗の包括的分析を実行してください。全フェーズのメタデータファイルを分析し、完了率、品質メトリクス、ボトルネック、次のアクションを特定してください。視覚的で理解しやすい進捗レポートとインテリジェントな推奨事項を提供してください。",
     "special_considerations": [
       "TDD/DDD/Layered Architecture全フェーズの完了状況分析",
       "Given-When-Thenシナリオと実装の整合性確認",
       "品質メトリクスとテストカバレッジの評価",
       "開発速度と予測可能性の計算"
     ],
     "custom_context": {
       "comprehensive_analysis": true,
       "progress_visualization": true,
       "intelligent_recommendations": true,
       "bottleneck_identification": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "📊 ステータス分析エージェントを起動します..."
   echo "専門エージェントが包括的進捗分析とレコメンデーションを実行します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   cat <<'AGENT_CALL'
   Task tool will be called with:
   - subagent_type: "16-use-case-status"
   - description: "Comprehensive development status analysis and intelligent recommendations"
   - prompt: |
     ユースケースステータス分析タスクを実行してください。
     
     ## コンテキスト情報の取得
     1. 一時コンテキスト（イシュー情報）:
        - /workspace/.claude/context/current-command-context.json を読み込み
     
     2. 開発状況の確認:
        - docs/use_cases/ で全メタデータファイルを分析
        - src/ で実装進捗を確認
        - tests/ でテスト状況を確認
     
     ## 実行タスク
     1. 全開発フェーズのメタデータファイル分析
     2. 完了率とフェーズ状態の視覚的進捗表示
     3. 現在状況に基づくインテリジェント次行動推奨
     4. イシューボトルネック特定と解決提案
     5. 品質メトリクス分析とトレンド可視化
     6. 開発速度計算と予測
     7. リソース使用率とキャパシティ計画インサイト
     8. スプリント進捗追跡とマイルストーン達成分析
     
     ## 処理完了後
     - 包括的な進捗レポートの作成
     - 次の推奨アクションの明確化
     - 開発効率改善提案の提示
   AGENT_CALL
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - 全開発フェーズのメタデータファイル分析"
   echo "  - 完了率とフェーズ状態の視覚的進捗表示"
   echo "  - 現在状況に基づくインテリジェント次行動推奨"
   echo "  - イシューボトルネック特定と解決提案"
   echo "  - 品質メトリクス分析とトレンド可視化"
   echo "  - 開発速度計算と予測"
   ```

3. **Display Comprehensive Status**:
   ```bash
   # 📊 Display comprehensive status summary
   echo ""
   echo "📊 ユースケース開発ステータス"
   echo "=============================="
   
   if [[ ${#ISSUES[@]} -gt 0 ]]; then
       echo "🎯 対象Issues: $(printf '#%s ' "${ISSUES[@]}")"
   else
       echo "🎯 対象: 全イシュー"
   fi
   
   echo ""
   echo "📈 開発進捗:"
   echo "   ✅ 分析完了 - 詳細レポートが利用可能"
   echo "   📊 進捗率とフェーズ状態を表示"
   echo "   🎯 次のアクション推奨を提供"
   echo ""
   echo "✅ ステータス分析完了 - 開発計画最適化準備完了!"
   ```

4. **Advanced Task Verification**:
   ```bash
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "16-use-case-status" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "16-use-case-status" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "16-use-case-status" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

