#!/bin/bash

# トランザクション フレームワーク
# 複数ステップ操作の原子性とロールバック機能を提供

set -euo pipefail

# トランザクション管理変数
declare -g TRANSACTION_ACTIVE=false
declare -g TRANSACTION_ID=""
declare -ga ROLLBACK_OPERATIONS=()
declare -g TRANSACTION_LOG=""

# トランザクション ログ記録
log_transaction() {
    local operation="$1"
    local status="$2"
    local details="${3:-}"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    TRANSACTION_LOG+="[$timestamp] TX:$TRANSACTION_ID $operation: $status"
    if [[ -n "$details" ]]; then
        TRANSACTION_LOG+=" - $details"
    fi
    TRANSACTION_LOG+=$'\n'
}

# トランザクション開始
begin_transaction() {
    local transaction_name="$1"
    
    if [[ "$TRANSACTION_ACTIVE" == "true" ]]; then
        echo "エラー: 既にトランザクションが実行中です: $TRANSACTION_ID" >&2
        return 1
    fi
    
    TRANSACTION_ID="${transaction_name}_$(date +%s)"
    TRANSACTION_ACTIVE=true
    ROLLBACK_OPERATIONS=()
    
    echo "🔄 トランザクション開始: $TRANSACTION_ID"
    log_transaction "begin" "success" "transaction started"
    return 0
}

# ロールバック操作の追加
add_rollback() {
    local rollback_command="$1"
    local description="${2:-}"
    
    if [[ "$TRANSACTION_ACTIVE" != "true" ]]; then
        echo "警告: トランザクション外でロールバック操作が追加されました" >&2
        return 1
    fi
    
    ROLLBACK_OPERATIONS=("$rollback_command" "${ROLLBACK_OPERATIONS[@]}")
    
    if [[ -n "$description" ]]; then
        log_transaction "add_rollback" "success" "$description"
    else
        log_transaction "add_rollback" "success" "rollback operation added"
    fi
}

# ロールバック実行
execute_rollback() {
    local reason="${1:-manual}"
    
    if [[ "$TRANSACTION_ACTIVE" != "true" ]]; then
        echo "警告: トランザクション外でロールバックが実行されました" >&2
        return 0
    fi
    
    echo "🔄 ロールバック実行中: $TRANSACTION_ID (理由: $reason)"
    log_transaction "rollback_start" "info" "reason: $reason"
    
    local rollback_count=0
    local rollback_errors=0
    
    for operation in "${ROLLBACK_OPERATIONS[@]}"; do
        ((rollback_count++))
        echo "  実行中 ($rollback_count/${#ROLLBACK_OPERATIONS[@]}): $operation"
        
        if eval "$operation" 2>/dev/null; then
            log_transaction "rollback_step" "success" "step $rollback_count: $operation"
        else
            ((rollback_errors++))
            echo "  ⚠️  ロールバック操作失敗: $operation" >&2
            log_transaction "rollback_step" "failed" "step $rollback_count: $operation"
        fi
    done
    
    if [[ $rollback_errors -eq 0 ]]; then
        echo "✅ ロールバック完了: 全 $rollback_count 操作成功"
        log_transaction "rollback_complete" "success" "$rollback_count operations completed"
    else
        echo "⚠️  ロールバック完了: $rollback_errors/$rollback_count 操作でエラー" >&2
        log_transaction "rollback_complete" "partial" "$rollback_errors errors in $rollback_count operations"
    fi
    
    # トランザクション状態リセット
    TRANSACTION_ACTIVE=false
    ROLLBACK_OPERATIONS=()
    return 0
}

# トランザクション コミット
commit_transaction() {
    if [[ "$TRANSACTION_ACTIVE" != "true" ]]; then
        echo "エラー: コミットするトランザクションがありません" >&2
        return 1
    fi
    
    echo "✅ トランザクション コミット: $TRANSACTION_ID"
    log_transaction "commit" "success" "transaction committed successfully"
    
    # 成功時はロールバック情報をクリア
    TRANSACTION_ACTIVE=false
    ROLLBACK_OPERATIONS=()
    return 0
}

# トランザクション状態確認
check_transaction_status() {
    if [[ "$TRANSACTION_ACTIVE" == "true" ]]; then
        echo "🔄 アクティブなトランザクション: $TRANSACTION_ID"
        echo "   ロールバック操作数: ${#ROLLBACK_OPERATIONS[@]}"
        return 0
    else
        echo "💤 アクティブなトランザクションはありません"
        return 1
    fi
}

# 安全な操作実行（トランザクション対応）
safe_execute_with_rollback() {
    local operation_name="$1"
    local execute_command="$2"
    local rollback_command="$3"
    local description="${4:-$operation_name}"
    
    echo "🔧 実行中: $description"
    
    # 実行
    if eval "$execute_command"; then
        echo "  ✅ 成功: $description"
        
        # ロールバック操作を追加（トランザクション内の場合のみ）
        if [[ "$TRANSACTION_ACTIVE" == "true" ]]; then
            add_rollback "$rollback_command" "$description"
        fi
        
        log_transaction "execute" "success" "$description"
        return 0
    else
        echo "  ❌ 失敗: $description" >&2
        log_transaction "execute" "failed" "$description"
        
        # トランザクション内の場合は自動ロールバック
        if [[ "$TRANSACTION_ACTIVE" == "true" ]]; then
            execute_rollback "operation_failed"
        fi
        
        return 1
    fi
}

# 複数ステップ操作の実行
execute_multi_step_operation() {
    local operation_name="$1"
    shift
    
    # ステップ定義の解析 (execute_cmd:rollback_cmd:description の形式)
    local steps=("$@")
    
    if ! begin_transaction "$operation_name"; then
        return 1
    fi
    
    echo "🚀 複数ステップ操作開始: $operation_name (${#steps[@]} ステップ)"
    
    local step_count=0
    for step_definition in "${steps[@]}"; do
        ((step_count++))
        
        # ステップ定義を分割
        IFS=':' read -ra STEP_PARTS <<< "$step_definition"
        local execute_cmd="${STEP_PARTS[0]}"
        local rollback_cmd="${STEP_PARTS[1]:-}"
        local description="${STEP_PARTS[2]:-Step $step_count}"
        
        echo "📋 ステップ $step_count/${#steps[@]}: $description"
        
        if ! safe_execute_with_rollback "step_$step_count" "$execute_cmd" "$rollback_cmd" "$description"; then
            echo "❌ 複数ステップ操作失敗: $operation_name (ステップ $step_count で失敗)" >&2
            return 1
        fi
    done
    
    if commit_transaction; then
        echo "🎉 複数ステップ操作完了: $operation_name"
        return 0
    else
        echo "❌ トランザクション コミット失敗: $operation_name" >&2
        return 1
    fi
}

# トランザクション ログの表示
show_transaction_log() {
    if [[ -n "$TRANSACTION_LOG" ]]; then
        echo "トランザクション ログ:"
        echo "$TRANSACTION_LOG"
    else
        echo "トランザクション ログはありません"
    fi
}

# 緊急停止ハンドラー
emergency_rollback() {
    if [[ "$TRANSACTION_ACTIVE" == "true" ]]; then
        echo ""
        echo "🚨 緊急停止検出 - ロールバック実行中..."
        execute_rollback "emergency_stop"
    fi
}

# シグナル ハンドラー設定
trap emergency_rollback EXIT INT TERM

# トランザクション使用例
example_transaction() {
    echo "📚 トランザクション使用例:"
    echo ""
    echo "# 基本的な使用方法"
    echo "begin_transaction \"feature_implementation\""
    echo "safe_execute_with_rollback \"create_branch\" \"git checkout -b feature\" \"git checkout main; git branch -D feature\""
    echo "safe_execute_with_rollback \"create_file\" \"echo 'content' > file.txt\" \"rm -f file.txt\""
    echo "commit_transaction"
    echo ""
    echo "# 複数ステップ操作"
    echo "execute_multi_step_operation \"complex_operation\" \\"
    echo "  \"git checkout -b feature:git checkout main; git branch -D feature:Create feature branch\" \\"
    echo "  \"echo 'content' > file.txt:rm -f file.txt:Create file\" \\"
    echo "  \"git add file.txt:git reset HEAD file.txt:Stage file\""
}

# ヘルプ表示
if [[ "${1:-}" == "--help" ]] || [[ "${1:-}" == "-h" ]]; then
    example_transaction
fi