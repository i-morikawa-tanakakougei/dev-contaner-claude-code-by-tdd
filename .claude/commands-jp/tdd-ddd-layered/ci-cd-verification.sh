#!/bin/bash
#
# TDD/DDD/Layered Architecture - CI/CD Verification Script
# Purpose: Continuous Integration/Deployment verification for task verification system
# Usage: ./ci-cd-verification.sh [environment] [check-type]
#

set -euo pipefail

# Configuration
SCRIPT_DIR="$(dirname "${BASH_SOURCE[0]}")"
PROJECT_ROOT="/workspace"
CI_REPORT_DIR="$PROJECT_ROOT/.claude/ci-reports"
LOG_FILE="$CI_REPORT_DIR/ci-cd-$(date +%Y%m%d-%H%M%S).log"

# Environment types
declare -A ENVIRONMENTS=(
    ["dev"]="開発環境"
    ["staging"]="ステージング環境"  
    ["prod"]="本番環境"
)

# Check types
declare -A CHECK_TYPES=(
    ["quick"]="クイックチェック (基本検証)"
    ["full"]="フルチェック (全検証)"
    ["security"]="セキュリティチェック"
    ["performance"]="パフォーマンステスト"
)

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

# Initialize CI/CD environment
init_ci_environment() {
    echo -e "${BLUE}🔧 CI/CD環境初期化中...${NC}"
    
    # Create necessary directories
    mkdir -p "$CI_REPORT_DIR"
    mkdir -p "$PROJECT_ROOT/.claude/ci-cache"
    
    # Initialize log
    {
        echo "=================================="
        echo "CI/CD Verification Session Start"
        echo "Time: $(date -u +"%Y-%m-%dT%H:%M:%SZ")"
        echo "Environment: ${1:-dev}"
        echo "Check Type: ${2:-quick}"
        echo "=================================="
    } > "$LOG_FILE"
    
    echo -e "${GREEN}✅ CI/CD環境初期化完了${NC}"
}

# Log function
log_ci() {
    local level="$1"
    local message="$2"
    echo "$(date -u +"%Y-%m-%dT%H:%M:%SZ") [$level] $message" >> "$LOG_FILE"
    
    case "$level" in
        "ERROR") echo -e "${RED}❌ $message${NC}" ;;
        "WARN")  echo -e "${YELLOW}⚠️ $message${NC}" ;;
        "INFO")  echo -e "${BLUE}ℹ️ $message${NC}" ;;
        "SUCCESS") echo -e "${GREEN}✅ $message${NC}" ;;
    esac
}

# Pre-deployment checks
pre_deployment_checks() {
    log_ci "INFO" "Pre-deployment checks starting"
    
    local checks_passed=0
    local total_checks=0
    
    # Check 1: Task verification library exists
    ((total_checks++))
    if [[ -f "$SCRIPT_DIR/_task_verification.sh" ]]; then
        log_ci "SUCCESS" "Task verification library found"
        ((checks_passed++))
    else
        log_ci "ERROR" "Task verification library missing"
        return 1
    fi
    
    # Check 2: Metadata files exist
    ((total_checks++))
    local metadata_count=$(find "$SCRIPT_DIR/task-definitions" -name "*.json" 2>/dev/null | wc -l)
    if [[ $metadata_count -ge 4 ]]; then
        log_ci "SUCCESS" "Sufficient metadata files found ($metadata_count files)"
        ((checks_passed++))
    else
        log_ci "ERROR" "Insufficient metadata files ($metadata_count files)"
        return 1
    fi
    
    # Check 3: Core commands have verification
    ((total_checks++))
    local verified_commands=0
    for cmd in "04.5-review-domain-design.md" "05.5-review-test-design.md" "10.5-review-test-results.md"; do
        if grep -q "_task_verification.sh" "$SCRIPT_DIR/$cmd" 2>/dev/null; then
            ((verified_commands++))
        fi
    done
    
    if [[ $verified_commands -ge 3 ]]; then
        log_ci "SUCCESS" "Core commands have verification ($verified_commands/3)"
        ((checks_passed++))
    else
        log_ci "ERROR" "Core commands missing verification ($verified_commands/3)"
        return 1
    fi
    
    # Check 4: Test automation system
    ((total_checks++))
    if [[ -x "$SCRIPT_DIR/test-automation-system.sh" ]]; then
        log_ci "SUCCESS" "Test automation system is executable"
        ((checks_passed++))
    else
        log_ci "ERROR" "Test automation system not executable"
        return 1
    fi
    
    log_ci "INFO" "Pre-deployment checks completed: $checks_passed/$total_checks"
    return $([ $checks_passed -eq $total_checks ] && echo 0 || echo 1)
}

# Run automated tests
run_ci_tests() {
    log_ci "INFO" "Running CI tests"
    
    # Run test automation system
    if "$SCRIPT_DIR/test-automation-system.sh" all >> "$LOG_FILE" 2>&1; then
        log_ci "SUCCESS" "All automated tests passed"
        return 0
    else
        log_ci "ERROR" "Automated tests failed - see logs for details"
        return 1
    fi
}

# Security checks
security_checks() {
    log_ci "INFO" "Running security checks"
    
    local security_issues=0
    
    # Check 1: No sensitive data in scripts
    if grep -r "password\|secret\|key\|token" "$SCRIPT_DIR" --include="*.sh" --include="*.md" >/dev/null 2>&1; then
        log_ci "WARN" "Potential sensitive data found in scripts"
        ((security_issues++))
    else
        log_ci "SUCCESS" "No sensitive data patterns found"
    fi
    
    # Check 2: Executable permissions are appropriate
    local executable_files=$(find "$SCRIPT_DIR" -type f -executable 2>/dev/null | wc -l)
    if [[ $executable_files -le 3 ]]; then
        log_ci "SUCCESS" "Executable file count is reasonable ($executable_files)"
    else
        log_ci "WARN" "High number of executable files ($executable_files)"
        ((security_issues++))
    fi
    
    # Check 3: No world-writable files
    if find "$SCRIPT_DIR" -type f -perm -o+w 2>/dev/null | grep -q .; then
        log_ci "ERROR" "World-writable files found"
        ((security_issues++))
    else
        log_ci "SUCCESS" "No world-writable files found"
    fi
    
    log_ci "INFO" "Security checks completed with $security_issues issues"
    return $security_issues
}

# Performance checks
performance_checks() {
    log_ci "INFO" "Running performance checks"
    
    # Time task verification library loading
    local load_start=$(date +%s%N)
    source "$SCRIPT_DIR/_task_verification.sh" >/dev/null 2>&1
    local load_end=$(date +%s%N)
    local load_time=$(( (load_end - load_start) / 1000000 )) # Convert to milliseconds
    
    if [[ $load_time -lt 1000 ]]; then
        log_ci "SUCCESS" "Library loading is fast (${load_time}ms)"
    else
        log_ci "WARN" "Library loading is slow (${load_time}ms)"
    fi
    
    # Check metadata file sizes
    local total_metadata_size=$(find "$SCRIPT_DIR/task-definitions" -name "*.json" -exec stat -c%s {} \; 2>/dev/null | awk '{sum+=$1} END {print sum}')
    total_metadata_size=${total_metadata_size:-0}
    
    if [[ $total_metadata_size -lt 50000 ]]; then # 50KB
        log_ci "SUCCESS" "Metadata files are reasonable size (${total_metadata_size} bytes)"
    else
        log_ci "WARN" "Metadata files are large (${total_metadata_size} bytes)"
    fi
    
    log_ci "INFO" "Performance checks completed"
    return 0
}

# Generate deployment report
generate_deployment_report() {
    local environment="$1"
    local check_type="$2"
    local overall_status="$3"
    
    cat > "$CI_REPORT_DIR/deployment-report-$(date +%Y%m%d-%H%M%S).md" <<EOF
# CI/CD Verification Report

**Environment**: ${ENVIRONMENTS[$environment]:-$environment}
**Check Type**: ${CHECK_TYPES[$check_type]:-$check_type}
**Execution Time**: $(date)
**Overall Status**: $([ "$overall_status" = "0" ] && echo "✅ SUCCESS" || echo "❌ FAILURE")

## Verification Summary

### Pre-deployment Checks
$(pre_deployment_checks >/dev/null 2>&1 && echo "✅ PASSED" || echo "❌ FAILED")

### Automated Tests  
$(run_ci_tests >/dev/null 2>&1 && echo "✅ PASSED" || echo "❌ FAILED")

### Security Checks
$(security_checks >/dev/null 2>&1 && echo "✅ PASSED" || echo "⚠️ WARNINGS")

### Performance Checks
$(performance_checks >/dev/null 2>&1 && echo "✅ PASSED" || echo "⚠️ ISSUES")

## System Status
- Task Verification Library: $([ -f "$SCRIPT_DIR/_task_verification.sh" ] && echo "✅ Active" || echo "❌ Missing")
- Metadata System: $([ -d "$SCRIPT_DIR/task-definitions" ] && echo "✅ Active" || echo "❌ Missing")
- Test Automation: $([ -x "$SCRIPT_DIR/test-automation-system.sh" ] && echo "✅ Active" || echo "❌ Missing")

## Next Steps
$([ "$overall_status" = "0" ] && echo "✅ System ready for deployment" || echo "❌ Address issues before deployment")

## Detailed Logs
See: $LOG_FILE
EOF
    
    log_ci "INFO" "Deployment report generated: $CI_REPORT_DIR/deployment-report-$(date +%Y%m%d-%H%M%S).md"
}

# Main CI/CD verification function
main() {
    local environment="${1:-dev}"
    local check_type="${2:-quick}"
    
    # Validate arguments
    if [[ ! "${ENVIRONMENTS[$environment]+isset}" ]]; then
        echo -e "${RED}❌ Invalid environment: $environment${NC}"
        echo "Available environments: ${!ENVIRONMENTS[@]}"
        exit 1
    fi
    
    if [[ ! "${CHECK_TYPES[$check_type]+isset}" ]]; then
        echo -e "${RED}❌ Invalid check type: $check_type${NC}"
        echo "Available check types: ${!CHECK_TYPES[@]}"
        exit 1
    fi
    
    echo -e "${BLUE}🚀 CI/CD Verification Starting${NC}"
    echo -e "Environment: ${ENVIRONMENTS[$environment]}"
    echo -e "Check Type: ${CHECK_TYPES[$check_type]}"
    echo ""
    
    init_ci_environment "$environment" "$check_type"
    
    local overall_status=0
    
    # Run checks based on type
    case "$check_type" in
        "quick")
            pre_deployment_checks || overall_status=1
            run_ci_tests || overall_status=1
            ;;
        "full")
            pre_deployment_checks || overall_status=1
            run_ci_tests || overall_status=1
            security_checks || overall_status=1
            performance_checks || overall_status=1
            ;;
        "security")
            pre_deployment_checks || overall_status=1
            security_checks || overall_status=1
            ;;
        "performance")
            pre_deployment_checks || overall_status=1
            performance_checks || overall_status=1
            ;;
    esac
    
    generate_deployment_report "$environment" "$check_type" "$overall_status"
    
    echo ""
    if [ $overall_status -eq 0 ]; then
        echo -e "${GREEN}🎉 CI/CD Verification Successful${NC}"
    else
        echo -e "${RED}❌ CI/CD Verification Failed${NC}"
    fi
    
    echo -e "Detailed report: $CI_REPORT_DIR/"
    echo -e "Logs: $LOG_FILE"
    
    exit $overall_status
}

# Execute if run directly
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    main "$@"
fi