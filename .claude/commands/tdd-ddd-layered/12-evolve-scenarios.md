Use the 12-evolve-scenarios subagent to evolve scenarios based on sprint feedback and requirements discovery. This command MUST USE PROACTIVELY the specialized 12-evolve-scenarios subagent for optimal scenario evolution.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information
- `/workspace/docs/vision/project-vision.md` - Current vision and core scenarios for evolution reference
- `/workspace/docs/metadata/project-state.json` - Integrated project status for update

## Metadata
- **Prerequisites**: Development cycle in progress or completed
- **Input**: Feature name (required), scenario evolution details
- **Output**: 
  - Updated scenario files in `docs/use_cases/evolved/`
  - Evolution tracking in metadata files
  - Integration with sprint planning
- **Dependencies**: Existing use case specifications, Git configuration
- **Execution Timing**: Any time during development when new scenarios are discovered

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Scenario Evolution Phase - Scenario Evolution (12/16)  
> 🎯 **Phase Purpose**: Add new scenarios based on sprint feedback  
> ⬅️ **Previous Stage**: 11-refactor (Refactoring)  
> ➡️ **Next Stage**: New 03-11 cycle or 13-review-issue (Review)
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Update core scenarios)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Track scenario evolution)
> - 🔧 **Execution**: `docs/use_cases/evolved/` (Create evolved scenario documents)

## 🔄 **SCENARIO EVOLUTION: DOCUMENTATION ONLY**

**⚠️ Important Notice:**
- **This step is SCENARIO EVOLUTION ONLY** - Create new scenarios based on feedback
- **NO FEATURE IMPLEMENTATION** - Focus on documenting new requirements  
- **Requirements discovery** - Capture edge cases and new requirements found during development
- **Create evolved scenario documents ONLY** - No code implementation

**Evolution Trigger Points:**
- During development when new requirements are discovered
- After sprint review feedback
- When edge cases are identified
- When integration issues reveal missing scenarios

**Evolution Process:**
1. `11-refactor` ← Development cycle completed
2. `12-evolve-scenarios` ← **【YOU ARE HERE】New scenario discovery and documentation**
3. Return to `02-sprint-planning` ← Integrate new scenarios into backlog
4. New `03-11` development cycle for evolved scenarios

## Common Errors and Solutions

### ❌ Error Case 1: Feature name not provided
**Cause**: Scenario evolution attempted without specifying target feature  
**Solution**: Provide feature name: `/evolve-scenarios <feature-name>`

### ❌ Error Case 2: Scenarios conflict with existing requirements
**Cause**: New scenarios contradict established specifications  
**Solution**: Review and resolve conflicts before integrating scenarios

### ❌ Error Case 3: Missing scenario documentation
**Cause**: Scenarios added without proper Given-When-Then format  
**Solution**: Ensure all scenarios follow structured format with clear conditions

## Execution Examples

### ✅ Success Example
```bash
$ /evolve-scenarios user-management
🌱 フィーチャー 'user-management' のシナリオ進化を開始します
📖 既存シナリオの分析中...
✅ 3個の既存シナリオを発見
🌱 新しいシナリオを追加中...
  ✅ シナリオ作成: ユーザーパスワードリセット
📋 スプリント統合確認中...
✅ 新しいGitHubイシューを作成
🎉 シナリオ進化完了!
```

### ❌ Failure Example and Fix
```bash
$ /evolve-scenarios
エラー: フィーチャー名が必要です
使用例: /evolve-scenarios user-management

# Fix: Provide feature name
$ /evolve-scenarios user-management
```

## 📋 **SCENARIO EVOLUTION TASK CHECKLIST**

**Use this checklist for systematic scenario discovery and integration:**

### 🔴 Required Tasks

#### **🔍 Feedback & Discovery Analysis**
- [ ] **Review sprint retrospective**: Analyze feedback from completed sprint
- [ ] **Parse development findings**: Extract new requirements discovered during implementation (steps 06-09)
- [ ] **Review issue comments**: Scan GitHub issue comments for mentioned edge cases
- [ ] **Analyze user feedback**: Process feedback from stakeholders and end users

#### **📝 New Scenario Identification**
- [ ] **Identify edge cases**: Document boundary conditions and edge cases not covered
- [ ] **Define error scenarios**: Create scenarios for error handling and failure modes
- [ ] **Extract performance scenarios**: Identify performance-related requirements
- [ ] **Define security scenarios**: Document security and authorization requirements

#### **📋 Given-When-Then Scenario Creation**
- [ ] **Write new Given-When-Then scenarios**: Create structured scenarios for each new requirement
- [ ] **Define preconditions**: Specify system state requirements for new scenarios
- [ ] **Document expected outcomes**: Define clear success criteria for each scenario
- [ ] **Specify acceptance criteria**: Create testable acceptance criteria for each scenario

### 🟡 Recommended Tasks

#### **🏗️ Domain Impact Assessment**
- [ ] **Assess domain model changes**: Identify needed changes to entities, value objects, services
- [ ] **Identify new domain concepts**: Document new business terms and concepts discovered
- [ ] **Update ubiquitous language**: Add new terms to project vocabulary
- [ ] **Assess aggregate boundaries**: Determine if new scenarios affect aggregate design
- [ ] **Identify repository changes**: Document needed changes to data access patterns
- [ ] **Evaluate service impacts**: Assess impact on existing domain and application services

#### **📊 Priority & Impact Analysis**
- [ ] **Assign business priority**: Classify scenarios as High/Medium/Low business value
- [ ] **Assess technical complexity**: Evaluate implementation difficulty and risk
- [ ] **Estimate effort**: Provide rough estimates for implementing each scenario
- [ ] **Identify dependencies**: Document dependencies between scenarios and existing features
- [ ] **Assess timeline impact**: Evaluate impact on current sprint and release plans
- [ ] **Risk assessment**: Identify risks associated with implementing or deferring scenarios

#### **📁 Scenario Documentation Creation**
- [ ] **Create evolved scenario files**: Generate files in `docs/use_cases/evolved/`
- [ ] **Update scenario metadata**: Add scenario evolution info to relevant issue-X-Y.json files
- [ ] **Cross-reference scenarios**: Link evolved scenarios to original requirements
- [ ] **Document traceability**: Maintain clear links between discovery source and new scenarios

### 🟢 Optional Tasks

#### **🔗 Integration Preparation**
- [ ] **Update sprint backlog**: Prepare scenarios for integration into product backlog
- [ ] **Create GitHub issue templates**: Draft issue descriptions for new scenarios
- [ ] **Plan implementation sequence**: Suggest optimal order for implementing evolved scenarios
- [ ] **Identify quick wins**: Flag scenarios that can be implemented rapidly
- [ ] **Document blockers**: Note any scenarios that are blocked by external dependencies
- [ ] **Prepare stakeholder communication**: Create summary for stakeholder review

#### **📈 Quality & Validation**
- [ ] **Validate scenario completeness**: Ensure all discovered requirements are captured
- [ ] **Review scenario quality**: Check that scenarios are testable and clear
- [ ] **Validate acceptance criteria**: Ensure criteria are specific and measurable
- [ ] **Check scenario consistency**: Ensure new scenarios align with existing vision
- [ ] **Review test failures**: Identify scenarios revealed by unexpected test failures
- [ ] **Document integration challenges**: Note scenarios discovered during system integration
- [ ] **Identify integration scenarios**: Create scenarios for external system interactions
- [ ] **Document usability scenarios**: Capture user experience and interface requirements
- [ ] **Add alternative flows**: Document alternate paths and decision points
- [ ] **Include error conditions**: Define expected behavior for error scenarios
- [ ] **Create implementation notes**: Provide guidance for future implementation
- [ ] **Generate summary report**: Create overview of all evolved scenarios for sprint planning
- [ ] **Validate business alignment**: Confirm scenarios deliver business value
- [ ] **Review technical feasibility**: Assess that scenarios are technically achievable

**💡 Pro Tip**: Scenario evolution is crucial for preventing requirement gaps - better to discover and document now than implement incorrectly later!

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `12-evolve-scenarios` subagent for optimal scenario evolution and requirements adaptation.
 Claude Code should automatically delegate this task to the 12-evolve-scenarios subagent based on the command description.

## 📖 Subagent Document Reading Instructions

This command delegates to the specialized `12-evolve-scenarios` subagent.

**MANDATORY: The subagent MUST read these files before execution:**

1. `docs/index.md` - Project overview and current status
2. `.claude/context/project-context.json` - Current project context
3. `/workspace/.claude/context/current-command-context.json` - Current execution context
4. `docs/use_cases/core/index.md` - Core scenarios for consistency check
5. `docs/use_cases/` - All existing use case files for evolution context
6. `docs/sprints/` - Sprint plans and feedback for evolution triggers
7. GitHub issue comments and feedback (if available) for requirement discovery

**Command-Specific Reading Focus - Scenario Evolution:**
- Analyze existing scenarios to identify gaps and evolution opportunities
- Review sprint feedback and retrospective findings for new requirements
- Understand domain model and business language for scenario consistency
- Examine implementation challenges that revealed missing scenarios
- Study integration issues that suggest additional edge cases

**CRITICAL:** Use the Read tool to actually read file contents, not just reference paths.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load lightweight structure validation
   source "$(dirname "${BASH_SOURCE[0]}")/_validate_structure.sh"
   
   # Validate feature name requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: フィーチャー名が必要です"
       echo "使用例:"
       echo "  /evolve-scenarios user-authentication        # 単一フィーチャー"
       echo "  /evolve-scenarios trading-execution          # システム拡張"
       exit 1
   fi
   
   # Extract feature name
   feature_name="$1"
   echo "🔄 フィーチャー: $feature_name のシナリオ進化を開始します"
   
   # Execute docs structure validation
   if ! main "12-evolve-scenarios"; then
       echo "❌ ドキュメント構造確認が失敗しました"
       exit 1
   fi
   
   echo "✅ 前提条件確認完了: シナリオ進化準備完了"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🔄 コンテキスト準備とエージェント起動..."
   
   # Create context file with scenario evolution information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for scenario evolution
   cat > "$context_file" <<EOF
   {
     "command": "evolve-scenarios",
     "timestamp": "$current_time",
     "feature_name": "$feature_name",
     "phase": "scenario-evolution",
     "context": {
       "expected_outputs": [
         "docs/use_cases/evolved/$feature_name-evolved.md",
         "docs/analysis/scenario-evolution-report.md"
       ],
       "architecture_patterns": ["Scenario Evolution", "Requirements Discovery", "Given-When-Then"]
     },
     "additional_instructions": "フィーチャー '$feature_name' のシナリオ進化を実行してください。スプリントフィードバック、開発中発見、ユーザー要望を分析し、新しいGiven-When-Thenシナリオを創出してください。",
     "special_considerations": [
       "既存シナリオとの整合性維持",
       "新規要件と制約の適切な文書化",
       "ドメインモデル影響の評価",
       "実装優先度と複雑度の評価"
     ],
     "custom_context": {
       "scenario_discovery": true,
       "requirements_evolution": true,
       "domain_impact_assessment": true,
       "priority_evaluation": true
     }
   }
   EOF
   
   feature_name="${other_args[0]}"
   
   # Set up metadata discovery
   if [[ ${#issue_numbers[@]} -gt 0 ]]; then
       issue_list=$(IFS=-; echo "${issue_numbers[*]}")
       metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
       echo "🎯 関連イシュー: #$(IFS=' #'; echo "${issue_numbers[*]}")"
   else
       # Find any metadata file matching the feature name
       metadata_file=$(find docs/use_cases -name "*-${feature_name}.json" | head -1)
       if [[ -z "$metadata_file" ]]; then
           echo "🆕 新しいフィーチャーとしてシナリオ進化を開始"
           metadata_file="docs/use_cases/evolved-${feature_name}.json"
       fi
   fi
   
   echo "🌱 フィーチャー '$feature_name' のシナリオ進化を開始します"
   echo "✅ 前提条件確認完了: シナリオ進化準備完了"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🌱 コンテキスト準備とエージェント起動..."
   
   # Create context file with scenario evolution information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for scenario evolution
   cat > "$context_file" <<EOF
   {
     "command": "evolve-scenarios",
     "timestamp": "$current_time",
     "feature_name": "$feature_name",
     "issue_numbers": [$(if [[ ${#issue_numbers[@]} -gt 0 ]]; then IFS=,; echo "${issue_numbers[*]}"; fi)],
     "phase": "scenario-evolution",
     "context": {
       "expected_outputs": [
         "docs/use_cases/evolved/",
         "docs/analysis/feedback-analysis.md",
         "docs/analysis/scenario-traceability.md"
       ],
       "architecture_patterns": ["Given-When-Then", "BDD", "Requirements Discovery"]
     },
     "additional_instructions": "スプリントフィードバックと開発で発見された要件に基づいてシナリオを進化させてください。エッジケース、エラーハンドリング、パフォーマンス、セキュリティ要件を含む新しいGiven-When-Thenシナリオを作成し、既存のビジョンとの整合性を保ってください。",
     "special_considerations": [
       "スプリントレトロスペクティブフィードバックの詳細分析",
       "実装フェーズ（06-09）で発見された要件の抽出",
       "エッジケースとエラーシナリオの体系的特定",
       "既存ビジョンとシナリオの一貫性維持"
     ],
     "custom_context": {
       "feedback_analysis": true,
       "requirements_discovery": true,
       "scenario_expansion": true,
       "traceability_documentation": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🌱 シナリオ進化エージェントを起動します..."
   echo "専門エージェントがフィードバックに基づくシナリオ進化を実行します"
   echo ""
   
   # Task tool execution with comprehensive prompt
   task_prompt="シナリオ進化タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（フィーチャー情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. 既存シナリオ情報の確認:
   - docs/use_cases/core/ で既存コアシナリオを確認
   - docs/analysis/ でスプリントフィードバックを確認
   - docs/vision/ でプロジェクトビジョンとの整合性を確認

## 実行タスク
1. スプリントフィードバック分析と要件発見
2. エッジケースとエラーシナリオの特定
3. パフォーマンス・セキュリティ要件の抽出
4. 新しいGiven-When-Thenシナリオの作成
5. ドメインモデル影響評価と更新提案
6. 優先度・複雑度分析とスプリント計画への統合
7. シナリオトレーサビリティ文書の作成
8. ビジョン整合性の検証と品質保証

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
COMPLETED/APPROVED/CONDITIONAL_APPROVAL のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 進化したシナリオファイルのパス報告
- フィードバック分析結果の要約報告
- 次のステップ（イシューレビュー・実装）への案内"

   # Execute with specialized 12-evolve-scenarios subagent
   # The 12-evolve-scenarios subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # 🔍 Verify agent execution results with advanced task checking
   echo "🔍 エージェント実行結果を検証中..."
   
   verification_issues=()
   
   # Check that evolved scenarios were created
   evolved_files=$(find docs/use_cases/evolved/ -name "*${feature_name}*.md" 2>/dev/null | wc -l)
   existing_files=$(find docs/use_cases/ -name "*${feature_name}*.md" 2>/dev/null | wc -l)
   
   # Find latest scenario evolution report
   latest_report=$(find docs/reports/scenario-evolution/ -name "*${feature_name}*.md" 2>/dev/null | sort | tail -1)
   
   if [[ -n "$latest_report" && -f "$latest_report" ]]; then
       echo "  ✅ シナリオ進化レポート: $latest_report"
       
       # ✨ New: Advanced task verification with retry capability
       echo "🔍 Critical tasks確認中..."
       if ! verify_critical_tasks "12-evolve-scenarios" "$latest_report"; then
           echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
           
           # Prepare retry context with specific issues
           prepare_retry_context "12-evolve-scenarios" "1" "${verification_issues[@]}"
           
           echo "🔄 エージェント再実行を準備中..."
           echo "💡 手動での再実行が必要です: /evolve-scenarios $feature_name"
           
           # For now, show the issues and continue
           echo "❌ 以下の問題が検出されました:"
           for issue in "${verification_issues[@]}"; do
               echo "  - $issue"
           done
       else
           echo "✅ Critical tasks確認完了"
       fi
   else
       verification_issues+=("シナリオ進化レポートが見つかりません")
       echo "❌ シナリオ進化レポートが見つかりません"
   fi
   
   # Basic file validation
   if [[ $evolved_files -eq 0 && $existing_files -eq 0 ]]; then
       verification_issues+=("シナリオ進化ドキュメントが見つかりません")
   fi
   
   # ✨ Show comprehensive verification results
   show_verification_results "12-evolve-scenarios"
   
   # Final decision based on verification results
   if [[ ${#verification_issues[@]} -eq 0 ]]; then
       echo "✅ エージェント結果検証完了"
   else
       echo "❌ エージェント実行検証失敗:"
       printf '  - %s\n' "${verification_issues[@]}"
       echo ""
       echo "💡 問題解決のための推奨アクション:"
       echo "  1. シナリオ進化の要件再確認"
       echo "  2. /evolve-scenarios $feature_name での再実行"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   echo "  - 進化シナリオファイル: ${evolved_files}個"
   echo "  - 更新既存ファイル: ${existing_files}個"
   ```

4. **Display Success Summary**:
   ```bash
   # 📊 Display comprehensive success summary
   echo ""
   echo "🎉 シナリオ進化完了!"
   echo "====================="
   
   # Show summary information
   echo "📊 実行サマリー:"
   echo "  🌱 対象フィーチャー: $feature_name"
   if [[ -n "$issue_number" ]]; then
       echo "  📂 関連Issue: #$issue_number"
   fi
   echo "  📝 進化ファイル: ${evolved_files}個"
   echo "  📝 更新ファイル: ${existing_files}個"
   echo ""
   echo "📋 次のステップ:"
   echo "   1. スプリント計画更新: /sprint-planning 次のスプリント番号"
   echo "   2. 新規イシュー作成（必要に応じて）"
   echo "   3. 開発サイクル実行: /create-use-case <new-issue-number>"
   echo ""
   echo "✅ シナリオ進化完了 - 継続的改善サイクル継続中!"
   ```

**💡 Key Benefits of Scenario Evolution:**
- **Requirements Discovery**: Capture new requirements discovered during development
- **Edge Case Documentation**: Document boundary conditions and error scenarios  
- **Feedback Integration**: Systematically incorporate sprint review feedback
- **Continuous Improvement**: Enable iterative requirement refinement
- **Sprint Planning Support**: Provide evolved scenarios for future sprint planning

**🎯 Critical Success Factors:**
- Focus on requirements discovery and documentation only
- Analyze multiple feedback sources comprehensively
- Maintain scenario consistency with existing vision
- Integrate findings with sprint planning process
- Ensure all scenarios follow Given-When-Then format