#!/bin/bash

# GitHub CLI 安全操作ラッパー
# エラーハンドリング、レート制限、リトライ機能を提供

set -euo pipefail

# GitHub API ログ
declare -g GITHUB_OPERATION_LOG=""

# ログ記録関数
log_github_operation() {
    local operation="$1"
    local status="$2"
    local details="${3:-}"
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    GITHUB_OPERATION_LOG+="[$timestamp] GitHub $operation: $status"
    if [[ -n "$details" ]]; then
        GITHUB_OPERATION_LOG+=" - $details"
    fi
    GITHUB_OPERATION_LOG+=$'\n'
}

# GitHub CLI 認証確認
check_github_auth() {
    echo "GitHub 認証状態を確認中..."
    
    if ! command -v gh &> /dev/null; then
        echo "エラー: GitHub CLI (gh) がインストールされていません" >&2
        log_github_operation "auth_check" "failed" "gh command not found"
        return 1
    fi
    
    if ! gh auth status &>/dev/null; then
        echo "エラー: GitHub CLI が認証されていません" >&2
        echo "認証方法: gh auth login" >&2
        log_github_operation "auth_check" "failed" "not authenticated"
        return 1
    fi
    
    # スコープ確認
    local auth_info
    auth_info=$(gh auth status 2>&1 || echo "")
    
    if ! echo "$auth_info" | grep -q "repo"; then
        echo "警告: リポジトリ操作に必要なスコープがない可能性があります" >&2
    fi
    
    log_github_operation "auth_check" "success" "authenticated"
    echo "✅ GitHub 認証OK"
    return 0
}

# レート制限チェック
check_rate_limit() {
    echo "GitHub API レート制限を確認中..."
    
    local rate_info
    if ! rate_info=$(gh api rate_limit 2>/dev/null); then
        echo "警告: レート制限情報の取得に失敗しました" >&2
        return 0  # 続行可能
    fi
    
    local remaining
    remaining=$(echo "$rate_info" | jq -r '.rate.remaining' 2>/dev/null || echo "unknown")
    
    if [[ "$remaining" != "unknown" ]] && [[ "$remaining" -lt 10 ]]; then
        echo "警告: GitHub API レート制限残り少数: $remaining" >&2
        local reset_time
        reset_time=$(echo "$rate_info" | jq -r '.rate.reset' 2>/dev/null || echo "unknown")
        if [[ "$reset_time" != "unknown" ]]; then
            echo "リセット時刻: $(date -d "@$reset_time")" >&2
        fi
    fi
    
    log_github_operation "rate_limit_check" "success" "remaining: $remaining"
    return 0
}

# GitHub コマンドの安全実行
safe_gh_command() {
    local command="$1"
    shift
    local max_retries=3
    local retry_count=0
    local base_delay=2
    
    echo "GitHub コマンド実行: gh $command $*"
    
    # 事前チェック
    if ! check_github_auth; then
        return 1
    fi
    
    check_rate_limit  # 警告のみ、エラーでは停止しない
    
    # リトライ実行
    while [[ $retry_count -lt $max_retries ]]; do
        local start_time=$(date +%s)
        
        if gh "$command" "$@" 2>/dev/null; then
            local end_time=$(date +%s)
            local duration=$((end_time - start_time))
            log_github_operation "$command" "success" "duration: ${duration}s, attempt: $((retry_count + 1))"
            echo "✅ GitHub コマンド成功"
            return 0
        else
            local error_code=$?
            ((retry_count++))
            
            echo "GitHub API エラー (試行 $retry_count/$max_retries)" >&2
            log_github_operation "$command" "retry" "attempt $retry_count failed with code $error_code"
            
            if [[ $retry_count -lt $max_retries ]]; then
                local delay=$((base_delay * retry_count))
                echo "待機中... ${delay}秒" >&2
                sleep $delay
            fi
        fi
    done
    
    echo "エラー: GitHub コマンドが最大試行回数後も失敗しました: gh $command $*" >&2
    log_github_operation "$command" "failed" "max retries exceeded"
    return 1
}

# イシュー作成（トランザクション対応）
safe_create_issue() {
    local title="$1"
    local body="$2"
    local labels="${3:-}"
    local assignees="${4:-}"
    
    echo "GitHub イシュー作成中..."
    
    # 引数検証
    if [[ -z "$title" ]]; then
        echo "エラー: イシュータイトルが空です" >&2
        return 1
    fi
    
    # イシュー作成コマンド構築
    local create_args=("--title" "$title" "--body" "$body")
    
    if [[ -n "$labels" ]]; then
        create_args+=("--label" "$labels")
    fi
    
    if [[ -n "$assignees" ]]; then
        create_args+=("--assignee" "$assignees")
    fi
    
    # イシュー作成実行
    local issue_output
    if issue_output=$(safe_gh_command "issue" "create" "${create_args[@]}"); then
        # イシュー番号抽出
        local issue_number
        issue_number=$(echo "$issue_output" | grep -oE '#[0-9]+' | head -1 | tr -d '#')
        
        if [[ -n "$issue_number" ]]; then
            echo "✅ イシュー作成成功: #$issue_number"
            echo "$issue_number"  # 戻り値
            log_github_operation "create_issue" "success" "issue #$issue_number created"
            return 0
        else
            echo "エラー: イシュー番号の抽出に失敗しました" >&2
            log_github_operation "create_issue" "failed" "could not extract issue number"
            return 1
        fi
    else
        echo "エラー: イシュー作成に失敗しました" >&2
        log_github_operation "create_issue" "failed" "issue creation failed"
        return 1
    fi
}

# イシュー コメント追加
safe_add_issue_comment() {
    local issue_number="$1"
    local comment_body="$2"
    
    echo "イシュー #$issue_number にコメント追加中..."
    
    # 引数検証
    if [[ -z "$issue_number" ]] || ! [[ "$issue_number" =~ ^[0-9]+$ ]]; then
        echo "エラー: 無効なイシュー番号: $issue_number" >&2
        return 1
    fi
    
    if [[ -z "$comment_body" ]]; then
        echo "エラー: コメント内容が空です" >&2
        return 1
    fi
    
    # イシュー存在確認
    if ! safe_gh_command "issue" "view" "$issue_number" >/dev/null; then
        echo "エラー: イシュー #$issue_number が存在しません" >&2
        return 1
    fi
    
    # コメント追加実行
    if safe_gh_command "issue" "comment" "$issue_number" "--body" "$comment_body"; then
        echo "✅ コメント追加成功: #$issue_number"
        log_github_operation "add_comment" "success" "comment added to issue #$issue_number"
        return 0
    else
        echo "エラー: コメント追加に失敗しました" >&2
        log_github_operation "add_comment" "failed" "comment addition failed for issue #$issue_number"
        return 1
    fi
}

# プルリクエスト作成
safe_create_pull_request() {
    local title="$1"
    local body="$2"
    local base_branch="${3:-main}"
    local head_branch="${4:-$(git branch --show-current)}"
    
    echo "プルリクエスト作成中: $head_branch → $base_branch"
    
    # 引数検証
    if [[ -z "$title" ]]; then
        echo "エラー: PRタイトルが空です" >&2
        return 1
    fi
    
    if [[ -z "$head_branch" ]]; then
        echo "エラー: ヘッドブランチが特定できません" >&2
        return 1
    fi
    
    # ブランチ存在確認
    if ! git show-ref --verify --quiet "refs/heads/$head_branch"; then
        echo "エラー: ヘッドブランチが存在しません: $head_branch" >&2
        return 1
    fi
    
    # 差分確認
    if ! git diff --quiet "$base_branch..$head_branch"; then
        echo "✅ ブランチ間に差分があります"
    else
        echo "警告: ブランチ間に差分がありません" >&2
    fi
    
    # PR作成実行
    local pr_output
    if pr_output=$(safe_gh_command "pr" "create" "--title" "$title" "--body" "$body" "--base" "$base_branch" "--head" "$head_branch"); then
        # PR番号抽出
        local pr_number
        pr_number=$(echo "$pr_output" | grep -oE '#[0-9]+' | head -1 | tr -d '#')
        
        if [[ -n "$pr_number" ]]; then
            echo "✅ プルリクエスト作成成功: #$pr_number"
            echo "$pr_number"  # 戻り値
            log_github_operation "create_pr" "success" "PR #$pr_number created"
            return 0
        else
            echo "エラー: PR番号の抽出に失敗しました" >&2
            log_github_operation "create_pr" "failed" "could not extract PR number"
            return 1
        fi
    else
        echo "エラー: プルリクエスト作成に失敗しました" >&2
        log_github_operation "create_pr" "failed" "PR creation failed"
        return 1
    fi
}

# イシュー情報取得
safe_get_issue_info() {
    local issue_number="$1"
    local format="${2:-json}"
    
    echo "イシュー #$issue_number の情報取得中..."
    
    # 引数検証
    if [[ -z "$issue_number" ]] || ! [[ "$issue_number" =~ ^[0-9]+$ ]]; then
        echo "エラー: 無効なイシュー番号: $issue_number" >&2
        return 1
    fi
    
    # イシュー情報取得
    case "$format" in
        "json")
            if safe_gh_command "issue" "view" "$issue_number" "--json" "title,body,state,number,url"; then
                log_github_operation "get_issue_info" "success" "retrieved info for issue #$issue_number (json)"
                return 0
            fi
            ;;
        "plain")
            if safe_gh_command "issue" "view" "$issue_number"; then
                log_github_operation "get_issue_info" "success" "retrieved info for issue #$issue_number (plain)"
                return 0
            fi
            ;;
        *)
            echo "エラー: 無効なフォーマット: $format" >&2
            return 1
            ;;
    esac
    
    echo "エラー: イシュー情報の取得に失敗しました" >&2
    log_github_operation "get_issue_info" "failed" "failed to retrieve info for issue #$issue_number"
    return 1
}

# GitHub操作ログの表示
show_github_operation_log() {
    if [[ -n "$GITHUB_OPERATION_LOG" ]]; then
        echo "GitHub 操作ログ:"
        echo "$GITHUB_OPERATION_LOG"
    else
        echo "GitHub 操作ログはありません"
    fi
}

# リポジトリ情報の取得
get_repository_info() {
    echo "リポジトリ情報取得中..."
    
    local repo_info
    if repo_info=$(safe_gh_command "repo" "view" "--json" "name,owner,url,defaultBranch"); then
        echo "✅ リポジトリ情報取得成功"
        echo "$repo_info"
        log_github_operation "get_repo_info" "success" "repository info retrieved"
        return 0
    else
        echo "エラー: リポジトリ情報の取得に失敗しました" >&2
        log_github_operation "get_repo_info" "failed" "repository info retrieval failed"
        return 1
    fi
}

# 🚀 バッチ処理機能: 複数イシューに対する一括操作
batch_github_operations() {
    local operation="$1"
    local -a issue_numbers=("${@:2}")
    
    if [[ ${#issue_numbers[@]} -eq 0 ]]; then
        echo "エラー: 処理するイシュー番号が指定されていません" >&2
        return 1
    fi
    
    echo "🔄 GitHub バッチ操作開始: $operation (${#issue_numbers[@]} イシュー)"
    
    # 認証とレート制限を1回だけチェック（重複チェックを排除）
    if ! check_github_auth; then
        return 1
    fi
    
    if ! check_rate_limit; then
        return 1
    fi
    
    case "$operation" in
        "add_comments")
            batch_add_comments "${issue_numbers[@]}"
            ;;
        "get_info")
            batch_get_issue_info "${issue_numbers[@]}"
            ;;
        "update_labels")
            batch_update_labels "${issue_numbers[@]}"
            ;;
        *)
            echo "エラー: 未対応のバッチ操作: $operation" >&2
            return 1
            ;;
    esac
}

# 複数イシューに並列でコメント追加
batch_add_comments() {
    local -a issue_numbers=("$@")
    local comment_body="${BATCH_COMMENT_BODY:-}"
    
    if [[ -z "$comment_body" ]]; then
        echo "エラー: BATCH_COMMENT_BODY 変数が設定されていません" >&2
        return 1
    fi
    
    echo "💬 ${#issue_numbers[@]} イシューにコメントを並列追加中..."
    
    local success_count=0
    local failure_count=0
    local pids=()
    
    # 並列実行用の一時ディレクトリ
    local temp_dir=$(mktemp -d -t batch_comments_XXXXXX)
    
    # 各イシューに対して並列処理を開始
    for issue_num in "${issue_numbers[@]}"; do
        {
            local result_file="$temp_dir/issue_${issue_num}.result"
            if safe_gh_command "issue" "comment" "$issue_num" --body "$comment_body" 2>"$temp_dir/issue_${issue_num}.error"; then
                echo "success" > "$result_file"
                log_github_operation "batch_comment" "success" "Issue #$issue_num"
            else
                echo "failure" > "$result_file"
                log_github_operation "batch_comment" "failed" "Issue #$issue_num - $(cat "$temp_dir/issue_${issue_num}.error" 2>/dev/null || echo 'unknown error')"
            fi
        } &
        pids+=($!)
    done
    
    # 全ての並列処理完了を待機
    for pid in "${pids[@]}"; do
        wait "$pid"
    done
    
    # 結果集計
    for issue_num in "${issue_numbers[@]}"; do
        local result_file="$temp_dir/issue_${issue_num}.result"
        if [[ -f "$result_file" ]]; then
            local result=$(cat "$result_file")
            if [[ "$result" == "success" ]]; then
                ((success_count++))
                echo "  ✅ Issue #$issue_num: コメント追加成功"
            else
                ((failure_count++))
                echo "  ❌ Issue #$issue_num: コメント追加失敗"
                if [[ -f "$temp_dir/issue_${issue_num}.error" ]]; then
                    echo "     エラー: $(cat "$temp_dir/issue_${issue_num}.error")"
                fi
            fi
        else
            ((failure_count++))
            echo "  ❓ Issue #$issue_num: 結果不明"
        fi
    done
    
    # 一時ディレクトリ削除
    rm -rf "$temp_dir"
    
    echo "📊 バッチコメント追加完了: 成功 $success_count, 失敗 $failure_count"
    log_github_operation "batch_add_comments" "completed" "$success_count/$((success_count + failure_count)) successful"
    
    return $([[ $failure_count -eq 0 ]] && echo 0 || echo 1)
}

# 複数イシューの情報を一括取得（GraphQL利用）
batch_get_issue_info() {
    local -a issue_numbers=("$@")
    
    echo "📊 ${#issue_numbers[@]} イシューの情報を一括取得中..."
    
    # GraphQL クエリを構築（動的にイシュー番号を組み込み）
    local issues_array=""
    for issue_num in "${issue_numbers[@]}"; do
        issues_array+="$issue_num,"
    done
    issues_array="${issues_array%,}"  # 末尾のカンマを削除
    
    # GitHub GraphQL APIを使用して一括取得
    local query='
    query($owner: String!, $name: String!, $issueNumbers: [Int!]!) {
        repository(owner: $owner, name: $name) {
            issues: nodes {
                ... on Issue {
                    number
                    title
                    state
                    updatedAt
                    comments {
                        totalCount
                    }
                    labels(first: 10) {
                        nodes {
                            name
                        }
                    }
                    assignees(first: 5) {
                        totalCount
                    }
                }
            }
        }
    }'
    
    # リポジトリ情報を取得
    local repo_info
    if repo_info=$(gh repo view --json owner,name 2>/dev/null); then
        local owner=$(echo "$repo_info" | jq -r '.owner.login')
        local name=$(echo "$repo_info" | jq -r '.name')
        
        # 一時ファイルに結果を保存
        local result_file=$(mktemp -t batch_issues_XXXXXX.json)
        
        if gh api graphql \
            -f query="$query" \
            -F owner="$owner" \
            -F name="$name" \
            -F issueNumbers="[$issues_array]" > "$result_file" 2>/dev/null; then
            
            echo "✅ GraphQL による一括取得成功"
            log_github_operation "batch_get_info" "success" "${#issue_numbers[@]} issues via GraphQL"
            
            # 結果をパース
            local issues_data=$(jq -c '.data.repository.issues[]' "$result_file")
            while IFS= read -r issue_data; do
                local issue_number=$(echo "$issue_data" | jq -r '.number')
                local issue_title=$(echo "$issue_data" | jq -r '.title')
                local issue_state=$(echo "$issue_data" | jq -r '.state')
                
                echo "  📋 Issue #$issue_number: $issue_state - $issue_title"
            done <<< "$issues_data"
            
            echo "$result_file"  # 結果ファイルのパスを返す
        else
            echo "⚠️ GraphQL一括取得に失敗、個別取得にフォールバック"
            log_github_operation "batch_get_info" "fallback" "GraphQL failed, using individual calls"
            
            # フォールバック: 個別取得
            for issue_num in "${issue_numbers[@]}"; do
                if safe_get_issue_info "$issue_num" "plain" >/dev/null; then
                    echo "  ✅ Issue #$issue_num: 個別取得成功"
                else
                    echo "  ❌ Issue #$issue_num: 個別取得失敗"
                fi
            done
        fi
        
        rm -f "$result_file"
    else
        echo "エラー: リポジトリ情報の取得に失敗しました" >&2
        return 1
    fi
}

# 環境変数でバッチコメント内容を設定する関数
set_batch_comment() {
    local comment="$1"
    export BATCH_COMMENT_BODY="$comment"
}

# バッチ操作の使用例を表示
show_batch_examples() {
    echo "📚 GitHub バッチ操作の使用例:"
    echo ""
    echo "# 1. 複数イシューに同じコメントを追加"
    echo 'set_batch_comment "機能実装が完了しました"'
    echo "batch_github_operations add_comments 1 2 3"
    echo ""
    echo "# 2. 複数イシューの情報を一括取得"
    echo "batch_github_operations get_info 1 2 3"
    echo ""
    echo "# 3. 従来の個別処理との比較"
    echo "# 従来: 3イシューで約15秒（5秒×3）"
    echo "# 並列: 3イシューで約3秒（並列実行）"
    echo "# GraphQL: 複数イシューで約1秒（一括取得）"
}