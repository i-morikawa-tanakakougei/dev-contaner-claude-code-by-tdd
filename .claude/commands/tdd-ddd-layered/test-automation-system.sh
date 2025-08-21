#!/bin/bash
#
# TDD/DDD/Layered Architecture - Test Automation System
# Purpose: Automated testing of task verification system functionality
# Usage: ./test-automation-system.sh [test-suite-name]
#

# Configuration
TEST_DIR="/workspace/.claude/test-automation"
REPORT_DIR="/workspace/.claude/test-automation/reports"
LOG_FILE="/workspace/.claude/test-automation/test-automation.log"

# Test suites
declare -A TEST_SUITES=(
    ["basic"]="基本機能テスト"
    ["metadata"]="メタデータ駆動テスト"
    ["verification"]="検証機能テスト"
    ["integration"]="統合テスト"
    ["all"]="全テストスイート"
)

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Initialize test environment
init_test_environment() {
    echo -e "${BLUE}🔧 テスト環境初期化中...${NC}"
    
    # Create test directories
    mkdir -p "$TEST_DIR"/{reports,fixtures,temp}
    mkdir -p "$REPORT_DIR"
    
    # Initialize log file
    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - Test automation system initialized" > "$LOG_FILE"
    
    echo -e "${GREEN}✅ テスト環境初期化完了${NC}"
}

# Log function
log_message() {
    local level="$1"
    local message="$2"
    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") - [$level] $message" >> "$LOG_FILE"
}

# Test basic task verification library functionality
test_basic_functionality() {
    echo -e "${BLUE}📋 基本機能テスト実行中...${NC}"
    log_message "INFO" "Starting basic functionality tests"
    
    local test_results=()
    local passed=0
    local total=0
    
    # Test 1: Library loading
    ((total++))
    echo -n "  • ライブラリ読み込みテスト... "
    if source ".claude/commands/tdd-ddd-layered/_task_verification.sh" 2>/dev/null; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Library loading: PASS")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Library loading: FAIL")
    fi
    
    # Test 2: Function export verification
    ((total++))
    echo -n "  • 関数エクスポート確認... "
    if type verify_critical_tasks >/dev/null 2>&1; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Function export: PASS")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Function export: FAIL")
    fi
    
    # Test 3: Metadata loading
    ((total++))
    echo -n "  • メタデータ読み込みテスト... "
    if load_task_metadata "04.5-review-domain-design" >/dev/null 2>&1; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Metadata loading: PASS")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Metadata loading: FAIL")
    fi
    
    # Generate report
    cat > "$REPORT_DIR/basic-functionality-$(date +%Y%m%d-%H%M%S).md" <<EOF
# 基本機能テスト結果

**実行日時**: $(date)
**テスト成功率**: ${passed}/${total} ($(( passed * 100 / total ))%)

## テスト結果詳細
$(printf '%s\n' "${test_results[@]}")

## ステータス
$([ $passed -eq $total ] && echo "✅ 全テスト合格" || echo "❌ テスト失敗あり")
EOF
    
    log_message "INFO" "Basic functionality tests completed: ${passed}/${total}"
    return $([ $passed -eq $total ] && echo 0 || echo 1)
}

# Test metadata-driven functionality
test_metadata_functionality() {
    echo -e "${BLUE}📊 メタデータ駆動テスト実行中...${NC}"
    log_message "INFO" "Starting metadata-driven tests"
    
    local test_results=()
    local passed=0
    local total=0
    
    # Load library
    source ".claude/commands/tdd-ddd-layered/_task_verification.sh" 2>/dev/null
    
    # Test metadata files exist
    local metadata_files=(
        "04.5-review-domain-design.json"
        "05.5-review-test-design.json"
        "10.5-review-test-results.json"
        "12-evolve-scenarios.json"
    )
    
    for metadata_file in "${metadata_files[@]}"; do
        ((total++))
        echo -n "  • メタデータファイル確認 ($metadata_file)... "
        if [[ -f ".claude/commands/tdd-ddd-layered/task-definitions/$metadata_file" ]]; then
            echo -e "${GREEN}PASS${NC}"
            test_results+=("Metadata file $metadata_file: PASS")
            ((passed++))
        else
            echo -e "${RED}FAIL${NC}"
            test_results+=("Metadata file $metadata_file: FAIL")
        fi
    done
    
    # Test enhanced verification with mock data
    ((total++))
    echo -n "  • 強化検証機能テスト... "
    
    # Create mock report
    mkdir -p "$TEST_DIR/temp"
    cat > "$TEST_DIR/temp/mock-report.md" <<EOF
# テストレポート

## 📊 実行サマリー
- ✅ **DDD準拠性確認**: 適切
- ✅ **集約境界検証**: 良好

## 📋 総合判定
**APPROVED** - 実装開始可能

## 💡 次のステップ
実装を開始してください
EOF
    
    if verify_critical_tasks "04.5-review-domain-design" "$TEST_DIR/temp/mock-report.md" >/dev/null 2>&1; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Enhanced verification: PASS")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Enhanced verification: FAIL")
    fi
    
    # Generate report
    cat > "$REPORT_DIR/metadata-functionality-$(date +%Y%m%d-%H%M%S).md" <<EOF
# メタデータ駆動テスト結果

**実行日時**: $(date)
**テスト成功率**: ${passed}/${total} ($(( passed * 100 / total ))%)

## テスト結果詳細
$(printf '%s\n' "${test_results[@]}")

## ステータス
$([ $passed -eq $total ] && echo "✅ 全テスト合格" || echo "❌ テスト失敗あり")
EOF
    
    # Cleanup
    rm -rf "$TEST_DIR/temp"
    
    log_message "INFO" "Metadata-driven tests completed: ${passed}/${total}"
    return $([ $passed -eq $total ] && echo 0 || echo 1)
}

# Test verification functionality
test_verification_functionality() {
    echo -e "${BLUE}🔍 検証機能テスト実行中...${NC}"
    log_message "INFO" "Starting verification functionality tests"
    
    local test_results=()
    local passed=0
    local total=0
    
    # Load library
    source ".claude/commands/tdd-ddd-layered/_task_verification.sh" 2>/dev/null
    
    # Test different report scenarios
    mkdir -p "$TEST_DIR/temp"
    
    # Test 1: Successful report
    ((total++))
    echo -n "  • 成功レポート検証... "
    cat > "$TEST_DIR/temp/success-report.md" <<EOF
# 成功テストレポート
## 📊 実行サマリー
- ✅ **DDD準拠性確認**: 適切
## 📋 総合判定
**APPROVED**
## 💡 次のステップ
実装開始
ドメイン設計レビュー完了
EOF
    
    if verify_critical_tasks "04.5-review-domain-design" "$TEST_DIR/temp/success-report.md" >/dev/null 2>&1; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Success report verification: PASS")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Success report verification: FAIL")
    fi
    
    # Test 2: Failed report
    ((total++))
    echo -n "  • 失敗レポート検証... "
    cat > "$TEST_DIR/temp/fail-report.md" <<EOF
# 失敗テストレポート
## 内容
問題が検出されました
EOF
    
    if ! verify_critical_tasks "04.5-review-domain-design" "$TEST_DIR/temp/fail-report.md" >/dev/null 2>&1; then
        echo -e "${GREEN}PASS${NC}"
        test_results+=("Fail report verification: PASS (correctly failed)")
        ((passed++))
    else
        echo -e "${RED}FAIL${NC}"
        test_results+=("Fail report verification: FAIL (should have failed)")
    fi
    
    # Generate report
    cat > "$REPORT_DIR/verification-functionality-$(date +%Y%m%d-%H%M%S).md" <<EOF
# 検証機能テスト結果

**実行日時**: $(date)
**テスト成功率**: ${passed}/${total} ($(( passed * 100 / total ))%)

## テスト結果詳細
$(printf '%s\n' "${test_results[@]}")

## ステータス
$([ $passed -eq $total ] && echo "✅ 全テスト合格" || echo "❌ テスト失敗あり")
EOF
    
    # Cleanup
    rm -rf "$TEST_DIR/temp"
    
    log_message "INFO" "Verification functionality tests completed: ${passed}/${total}"
    return $([ $passed -eq $total ] && echo 0 || echo 1)
}

# Run integration tests
test_integration() {
    echo -e "${BLUE}🔗 統合テスト実行中...${NC}"
    log_message "INFO" "Starting integration tests"
    
    # Run all component tests
    local overall_result=0
    
    test_basic_functionality || overall_result=1
    test_metadata_functionality || overall_result=1
    test_verification_functionality || overall_result=1
    
    # Generate integration report
    cat > "$REPORT_DIR/integration-test-$(date +%Y%m%d-%H%M%S).md" <<EOF
# 統合テスト結果

**実行日時**: $(date)

## テストスイート実行結果
- 基本機能テスト: $(test_basic_functionality >/dev/null 2>&1 && echo "✅ PASS" || echo "❌ FAIL")
- メタデータ駆動テスト: $(test_metadata_functionality >/dev/null 2>&1 && echo "✅ PASS" || echo "❌ FAIL")
- 検証機能テスト: $(test_verification_functionality >/dev/null 2>&1 && echo "✅ PASS" || echo "❌ FAIL")

## 総合ステータス
$([ $overall_result -eq 0 ] && echo "✅ 全統合テスト合格" || echo "❌ 統合テスト失敗")

## 推奨アクション
$([ $overall_result -eq 0 ] && echo "システムは正常に動作しています" || echo "失敗したテストの詳細を確認し、修正してください")
EOF
    
    log_message "INFO" "Integration tests completed with result: $overall_result"
    return $overall_result
}

# Main function
main() {
    local test_suite="${1:-all}"
    
    echo -e "${BLUE}🚀 タスク確認システム自動テスト開始${NC}"
    echo -e "${BLUE}テストスイート: ${TEST_SUITES[$test_suite]}${NC}"
    echo ""
    
    init_test_environment
    
    case "$test_suite" in
        "basic")
            test_basic_functionality
            ;;
        "metadata") 
            test_metadata_functionality
            ;;
        "verification")
            test_verification_functionality
            ;;
        "integration")
            test_integration
            ;;
        "all")
            echo -e "${YELLOW}📊 全テストスイート実行中...${NC}"
            test_integration
            ;;
        *)
            echo -e "${RED}❌ 不明なテストスイート: $test_suite${NC}"
            echo "利用可能なテストスイート: ${!TEST_SUITES[@]}"
            exit 1
            ;;
    esac
    
    local exit_code=$?
    
    echo ""
    echo -e "${BLUE}📈 テスト実行完了${NC}"
    echo -e "レポート場所: $REPORT_DIR"
    echo -e "ログファイル: $LOG_FILE"
    
    if [ $exit_code -eq 0 ]; then
        echo -e "${GREEN}🎉 全テスト合格!${NC}"
    else
        echo -e "${RED}❌ テスト失敗あり${NC}"
    fi
    
    exit $exit_code
}

# Check if script is being executed directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi