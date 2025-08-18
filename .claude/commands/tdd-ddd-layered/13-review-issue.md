Review TDD/DDD/Layered Architecture implementation with comprehensive analysis and safety features.

## Metadata
- **Prerequisites**: Implementation completed, all tests passing
- **Input**: Issue number(s) (required)
- **Output**: 
  - Comprehensive review report
  - Quality metrics and analysis
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: Implementation code, test results, analysis tools
- **Execution Timing**: After refactoring, before creating pull request

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Review and Feedback Phase - Implementation Review (13/16)  
> 🎯 **Phase Purpose**: Review implementation quality and architecture compliance  
> ⬅️ **Previous Stage**: 11-refactor (Refactoring) or 12-evolve-scenarios (Scenario Evolution)  
> ➡️ **Next Stage**: 14-apply-feedback (Apply Feedback)
>
> **📋 3-Layer Architecture Operations**:
>
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Validate against vision)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update review status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track review results)

## 🔍 **QUALITY REVIEW: ANALYSIS ONLY**

**⚠️ Important Notice:**
- **This step is QUALITY REVIEW ONLY** - Analyze and assess implementation quality
- **NO IMPLEMENTATION CHANGES** - Focus on evaluation and feedback generation  
- **Quality analysis** - Review architecture compliance, test coverage, and code quality
- **Generate review reports ONLY** - No code modifications

**Review Process:**
1. `11-refactor` ← Implementation and refactoring completed
2. `13-review-issue` ← **【YOU ARE HERE】Quality review and analysis**
3. `14-apply-feedback` ← Apply review feedback and improvements
4. `15-create-pr` ← Create pull request

**Review Focus Areas:**
- ✅ Architecture compliance (DDD/Clean Architecture)
- ✅ Given-When-Then specification coverage and test quality
- ✅ Code quality and maintainability
- ✅ Test coverage and effectiveness

## 📋 **COMPREHENSIVE QUALITY REVIEW TASK CHECKLIST**

**Use this checklist for thorough implementation quality assessment:**

### 🔴 Required Tasks

#### **📖 Given-When-Then Specification Coverage Analysis**
- [ ] **Map scenarios to tests**: Verify each Given-When-Then scenario has corresponding tests
- [ ] **Validate scenario completeness**: Ensure all scenarios from issue specification are tested
- [ ] **Check scenario accuracy**: Verify tests accurately implement the specified scenarios
- [ ] **Assess acceptance criteria coverage**: Confirm all acceptance criteria have test validation

#### **🧪 Test Quality Assessment**
- [ ] **Analyze test structure**: Review test organization and naming conventions
- [ ] **Evaluate test readability**: Assess how clearly tests express business intent
- [ ] **Check test isolation**: Verify tests run independently without side effects
- [ ] **Validate assertion quality**: Ensure tests verify behavior, not just implementation

#### **📊 Test Coverage Analysis**
- [ ] **Generate coverage reports**: Execute `uv run --frozen pytest --cov=src --cov-report=html`
- [ ] **Analyze line coverage**: Review code coverage percentages by layer
- [ ] **Assess branch coverage**: Evaluate decision path coverage in business logic
- [ ] **Identify coverage gaps**: Find critical untested code paths

### 🟡 Recommended Tasks

#### **🏗️ Architecture Compliance Review**
- [ ] **Validate layer separation**: Ensure clean separation between domain/application/infrastructure/presentation
- [ ] **Check dependency directions**: Verify dependencies point inward (Clean Architecture)
- [ ] **Review interface segregation**: Assess repository interfaces and their implementations
- [ ] **Validate domain purity**: Ensure domain layer has no external dependencies
- [ ] **Check aggregate boundaries**: Review aggregate design and transaction boundaries
- [ ] **Assess domain model richness**: Evaluate business logic placement and organization

#### **🎯 Domain-Driven Design Review**
- [ ] **Validate ubiquitous language**: Check consistency of domain terminology across code
- [ ] **Review entity design**: Assess entity identity, lifecycle, and behavior
- [ ] **Evaluate value objects**: Check immutability, validation, and equality implementation
- [ ] **Assess domain services**: Review complex business logic placement

### 🟢 Optional Tasks

#### **📀 Advanced Test Quality Assessment**
- [ ] **Review edge case coverage**: Verify edge cases from scenarios are properly tested
- [ ] **Validate error scenario testing**: Ensure error scenarios have corresponding failure tests
- [ ] **Review test data quality**: Assess test fixtures and data setup appropriateness
- [ ] **Check test performance**: Identify slow tests and performance bottlenecks
- [ ] **Review integration coverage**: Assess cross-layer integration test coverage
- [ ] **Validate e2e coverage**: Ensure complete user scenarios are tested
- [ ] **Review domain events**: Evaluate event design and integration patterns
- [ ] **Validate bounded context integrity**: Ensure context boundaries are respected

### **💻 Code Quality Assessment**
- [ ] **Run static analysis**: Execute `uv run --frozen ruff check src/` and analyze results
- [ ] **Check formatting compliance**: Verify `uv run --frozen ruff format src/` shows no changes
- [ ] **Validate type annotations**: Run `uv run --frozen pyright src/` and review type coverage
- [ ] **Assess code complexity**: Identify overly complex methods and classes
- [ ] **Review naming conventions**: Evaluate variable, method, and class naming clarity
- [ ] **Check code duplication**: Identify and assess duplicate code patterns

### **🔗 Integration Quality Review**
- [ ] **Test repository implementations**: Verify data access patterns and error handling
- [ ] **Review external service integration**: Assess third-party service integration patterns
- [ ] **Validate configuration management**: Review environment and configuration handling
- [ ] **Check error propagation**: Ensure errors are properly handled across layers
- [ ] **Assess transaction management**: Review database transaction patterns
- [ ] **Validate monitoring and logging**: Check observability implementation

### **🌐 Presentation Layer Review**
- [ ] **Validate API design**: Review REST endpoint design and HTTP status codes
- [ ] **Check input validation**: Assess request validation and error response quality
- [ ] **Review authentication/authorization**: Evaluate security implementation
- [ ] **Assess response formatting**: Check response structure and error handling
- [ ] **Validate API documentation**: Review endpoint documentation quality
- [ ] **Check CLI usability**: Evaluate command-line interface user experience

### **🚀 Performance and Scalability Assessment**
- [ ] **Identify performance bottlenecks**: Review slow code paths and database queries
- [ ] **Assess memory usage**: Check for memory leaks and inefficient data structures
- [ ] **Review caching strategies**: Evaluate caching implementation where applicable
- [ ] **Check database optimization**: Review query performance and indexing
- [ ] **Assess scalability patterns**: Evaluate code scalability and concurrency handling
- [ ] **Review resource management**: Check proper resource cleanup and disposal

### **🔒 Security Review**
- [ ] **Validate input sanitization**: Check protection against injection attacks
- [ ] **Review authentication implementation**: Assess login/logout security
- [ ] **Check authorization patterns**: Evaluate access control implementation
- [ ] **Assess data protection**: Review sensitive data handling and storage
- [ ] **Validate configuration security**: Check for exposed secrets or credentials
- [ ] **Review error information disclosure**: Ensure errors don't leak sensitive data

### **📚 Documentation Quality Review**
- [ ] **Review code documentation**: Assess docstring quality and completeness
- [ ] **Validate API documentation**: Check endpoint documentation accuracy
- [ ] **Assess architecture documentation**: Review system design documentation
- [ ] **Check setup instructions**: Validate project setup and development guides
- [ ] **Review decision records**: Assess architectural decision documentation
- [ ] **Evaluate user documentation**: Check end-user facing documentation

### **📊 Business Value Assessment**
- [ ] **Validate requirement fulfillment**: Confirm all business requirements are met
- [ ] **Assess user experience**: Evaluate end-user interaction quality
- [ ] **Review business rule implementation**: Verify business logic correctness
- [ ] **Check acceptance criteria satisfaction**: Ensure all criteria are met
- [ ] **Validate edge case handling**: Confirm proper handling of business edge cases
- [ ] **Assess maintainability for business**: Evaluate ease of future business changes

### **📈 Quality Metrics Generation**
- [ ] **Generate comprehensive quality report**: Create detailed quality assessment document
- [ ] **Document specific improvements**: List concrete, actionable improvement suggestions
- [ ] **Prioritize feedback items**: Rank improvements by impact and effort
- [ ] **Create stakeholder summary**: Generate business-friendly quality summary
- [ ] **Document architectural compliance**: Record adherence to design principles
- [ ] **Generate metrics dashboard**: Create visual quality indicators

### **🔄 Review Documentation and Handoff**
- [ ] **Update review metadata**: Record review results in issue-X-Y.json
- [ ] **Create feedback action items**: Generate specific tasks for 14-apply-feedback
- [ ] **Document review findings**: Create comprehensive review report
- [ ] **Prepare improvement roadmap**: Suggest sequence for applying improvements
- [ ] **Communicate to stakeholders**: Share review results with relevant parties
- [ ] **Archive review artifacts**: Store review documents for future reference

**💡 Pro Tip: Focus on Given-When-Then traceability - every business scenario should have clear test coverage demonstrating the expected behavior!
- ✅ Test coverage and quality
- ✅ Code quality metrics
- ✅ Scenario implementation completeness
- ❌ Do not make implementation changes
- ❌ Do not modify existing code

**ANALYZE AND REVIEW ONLY - NO CODE CHANGES.**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **レビュープロセスの不整合**: 自動化されたチェックリストと網羅的分析
- **品質基準の曖昧さ**: 定量的メトリクスと明確な合格基準
- **フィードバック追跡**: 改善提案から実装まで完全なトレーサビリティ
- **レビュー漏れ**: 多角的分析による包括的品質評価
- **アーキテクチャ違反**: 自動検出と詳細分析

### **🆕 新機能**

1. **🔄 自動品質分析**: 全レイヤーの包括的自動評価
2. **📊 定量的評価**: 客観的指標による品質スコアリング
3. **🛡️ アーキテクチャガード**: DDD/Clean Architecture 原則の自動検証
4. **🔍 深度分析**: コード品質・テスト・設計の多角的評価
5. **📈 改善トラッキング**: 問題から解決まで完全追跡

## Common Errors and Solutions

### ❌ Error Case 1: Implementation not completed
**Cause**: Review attempted before all implementation phases finished  
**Solution**: Complete all phases: domain → application → infrastructure → presentation → tests → refactor

### ❌ Error Case 2: Quality metrics below threshold
**Cause**: Code quality issues detected during review  
**Solution**: Address quality issues and re-run review process

### ❌ Error Case 3: Architecture violations detected
**Cause**: Layer dependencies or patterns not following clean architecture  
**Solution**: Fix architecture violations and verify compliance

## Execution Examples

### ✅ Success Example
```bash
$ /review-issue 15
🔍 Issues: #15 の実装レビューを開始します
📊 品質メトリクス分析中...
✅ テストカバレッジ: 92%
✅ アーキテクチャコンプライアンス: ✅
✅ コード品質: Grade A
📝 レビューレポート作成中...
✅ レビューレポート: docs/reviews/issue-15-review.md
🎉 レビュー完了 - PR作成準備完了!
```

### ❌ Failure Example and Fix
```bash
$ /review-issue 15
❌ アーキテクチャ違反が検出されました
💡 違反箷所を修正してから再レビューしてください
# Fix: Address violations then re-review
$ /review-issue 15
```

## Task Details

## 1. **Setup Safe Environment and Parse Arguments**

```bash
# 🔧 Load all safe operation functions with automatic argument parsing and validation
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "13-review-issue" "$ARGUMENTS"

# Arguments are already parsed and validated by setup script
# Additional validation for this specific command
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "review-issue" "1" "単一イシューのレビュー"
    show_usage_example "review-issue" "1,7" "複数イシューのレビュー"
    show_usage_example "review-issue" "1,feature-name" "イシュー + フィーチャー指定"
    exit 1
fi
```

## 2. **Transaction Management and Artifact Discovery**

```bash
# Begin transaction for review process
transaction_id="review_issue_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# Setup rollback handlers
add_rollback_handler "echo '🔄 レビュープロセスをロールバック中...'"
add_rollback_handler "rm -rf review_temp_* 2>/dev/null || true"
add_rollback_handler "echo '📋 レビュー前の状態に復旧しました'"

# Discover metadata and feature information
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    # Extract feature name from use case file
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    if [[ -z "$feature_name" ]]; then
        echo "❌ エラー: フィーチャー名を特定できませんでした"
        echo "💡 使用方法: /review-issue $issue_list,<feature-name>"
        execute_rollback
        exit 1
    fi
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

echo "🎯 レビュー対象: Issues #$(IFS=' #'; echo "${issue_numbers[*]}") - ${feature_name}"

# Validate prerequisites
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# Check that implementation is completed
validate_phase_completion "$metadata_file" "all_tests_completed"

echo "✅ 前提条件チェック完了"
```

## 3. **Comprehensive Artifact Analysis**

```bash
# Gather and analyze all implementation artifacts
echo "📋 実装成果物を包括的に分析中..."

review_workspace="$(mktemp -d -t review_workspace_XXXXXX)"
add_rollback_handler "rm -rf '$review_workspace'"

analyze_implementation_artifacts() {
    local artifacts_report="$review_workspace/artifacts_analysis.json"

    # Initialize artifacts analysis
    cat > "$artifacts_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "issues": [$(IFS=','; echo "\"${issue_numbers[*]}\"")],
  "artifacts": {},
  "completeness_score": 0
}
EOF

    local score=0
    local max_score=100

    echo "  📄 ドキュメント成果物を確認中..."

    # Check use case specifications
    if [[ -f "$spec_file" ]]; then
        jq '.artifacts.use_case_spec = {"exists": true, "path": "'$spec_file'"}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        score=$((score + 15))
        echo "    ✅ ユースケース仕様: $spec_file"
    else
        jq '.artifacts.use_case_spec = {"exists": false, "issue": "Missing use case specification"}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        echo "    ❌ ユースケース仕様: 見つかりません"
    fi

    # Check domain model documentation
    local domain_docs=$(find docs/domain -name "*${feature_name}*" -o -name "issue-${issue_list}-*" 2>/dev/null | head -5)
    if [[ -n "$domain_docs" ]]; then
        jq --arg docs "$domain_docs" '.artifacts.domain_model = {"exists": true, "docs": $docs}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        score=$((score + 10))
        echo "    ✅ ドメインモデル文書"
    else
        jq '.artifacts.domain_model = {"exists": false, "issue": "Missing domain model documentation"}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        echo "    ⚠️ ドメインモデル文書: 部分的"
    fi

    # Check test documentation
    local test_docs=$(find docs/test_results -name "*${feature_name}*" -o -name "*issue-${issue_list}-*" 2>/dev/null | head -5)
    if [[ -n "$test_docs" ]]; then
        jq --arg docs "$test_docs" '.artifacts.test_docs = {"exists": true, "docs": $docs}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        score=$((score + 10))
        echo "    ✅ テストドキュメント"
    else
        jq '.artifacts.test_docs = {"exists": false, "issue": "Missing test documentation"}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
        echo "    ⚠️ テストドキュメント: 限定的"
    fi

    echo "  🏗️ 実装レイヤーを確認中..."

    # Check implementation layers
    local layers=("domain" "application" "infrastructure" "presentation")
    for layer in "${layers[@]}"; do
        local layer_files=$(find src/$layer -name "*.py" 2>/dev/null | wc -l)
        if [[ $layer_files -gt 0 ]]; then
            jq --arg layer "$layer" --argjson count "$layer_files" '.artifacts[$layer + "_layer"] = {"exists": true, "file_count": $count}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
            score=$((score + 15))
            echo "    ✅ ${layer}層: ${layer_files} ファイル"
        else
            jq --arg layer "$layer" '.artifacts[$layer + "_layer"] = {"exists": false, "issue": "No implementation files found"}' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"
            echo "    ❌ ${layer}層: 実装なし"
        fi
    done

    # Update completeness score
    jq --argjson score "$score" '.completeness_score = $score' "$artifacts_report" > "${artifacts_report}.tmp" && mv "${artifacts_report}.tmp" "$artifacts_report"

    echo "📊 成果物完成度: ${score}/${max_score} ($(( score * 100 / max_score ))%)"
    echo "$artifacts_report"
}

artifacts_analysis=$(analyze_implementation_artifacts)
```

## 4. **Multi-Layer Architecture Review**

```bash
# Conduct comprehensive architecture review
echo "🏗️ レイヤードアーキテクチャを包括的にレビュー中..."

conduct_architecture_review() {
    local arch_review_report="$review_workspace/architecture_review.json"

    # Initialize architecture review
    cat > "$arch_review_report" << EOF
{
  "review_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "layers": {},
  "architecture_score": 0,
  "violations": [],
  "recommendations": []
}
EOF

    local total_score=0
    local violations=()

    echo "  📦 ドメイン層をレビュー中..."

    # Domain Layer Review
    local domain_score=0
    local domain_issues=()

    if [[ -d "src/domain" ]]; then
        # Check entities
        local entities=$(find src/domain -name "*entit*.py" -o -name "*entity*.py" 2>/dev/null | wc -l)
        if [[ $entities -gt 0 ]]; then
            domain_score=$((domain_score + 25))
            echo "    ✅ エンティティ: ${entities} 個"
        else
            domain_issues+=("エンティティが見つかりません")
            echo "    ⚠️ エンティティ: 見つかりません"
        fi

        # Check value objects
        local value_objects=$(find src/domain -name "*value*.py" -o -name "*vo.py" 2>/dev/null | wc -l)
        if [[ $value_objects -gt 0 ]]; then
            domain_score=$((domain_score + 25))
            echo "    ✅ 値オブジェクト: ${value_objects} 個"
        else
            domain_issues+=("値オブジェクトが見つかりません")
            echo "    ⚠️ 値オブジェクト: 見つかりません"
        fi

        # Check repositories (interfaces)
        local repositories=$(find src/domain -name "*repo*.py" -o -name "*repository*.py" 2>/dev/null | wc -l)
        if [[ $repositories -gt 0 ]]; then
            domain_score=$((domain_score + 25))
            echo "    ✅ リポジトリインターフェース: ${repositories} 個"
        else
            domain_issues+=("リポジトリインターフェースが見つかりません")
            echo "    ⚠️ リポジトリ: 見つかりません"
        fi

        # Check external dependencies in domain
        if grep -r "import.*\(sqlalchemy\|requests\|fastapi\)" src/domain/ 2>/dev/null; then
            violations+=("ドメイン層に外部依存が検出されました")
            echo "    ❌ 外部依存: 検出（DDD違反）"
        else
            domain_score=$((domain_score + 25))
            echo "    ✅ 外部依存: なし（DDD準拠）"
        fi
    else
        domain_issues+=("ドメイン層のディレクトリが存在しません")
    fi

    jq --argjson score "$domain_score" --argjson issues "$(printf '%s\n' "${domain_issues[@]}" | jq -R . | jq -s .)" \
       '.layers.domain = {"score": $score, "max_score": 100, "issues": $issues}' \
       "$arch_review_report" > "${arch_review_report}.tmp" && mv "${arch_review_report}.tmp" "$arch_review_report"

    echo "  🎯 アプリケーション層をレビュー中..."

    # Application Layer Review
    local app_score=0
    local app_issues=()

    if [[ -d "src/application" ]]; then
        # Check use cases
        local use_cases=$(find src/application -name "*use_case*.py" -o -name "*usecase*.py" 2>/dev/null | wc -l)
        if [[ $use_cases -gt 0 ]]; then
            app_score=$((app_score + 30))
            echo "    ✅ ユースケース: ${use_cases} 個"
        else
            app_issues+=("ユースケースが見つかりません")
            echo "    ⚠️ ユースケース: 見つかりません"
        fi

        # Check DTOs
        local dtos=$(find src/application -name "*dto*.py" -o -name "*request*.py" -o -name "*response*.py" 2>/dev/null | wc -l)
        if [[ $dtos -gt 0 ]]; then
            app_score=$((app_score + 35))
            echo "    ✅ DTO/リクエスト/レスポンス: ${dtos} 個"
        else
            app_issues+=("DTOクラスが見つかりません")
            echo "    ⚠️ DTO: 見つかりません"
        fi

        # Check for business logic in application layer (should be minimal)
        local business_logic_lines=$(find src/application -name "*.py" -exec grep -l "if.*business\|calculate\|validate.*business" {} \; 2>/dev/null | wc -l)
        if [[ $business_logic_lines -eq 0 ]]; then
            app_score=$((app_score + 35))
            echo "    ✅ ビジネスロジック: ドメイン層に適切に分離"
        else
            app_issues+=("アプリケーション層にビジネスロジックが含まれている可能性")
            echo "    ⚠️ ビジネスロジック: アプリケーション層に検出"
        fi
    else
        app_issues+=("アプリケーション層のディレクトリが存在しません")
    fi

    jq --argjson score "$app_score" --argjson issues "$(printf '%s\n' "${app_issues[@]}" | jq -R . | jq -s .)" \
       '.layers.application = {"score": $score, "max_score": 100, "issues": $issues}' \
       "$arch_review_report" > "${arch_review_report}.tmp" && mv "${arch_review_report}.tmp" "$arch_review_report"

    echo "  🗄️ インフラストラクチャ層をレビュー中..."

    # Infrastructure Layer Review
    local infra_score=0
    local infra_issues=()

    if [[ -d "src/infrastructure" ]]; then
        # Check repository implementations
        local repo_impls=$(find src/infrastructure -name "*repo*.py" -o -name "*repository*.py" 2>/dev/null | wc -l)
        if [[ $repo_impls -gt 0 ]]; then
            infra_score=$((infra_score + 40))
            echo "    ✅ リポジトリ実装: ${repo_impls} 個"
        else
            infra_issues+=("リポジトリ実装が見つかりません")
            echo "    ⚠️ リポジトリ実装: 見つかりません"
        fi

        # Check persistence models
        local models=$(find src/infrastructure -name "*model*.py" -o -name "*entity*.py" 2>/dev/null | wc -l)
        if [[ $models -gt 0 ]]; then
            infra_score=$((infra_score + 30))
            echo "    ✅ 永続化モデル: ${models} 個"
        else
            infra_issues+=("永続化モデルが見つかりません")
            echo "    ⚠️ 永続化モデル: 見つかりません"
        fi

        # Check mappers
        local mappers=$(find src/infrastructure -name "*mapper*.py" -o -name "*convert*.py" 2>/dev/null | wc -l)
        if [[ $mappers -gt 0 ]]; then
            infra_score=$((infra_score + 30))
            echo "    ✅ マッパー: ${mappers} 個"
        else
            infra_issues+=("マッパークラスが見つかりません")
            echo "    ⚠️ マッパー: 見つかりません"
        fi
    else
        infra_issues+=("インフラストラクチャ層のディレクトリが存在しません")
    fi

    jq --argjson score "$infra_score" --argjson issues "$(printf '%s\n' "${infra_issues[@]}" | jq -R . | jq -s .)" \
       '.layers.infrastructure = {"score": $score, "max_score": 100, "issues": $issues}' \
       "$arch_review_report" > "${arch_review_report}.tmp" && mv "${arch_review_report}.tmp" "$arch_review_report"

    echo "  🌐 プレゼンテーション層をレビュー中..."

    # Presentation Layer Review
    local pres_score=0
    local pres_issues=()

    if [[ -d "src/presentation" ]]; then
        # Check controllers/endpoints
        local controllers=$(find src/presentation -name "*controller*.py" -o -name "*endpoint*.py" -o -name "*api*.py" 2>/dev/null | wc -l)
        if [[ $controllers -gt 0 ]]; then
            pres_score=$((pres_score + 30))
            echo "    ✅ コントローラー/エンドポイント: ${controllers} 個"
        else
            pres_issues+=("コントローラーが見つかりません")
            echo "    ⚠️ コントローラー: 見つかりません"
        fi

        # Check validators
        local validators=$(find src/presentation -name "*valid*.py" 2>/dev/null | wc -l)
        if [[ $validators -gt 0 ]]; then
            pres_score=$((pres_score + 35))
            echo "    ✅ バリデーター: ${validators} 個"
        else
            pres_issues+=("入力バリデーターが見つかりません")
            echo "    ⚠️ バリデーター: 見つかりません"
        fi

        # Check serializers
        local serializers=$(find src/presentation -name "*serial*.py" -o -name "*format*.py" 2>/dev/null | wc -l)
        if [[ $serializers -gt 0 ]]; then
            pres_score=$((pres_score + 35))
            echo "    ✅ シリアライザー: ${serializers} 個"
        else
            pres_issues+=("レスポンスシリアライザーが見つかりません")
            echo "    ⚠️ シリアライザー: 見つかりません"
        fi
    else
        pres_issues+=("プレゼンテーション層のディレクトリが存在しません")
    fi

    jq --argjson score "$pres_score" --argjson issues "$(printf '%s\n' "${pres_issues[@]}" | jq -R . | jq -s .)" \
       '.layers.presentation = {"score": $score, "max_score": 100, "issues": $issues}' \
       "$arch_review_report" > "${arch_review_report}.tmp" && mv "${arch_review_report}.tmp" "$arch_review_report"

    # Calculate total architecture score
    total_score=$(jq '[.layers[] | .score] | add / 4' "$arch_review_report")

    # Add violations to report
    jq --argjson violations "$(printf '%s\n' "${violations[@]}" | jq -R . | jq -s .)" \
       --argjson total_score "$total_score" \
       '.violations = $violations | .architecture_score = $total_score' \
       "$arch_review_report" > "${arch_review_report}.tmp" && mv "${arch_review_report}.tmp" "$arch_review_report"

    echo "🏗️ アーキテクチャスコア: ${total_score}/100"

    echo "$arch_review_report"
}

architecture_review=$(conduct_architecture_review)
```

## 5. **Comprehensive Quality Analysis**

```bash
# Perform detailed code quality and test analysis
echo "🔍 コード品質とテスト分析を実行中..."

conduct_quality_analysis() {
    local quality_report="$review_workspace/quality_analysis.json"

    # Initialize quality analysis
    cat > "$quality_report" << EOF
{
  "analysis_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "metrics": {},
  "quality_score": 0,
  "issues": [],
  "recommendations": []
}
EOF

    local quality_score=0
    local quality_issues=()

    echo "  🧪 テストカバレッジを分析中..."

    # Test Coverage Analysis
    local coverage_file="$review_workspace/coverage_results.json"
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=json:"$coverage_file" --cov-report=term-missing tests/ > "$review_workspace/coverage_output.txt" 2>&1; then
        if [[ -f "$coverage_file" ]]; then
            local coverage_percent=$(jq -r '.totals.percent_covered' "$coverage_file")
            jq --argjson coverage "$coverage_percent" '.metrics.test_coverage = $coverage' "$quality_report" > "${quality_report}.tmp" && mv "${quality_report}.tmp" "$quality_report"

            if (( $(echo "$coverage_percent >= 80" | bc -l) )); then
                quality_score=$((quality_score + 30))
                echo "    ✅ テストカバレッジ: ${coverage_percent}% (目標: 80%以上)"
            else
                quality_issues+=("テストカバレッジが基準値を下回っています: ${coverage_percent}%")
                echo "    ⚠️ テストカバレッジ: ${coverage_percent}% (目標: 80%以上)"
            fi
        else
            quality_issues+=("カバレッジレポートの生成に失敗しました")
            echo "    ❌ カバレッジ測定: 失敗"
        fi
    else
        quality_issues+=("テスト実行が失敗しました")
        echo "    ❌ テスト実行: 失敗"
    fi

    echo "  🧹 コード品質（Ruff）を分析中..."

    # Ruff Analysis
    local ruff_results="$review_workspace/ruff_results.json"
    if uv run --frozen ruff check . --output-format=json > "$ruff_results" 2>/dev/null; then
        local ruff_errors=$(jq '. | length' "$ruff_results")
        jq --argjson errors "$ruff_errors" '.metrics.ruff_errors = $errors' "$quality_report" > "${quality_report}.tmp" && mv "${quality_report}.tmp" "$quality_report"

        if [[ $ruff_errors -eq 0 ]]; then
            quality_score=$((quality_score + 25))
            echo "    ✅ Ruff検査: エラーなし"
        elif [[ $ruff_errors -le 5 ]]; then
            quality_score=$((quality_score + 15))
            quality_issues+=("軽微なRuffエラーがあります: ${ruff_errors}件")
            echo "    ⚠️ Ruff検査: ${ruff_errors}件の軽微なエラー"
        else
            quality_issues+=("多数のRuffエラーがあります: ${ruff_errors}件")
            echo "    ❌ Ruff検査: ${ruff_errors}件のエラー"
        fi
    else
        quality_issues+=("Ruff分析の実行に失敗しました")
        echo "    ❌ Ruff検査: 実行失敗"
    fi

    echo "  📝 型チェック（Pyright）を分析中..."

    # Pyright Analysis
    local pyright_results="$review_workspace/pyright_results.json"
    if uv run --frozen pyright --outputjson > "$pyright_results" 2>/dev/null; then
        local pyright_errors=$(jq '.summary.errorCount // 0' "$pyright_results")
        jq --argjson errors "$pyright_errors" '.metrics.pyright_errors = $errors' "$quality_report" > "${quality_report}.tmp" && mv "${quality_report}.tmp" "$quality_report"

        if [[ $pyright_errors -eq 0 ]]; then
            quality_score=$((quality_score + 25))
            echo "    ✅ Pyright検査: エラーなし"
        elif [[ $pyright_errors -le 3 ]]; then
            quality_score=$((quality_score + 15))
            quality_issues+=("軽微な型エラーがあります: ${pyright_errors}件")
            echo "    ⚠️ Pyright検査: ${pyright_errors}件の軽微なエラー"
        else
            quality_issues+=("多数の型エラーがあります: ${pyright_errors}件")
            echo "    ❌ Pyright検査: ${pyright_errors}件のエラー"
        fi
    else
        quality_issues+=("Pyright分析の実行に失敗しました")
        echo "    ❌ Pyright検査: 実行失敗"
    fi

    echo "  🧮 複雑度を分析中..."

    # Complexity Analysis (simplified - counting large functions)
    local complex_functions=$(find src/ -name "*.py" -exec grep -l "def.*(" {} \; | xargs -I {} sh -c 'wc -l < "$1"' _ {} | awk '$1 > 50' | wc -l)
    jq --argjson complex "$complex_functions" '.metrics.complex_functions = $complex' "$quality_report" > "${quality_report}.tmp" && mv "${quality_report}.tmp" "$quality_report"

    if [[ $complex_functions -eq 0 ]]; then
        quality_score=$((quality_score + 20))
        echo "    ✅ 複雑度: 適切（大きな関数なし）"
    elif [[ $complex_functions -le 2 ]]; then
        quality_score=$((quality_score + 10))
        quality_issues+=("一部の関数が大きすぎます: ${complex_functions}個")
        echo "    ⚠️ 複雑度: ${complex_functions}個の大きな関数"
    else
        quality_issues+=("多数の関数が大きすぎます: ${complex_functions}個")
        echo "    ❌ 複雑度: ${complex_functions}個の大きな関数"
    fi

    # Update quality score and issues
    jq --argjson score "$quality_score" \
       --argjson issues "$(printf '%s\n' "${quality_issues[@]}" | jq -R . | jq -s .)" \
       '.quality_score = $score | .issues = $issues' \
       "$quality_report" > "${quality_report}.tmp" && mv "${quality_report}.tmp" "$quality_report"

    echo "📊 品質スコア: ${quality_score}/100"

    echo "$quality_report"
}

quality_analysis=$(conduct_quality_analysis)
```

## 6. **Given-When-Then Scenario Verification**

```bash
# Verify Given-When-Then scenario implementation
echo "📋 Given-When-Thenシナリオ実装を検証中..."

verify_scenario_implementation() {
    local scenario_report="$review_workspace/scenario_verification.json"

    # Initialize scenario verification
    cat > "$scenario_report" << EOF
{
  "verification_date": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "feature": "$feature_name",
  "scenarios": {},
  "implementation_score": 0,
  "coverage_by_scenario": {}
}
EOF

    local implementation_score=0

    echo "  📄 ユースケース仕様からシナリオを抽出中..."

    if [[ -f "$spec_file" ]]; then
        # Extract scenarios from spec file
        local scenarios_count=$(grep -c "Given.*When.*Then" "$spec_file" 2>/dev/null || echo "0")

        if [[ $scenarios_count -gt 0 ]]; then
            echo "    📋 発見されたシナリオ: ${scenarios_count}個"

            # Extract scenario details
            local scenario_lines=""
            while IFS= read -r line; do
                if [[ "$line" =~ Given.*When.*Then ]] || [[ "$line" =~ - Given ]] || [[ "$line" =~ - When ]] || [[ "$line" =~ - Then ]]; then
                    scenario_lines+="$line\n"
                fi
            done < "$spec_file"

            jq --arg scenarios "$scenario_lines" --argjson count "$scenarios_count" \
               '.scenarios.spec_scenarios = $scenarios | .scenarios.count = $count' \
               "$scenario_report" > "${scenario_report}.tmp" && mv "${scenario_report}.tmp" "$scenario_report"

            implementation_score=$((implementation_score + 30))
        else
            echo "    ⚠️ 仕様書にGiven-When-Thenシナリオが見つかりません"
        fi

        echo "  🧪 対応するテストを確認中..."

        # Check corresponding tests
        local test_scenarios=$(find tests/ -name "*.py" -exec grep -l "test.*given\|test.*when\|test.*then" {} \; 2>/dev/null | wc -l)

        if [[ $test_scenarios -gt 0 ]]; then
            jq --argjson test_count "$test_scenarios" '.scenarios.test_scenarios = $test_count' "$scenario_report" > "${scenario_report}.tmp" && mv "${scenario_report}.tmp" "$scenario_report"
            implementation_score=$((implementation_score + 40))
            echo "    ✅ シナリオベーステスト: ${test_scenarios}ファイル"
        else
            echo "    ⚠️ Given-When-Thenテストパターンが見つかりません"
        fi

        echo "  🎯 E2Eテストでシナリオカバレッジを確認中..."

        # Check E2E test coverage for scenarios
        local e2e_tests=$(find tests/e2e -name "*.py" 2>/dev/null | wc -l)

        if [[ $e2e_tests -gt 0 ]]; then
            jq --argjson e2e_count "$e2e_tests" '.scenarios.e2e_tests = $e2e_count' "$scenario_report" > "${scenario_report}.tmp" && mv "${scenario_report}.tmp" "$scenario_report"
            implementation_score=$((implementation_score + 30))
            echo "    ✅ E2Eテスト: ${e2e_tests}ファイル"
        else
            echo "    ⚠️ E2Eテストが見つかりません"
        fi
    else
        echo "    ❌ ユースケース仕様書が見つかりません"
    fi

    # Update implementation score
    jq --argjson score "$implementation_score" '.implementation_score = $score' "$scenario_report" > "${scenario_report}.tmp" && mv "${scenario_report}.tmp" "$scenario_report"

    echo "📋 シナリオ実装スコア: ${implementation_score}/100"

    echo "$scenario_report"
}

scenario_verification=$(verify_scenario_implementation)
```

## 7. **Comprehensive Review Report Generation**

```bash
# Generate detailed review report
echo "📋 包括的レビューレポートを生成中..."

generate_review_report() {
    local review_report_file="docs/review/issue-${issue_list}-${feature_name}-review.md"
    mkdir -p "$(dirname "$review_report_file")"

    # Get reviewer information
    local reviewer=$(git config user.name 2>/dev/null || echo "Unknown Reviewer")
    local review_date=$(date)

    # Extract scores and metrics
    local completeness_score=$(jq -r '.completeness_score' "$artifacts_analysis")
    local architecture_score=$(jq -r '.architecture_score' "$architecture_review")
    local quality_score=$(jq -r '.quality_score' "$quality_analysis")
    local scenario_score=$(jq -r '.implementation_score' "$scenario_verification")

    # Calculate overall score
    local overall_score=$(echo "scale=1; ($completeness_score + $architecture_score + $quality_score + $scenario_score) / 4" | bc)

    # Get specific metrics
    local test_coverage=$(jq -r '.metrics.test_coverage // "N/A"' "$quality_analysis")
    local ruff_errors=$(jq -r '.metrics.ruff_errors // "N/A"' "$quality_analysis")
    local pyright_errors=$(jq -r '.metrics.pyright_errors // "N/A"' "$quality_analysis")
    local complex_functions=$(jq -r '.metrics.complex_functions // "N/A"' "$quality_analysis")

    cat > "$review_report_file" << EOF
# レビューレポート: ${feature_name}

## 基本情報
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **レビュー実行者**: ${reviewer}
- **レビュー日時**: ${review_date}
- **総合スコア**: ${overall_score}/100

## 📊 評価サマリー

| 評価項目 | スコア | 評価 |
|---------|--------|------|
| 成果物完成度 | ${completeness_score}/100 | $(if (( $(echo "$completeness_score >= 80" | bc -l) )); then echo "✅ 良好"; elif (( $(echo "$completeness_score >= 60" | bc -l) )); then echo "⚠️ 要改善"; else echo "❌ 不十分"; fi) |
| アーキテクチャ | ${architecture_score}/100 | $(if (( $(echo "$architecture_score >= 80" | bc -l) )); then echo "✅ 良好"; elif (( $(echo "$architecture_score >= 60" | bc -l) )); then echo "⚠️ 要改善"; else echo "❌ 不十分"; fi) |
| コード品質 | ${quality_score}/100 | $(if (( $(echo "$quality_score >= 80" | bc -l) )); then echo "✅ 良好"; elif (( $(echo "$quality_score >= 60" | bc -l) )); then echo "⚠️ 要改善"; else echo "❌ 不十分"; fi) |
| シナリオ実装 | ${scenario_score}/100 | $(if (( $(echo "$scenario_score >= 80" | bc -l) )); then echo "✅ 良好"; elif (( $(echo "$scenario_score >= 60" | bc -l) )); then echo "⚠️ 要改善"; else echo "❌ 不十分"; fi) |

## 📋 実装成果物の確認

### ドキュメント
$(jq -r '.artifacts | to_entries[] | if .value.exists then "- [x] " + (.key | gsub("_"; " ")) + ": " + (.value.path // "存在") else "- [ ] " + (.key | gsub("_"; " ")) + ": " + (.value.issue // "見つかりません") end' "$artifacts_analysis")

### 実装レイヤー
$(jq -r '.layers | to_entries[] | if .value.score > 50 then "- [x] " + (.key | gsub("_"; " ")) + "層: スコア " + (.value.score | tostring) + "/100" else "- [ ] " + (.key | gsub("_"; " ")) + "層: スコア " + (.value.score | tostring) + "/100 (要改善)" end' "$architecture_review")

## 🏗️ アーキテクチャ準拠性

### DDD原則
- $(if (( $(echo "$architecture_score >= 80" | bc -l) )); then echo "[x]"; else echo "[ ]"; fi) ユビキタス言語の一貫性
- $(if jq -e '.layers.domain.score >= 75' "$architecture_review" >/dev/null; then echo "[x]"; else echo "[ ]"; fi) 集約境界の適切性
- $(if jq -e '.violations | length == 0' "$architecture_review" >/dev/null; then echo "[x]"; else echo "[ ]"; fi) ドメインロジックの純粋性
- $(if jq -e '.layers.domain.score >= 75' "$architecture_review" >/dev/null; then echo "[x]"; else echo "[ ]"; fi) 値オブジェクトの適切な使用

### レイヤードアーキテクチャ
- $(if jq -e '.violations | length == 0' "$architecture_review" >/dev/null; then echo "[x]"; else echo "[ ]"; fi) レイヤー間の依存方向
- $(if jq -e '.layers | [.[] | .score] | add / length >= 70' "$architecture_review" >/dev/null; then echo "[x]"; else echo "[ ]"; fi) 関心の分離
- $(if (( $(echo "$architecture_score >= 70" | bc -l) )); then echo "[x]"; else echo "[ ]"; fi) 依存性注入の活用

### TDD実践
- $(if (( $(echo "$scenario_score >= 70" | bc -l) )); then echo "[x]"; else echo "[ ]"; fi) Given-When-Thenシナリオの実装
- $(if (( $(echo "$test_coverage >= 80" | bc -l) )); then echo "[x]"; else echo "[ ]"; fi) テストカバレッジ: ${test_coverage}%
- $(if [[ "$ruff_errors" == "0" && "$pyright_errors" == "0" ]]; then echo "[x]"; else echo "[ ]"; fi) コード品質基準の達成

## 📈 品質メトリクス

| メトリクス | 結果 | 基準 | 評価 |
|-----------|------|------|------|
| テストカバレッジ | ${test_coverage}% | >80% | $(if (( $(echo "$test_coverage >= 80" | bc -l) )); then echo "✅"; else echo "❌"; fi) |
| Ruffエラー数 | ${ruff_errors} | 0 | $(if [[ "$ruff_errors" == "0" ]]; then echo "✅"; elif [[ "$ruff_errors" -le 5 ]]; then echo "⚠️"; else echo "❌"; fi) |
| Pyrightエラー数 | ${pyright_errors} | 0 | $(if [[ "$pyright_errors" == "0" ]]; then echo "✅"; elif [[ "$pyright_errors" -le 3 ]]; then echo "⚠️"; else echo "❌"; fi) |
| 複雑な関数数 | ${complex_functions} | 0 | $(if [[ "$complex_functions" == "0" ]]; then echo "✅"; elif [[ "$complex_functions" -le 2 ]]; then echo "⚠️"; else echo "❌"; fi) |

## 🔍 改善提案

### 必須対応項目（高優先度）
EOF

    # Add high priority issues
    jq -r '.issues[]?' "$quality_analysis" | while IFS= read -r issue; do
        echo "1. $issue" >> "$review_report_file"
    done

    jq -r '.violations[]?' "$architecture_review" | while IFS= read -r violation; do
        echo "2. $violation" >> "$review_report_file"
    done

    cat >> "$review_report_file" << EOF

### 推奨改善項目（中優先度）
EOF

    # Add medium priority recommendations
    if (( $(echo "$completeness_score < 80" | bc -l) )); then
        echo "1. ドキュメント成果物の完成度向上" >> "$review_report_file"
    fi

    if (( $(echo "$architecture_score < 80" | bc -l) )); then
        echo "2. アーキテクチャ準拠性の改善" >> "$review_report_file"
    fi

    cat >> "$review_report_file" << EOF

### 将来的な改善案（低優先度）
1. パフォーマンス最適化の検討
2. 追加テストシナリオの実装
3. ドキュメントの充実

## 📋 Given-When-Thenシナリオ実装状況

| シナリオ分類 | 数量 | 実装状況 | 評価 |
|-------------|------|----------|------|
| 仕様書シナリオ | $(jq -r '.scenarios.count // 0' "$scenario_verification") | $(if jq -e '.scenarios.count > 0' "$scenario_verification" >/dev/null; then echo "実装済み"; else echo "要確認"; fi) | $(if jq -e '.scenarios.count > 0' "$scenario_verification" >/dev/null; then echo "✅"; else echo "⚠️"; fi) |
| テストシナリオ | $(jq -r '.scenarios.test_scenarios // 0' "$scenario_verification") | $(if jq -e '.scenarios.test_scenarios > 0' "$scenario_verification" >/dev/null; then echo "実装済み"; else echo "要実装"; fi) | $(if jq -e '.scenarios.test_scenarios > 0' "$scenario_verification" >/dev/null; then echo "✅"; else echo "❌"; fi) |
| E2Eテスト | $(jq -r '.scenarios.e2e_tests // 0' "$scenario_verification") | $(if jq -e '.scenarios.e2e_tests > 0' "$scenario_verification" >/dev/null; then echo "実装済み"; else echo "要実装"; fi) | $(if jq -e '.scenarios.e2e_tests > 0' "$scenario_verification" >/dev/null; then echo "✅"; else echo "❌"; fi) |

## 🎯 総評

$(if (( $(echo "$overall_score >= 80" | bc -l) )); then
echo "**✅ 優秀**: 実装品質は基準を満たしており、本番環境への展開準備が整っています。"
elif (( $(echo "$overall_score >= 70" | bc -l) )); then
echo "**⚠️ 良好**: 実装品質は概ね良好ですが、いくつかの改善項目があります。"
elif (( $(echo "$overall_score >= 60" | bc -l) )); then
echo "**📋 要改善**: 実装品質に改善が必要な項目があります。対応後に再レビューを推奨します。"
else
echo "**❌ 不十分**: 実装品質が基準を大きく下回っています。包括的な改善が必要です。"
fi)

### 次のステップ
$(if (( $(echo "$overall_score >= 80" | bc -l) )); then
echo "1. 軽微な調整があれば対応"
echo "2. 本番展開の準備"
echo "3. ドキュメントの最終確認"
else
echo "1. 高優先度項目の対応: /apply-feedback $(IFS=','; echo "${issue_numbers[*]}")"
echo "2. 改善後の再レビュー実施"
echo "3. 品質基準達成まで反復"
fi)

## 📊 詳細分析レポート

- **成果物分析**: \`${artifacts_analysis}\`
- **アーキテクチャレビュー**: \`${architecture_review}\`
- **品質分析**: \`${quality_analysis}\`
- **シナリオ検証**: \`${scenario_verification}\`

---

**レビュー実行者**: ${reviewer}
**レビュー完了日時**: ${review_date}
EOF

    echo "✅ レビューレポート生成完了: $review_report_file"
    echo "$review_report_file"
}

review_report_file=$(generate_review_report)
```

## 8. **Atomic Metadata Update**

```bash
# Update metadata with review results
echo "📊 メタデータを原子的に更新中..."

if [[ -f "$metadata_file" ]]; then
    # Get reviewer information
    reviewer=$(git config user.name 2>/dev/null || echo "Unknown Reviewer")

    # Calculate overall score
    completeness_score=$(jq -r '.completeness_score' "$artifacts_analysis")
    architecture_score=$(jq -r '.architecture_score' "$architecture_review")
    quality_score=$(jq -r '.quality_score' "$quality_analysis")
    scenario_score=$(jq -r '.implementation_score' "$scenario_verification")
    overall_score=$(echo "scale=1; ($completeness_score + $architecture_score + $quality_score + $scenario_score) / 4" | bc)

    # Update metadata atomically
    update_metadata_atomic "$metadata_file" "
        .phases.review.reviewed = true |
        .phases.review.reviewed_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.review.reviewer = \"$reviewer\" |
        .phases.review.overall_score = $overall_score |
        .phases.review.completeness_score = $completeness_score |
        .phases.review.architecture_score = $architecture_score |
        .phases.review.quality_score = $quality_score |
        .phases.review.scenario_score = $scenario_score |
        .phases.review.review_report = \"$review_report_file\" |
        .phases.review.artifacts_analysis = \"$artifacts_analysis\" |
        .phases.review.architecture_review = \"$architecture_review\" |
        .phases.review.quality_analysis = \"$quality_analysis\" |
        .phases.review.scenario_verification = \"$scenario_verification\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"reviewed\"
    "

    echo "✅ メタデータ更新完了"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 9. **GitHub Issue Updates and Use Case Index**

```bash
# Update GitHub issues with review results
echo "📢 GitHub イシューとインデックスを更新中..."

# Create comprehensive review summary for GitHub
github_review_summary="🔍 **包括的レビュー完了**

📊 **評価サマリー**:
- 総合スコア: ${overall_score}/100
- 成果物完成度: ${completeness_score}/100
- アーキテクチャ: ${architecture_score}/100
- コード品質: ${quality_score}/100
- シナリオ実装: ${scenario_score}/100

📈 **品質メトリクス**:
- テストカバレッジ: $(jq -r '.metrics.test_coverage // "N/A"' "$quality_analysis")%
- Ruffエラー: $(jq -r '.metrics.ruff_errors // "N/A"' "$quality_analysis")件
- Pyrightエラー: $(jq -r '.metrics.pyright_errors // "N/A"' "$quality_analysis")件

🏗️ **アーキテクチャ評価**:
$(jq -r '.layers | to_entries[] | "- " + (.key | gsub("_"; " ")) + "層: " + (.value.score | tostring) + "/100"' "$architecture_review")

$(if (( $(echo "$overall_score >= 80" | bc -l) )); then
echo "✅ **評価**: 優秀 - 本番展開準備完了"
elif (( $(echo "$overall_score >= 70" | bc -l) )); then
echo "⚠️ **評価**: 良好 - 軽微な改善推奨"
elif (( $(echo "$overall_score >= 60" | bc -l) )); then
echo "📋 **評価**: 要改善 - フィードバック対応必須"
else
echo "❌ **評価**: 不十分 - 包括的改善が必要"
fi)

📋 **詳細レポート**: \`${review_report_file}\`

🔍 **次のステップ**: $(if (( $(echo "$overall_score >= 80" | bc -l) )); then echo "軽微調整後に本番展開可能"; else echo "/apply-feedback コマンドで改善項目に対応"; fi)"

# Update GitHub issues
for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$github_review_summary"; then
        echo "✅ Issue #$issue_num にレビュー結果を報告"
    else
        echo "⚠️ 警告: Issue #$issue_num への報告に失敗"
    fi
done

# Update use case index
if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"
    test_coverage=$(jq -r '.metrics.test_coverage // "N/A"' "$quality_analysis")

    # Create comprehensive status
    status_icon="✅"
    if (( $(echo "$overall_score < 80" | bc -l) )); then
        if (( $(echo "$overall_score >= 60" | bc -l) )); then
            status_icon="⚠️"
        else
            status_icon="❌"
        fi
    fi

    # Update with comprehensive review information
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: reviewed, Score: ${overall_score}/100, Coverage: ${test_coverage}%, Status: ${status_icon})|" docs/use_cases/index.md

    echo "✅ ユースケースインデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 10. **Transaction Commit and Summary**

```bash
# Commit transaction and provide comprehensive summary
echo "💾 レビュー結果をコミット中..."

# Add all created files to git
git add -A

# Create comprehensive commit message
commit_message="docs: comprehensive review for issues #$(IFS=' #'; echo "${issue_numbers[*]}")

Feature: ${feature_name}
Overall Score: ${overall_score}/100

Review Results:
- Completeness: ${completeness_score}/100
- Architecture: ${architecture_score}/100
- Code Quality: ${quality_score}/100
- Scenario Implementation: ${scenario_score}/100

Quality Metrics:
- Test Coverage: $(jq -r '.metrics.test_coverage // "N/A"' "$quality_analysis")%
- Ruff Errors: $(jq -r '.metrics.ruff_errors // "N/A"' "$quality_analysis")
- Pyright Errors: $(jq -r '.metrics.pyright_errors // "N/A"' "$quality_analysis")

Generated Reports:
- Review Report: ${review_report_file}
- Analysis Reports: ${review_workspace}

Reviewer: $(git config user.name 2>/dev/null || echo "Unknown")"

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
echo "🎉 包括的レビュー完了!"
echo ""
echo "📊 **レビューサマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - Reviewer: $(git config user.name 2>/dev/null || echo "Unknown")"
echo "   - 総合スコア: ${overall_score}/100"
echo ""
echo "📈 **詳細評価**:"
echo "   - 成果物完成度: ${completeness_score}/100"
echo "   - アーキテクチャ: ${architecture_score}/100"
echo "   - コード品質: ${quality_score}/100"
echo "   - シナリオ実装: ${scenario_score}/100"
echo ""
echo "🔍 **品質メトリクス**:"
echo "   - テストカバレッジ: $(jq -r '.metrics.test_coverage // "N/A"' "$quality_analysis")%"
echo "   - Ruffエラー: $(jq -r '.metrics.ruff_errors // "N/A"' "$quality_analysis")件"
echo "   - Pyrightエラー: $(jq -r '.metrics.pyright_errors // "N/A"' "$quality_analysis")件"
echo "   - 複雑関数: $(jq -r '.metrics.complex_functions // "N/A"' "$quality_analysis")個"
echo ""
echo "📋 **生成されたリソース**:"
echo "   - 📄 レビューレポート: ${review_report_file}"
echo "   - 📊 分析データ: ${review_workspace}/"
echo ""
echo "🎯 **評価結果**:"

if (( $(echo "$overall_score >= 80" | bc -l) )); then
    echo "   ✅ 優秀: 本番環境への展開準備が整っています"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🚀 本番展開: 準備完了"
    echo "   - 📋 最終確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🎯 PR作成: /create-pr $(IFS=','; echo "${issue_numbers[*]}")"
elif (( $(echo "$overall_score >= 70" | bc -l) )); then
    echo "   ⚠️ 良好: 軽微な改善後に展開可能"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 📋 改善実施: /apply-feedback $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🔄 再レビュー: 改善後に実施"
    echo "   - 📊 進捗確認: /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
elif (( $(echo "$overall_score >= 60" | bc -l) )); then
    echo "   📋 要改善: フィードバック対応が必要"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🚨 必須対応: /apply-feedback $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🔄 改善実装: 高優先度項目から順次対応"
    echo "   - 📊 進捗追跡: 定期的な状況確認"
else
    echo "   ❌ 不十分: 包括的な改善が必要"
    echo ""
    echo "🔍 **次のステップ**:"
    echo "   - 🚨 緊急対応: /apply-feedback $(IFS=','; echo "${issue_numbers[*]}")"
    echo "   - 🔄 全面改善: アーキテクチャから見直し"
    echo "   - 👥 チーム相談: 改善戦略の検討"
fi

echo ""
echo "✅ 包括的レビュープロセスが正常に完了しました"
```

## 重要な注意事項

### **包括的品質評価**

- 成果物・アーキテクチャ・品質・シナリオの 4 軸による多角的評価
- 定量的メトリクスによる客観的な品質判定
- DDD/Clean Architecture 原則の自動検証
- Given-When-Then シナリオの実装状況確認

### **安全性保証**

- 全レビュープロセスでのトランザクション管理
- 詳細な分析データのバックアップと保護
- エラー時の安全な状態復旧
- レビュー結果の完全なトレーサビリティ

### **実用性とチーム協力**

- 優先度付きの具体的改善提案
- GitHub イシューとの完全連携
- 次のステップの明確な指示
- レビュー結果の包括的可視化

**統合版レビューコマンドにより、確実で包括的な品質保証レビューが実現されます！**

## 🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK

レビュー中に新課題・改善点・要件変更発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: レビューは品質向上と新要件発見の重要な機会です
