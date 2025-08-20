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

**🤖 Agent Integration**: This command uses the specialized `13-review-issue` agent for comprehensive implementation review and quality analysis.

Follow these steps:

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 最低1つのイシュー番号が必要です"
       echo "使用例:"
       echo "  /review-issue 15        # 単一イシューレビュー"
       echo "  /review-issue 15,23     # 複数イシューレビュー"
       exit 1
   fi
   
   # Parse issue numbers
   IFS=',' read -ra ISSUES <<< "$1"
   echo "🔍 Issues: $(printf '#%s ' "${ISSUES[@]}")の実装レビューを開始します"
   
   # Check implementation exists
   implementation_found=false
   for issue_num in "${ISSUES[@]}"; do
       if find src/ -name "*${issue_num}*" -type f 2>/dev/null | head -1 >/dev/null; then
           implementation_found=true
           break
       fi
   done
   
   if [[ "$implementation_found" != "true" ]]; then
       echo "❌ 実装ファイルが見つかりません"
       echo "💡 実装完了後にレビューを実行してください"
       exit 1
   fi
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🔍 コンテキスト準備とエージェント起動..."
   
   # Create context file with implementation review information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for implementation review
   cat > "$context_file" <<EOF
   {
     "command": "review-issue",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; printf '%s\n' "${ISSUES[@]}" | paste -sd,)],
     "phase": "implementation-review",
     "context": {
       "expected_outputs": [
         "docs/analysis/quality-report.json",
         "docs/analysis/architecture-review.md",
         "docs/analysis/improvement-recommendations.md"
       ],
       "architecture_patterns": ["DDD", "Clean Architecture", "TDD"]
     },
     "additional_instructions": "実装の包括的品質レビューを実行してください。アーキテクチャ準拠性、コード品質、テストカバレッジ、Given-When-Thenトレーサビリティを詳細に分析し、改善提案を提供してください。TDDサイクル準拠性とClean Architectureの層分離も検証してください。",
     "special_considerations": [
       "DDD/Clean Architectureの原則遵守確認",
       "TDD RED-GREEN-REFACTORサイクル完了検証",
       "Given-When-Thenシナリオとテストの完全トレーサビリティ",
       "層間依存関係と責務分離の厳密な検証"
     ],
     "custom_context": {
       "architecture_compliance": true,
       "code_quality_analysis": true,
       "test_coverage_assessment": true,
       "scenario_traceability": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🔍 実装レビューエージェントを起動します..."
   echo "専門エージェントが包括的品質分析を実行します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   cat <<'AGENT_CALL'
   Task tool will be called with:
   - subagent_type: "13-review-issue"
   - description: "Comprehensive implementation review and quality analysis"
   - prompt: |
     実装レビュータスクを実行してください。
     
     ## コンテキスト情報の取得
     1. 一時コンテキスト（イシュー情報）:
        - /workspace/.claude/context/current-command-context.json を読み込み
     
     2. 実装状況の確認:
        - src/ ディレクトリで実装済みコードを分析
        - tests/ でテストカバレッジとトレーサビリティを確認
        - docs/use_cases/issue-X-Y.json で完了フェーズを確認
     
     ## 実行タスク
     1. アーキテクチャ準拠性分析（DDD/Clean Architecture）
     2. コード品質メトリクスと静的解析
     3. テストカバレッジとGiven-When-Thenトレーサビリティ
     4. TDDサイクル準拠性検証（RED-GREEN-REFACTOR）
     5. 層分離と依存関係検証
     6. ドキュメント完全性レビュー
     7. パフォーマンスとセキュリティの基本チェック
     8. 保守性と技術的負債の評価
     
     ## 処理完了後
     - 品質レポートと改善提案の作成
     - アーキテクチャ遵守状況の詳細報告
     - 次のステップ（フィードバック適用・PR作成）への案内
   AGENT_CALL
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - アーキテクチャ準拠性分析"
   echo "  - コード品質メトリクスと静的解析"
   echo "  - テストカバレッジとGiven-When-Thenトレーサビリティ"
   echo "  - TDD サイクル準拠性検証"
   echo "  - 層分離と依存関係検証"
   echo "  - ドキュメント完全性レビュー"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that review reports were created
   review_files=$(find docs/analysis/ -name "*review*.json" -o -name "*analysis*.md" 2>/dev/null | wc -l)
   
   # Validate review results
   if [[ $review_files -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       echo "  レビューレポートが見つかりません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   echo "  - レビューレポート: ${review_files}個"
   ```

4. **Display Success Summary**:
   ```bash
   # 📊 Display comprehensive success summary
   echo ""
   echo "🎉 実装レビュー完了!"
   echo "==================="
   
   # Show summary information
   echo "📊 レビューサマリー:"
   echo "  🔍 対象Issues: $(printf '#%s ' "${ISSUES[@]}")"
   echo "  📝 レビューレポート: ${review_files}個"
   echo ""
   echo "📋 次のステップ:"
   echo "   1. フィードバック適用: /apply-feedback $1"
   echo "   2. プルリクエスト作成: /create-pr $1"
   echo "   3. ステータス確認: /use-case-status"
   echo ""
   echo "✅ 実装レビュー完了 - フィードバック適用準備完了!"
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