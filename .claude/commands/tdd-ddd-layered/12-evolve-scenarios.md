Evolve scenarios based on sprint feedback with comprehensive safety and traceability features.

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

### **🔄 Sprint Planning Integration**
- [ ] **Update use cases index**: Add evolved scenarios to tactical tracking document
- [ ] **Prepare for sprint planning**: Package scenarios for next /sprint-planning execution
- [ ] **Update project roadmap**: Reflect scenario evolution in project timeline
- [ ] **Communicate evolution**: Inform stakeholders of scenario discoveries and impacts
- [ ] **Document lessons learned**: Record insights for improving future scenario discovery
- [ ] **Prepare development teams**: Brief teams on new scenarios and implementation approaches

### **📊 Evolution Documentation**
- [ ] **Update metadata**: Record scenario evolution activities in tracking systems
- [ ] **Create evolution report**: Document what scenarios were added and why
- [ ] **Commit scenario files**: Version control all evolved scenario documentation
- [ ] **Update project metrics**: Reflect scenario evolution in project health metrics
- [ ] **Archive discovery notes**: Store raw discovery notes for future reference
- [ ] **Prepare handoff**: Ensure evolved scenarios are ready for next development cycle

**💡 Pro Tip: Scenario evolution is crucial for preventing requirement gaps - better to discover and document now than implement incorrectly later!
2. `12-evolve-scenarios` ← **【YOU ARE HERE】Document new scenarios**
3. `02-sprint-planning` ← Plan new scenarios in next sprint
4. Start new TDD/DDD cycle for evolved scenarios

**CREATE NEW SCENARIO DOCUMENTATION ONLY.**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **フィードバック分析の不備**: 自動的なフィードバック源の検出と統合
- **シナリオ一貫性**: 既存シナリオとの整合性自動チェック
- **ドキュメント同期**: シナリオ・イシュー・スプリント計画の自動連携
- **影響分析の漏れ**: 進化による影響範囲の包括的分析
- **追跡可能性**: 変更理由から実装までの完全トレーサビリティ

### **🆕 新機能**

1. **🔄 インテリジェント分析**: 多様なフィードバック源の自動統合分析
2. **📊 影響評価エンジン**: シナリオ変更の影響範囲自動計算
3. **🛡️ 整合性保証**: 既存アーキテクチャとの一貫性自動検証
4. **🔍 スマート推奨**: 実装タイミングと優先度の自動提案
5. **📈 進化追跡**: シナリオ進化の詳細履歴とパターン分析

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

## Task Details

## 1. **Setup Safe Environment and Parse Arguments**

```bash
# 🔧 Load all safe operation functions with automatic argument parsing and validation
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "12-evolve-scenarios" "$ARGUMENTS"

# Arguments are already parsed and validated by setup script
# Additional validation for this specific command
if [[ ${#other_args[@]} -eq 0 ]]; then
    echo "エラー: フィーチャー名が必要です"
    show_usage_example "evolve-scenarios" "feature-name" "新機能'feature-name'のシナリオ進化"
    show_usage_example "evolve-scenarios" "1,feature-name" "イシュー1関連での'feature-name'シナリオ進化"
    show_usage_example "evolve-scenarios" "1,7,mt5-extended-data" "複数イシュー(1,7)統合での'mt5-extended-data'シナリオ進化"
    exit 1
fi

feature_name="${other_args[0]}"
```

## 2. **Transaction Management and Metadata Discovery**

```bash
# Begin transaction for scenario evolution
transaction_id="evolve_scenarios_$(date +%s)_${feature_name}"
begin_transaction "$transaction_id"

# Setup rollback handlers
add_rollback_handler "echo '🔄 シナリオ進化をロールバック中...'"
add_rollback_handler "git stash push -m 'Auto-stash evolve scenarios rollback' 2>/dev/null || true"
add_rollback_handler "echo '📋 進化前の状態に復旧しました'"

# Discover metadata file
if [[ ${#issue_numbers[@]} -gt 0 ]]; then
    issue_list=$(IFS=-; echo "${issue_numbers[*]}")
    metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
    echo "🎯 関連イシュー: #$(IFS=' #'; echo "${issue_numbers[*]}")"
else
    # Find any metadata file matching the feature name
    metadata_file=$(find docs/use_cases -name "*-${feature_name}.json" | head -1)
    if [[ -z "$metadata_file" ]]; then
        echo "🆕 新しいフィーチャーとしてシナリオ進化を開始"
        # Create minimal metadata for new feature
        metadata_file="docs/use_cases/evolved-${feature_name}.json"
        cat > "$metadata_file" << EOF
{
  "feature": "$feature_name",
  "type": "evolved",
  "created_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "updated_at": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "phase": "scenario_evolution",
  "phases": {
    "scenario_evolution": {
      "evolution_count": 0,
      "evolved": false
    }
  }
}
EOF
    fi
fi

echo "📊 メタデータファイル: $metadata_file"
echo "🎯 フィーチャー: $feature_name"
```

## 3. **Comprehensive Feedback Analysis**

```bash
# Analyze multiple feedback sources intelligently
echo "🔍 フィードバック源を包括的に分析中..."

feedback_analysis_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$feedback_analysis_dir'"

analyze_feedback_sources() {
    local analysis_report="$feedback_analysis_dir/feedback_analysis.json"
    local sources_found=0

    # Initialize analysis report
    cat > "$analysis_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "sources": {},
  "recommendations": [],
  "priority_score": 0
}
EOF

    # 1. Sprint review notes
    echo "  📋 スプリントレビューノートを確認中..."
    if [[ -d "docs/sprints" ]]; then
        local sprint_feedback=""
        for sprint_file in docs/sprints/sprint-*-review.md docs/sprints/sprint-*-retrospective.md; do
            if [[ -f "$sprint_file" ]] && grep -i "$feature_name" "$sprint_file" >/dev/null 2>&1; then
                sprint_feedback+="$(basename "$sprint_file"): $(grep -A 3 -B 1 -i "$feature_name" "$sprint_file" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$sprint_feedback" ]]; then
            jq --arg feedback "$sprint_feedback" '.sources.sprint_reviews = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ スプリントフィードバック発見"
        fi
    fi

    # 2. Review reports
    echo "  📝 レビューレポートを確認中..."
    if [[ -d "docs/review" ]]; then
        local review_feedback=""
        for review_file in docs/review/issue-*-review.md; do
            if [[ -f "$review_file" ]] && grep -i "$feature_name" "$review_file" >/dev/null 2>&1; then
                review_feedback+="$(basename "$review_file"): $(grep -A 3 -B 1 -i "$feature_name" "$review_file" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$review_feedback" ]]; then
            jq --arg feedback "$review_feedback" '.sources.review_reports = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ レビューフィードバック発見"
        fi
    fi

    # 3. GitHub issue comments
    echo "  💬 GitHub イシューコメントを確認中..."
    if [[ ${#issue_numbers[@]} -gt 0 ]]; then
        local github_feedback=""
        for issue_num in "${issue_numbers[@]}"; do
            if safe_gh_command "issue" "view" "$issue_num" --json comments; then
                local comments=$(safe_gh_command "issue" "view" "$issue_num" --json comments | jq -r '.comments[]?.body // empty' | grep -i "$feature_name" | head -5 || true)
                if [[ -n "$comments" ]]; then
                    github_feedback+="Issue #$issue_num: $comments\n"
                    sources_found=$((sources_found + 1))
                fi
            fi
        done

        if [[ -n "$github_feedback" ]]; then
            jq --arg feedback "$github_feedback" '.sources.github_issues = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ GitHub フィードバック発見"
        fi
    fi

    # 4. Test results analysis
    echo "  🧪 テスト結果を分析中..."
    if [[ -d "docs/test_results" ]]; then
        local test_feedback=""
        for test_dir in docs/test_results/*${feature_name}*; do
            if [[ -d "$test_dir" && -f "$test_dir/comprehensive_test_report.md" ]]; then
                # Extract recommendations and issues from test reports
                test_feedback+="$(basename "$test_dir"): $(grep -A 3 "推奨事項\|改善点\|エラー" "$test_dir/comprehensive_test_report.md" | head -10)\n"
                sources_found=$((sources_found + 1))
            fi
        done

        if [[ -n "$test_feedback" ]]; then
            jq --arg feedback "$test_feedback" '.sources.test_results = $feedback' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
            echo "    ✅ テスト結果フィードバック発見"
        fi
    fi

    # Calculate priority score based on sources
    local priority_score=$((sources_found * 20))
    if [[ $priority_score -gt 100 ]]; then priority_score=100; fi

    jq --argjson score "$priority_score" '.priority_score = $score' "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"

    echo "📊 フィードバック分析完了: $sources_found 源から情報収集"
    echo "🎯 優先度スコア: $priority_score/100"

    echo "$analysis_report"
}

analysis_report=$(analyze_feedback_sources)
```

## 4. **Intelligent Scenario Evolution Strategy**

```bash
# Determine evolution strategy based on analysis
echo "🧠 シナリオ進化戦略を決定中..."

evolution_strategy_file="$feedback_analysis_dir/evolution_strategy.json"

determine_evolution_strategy() {
    local priority_score=$(jq -r '.priority_score' "$analysis_report")
    local sources=$(jq -r '.sources | keys[]' "$analysis_report")

    # Determine scenario type and approach
    local scenario_type="extension"  # default
    local implementation_timing="next_sprint"  # default
    local urgency="medium"  # default

    # Analyze content to determine type
    if jq -r '.sources[]' "$analysis_report" | grep -i "error\|bug\|fail" >/dev/null; then
        scenario_type="error_case"
        urgency="high"
        implementation_timing="current_sprint"
    elif jq -r '.sources[]' "$analysis_report" | grep -i "edge\|special\|corner" >/dev/null; then
        scenario_type="edge_case"
        urgency="medium"
    elif jq -r '.sources[]' "$analysis_report" | grep -i "new\|additional\|feature" >/dev/null; then
        scenario_type="new_feature"
        urgency="low"
    fi

    # Adjust based on priority score
    if [[ $priority_score -ge 80 ]]; then
        urgency="high"
        implementation_timing="current_sprint"
    elif [[ $priority_score -ge 50 ]]; then
        urgency="medium"
        implementation_timing="next_sprint"
    else
        urgency="low"
        implementation_timing="future_sprint"
    fi

    cat > "$evolution_strategy_file" << EOF
{
  "feature": "$feature_name",
  "scenario_type": "$scenario_type",
  "urgency": "$urgency",
  "implementation_timing": "$implementation_timing",
  "priority_score": $priority_score,
  "sources_count": $(echo "$sources" | wc -l),
  "recommendations": [
    "シナリオタイプ: $scenario_type",
    "実装タイミング: $implementation_timing",
    "緊急度: $urgency"
  ]
}
EOF

    echo "✅ 進化戦略決定完了"
    echo "  📋 シナリオタイプ: $scenario_type"
    echo "  ⏰ 実装タイミング: $implementation_timing"
    echo "  🚨 緊急度: $urgency"
}

determine_evolution_strategy
```

## 5. **Safe Scenario Document Creation**

```bash
# Create or update scenario document safely
echo "📄 シナリオドキュメントを安全に作成中..."

create_evolved_scenario_document() {
    local doc_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    local urgency=$(jq -r '.urgency' "$evolution_strategy_file")
    local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")

    # Determine document path
    local scenario_doc=""
    if [[ -f "docs/use_cases/${feature_name}.md" ]]; then
        # Update existing document
        scenario_doc="docs/use_cases/${feature_name}.md"
        echo "  📝 既存ドキュメントを更新: $scenario_doc"
    else
        # Create new evolved document
        mkdir -p "docs/use_cases/evolved"
        local timestamp=$(date +%Y%m%d)
        scenario_doc="docs/use_cases/evolved/${feature_name}-${doc_type}-${timestamp}.md"
        echo "  🆕 新規ドキュメントを作成: $scenario_doc"
    fi

    # Create backup if updating existing
    if [[ -f "$scenario_doc" ]]; then
        cp "$scenario_doc" "${scenario_doc}.backup"
        add_rollback_handler "mv '${scenario_doc}.backup' '$scenario_doc'"
    fi

    # Get current sprint number
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    # Generate comprehensive scenario document
    cat > "$scenario_doc" << EOF
# 進化したユースケース: ${feature_name}

## 変更理由
- **発見時期**: Sprint ${current_sprint}
- **フィードバック源**: $(jq -r '.sources | keys | join(", ")' "$analysis_report")
- **重要度**: ${urgency}
- **実装タイミング**: ${timing}

## フィードバック分析詳細

### 分析サマリー
- **優先度スコア**: $(jq -r '.priority_score' "$analysis_report")/100
- **フィードバック源数**: $(jq -r '.sources | length' "$analysis_report")
- **シナリオタイプ**: ${doc_type}

### 主要フィードバック
$(jq -r '.sources | to_entries[] | "#### " + .key + "\n" + .value + "\n"' "$analysis_report")

## 新規/更新シナリオ

### シナリオ1: ${feature_name}の基本進化
- **Given**: 基本機能が実装済みである
- **When**: $(echo "$doc_type" | sed 's/_/ /g')の要求が発生した時
- **Then**: システムは適切に対応する
- **追加理由**: フィードバック分析により$(echo "$doc_type" | sed 's/_/ /g')への対応が必要と判明

### シナリオ2: エラー処理の強化
- **Given**: システムが予期しない状況に遭遇した
- **When**: エラーハンドリングが必要な場合
- **Then**: 適切なエラーメッセージとリカバリ手順を提供する
- **発見経緯**: テスト結果とユーザーフィードバックから

## ドメインへの影響
- **新規概念**: ${doc_type}関連の概念
- **既存概念の変更**: 既存の${feature_name}概念の拡張
- **ユビキタス言語の追加**:
  - ${feature_name}進化: フィードバックに基づく機能改善
  - ${doc_type}: 特定の状況への対応

## 実装への影響
- **影響を受けるレイヤー**: Domain/Application/Infrastructure/Presentation
- **必要な変更**:
  - ドメイン層: 新しいビジネスルールの追加
  - アプリケーション層: 新しいユースケースの実装
  - インフラ層: 必要に応じてデータ永続化の拡張
  - プレゼンテーション層: 新しいAPIエンドポイントの追加
- **推定工数**: $(case "$urgency" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

## 関連するコアシナリオ
- 既存の${feature_name}機能
- 関係性: 既存機能の拡張・改善

## 進化履歴
- **進化日**: $(date)
- **進化理由**: フィードバック駆動開発
- **関連Issue**: $(if [[ ${#issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}")"; else echo "新規作成予定"; fi)

EOF

    echo "✅ シナリオドキュメント作成完了: $scenario_doc"
    echo "$scenario_doc"
}

scenario_document=$(create_evolved_scenario_document)
```

## 6. **GitHub Issue Management with Safety**

```bash
# Create or link GitHub issues safely
echo "🔗 GitHub イシューを安全に管理中..."

manage_github_issues() {
    local new_issues=()

    if [[ ${#issue_numbers[@]} -eq 0 ]]; then
        echo "🆕 新しいイシューを作成中..."

        # Extract scenario details for issue creation
        local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
        local urgency=$(jq -r '.urgency' "$evolution_strategy_file")
        local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")

        # Create comprehensive issue body
        local issue_body="## 概要
${feature_name}のシナリオ進化により発見された新しい要求の実装

## シナリオタイプ
${scenario_type}

## 優先度・緊急度
- 緊急度: ${urgency}
- 実装タイミング: ${timing}
- 優先度スコア: $(jq -r '.priority_score' "$analysis_report")/100

## 発見されたシナリオ
- Given: 基本機能が実装済みである
- When: ${scenario_type}の要求が発生した時
- Then: システムは適切に対応する

## フィードバック源
$(jq -r '.sources | keys | map("- " + .) | join("\n")' "$analysis_report")

## 発見経緯
フィードバック分析により、以下の要求が明確になりました：
$(jq -r '.sources | to_entries[] | "### " + .key + "\n" + (.value | split("\n")[0:3] | join("\n")) + "\n"' "$analysis_report")

## 実装への影響
- 影響レイヤー: Domain/Application/Infrastructure/Presentation
- 推定工数: $(case "$urgency" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

## 関連ドキュメント
- [進化シナリオ](${scenario_document})"

        # Determine labels based on characteristics
        local labels="enhancement,evolved-scenario"
        case "$urgency" in
            "high") labels+=",priority-high,urgent" ;;
            "medium") labels+=",priority-medium" ;;
            "low") labels+=",priority-low" ;;
        esac

        case "$scenario_type" in
            "error_case") labels+=",bug,error-handling" ;;
            "edge_case") labels+=",edge-case" ;;
            "new_feature") labels+=",feature" ;;
        esac

        # Create issue with retry mechanism
        local issue_title="実装: ${feature_name} ${scenario_type}対応"

        if safe_gh_command "issue" "create" --title "$issue_title" --body "$issue_body" --label "$labels"; then
            local new_issue_number=$(safe_gh_command "issue" "list" --label "evolved-scenario" --limit 1 --json number --jq '.[0].number')
            new_issues+=("$new_issue_number")
            issue_numbers+=("$new_issue_number")
            echo "✅ 新しいイシュー作成: #$new_issue_number"
        else
            echo "⚠️ 警告: イシューの作成に失敗しました"
        fi
    else
        echo "🔗 既存イシューにコメント追加中..."

        local comment="🔄 **シナリオ進化**

${feature_name}に関連して新しいシナリオを追加しました。

📋 **詳細**:
- シナリオタイプ: $(jq -r '.scenario_type' "$evolution_strategy_file")
- 緊急度: $(jq -r '.urgency' "$evolution_strategy_file")
- 実装タイミング: $(jq -r '.implementation_timing' "$evolution_strategy_file")

📄 **ドキュメント**: \`${scenario_document}\`

📊 **フィードバック分析**:
- 優先度スコア: $(jq -r '.priority_score' "$analysis_report")/100
- フィードバック源: $(jq -r '.sources | keys | join(", ")' "$analysis_report")"

        for issue_num in "${issue_numbers[@]}"; do
            if safe_gh_command "issue" "comment" "$issue_num" --body "$comment"; then
                echo "✅ Issue #$issue_num にコメント追加"
            else
                echo "⚠️ 警告: Issue #$issue_num へのコメント追加に失敗"
            fi
        done
    fi

    echo "${new_issues[@]}"
}

new_issue_numbers=($(manage_github_issues))
```

## 7. **Scenario Index and Sprint Integration**

```bash
# Update scenario index and integrate with sprint planning
echo "📋 シナリオインデックスとスプリント統合を更新中..."

update_scenario_index() {
    local index_file="docs/use_cases/index.md"
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    # Create backup
    if [[ -f "$index_file" ]]; then
        cp "$index_file" "${index_file}.backup"
        add_rollback_handler "mv '${index_file}.backup' '$index_file'"
    else
        mkdir -p "$(dirname "$index_file")"
        touch "$index_file"
    fi

    # Add evolved scenarios section if not exists
    if ! grep -q "## 進化したシナリオ" "$index_file"; then
        cat >> "$index_file" << EOF

## 進化したシナリオ (Sprint ${current_sprint})
EOF
    fi

    # Add new scenario entry
    local scenario_name="${feature_name} $(jq -r '.scenario_type' "$evolution_strategy_file")対応"
    local issue_ref=""
    if [[ ${#issue_numbers[@]} -gt 0 ]]; then
        issue_ref="Issue #$(IFS=' #'; echo "${issue_numbers[*]}")"
    elif [[ ${#new_issue_numbers[@]} -gt 0 ]]; then
        issue_ref="Issue #$(IFS=' #'; echo "${new_issue_numbers[*]}")"
    else
        issue_ref="新規作成予定"
    fi

    cat >> "$index_file" << EOF
- [${scenario_name}]($(basename "$scenario_document")) - ${issue_ref}
  - 追加理由: フィードバック分析による$(jq -r '.scenario_type' "$evolution_strategy_file")要求
  - ステータス: 計画中
  - 緊急度: $(jq -r '.urgency' "$evolution_strategy_file")
  - 実装予定: $(jq -r '.implementation_timing' "$evolution_strategy_file")
EOF

    echo "✅ シナリオインデックス更新完了"
}

update_sprint_integration() {
    local timing=$(jq -r '.implementation_timing' "$evolution_strategy_file")
    local current_sprint=$(find docs/sprints -name "sprint-*-backlog.md" | sed 's/.*sprint-\([0-9]*\).*/\1/' | sort -n | tail -1)
    if [[ -z "$current_sprint" ]]; then current_sprint="1"; fi

    local target_sprint="$current_sprint"
    case "$timing" in
        "current_sprint") target_sprint="$current_sprint" ;;
        "next_sprint") target_sprint=$((current_sprint + 1)) ;;
        "future_sprint") target_sprint=$((current_sprint + 2)) ;;
    esac

    # Create sprint directories if needed
    mkdir -p "docs/sprints"

    local sprint_backlog="docs/sprints/sprint-${target_sprint}-backlog.md"
    local evolution_report="docs/sprints/sprint-${current_sprint}-evolution.md"

    # Update sprint backlog
    if [[ ! -f "$sprint_backlog" ]]; then
        cat > "$sprint_backlog" << EOF
# スプリント${target_sprint} バックログ

## 進化したシナリオ

EOF
    fi

    # Add to sprint backlog
    cat >> "$sprint_backlog" << EOF
### ${feature_name} 進化対応
- **Issue**: $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "新規作成予定"; fi)
- **タイプ**: $(jq -r '.scenario_type' "$evolution_strategy_file")
- **緊急度**: $(jq -r '.urgency' "$evolution_strategy_file")
- **推定工数**: $(case "$(jq -r '.urgency' "$evolution_strategy_file")" in
    "high") echo "2-3日" ;;
    "medium") echo "1-2週間" ;;
    *) echo "2-4週間" ;;
  esac)

EOF

    # Create evolution report
    cat > "$evolution_report" << EOF
# スプリント${current_sprint} シナリオ進化

## 追加されたシナリオ
1. ${feature_name} $(jq -r '.scenario_type' "$evolution_strategy_file")対応 - Issue $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "新規作成予定"; fi)
   - 優先度: $(jq -r '.urgency' "$evolution_strategy_file")
   - 実装タイミング: スプリント${target_sprint}

## フィードバック分析結果
- **優先度スコア**: $(jq -r '.priority_score' "$analysis_report")/100
- **フィードバック源**: $(jq -r '.sources | keys | join(", ")' "$analysis_report")

## ビジョンへの影響
$(jq -r '.scenario_type' "$evolution_strategy_file")要求により、${feature_name}の機能拡張が必要。
既存アーキテクチャとの整合性は保たれる予定。

## 学習事項
- フィードバック駆動開発により早期に$(jq -r '.scenario_type' "$evolution_strategy_file")要求を発見
- 継続的なユーザーフィードバック収集の重要性を確認
- テスト結果からの学習により品質向上につながった

## 次のアクション
1. 対象スプリント（${target_sprint}）での実装計画策定
2. 関連チームとの調整
3. アーキテクチャレビューの実施

EOF

    echo "✅ スプリント統合更新完了"
    echo "  📋 対象スプリント: ${target_sprint}"
    echo "  📄 進化レポート: ${evolution_report}"
}

update_scenario_index
update_sprint_integration
```

## 8. **Consistency Validation and Architecture Impact**

```bash
# Validate consistency and analyze architecture impact
echo "🏗️ 整合性検証とアーキテクチャ影響分析中..."

validate_scenario_consistency() {
    echo "  🔍 既存シナリオとの整合性をチェック中..."

    local consistency_report="$feedback_analysis_dir/consistency_validation.json"
    local issues_found=0

    # Initialize consistency report
    cat > "$consistency_report" << EOF
{
  "validation_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "checks": {},
  "issues_found": 0,
  "recommendations": []
}
EOF

    # Check vision alignment
    if [[ -f "docs/vision/core_vision.md" ]]; then
        if grep -i "$feature_name" "docs/vision/core_vision.md" >/dev/null 2>&1; then
            jq '.checks.vision_alignment = "aligned"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ ビジョンとの整合性: 整合"
        else
            jq '.checks.vision_alignment = "needs_review" | .issues_found += 1' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ ビジョンとの整合性: 要確認"
            issues_found=$((issues_found + 1))
        fi
    fi

    # Check ubiquitous language consistency
    if [[ -f "docs/domain/ubiquitous_language.md" ]]; then
        local language_conflicts=$(grep -i "$feature_name" "docs/domain/ubiquitous_language.md" | wc -l)
        if [[ $language_conflicts -gt 0 ]]; then
            jq '.checks.language_consistency = "consistent"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ ユビキタス言語: 一貫性保持"
        else
            jq '.checks.language_consistency = "needs_update" | .issues_found += 1' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ ユビキタス言語: 更新必要"
            issues_found=$((issues_found + 1))
        fi
    fi

    # Validate testability
    local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    case "$scenario_type" in
        "error_case"|"edge_case")
            jq '.checks.testability = "high"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ✅ テスト可能性: 高"
            ;;
        "new_feature")
            jq '.checks.testability = "medium"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    📊 テスト可能性: 中"
            ;;
        *)
            jq '.checks.testability = "needs_analysis"' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"
            echo "    ⚠️ テスト可能性: 要分析"
            issues_found=$((issues_found + 1))
            ;;
    esac

    # Update final issues count
    jq --argjson count "$issues_found" '.issues_found = $count' "$consistency_report" > "${consistency_report}.tmp" && mv "${consistency_report}.tmp" "$consistency_report"

    echo "  📊 整合性チェック完了: $issues_found 件の要確認項目"

    return $issues_found
}

analyze_architecture_impact() {
    echo "  🏗️ アーキテクチャ影響を分析中..."

    local impact_report="$feedback_analysis_dir/architecture_impact.json"

    # Determine impacted layers based on scenario type
    local scenario_type=$(jq -r '.scenario_type' "$evolution_strategy_file")
    local impacted_layers=()
    local complexity_score=0

    case "$scenario_type" in
        "error_case")
            impacted_layers=("Domain" "Application" "Presentation")
            complexity_score=60
            ;;
        "edge_case")
            impacted_layers=("Domain" "Application")
            complexity_score=40
            ;;
        "new_feature")
            impacted_layers=("Domain" "Application" "Infrastructure" "Presentation")
            complexity_score=80
            ;;
        "extension")
            impacted_layers=("Application" "Presentation")
            complexity_score=30
            ;;
    esac

    cat > "$impact_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "scenario_type": "$scenario_type",
  "impacted_layers": $(printf '%s\n' "${impacted_layers[@]}" | jq -R . | jq -s .),
  "complexity_score": $complexity_score,
  "recommendations": [
    "影響レイヤー数: ${#impacted_layers[@]}",
    "複雑度スコア: $complexity_score/100",
    "推奨レビュー: $(if [[ $complexity_score -ge 70 ]]; then echo "アーキテクチャレビュー必須"; elif [[ $complexity_score -ge 40 ]]; then echo "設計レビュー推奨"; else echo "実装レビューで十分"; fi)"
  ]
}
EOF

    echo "  📊 影響分析完了:"
    echo "    🎯 影響レイヤー: ${impacted_layers[*]}"
    echo "    📈 複雑度: $complexity_score/100"

    # Validate current architecture if possible
    if command -v validate_architecture_compliance >/dev/null 2>&1; then
        if validate_architecture_compliance; then
            echo "    ✅ 現在のアーキテクチャ: 準拠"
        else
            echo "    ⚠️ 現在のアーキテクチャ: 要確認"
        fi
    fi
}

# Execute validation
if validate_scenario_consistency; then
    echo "✅ 整合性検証: 問題なし"
else
    echo "⚠️ 整合性検証: 要確認項目あり（継続可能）"
fi

analyze_architecture_impact
```

## 9. **Atomic Metadata Update**

```bash
# Update metadata with evolution information
echo "📊 メタデータを原子的に更新中..."

if [[ -f "$metadata_file" ]]; then
    # Count evolution cycles
    current_count=$(jq '.phases.scenario_evolution.evolution_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # Prepare all issue numbers for metadata
    all_issues=("${issue_numbers[@]}" "${new_issue_numbers[@]}")
    issue_json=$(printf '%s\n' "${all_issues[@]}" | jq -R . | jq -s .)

    # Update metadata atomically
    update_metadata_atomic "$metadata_file" "
        .phases.scenario_evolution.evolved = true |
        .phases.scenario_evolution.evolution_count = ${new_count} |
        .phases.scenario_evolution.last_evolved_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.scenario_evolution.scenario_type = \"$(jq -r '.scenario_type' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.urgency = \"$(jq -r '.urgency' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.implementation_timing = \"$(jq -r '.implementation_timing' "$evolution_strategy_file")\" |
        .phases.scenario_evolution.scenario_document = \"$scenario_document\" |
        .phases.scenario_evolution.analysis_report = \"$analysis_report\" |
        .phases.scenario_evolution.related_issues = $issue_json |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"scenarios_evolved\"
    "

    echo "✅ メタデータ更新完了 (進化回数: ${new_count})"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません"
fi
```

## 10. **Transaction Commit and Summary**

```bash
# Commit transaction and provide comprehensive summary
echo "💾 シナリオ進化をコミット中..."

# Add all created files to git
git add -A

# Create comprehensive commit message
commit_message="feat: evolve scenarios for ${feature_name}

Scenario evolution cycle #${new_count} completed based on comprehensive feedback analysis.

Evolution Details:
- Feature: ${feature_name}
- Type: $(jq -r '.scenario_type' "$evolution_strategy_file")
- Urgency: $(jq -r '.urgency' "$evolution_strategy_file")
- Implementation: $(jq -r '.implementation_timing' "$evolution_strategy_file")
- Priority Score: $(jq -r '.priority_score' "$analysis_report")/100

Generated Documents:
- Scenario Document: ${scenario_document}
- Analysis Report: ${analysis_report}
- Strategy Document: ${evolution_strategy_file}

Feedback Sources:
$(jq -r '.sources | keys | map("- " + .) | join("\n")' "$analysis_report")

Related Issues: $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "#$(IFS=' #'; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "None"; fi)"

# Commit changes
if git commit -m "$commit_message"; then
    echo "✅ Git コミット完了"
else
    echo "⚠️ 警告: Git コミットに失敗しました"
fi

# Commit transaction
commit_transaction

# Display comprehensive summary
echo ""
echo "🎉 シナリオ進化完了!"
echo ""
echo "📊 **進化サマリー**:"
echo "   - Feature: ${feature_name}"
echo "   - Evolution Cycle: ${new_count}"
echo "   - Scenario Type: $(jq -r '.scenario_type' "$evolution_strategy_file")"
echo "   - Urgency: $(jq -r '.urgency' "$evolution_strategy_file")"
echo "   - Implementation: $(jq -r '.implementation_timing' "$evolution_strategy_file")"
echo "   - Priority Score: $(jq -r '.priority_score' "$analysis_report")/100"
echo ""
echo "🔍 **フィードバック分析**:"
echo "   - Sources: $(jq -r '.sources | length' "$analysis_report") 種類"
echo "   - Source Types: $(jq -r '.sources | keys | join(", ")' "$analysis_report")"
echo ""
echo "📋 **作成されたリソース**:"
echo "   - 📄 シナリオドキュメント: ${scenario_document}"
echo "   - 📊 分析レポート: ${analysis_report}"
echo "   - 🎯 戦略ドキュメント: ${evolution_strategy_file}"
if [[ ${#new_issue_numbers[@]} -gt 0 ]]; then
    echo "   - 🆕 新規Issue: #$(IFS=' #'; echo "${new_issue_numbers[*]}")"
fi
if [[ ${#issue_numbers[@]} -gt 0 ]]; then
    echo "   - 🔗 関連Issue: #$(IFS=' #'; echo "${issue_numbers[*]}")"
fi
echo ""
echo "🔍 **次のステップ**:"

case "$(jq -r '.implementation_timing' "$evolution_strategy_file")" in
    "current_sprint")
        echo "   - 🚨 緊急: 現在のスプリントで実装開始"
        echo "   - 💡 推奨: /create-tests $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "$(IFS=','; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "<issue-number>"; fi)"
        ;;
    "next_sprint")
        echo "   - 📅 計画: 次のスプリントで実装予定"
        echo "   - 💡 推奨: /sprint-planning $((current_sprint + 1))"
        ;;
    *)
        echo "   - 📋 計画: 将来のスプリントで実装検討"
        echo "   - 💡 推奨: /use-case-status で状況確認"
        ;;
esac

echo "   - 📊 状況確認: /use-case-status ${feature_name}"
echo "   - 📝 レビュー: /review-issue $(if [[ ${#issue_numbers[@]} -gt 0 || ${#new_issue_numbers[@]} -gt 0 ]]; then echo "$(IFS=','; echo "${issue_numbers[*]}${new_issue_numbers[*]}")"; else echo "<issue-number>"; fi)"
echo ""
echo "✅ シナリオ進化プロセスが正常に完了しました"
```

## 重要な注意事項

### **包括的フィードバック分析**

- 複数のフィードバック源（スプリント、レビュー、GitHub、テスト）の自動統合
- 優先度スコアによる客観的な重要度評価
- 進化戦略の自動決定とタイミング提案

### **安全性保証**

- 全操作でのトランザクション管理とロールバック機能
- 既存ドキュメントのバックアップと復旧
- GitHub API の安全な実行とエラーハンドリング

### **整合性とトレーサビリティ**

- 既存アーキテクチャとの一貫性自動検証
- フィードバックから実装までの完全追跡
- スプリント計画との自動統合

### **チーム協力支援**

- 詳細な分析レポートと推奨事項の提供
- GitHub イシューとの完全連携
- 実装タイミングの最適化提案

**統合版シナリオ進化コマンドにより、フィードバック駆動開発が安全かつ効率的に実現されます！**
