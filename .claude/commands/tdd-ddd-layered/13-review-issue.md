Review TDD/DDD/Layered Architecture implementation with comprehensive analysis.

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

#### **💻 Code Quality Assessment**
- [ ] **Run static analysis**: Execute `uv run --frozen ruff check src/` and analyze results
- [ ] **Check formatting compliance**: Verify `uv run --frozen ruff format src/` shows no changes
- [ ] **Validate type annotations**: Run `uv run --frozen pyright src/` and review type coverage
- [ ] **Assess code complexity**: Identify overly complex methods and classes
- [ ] **Review naming conventions**: Evaluate variable, method, and class naming clarity
- [ ] **Check code duplication**: Identify and assess duplicate code patterns

#### **🔗 Integration Quality Review**
- [ ] **Test repository implementations**: Verify data access patterns and error handling
- [ ] **Review external service integration**: Assess third-party service integration patterns
- [ ] **Validate configuration management**: Review environment and configuration handling
- [ ] **Check error propagation**: Ensure errors are properly handled across layers
- [ ] **Assess transaction management**: Review database transaction patterns
- [ ] **Validate monitoring and logging**: Check observability implementation

#### **🌐 Presentation Layer Review**
- [ ] **Validate API design**: Review REST endpoint design and HTTP status codes
- [ ] **Check input validation**: Assess request validation and error response quality
- [ ] **Review authentication/authorization**: Evaluate security implementation
- [ ] **Assess response formatting**: Check response structure and error handling
- [ ] **Validate API documentation**: Review endpoint documentation quality
- [ ] **Check CLI usability**: Evaluate command-line interface user experience

#### **🚀 Performance and Scalability Assessment**
- [ ] **Identify performance bottlenecks**: Review slow code paths and database queries
- [ ] **Assess memory usage**: Check for memory leaks and inefficient data structures
- [ ] **Review caching strategies**: Evaluate caching implementation where applicable
- [ ] **Check database optimization**: Review query performance and indexing
- [ ] **Assess scalability patterns**: Evaluate code scalability and concurrency handling
- [ ] **Review resource management**: Check proper resource cleanup and disposal

#### **🔒 Security Review**
- [ ] **Validate input sanitization**: Check protection against injection attacks
- [ ] **Review authentication implementation**: Assess login/logout security
- [ ] **Check authorization patterns**: Evaluate access control implementation
- [ ] **Assess data protection**: Review sensitive data handling and storage
- [ ] **Validate configuration security**: Check for exposed secrets or credentials
- [ ] **Review error information disclosure**: Ensure errors don't leak sensitive data

#### **📚 Documentation Quality Review**
- [ ] **Review code documentation**: Assess docstring quality and completeness
- [ ] **Validate API documentation**: Check endpoint documentation accuracy
- [ ] **Assess architecture documentation**: Review system design documentation
- [ ] **Check setup instructions**: Validate project setup and development guides
- [ ] **Review decision records**: Assess architectural decision documentation
- [ ] **Evaluate user documentation**: Check end-user facing documentation

#### **📊 Business Value Assessment**
- [ ] **Validate requirement fulfillment**: Confirm all business requirements are met
- [ ] **Assess user experience**: Evaluate end-user interaction quality
- [ ] **Review business rule implementation**: Verify business logic correctness
- [ ] **Check acceptance criteria satisfaction**: Ensure all criteria are met
- [ ] **Validate edge case handling**: Confirm proper handling of business edge cases
- [ ] **Assess maintainability for business**: Evaluate ease of future business changes

**💡 Pro Tip**: Focus on Given-When-Then traceability - every business scenario should have clear test coverage demonstrating the expected behavior!

## Task Details

**Agent Integration Pattern - 4 Steps:**

1. **Pre-execution Validation**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "13-review-issue" "$ARGUMENTS"
   
   # Validate issue number requirement
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       show_usage_example "review-issue" "1" "単一イシューの実装レビュー"
       show_usage_example "review-issue" "1,7" "複数イシューの実装レビュー"
       show_usage_example "review-issue" "1,feature-name" "イシュー + フィーチャー指定"
       exit 1
   fi
   
   # Discover feature name and metadata
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Extract feature name from use case file
       feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
       if [[ -z "$feature_name" ]]; then
           echo "❌ エラー: フィーチャー名を特定できませんでした"
           echo "💡 使用方法: /review-issue $issue_list,<feature-name>"
           exit 1
       fi
   fi
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   echo "🔍 Issues: #$(IFS=' #'; echo "${issue_numbers[*]}") - ${feature_name} の実装レビューを開始します"
   echo "✅ 前提条件確認完了: 実装レビュー準備完了"
   ```

2. **Execute Specialized Agent**:
   ```bash
   # 🤖 Call specialized agent with Task tool for implementation review
   echo "🤖 専用エージェント実行中: 13-review-issue"
   
   # Build comprehensive task context
   task_context="Implementation Review Request:
   
   Issues: $(printf '#%s ' "${issue_numbers[@]}")
   Feature: $feature_name
   
   Request: Comprehensive implementation quality review and analysis
   
   COMPREHENSIVE TASK CHECKLIST:
   
   🔴 Required Tasks:
   
   📖 Given-When-Then Specification Coverage Analysis:
   - Map scenarios to tests: verify each Given-When-Then scenario has corresponding tests
   - Validate scenario completeness: ensure all scenarios from issue specification are tested
   - Check scenario accuracy: verify tests accurately implement the specified scenarios
   - Assess acceptance criteria coverage: confirm all acceptance criteria have test validation
   
   🧪 Test Quality Assessment:
   - Analyze test structure: review test organization and naming conventions
   - Evaluate test readability: assess how clearly tests express business intent
   - Check test isolation: verify tests run independently without side effects
   - Validate assertion quality: ensure tests verify behavior, not just implementation
   
   📊 Test Coverage Analysis:
   - Generate coverage reports: execute pytest --cov=src --cov-report=html
   - Analyze line coverage: review code coverage percentages by layer
   - Assess branch coverage: evaluate decision path coverage in business logic
   - Identify coverage gaps: find critical untested code paths
   
   🟡 Recommended Tasks:
   
   🏗️ Architecture Compliance Review:
   - Validate layer separation: ensure clean separation between domain/application/infrastructure/presentation
   - Check dependency directions: verify dependencies point inward (Clean Architecture)
   - Review interface segregation: assess repository interfaces and their implementations
   - Validate domain purity: ensure domain layer has no external dependencies
   - Check aggregate boundaries: review aggregate design and transaction boundaries
   - Assess domain model richness: evaluate business logic placement and organization
   
   🎯 Domain-Driven Design Review:
   - Validate ubiquitous language: check consistency of domain terminology across code
   - Review entity design: assess entity identity, lifecycle, and behavior
   - Evaluate value objects: check immutability, validation, and equality implementation
   - Assess domain services: review complex business logic placement
   
   🟢 Optional Tasks:
   
   📀 Advanced Test Quality Assessment:
   - Review edge case coverage: verify edge cases from scenarios are properly tested
   - Validate error scenario testing: ensure error scenarios have corresponding failure tests
   - Review test data quality: assess test fixtures and data setup appropriateness
   - Check test performance: identify slow tests and performance bottlenecks
   - Review integration coverage: assess cross-layer integration test coverage
   - Validate e2e coverage: ensure complete user scenarios are tested
   
   💻 Code Quality Assessment:
   - Run static analysis: execute ruff check src/ and analyze results
   - Check formatting compliance: verify ruff format src/ shows no changes
   - Validate type annotations: run pyright src/ and review type coverage
   - Assess code complexity: identify overly complex methods and classes
   - Review naming conventions: evaluate variable, method, and class naming clarity
   - Check code duplication: identify and assess duplicate code patterns
   
   🔗 Integration Quality Review:
   - Test repository implementations: verify data access patterns and error handling
   - Review external service integration: assess third-party service integration patterns
   - Validate configuration management: review environment and configuration handling
   - Check error propagation: ensure errors are properly handled across layers
   - Assess transaction management: review database transaction patterns
   - Validate monitoring and logging: check observability implementation
   
   🌐 Presentation Layer Review:
   - Validate API design: review REST endpoint design and HTTP status codes
   - Check input validation: assess request validation and error response quality
   - Review authentication/authorization: evaluate security implementation
   - Assess response formatting: check response structure and error handling
   - Validate API documentation: review endpoint documentation quality
   - Check CLI usability: evaluate command-line interface user experience
   
   🚀 Performance and Scalability Assessment:
   - Identify performance bottlenecks: review slow code paths and database queries
   - Assess memory usage: check for memory leaks and inefficient data structures
   - Review caching strategies: evaluate caching implementation where applicable
   - Check database optimization: review query performance and indexing
   - Assess scalability patterns: evaluate code scalability and concurrency handling
   - Review resource management: check proper resource cleanup and disposal
   
   🔒 Security Review:
   - Validate input sanitization: check protection against injection attacks
   - Review authentication implementation: assess login/logout security
   - Check authorization patterns: evaluate access control implementation
   - Assess data protection: review sensitive data handling and storage
   - Validate configuration security: check for exposed secrets or credentials
   - Review error information disclosure: ensure errors don't leak sensitive data
   
   📚 Documentation Quality Review:
   - Review code documentation: assess docstring quality and completeness
   - Validate API documentation: check endpoint documentation accuracy
   - Assess architecture documentation: review system design documentation
   - Check setup instructions: validate project setup and development guides
   - Review decision records: assess architectural decision documentation
   - Evaluate user documentation: check end-user facing documentation
   
   📊 Business Value Assessment:
   - Validate requirement fulfillment: confirm all business requirements are met
   - Assess user experience: evaluate end-user interaction quality
   - Review business rule implementation: verify business logic correctness
   - Check acceptance criteria satisfaction: ensure all criteria are met
   - Validate edge case handling: confirm proper handling of business edge cases
   - Assess maintainability for business: evaluate ease of future business changes
   
   OUTPUT REQUIREMENTS:
   - Generate comprehensive review report in docs/reviews/
   - Update metadata files with review status and scores
   - Create analysis artifacts in docs/analysis/
   - Focus on quality analysis and assessment only (no code changes)
   - Provide actionable improvement recommendations
   - Maintain full traceability to Given-When-Then scenarios
   - Generate multi-dimensional evaluation scores
   
   CRITICAL SCENARIO EVOLUTION CHECK:
   If new issues, improvements, or requirement changes are discovered during review,
   immediately interrupt the work and execute /evolve-scenarios <feature-name>
   Review is a critical opportunity for quality improvement and new requirement discovery"
   
   # Execute the specialized agent
   claude_task="$task_context" \
       claude_agent="13-review-issue" \
       claude_working_dir="$(pwd)" \
       claude_issues="$(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')" \
       claude_feature_name="$feature_name" \
       claude --agent
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント結果検証中..."
   
   verification_issues=()
   
   # Check that review report was generated
   review_report_pattern="docs/reviews/*issue*${issue_list}*${feature_name}*review*.md"
   review_reports=($(ls $review_report_pattern 2>/dev/null))
   
   if [[ ${#review_reports[@]} -eq 0 ]]; then
       # Try alternative pattern
       review_report_pattern="docs/reviews/*issue*${issue_list}*.md"
       review_reports=($(ls $review_report_pattern 2>/dev/null))
   fi
   
   if [[ ${#review_reports[@]} -eq 0 ]]; then
       verification_issues+=("レビューレポートが作成されていません")
   else
       review_report="${review_reports[-1]}"  # Get most recent
       echo "  ✅ レビューレポート: $(basename "$review_report")"
       
       # Verify report content completeness
       if ! grep -q "総合スコア\|Overall Score" "$review_report"; then
           verification_issues+=("レビューレポートに総合スコアが記載されていません")
       fi
       
       if ! grep -q "アーキテクチャ\|Architecture" "$review_report"; then
           verification_issues+=("アーキテクチャレビューが不完全です")
       fi
   fi
   
   # Check metadata update
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       review_status=$(jq -r '.phases.review.reviewed // false' "$metadata_file" 2>/dev/null)
       if [[ "$review_status" == "true" ]]; then
           overall_score=$(jq -r '.phases.review.overall_score // "N/A"' "$metadata_file" 2>/dev/null)
           echo "  ✅ メタデータ更新完了 (総合スコア: $overall_score/100)"
       else
           verification_issues+=("メタデータ更新が未確認")
       fi
   fi
   
   # Check for analysis artifacts
   analysis_pattern="docs/analysis/*${feature_name}*review*.json"
   if ls $analysis_pattern 2>/dev/null | head -1 >/dev/null; then
       echo "  ✅ 分析データファイル"
   else
       verification_issues+=("分析データファイルが見つかりません")
   fi
   
   # Check agent exit code
   if [[ $agent_exit_code -ne 0 ]]; then
       verification_issues+=("エージェント実行エラー (終了コード: $agent_exit_code)")
   fi
   
   # Report validation results
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
   echo "🎉 実装レビュー完了!"
   echo ""
   echo "📊 実行サマリー:"
   echo "  📂 対象Issues: $(printf '#%s ' "${issue_numbers[@]}")"
   echo "  🏷️ フィーチャー: $feature_name"
   echo "  📝 生成レポート: $review_report"
   echo "  🔄 メタデータ: $metadata_file"
   echo ""
   
   # Show review summary
   if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
       overall_score=$(jq -r '.phases.review.overall_score // "N/A"' "$metadata_file" 2>/dev/null)
       completeness_score=$(jq -r '.phases.review.completeness_score // "N/A"' "$metadata_file" 2>/dev/null)
       architecture_score=$(jq -r '.phases.review.architecture_score // "N/A"' "$metadata_file" 2>/dev/null)
       quality_score=$(jq -r '.phases.review.quality_score // "N/A"' "$metadata_file" 2>/dev/null)
       scenario_score=$(jq -r '.phases.review.scenario_score // "N/A"' "$metadata_file" 2>/dev/null)
       
       echo "🔍 レビューサマリー:"
       echo "   📊 総合スコア: $overall_score/100"
       echo "   📊 成果物完成度: $completeness_score/100"
       echo "   📊 アーキテクチャ: $architecture_score/100"
       echo "   📊 コード品質: $quality_score/100"
       echo "   📊 シナリオ実装: $scenario_score/100"
       
       # Show quality status
       if [[ "$overall_score" != "N/A" ]]; then
           if (( $(echo "$overall_score >= 80" | bc -l 2>/dev/null || echo "0") )); then
               echo "   ✅ 評価: 優秀 - 本番展開準備完了"
               next_step="/create-pr ${issue_numbers[*]}"
           elif (( $(echo "$overall_score >= 70" | bc -l 2>/dev/null || echo "0") )); then
               echo "   ⚠️ 評価: 良好 - 軽微な改善推奨"
               next_step="/apply-feedback ${issue_numbers[*]}"
           elif (( $(echo "$overall_score >= 60" | bc -l 2>/dev/null || echo "0") )); then
               echo "   📋 評価: 要改善 - フィードバック対応必須"
               next_step="/apply-feedback ${issue_numbers[*]}"
           else
               echo "   ❌ 評価: 不十分 - 包括的改善が必要"
               next_step="/apply-feedback ${issue_numbers[*]}"
           fi
       else
           next_step="/apply-feedback ${issue_numbers[*]}"
       fi
   else
       next_step="/apply-feedback ${issue_numbers[*]}"
   fi
   
   echo ""
   echo "📋 次のステップ:"
   echo "   💡 $next_step"
   echo "   💡 /use-case-status $(IFS=','; echo "${issue_numbers[*]}")"
   
   echo ""
   echo "📁 生成ファイル:"
   echo "  📝 レビューレポート: $review_report"
   echo "  🔄 メタデータ: $metadata_file"
   if ls docs/analysis/*${feature_name}*review*.json 2>/dev/null | head -1 >/dev/null; then
       analysis_file=$(ls docs/analysis/*${feature_name}*review*.json 2>/dev/null | head -1)
       echo "  📊 分析データ: $analysis_file"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "🎯 実装レビューが正常に完了しました!"
   ```

**💡 Key Benefits of Implementation Review:**
- **Quality Gate Validation**: Ensure implementation meets quality standards before PR
- **Architecture Compliance**: Validate adherence to DDD/Clean Architecture principles
- **Comprehensive Analysis**: Multi-dimensional evaluation of implementation quality
- **Actionable Feedback**: Generate specific improvement recommendations
- **Scenario Traceability**: Maintain full traceability to Given-When-Then scenarios

**🎯 Critical Success Factors:**
- Focus on Given-When-Then traceability - every business scenario should have clear test coverage
- Validate architecture compliance across all layers
- Ensure comprehensive quality analysis before proceeding to PR
- Generate actionable improvement recommendations
- Maintain focus on analysis only - no code modifications during review

**🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK**

レビュー中に新課題・改善点・要件変更発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: レビューは品質向上と新要件発見の重要な機会です