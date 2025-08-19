Evolve scenarios based on sprint feedback and requirements discovery.

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

**Agent Integration Pattern - 4 Steps:**

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "12-evolve-scenarios" "$ARGUMENTS"
   
   # Validate feature name requirement
   if [[ ${#other_args[@]} -eq 0 ]]; then
       echo "エラー: フィーチャー名が必要です"
       show_usage_example "evolve-scenarios" "feature-name" "フィーチャーのシナリオ進化"
       show_usage_example "evolve-scenarios" "1,feature-name" "イシュー1関連のシナリオ進化"
       show_usage_example "evolve-scenarios" "1,7,feature-name" "複数イシュー統合のシナリオ進化"
       exit 1
   fi
   
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

2. **Execute Specialized Agent**:
   ```bash
   # 🤖 Call specialized agent with Task tool for scenario evolution
   echo "🤖 専用エージェント実行中: 12-evolve-scenarios"
   
   # Build comprehensive task context
   task_context="Scenario Evolution Request:
   
   Feature: $feature_name
   $(if [[ ${#issue_numbers[@]} -gt 0 ]]; then echo "Issues: $(printf '#%s ' "${issue_numbers[@]}")"; fi)
   
   Request: Comprehensive scenario evolution based on feedback and requirements discovery
   
   COMPREHENSIVE TASK CHECKLIST:
   
   🔴 Required Tasks:
   
   🔍 Feedback & Discovery Analysis:
   - Review sprint retrospective feedback from completed sprint
   - Parse development findings from implementation phases (06-09)
   - Review GitHub issue comments for mentioned edge cases
   - Analyze user feedback from stakeholders and end users
   
   📝 New Scenario Identification:
   - Identify edge cases and boundary conditions not covered
   - Define error scenarios for error handling and failure modes
   - Extract performance scenarios and performance requirements
   - Define security scenarios and authorization requirements
   
   📋 Given-When-Then Scenario Creation:
   - Write new Given-When-Then scenarios for each requirement
   - Define preconditions and system state requirements
   - Document expected outcomes and clear success criteria
   - Specify acceptance criteria that are testable
   
   🟡 Recommended Tasks:
   
   🏗️ Domain Impact Assessment:
   - Assess domain model changes (entities, value objects, services)
   - Identify new domain concepts and business terms discovered
   - Update ubiquitous language with new terminology
   - Assess aggregate boundaries and design impacts
   - Identify repository changes and data access patterns
   - Evaluate service impacts on domain and application services
   
   📊 Priority & Impact Analysis:
   - Assign business priority (High/Medium/Low business value)
   - Assess technical complexity and implementation difficulty
   - Estimate effort for implementing each scenario
   - Identify dependencies between scenarios and existing features
   - Assess timeline impact on current sprint and release plans
   - Risk assessment for implementing or deferring scenarios
   
   📁 Scenario Documentation Creation:
   - Create evolved scenario files in docs/use_cases/evolved/
   - Update scenario metadata in relevant issue-X-Y.json files
   - Cross-reference scenarios to original requirements
   - Document traceability between discovery source and scenarios
   
   🟢 Optional Tasks:
   
   🔗 Integration Preparation:
   - Update sprint backlog for integration into product backlog
   - Create GitHub issue templates for new scenarios
   - Plan implementation sequence and optimal order
   - Identify quick wins that can be implemented rapidly
   - Document blockers and external dependencies
   - Prepare stakeholder communication summary
   
   📈 Quality & Validation:
   - Validate scenario completeness and requirement capture
   - Review scenario quality (testable and clear)
   - Validate acceptance criteria (specific and measurable)
   - Check scenario consistency with existing vision
   - Review test failures for revealed scenarios
   - Document integration challenges and system interactions
   - Identify integration scenarios for external systems
   - Document usability scenarios and user experience requirements
   - Add alternative flows and decision points
   - Include error conditions and expected behavior
   - Create implementation notes for future guidance
   - Generate summary report for sprint planning overview
   - Validate business alignment and value delivery
   - Review technical feasibility and achievability
   
   OUTPUT REQUIREMENTS:
   - Generate evolved scenario documents in docs/use_cases/evolved/
   - Update metadata files with evolution tracking
   - Create feedback analysis reports in docs/analysis/
   - Document scenario traceability and cross-references
   - Focus on requirements discovery and documentation only
   - No feature implementation - documentation phase only
   - Maintain scenario consistency with existing vision
   - Integrate findings with sprint planning process"
   
   # Execute the specialized agent
   claude_task="$task_context" \
       claude_agent="12-evolve-scenarios" \
       claude_working_dir="$(pwd)" \
       claude_feature_name="$feature_name" \
       $(if [[ ${#issue_numbers[@]} -gt 0 ]]; then echo "claude_issues=\"$(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\""'; fi) \
       claude --agent
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント結果検証中..."
   
   verification_issues=()
   
   # Check that evolved scenarios were created
   evolved_files=()
   
   # Look for evolved scenario documents
   scenario_pattern="docs/use_cases/evolved/*${feature_name}*.md"
   if ls $scenario_pattern 2>/dev/null | head -1 >/dev/null; then
       scenario_files=$(ls $scenario_pattern 2>/dev/null)
       for file in $scenario_files; do
           evolved_files+=("$file")
           echo "  ✅ 進化シナリオ: $(basename "$file")"
       done
   else
       # Check for updated existing scenario
       existing_pattern="docs/use_cases/*${feature_name}*.md"
       if ls $existing_pattern 2>/dev/null | head -1 >/dev/null; then
           existing_files=$(ls $existing_pattern 2>/dev/null)
           for file in $existing_files; do
               evolved_files+=("$file")
               echo "  ✅ 既存シナリオ更新: $(basename "$file")"
           done
       else
           verification_issues+=("シナリオドキュメントが見つかりません")
       fi
   fi
   
   # Check metadata update
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       evolution_status=$(jq -r '.phases.scenario_evolution.evolved // false' "$metadata_file" 2>/dev/null)
       if [[ "$evolution_status" == "true" ]]; then
           echo "  ✅ メタデータ更新完了"
       else
           verification_issues+=("メタデータ更新が未確認")
       fi
   fi
   
   # Check for analysis reports
   analysis_pattern="docs/analysis/*${feature_name}*evolution*.json"
   if ls $analysis_pattern 2>/dev/null | head -1 >/dev/null; then
       echo "  ✅ フィードバック分析レポート"
   else
       verification_issues+=("フィードバック分析レポートが見つかりません")
   fi
   
   # Check agent exit code
   if [[ $agent_exit_code -ne 0 ]]; then
       verification_issues+=("エージェント実行エラー (終了コード: $agent_exit_code)")
   fi
   
   # Report validation results
   if [[ ${#evolved_files[@]} -eq 0 ]]; then
       verification_issues+=("シナリオ進化ドキュメントが作成されていません")
   fi
   
   if [[ ${#verification_issues[@]} -eq 0 ]]; then
       echo "✅ エージェント結果検証完了"
   else
       echo "❌ エージェント結果検証で問題が発見されました:"
       printf '  - %s\n' "${verification_issues[@]}"
       exit 1
   fi
   ```

4. **Display Success Summary**:
   ```bash
   # 🎉 Display comprehensive success summary
   echo ""
   echo "🎉 シナリオ進化完了!"
   echo ""
   echo "📊 実行サマリー:"
   echo "  🌱 対象フィーチャー: $feature_name"
   $(if [[ ${#issue_numbers[@]} -gt 0 ]]; then echo "  📂 関連Issues: $(printf '#%s ' "${issue_numbers[@]}")"; fi)
   echo "  📝 進化ファイル: ${#evolved_files[@]} 個"
   echo "  🔄 メタデータ: $metadata_file"
   echo ""
   
   # Show evolved scenario files
   echo "📁 進化したシナリオファイル:"
   for file in "${evolved_files[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show evolution summary from metadata
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       evolution_count=$(jq -r '.phases.scenario_evolution.evolution_count // 0' "$metadata_file" 2>/dev/null)
       scenario_type=$(jq -r '.phases.scenario_evolution.scenario_type // "unknown"' "$metadata_file" 2>/dev/null)
       urgency=$(jq -r '.phases.scenario_evolution.urgency // "unknown"' "$metadata_file" 2>/dev/null)
       
       echo ""
       echo "🌱 シナリオ進化サマリー:"
       echo "   📊 進化回数: $evolution_count"
       echo "   📊 シナリオタイプ: $scenario_type"
       echo "   📊 緊急度: $urgency"
   fi
   
   echo ""
   echo "📋 次のステップ (実装・スプリント計画):"
   if [[ ${#issue_numbers[@]} -gt 0 ]]; then
       echo "   💡 /create-use-case $(IFS=','; echo "${issue_numbers[*]}")"
       echo "   💡 /sprint-planning $(IFS=','; echo "${issue_numbers[*]}")"
   else
       echo "   💡 /sprint-planning <next-sprint-number>"
   fi
   echo "   💡 /use-case-status $feature_name"
   
   echo ""
   echo "📁 生成ファイル:"
   for file in "${evolved_files[@]}"; do
       echo "  📝 シナリオ: $file"
   done
   echo "  🔄 メタデータ: $metadata_file"
   
   echo ""
   echo "🔗 関連リソース:"
   if [[ ${#issue_numbers[@]} -gt 0 ]]; then
       for issue_num in "${issue_numbers[@]}"; do
           echo "   - Issue #$issue_num: gh issue view $issue_num"
       done
   else
       echo "   - Feature: $feature_name"
   fi
   
   echo ""
   echo "🎯 シナリオ進化が正常に完了しました!"
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