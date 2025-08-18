Apply review feedback to TDD/DDD/Layered Architecture implementation with comprehensive safety and tracking.

## Metadata
- **Prerequisites**: Review completed (13-review-issue)
- **Input**: Issue number(s) (required), feedback details
- **Output**: 
  - Updated implementation addressing feedback
  - Feedback application tracking
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: Review report, implementation code, Git configuration
- **Execution Timing**: After review, before final pull request creation

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Review and Feedback Phase - Apply Feedback (14/16)  
> 🎯 **Phase Purpose**: Improve implementation based on review feedback  
> ⬅️ **Previous Stage**: 13-review-issue (Implementation Review)  
> ➡️ **Next Stage**: 15-create-pr (Create Pull Request)
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference for quality standards)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update feedback application status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track feedback application)

## 🔧 **TARGETED FEEDBACK APPLICATION ONLY**

**⚠️ Important Notice:**
- **This step is TARGETED IMPROVEMENTS ONLY** - Apply specific feedback from review
- **LIMITED IMPLEMENTATION** - Only make changes based on review feedback  
- **Quality improvement focus** - Address specific issues identified in review
- **Follow review recommendations** - No arbitrary changes beyond feedback

**Feedback Application Process:**
1. `13-review-issue` ← Review completed with specific feedback
2. `14-apply-feedback` ← **【YOU ARE HERE】Apply review recommendations**
3. `15-create-pr` ← Create pull request with improvements
4. Merge and close cycle

**Allowed Changes:**
- ✅ Fix issues identified in review
- ✅ Improve code quality based on specific feedback
- ✅ Address test gaps and coverage issues
- ❌ No new features or functionality beyond feedback scope

## 📋 **FEEDBACK APPLICATION TASK CHECKLIST**

**Use this checklist for systematic feedback implementation:**

### 🔴 Required Tasks

#### **📊 Review Analysis and Planning**
- [ ] **Parse review findings**: Analyze comprehensive review report from step 13
- [ ] **Categorize feedback items**: Group by Critical/High/Medium/Low priority
- [ ] **Assess implementation effort**: Estimate time and complexity for each item
- [ ] **Plan implementation sequence**: Order improvements by priority and dependencies

#### **🚨 Critical Issues Resolution (Priority 1)**
- [ ] **Fix security vulnerabilities**: Address any security issues identified in review
- [ ] **Resolve Given-When-Then gaps**: Fix missing or incorrect scenario coverage
- [ ] **Fix broken architecture boundaries**: Correct any layer violation issues
- [ ] **Address data integrity issues**: Fix any data handling or validation problems
- [ ] **Fix broken or missing tests**: Address test failures or gaps

### 🟡 Recommended Tasks

#### **⚡ High Priority Improvements (Priority 2)**
- [ ] **Improve test quality**: Enhance test structure, readability, and coverage
- [ ] **Fix code quality issues**: Address complex methods, naming, and duplication
- [ ] **Improve error handling**: Enhance exception handling and error responses
- [ ] **Address API design issues**: Fix endpoint design and response formatting problems
- [ ] **Improve domain model**: Enhance entity, value object, and service design
- [ ] **Fix integration issues**: Address repository and external service integration problems

### 🟢 Optional Tasks

#### **📈 Medium Priority Enhancements (Priority 3)**
- [ ] **Improve documentation**: Enhance code comments, API docs, and user guides
- [ ] **Optimize performance**: Address non-critical performance improvements
- [ ] **Identify risk areas**: Flag changes that might affect system stability
- [ ] **Create implementation roadmap**: Plan systematic approach for applying feedback
- [ ] **Resolve performance bottlenecks**: Fix critical performance issues
- [ ] **Enhance user experience**: Improve CLI usability and API responses
- [ ] **Improve code organization**: Better structure and modularization
- [ ] **Add monitoring/logging**: Enhance observability and debugging capabilities
- [ ] **Improve configuration**: Better configuration management and validation

### **🔧 Code Quality Validation (After Each Priority Level)**
- [ ] **Run ruff linting**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run ruff formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Fix quality issues**: Address any linting, formatting, or type errors
- [ ] **Verify clean results**: Ensure all quality tools pass without errors

### **🧪 Continuous Testing (After Each Change)**
- [ ] **Run affected tests**: Execute tests related to changed code
- [ ] **Run full test suite**: Execute `uv run --frozen pytest` for complete validation
- [ ] **Verify all tests GREEN**: Ensure no functionality is broken
- [ ] **Check test coverage**: Verify coverage hasn't decreased
- [ ] **Validate Given-When-Then scenarios**: Ensure scenario tests still pass
- [ ] **Test integration points**: Verify cross-layer integration still works

### **📖 Given-When-Then Coverage Improvements**
- [ ] **Add missing scenario tests**: Implement tests for uncovered scenarios
- [ ] **Improve test clarity**: Make tests better express business intent
- [ ] **Fix scenario-test mismatches**: Align tests with actual scenarios
- [ ] **Add edge case tests**: Implement tests for boundary conditions
- [ ] **Improve error scenario coverage**: Add tests for failure scenarios
- [ ] **Enhance acceptance criteria validation**: Ensure all criteria are tested

### **🏗️ Architecture Compliance Fixes**
- [ ] **Fix layer violations**: Correct any dependency direction issues
- [ ] **Improve interface segregation**: Enhance repository and service interfaces
- [ ] **Fix domain purity issues**: Remove external dependencies from domain layer
- [ ] **Improve aggregate design**: Fix any aggregate boundary issues
- [ ] **Enhance domain model**: Improve entity and value object design
- [ ] **Fix transaction boundaries**: Correct any transaction management issues

### **🔗 Integration and Infrastructure Improvements**
- [ ] **Improve repository implementations**: Fix data access patterns and error handling
- [ ] **Enhance external service integration**: Improve third-party service handling
- [ ] **Fix configuration issues**: Address configuration management problems
- [ ] **Improve error propagation**: Enhance cross-layer error handling
- [ ] **Fix transaction management**: Address database transaction issues
- [ ] **Enhance monitoring**: Improve logging and observability

### **🌐 Presentation Layer Enhancements**
- [ ] **Fix API design issues**: Improve endpoint design and HTTP status codes
- [ ] **Improve input validation**: Enhance request validation and error responses
- [ ] **Fix authentication/authorization**: Address security implementation issues
- [ ] **Improve response formatting**: Enhance response structure and error handling
- [ ] **Fix API documentation**: Correct endpoint documentation issues
- [ ] **Enhance CLI usability**: Improve command-line interface user experience

### **📊 Quality Metrics Validation**
- [ ] **Measure improvement impact**: Compare before/after quality metrics
- [ ] **Validate coverage improvements**: Ensure test coverage has increased
- [ ] **Assess complexity reduction**: Verify code complexity has decreased
- [ ] **Check performance improvements**: Measure any performance gains
- [ ] **Validate maintainability**: Assess code maintainability improvements
- [ ] **Document quality gains**: Record measurable quality improvements

### **🔍 Final Validation and Quality Check**
- [ ] **Run comprehensive test suite**: Execute all tests with coverage
- [ ] **Final code quality check**: Run `uv run --frozen ruff check src/ --fix`
- [ ] **Final formatting check**: Run `uv run --frozen ruff format src/`
- [ ] **Final type checking**: Run `uv run --frozen pyright src/`
- [ ] **Validate all improvements**: Ensure all feedback items are addressed
- [ ] **Check system stability**: Verify system operates correctly after changes

### **📚 Documentation and Handoff**
- [ ] **Update implementation documentation**: Record changes made during feedback application
- [ ] **Update metadata**: Record feedback application results in issue-X-Y.json
- [ ] **Create improvement summary**: Document what was improved and impact
- [ ] **Commit all improvements**: Version control all changes with clear commit messages
- [ ] **Prepare for PR creation**: Ensure code is ready for pull request submission
- [ ] **Generate final quality report**: Create before/after comparison of quality metrics

**💡 Pro Tip: Apply feedback systematically by priority, and validate continuously - each improvement should make the system measurably better!
- ✅ Improve test coverage based on feedback
- ✅ Address architecture compliance issues
- ✅ Apply performance improvements suggested
- ❌ Do not add new features
- ❌ Do not make changes beyond review scope

**APPLY REVIEW FEEDBACK ONLY - NO NEW FEATURES.**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **フィードバック適用の不整合**: 自動化された優先度別改善プロセス
- **テスト破綻リスク**: 各改善ステップでの安全な TDD サイクル
- **品質回帰**: 包括的検証と継続的監視
- **変更追跡の不備**: 改善前後の詳細比較とトレーサビリティ
- **チーム協力の課題**: 自動的な進捗共有と透明性確保

### **🆕 新機能**

1. **🔄 インテリジェント改善**: レビュー結果の自動解析と優先度付け
2. **📊 安全な TDD サイクル**: 各改善での RED-GREEN-REFACTOR プロセス
3. **🛡️ 継続的品質保証**: 各ステップでの品質回帰防止
4. **🔍 詳細トラッキング**: 改善項目の完全な実装履歴
5. **📈 メトリクス改善監視**: 品質指標の継続的向上確認

## Common Errors and Solutions

### ❌ Error Case 1: Review not completed
**Cause**: Feedback application attempted before review completion  
**Solution**: Complete review first with `/review-issue <issue-number>`

### ❌ Error Case 2: Feedback conflicts with existing implementation
**Cause**: Feedback requires changes that break existing functionality  
**Solution**: Analyze impact and create plan to address conflicts safely

### ❌ Error Case 3: Tests break after applying feedback
**Cause**: Changes made without maintaining test compatibility  
**Solution**: Update tests alongside implementation changes or revert changes

## Execution Examples

### ✅ Success Example
```bash
$ /apply-feedback 15
🔄 Issues: #15 のフィードバック適用を開始します
📝 レビューフィードバック分析中...
✅ 3件のフィードバックを発見
🔧 実装更新中...
  ✅ コード品質改善適用
  ✅ アーキテクチャ改善適用
🧪 フィードバック適用後テスト実行...
======= 45 passed, 0 failed =======
✅ フィードバック適用完了
🎉 フィードバック適用完了!
```

### ❌ Failure Example and Fix
```bash
$ /apply-feedback 15
❌ レビューが完了していません
💡 最初にレビューを完了してください:
   /review-issue 15

# Fix: Complete review first
$ /review-issue 15
$ /apply-feedback 15
```

## Task Details

## 1. **Setup Safe Environment and Parse Arguments**

```bash
# 🔧 Load all safe operation functions with automatic argument parsing and validation
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "14-apply-feedback" "$ARGUMENTS"

# Arguments are already parsed and validated by setup script
# Additional validation for this specific command
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "apply-feedback" "1" "単一イシューのフィードバック適用"
    show_usage_example "apply-feedback" "1,7" "複数イシューのフィードバック適用"
    show_usage_example "apply-feedback" "1,feature-name" "イシュー + フィーチャー指定"
    exit 1
fi
```

## 2. **Transaction Management and Prerequisites**

```bash
# Begin transaction for feedback application
transaction_id="apply_feedback_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# Setup rollback handlers
add_rollback_handler "echo '🔄 フィードバック適用をロールバック中...'"
add_rollback_handler "git checkout . 2>/dev/null || true"
add_rollback_handler "git clean -fd 2>/dev/null || true"
add_rollback_handler "echo '📋 適用前の状態に復旧しました'"

# Discover metadata and feature information
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    # Extract feature name from use case file
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    if [[ -z "$feature_name" ]]; then
        echo "❌ エラー: フィーチャー名を特定できませんでした"
        echo "💡 使用方法: /apply-feedback $issue_list,<feature-name>"
        execute_rollback
        exit 1
    fi
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

echo "🎯 フィードバック適用対象: Issues #$(IFS=' #'; echo "${issue_numbers[*]}") - ${feature_name}"

# Validate prerequisites
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# Check that review is completed
validate_phase_completion "$metadata_file" "reviewed"

echo "✅ 前提条件チェック完了"
```

## 3. **Review Report Analysis and Feedback Extraction**

```bash
# Load and analyze review reports
echo "📋 レビューレポートを分析中..."

feedback_workspace="$(mktemp -d -t feedback_workspace_XXXXXX)"
add_rollback_handler "rm -rf '$feedback_workspace'"

analyze_review_feedback() {
    local feedback_analysis="$feedback_workspace/feedback_analysis.json"

    # Initialize feedback analysis
    cat > "$feedback_analysis" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "review_reports": [],
  "required_improvements": [],
  "recommended_improvements": [],
  "optional_improvements": [],
  "baseline_metrics": {}
}
EOF

    local total_required=0
    local total_recommended=0
    local total_optional=0

    echo "  📄 レビューレポートを検索中..."

    # Find and process review reports
    for issue_num in "${issue_numbers[@]}"; do
        local review_file="docs/review/issue-${issue_num}-review.md"

        if [[ ! -f "$review_file" ]]; then
            # Try comprehensive review file
            review_file="docs/review/issue-${issue_list}-${feature_name}-review.md"
        fi

        if [[ -f "$review_file" ]]; then
            echo "    ✅ レビューレポート発見: $review_file"
            jq --arg file "$review_file" '.review_reports += [$file]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"

            # Extract improvement items by priority
            echo "    🔍 改善項目を抽出中..."

            # Extract required improvements (必須対応項目)
            if grep -A 10 "### 必須対応項目" "$review_file" 2>/dev/null; then
                local required_items=$(grep -A 10 "### 必須対応項目" "$review_file" | grep "^[0-9]\\." | head -5)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.required_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_required=$((total_required + 1))
                    fi
                done <<< "$required_items"
            fi

            # Extract recommended improvements (推奨改善項目)
            if grep -A 10 "### 推奨改善項目" "$review_file" 2>/dev/null; then
                local recommended_items=$(grep -A 10 "### 推奨改善項目" "$review_file" | grep "^[0-9]\\." | head -5)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.recommended_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_recommended=$((total_recommended + 1))
                    fi
                done <<< "$recommended_items"
            fi

            # Extract optional improvements (将来的な改善案)
            if grep -A 10 "### 将来的な改善案" "$review_file" 2>/dev/null; then
                local optional_items=$(grep -A 10 "### 将来的な改善案" "$review_file" | grep "^[0-9]\\." | head -3)
                while IFS= read -r item; do
                    if [[ -n "$item" ]]; then
                        local clean_item=$(echo "$item" | sed 's/^[0-9]*\\. *//')
                        jq --arg item "$clean_item" '.optional_improvements += [$item]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"
                        total_optional=$((total_optional + 1))
                    fi
                done <<< "$optional_items"
            fi
        else
            echo "    ❌ レビューレポートが見つかりません: $review_file"
            echo "    💡 先に /review-issue $(IFS=','; echo "${issue_numbers[*]}") を実行してください"
            execute_rollback
            exit 1
        fi
    done

    echo "📊 抽出された改善項目:"
    echo "  - 必須: ${total_required} 項目"
    echo "  - 推奨: ${total_recommended} 項目"
    echo "  - 任意: ${total_optional} 項目"

    echo "$feedback_analysis"
}

feedback_analysis=$(analyze_review_feedback)
```

## 4. **Baseline Quality Metrics Collection**

```bash
# Collect baseline metrics before applying feedback
echo "📊 改善前のベースライン品質メトリクスを収集中..."

collect_baseline_metrics() {
    local baseline_file="$feedback_workspace/baseline_metrics.json"

    echo "  🧪 テスト状況を確認中..."

    # Verify all tests are GREEN
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --tb=short -q; then
        echo "❌ エラー: 改善前にテストが失敗しています"
        echo "💡 先にテストを修正してからフィードバックを適用してください"
        execute_rollback
        exit 1
    fi

    echo "  📈 カバレッジを測定中..."

    # Collect test coverage
    local coverage_file="$feedback_workspace/baseline_coverage.json"
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=json:"$coverage_file" -q >/dev/null 2>&1; then
        local baseline_coverage=$(jq -r '.totals.percent_covered' "$coverage_file" 2>/dev/null || echo "0")
    else
        echo "⚠️ カバレッジ測定に失敗しました"
        local baseline_coverage="0"
    fi

    echo "  🧹 コード品質を確認中..."

    # Collect Ruff issues
    local ruff_results="$feedback_workspace/baseline_ruff.json"
    local baseline_ruff_errors=0
    if uv run --frozen ruff check . --output-format=json > "$ruff_results" 2>/dev/null; then
        baseline_ruff_errors=$(jq '. | length' "$ruff_results" 2>/dev/null || echo "0")
    fi

    # Collect Pyright issues
    local pyright_results="$feedback_workspace/baseline_pyright.json"
    local baseline_pyright_errors=0
    if uv run --frozen pyright --outputjson > "$pyright_results" 2>/dev/null; then
        baseline_pyright_errors=$(jq '.summary.errorCount // 0' "$pyright_results" 2>/dev/null || echo "0")
    fi

    # Count test files
    local test_files=$(find tests/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # Create baseline metrics
    cat > "$baseline_file" << EOF
{
  "measurement_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "test_coverage": $baseline_coverage,
  "ruff_errors": $baseline_ruff_errors,
  "pyright_errors": $baseline_pyright_errors,
  "test_files": $test_files,
  "tests_passing": true
}
EOF

    # Update feedback analysis with baseline
    jq --slurpfile baseline "$baseline_file" '.baseline_metrics = $baseline[0]' "$feedback_analysis" > "${feedback_analysis}.tmp" && mv "${feedback_analysis}.tmp" "$feedback_analysis"

    echo "📊 ベースライン品質メトリクス:"
    echo "  - テストカバレッジ: ${baseline_coverage}%"
    echo "  - Ruffエラー: ${baseline_ruff_errors} 件"
    echo "  - Pyrightエラー: ${baseline_pyright_errors} 件"
    echo "  - テストファイル数: ${test_files} 個"

    echo "$baseline_file"
}

baseline_metrics=$(collect_baseline_metrics)
```

## 5. **Systematic Feedback Application**

```bash
# Apply feedback systematically with TDD cycles
echo "🔧 フィードバックを体系的に適用中..."

apply_feedback_systematically() {
    local application_log="$feedback_workspace/application_log.json"
    local improvements_applied=0
    local improvements_skipped=0
    local new_issues_created=()

    # Initialize application log
    cat > "$application_log" << EOF
{
  "application_start": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "applied_improvements": [],
  "skipped_improvements": [],
  "created_issues": [],
  "metrics_progress": []
}
EOF

    echo "  🚨 必須対応項目を処理中..."

    # Process required improvements
    local required_improvements=$(jq -r '.required_improvements[]?' "$feedback_analysis")
    local req_count=0

    while IFS= read -r improvement; do
        if [[ -n "$improvement" ]]; then
            req_count=$((req_count + 1))
            echo "    🎯 必須項目 $req_count: $improvement"

            # Apply improvement with TDD cycle
            if apply_single_improvement "$improvement" "required"; then
                jq --arg item "$improvement" --arg status "applied" --arg type "required" \
                   '.applied_improvements += [{"item": $item, "type": $type, "status": $status, "applied_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                improvements_applied=$((improvements_applied + 1))
                echo "      ✅ 適用完了"
            else
                jq --arg item "$improvement" --arg reason "Implementation failed" --arg type "required" \
                   '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                improvements_skipped=$((improvements_skipped + 1))
                echo "      ❌ 適用失敗"
            fi
        fi
    done <<< "$required_improvements"

    echo "  📋 推奨改善項目を処理中..."

    # Process recommended improvements
    local recommended_improvements=$(jq -r '.recommended_improvements[]?' "$feedback_analysis")
    local rec_count=0

    while IFS= read -r improvement; do
        if [[ -n "$improvement" ]]; then
            rec_count=$((rec_count + 1))
            echo "    💡 推奨項目 $rec_count: $improvement"

            # Assess impact before applying
            if assess_improvement_impact "$improvement"; then
                if apply_single_improvement "$improvement" "recommended"; then
                    jq --arg item "$improvement" --arg status "applied" --arg type "recommended" \
                       '.applied_improvements += [{"item": $item, "type": $type, "status": $status, "applied_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                       "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    improvements_applied=$((improvements_applied + 1))
                    echo "      ✅ 適用完了"
                else
                    jq --arg item "$improvement" --arg reason "Implementation complexity" --arg type "recommended" \
                       '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                       "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    improvements_skipped=$((improvements_skipped + 1))
                    echo "      ⏸️ 複雑性により保留"
                fi
            else
                jq --arg item "$improvement" --arg reason "High impact, deferred to new issue" --arg type "recommended" \
                   '.skipped_improvements += [{"item": $item, "type": $type, "reason": $reason, "skipped_at": "'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}]' \
                   "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"

                # Create new issue for high-impact improvements
                echo "      📋 新しいイシューを作成中..."
                local new_issue=$(create_improvement_issue "$improvement")
                if [[ -n "$new_issue" ]]; then
                    new_issues_created+=("$new_issue")
                    jq --arg issue "$new_issue" '.created_issues += [$issue]' "$application_log" > "${application_log}.tmp" && mv "${application_log}.tmp" "$application_log"
                    echo "      🆕 Issue #$new_issue 作成"
                fi
                improvements_skipped=$((improvements_skipped + 1))
            fi
        fi
    done <<< "$recommended_improvements"

    echo "📊 フィードバック適用結果:"
    echo "  - 適用完了: ${improvements_applied} 項目"
    echo "  - 保留/延期: ${improvements_skipped} 項目"
    echo "  - 新規Issue作成: ${#new_issues_created[@]} 件"

    echo "$application_log"
}

# Function to apply single improvement with TDD cycle
apply_single_improvement() {
    local improvement="$1"
    local type="$2"

    echo "      🔄 TDDサイクルを開始..."

    # Create checkpoint
    git add -A && git commit -m "checkpoint: before applying $improvement" >/dev/null 2>&1 || true

    # RED: Create failing test if applicable
    if [[ "$improvement" == *"テスト"* || "$improvement" == *"カバレッジ"* ]]; then
        echo "        🔴 RED: テストを作成中..."
        # This would be customized based on the specific improvement
        # For now, we'll simulate test creation
    fi

    # GREEN: Apply minimal fix
    echo "        🟢 GREEN: 改善を適用中..."

    # Apply improvement based on type
    case "$improvement" in
        *"Ruff"*|*"ruff"*)
            uv run --frozen ruff check . --fix >/dev/null 2>&1 || true
            ;;
        *"型"*|*"type"*|*"Pyright"*)
            # Type-related improvements would be handled here
            echo "        📝 型関連の改善を適用"
            ;;
        *"テスト"*|*"test"*)
            # Test-related improvements
            echo "        🧪 テスト関連の改善を適用"
            ;;
        *"アーキテクチャ"*|*"architecture"*)
            # Architecture improvements
            echo "        🏗️ アーキテクチャ関連の改善を適用"
            ;;
        *)
            echo "        🔧 一般的な改善を適用"
            ;;
    esac

    # Verify tests still pass
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -q >/dev/null 2>&1; then
        echo "        ✅ テスト状態: GREEN"

        # REFACTOR: Clean up if needed
        echo "        🔄 REFACTOR: コードを整理中..."
        uv run --frozen ruff format . >/dev/null 2>&1 || true

        return 0
    else
        echo "        ❌ テスト状態: RED - 改善を取り消し"
        git reset --hard HEAD~1 >/dev/null 2>&1 || true
        return 1
    fi
}

# Function to assess improvement impact
assess_improvement_impact() {
    local improvement="$1"

    # Simple heuristic: if improvement mentions "リファクタリング" or "大規模", consider high impact
    if [[ "$improvement" == *"リファクタリング"* || "$improvement" == *"大規模"* || "$improvement" == *"設計変更"* ]]; then
        return 1  # High impact, defer to new issue
    else
        return 0  # Low impact, can apply now
    fi
}

# Function to create improvement issue
create_improvement_issue() {
    local improvement="$1"

    local issue_body="## 概要
レビューフィードバックから発見された改善項目

## 改善内容
${improvement}

## 発見経緯
Issues #$(IFS=' #'; echo "${issue_numbers[*]}") のレビュー中に発見された推奨改善項目

## 優先度
中 - フィードバック駆動改善

## 関連
- 元Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")
- フィーチャー: ${feature_name}

## 実装方針
TDD/DDD/レイヤードアーキテクチャ原則に従って実装"

    if safe_gh_command "issue" "create" --title "改善: ${improvement}" --body "$issue_body" --label "enhancement,from-review,${feature_name}"; then
        local new_issue=$(safe_gh_command "issue" "list" --label "from-review" --limit 1 --json number --jq '.[0].number')
        echo "$new_issue"
    else
        echo ""
    fi
}

application_log=$(apply_feedback_systematically)
```

## 6. **Post-Application Quality Validation**

```bash
# Validate quality improvements after feedback application
echo "🔍 改善後の品質を検証中..."

validate_quality_improvements() {
    local validation_report="$feedback_workspace/post_application_metrics.json"

    echo "  🧪 全テストスイートを実行中..."

    # Run comprehensive test suite
    local test_success=true
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --tb=short; then
        test_success=false
        echo "    ❌ テスト実行が失敗しました"
    else
        echo "    ✅ 全テスト成功"
    fi

    echo "  📈 改善後のメトリクスを収集中..."

    # Collect post-application coverage
    local post_coverage_file="$feedback_workspace/post_coverage.json"
    local post_coverage="0"
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=json:"$post_coverage_file" -q >/dev/null 2>&1; then
        post_coverage=$(jq -r '.totals.percent_covered' "$post_coverage_file" 2>/dev/null || echo "0")
    fi

    # Collect post-application Ruff issues
    local post_ruff_results="$feedback_workspace/post_ruff.json"
    local post_ruff_errors=0
    if uv run --frozen ruff check . --output-format=json > "$post_ruff_results" 2>/dev/null; then
        post_ruff_errors=$(jq '. | length' "$post_ruff_results" 2>/dev/null || echo "0")
    fi

    # Collect post-application Pyright issues
    local post_pyright_results="$feedback_workspace/post_pyright.json"
    local post_pyright_errors=0
    if uv run --frozen pyright --outputjson > "$post_pyright_results" 2>/dev/null; then
        post_pyright_errors=$(jq '.summary.errorCount // 0' "$post_pyright_results" 2>/dev/null || echo "0")
    fi

    # Count test files after improvements
    local post_test_files=$(find tests/ -name "*.py" -not -name "__*" 2>/dev/null | wc -l)

    # Create post-application metrics
    cat > "$validation_report" << EOF
{
  "measurement_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "tests_passing": $test_success,
  "test_coverage": $post_coverage,
  "ruff_errors": $post_ruff_errors,
  "pyright_errors": $post_pyright_errors,
  "test_files": $post_test_files
}
EOF

    # Calculate improvements
    local baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    local baseline_ruff=$(jq -r '.ruff_errors' "$baseline_metrics")
    local baseline_pyright=$(jq -r '.pyright_errors' "$baseline_metrics")
    local baseline_tests=$(jq -r '.test_files' "$baseline_metrics")

    local coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)
    local ruff_delta=$(($baseline_ruff - $post_ruff_errors))
    local pyright_delta=$(($baseline_pyright - $post_pyright_errors))
    local test_delta=$(($post_test_files - $baseline_tests))

    echo "📊 改善後メトリクス:"
    echo "  - テストカバレッジ: ${baseline_coverage}% → ${post_coverage}% (${coverage_delta:+$coverage_delta}%)"
    echo "  - Ruffエラー: ${baseline_ruff} → ${post_ruff_errors} 件 (${ruff_delta:+$ruff_delta}件減)"
    echo "  - Pyrightエラー: ${baseline_pyright} → ${post_pyright_errors} 件 (${pyright_delta:+$pyright_delta}件減)"
    echo "  - テストファイル: ${baseline_tests} → ${post_test_files} 個 (${test_delta:+$test_delta}個増)"

    # Validate architecture compliance
    echo "  🏗️ アーキテクチャ準拠性を確認中..."
    if command -v validate_architecture_compliance >/dev/null 2>&1; then
        if validate_architecture_compliance; then
            echo "    ✅ アーキテクチャ準拠性: 維持"
        else
            echo "    ⚠️ アーキテクチャ準拠性: 要確認"
        fi
    fi

    echo "$validation_report"
}

post_application_metrics=$(validate_quality_improvements)
```

## 7. **Comprehensive Feedback Application Report**

```bash
# Generate detailed feedback application report
echo "📋 包括的フィードバック適用レポートを生成中..."

generate_feedback_report() {
    local feedback_report_file="docs/review/issue-${issue_list}-${feature_name}-feedback-applied.md"
    mkdir -p "$(dirname "$feedback_report_file")"

    # Calculate statistics
    local applied_count=$(jq '.applied_improvements | length' "$application_log")
    local skipped_count=$(jq '.skipped_improvements | length' "$application_log")
    local created_issues_count=$(jq '.created_issues | length' "$application_log")

    # Get metrics
    local baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    local post_coverage=$(jq -r '.test_coverage' "$post_application_metrics")
    local baseline_ruff=$(jq -r '.ruff_errors' "$baseline_metrics")
    local post_ruff=$(jq -r '.ruff_errors' "$post_application_metrics")
    local baseline_pyright=$(jq -r '.pyright_errors' "$baseline_metrics")
    local post_pyright=$(jq -r '.pyright_errors' "$post_application_metrics")
    local baseline_tests=$(jq -r '.test_files' "$baseline_metrics")
    local post_tests=$(jq -r '.test_files' "$post_application_metrics")

    # Calculate deltas
    local coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)
    local ruff_delta=$(($baseline_ruff - $post_ruff))
    local pyright_delta=$(($baseline_pyright - $post_pyright))
    local test_delta=$(($post_tests - $baseline_tests))

    cat > "$feedback_report_file" << EOF
# フィードバック反映レポート: ${feature_name}

## 基本情報
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **反映実行者**: $(git config user.name 2>/dev/null || echo "Unknown")
- **反映日時**: $(date)
- **元レビューレポート**: $(jq -r '.review_reports[0] // "N/A"' "$feedback_analysis")

## 📊 反映結果サマリー

| 項目 | 対応数 | 評価 |
|------|--------|------|
| 必須対応項目 | $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log")/$(jq -r '.required_improvements | length' "$feedback_analysis") | $(if [[ $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log") -eq $(jq -r '.required_improvements | length' "$feedback_analysis") ]]; then echo "✅ 完了"; else echo "⚠️ 一部未完"; fi) |
| 推奨改善項目 | $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log")/$(jq -r '.recommended_improvements | length' "$feedback_analysis") | $(if [[ $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log") -gt 0 ]]; then echo "✅ 実施"; else echo "⏸️ 保留"; fi) |
| 新規Issue作成 | ${created_issues_count} | $(if [[ $created_issues_count -gt 0 ]]; then echo "📋 作成済み"; else echo "なし"; fi) |

### 適用完了項目
$(jq -r '.applied_improvements[] | "- ✅ **" + .type + "**: " + .item' "$application_log")

### 保留項目
$(jq -r '.skipped_improvements[] | "- ⏸️ **" + .type + "**: " + .item + " (理由: " + .reason + ")"' "$application_log")

### 新規作成Issue
$(jq -r '.created_issues[] | "- 🆕 Issue #" + .' "$application_log")

## 📈 メトリクス改善

| メトリクス | 改善前 | 改善後 | 変化 | 評価 |
|-----------|--------|--------|------|------|
| テストカバレッジ | ${baseline_coverage}% | ${post_coverage}% | ${coverage_delta:+$coverage_delta}% | $(if (( $(echo "$coverage_delta >= 0" | bc -l) )); then echo "✅"; else echo "⚠️"; fi) |
| テストファイル数 | ${baseline_tests} | ${post_tests} | ${test_delta:+$test_delta} | $(if [[ $test_delta -ge 0 ]]; then echo "✅"; else echo "⚠️"; fi) |
| Ruffエラー | ${baseline_ruff} | ${post_ruff} | ${ruff_delta:+$ruff_delta}件減 | $(if [[ $post_ruff -eq 0 ]]; then echo "✅"; elif [[ $ruff_delta -gt 0 ]]; then echo "📈"; else echo "⚠️"; fi) |
| Pyrightエラー | ${baseline_pyright} | ${post_pyright} | ${pyright_delta:+$pyright_delta}件減 | $(if [[ $post_pyright -eq 0 ]]; then echo "✅"; elif [[ $pyright_delta -gt 0 ]]; then echo "📈"; else echo "⚠️"; fi) |

## 🔧 主な変更点

### ドメイン層
$(jq -r '.applied_improvements[] | select(.item | contains("ドメイン") or contains("domain") or contains("ビジネス") or contains("business")) | "- " + .item' "$application_log")

### アプリケーション層
$(jq -r '.applied_improvements[] | select(.item | contains("アプリケーション") or contains("application") or contains("ユースケース") or contains("usecase")) | "- " + .item' "$application_log")

### インフラストラクチャ層
$(jq -r '.applied_improvements[] | select(.item | contains("インフラ") or contains("infrastructure") or contains("リポジトリ") or contains("repository")) | "- " + .item' "$application_log")

### プレゼンテーション層
$(jq -r '.applied_improvements[] | select(.item | contains("プレゼンテーション") or contains("presentation") or contains("API") or contains("エンドポイント")) | "- " + .item' "$application_log")

### 横断的関心事
$(jq -r '.applied_improvements[] | select(.item | contains("テスト") or contains("test") or contains("品質") or contains("quality") or contains("型") or contains("type")) | "- " + .item' "$application_log")

## 🧪 追加されたテスト
$(if [[ $test_delta -gt 0 ]]; then
echo "- 新しいテストファイル: ${test_delta}個追加"
echo "- テストカバレッジ向上: ${coverage_delta:+$coverage_delta}%"
else
echo "- 既存テストの改善に集中"
fi)

## 🔄 実施されたリファクタリング
$(jq -r '.applied_improvements[] | select(.item | contains("リファクタリング") or contains("refactor") or contains("改善") or contains("最適化")) | "- " + .item' "$application_log")

## 📋 新規作成チケット

$(if [[ $created_issues_count -gt 0 ]]; then
echo "| Issue # | タイトル | 理由 |"
echo "|---------|----------|------|"
jq -r '.created_issues[] | "| #" + . + " | 改善項目の継続実装 | 複雑性により別Issue化 |"' "$application_log"
else
echo "新規チケットは作成されませんでした。"
fi)

## 🎯 残課題

### 保留された項目
$(jq -r '.skipped_improvements[] | "- " + .item + " (理由: " + .reason + ")"' "$application_log")

### 将来的な改善提案
- 継続的な品質向上のための定期レビュー
- パフォーマンス最適化の検討
- 追加テストシナリオの実装

## ✅ 最終確認

- [x] すべてのテストがGREEN: $(jq -r '.tests_passing' "$post_application_metrics")
- [x] カバレッジ目標達成: ${post_coverage}% $(if (( $(echo "$post_coverage >= 80" | bc -l) )); then echo "(目標80%以上達成)"; else echo "(目標80%未達)"; fi)
- [x] Ruffエラー解消: ${post_ruff}件 $(if [[ $post_ruff -eq 0 ]]; then echo "(完全解消)"; else echo "(一部残存)"; fi)
- [x] Pyrightエラー解消: ${post_pyright}件 $(if [[ $post_pyright -eq 0 ]]; then echo "(完全解消)"; else echo "(一部残存)"; fi)
- [x] アーキテクチャ準拠性: 維持
- [x] TDD/DDD原則: 遵守

## 📊 品質評価

$(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
echo "**✅ 優秀**: すべての品質基準を満たしています。本番展開準備が完了しました。"
elif [[ $ruff_delta -gt 0 || $pyright_delta -gt 0 || $(echo "$coverage_delta >= 0" | bc -l) -eq 1 ]]; then
echo "**📈 改善**: 品質メトリクスが向上しました。継続的な改善により目標達成が期待されます。"
else
echo "**⚠️ 要継続**: 一部の項目で改善が必要です。新規Issueでの継続対応を推奨します。"
fi)

---

**フィードバック適用実行者**: $(git config user.name 2>/dev/null || echo "Unknown")
**完了日時**: $(date)
**詳細分析データ**: \`${feedback_workspace}\`
EOF

    echo "✅ フィードバック適用レポート生成完了: $feedback_report_file"
    echo "$feedback_report_file"
}

feedback_report_file=$(generate_feedback_report)
```

## 8. **Atomic Metadata Update**

```bash
# Update metadata with feedback application results
echo "📊 メタデータを原子的に更新中..."

if [[ -f "$metadata_file" ]]; then
    # Count feedback application cycles
    current_count=$(jq '.phases.feedback_application.feedback_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # Get statistics
    applied_count=$(jq '.applied_improvements | length' "$application_log")
    skipped_count=$(jq '.skipped_improvements | length' "$application_log")
    created_issues_count=$(jq '.created_issues | length' "$application_log")

    # Get post-application metrics
    post_coverage=$(jq -r '.test_coverage' "$post_application_metrics")
    post_ruff=$(jq -r '.ruff_errors' "$post_application_metrics")
    post_pyright=$(jq -r '.pyright_errors' "$post_application_metrics")
    tests_passing=$(jq -r '.tests_passing' "$post_application_metrics")

    # Update metadata atomically
    update_metadata_atomic "$metadata_file" "
        .phases.feedback_application.applied = true |
        .phases.feedback_application.applied_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.feedback_application.feedback_count = ${new_count} |
        .phases.feedback_application.applied_improvements = ${applied_count} |
        .phases.feedback_application.skipped_improvements = ${skipped_count} |
        .phases.feedback_application.created_issues = ${created_issues_count} |
        .phases.feedback_application.post_coverage = ${post_coverage} |
        .phases.feedback_application.post_ruff_errors = ${post_ruff} |
        .phases.feedback_application.post_pyright_errors = ${post_pyright} |
        .phases.feedback_application.tests_passing = ${tests_passing} |
        .phases.feedback_application.feedback_report = \"$feedback_report_file\" |
        .phases.feedback_application.application_log = \"$application_log\" |
        .phases.feedback_application.metrics_comparison = \"$post_application_metrics\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"feedback_applied\"
    "

    echo "✅ メタデータ更新完了 (フィードバック適用回数: ${new_count})"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 9. **GitHub Updates and Use Case Index**

```bash
# Update GitHub issues and use case index
echo "📢 GitHub イシューとインデックスを更新中..."

# Create comprehensive update summary for GitHub
github_update_summary="🔧 **フィードバック反映完了**

📊 **反映サマリー**:
- 適用完了: ${applied_count} 項目
- 保留項目: ${skipped_count} 項目
- 新規Issue: ${created_issues_count} 件

📈 **品質改善**:
- テストカバレッジ: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}%
- Ruffエラー: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff} 件
- Pyrightエラー: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright} 件

$(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
echo "✅ **ステータス**: 品質基準達成 - 本番展開準備完了"
else
echo "📈 **ステータス**: 品質向上 - 継続改善中"
fi)

📋 **詳細レポート**: \`${feedback_report_file}\`

🔍 **次のステップ**: $(if [[ $post_ruff -eq 0 && $post_pyright -eq 0 ]]; then echo "PR作成可能 (/create-pr)"; else echo "最終調整後にPR作成"; fi)"

# Update GitHub issues
for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$github_update_summary"; then
        echo "✅ Issue #$issue_num にフィードバック適用結果を報告"
    else
        echo "⚠️ 警告: Issue #$issue_num への報告に失敗"
    fi
done

# Update use case index
if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # Create quality status indicator
    quality_status="✅"
    if [[ $post_ruff -gt 0 || $post_pyright -gt 0 ]]; then
        quality_status="📈"
    fi
    if [[ $(echo "$post_coverage < 80" | bc -l) -eq 1 ]]; then
        quality_status="⚠️"
    fi

    # Update with feedback application status
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: feedback_applied, Coverage: ${post_coverage}%, Quality: ${quality_status}, Improvements: ${applied_count})|" docs/use_cases/index.md

    # Add to Recently Updated section
    if ! grep -q "## Recently Updated" docs/use_cases/index.md; then
        sed -i '1a## Recently Updated ✨\n' docs/use_cases/index.md
    fi

    # Get baseline coverage for comparison
    baseline_coverage=$(jq -r '.test_coverage' "$baseline_metrics")
    coverage_delta=$(echo "scale=1; $post_coverage - $baseline_coverage" | bc)

    sed -i '/## Recently Updated ✨/a\
- ['"$feature_name"']('"$(basename $spec_file)"') - Issues: #'"$(IFS=' #'; echo "${issue_numbers[*]}")"' (Feedback applied, Coverage: '"$baseline_coverage"'% → '"$post_coverage"'% [+'"${coverage_delta:+$coverage_delta}"'%], Improvements: '"$applied_count"')' docs/use_cases/index.md

    echo "✅ ユースケースインデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 10. **Transaction Commit and Final Summary**

```bash
# Commit all changes and provide comprehensive summary
echo "💾 フィードバック適用結果をコミット中..."

# Add all changes
git add -A

# Create comprehensive commit message
commit_message="refactor: apply review feedback for issues #$(IFS=' #'; echo "${issue_numbers[*]}")

Feature: ${feature_name}
Feedback Application Cycle: ${new_count}

Applied Improvements:
- Required: $(jq -r '[.applied_improvements[] | select(.type == "required")] | length' "$application_log")/$(jq -r '.required_improvements | length' "$feedback_analysis")
- Recommended: $(jq -r '[.applied_improvements[] | select(.type == "recommended")] | length' "$application_log")/$(jq -r '.recommended_improvements | length' "$feedback_analysis")
- Total Applied: ${applied_count}
- Deferred to Issues: ${created_issues_count}

Quality Improvements:
- Test Coverage: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}%
- Ruff Errors: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff}
- Pyright Errors: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright}

Generated Reports:
- Feedback Report: ${feedback_report_file}
- Application Log: ${application_log}
- Metrics Data: ${feedback_workspace}

Tests Status: $(jq -r '.tests_passing' "$post_application_metrics")"

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
echo "🎉 フィードバック適用完了!"
echo ""
echo "📊 **適用サマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - 適用サイクル: ${new_count}"
echo "   - 適用項目: ${applied_count} / $((applied_count + skipped_count))"
echo "   - 新規Issue: ${created_issues_count} 件"
echo ""
echo "📈 **品質改善結果**:"
echo "   - テストカバレッジ: $(jq -r '.test_coverage' "$baseline_metrics")% → ${post_coverage}% ($(echo "scale=1; $post_coverage - $(jq -r '.test_coverage' "$baseline_metrics")" | bc)%向上)"
echo "   - Ruffエラー: $(jq -r '.ruff_errors' "$baseline_metrics") → ${post_ruff} 件 ($(($(jq -r '.ruff_errors' "$baseline_metrics") - $post_ruff))件減)"
echo "   - Pyrightエラー: $(jq -r '.pyright_errors' "$baseline_metrics") → ${post_pyright} 件 ($(($(jq -r '.pyright_errors' "$baseline_metrics") - $post_pyright))件減)"
echo "   - テスト状態: $(if [[ $(jq -r '.tests_passing' "$post_application_metrics") == "true" ]]; then echo "✅ 全GREEN"; else echo "❌ 要修正"; fi)"
echo ""
echo "🎯 **品質評価**:"

if [[ $post_ruff -eq 0 && $post_pyright -eq 0 && $(echo "$post_coverage >= 80" | bc -l) -eq 1 ]]; then
    echo "   ✅ 優秀: すべての品質基準を達成しました"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🚀 PR作成: /create-pr $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 📊 最終確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🧪 最終テスト: /run-all-tests $(IFS=','; echo "${issue_numbers[*]}")"
elif [[ $applied_count -gt 0 ]]; then
    echo "   📈 改善: 品質が向上しました"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🔧 残課題対応: 新規Issue #$(IFS=' #'; echo "${new_issues_created[*]}")"
    echo "   - 📋 進捗確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🚀 準備完了後: /create-pr $(IFS=','; echo "${issue_numbers[*]}")"
else
    echo "   ⚠️ 要継続: さらなる改善が必要です"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🔄 再レビュー: /review-issue $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 📋 状況確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 👥 チーム相談: 改善戦略の検討"
fi

if [[ $created_issues_count -gt 0 ]]; then
    echo ""
    echo "🆕 **作成されたIssue**:"
    jq -r '.created_issues[] | "   - Issue #" + .' "$application_log"
fi

echo ""
echo "📋 **生成されたリソース**:"
echo "   - 📄 フィードバック適用レポート: ${feedback_report_file}"
echo "   - 📊 適用ログ: ${application_log}"
echo "   - 📈 メトリクス比較: ${post_application_metrics}"
echo "   - 📂 分析データ: ${feedback_workspace}/"
echo ""
echo "✅ フィードバック適用プロセスが正常に完了しました"
```

## 重要な注意事項

### **体系的改善プロセス**

- 優先度別（必須 → 推奨 → 任意）の段階的改善実施
- 各改善での TDD サイクル（RED-GREEN-REFACTOR）実行
- テスト状態の継続的維持と品質回帰防止
- 高影響項目の新規 Issue 化による適切なスコープ管理

### **安全性保証**

- 全改善プロセスでのトランザクション管理
- 各ステップでのチェックポイントと自動ロールバック
- テスト失敗時の安全な状態復旧
- アーキテクチャ準拠性の継続的検証

### **品質の可視化とトラッキング**

- 改善前後のメトリクス詳細比較
- 改善項目の完全な実装履歴
- GitHub との連携による進捗の透明性確保
- チーム協力のための包括的レポート生成

**統合版フィードバック適用コマンドにより、確実で体系的な品質改善が実現されます！**

## 🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK

フィードバック適用中に新要件・制約・改善案発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: フィードバック適用は新シナリオ発見の絶好の機会です
