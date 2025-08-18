#!/bin/bash

# Git操作の安全な実行関数群
# エラーハンドリングとロールバック機能を提供

set -euo pipefail

# Git操作の結果を格納する変数
declare -g GIT_OPERATION_LOG=""

# ログ記録関数
log_git_operation() {
    local operation="$1"
    local status="$2"
    local details="${3:-}"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    GIT_OPERATION_LOG+="[$timestamp] $operation: $status"
    if [[ -n "$details" ]]; then
        GIT_OPERATION_LOG+=" - $details"
    fi
    GIT_OPERATION_LOG+=$'\n'
}

# 安全なブランチ作成または切り替え
safe_create_or_switch_branch() {
    local branch_name="$1"
    local base_branch="${2:-main}"
    
    echo "ブランチ操作を実行中: $branch_name"
    
    # 現在のブランチを記録
    local current_branch
    current_branch=$(git branch --show-current 2>/dev/null || echo "")
    
    # ブランチ名の妥当性チェック
    if ! [[ "$branch_name" =~ ^[a-zA-Z0-9/_-]+$ ]]; then
        echo "エラー: 無効なブランチ名です: $branch_name" >&2
        log_git_operation "create_branch" "failed" "invalid branch name: $branch_name"
        return 1
    fi
    
    # 既存ブランチの確認
    if git show-ref --verify --quiet "refs/heads/$branch_name"; then
        echo "ブランチ '$branch_name' が既に存在します。切り替えます。"
        
        # 未コミット変更の確認
        if ! git diff-index --quiet HEAD --; then
            echo "警告: 未コミットの変更があります。" >&2
            echo "変更をコミットまたはスタッシュしてからブランチを切り替えることを推奨します。" >&2
            read -p "続行しますか？ (y/N): " -n 1 -r
            echo
            if [[ ! $REPLY =~ ^[Yy]$ ]]; then
                log_git_operation "switch_branch" "cancelled" "user cancelled due to uncommitted changes"
                return 1
            fi
        fi
        
        if ! git checkout "$branch_name"; then
            echo "エラー: ブランチ '$branch_name' への切り替えに失敗しました" >&2
            log_git_operation "switch_branch" "failed" "checkout failed: $branch_name"
            return 1
        fi
        
        log_git_operation "switch_branch" "success" "switched to existing branch: $branch_name"
        echo "ブランチ '$branch_name' に切り替えました"
        return 0
    fi
    
    # 新規ブランチ作成
    echo "新しいブランチ '$branch_name' を作成します (ベース: $base_branch)"
    
    # ベースブランチの存在確認
    if ! git show-ref --verify --quiet "refs/heads/$base_branch" && 
       ! git show-ref --verify --quiet "refs/remotes/origin/$base_branch"; then
        echo "エラー: ベースブランチ '$base_branch' が存在しません" >&2
        log_git_operation "create_branch" "failed" "base branch not found: $base_branch"
        return 1
    fi
    
    # ベースブランチが最新か確認（リモートブランチが存在する場合）
    if git show-ref --verify --quiet "refs/remotes/origin/$base_branch"; then
        local local_hash
        local remote_hash
        local_hash=$(git rev-parse "refs/heads/$base_branch" 2>/dev/null || echo "")
        remote_hash=$(git rev-parse "refs/remotes/origin/$base_branch" 2>/dev/null || echo "")
        
        if [[ -n "$local_hash" ]] && [[ -n "$remote_hash" ]] && [[ "$local_hash" != "$remote_hash" ]]; then
            echo "警告: ローカルの '$base_branch' がリモートと異なります" >&2
            echo "最新の変更を取得することを推奨します: git pull origin $base_branch" >&2
        fi
    fi
    
    # ブランチ作成と切り替え
    if ! git checkout -b "$branch_name" "$base_branch"; then
        echo "エラー: ブランチ '$branch_name' の作成に失敗しました" >&2
        log_git_operation "create_branch" "failed" "checkout -b failed: $branch_name from $base_branch"
        return 1
    fi
    
    log_git_operation "create_branch" "success" "created and switched to: $branch_name from $base_branch"
    echo "ブランチ '$branch_name' を作成し、切り替えました"
    return 0
}

# 安全なコミット実行
safe_git_commit() {
    local commit_message="$1"
    local files_to_add=("${@:2}")
    
    echo "コミット操作を実行中..."
    
    # コミットメッセージの妥当性チェック
    if [[ -z "$commit_message" ]]; then
        echo "エラー: コミットメッセージが空です" >&2
        log_git_operation "commit" "failed" "empty commit message"
        return 1
    fi
    
    # コミットメッセージの長さチェック
    if [[ ${#commit_message} -gt 200 ]]; then
        echo "警告: コミットメッセージが長すぎます (${#commit_message}文字)" >&2
    fi
    
    # ファイル追加
    if [[ ${#files_to_add[@]} -gt 0 ]]; then
        echo "ファイルをステージング: ${files_to_add[*]}"
        
        for file in "${files_to_add[@]}"; do
            if [[ ! -e "$file" ]]; then
                echo "警告: ファイルが存在しません: $file" >&2
                continue
            fi
            
            if ! git add "$file"; then
                echo "エラー: ファイルの追加に失敗しました: $file" >&2
                log_git_operation "add" "failed" "failed to add: $file"
                return 1
            fi
        done
        
        log_git_operation "add" "success" "added files: ${files_to_add[*]}"
    fi
    
    # ステージされた変更の確認
    if git diff-index --quiet --cached HEAD --; then
        echo "コミットする変更がありません"
        log_git_operation "commit" "skipped" "no changes to commit"
        return 0
    fi
    
    # 変更内容の表示
    echo "コミット予定の変更:"
    git diff --cached --stat
    
    # コミット実行
    if ! git commit -m "$commit_message"; then
        echo "エラー: コミットに失敗しました" >&2
        log_git_operation "commit" "failed" "commit command failed"
        return 1
    fi
    
    log_git_operation "commit" "success" "committed: $commit_message"
    echo "コミットが完了しました"
    return 0
}

# 安全なプッシュ実行
safe_git_push() {
    local branch_name="${1:-}"
    local force_push="${2:-false}"
    
    echo "プッシュ操作を実行中..."
    
    # 現在のブランチ取得
    if [[ -z "$branch_name" ]]; then
        branch_name=$(git branch --show-current 2>/dev/null || echo "")
        if [[ -z "$branch_name" ]]; then
            echo "エラー: 現在のブランチ名を取得できません" >&2
            log_git_operation "push" "failed" "could not determine current branch"
            return 1
        fi
    fi
    
    # リモート接続確認
    if ! git ls-remote --exit-code origin &>/dev/null; then
        echo "エラー: リモートリポジトリに接続できません" >&2
        log_git_operation "push" "failed" "remote connection failed"
        return 1
    fi
    
    # アップストリームブランチの確認
    local upstream_branch
    upstream_branch=$(git rev-parse --abbrev-ref "$branch_name@{upstream}" 2>/dev/null || echo "")
    
    if [[ -z "$upstream_branch" ]]; then
        echo "アップストリームブランチが設定されていません。新しいブランチとしてプッシュします。"
        
        if ! git push -u origin "$branch_name"; then
            echo "エラー: ブランチ '$branch_name' のプッシュに失敗しました" >&2
            log_git_operation "push" "failed" "push -u failed: $branch_name"
            return 1
        fi
        
        log_git_operation "push" "success" "pushed new branch with upstream: $branch_name"
        echo "ブランチ '$branch_name' をプッシュし、アップストリームを設定しました"
        return 0
    fi
    
    # 強制プッシュの場合
    if [[ "$force_push" == "true" ]]; then
        echo "警告: 強制プッシュを実行します" >&2
        read -p "続行しますか？ (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            log_git_operation "push" "cancelled" "user cancelled force push"
            return 1
        fi
        
        if ! git push --force-with-lease origin "$branch_name"; then
            echo "エラー: 強制プッシュに失敗しました" >&2
            log_git_operation "push" "failed" "force push failed: $branch_name"
            return 1
        fi
        
        log_git_operation "push" "success" "force pushed: $branch_name"
        echo "強制プッシュが完了しました"
        return 0
    fi
    
    # 通常のプッシュ
    if ! git push origin "$branch_name"; then
        echo "エラー: プッシュに失敗しました" >&2
        log_git_operation "push" "failed" "push failed: $branch_name"
        return 1
    fi
    
    log_git_operation "push" "success" "pushed: $branch_name"
    echo "プッシュが完了しました"
    return 0
}

# 作業ディレクトリの状態確認
check_working_directory_clean() {
    if ! git diff-index --quiet HEAD --; then
        echo "作業ディレクトリに未コミットの変更があります:"
        git status --porcelain
        return 1
    fi
    
    if ! git diff-index --quiet --cached HEAD --; then
        echo "ステージングエリアに変更があります:"
        git diff --cached --name-only
        return 1
    fi
    
    return 0
}

# Git操作のロールバック（簡易版）
rollback_git_operation() {
    local operation_type="$1"
    local target="${2:-}"
    
    echo "ロールバックを実行中: $operation_type"
    
    case "$operation_type" in
        "commit")
            if [[ -n "$target" ]] && git show-ref --verify --quiet "refs/heads/$target"; then
                echo "最新のコミットを取り消します"
                git reset --soft HEAD~1
                log_git_operation "rollback" "success" "rolled back commit"
            fi
            ;;
        "branch")
            if [[ -n "$target" ]] && git show-ref --verify --quiet "refs/heads/$target"; then
                echo "ブランチ '$target' を削除します"
                git branch -D "$target"
                log_git_operation "rollback" "success" "deleted branch: $target"
            fi
            ;;
        *)
            echo "警告: サポートされていないロールバック操作: $operation_type" >&2
            log_git_operation "rollback" "failed" "unsupported operation: $operation_type"
            return 1
            ;;
    esac
}

# Git操作ログの表示
show_git_operation_log() {
    if [[ -n "$GIT_OPERATION_LOG" ]]; then
        echo "Git操作ログ:"
        echo "$GIT_OPERATION_LOG"
    else
        echo "Git操作ログはありません"
    fi
}

# リモートブランチとの同期確認
check_remote_sync() {
    local branch_name="${1:-$(git branch --show-current)}"
    
    if [[ -z "$branch_name" ]]; then
        echo "エラー: ブランチ名を取得できません" >&2
        return 1
    fi
    
    # リモートブランチの存在確認
    if ! git show-ref --verify --quiet "refs/remotes/origin/$branch_name"; then
        echo "リモートブランチが存在しません: origin/$branch_name"
        return 0
    fi
    
    # ローカルとリモートの差分確認
    local ahead_count
    local behind_count
    
    ahead_count=$(git rev-list --count "origin/$branch_name..$branch_name" 2>/dev/null || echo "0")
    behind_count=$(git rev-list --count "$branch_name..origin/$branch_name" 2>/dev/null || echo "0")
    
    if [[ "$ahead_count" -gt 0 ]]; then
        echo "ローカルブランチがリモートより $ahead_count コミット進んでいます"
    fi
    
    if [[ "$behind_count" -gt 0 ]]; then
        echo "ローカルブランチがリモートより $behind_count コミット遅れています"
        echo "git pull を実行することを推奨します"
    fi
    
    if [[ "$ahead_count" -eq 0 ]] && [[ "$behind_count" -eq 0 ]]; then
        echo "ローカルとリモートのブランチは同期されています"
    fi
}