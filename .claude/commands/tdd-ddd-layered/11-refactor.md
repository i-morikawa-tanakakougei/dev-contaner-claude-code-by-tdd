Use the 11-refactor subagent to refactor code after all tests are GREEN (TDD REFACTOR phase). This command MUST USE the specialized 11-refactor subagent for optimal refactoring implementation.

## Metadata
- **Prerequisites**: All tests passing (10-run-all-tests)
- **Input**: Issue number(s) (required)
- **Output**: 
  - Refactored code with improved quality
  - Maintained test coverage
  - Updated `docs/use_cases/issue-X-Y.json` metadata
- **Dependencies**: All tests green, code analysis tools
- **Execution Timing**: TDD REFACTOR phase - after all tests pass

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Refactoring (11/16)  
> 🎯 **Phase Purpose**: Improve code quality after tests pass (REFACTOR)  
> ⬅️ **Previous Stage**: 10-run-all-tests (Test Execution)  
> ➡️ **Next Stage**: 12-evolve-scenarios (Scenario Evolution) or 13-review-issue (Review)
>
> **📋 3-Layer Architecture Operations**:
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference for refactoring goals)
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update TDD REFACTOR status)
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track refactoring cycles)

## 🔵 **TDD REFACTOR PHASE: QUALITY IMPROVEMENT ONLY**

**⚠️ Important Notice:**
- **This step is TDD REFACTOR PHASE** - Improve code quality while maintaining functionality
- **ALL TESTS MUST REMAIN GREEN** - Do not break existing functionality  
- **Quality improvement focus** - Remove duplication, improve readability, optimize performance
- **No new features** - Only improve existing implementation

**TDD Cycle Completion:**
1. `05-create-tests` ← TDD RED (failing tests created)
2. `06-09-implement-*` ← TDD GREEN (implementation completed)
3. `10-run-all-tests` ← All tests passing verification
4. `11-refactor` ← **【YOU ARE HERE】TDD REFACTOR (quality improvement)**

**Refactoring Rules:**
- ✅ Improve code structure and readability
- ✅ All tests must remain GREEN throughout refactoring
- ❌ No new features or functionality

## 📋 **TDD REFACTOR TASK CHECKLIST**

**Use this checklist for systematic code quality improvement:**

### 🔴 Required Tasks

#### **📖 Current Issue Analysis**
- [ ] **Review current issue code**: Analyze code implemented in steps 06-09 for current issue
- [ ] **Identify code smells**: Find duplication, long methods, complex conditionals
- [ ] **Assess test coverage**: Ensure current code is well-tested before refactoring
- [ ] **Plan refactoring sequence**: Order improvements by safety and impact

#### **🔧 Code Quality Improvements**
- [ ] **Extract common methods**: Remove duplication within current issue's code
- [ ] **Improve naming**: Use more descriptive variable, method, and class names
- [ ] **Simplify complex methods**: Break down large methods into smaller, focused ones
- [ ] **Reduce conditional complexity**: Simplify complex if/else chains and switch statements

#### **🧪 Continuous Testing**
- [ ] **Run tests after each change**: Execute `uv run --frozen pytest` after every refactoring
- [ ] **Verify all tests remain GREEN**: Ensure no functionality is broken
- [ ] **Check code quality**: Run `uv run --frozen ruff check src/ --fix`
- [ ] **Verify type safety**: Run `uv run --frozen pyright src/`

### 🟡 Recommended Tasks

#### **🏗️ Structure Improvements**
- [ ] **Apply design patterns**: Implement appropriate patterns (Strategy, Factory, etc.)
- [ ] **Improve class organization**: Ensure single responsibility principle
- [ ] **Enhance error handling**: Improve exception handling and error messages
- [ ] **Optimize data structures**: Use more appropriate data structures where beneficial
- [ ] **Optimize imports and dependencies**: Clean up unused imports and dependencies

#### **🔍 Cross-Layer Improvements**
- [ ] **Scan domain layer**: Find similar patterns in src/domain/ across other features
- [ ] **Scan application layer**: Identify duplicate use case patterns in src/application/
- [ ] **Scan infrastructure layer**: Find repeated repository or service patterns
- [ ] **Scan test code**: Identify duplicate test setup and helper code
- [ ] **Document integration opportunities**: List potential consolidation targets

### 🟢 Optional Tasks

#### **🎯 Quality Enhancement**
- [ ] **Document improvement opportunities**: List specific refactoring targets
- [ ] **Improve algorithm efficiency**: Optimize performance-critical code sections
- [ ] **Validate performance**: Ensure refactoring doesn't degrade performance

#### **✅ Final Quality Validation**
- [ ] **Run final code quality check**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run final formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run final type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Execute complete test suite**: Run `uv run --frozen pytest --cov=src`
- [ ] **Validate all tests GREEN**: Ensure no functionality was broken during refactoring

#### **📊 Refactoring Documentation**
- [ ] **Document improvements made**: Record what was refactored and why
- [ ] **Update metadata**: Mark refactoring phase complete in issue-X-Y.json
- [ ] **Create refactoring report**: Document metrics improvements (complexity, duplication, etc.)
- [ ] **Commit refactored code**: Version control all improvements with clear commit message
- [ ] **Prepare for review**: Ensure code is ready for quality review phase

**💡 Pro Tip**: Refactor fearlessly but test continuously - green tests are your safety net!

## Common Errors and Solutions

### ❌ Error Case 1: Tests not all passing
**Cause**: Refactoring attempted before achieving GREEN phase  
**Solution**: Ensure all tests pass first with `/run-all-tests <issue-number>`

### ❌ Error Case 2: Refactoring breaks tests
**Cause**: Changing behavior instead of structure during refactoring  
**Solution**: Focus only on code structure, design patterns, and readability

### ❌ Error Case 3: Large refactoring scope
**Cause**: Attempting too many changes at once  
**Solution**: Make small, incremental changes and run tests frequently

### ❌ Error Case 4: Entity inheritance causing ID type conflicts
**Cause**: Refactoring entities to inherit from base classes with different ID requirements  
**Solution**: 
```bash
# Example: UUID conversion errors in Configuration entity
# Problem: BaseDomainEntity expects UUID, but existing tests use string IDs like "test-config-1"

# Before refactoring: Validate ID compatibility
grep -r "test.*config.*id" tests/  # Check existing test ID formats
grep -r "UUID" src/domain/entities/  # Check base class requirements

# Solution: Use composition over inheritance
# - Keep existing ID format for backward compatibility
# - Use static methods from base class for validation
# - Avoid direct inheritance when ID types don't match
```
**Critical**: Always validate ID type compatibility before applying inheritance patterns

## Execution Examples

### ✅ Success Example
```bash
$ /refactor 15
🔄 Issues: #15 のリファクタリングを開始します
🟢 テスト状態確認中...
✅ 全テストが成功しています
🎨 コード品質改善中...
  ✅ 重複コードの除去
  ✅ メソッドの分割と整理
🧪 リファクタリング後テスト実行...
======= 45 passed, 0 failed =======
✅ リファクタリング完了 - テスト維持
🎉 TDD REFACTORフェーズ完了!
```

### ❌ Failure Example and Fix
```bash
$ /refactor 15
❌ 2 tests failed after refactoring
💡 リファクタリングを元に戻してください
# Fix: Revert changes and make smaller improvements
git checkout HEAD~1
$ /refactor 15
```

## Task Details

**🤖 Agent Integration**: This command MUST USE PROACTIVELY the specialized `11-refactor` subagent for optimal code refactoring.
 Claude Code should automatically delegate this task to the 11-refactor subagent based on the command description.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /refactor 1"
       echo "使用例: /refactor 1,7 (複数イシュー)"
       exit 1
   fi
   
   # Extract issue numbers from arguments
   issue_numbers=()
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Check for test execution completion
   missing_tests=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for test results
       if ! find docs/test_results/ -name "*issue*${issue_num}*" -type f 2>/dev/null | head -1 >/dev/null; then
           missing_tests+=("$issue_num")
       fi
   done
   
   if [[ ${#missing_tests[@]} -gt 0 ]]; then
       echo "❌ エラー: 以下のIssueのテスト実行が完了していません:"
       printf '  - Issue #%s\n' "${missing_tests[@]}"
       echo "💡 先に /run-all-tests を実行してください"
       exit 1
   fi
   
   echo "🔧 Issues: $(printf '#%s ' "${issue_numbers[@]}")のリファクタリングを開始します"
   ```

2. **Context Preparation and Agent Execution**:
   ```bash
   # 🔄 Prepare context for agent (Pattern B: Hybrid approach)
   echo "🔧 コンテキスト準備とエージェント起動..."
   
   # Create context file with refactoring information
   context_file="/workspace/.claude/context/current-command-context.json"
   current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
   
   # Build context JSON for refactoring
   cat > "$context_file" <<EOF
   {
     "command": "refactor",
     "timestamp": "$current_time",
     "issue_numbers": [$(IFS=,; echo "${issue_numbers[*]}")],
     "phase": "tdd-refactor-phase",
     "context": {
       "expected_outputs": [
         "docs/refactoring/code-quality-improvement.md",
         "docs/refactoring/refactoring-report.json",
         "refactored codebase in src/"
       ],
       "architecture_patterns": ["TDD", "Clean Code", "SOLID Principles"]
     },
     "additional_instructions": "TDD REFACTORフェーズでコード品質を改善してください。全テストをGREEN状態に保ちながら、重複コードの除去、メソッドの分割、デザインパターンの適用、パフォーマンス最適化を行ってください。リファクタリング前後でのメトリクス比較も提供してください。",
     "special_considerations": [
       "全テストが引き続きGREEN状態を維持すること",
       "新機能追加は一切行わない（リファクタリングのみ）",
       "レイヤー間の責務分離と依存関係の遵守",
       "コード品質メトリクスの測定と改善報告"
     ],
     "custom_context": {
       "tdd_refactor_phase": true,
       "quality_improvement": true,
       "test_preservation": true,
       "metrics_reporting": true
     }
   }
   EOF
   
   echo "✅ コンテキストファイル作成完了: $context_file"
   
   # 🤖 Call the specialized agent with hybrid context
   echo ""
   echo "🔧 リファクタリングエージェントを起動します..."
   echo "専門エージェントがTDD REFACTOR フェーズを実行します"
   echo ""
   
   # Actual Claude Code Task tool invocation with hybrid approach
   # Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[11-refactor固有のタスクを実行]

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 実行結果の報告
- 次のステップへの案内"

   # Execute with specialized 11-refactor subagent
   # The 11-refactor subagent will be automatically invoked based on the task description
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"
   
   echo "✅ エージェント呼び出し設定完了"
   echo "エージェントが以下の処理を実行します:"
   echo "  - コンテキストファイルからのイシュー情報取得"
   echo "  - コード品質分析と改善機会の特定"
   echo "  - 継続的テスト検証付きの安全なリファクタリング実行"
   echo "  - 重複除去とデザインパターンの適用"
   echo "  - パフォーマンス最適化とコード構造改善"
   echo "  - レイヤー間一貫性とアーキテクチャ遵守"
   echo "  - テストコードリファクタリングと改善"
   echo "  - 品質メトリクス測定とレポート作成"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that refactoring was completed successfully
   echo "  🔍 リファクタリング完了状況の確認中..."
   
   refactoring_results=()
   for issue_num in "${issue_numbers[@]}"; do
       # Look for refactoring documentation
       doc_pattern="docs/refactoring/*issue*${issue_num}*"
       if ls $doc_pattern 2>/dev/null | head -1 >/dev/null; then
           doc_files=$(ls $doc_pattern 2>/dev/null)
           for file in $doc_files; do
               refactoring_results+=("$file")
               echo "    ✅ Issue #$issue_num のリファクタリング文書を確認: $(basename "$file")"
           done
       else
           echo "    ❌ Issue #$issue_num のリファクタリング文書が見つかりません"
       fi
       
       # Check metadata update
       metadata_pattern="docs/use_cases/*issue*${issue_num}*.json"
       if ls $metadata_pattern 2>/dev/null | head -1 >/dev/null; then
           metadata_file=$(ls $metadata_pattern 2>/dev/null | head -1)
           if command -v jq >/dev/null 2>&1; then
               refactor_status=$(jq -r '.phases.refactor.completed // false' "$metadata_file" 2>/dev/null)
               if [[ "$refactor_status" == "true" ]]; then
                   echo "    ✅ Issue #$issue_num のメタデータが更新されました"
               else
                   echo "    ⚠️ Issue #$issue_num のメタデータ更新が未確認"
               fi
           fi
       fi
   done
   
   # Verify all tests are still passing
   echo "  🧪 テスト状態の確認中..."
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --tb=short >/dev/null 2>&1; then
       echo "    ✅ 全テストが成功しています"
   else
       echo "    ❌ エラー: リファクタリング後にテストが失敗しています"
       exit 1
   fi
   
   # Report validation results
   if [[ ${#refactoring_results[@]} -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗: リファクタリング文書が作成されていません"
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   
   # 🔧 Load advanced task verification library
   source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
   
   # ✨ New: Advanced task verification with retry capability
   echo "🔍 Critical tasks確認中..."
   if ! verify_critical_tasks "11-refactor" "$latest_report"; then
       echo "⚠️ Critical tasks確認で問題が検出されました - 再実行を試行します"
       prepare_retry_context "11-refactor" "1" "${verification_issues[@]}"
       
       # Enhanced context for retry
       echo "🔄 再実行用の強化コンテキスト準備中..."
       prepare_enhanced_context "11-refactor" "$context_file" "${verification_issues[@]}"
       
       echo "💡 推奨アクション: エージェントを再実行してください"
       echo "   重点項目: $(IFS='|'; echo "${verification_issues[*]}")"
       exit 1
   fi
   
   echo "✅ Critical tasks確認完了 - 全項目クリア"
   ```

4. **Display Refactoring Success Summary**:
   ```bash
   # 📊 Display comprehensive refactoring summary
   echo ""
   echo "🎉 TDD REFACTORフェーズ完了!"
   echo "============================================="
   
   # Show created refactoring documentation
   echo "📁 作成されたリファクタリング文書:"
   for file in "${refactoring_results[@]}"; do
       if [[ -f "$file" ]]; then
           echo "   ✅ $file"
       fi
   done
   
   # Show refactoring summary
   echo ""
   echo "🔧 リファクタリング実行サマリー:"
   if [[ ${#refactoring_results[@]} -gt 0 ]]; then
       # Try to extract basic refactoring information
       echo "   📊 コード品質が改善されました"
       echo "   🧪 全テストが引き続き成功しています"
       echo "   🏗️ アーキテクチャの整合性が維持されています"
   fi
   
   # Show next steps
   echo ""
   echo "📋 次のステップ (シナリオ進化・レビュー):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /evolve-scenarios ${issue_num}"
       echo "   /review-issue ${issue_num}"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - リファクタリング文書: docs/refactoring/"
   echo "   - 品質改善レポート: 各文書を確認"
   if [[ ${#refactoring_results[@]} -gt 0 ]]; then
       echo "   - 作成された文書: ${refactoring_results[0]} 他"
   fi
   
   echo ""
   echo "🔗 関連リソース:"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   - Issue #$issue_num: gh issue view $issue_num"
   done
   
   echo ""
   echo "✅ TDD REFACTORフェーズ完了 - コード品質向上完了!"
   ```

Important Notes:
- Keep all tests GREEN throughout refactoring
- Focus on code quality improvement, not new features
- Make incremental changes with continuous testing
- Document all improvements for team knowledge
- All user-facing output must be in JAPANESE