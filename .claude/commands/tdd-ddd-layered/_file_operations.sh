#!/bin/bash

# 安全なファイル操作関数群
# エラーハンドリングとバックアップ機能を提供

set -euo pipefail

# ファイル操作ログ
declare -g FILE_OPERATION_LOG=""

# ログ記録関数
log_file_operation() {
    local operation="$1"
    local target="$2"
    local status="$3"
    local details="${4:-}"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    FILE_OPERATION_LOG+="[$timestamp] $operation $target: $status"
    if [[ -n "$details" ]]; then
        FILE_OPERATION_LOG+=" - $details"
    fi
    FILE_OPERATION_LOG+=$'\n'
}

# 安全なディレクトリ作成
safe_mkdir() {
    local dir_path="$1"
    local mode="${2:-755}"
    
    echo "ディレクトリ作成: $dir_path"
    
    # パス検証
    if [[ -z "$dir_path" ]]; then
        echo "エラー: ディレクトリパスが空です" >&2
        log_file_operation "mkdir" "$dir_path" "failed" "empty path"
        return 1
    fi
    
    # 既存チェック
    if [[ -d "$dir_path" ]]; then
        echo "ディレクトリは既に存在します: $dir_path"
        log_file_operation "mkdir" "$dir_path" "exists" "directory already exists"
        return 0
    fi
    
    # 親ディレクトリの確認
    local parent_dir
    parent_dir=$(dirname "$dir_path")
    
    if [[ ! -d "$parent_dir" ]]; then
        echo "親ディレクトリを作成します: $parent_dir"
        if ! mkdir -p "$parent_dir"; then
            echo "エラー: 親ディレクトリの作成に失敗しました: $parent_dir" >&2
            log_file_operation "mkdir" "$dir_path" "failed" "parent directory creation failed"
            return 1
        fi
    fi
    
    # ディレクトリ作成
    if ! mkdir -m "$mode" "$dir_path"; then
        echo "エラー: ディレクトリの作成に失敗しました: $dir_path" >&2
        log_file_operation "mkdir" "$dir_path" "failed" "mkdir command failed"
        return 1
    fi
    
    log_file_operation "mkdir" "$dir_path" "success" "mode: $mode"
    echo "ディレクトリを作成しました: $dir_path"
    return 0
}

# 安全なファイル作成
safe_create_file() {
    local file_path="$1"
    local content="${2:-}"
    local backup="${3:-true}"
    
    echo "ファイル作成: $file_path"
    
    # パス検証
    if [[ -z "$file_path" ]]; then
        echo "エラー: ファイルパスが空です" >&2
        log_file_operation "create" "$file_path" "failed" "empty path"
        return 1
    fi
    
    # 既存ファイルのバックアップ
    if [[ -f "$file_path" ]] && [[ "$backup" == "true" ]]; then
        local backup_file="${file_path}.backup.$(date +%Y%m%d_%H%M%S)"
        echo "既存ファイルをバックアップ: $backup_file"
        
        if ! cp "$file_path" "$backup_file"; then
            echo "警告: バックアップの作成に失敗しました" >&2
            log_file_operation "backup" "$file_path" "failed" "backup creation failed"
        else
            log_file_operation "backup" "$file_path" "success" "backup: $backup_file"
        fi
    fi
    
    # 親ディレクトリの確認・作成
    local parent_dir
    parent_dir=$(dirname "$file_path")
    
    if [[ ! -d "$parent_dir" ]]; then
        if ! safe_mkdir "$parent_dir"; then
            log_file_operation "create" "$file_path" "failed" "parent directory creation failed"
            return 1
        fi
    fi
    
    # ファイル作成
    if ! echo -n "$content" > "$file_path"; then
        echo "エラー: ファイルの作成に失敗しました: $file_path" >&2
        log_file_operation "create" "$file_path" "failed" "write operation failed"
        return 1
    fi
    
    # 権限設定
    if ! chmod 644 "$file_path"; then
        echo "警告: ファイル権限の設定に失敗しました: $file_path" >&2
    fi
    
    log_file_operation "create" "$file_path" "success" "size: $(wc -c < "$file_path") bytes"
    echo "ファイルを作成しました: $file_path"
    return 0
}

# 安全なファイル移動
safe_move_file() {
    local src_path="$1"
    local dest_path="$2"
    local backup="${3:-true}"
    
    echo "ファイル移動: $src_path -> $dest_path"
    
    # ソースファイル存在確認
    if [[ ! -f "$src_path" ]]; then
        echo "エラー: ソースファイルが存在しません: $src_path" >&2
        log_file_operation "move" "$src_path" "failed" "source file not found"
        return 1
    fi
    
    # 既存ファイルのバックアップ
    if [[ -f "$dest_path" ]] && [[ "$backup" == "true" ]]; then
        local backup_file="${dest_path}.backup.$(date +%Y%m%d_%H%M%S)"
        echo "既存ファイルをバックアップ: $backup_file"
        
        if ! cp "$dest_path" "$backup_file"; then
            echo "警告: バックアップの作成に失敗しました" >&2
        else
            log_file_operation "backup" "$dest_path" "success" "backup: $backup_file"
        fi
    fi
    
    # 移動先ディレクトリの確認・作成
    local dest_dir
    dest_dir=$(dirname "$dest_path")
    
    if [[ ! -d "$dest_dir" ]]; then
        if ! safe_mkdir "$dest_dir"; then
            log_file_operation "move" "$src_path" "failed" "destination directory creation failed"
            return 1
        fi
    fi
    
    # ファイル移動
    if ! mv "$src_path" "$dest_path"; then
        echo "エラー: ファイルの移動に失敗しました: $src_path -> $dest_path" >&2
        log_file_operation "move" "$src_path" "failed" "mv command failed"
        return 1
    fi
    
    log_file_operation "move" "$src_path" "success" "moved to: $dest_path"
    echo "ファイルを移動しました: $dest_path"
    return 0
}

# 安全なファイル削除
safe_remove_file() {
    local file_path="$1"
    local backup="${2:-true}"
    
    echo "ファイル削除: $file_path"
    
    # ファイル存在確認
    if [[ ! -f "$file_path" ]]; then
        echo "警告: ファイルが存在しません: $file_path"
        log_file_operation "remove" "$file_path" "skipped" "file not found"
        return 0
    fi
    
    # バックアップ作成
    if [[ "$backup" == "true" ]]; then
        local backup_file="${file_path}.deleted.$(date +%Y%m%d_%H%M%S)"
        echo "削除前にバックアップを作成: $backup_file"
        
        if ! cp "$file_path" "$backup_file"; then
            echo "エラー: バックアップの作成に失敗しました" >&2
            log_file_operation "remove" "$file_path" "failed" "backup creation failed"
            return 1
        else
            log_file_operation "backup" "$file_path" "success" "deletion backup: $backup_file"
        fi
    fi
    
    # ファイル削除
    if ! rm "$file_path"; then
        echo "エラー: ファイルの削除に失敗しました: $file_path" >&2
        log_file_operation "remove" "$file_path" "failed" "rm command failed"
        return 1
    fi
    
    log_file_operation "remove" "$file_path" "success" "file deleted"
    echo "ファイルを削除しました: $file_path"
    return 0
}

# ディスク容量チェック
check_disk_space() {
    local target_dir="${1:-.}"
    local required_mb="${2:-100}"
    
    echo "ディスク容量チェック: $target_dir (必要: ${required_mb}MB)"
    
    # df コマンドでディスク使用量を取得
    local available_kb
    available_kb=$(df "$target_dir" | awk 'NR==2 {print $4}')
    
    if [[ -z "$available_kb" ]] || ! [[ "$available_kb" =~ ^[0-9]+$ ]]; then
        echo "警告: ディスク容量の取得に失敗しました" >&2
        return 1
    fi
    
    local available_mb=$((available_kb / 1024))
    local required_kb=$((required_mb * 1024))
    
    echo "利用可能容量: ${available_mb}MB"
    
    if [[ $available_kb -lt $required_kb ]]; then
        echo "エラー: ディスク容量が不足しています (必要: ${required_mb}MB, 利用可能: ${available_mb}MB)" >&2
        return 1
    fi
    
    echo "✅ ディスク容量OK"
    return 0
}

# ファイル権限チェック
check_file_permissions() {
    local file_path="$1"
    local operation="${2:-read}"
    
    case "$operation" in
        "read")
            if [[ ! -r "$file_path" ]]; then
                echo "エラー: ファイル読み取り権限がありません: $file_path" >&2
                return 1
            fi
            ;;
        "write")
            if [[ -f "$file_path" ]] && [[ ! -w "$file_path" ]]; then
                echo "エラー: ファイル書き込み権限がありません: $file_path" >&2
                return 1
            fi
            
            # 親ディレクトリの書き込み権限チェック
            local parent_dir
            parent_dir=$(dirname "$file_path")
            if [[ ! -w "$parent_dir" ]]; then
                echo "エラー: ディレクトリ書き込み権限がありません: $parent_dir" >&2
                return 1
            fi
            ;;
        "execute")
            if [[ ! -x "$file_path" ]]; then
                echo "エラー: ファイル実行権限がありません: $file_path" >&2
                return 1
            fi
            ;;
        *)
            echo "エラー: 不明な権限チェック操作: $operation" >&2
            return 1
            ;;
    esac
    
    return 0
}

# ファイル整合性チェック
verify_file_integrity() {
    local file_path="$1"
    local expected_size="${2:-}"
    local expected_hash="${3:-}"
    
    echo "ファイル整合性チェック: $file_path"
    
    if [[ ! -f "$file_path" ]]; then
        echo "エラー: ファイルが存在しません: $file_path" >&2
        return 1
    fi
    
    # サイズチェック
    if [[ -n "$expected_size" ]]; then
        local actual_size
        actual_size=$(wc -c < "$file_path")
        
        if [[ "$actual_size" != "$expected_size" ]]; then
            echo "エラー: ファイルサイズが一致しません (期待: $expected_size, 実際: $actual_size)" >&2
            return 1
        fi
        
        echo "✅ ファイルサイズOK: $actual_size bytes"
    fi
    
    # ハッシュチェック
    if [[ -n "$expected_hash" ]]; then
        local actual_hash
        actual_hash=$(sha256sum "$file_path" | cut -d' ' -f1)
        
        if [[ "$actual_hash" != "$expected_hash" ]]; then
            echo "エラー: ファイルハッシュが一致しません" >&2
            echo "期待: $expected_hash" >&2
            echo "実際: $actual_hash" >&2
            return 1
        fi
        
        echo "✅ ファイルハッシュOK"
    fi
    
    return 0
}

# 一時ファイル管理
create_temp_file() {
    local prefix="${1:-tmp}"
    local suffix="${2:-}"
    
    local temp_file
    temp_file=$(mktemp "/tmp/${prefix}.XXXXXX${suffix}")
    
    if [[ -z "$temp_file" ]] || [[ ! -f "$temp_file" ]]; then
        echo "エラー: 一時ファイルの作成に失敗しました" >&2
        return 1
    fi
    
    echo "$temp_file"
    log_file_operation "create_temp" "$temp_file" "success" "temporary file created"
}

# クリーンアップ関数
cleanup_temp_files() {
    local temp_pattern="${1:-/tmp/tmp.*}"
    local max_age_minutes="${2:-60}"
    
    echo "一時ファイルクリーンアップ実行中..."
    
    # 指定した時間より古い一時ファイルを削除
    find /tmp -name "$(basename "$temp_pattern")" -type f -mmin +$max_age_minutes -delete 2>/dev/null || true
    
    echo "一時ファイルクリーンアップ完了"
}

# ファイル操作ログの表示
show_file_operation_log() {
    if [[ -n "$FILE_OPERATION_LOG" ]]; then
        echo "ファイル操作ログ:"
        echo "$FILE_OPERATION_LOG"
    else
        echo "ファイル操作ログはありません"
    fi
}

# ファイル操作の安全性チェック
verify_safe_operation() {
    local operation="$1"
    local target="$2"
    local min_disk_space="${3:-50}"
    
    echo "操作前安全性チェック: $operation $target"
    
    # ディスク容量チェック
    if ! check_disk_space "$(dirname "$target")" "$min_disk_space"; then
        return 1
    fi
    
    # パス検証（危険なパターンの検出）
    if [[ "$target" =~ \.\./|^/etc/|^/usr/|^/bin/|^/sbin/ ]]; then
        echo "エラー: 危険なパスが検出されました: $target" >&2
        return 1
    fi
    
    # 権限チェック
    case "$operation" in
        "create"|"write"|"move")
            local parent_dir
            parent_dir=$(dirname "$target")
            if [[ ! -w "$parent_dir" ]]; then
                echo "エラー: 書き込み権限がありません: $parent_dir" >&2
                return 1
            fi
            ;;
        "read")
            if [[ ! -r "$target" ]]; then
                echo "エラー: 読み取り権限がありません: $target" >&2
                return 1
            fi
            ;;
    esac
    
    echo "✅ 安全性チェックOK"
    return 0
}