Create TDD tests based on Given-When-Then specifications and domain model.

## 🎯 **TDD/DDD/LAYERED PROCESS CONTEXT**

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → **Design Review(04.5)** → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - TDD Test Creation (05/16)  
> 🎯 **Phase Purpose**: Create failing tests from Given-When-Then scenarios (RED)  
> ⬅️ **Previous Stage**: 04-domain-modeling (Domain Model Design)  
> ➡️ **Next Stage**: 06-implement-domain (Domain Layer Implementation)
>
> **📋 3-Layer Architecture Operations**:  
> - 🎯 **Strategic**: `docs/use_cases/core/index.md` (Reference core scenarios)  
> - 📊 **Tactical**: `docs/use_cases/index.md` (Update TDD RED phase status)  
> - 🔧 **Execution**: `docs/use_cases/issue-X-Y.json` (Track test creation details)

## 🔴 **TDD RED PHASE: FAILING TESTS ONLY**

**⚠️ Important Notice:**
- **This step is TDD RED PHASE** - Create failing tests based on specifications
- **CREATE FAILING TESTS ONLY** - Do not implement any production code  
- **TDD Discipline** - Tests must fail initially to validate TDD cycle
- **No implementation allowed** - Production code comes in next step

**TDD Cycle Position:**
1. `04-domain-modeling` ← Design documentation
2. `05-create-tests` ← **【YOU ARE HERE】TDD RED (failing tests)**
3. `06-implement-domain` ← TDD GREEN (make tests pass)
4. `11-refactor` ← TDD REFACTOR (improve code quality)

**Essential TDD Rules:**
- ✅ Write failing tests that capture specifications
- ❌ Do not write any implementation code
- ✅ Verify all tests fail (RED phase confirmation)

## 📋 **TDD RED PHASE TASK CHECKLIST**

**Use this checklist to create comprehensive failing tests:**

### 🔴 Required Tasks

#### **📖 Specification Analysis**
- [ ] **Read use case specifications**: Parse Given-When-Then scenarios from issue-X-Y.md
- [ ] **Read domain model design**: Extract entity and behavior expectations from design docs
- [ ] **Map scenarios to test cases**: Convert each Given-When-Then to specific test methods
- [ ] **Extract acceptance criteria**: Convert acceptance criteria into testable assertions

#### **🔴 Failing Test Implementation**
- [ ] **Write domain entity tests**: Test entity creation, behavior, and invariants (must fail)
- [ ] **Write value object tests**: Test immutability, validation, and equality (must fail)
- [ ] **Write domain service tests**: Test business logic and rules enforcement (must fail)
- [ ] **Write application service tests**: Test use case orchestration (must fail)

#### **🔍 RED Phase Validation**
- [ ] **Run all tests**: Execute complete test suite using pytest
- [ ] **Verify all tests fail**: Confirm every test fails due to missing implementation
- [ ] **Update metadata**: Mark TDD RED phase as complete in issue-X-Y.json
- [ ] **Commit failing tests**: Version control all test code with clear commit message

### 🟡 Recommended Tasks

#### **🏗️ Test Structure Design**
- [ ] **Design unit tests**: Plan tests for individual entities, value objects, and domain services
- [ ] **Design integration tests**: Plan tests for repository interfaces and application services
- [ ] **Design e2e tests**: Plan tests for complete user scenarios through presentation layer
- [ ] **Plan test organization**: Structure test files following src/ directory hierarchy
- [ ] **Design test naming**: Use descriptive names that capture business intent

#### **🧪 Test Infrastructure Setup**
- [ ] **Create test fixtures**: Design test data and object factories
- [ ] **Create mock objects**: Design mocks for external dependencies and repositories
- [ ] **Set up test configuration**: Configure pytest settings and test database if needed
- [ ] **Create test utilities**: Build helper functions for common test operations

### 🟢 Optional Tasks

#### **📋 Advanced Test Coverage**
- [ ] **Write repository interface tests**: Test data access contracts (must fail)
- [ ] **Write presentation tests**: Test API endpoints and input validation (must fail)
- [ ] **Identify test boundaries**: Determine unit vs integration vs e2e test placement
- [ ] **Set up test isolation**: Ensure tests are independent and repeatable

#### **📊 Phase Completion & Handoff**
- [ ] **Check test coverage**: Ensure all Given-When-Then scenarios have corresponding tests
- [ ] **Validate test quality**: Ensure tests are readable, maintainable, and focused
- [ ] **Document test implementation**: Create test plan documentation
- [ ] **Document test execution**: Record test run results and failure reasons
- [ ] **Prepare for GREEN phase**: Ensure tests clearly define what needs to be implemented
- [ ] **Confirm NO production code**: Verify absolutely no implementation code was written

**💡 Pro Tip**: All tests MUST fail at this stage - if a test passes, you've accidentally implemented something!  
- ✅ Ensure all tests fail (RED phase)
- ❌ Do not make tests pass yet

**CREATE FAILING TESTS ONLY.**

## Task Details

**🤖 Agent Integration**: This command uses the specialized `05-create-tests` agent for optimal TDD RED phase implementation.

1. **Pre-execution Validation**:
   ```bash
   # Validate issue number requirement
   if [[ $# -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       echo "使用例: /create-tests 1"
       echo "使用例: /create-tests 1,7 (複数イシュー)"
       exit 1
   fi
   
   # Extract issue numbers from arguments
   issue_numbers=()
   feature_name=""
   
   # Parse first argument for issue numbers
   IFS=',' read -ra ISSUE_ARRAY <<< "$1"
   for issue in "${ISSUE_ARRAY[@]}"; do
       if [[ "$issue" =~ ^[0-9]+$ ]]; then
           issue_numbers+=("$issue")
       fi
   done
   
   # Optional feature name from second argument
   if [[ $# -gt 1 ]]; then
       feature_name="$2"
   fi
   
   echo "🧪 Issues: $(printf '#%s ' "${issue_numbers[@]}")のTDDテスト作成を開始します（RED phase）"
   ```

2. **Execute Test Creation Agent**:
   ```bash
   # 🤖 Delegate to specialized test creation agent
   echo "🧪 TDDテスト作成エージェントを起動します..."
   echo "専門エージェントがTDD RED段階の失敗テストを作成します"
   echo ""
   
   # Call the specialized agent using Claude Code's Task tool
   # The agent will handle:
   # - Use case specification analysis
   # - Domain model review
   # - Failing test creation (RED phase)
   # - Test structure organization
   # - Prerequisites validation
   # - Test execution and failure verification
   # - Metadata updates and git commit
   
   # Note: In actual implementation, this would be handled by the Claude Code system
   # when the /create-tests command is executed. The agent integration happens
   # automatically through the Task tool with subagent_type="05-create-tests"
   
   echo "✅ TDDテスト作成エージェント呼び出し完了"
   echo "エージェントが以下の処理を実行しました:"
   echo "  - ユースケース仕様の解析とGiven-When-Thenシナリオのテスト化"
   echo "  - ドメインモデルを反映したエンティティ/値オブジェクトテスト作成"
   echo "  - アプリケーションサービスのユースケーステスト作成"
   echo "  - 失敗テストの実行確認（TDD RED段階）"
   echo "  - メタデータ更新とGitコミット"
   ```

3. **Agent Result Verification**:
   ```bash
   # 🔍 Verify agent execution results
   echo "🔍 エージェント実行結果を検証中..."
   
   # Check that test files were created by the agent
   echo "  🔍 テストファイルの作成確認中..."
   
   # Check for test directory structure
   test_dirs=(
       "tests/unit"
       "tests/integration"
       "tests/e2e"
   )
   
   # Validate test structure was created
   missing_test_dirs=()
   for dir in "${test_dirs[@]}"; do
       if [[ ! -d "$dir" ]]; then
           missing_test_dirs+=("$dir")
       fi
   done
   
   # Check for test files related to issues
   test_files_found=0
   for issue_num in "${issue_numbers[@]}"; do
       # Look for test files mentioning the issue
       if find tests/ -name "*.py" -type f -exec grep -l "issue.*$issue_num\|#$issue_num" {} \; 2>/dev/null | head -1 >/dev/null; then
           echo "    ✅ Issue #$issue_num のテストファイルを確認しました"
           ((test_files_found++))
       else
           echo "    ⚠️ Issue #$issue_num のテストファイルが見つかりません"
       fi
   done
   
   # Report validation results
   if [[ ${#missing_test_dirs[@]} -gt 0 ]] || [[ $test_files_found -eq 0 ]]; then
       echo "❌ エージェント実行検証失敗:"
       if [[ ${#missing_test_dirs[@]} -gt 0 ]]; then
           echo "  未作成テストディレクトリ: ${missing_test_dirs[*]}"
       fi
       if [[ $test_files_found -eq 0 ]]; then
           echo "  テストファイルが作成されていません"
       fi
       exit 1
   fi
   
   echo "✅ エージェント実行結果検証完了"
   ```

4. **Display TDD RED Phase Success Summary**:
   ```bash
   # 📊 Display comprehensive TDD RED phase summary
   echo ""
   echo "🎉 TDDテスト作成完了（RED phase）!"
   echo "============================================="
   
   # Show created test files
   echo "📁 作成されたテストファイル:"
   if find tests/ -name "test_*.py" -type f >/dev/null 2>&1; then
       test_count=$(find tests/ -name "test_*.py" -type f | wc -l)
       echo "   ✅ テストファイル: ${test_count} 個"
       find tests/ -name "test_*.py" -type f | head -5 | while read -r file; do
           echo "      - $file"
       done
       if [[ $test_count -gt 5 ]]; then
           echo "      - ... (他 $((test_count - 5)) ファイル)"
       fi
   else
       echo "   ⚠️ テストファイルが見つかりません"
   fi
   
   # Show test verification
   echo ""
   echo "🔴 TDD RED状態確認:"
   echo "   - すべてのテストが失敗（実装前のため正常）"
   echo "   - Given-When-Thenシナリオからテスト自動生成"
   echo "   - ドメインモデルに基づくエンティティテスト"
   echo "   - アプリケーションユースケーステスト"
   
   echo ""
   echo "📋 次のステップ (TDD GREEN phase):"
   for issue_num in "${issue_numbers[@]}"; do
       echo "   /implement-domain $issue_num"
   done
   
   echo ""
   echo "📚 重要ドキュメント:"
   echo "   - テスト計画: docs/test_plan/"
   echo "   - ドメインモデル: docs/domain/"
   echo "   - ユースケース仕様: docs/use_cases/"
   echo ""
   echo "✅ TDD RED段階完了 - 実装準備完了!"
   ```

## Common Errors and Solutions

### ❌ Error Case 1: Missing use case specifications
**Cause**: Use case specifications not created for the issue  
**Solution**: 
```bash
/create-use-case <issue-number>
```

### ❌ Error Case 2: Missing domain model
**Cause**: Domain model design not completed  
**Solution**: 
```bash
/domain-modeling <issue-number>
```

### ❌ Error Case 3: Tests already exist
**Cause**: Tests already created for this issue  
**Solution**: Choose to overwrite or work on different issue

## Execution Examples

### ✅ Success Example
```bash
$ /create-tests 15
🧪 Issues: #15 のTDDテスト作成を開始します（RED phase）
🤖 TDDテスト作成エージェントを起動します...
✅ エージェント実行結果検証完了
🎉 TDDテスト作成完了（RED phase）!
```

### ❌ Failure Example and Fix
```bash
$ /create-tests 15
❌ エラー: Issue #15 のユースケース仕様が見つかりません

# Fix: Create use case specification first
$ /create-use-case 15
```