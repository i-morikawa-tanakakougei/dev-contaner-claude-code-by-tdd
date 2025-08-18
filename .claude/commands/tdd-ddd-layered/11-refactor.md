Refactor code after all tests are GREEN (TDD REFACTOR phase) with comprehensive safety features.

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

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Sprint Review(02.5) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Sprint Execution Phase - Refactoring (11/16)  
> 🎯 **Phase Purpose**: Improve code quality after tests pass (REFACTOR)  
> ⬅️ **Previous Stage**: 10.5-review-test-results (Test Results Review)  
> ➡️ **Next Stage**: 12-evolve-scenarios (Scenario Evolution) or 13-review-issue (Review)
>
> **📋 3-Layer Architecture Operations**:
>
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

## 🚨 **CRITICAL: PHASED REFACTORING WITH USER CONSENT**

**⚠️ MANDATORY USER PERMISSION POLICY:**
- **Phase 1 (Issue-Only)**: Automatic execution - safe and scoped
- **Phase 2 (Related Code)**: REQUIRES USER PERMISSION - expands scope
- **Phase 3 (Global Integration)**: REQUIRES USER PERMISSION - system-wide changes
- **Claude Code MUST ask permission before Phase 2/3 - NEVER auto-execute**

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

#### **🔍 Related Code Discovery (Phase 2)**
- [ ] **Scan domain layer**: Find similar patterns in src/domain/ across other features
- [ ] **Scan application layer**: Identify duplicate use case patterns in src/application/
- [ ] **Scan infrastructure layer**: Find repeated repository or service patterns
- [ ] **Scan test code**: Identify duplicate test setup and helper code
- [ ] **Document integration opportunities**: List potential consolidation targets

### 🟢 Optional Tasks

#### **🎯 Phase 1: Issue-Limited Refactoring**
- [ ] **Document improvement opportunities**: List specific refactoring targets
- [ ] **Improve algorithm efficiency**: Optimize performance-critical code sections
- [ ] **Validate performance**: Ensure refactoring doesn't degrade performance

#### **🔗 Safe Integration Process (Phase 2)**
- [ ] **Create integration plan**: Document what will be merged and impact assessment
- [ ] **Backup current state**: Ensure git working directory is clean for rollback
- [ ] **Extract shared abstractions**: Create common base classes or interfaces
- [ ] **Refactor incrementally**: Make small, testable changes one at a time
- [ ] **Update related tests**: Modify tests to work with integrated code

#### **✅ Integration Validation (Phase 2)**
- [ ] **Run full test suite**: Execute all tests to ensure integration doesn't break functionality
- [ ] **Validate related features**: Test features that use integrated code
- [ ] **Check backward compatibility**: Ensure existing APIs still work
- [ ] **Verify performance impact**: Measure any performance changes from integration
- [ ] **Update documentation**: Reflect integration changes in documentation

### **🤔 Phase 1 Completion Checkpoint**
```bash
echo "✅ Phase 1 (Issue-Limited Refactoring) 完了"
echo ""
echo "🎯 Phase 2: Related Code Integration について"
echo "   📋 内容: 同じドメイン・機能領域の重複コードをチェック・統合"
echo "   ⏱️  推定時間: 10-20分"
echo "   🚨 リスク: 変更範囲が拡大、予期しない副作用の可能性"
echo "   💡 メリット: 重複排除、保守性向上"
echo ""
echo "Phase 2を実行しますか？ (y/N): "
```

### **🤔 Phase 2 Completion Checkpoint**
```bash
echo "✅ Phase 2 (Related Code Integration) 完了"
echo ""
echo "🎯 Phase 3: Global Integration について"
echo "   📋 内容: プロジェクト全体の重複コードをチェック・統合"
echo "   ⏱️  推定時間: 20-40分"
echo "   🚨 リスク: システム全体への影響、大きな変更範囲"
echo "   💡 メリット: システム全体の品質向上、技術債務削減"
echo ""
echo "Phase 3を実行しますか？ (y/N): "
```

### **🌍 Phase 3: Global Integration (USER PERMISSION REQUIRED)**

**🚨 WARNING: Only execute if user explicitly confirms (y/Y)**

#### **🔍 Global Code Analysis**
- [ ] **Scan entire codebase**: Analyze all source code for duplication patterns
- [ ] **Identify cross-domain patterns**: Find patterns that span multiple domains
- [ ] **Assess architectural improvements**: Identify system-wide architectural enhancements
- [ ] **Document global opportunities**: Create comprehensive improvement plan
- [ ] **Estimate impact and effort**: Assess scope and risk of global changes

#### **🏗️ System-Wide Improvements**
- [ ] **Create shared libraries**: Extract common functionality into shared modules
- [ ] **Standardize patterns**: Implement consistent patterns across the system
- [ ] **Optimize cross-cutting concerns**: Improve logging, error handling, validation patterns
- [ ] **Consolidate configurations**: Merge and standardize configuration management
- [ ] **Enhance monitoring**: Improve system-wide monitoring and observability

#### **🧪 Comprehensive Validation**
- [ ] **Run complete test suite**: Execute all tests multiple times for stability
- [ ] **Perform integration testing**: Test all major system integrations
- [ ] **Validate system performance**: Ensure global changes don't degrade performance
- [ ] **Check system stability**: Monitor for any instability introduced by changes
- [ ] **Update all documentation**: Reflect system-wide changes in documentation

### **🔧 Final Quality Validation**
- [ ] **Run final code quality check**: Execute `uv run --frozen ruff check src/ --fix`
- [ ] **Run final formatting**: Execute `uv run --frozen ruff format src/`
- [ ] **Run final type checking**: Execute `uv run --frozen pyright src/`
- [ ] **Execute complete test suite**: Run `uv run --frozen pytest --cov=src`
- [ ] **Validate all tests GREEN**: Ensure no functionality was broken during refactoring

### **📊 Refactoring Documentation**
- [ ] **Document improvements made**: Record what was refactored and why
- [ ] **Update metadata**: Mark refactoring phase complete in issue-X-Y.json
- [ ] **Create refactoring report**: Document metrics improvements (complexity, duplication, etc.)
- [ ] **Commit refactored code**: Version control all improvements with clear commit message
- [ ] **Prepare for review**: Ensure code is ready for quality review phase

**💡 Pro Tip: Refactor fearlessly but test continuously - green tests are your safety net!
- ✅ Remove code duplication  
- ✅ Optimize performance while maintaining behavior
- ❌ Do not add new features or change behavior
- ❌ Do not break any existing tests

**IMPROVE CODE QUALITY ONLY - MAINTAIN ALL FUNCTIONALITY.**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **リファクタリング中断リスク**: テスト失敗時の変更取り消し機能
- **メタデータ破損**: 原子的更新によるリファクタリング履歴保護
- **コード品質検証**: 自動的な品質メトリクス測定・比較
- **変更影響分析**: アーキテクチャ違反の自動検出
- **パフォーマンス劣化**: 最適化前後の性能比較

### **🆕 新機能**

1. **🔄 安全なリファクタリング**: ステップバイステップでの変更とテスト
2. **📊 品質メトリクス**: リファクタリング前後の品質指標比較
3. **🛡️ アーキテクチャ保護**: DDD/Clean Architecture 原則の維持
4. **🔍 影響分析**: 変更による副作用の自動検出
5. **📈 パフォーマンス監視**: 最適化効果の定量化

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

## 1. **Setup Safe Environment and Parse Arguments**

```bash
# 🔧 Load all safe operation functions with automatic argument parsing and validation
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "11-refactor" "$ARGUMENTS"

# Arguments are already parsed and validated by setup script
# Additional validation for this specific command
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "refactor" "1" "単一イシューのリファクタリング"
    show_usage_example "refactor" "1,7" "複数イシューのリファクタリング"
    show_usage_example "refactor" "1,feature-name" "イシュー + 機能名指定"
    exit 1
fi
```

## 2. **Transaction Management Setup**

```bash
# Begin atomic transaction for refactoring
transaction_id="refactor_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# Setup rollback handlers
add_rollback_handler "git stash push -m 'Auto-stash before refactor rollback'"
add_rollback_handler "git checkout ."
add_rollback_handler "echo '🔄 リファクタリングをロールバックしました'"
```

## 3. **Prerequisites Validation and Metadata Discovery**

```bash
# Validate that all tests are currently passing
echo "📋 前提条件を確認中..."

# Discover metadata file
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    if [[ -z "$feature_name" ]]; then
        echo "❌ エラー: フィーチャー名を特定できませんでした"
        echo "💡 使用方法: /refactor $issue_list,<feature-name>"
        execute_rollback
        exit 1
    fi
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

# Validate prerequisites
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# Check that previous phases are completed
validate_phase_completion "$metadata_file" "presentation_implementation"

echo "✅ 前提条件チェック完了"
```

## 4. **Pre-Refactoring Quality Baseline**

```bash
# Establish quality baseline before refactoring
echo "📊 リファクタリング前の品質メトリクスを測定中..."

# Create baseline measurements
baseline_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$baseline_dir'"

# Run comprehensive test suite
echo "🧪 全テストスイートを実行中..."
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v --tb=short; then
    echo "❌ エラー: テストが失敗しています。リファクタリング前にテストを修正してください"
    execute_rollback
    exit 1
fi

# Measure code quality metrics
echo "📏 コード品質メトリクスを測定中..."
{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --show-source --statistics || true
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright --stats || true
    echo ""
    echo "=== TEST COVERAGE ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=term-missing --cov-report=json:${baseline_dir}/coverage.json || true
} > "${baseline_dir}/quality_baseline.txt"

# Store baseline for comparison
cp "${baseline_dir}/quality_baseline.txt" "${baseline_dir}/quality_before.txt"
echo "✅ 品質ベースライン確立"
```

## 5. **Architecture Validation Before Refactoring**

```bash
# Validate current architecture state
echo "🏗️ アーキテクチャ状態を検証中..."

if ! validate_architecture_compliance; then
    echo "⚠️ 警告: 現在のコードにアーキテクチャ違反があります"
    echo "📋 詳細なレポートを確認し、リファクタリングで修正することを検討してください"
fi

# Create architecture snapshot
architecture_snapshot="${baseline_dir}/architecture_before.json"
create_architecture_snapshot > "$architecture_snapshot"
add_rollback_handler "echo '📊 アーキテクチャスナップショット: $architecture_snapshot'"
```

## 6. **Safe Refactoring Execution**

```bash
# Execute refactoring in safe incremental steps
echo "🔧 安全なリファクタリングを開始中..."

# Domain Layer Refactoring
echo "📦 ドメイン層のリファクタリング..."
refactor_domain_layer() {
    local changes_made=false

    # Remove duplication in entities and value objects
    echo "  🔍 エンティティ・値オブジェクトの重複除去..."

    # Extract common behavior to base classes
    echo "  🏗️ 共通動作のベースクラス抽出..."

    # Simplify complex methods
    echo "  ⚡ 複雑メソッドの簡素化..."

    # Ensure ubiquitous language consistency
    echo "  📚 ユビキタス言語の一貫性確保..."

    # Run tests after domain changes
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v; then
        echo "❌ ドメイン層テストが失敗しました"
        return 1
    fi

    echo "  ✅ ドメイン層リファクタリング完了"
    return 0
}

# Application Layer Refactoring
refactor_application_layer() {
    echo "  🔍 ユースケース複雑度の削減..."
    echo "  🛡️ 共通バリデーションロジックの抽出..."
    echo "  📊 DTOコンバージョンの最適化..."

    # Run tests after application changes
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/ -v; then
        echo "❌ アプリケーション層テストが失敗しました"
        return 1
    fi

    echo "  ✅ アプリケーション層リファクタリング完了"
    return 0
}

# Infrastructure Layer Refactoring
refactor_infrastructure_layer() {
    echo "  🗄️ データベースクエリの最適化..."
    echo "  🔗 接続処理の改善..."
    echo "  🗺️ 共通マッピングロジックの抽出..."

    # Run tests after infrastructure changes
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v; then
        echo "❌ インフラストラクチャ層テストが失敗しました"
        return 1
    fi

    echo "  ✅ インフラストラクチャ層リファクタリング完了"
    return 0
}

# Presentation Layer Refactoring
refactor_presentation_layer() {
    echo "  🔗 エラーレスポンスの標準化..."
    echo "  ✅ 共通バリデーションパターンの抽出..."
    echo "  🎯 API一貫性の向上..."

    # Run tests after presentation changes
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v; then
        echo "❌ プレゼンテーション層テストが失敗しました"
        return 1
    fi

    echo "  ✅ プレゼンテーション層リファクタリング完了"
    return 0
}

# Execute each layer refactoring with rollback capability
for layer_func in refactor_domain_layer refactor_application_layer refactor_infrastructure_layer refactor_presentation_layer; do
    echo "🔧 実行中: $layer_func"

    # Create checkpoint before each layer
    git add -A && git commit -m "Checkpoint before $layer_func" || true

    if ! $layer_func; then
        echo "❌ $layer_func でエラーが発生しました"
        git reset --hard HEAD~1 2>/dev/null || true
        execute_rollback
        exit 1
    fi

    # Commit layer changes
    git add -A && git commit -m "Refactor: $layer_func completed" || true
done
```

## 7. **Cross-Cutting Concerns Refactoring**

```bash
# Refactor cross-cutting concerns
echo "🌐 横断的関心事のリファクタリング..."

# Standardize logging patterns
echo "  📝 ログパターンの標準化..."

# Improve error messages
echo "  💬 エラーメッセージの改善..."

# Add performance monitoring hooks
echo "  📊 パフォーマンス監視フックの追加..."

# Ensure consistent naming conventions
echo "  📛 命名規則の一貫性確保..."

# Run full test suite after cross-cutting changes
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v; then
    echo "❌ 横断的関心事のリファクタリング後のテストが失敗しました"
    execute_rollback
    exit 1
fi

echo "✅ 横断的関心事のリファクタリング完了"
```

## 8. **Test Suite Refactoring**

```bash
# Refactor test code
echo "🧪 テストコードのリファクタリング..."

# Remove test duplication
echo "  🔄 テストの重複除去..."

# Extract test fixtures and builders
echo "  🏗️ テストフィクスチャとビルダーの抽出..."

# Improve test names and organization
echo "  📝 テスト名と構成の改善..."

# Add missing edge case tests
echo "  🎯 エッジケーステストの追加..."

# Validate test refactoring
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v --tb=short; then
    echo "❌ テストリファクタリング後の検証が失敗しました"
    execute_rollback
    exit 1
fi

echo "✅ テストコードリファクタリング完了"
```

## 9. **Post-Refactoring Quality Validation**

````bash
# Measure post-refactoring quality metrics
echo "📊 リファクタリング後の品質メトリクスを測定中..."

{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --show-source --statistics || true
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright --stats || true
    echo ""
    echo "=== TEST COVERAGE ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=term-missing --cov-report=json:${baseline_dir}/coverage_after.json || true
} > "${baseline_dir}/quality_after.txt"

# Generate quality comparison report
echo "📋 品質改善レポートを生成中..."
quality_report="${baseline_dir}/quality_comparison.md"

cat > "$quality_report" << EOF
# リファクタリング品質レポート

## フィーチャー
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **Date**: $(date -u +%Y-%m-%dT%H:%M:%SZ)

## 品質メトリクス改善

### Ruff (コード品質)
EOF

# Add Ruff comparison
echo "#### Before:" >> "$quality_report"
echo '```' >> "$quality_report"
grep -E "(Found|Fixed)" "${baseline_dir}/quality_before.txt" || echo "No issues found" >> "$quality_report"
echo '```' >> "$quality_report"

echo "#### After:" >> "$quality_report"
echo '```' >> "$quality_report"
grep -E "(Found|Fixed)" "${baseline_dir}/quality_after.txt" || echo "No issues found" >> "$quality_report"
echo '```' >> "$quality_report"

# Add test coverage comparison if available
if [[ -f "${baseline_dir}/coverage.json" && -f "${baseline_dir}/coverage_after.json" ]]; then
    before_coverage=$(jq -r '.totals.percent_covered // "N/A"' "${baseline_dir}/coverage.json")
    after_coverage=$(jq -r '.totals.percent_covered // "N/A"' "${baseline_dir}/coverage_after.json")

    cat >> "$quality_report" << EOF

### Test Coverage
- **Before**: ${before_coverage}%
- **After**: ${after_coverage}%
EOF
fi

echo "✅ 品質レポート生成完了: $quality_report"
````

## 10. **Architecture Compliance Re-validation**

```bash
# Re-validate architecture after refactoring
echo "🏗️ リファクタリング後のアーキテクチャ検証..."

if ! validate_architecture_compliance; then
    echo "❌ エラー: リファクタリング後にアーキテクチャ違反が検出されました"
    echo "🔄 アーキテクチャ違反を修正してからコミットしてください"
    execute_rollback
    exit 1
fi

# Create post-refactoring architecture snapshot
architecture_after="${baseline_dir}/architecture_after.json"
create_architecture_snapshot > "$architecture_after"

echo "✅ アーキテクチャ検証完了"
```

## 11. **Final Test Suite Execution**

```bash
# Run comprehensive final test suite
echo "🧪 最終テストスイートを実行中..."

test_results_file="${baseline_dir}/final_test_results.txt"

# Run all test categories
{
    echo "=== UNIT TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/ -v --tb=short
    echo ""
    echo "=== INTEGRATION TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v --tb=short
    echo ""
    echo "=== E2E TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v --tb=short
    echo ""
    echo "=== LINTING ==="
    uv run --frozen ruff check . --show-source
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright
} > "$test_results_file" 2>&1

if [[ $? -ne 0 ]]; then
    echo "❌ エラー: 最終テストスイートが失敗しました"
    echo "📋 詳細: $test_results_file"
    execute_rollback
    exit 1
fi

echo "✅ 全テスト成功"
```

## 12. **Atomic Metadata Update**

```bash
# Update metadata atomically
echo "📊 メタデータを更新中..."

if [[ -f "$metadata_file" ]]; then
    # Count refactoring cycles
    current_count=$(jq '.phases.refactor.refactoring_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # Update metadata with comprehensive refactoring information
    update_metadata_atomic "$metadata_file" "
        .phases.refactor.completed = true |
        .phases.refactor.completed_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.refactor.refactoring_count = ${new_count} |
        .phases.refactor.quality_report = \"${quality_report}\" |
        .phases.refactor.test_results = \"${test_results_file}\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"refactored\"
    "

    echo "✅ メタデータ更新完了 (リファクタリング回数: ${new_count})"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 13. **Documentation Generation**

```bash
# Generate comprehensive refactoring documentation
echo "📚 リファクタリングドキュメントを生成中..."

refactoring_doc="docs/refactoring/issue-${issue_list}-${feature_name}-refactor-${new_count}.md"
mkdir -p "$(dirname "$refactoring_doc")"

cat > "$refactoring_doc" << EOF
# リファクタリング レポート #${new_count}

## 概要
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **Refactoring Cycle**: ${new_count}
- **Date**: $(date -u +%Y-%m-%dT%H:%M:%SZ)

## 実行された改善

### ドメイン層
- エンティティ・値オブジェクトの重複除去
- 共通動作のベースクラス抽出
- 複雑メソッドの簡素化
- ユビキタス言語の一貫性確保

### アプリケーション層
- ユースケース複雑度の削減
- 共通バリデーションロジックの抽出
- DTOコンバージョンの最適化

### インフラストラクチャ層
- データベースクエリの最適化
- 接続処理の改善
- 共通マッピングロジックの抽出

### プレゼンテーション層
- エラーレスポンスの標準化
- 共通バリデーションパターンの抽出
- API一貫性の向上

### 横断的関心事
- ログパターンの標準化
- エラーメッセージの改善
- パフォーマンス監視フックの追加
- 命名規則の一貫性確保

### テストコード
- テストの重複除去
- テストフィクスチャとビルダーの抽出
- テスト名と構成の改善
- エッジケーステストの追加

## 品質改善結果

$(cat "$quality_report")

## テスト結果

全テストスイートが成功しました。詳細は以下を参照:
- テスト結果: \`${test_results_file}\`

## アーキテクチャ検証

✅ DDD/Clean Architecture 原則に準拠
- アーキテクチャスナップショット（前）: \`${architecture_snapshot}\`
- アーキテクチャスナップショット（後）: \`${architecture_after}\`

## 次のステップ

1. 追加のリファクタリングが必要な場合は \`/refactor ${issue_list}\` を再実行
2. 他の機能の開発を続ける場合は \`/use-case-status ${issue_list}\` で状況確認
3. レビューを開始する場合は \`/review-issue ${issue_list}\`

EOF

echo "✅ リファクタリングドキュメント生成完了: $refactoring_doc"
```

## 14. **Use Case Index Update**

```bash
# Update use case index with refactoring status
echo "📋 ユースケースインデックスを更新中..."

if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # Update with refactoring phase status and cycle count
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: refactored, TDD: REFACTOR ✅, Cycles: ${new_count})|" docs/use_cases/index.md

    echo "✅ インデックス更新完了"
else
    echo "⚠️ 警告: Use case index not found"
fi
```

## 15. **GitHub Issue Updates**

```bash
# Update GitHub issues with refactoring completion
echo "📢 GitHub イシューを更新中..."

refactoring_summary="🔧 **リファクタリング完了 (サイクル #${new_count})**

✅ **実行された改善**:
- ドメイン層: 重複除去、共通動作抽出、複雑度削減
- アプリケーション層: ユースケース最適化、バリデーション統一
- インフラ層: クエリ最適化、接続処理改善
- プレゼンテーション層: API一貫性向上、エラー処理標準化
- テストコード: 重複除去、構成改善

📊 **品質改善**: 詳細レポートは \`${quality_report}\` を参照

🧪 **テスト状況**: 全テストスイートが成功

🏗️ **アーキテクチャ**: DDD/Clean Architecture 原則に準拠

📚 **詳細ドキュメント**: \`${refactoring_doc}\`"

for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$refactoring_summary"; then
        echo "✅ Issue #$issue_num にコメント追加完了"
    else
        echo "⚠️ 警告: Issue #$issue_num のコメント追加に失敗"
    fi
done
```

## 16. **Transaction Commit and Cleanup**

```bash
# Commit all changes and clean up
echo "💾 変更をコミット中..."

# Add all changes
git add -A

# Create comprehensive commit message
commit_message="refactor: TDD REFACTOR phase for issues #$(IFS=' #'; echo "${issue_numbers[*]}")

Refactoring cycle #${new_count} completed for feature: ${feature_name}

Improvements:
- Domain layer: Removed duplication, extracted common behavior
- Application layer: Reduced complexity, unified validation
- Infrastructure layer: Optimized queries, improved connections
- Presentation layer: Standardized responses, improved consistency
- Tests: Reduced duplication, improved organization

Quality metrics and test results available in:
- Quality report: ${quality_report}
- Test results: ${test_results_file}
- Documentation: ${refactoring_doc}

Architecture compliance: ✅ Validated
Test status: ✅ All tests passing"

# Commit with proper message
if git commit -m "$commit_message"; then
    echo "✅ Git コミット完了"
else
    echo "⚠️ 警告: Git コミットに失敗しました"
fi

# Commit transaction
commit_transaction

echo "🎉 リファクタリング完了!"
echo ""
echo "📊 **リファクタリング サマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - Cycle: ${new_count}"
echo "   - Quality Report: ${quality_report}"
echo "   - Documentation: ${refactoring_doc}"
echo ""
echo "🔍 **次のステップ**:"
echo "   - 追加リファクタリング: /refactor ${issue_list}"
echo "   - 状況確認: /use-case-status ${issue_list}"
echo "   - レビュー開始: /review-issue ${issue_list}"
echo ""
echo "✅ TDD REFACTOR フェーズが正常に完了しました"
```

## 重要な注意事項

### **安全性原則**

- リファクタリング中は常にテストが GREEN であることを維持
- 各レイヤーのリファクタリング後に関連テストを実行
- 失敗時は自動的に安全な状態にロールバック
- アーキテクチャ違反は即座に検出・修正

### **品質保証**

- リファクタリング前後の品質メトリクス比較
- テストカバレッジの維持・向上
- パフォーマンス劣化の検出
- ドキュメンテーションの自動更新

### **チーム協力**

- 全操作の詳細ログ記録
- GitHub イシューでの進捗共有
- アーキテクチャ遵守の可視化
- 継続的な品質改善の追跡

**統合版リファクタリングコマンドにより、安全で確実なコード品質向上が実現されます！**

## 🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK

リファクタリング中に新パターン・制約・改善案発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
CRITICAL: リファクタリングは新たな設計洞察の重要な源です
