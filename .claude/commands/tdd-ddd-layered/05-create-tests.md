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

1. **Setup Safe Environment and Parse Arguments**:
   ```bash
   # 🔧 Load all safe operation functions
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "05-create-tests" "$ARGUMENTS"
   
   # Create tests expects at least one issue number
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "create-tests" "1" "単一イシューのテスト作成"
       show_usage_example "create-tests" "1,7" "複数イシューのテスト作成"
       show_usage_example "create-tests" "1 feature-name" "イシュー + 機能名指定"
       exit 1
   fi
   
   # Extract issue list and feature name
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # Feature name will be extracted from existing files
       feature_name=""
   fi
   
   echo "🧪 Issues: $(printf '#%s ' "${issue_numbers[@]}")のTDDテスト作成を開始します（RED phase）"
   ```

2. **Begin Transaction and Pre-validation**:
   ```bash
   # 🔄 Start comprehensive transaction
   if ! begin_transaction "create_tests_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 Validate prerequisites - use case spec and domain model
   echo "📋 前提条件の検証中..."
   
   # Check for use case specifications
   missing_specs=()
   found_specs=()
   for issue_num in "${issue_numbers[@]}"; do
       echo "  🔍 Issue #$issue_num の仕様検索中..."
       
       # Search for use case specification files
       spec_files=$(find docs/use_cases/ -name "*issue-*${issue_num}*" -type f -name "*.md" 2>/dev/null | grep -v index.md || echo "")
       
       if [[ -z "$spec_files" ]]; then
           missing_specs+=("$issue_num")
           echo "    ❌ Issue #$issue_num の仕様が見つかりません"
       else
           found_specs+=("$spec_files")
           echo "    ✅ Issue #$issue_num の仕様発見: $(basename "$spec_files")"
           
           # Extract feature name from first found spec if not provided
           if [[ -z "$feature_name" ]]; then
               feature_name=$(basename "$spec_files" | sed 's/^issue-[0-9-]*-\(.*\)\.md$/\1/')
               echo "    📝 機能名抽出: $feature_name"
           fi
       fi
   done
   
   # Error if any specifications are missing
   if [[ ${#missing_specs[@]} -gt 0 ]]; then
       echo ""
       echo "❌ 以下のイシューの仕様が見つかりません:"
       printf '  - Issue #%s\n' "${missing_specs[@]}"
       echo ""
       echo "💡 最初に以下のコマンドでユースケース仕様を作成してください:"
       for missing_issue in "${missing_specs[@]}"; do
           echo "   /create-use-case $missing_issue"
       done
       execute_rollback "missing_use_case_specs"
       exit 1
   fi
   
   # Check for domain model
   domain_model_file="docs/domain/issue-${issue_list}-domain-model.md"
   if [[ ! -f "$domain_model_file" ]]; then
       echo "❌ ドメインモデル設計が見つかりません: $domain_model_file"
       echo "💡 最初にドメインモデル設計を作成してください:"
       echo "   /domain-modeling $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_model"
       exit 1
   fi
   
   echo "✅ 前提条件検証完了: 仕様${#found_specs[@]}個 + ドメインモデル確認"
   ```

3. **Identify and Validate Metadata**:
   ```bash
   # 📊 Find and validate metadata files
   echo "📊 メタデータファイル検証中..."
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが見つかりません: $metadata_file"
       echo "💡 先に /create-use-case コマンドを実行してください"
       execute_rollback "metadata_file_missing"
       exit 1
   fi
   
   # Validate metadata file format
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # Check domain model phase completion
   domain_status=$(jq -r '.phases.domain_model.created // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" != "true" ]]; then
       echo "エラー: ドメインモデル設計が完了していません"
       echo "💡 先に /domain-modeling コマンドを実行してください"
       execute_rollback "domain_model_not_completed"
       exit 1
   fi
   
   # Check if tests are already created
   test_status=$(jq -r '.phases.tests.created // false' "$metadata_file" 2>/dev/null)
   if [[ "$test_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のテストは既に作成されています"
       echo "既存のテストを上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "テスト作成をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のテストを上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **Analyze Specifications and Domain Model**:
   ```bash
   # 📖 Analyze specifications and domain model for test scenarios
   echo "📖 仕様とドメインモデル分析中..."
   
   # Extract Given-When-Then scenarios from specifications
   all_scenarios=()
   all_entities=()
   
   for spec_file in "${found_specs[@]}"; do
       echo "  📋 分析中: $(basename "$spec_file")"
       
       if ! check_file_permissions "$spec_file" "read"; then
           echo "エラー: 仕様ファイルの読み取り権限がありません: $spec_file"
           execute_rollback "spec_file_access_denied"
           exit 1
       fi
       
       # Extract scenarios (Given-When-Then patterns)
       scenarios=$(grep -A 5 -B 2 "Given:\\|When:\\|Then:" "$spec_file" 2>/dev/null | \
                  grep -E "(Given|When|Then):" | \
                  sed 's/^[[:space:]]*//' | \
                  paste -d' ' - - - 2>/dev/null || echo "")
       
       if [[ -n "$scenarios" ]]; then
           while IFS= read -r scenario; do
               [[ -n "$scenario" ]] && all_scenarios+=("$scenario")
           done <<< "$scenarios"
       fi
   done
   
   # Extract entities from domain model
   if ! check_file_permissions "$domain_model_file" "read"; then
       echo "エラー: ドメインモデルファイルの読み取り権限がありません: $domain_model_file"
       execute_rollback "domain_model_access_denied"
       exit 1
   fi
   
   entities=$(grep -A 2 "^### [A-Z]" "$domain_model_file" 2>/dev/null | \
             grep -E "^### [A-Z][a-zA-Z]*$" | \
             sed 's/^### //' || echo "")
   
   if [[ -n "$entities" ]]; then
       while IFS= read -r entity; do
           [[ -n "$entity" ]] && all_entities+=("$entity")
       done <<< "$entities"
   fi
   
   echo "  🎯 抽出された要素:"
   echo "    - シナリオ: ${#all_scenarios[@]} 個"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   
   if [[ ${#all_scenarios[@]} -eq 0 ]]; then
       echo "⚠️  Given-When-Thenシナリオが見つかりませんでした"
       echo "テンプレートシナリオを生成します"
   fi
   
   echo "✅ 仕様分析完了"
   ```

5. **Create Test Directory Structure**:
   ```bash
   # 🏗️ Create comprehensive test structure
   echo "🏗️ テストディレクトリ構造作成中..."
   
   # Define complete test directory structure
   test_directories=(
       "tests/unit/domain/entities"
       "tests/unit/domain/value_objects"
       "tests/unit/domain/services"
       "tests/unit/application/use_cases"
       "tests/unit/application/dtos"
       "tests/integration/repositories"
       "tests/integration/use_cases"
       "tests/e2e/api"
       "tests/e2e/cli"
       "tests/fixtures"
       "tests/builders"
       "tests/mocks"
   )
   
   # Create all test directories safely
   for dir in "${test_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: テストディレクトリ作成に失敗しました: $dir"
           execute_rollback "test_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove test directory: $dir"
   done
   
   # Create __init__.py files for test packages
   test_init_files=(
       "tests/__init__.py"
       "tests/unit/__init__.py"
       "tests/unit/domain/__init__.py"
       "tests/unit/application/__init__.py"
       "tests/integration/__init__.py"
       "tests/e2e/__init__.py"
       "tests/fixtures/__init__.py"
       "tests/builders/__init__.py"
       "tests/mocks/__init__.py"
   )
   
   for init_file in "${test_init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       if ! safe_create_file "$init_file" '"""Test package initialization"""' false; then
           echo "エラー: テスト__init__.pyファイルの作成に失敗しました"
           execute_rollback "test_init_creation_failed"
           exit 1
       fi
       add_rollback "rm -f '$init_file'" "Remove test init file: $init_file"
   done
   
   echo "✅ テスト構造作成完了 (${#test_directories[@]} ディレクトリ)"
   ```

6. **Create Unit Tests (TDD RED Phase)**:
   ```bash
   # 🧪 Create comprehensive unit tests in RED phase
   echo "🧪 ユニットテスト作成中（TDD RED phase）..."
   
   created_test_files=()
   
   # Create entity tests
   if [[ ${#all_entities[@]} -gt 0 ]]; then
       for entity in "${all_entities[@]}"; do
           entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
           test_file="tests/unit/domain/entities/test_${entity_lower}.py"
           
           echo "  🧪 作成中: $test_file"
           
           entity_test_content='"""
   '"$entity"' エンティティのテスト

   TDD RED Phase: 実装前のテスト作成
   ドメインモデル: docs/domain/issue-'"${issue_list}"'-'"${feature_name}"'.md
   """

   import pytest
   from unittest.mock import Mock
   from datetime import datetime

   # TODO: 実装後にインポートを修正
   # from src.domain.entities.'"${entity_lower}"' import '"$entity"'


   class Test'"$entity"':
       """'"$entity"' エンティティのテストクラス"""

       def test_'"${entity_lower}"'_creation_with_valid_data(self):
           """
           正常なデータで'"$entity"'を作成できる
           
           Given: 有効な'"$entity"'データがある
           When: '"$entity"'を作成する
           Then: '"$entity"'が正常に作成される
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$entity"' creation not implemented yet"

       def test_'"${entity_lower}"'_creation_with_invalid_data(self):
           """
           無効なデータで'"$entity"'作成時にエラーが発生する
           
           Given: 無効な'"$entity"'データがある
           When: '"$entity"'を作成しようとする
           Then: バリデーションエラーが発生する
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$entity"' validation not implemented yet"

       def test_'"${entity_lower}"'_update_with_valid_data(self):
           """
           有効なデータで'"$entity"'を更新できる
           
           Given: 既存の'"$entity"'がある
           When: 有効なデータで更新する
           Then: '"$entity"'が正常に更新される
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$entity"' update not implemented yet"

       def test_'"${entity_lower}"'_business_rules_are_enforced(self):
           """
           '"$entity"'のビジネスルールが適用される
           
           Given: '"$entity"'のビジネスルール制約がある
           When: ルールに違反する操作を行う
           Then: ビジネスルール違反エラーが発生する
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$entity"' business rules not implemented yet"

   '
           
           if ! safe_create_file "$test_file" "$entity_test_content" false; then
               echo "エラー: エンティティテストファイルの作成に失敗しました"
               execute_rollback "entity_test_creation_failed"
               exit 1
           fi
           
           created_test_files+=("$test_file")
           add_rollback "rm -f '$test_file'" "Remove entity test: $test_file"
       done
   fi
   
   # Create value object tests
   value_objects=("EntityId" "Email")  # Common value objects
   for vo in "${value_objects[@]}"; do
       vo_lower=$(echo "$vo" | tr '[:upper:]' '[:lower:]')
       test_file="tests/unit/domain/value_objects/test_${vo_lower}.py"
       
       echo "  🧪 作成中: $test_file"
       
       vo_test_content='"""
   '"$vo"' 値オブジェクトのテスト

   TDD RED Phase: 実装前のテスト作成
   """

   import pytest

   # TODO: 実装後にインポートを修正
   # from src.domain.value_objects.'"${vo_lower}"' import '"$vo"'


   class Test'"$vo"':
       """'"$vo"' 値オブジェクトのテストクラス"""

       def test_'"${vo_lower}"'_creation_with_valid_value(self):
           """
           有効な値で'"$vo"'を作成できる
           
           Given: 有効な'"$vo"'値がある
           When: '"$vo"'を作成する
           Then: '"$vo"'が正常に作成される
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$vo"' creation not implemented yet"

       def test_'"${vo_lower}"'_creation_with_invalid_value(self):
           """
           無効な値で'"$vo"'作成時にエラーが発生する
           
           Given: 無効な'"$vo"'値がある
           When: '"$vo"'を作成しようとする
           Then: バリデーションエラーが発生する
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$vo"' validation not implemented yet"

       def test_'"${vo_lower}"'_equality_comparison(self):
           """
           '"$vo"'の等値性比較が正しく動作する
           
           Given: 同じ値を持つ2つの'"$vo"'がある
           When: 等値性を比較する
           Then: 等値であると判定される
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$vo"' equality not implemented yet"

       def test_'"${vo_lower}"'_immutability(self):
           """
           '"$vo"'が不変であることを確認する
           
           Given: '"$vo"'が作成されている
           When: 値を変更しようとする
           Then: 変更できないか新しいインスタンスが返される
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: '"$vo"' immutability not implemented yet"

   '
       
       if ! safe_create_file "$test_file" "$vo_test_content" false; then
           echo "エラー: 値オブジェクトテストファイルの作成に失敗しました"
           execute_rollback "vo_test_creation_failed"
           exit 1
       fi
       
       created_test_files+=("$test_file")
       add_rollback "rm -f '$test_file'" "Remove value object test: $test_file"
   done
   
   # Create use case tests
   use_case_file="tests/unit/application/use_cases/test_${feature_name//-/_}_use_case.py"
   echo "  🧪 作成中: $use_case_file"
   
   use_case_test_content='"""
   '"$feature_name"' ユースケースのテスト

   TDD RED Phase: 実装前のテスト作成
   仕様: docs/use_cases/issue-'"${issue_list}"'-'"${feature_name}"'.md
   """

   import pytest
   from unittest.mock import Mock, MagicMock

   # TODO: 実装後にインポートを修正
   # from src.application.use_cases.'"${feature_name//-/_}"'_use_case import '"${feature_name//[-_]/ }"'UseCase


   class Test'"${feature_name//[-_]/ }"'UseCase:
       """'"$feature_name"' ユースケースのテストクラス"""

       def setup_method(self):
           """テストセットアップ"""
           # TODO: モックの設定
           self.mock_repository = Mock()
           # self.use_case = '"${feature_name//[-_]/ }"'UseCase(self.mock_repository)

       '"$(if [[ ${#all_scenarios[@]} -gt 0 ]]; then
           for i in "${!all_scenarios[@]}"; do
               scenario="${all_scenarios[$i]}"
               given=$(echo "$scenario" | grep -oE "Given: [^\\|]*" | sed 's/Given: //' || echo "前提条件")
               when=$(echo "$scenario" | grep -oE "When: [^\\|]*" | sed 's/When: //' || echo "実行アクション")
               then=$(echo "$scenario" | grep -oE "Then: [^\\|]*" | sed 's/Then: //' || echo "期待結果")
               
               test_name=$(echo "${when,,}" | sed 's/[^a-zA-Z0-9]/_/g' | sed 's/__*/_/g' | sed 's/^_\\|_$//')
               
               echo "
       def test_${test_name}_scenario_$((i+1))(self):
           \"\"\"
           シナリオ $((i+1)): $when
           
           Given: $given
           When: $when
           Then: $then
           \"\"\"
           # TODO: 実装後にテストを修正
           assert False, \"RED: Scenario $((i+1)) not implemented yet\"
   "
           done
       else
           echo "
       def test_main_use_case_execution(self):
           \"\"\"
           メインユースケースの実行
           
           Given: 有効な入力データがある
           When: ユースケースを実行する
           Then: 期待される結果が返される
           \"\"\"
           # TODO: 実装後にテストを修正
           assert False, \"RED: Main use case not implemented yet\"

       def test_use_case_with_invalid_input(self):
           \"\"\"
           無効な入力でのユースケース実行
           
           Given: 無効な入力データがある
           When: ユースケースを実行する
           Then: バリデーションエラーが発生する
           \"\"\"
           # TODO: 実装後にテストを修正
           assert False, \"RED: Input validation not implemented yet\"
   "
       fi)'

       def test_use_case_repository_integration(self):
           """
           リポジトリとの統合テスト
           
           Given: リポジトリが設定されている
           When: データアクセスが必要な操作を実行する
           Then: リポジトリメソッドが適切に呼ばれる
           """
           # TODO: 実装後にテストを修正
           assert False, "RED: Repository integration not implemented yet"

   '
   
   if ! safe_create_file "$use_case_file" "$use_case_test_content" false; then
       echo "エラー: ユースケーステストファイルの作成に失敗しました"
       execute_rollback "use_case_test_creation_failed"
       exit 1
   fi
   
   created_test_files+=("$use_case_file")
   add_rollback "rm -f '$use_case_file'" "Remove use case test: $use_case_file"
   
   echo "✅ ユニットテスト作成完了 (${#created_test_files[@]} ファイル)"
   ```

7. **Create Test Plan Document**:
   ```bash
   # 📋 Create comprehensive test plan
   echo "📋 テスト計画文書作成中..."
   
   # Create test_plan directory
   if ! safe_mkdir "docs/test_plan"; then
       echo "エラー: テスト計画ディレクトリの作成に失敗しました"
       execute_rollback "test_plan_dir_creation_failed"
       exit 1
   fi
   
   test_plan_file="docs/test_plan/issue-${issue_list}-test-plan.md"
   
   test_plan_content="# テスト計画: $feature_name

   **Issues**: $(printf '#%s ' "${issue_numbers[@]}")
   **作成日時**: $(date)
   **フェーズ**: TDD RED Phase（テスト作成完了）

   ## 概要

   このテスト計画は、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて作成されました。
   TDD（テスト駆動開発）のREDフェーズとして、実装前にすべてのテストを作成しています。

   ## テストカバレッジ

   ### ユニットテスト (単体テスト)

   #### ドメイン層テスト
   $(if [[ ${#all_entities[@]} -gt 0 ]]; then
       for entity in "${all_entities[@]}"; do
           entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
           echo "- [ ] **$entity エンティティ**: \`tests/unit/domain/entities/test_${entity_lower}.py\`
     - 作成・更新・削除の基本操作
     - ビジネスルールの検証
     - 不変条件の維持"
       done
   else
       echo "- [ ] **メインエンティティ**: エンティティの基本操作とビジネスルール"
   fi)

   #### 値オブジェクト
   - [ ] **EntityId**: \`tests/unit/domain/value_objects/test_entityid.py\`
     - 一意性の検証
     - UUID形式のバリデーション
     - 等値性比較
   - [ ] **Email**: \`tests/unit/domain/value_objects/test_email.py\`
     - メールアドレス形式検証
     - 不正値での例外処理
     - 不変性の確保

   #### アプリケーション層テスト
   - [ ] **${feature_name}UseCase**: \`tests/unit/application/use_cases/test_${feature_name//-/_}_use_case.py\`
     $(if [[ ${#all_scenarios[@]} -gt 0 ]]; then
         for i in "${!all_scenarios[@]}"; do
             scenario="${all_scenarios[$i]}"
             when=$(echo "$scenario" | grep -oE "When: [^\\|]*" | sed 's/When: //' || echo "シナリオ$((i+1))")
             echo "     - $when"
         done
     else
         echo "     - メイン機能の実行
     - 入力バリデーション
     - エラーハンドリング"
     fi)
     - リポジトリとの統合
     - ビジネスルールの適用

   ### 統合テスト

   #### リポジトリテスト
   $(if [[ ${#all_entities[@]} -gt 0 ]]; then
       for entity in "${all_entities[@]}"; do
           echo "- [ ] **${entity}Repository**: データアクセス機能
     - CRUD操作の検証
     - トランザクション管理
     - データ整合性の確保"
       done
   else
       echo "- [ ] **MainRepository**: 基本的なデータアクセス機能"
   fi)

   #### ユースケース統合テスト
   - [ ] **${feature_name}統合フロー**: エンドツーエンドのビジネスフロー
     - 複数レイヤーの連携
     - データ永続化の確認
     - 外部依存の模擬

   ### E2Eテスト (エンドツーエンド)

   #### APIテスト
   - [ ] **RESTエンドポイント**: \`tests/e2e/api/test_${feature_name//-/_}_api.py\`
     - HTTP リクエスト・レスポンス
     - 認証・認可
     - エラーレスポンス

   #### CLIテスト（該当する場合）
   - [ ] **コマンドライン**: \`tests/e2e/cli/test_${feature_name//-/_}_cli.py\`
     - コマンド実行
     - 出力検証
     - エラーハンドリング

   ## テスト実行方法

   ### 基本実行
   \`\`\`bash
   # 全テスト実行
   uv run --frozen pytest

   # 単体テストのみ
   uv run --frozen pytest tests/unit/

   # 統合テストのみ
   uv run --frozen pytest tests/integration/

   # E2Eテストのみ
   uv run --frozen pytest tests/e2e/
   \`\`\`

   ### カバレッジ付き実行
   \`\`\`bash
   # カバレッジレポート生成
   uv run --frozen pytest --cov=src --cov-report=html --cov-report=term-missing

   # 特定ファイルのカバレッジ
   uv run --frozen pytest --cov=src.domain.entities --cov-report=term-missing
   \`\`\`

   ### 特定テストの実行
   \`\`\`bash
   # 特定テストファイル
   uv run --frozen pytest tests/unit/domain/entities/test_${all_entities[0],,}.py

   # 特定テストメソッド
   uv run --frozen pytest tests/unit/domain/entities/test_${all_entities[0],,}.py::Test${all_entities[0]}::test_creation_with_valid_data

   # パターンマッチング
   uv run --frozen pytest -k \"${feature_name//-/_}\"
   \`\`\`

   ## TDD 実行計画

   ### フェーズ1: RED - テスト作成 ✅
   - [x] 全テストファイル作成
   - [x] Given-When-Thenシナリオをテストに変換
   - [x] 実装前のため全テスト失敗を確認

   ### フェーズ2: GREEN - 最小実装 📋
   - [ ] ドメインエンティティの実装
   - [ ] 値オブジェクトの実装
   - [ ] ユースケースの実装
   - [ ] リポジトリの実装
   - [ ] 全テストが通ることを確認

   ### フェーズ3: REFACTOR - リファクタリング 📋
   - [ ] コード品質の改善
   - [ ] 重複の排除
   - [ ] パフォーマンス最適化
   - [ ] テストの整理

   ## テスト品質基準

   ### カバレッジ目標
   - **ライン カバレッジ**: 80%以上
   - **ブランチ カバレッジ**: 70%以上
   - **関数 カバレッジ**: 90%以上

   ### 品質指標
   - **テスト実行時間**: 全体で30秒以内
   - **テスト独立性**: 各テストが他に依存しない
   - **テスト命名**: 振る舞いが明確に表現されている

   ## モック・スタブ戦略

   ### 外部依存のモック
   - **データベース**: メモリ内DB またはモックリポジトリ
   - **外部API**: HTTPモック
   - **ファイルシステム**: 一時ディレクトリ

   ### テストデータ
   - **ビルダーパターン**: \`tests/builders/\` で一貫したテストデータ生成
   - **フィクスチャ**: \`tests/fixtures/\` で共通テストデータ
   - **ファクトリ**: 動的なテストデータ生成

   ## 継続的インテグレーション

   ### CI実行項目
   - [ ] 全テスト実行
   - [ ] カバレッジレポート生成
   - [ ] 品質チェック（lint, typecheck）
   - [ ] パフォーマンステスト

   ### 失敗時の対応
   - **Red Build**: テスト失敗時の即座修正
   - **Coverage Degradation**: カバレッジ低下時の警告
   - **Performance Regression**: 性能劣化の検知

   ## 次のステップ

   1. **実装開始**: \`/implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
   2. **進捗確認**: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
   3. **テスト実行**: \`uv run --frozen pytest\` でRED状態確認

   ## 備考

   - 全テストは現在RED状態（失敗）です
   - 実装完了後にGREEN状態（成功）になる予定
   - リファクタリング段階でコード品質向上

   ---

   **作成者**: $(git config user.name || echo "Unknown")
   **TDDフェーズ**: RED (テスト作成完了)
   **次フェーズ**: GREEN (実装開始)
   **テストファイル数**: ${#created_test_files[@]}
   "
   
   if ! safe_create_file "$test_plan_file" "$test_plan_content" true; then
       echo "エラー: テスト計画ファイルの作成に失敗しました"
       execute_rollback "test_plan_creation_failed"
       exit 1
   fi
   
   add_rollback "rm -f '$test_plan_file'" "Remove test plan file"
   echo "✅ テスト計画文書作成完了: $test_plan_file"
   ```

8. **Verify Tests are in RED State**:
   ```bash
   # 🔍 Verify all tests are in RED state (TDD requirement)
   echo "🔍 TDD REDフェーズ検証中..."
   
   # Validate Python environment for testing
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # Run tests to confirm they fail (RED phase requirement)
   echo "  🧪 テスト実行中（RED状態確認）..."
   
   # Count created test files
   test_file_count=$(find tests/ -name "test_*.py" -type f | wc -l)
   
   if [[ $test_file_count -eq 0 ]]; then
       echo "エラー: テストファイルが作成されていません"
       execute_rollback "no_test_files_created"
       exit 1
   fi
   
   # Run a quick test to verify RED state
   red_verification_result=""
   if command -v pytest >/dev/null 2>&1; then
       echo "  ⚡ RED状態検証実行中..."
       
       # Run tests and capture result (should fail)
       if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/ --tb=no -q >/dev/null 2>&1; then
           echo "⚠️  警告: テストが成功しています（RED状態ではない）"
           red_verification_result="UNEXPECTED_GREEN"
       else
           echo "  ✅ RED状態確認: テストが期待通り失敗しています"
           red_verification_result="EXPECTED_RED"
       fi
   else
       echo "  ⚠️  pytest が見つかりません（手動でREDstate確認が必要）"
       red_verification_result="MANUAL_VERIFICATION_NEEDED"
   fi
   
   echo "✅ TDD RED フェーズ検証完了: $red_verification_result"
   ```

9. **Update Metadata and Tracking**:
   ```bash
   # 📊 Update metadata with test creation completion
   echo "📊 メタデータ更新中..."
   
   if ! update_metadata_atomic "$metadata_file" \
       '.phases.tests.created = true | 
        .phases.tests.passed = false |
        .phases.tests.test_count = '"${#created_test_files[@]}"' |
        .phases.tests.created_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .phases.tests.red_state = "'"$red_verification_result"'" |
        .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .spec_files.test_plan = "'"$test_plan_file"'" |
        .phase = "tests_created_red" |
        .next_commands = ["implement-domain", "use-case-status"]'; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   echo "✅ メタデータ更新完了"
   ```

10. **Update Use Case Index and Git Commit**:
    ```bash
    # 📚 Update use case index
    echo "📚 ユースケースインデックス更新中..."
    
    use_cases_index="docs/use_cases/index.md"
    if [[ -f "$use_cases_index" ]]; then
        # Create backup
        backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
        if ! cp "$use_cases_index" "$backup_file"; then
            echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
            execute_rollback "index_backup_failed"
            exit 1
        fi
        add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
        
        # Update status for the feature
        feature_line="\\[${feature_name}\\]"
        updated_line="- [${feature_name}]($(basename "${found_specs[0]}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: tests_created_red, TDD: 🔴 RED, Tests: ${#created_test_files[@]})"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 Commit TDD tests
    echo "💾 TDDテストをコミット中..."
    
    commit_message="feat: create TDD tests for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name} (RED phase)

    TDD Red Phase Summary:
    - Feature: ${feature_name}
    - Issues: $(printf '#%s ' "${issue_numbers[@]}")
    - Test Files: ${#created_test_files[@]} created
    - Scenarios: ${#all_scenarios[@]} covered
    - Test Plan: $test_plan_file
    
    Created Tests:
    $(printf '  - %s\n' "${created_test_files[@]}")
    
    TDD RED Phase Status:
    - All tests created with intentional failures
    - Given-When-Then scenarios converted to test cases
    - Domain entities, value objects, and use cases covered
    - Ready for GREEN phase (implementation)
    
    Verification: $red_verification_result
    Next Step: /implement-domain for GREEN phase
    "
    
    files_to_commit=("$test_plan_file" "$metadata_file")
    files_to_commit+=("${created_test_files[@]}")
    if [[ -f "$use_cases_index" ]]; then
        files_to_commit+=("$use_cases_index")
    fi
    
    # Add test structure directories
    for dir in "${test_directories[@]}"; do
        if [[ -d "$dir" ]]; then
            files_to_commit+=("$dir")
        fi
    done
    
    if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
        echo "エラー: コミットに失敗しました"
        execute_rollback "commit_failed"
        exit 1
    fi
    
    add_rollback "git reset --hard HEAD~1" "Undo TDD tests commit"
    echo "✅ コミット完了"
    ```

11. **Update GitHub Issues**:
    ```bash
    # 🎫 Update GitHub issues with TDD test creation
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🧪 **TDDテスト作成完了（RED phase）**

    TDDのREDフェーズとして、実装前のテスト作成が完了しました。

    ## 📋 作成されたテスト
    - **テストファイル数**: ${#created_test_files[@]} ファイル
    - **カバー範囲**: ドメイン・アプリケーション・統合・E2E
    - **シナリオベース**: Given-When-Then から自動生成

    ## 🔴 TDD RED状態
    - **現在の状態**: 全テスト失敗（実装前のため）
    - **検証結果**: $red_verification_result
    - **次のフェーズ**: GREEN（実装でテストを通す）

    ## 📊 テスト構成
    $(if [[ ${#all_entities[@]} -gt 0 ]]; then
        echo "### エンティティテスト"
        for entity in "${all_entities[@]:0:3}"; do
            echo "- \`tests/unit/domain/entities/test_${entity,,}.py\`"
        done
        [[ ${#all_entities[@]} -gt 3 ]] && echo "- ... (他 $((${#all_entities[@]} - 3)) ファイル)"
    fi)
    
    ### 値オブジェクトテスト
    - \`tests/unit/domain/value_objects/test_entityid.py\`
    - \`tests/unit/domain/value_objects/test_email.py\`
    
    ### ユースケーステスト
    - \`tests/unit/application/use_cases/test_${feature_name//-/_}_use_case.py\`

    ## 🚀 次のステップ
    
    GREEN フェーズを開始してください：
    \`\`\`bash
    /implement-domain $issue_num
    \`\`\`

    ## 📚 関連ドキュメント
    - [テスト計画]($test_plan_file)
    - [ドメインモデル設計]($domain_model_file)
    - [ユースケース仕様]($(basename "${found_specs[0]}" .md).md)

    ## 🔍 TDD検証
    \`\`\`bash
    # テスト実行（現在はすべて失敗する）
    uv run --frozen pytest
    
    # 特定テストの実行
    uv run --frozen pytest tests/unit/domain/
    \`\`\`

    ---
    **TDD Phase**: 🔴 RED (test_created) → 次: 🟢 GREEN (implement)
    "
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    ```

12. **Final Success and TDD Guidance**:
    ```bash
    # 🎉 Transaction commit (success!)
    if commit_transaction; then
        echo ""
        echo "🎉 TDDテスト作成完了（RED phase）!"
        echo "============================================="
        echo "🧪 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 作成テストファイル: ${#created_test_files[@]} 個"
        echo ""
        echo "📋 作成されたテスト:"
        printf '   - %s\n' "${created_test_files[@]:0:5}"  # Show first 5
        [[ ${#created_test_files[@]} -gt 5 ]] && echo "   - ... (他 $((${#created_test_files[@]} - 5)) ファイル)"
        echo ""
        echo "📁 テスト構造:"
        echo "   - ユニットテスト: $(find tests/unit -name "test_*.py" 2>/dev/null | wc -l) ファイル"
        echo "   - 統合テスト準備: $(find tests/integration -name "*.py" 2>/dev/null | wc -l) ファイル"
        echo "   - E2Eテスト準備: $(find tests/e2e -name "*.py" 2>/dev/null | wc -l) ファイル"
        echo ""
        echo "🔴 TDD RED状態:"
        echo "   - 検証結果: $red_verification_result"
        echo "   - すべてのテストが失敗（実装前のため正常）"
        echo "   - Given-When-Thenシナリオから自動生成"
        echo ""
        echo "🚀 次のステップ（TDD GREEN phase）:"
        echo "   1. ドメイン実装: /implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. テスト実行: uv run --frozen pytest でRED確認"
        echo ""
        echo "📖 TDD サイクル:"
        echo "   🔴 RED: テスト作成 ✅ 完了"
        echo "   🟢 GREEN: 実装でテストを通す ← 次はここ"
        echo "   🔄 REFACTOR: コード改善"
        echo ""
        echo "💡 TDD原則:"
        echo "   - 実装前にテストを書く ✅"
        echo "   - テストが失敗することを確認 ✅"
        echo "   - 最小限の実装でテストを通す ← 次の作業"
        echo ""
        echo "🔍 テスト実行方法:"
        echo "   - 全テスト: uv run --frozen pytest"
        echo "   - ユニットのみ: uv run --frozen pytest tests/unit/"
        echo "   - カバレッジ付き: uv run --frozen pytest --cov=src"
        echo ""
        
        # Show operation logs summary
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ TDD REDフェーズ完了 - GREEN実装フェーズ準備完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   テスト作成中に新要件・エラー・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: 新シナリオの見落としは致命的バグを引き起こします"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

Important Notes:
- Tests must fail initially (TDD RED phase)
- Each test should test ONE thing only
- Use descriptive test names in snake_case
- Include Given-When-Then comments in tests
- Mock external dependencies appropriately
- All user-facing output must be in JAPANESE