#!/bin/bash
#
# TDD/DDD/Layered Architecture - Task Verification Common Library
# Purpose: Provide unified task verification capabilities for all commands
# Date: 2025-08-20
#

# Source the structure validation utility
source "$(dirname "${BASH_SOURCE[0]}")/_validate_structure.sh"

# Global variables for verification
declare -a verification_issues
declare -a critical_tasks
declare -a critical_patterns

#
# Load task metadata from JSON definition file
#
load_task_metadata() {
    local command_name="$1"
    local metadata_file=".claude/commands/tdd-ddd-layered/task-definitions/${command_name}.json"
    
    # Reset arrays
    critical_tasks=()
    critical_patterns=()
    success_indicators=()
    failure_indicators=()
    
    if [[ -f "$metadata_file" ]]; then
        echo "📋 タスクメタデータ読み込み: $metadata_file"
        
        # Load metadata if jq is available
        if command -v jq >/dev/null 2>&1; then
            # Load critical tasks and patterns
            mapfile -t critical_tasks < <(jq -r '.critical_tasks[]?' "$metadata_file" 2>/dev/null)
            mapfile -t critical_patterns < <(jq -r '.output_requirements.critical_patterns[]?' "$metadata_file" 2>/dev/null)
            
            # Load success and failure indicators
            mapfile -t success_indicators < <(jq -r '.output_requirements.success_indicators[]?' "$metadata_file" 2>/dev/null)
            mapfile -t failure_indicators < <(jq -r '.output_requirements.failure_indicators[]?' "$metadata_file" 2>/dev/null)
            
            echo "   - Critical tasks: ${#critical_tasks[@]} 項目"
            echo "   - Critical patterns: ${#critical_patterns[@]} パターン"
            echo "   - Success indicators: ${#success_indicators[@]} 項目"
            echo "   - Failure indicators: ${#failure_indicators[@]} 項目"
        else
            echo "⚠️ jq コマンドが見つからないため、基本確認のみ実行します"
        fi
    else
        echo "📋 メタデータファイルなし、基本確認のみ実行: $command_name"
    fi
}

#
# Verify critical tasks completion based on patterns
#
verify_critical_tasks() {
    local command_name="$1"
    local report_file="$2"
    
    # Reset verification issues
    verification_issues=()
    
    if [[ ! -f "$report_file" ]]; then
        verification_issues+=("レポートファイルが存在しません: $report_file")
        return 1
    fi
    
    echo "🔍 Critical tasks確認中..."
    
    # Load metadata for this command
    load_task_metadata "$command_name"
    
    # Enhanced pattern-based verification using metadata
    for pattern in "${critical_patterns[@]}"; do
        if ! grep -qP "$pattern" "$report_file"; then
            verification_issues+=("Missing critical pattern: $pattern")
            echo "   ❌ パターンなし: $pattern"
        else
            echo "   ✅ パターン確認: $pattern"
        fi
    done
    
    # Success indicators verification (positive signals)
    success_count=0
    for indicator in "${success_indicators[@]}"; do
        if grep -qP "$indicator" "$report_file"; then
            success_count=$((success_count + 1))
            echo "   ✅ 成功指標: $indicator"
        fi
    done
    
    # Failure indicators check (negative signals)
    failure_count=0
    for indicator in "${failure_indicators[@]}"; do
        if grep -qP "$indicator" "$report_file"; then
            failure_count=$((failure_count + 1))
            verification_issues+=("Failure indicator detected: $indicator")
            echo "   ❌ 失敗指標: $indicator"
        fi
    done
    
    # Required sections verification
    if ! grep -q "📊 実行サマリー\|実行サマリー" "$report_file"; then
        verification_issues+=("実行サマリーセクションが見つかりません")
        echo "   ❌ 実行サマリーセクションなし"
    else
        echo "   ✅ 実行サマリーセクション確認"
    fi
    
    if ! grep -q "📋 総合判定\|総合判定" "$report_file"; then
        verification_issues+=("総合判定セクションが見つかりません")
        echo "   ❌ 総合判定セクションなし"
    else
        echo "   ✅ 総合判定セクション確認"
    fi
    
    # Enhanced status determination
    echo "📊 検証結果: 成功指標 $success_count 件、失敗指標 $failure_count 件"
    
    if [[ ${#verification_issues[@]} -eq 0 ]]; then
        echo "✅ Critical tasks確認完了 - 問題なし"
        return 0
    else
        echo "⚠️ Critical tasks確認完了 - ${#verification_issues[@]} 件の問題あり"
        return 1
    fi
}

#
# Execute agent with retry mechanism
#
execute_agent_with_retry() {
    local agent_type="$1"
    local max_attempts="${2:-2}"
    local latest_report="${3:-}"
    local attempt=1
    
    while [[ $attempt -le $max_attempts ]]; do
        echo "🔄 エージェント実行試行 $attempt/$max_attempts..."
        
        # Execute the agent (implementation depends on specific command)
        # This function is meant to be called from individual commands
        # where the actual Task execution happens
        
        if [[ -n "$latest_report" && -f "$latest_report" ]]; then
            if verify_critical_tasks "$agent_type" "$latest_report"; then
                echo "✅ エージェント実行成功 (試行 $attempt)"
                return 0
            else
                echo "⚠️ 結果不十分 - 再試行準備中..."
                if [[ $attempt -lt $max_attempts ]]; then
                    prepare_retry_context "$attempt" "${verification_issues[@]}"
                fi
            fi
        else
            echo "❌ レポートファイルが生成されていません: $latest_report"
        fi
        
        ((attempt++))
        sleep 2
    done
    
    echo "❌ 最大試行回数に達しました"
    return 1
}

#
# Prepare retry context with previous issues for improvement
#
prepare_retry_context() {
    local command_name="$1" 
    local attempt="$2"
    shift 2
    local issues=("$@")
    local context_file="/workspace/.claude/context/current-command-context.json"
    
    # Create context directory if needed
    mkdir -p "$(dirname "$context_file")"
    
    # Join issues into a string
    local issues_str
    if [[ ${#issues[@]} -gt 0 ]]; then
        issues_str=$(IFS=', '; echo "${issues[*]}")
    else
        issues_str="一般的な品質向上"
    fi
    
    # Load metadata for enhanced context
    load_task_metadata "$command_name" >/dev/null 2>&1
    
    # Build retry guidance from metadata
    local metadata_file=".claude/commands/tdd-ddd-layered/task-definitions/${command_name}.json"
    local focus_areas=""
    local common_issues=""
    
    if [[ -f "$metadata_file" ]] && command -v jq >/dev/null 2>&1; then
        focus_areas=$(jq -r '.retry_context.focus_areas[]?' "$metadata_file" 2>/dev/null | tr '\n' ',' | sed 's/,$//')
        common_issues=$(jq -r '.retry_context.common_issues[]?' "$metadata_file" 2>/dev/null | tr '\n' ',' | sed 's/,$//')
    fi
    
    # Create or update context file with enhanced metadata
    if [[ -f "$context_file" ]] && command -v jq >/dev/null 2>&1; then
        # Update existing context with metadata
        jq --arg attempt "$attempt" \
           --arg issues "$issues_str" \
           --arg focus_areas "$focus_areas" \
           --arg common_issues "$common_issues" \
           --arg special_focus "前回の不足項目に特に注意: $issues_str" \
           '. + {
             "retry_attempt": $attempt,
             "previous_issues": $issues,
             "special_focus": $special_focus,
             "metadata_focus_areas": ($focus_areas | split(",") | map(select(. != ""))),
             "metadata_common_issues": ($common_issues | split(",") | map(select(. != ""))),
             "enhanced_guidance": true
           }' "$context_file" > "${context_file}.tmp" && \
        mv "${context_file}.tmp" "$context_file"
    else
        # Create new context with metadata
        cat > "$context_file" <<EOF
{
  "retry_attempt": "$attempt",
  "previous_issues": "$issues_str",
  "special_focus": "前回の不足項目に特に注意: $issues_str",
  "metadata_focus_areas": $(echo "$focus_areas" | jq -R 'split(",") | map(select(. != ""))' 2>/dev/null || echo '[]'),
  "metadata_common_issues": $(echo "$common_issues" | jq -R 'split(",") | map(select(. != ""))' 2>/dev/null || echo '[]'),
  "enhanced_guidance": true,
  "timestamp": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
}
EOF
    fi
    
    echo "📝 再試行コンテキスト更新 (メタデータ強化): $context_file"
    if [[ -n "$focus_areas" ]]; then
        echo "   🎯 重点領域: $focus_areas"
    fi
    if [[ -n "$common_issues" ]]; then
        echo "   ⚠️ 一般的な問題: $common_issues"
    fi
}

#
# Basic verification for commands without metadata
#
basic_verification() {
    local report_file="$1"
    local command_name="${2:-unknown}"
    
    verification_issues=()
    
    if [[ ! -f "$report_file" ]]; then
        verification_issues+=("レポートファイルが存在しません: $report_file")
        return 1
    fi
    
    # Basic file content check
    if [[ ! -s "$report_file" ]]; then
        verification_issues+=("レポートファイルが空です")
        return 1
    fi
    
    # Look for basic success indicators
    if grep -q "エラー\|ERROR\|失敗" "$report_file"; then
        echo "⚠️ エラーの可能性が検出されました"
    fi
    
    if grep -q "完了\|成功\|SUCCESS\|✅" "$report_file"; then
        echo "✅ 成功指標が検出されました"
        return 0
    fi
    
    echo "📋 基本確認完了: $command_name"
    return 0
}

#
# Show verification results summary
#
show_verification_results() {
    local command_name="$1"
    
    echo ""
    echo "📊 $command_name 検証結果サマリー:"
    echo "   - 検証問題: ${#verification_issues[@]} 件"
    
    if [[ ${#verification_issues[@]} -gt 0 ]]; then
        echo "   - 検出された問題:"
        for issue in "${verification_issues[@]}"; do
            echo "     • $issue"
        done
    else
        echo "   - ステータス: ✅ すべての確認項目をクリア"
    fi
    echo ""
}

#
# Helper function to find latest report file in common locations
#
find_latest_report() {
    local base_pattern="$1"
    local search_dirs=(
        "/workspace/reports"
        "/workspace/.claude/reports"
        "/workspace/docs/reports"
        "/workspace"
    )
    
    for dir in "${search_dirs[@]}"; do
        if [[ -d "$dir" ]]; then
            # Find latest matching file
            local latest_file
            latest_file=$(find "$dir" -name "*$base_pattern*" -type f -printf '%T@ %p\n' 2>/dev/null | sort -n | tail -1 | cut -d' ' -f2-)
            if [[ -n "$latest_file" && -f "$latest_file" ]]; then
                echo "$latest_file"
                return 0
            fi
        fi
    done
    
    return 1
}

# Export functions for use in commands
export -f load_task_metadata
export -f verify_critical_tasks
export -f execute_agent_with_retry
export -f prepare_retry_context
export -f basic_verification
export -f show_verification_results
export -f find_latest_report

echo "🔧 Task Verification Library loaded successfully"