#!/bin/bash

# 解決手順自動提案エンジン
# 現在の状況を分析して、具体的な次のアクションを自動提案

set -euo pipefail

# 提案の信頼度レベル
declare -g -A CONFIDENCE_LEVELS=(
    ["HIGH"]="🎯 確実"
    ["MEDIUM"]="💡 推奨" 
    ["LOW"]="🤔 提案"
)

# 状況パターンと提案のマッピング
declare -g -A SITUATION_PATTERNS=(
    # メタデータ関連
    ["metadata_missing"]="create_use_case_first"
    ["metadata_corrupted"]="restore_metadata"
    
    # Git関連
    ["git_uncommitted"]="commit_changes"
    ["git_conflict"]="resolve_conflict"
    ["git_branch_missing"]="create_branch"
    
    # GitHub関連
    ["github_auth_failed"]="setup_github_auth"
    ["github_rate_limit"]="wait_rate_limit"
    ["github_issue_closed"]="reopen_or_new_issue"
    
    # 依存関係
    ["missing_dependencies"]="install_dependencies"
    ["python_env_invalid"]="setup_python_env"
    
    # ワークフロー
    ["wrong_phase"]="correct_phase_sequence"
    ["prerequisite_missing"]="complete_prerequisite"
    ["test_failing"]="fix_failing_tests"
)

# 🧠 メイン提案エンジン
suggest_next_actions() {
    local issue_numbers=("$@")
    
    if [[ ${#issue_numbers[@]} -eq 0 ]]; then
        echo "エラー: イシュー番号が指定されていません" >&2
        return 1
    fi
    
    echo "🔍 状況分析と提案生成中..."
    
    # 一時的な分析結果ディレクトリ
    local analysis_workspace=$(mktemp -d -t analysis_XXXXXX)
    local analysis_report="$analysis_workspace/analysis.json"
    
    # 現在の状況を総合分析
    analyze_current_situation "$analysis_report" "${issue_numbers[@]}"
    
    # 提案を生成
    generate_suggestions "$analysis_report"
    
    # 実行可能なコマンド提案
    suggest_executable_commands "$analysis_report"
    
    # 詳細分析結果の表示
    show_detailed_analysis "$analysis_report"
    
    # クリーンアップ
    rm -rf "$analysis_workspace"
}

# 状況分析関数
analyze_current_situation() {
    local analysis_report="$1"
    shift
    local issue_numbers=("$@")
    
    # 初期分析結果
    cat > "$analysis_report" << EOF
{
  "analysis_timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "issue_numbers": [$(IFS=','; echo "\"${issue_numbers[*]//,/\",\"}")"],
  "detected_problems": [],
  "environment_status": {},
  "metadata_status": {},
  "git_status": {},
  "github_status": {},
  "suggestions": [],
  "confidence_scores": {}
}
EOF
    
    echo "  📊 環境状態を分析中..."
    analyze_environment "$analysis_report"
    
    echo "  📋 メタデータ状態を分析中..."
    analyze_metadata_status "$analysis_report" "${issue_numbers[@]}"
    
    echo "  🌿 Git状態を分析中..."
    analyze_git_status "$analysis_report"
    
    echo "  🔗 GitHub状態を分析中..."
    analyze_github_status "$analysis_report" "${issue_numbers[@]}"
    
    echo "  🎯 問題を特定中..."
    identify_problems "$analysis_report"
}

# 環境状態分析
analyze_environment() {
    local analysis_report="$1"
    
    local env_status="{}"
    local problems=()
    
    # Python/uv環境チェック
    if command -v uv >/dev/null 2>&1; then
        env_status=$(echo "$env_status" | jq '.uv_available = true')
    else
        env_status=$(echo "$env_status" | jq '.uv_available = false')
        problems+=("missing_uv")
    fi
    
    # GitHub CLI チェック
    if command -v gh >/dev/null 2>&1; then
        env_status=$(echo "$env_status" | jq '.gh_available = true')
        
        # 認証状態チェック
        if gh auth status >/dev/null 2>&1; then
            env_status=$(echo "$env_status" | jq '.gh_authenticated = true')
        else
            env_status=$(echo "$env_status" | jq '.gh_authenticated = false')
            problems+=("github_not_authenticated")
        fi
    else
        env_status=$(echo "$env_status" | jq '.gh_available = false')
        problems+=("missing_gh")
    fi
    
    # jq チェック
    if command -v jq >/dev/null 2>&1; then
        env_status=$(echo "$env_status" | jq '.jq_available = true')
    else
        env_status=$(echo "$env_status" | jq '.jq_available = false')
        problems+=("missing_jq")
    fi
    
    # プロジェクトファイル存在確認
    if [[ -f "pyproject.toml" ]] || [[ -f "requirements.txt" ]]; then
        env_status=$(echo "$env_status" | jq '.python_project = true')
    else
        env_status=$(echo "$env_status" | jq '.python_project = false')
        problems+=("not_python_project")
    fi
    
    # 結果をレポートに記録
    jq --argjson env "$env_status" \
       --argjson problems "$(printf '%s\n' "${problems[@]}" | jq -R . | jq -s .)" \
       '.environment_status = $env | .detected_problems += $problems' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# メタデータ状態分析
analyze_metadata_status() {
    local analysis_report="$1"
    shift
    local issue_numbers=("$@")
    
    local metadata_status="{}"
    local problems=()
    
    # 各イシューのメタデータをチェック
    for issue_num in "${issue_numbers[@]}"; do
        echo "    🔍 Issue #$issue_num のメタデータ確認中..."
        
        # メタデータファイル検索
        local found_files=()
        mapfile -t found_files < <(find docs/use_cases -name "*issue-*${issue_num}*" -name "*.json" 2>/dev/null)
        
        if [[ ${#found_files[@]} -eq 0 ]]; then
            metadata_status=$(echo "$metadata_status" | jq --arg issue "$issue_num" '.[$issue] = {"exists": false, "valid": false}')
            problems+=("metadata_missing_$issue_num")
        elif [[ ${#found_files[@]} -eq 1 ]]; then
            local metadata_file="${found_files[0]}"
            
            if jq empty "$metadata_file" 2>/dev/null; then
                # 現在のフェーズを確認
                local current_phase=$(jq -r '.phase // "unknown"' "$metadata_file")
                
                metadata_status=$(echo "$metadata_status" | jq \
                    --arg issue "$issue_num" \
                    --arg phase "$current_phase" \
                    --arg file "$metadata_file" \
                    '.[$issue] = {"exists": true, "valid": true, "current_phase": $phase, "file": $file}')
                
                # フェーズに基づいて必要なアクションを判定
                case "$current_phase" in
                    "created"|"use_case_created")
                        problems+=("needs_domain_modeling_$issue_num")
                        ;;
                    "domain_modeled")
                        problems+=("needs_test_creation_$issue_num")
                        ;;
                    "tests_created"|"tests_created_red")
                        problems+=("needs_domain_implementation_$issue_num")
                        ;;
                    "domain_implemented")
                        problems+=("needs_usecase_implementation_$issue_num")
                        ;;
                    # 他のフェーズも同様に追加可能
                esac
            else
                metadata_status=$(echo "$metadata_status" | jq --arg issue "$issue_num" '.[$issue] = {"exists": true, "valid": false}')
                problems+=("metadata_corrupted_$issue_num")
            fi
        else
            metadata_status=$(echo "$metadata_status" | jq --arg issue "$issue_num" '.[$issue] = {"exists": true, "valid": false, "multiple": true}')
            problems+=("metadata_multiple_$issue_num")
        fi
    done
    
    # 結果を記録
    jq --argjson metadata "$metadata_status" \
       --argjson problems "$(printf '%s\n' "${problems[@]}" | jq -R . | jq -s .)" \
       '.metadata_status = $metadata | .detected_problems += $problems' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# Git状態分析
analyze_git_status() {
    local analysis_report="$1"
    
    local git_status="{}"
    local problems=()
    
    if git rev-parse --git-dir >/dev/null 2>&1; then
        git_status=$(echo "$git_status" | jq '.is_git_repo = true')
        
        # 現在のブランチ
        local current_branch=$(git branch --show-current)
        git_status=$(echo "$git_status" | jq --arg branch "$current_branch" '.current_branch = $branch')
        
        # 変更状態確認
        if ! git diff --quiet; then
            git_status=$(echo "$git_status" | jq '.has_uncommitted_changes = true')
            problems+=("git_uncommitted_changes")
        else
            git_status=$(echo "$git_status" | jq '.has_uncommitted_changes = false')
        fi
        
        # ステージング状態
        if ! git diff --cached --quiet; then
            git_status=$(echo "$git_status" | jq '.has_staged_changes = true')
        else
            git_status=$(echo "$git_status" | jq '.has_staged_changes = false')
        fi
        
        # リモート同期状態
        if git remote >/dev/null 2>&1; then
            local behind=$(git rev-list --count HEAD..@{u} 2>/dev/null || echo "0")
            local ahead=$(git rev-list --count @{u}..HEAD 2>/dev/null || echo "0")
            
            git_status=$(echo "$git_status" | jq --argjson behind "$behind" --argjson ahead "$ahead" '.behind = $behind | .ahead = $ahead')
            
            if [[ $behind -gt 0 ]]; then
                problems+=("git_behind_remote")
            fi
        fi
        
    else
        git_status=$(echo "$git_status" | jq '.is_git_repo = false')
        problems+=("not_git_repository")
    fi
    
    # 結果を記録
    jq --argjson git "$git_status" \
       --argjson problems "$(printf '%s\n' "${problems[@]}" | jq -R . | jq -s .)" \
       '.git_status = $git | .detected_problems += $problems' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# GitHub状態分析
analyze_github_status() {
    local analysis_report="$1"
    shift
    local issue_numbers=("$@")
    
    local github_status="{}"
    local problems=()
    
    if command -v gh >/dev/null 2>&1 && gh auth status >/dev/null 2>&1; then
        github_status=$(echo "$github_status" | jq '.authenticated = true')
        
        # レート制限チェック
        if rate_info=$(gh api rate_limit 2>/dev/null); then
            local remaining=$(echo "$rate_info" | jq -r '.rate.remaining')
            github_status=$(echo "$github_status" | jq --argjson remaining "$remaining" '.rate_limit_remaining = $remaining')
            
            if [[ $remaining -lt 10 ]]; then
                problems+=("github_rate_limit_low")
            fi
        fi
        
        # 各イシューの状態確認
        for issue_num in "${issue_numbers[@]}"; do
            if issue_info=$(gh issue view "$issue_num" --json state,title 2>/dev/null); then
                local issue_state=$(echo "$issue_info" | jq -r '.state')
                local issue_title=$(echo "$issue_info" | jq -r '.title')
                
                github_status=$(echo "$github_status" | jq \
                    --arg issue "$issue_num" \
                    --arg state "$issue_state" \
                    --arg title "$issue_title" \
                    '.issues[$issue] = {"state": $state, "title": $title}')
                
                if [[ "$issue_state" == "closed" ]]; then
                    problems+=("github_issue_closed_$issue_num")
                fi
            else
                problems+=("github_issue_not_found_$issue_num")
            fi
        done
        
    else
        github_status=$(echo "$github_status" | jq '.authenticated = false')
        problems+=("github_not_authenticated")
    fi
    
    # 結果を記録
    jq --argjson github "$github_status" \
       --argjson problems "$(printf '%s\n' "${problems[@]}" | jq -R . | jq -s .)" \
       '.github_status = $github | .detected_problems += $problems' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# 問題特定
identify_problems() {
    local analysis_report="$1"
    
    # 問題を重要度順にソート
    jq '.detected_problems |= sort | .detected_problems |= unique' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# 提案生成
generate_suggestions() {
    local analysis_report="$1"
    
    echo "  💡 解決策を生成中..."
    
    local suggestions=()
    local confidence_scores="{}"
    
    # 問題に基づいて提案を生成
    local problems
    problems=$(jq -r '.detected_problems[]' "$analysis_report")
    
    while IFS= read -r problem; do
        if [[ -n "$problem" ]]; then
            local suggestion
            local confidence
            
            case "$problem" in
                "github_not_authenticated")
                    suggestion='{"action": "gh auth login", "description": "GitHub認証を設定してください", "category": "environment", "priority": 1}'
                    confidence="HIGH"
                    ;;
                "metadata_missing_"*)
                    local issue_num=$(echo "$problem" | sed 's/metadata_missing_//')
                    suggestion="{\"action\": \"/create-use-case $issue_num <feature-name>\", \"description\": \"Issue #$issue_num のユースケース仕様を作成してください\", \"category\": \"workflow\", \"priority\": 2}"
                    confidence="HIGH"
                    ;;
                "needs_domain_modeling_"*)
                    local issue_num=$(echo "$problem" | sed 's/needs_domain_modeling_//')
                    suggestion="{\"action\": \"/domain-modeling $issue_num\", \"description\": \"Issue #$issue_num のドメインモデル設計を実行してください\", \"category\": \"workflow\", \"priority\": 2}"
                    confidence="HIGH"
                    ;;
                "needs_test_creation_"*)
                    local issue_num=$(echo "$problem" | sed 's/needs_test_creation_//')
                    suggestion="{\"action\": \"/create-tests $issue_num\", \"description\": \"Issue #$issue_num のTDDテスト作成を実行してください\", \"category\": \"workflow\", \"priority\": 2}"
                    confidence="HIGH"
                    ;;
                "git_uncommitted_changes")
                    suggestion='{"action": "git add . && git commit -m \"WIP: Save current changes\"", "description": "未コミットの変更をコミットしてください", "category": "git", "priority": 3}'
                    confidence="MEDIUM"
                    ;;
                "missing_uv")
                    suggestion='{"action": "curl -LsSf https://astral.sh/uv/install.sh | sh", "description": "uvパッケージマネージャーをインストールしてください", "category": "environment", "priority": 1}'
                    confidence="HIGH"
                    ;;
                *)
                    suggestion="{\"action\": \"echo 'Unknown problem: $problem'\", \"description\": \"未知の問題が発生しました: $problem\", \"category\": \"unknown\", \"priority\": 5}"
                    confidence="LOW"
                    ;;
            esac
            
            suggestions+=("$suggestion")
            confidence_scores=$(echo "$confidence_scores" | jq --arg problem "$problem" --arg confidence "$confidence" '.[$problem] = $confidence')
        fi
    done <<< "$problems"
    
    # 提案を優先度順にソート
    local sorted_suggestions
    sorted_suggestions=$(printf '%s\n' "${suggestions[@]}" | jq -s 'sort_by(.priority)')
    
    # 結果を記録
    jq --argjson suggestions "$sorted_suggestions" \
       --argjson confidence "$confidence_scores" \
       '.suggestions = $suggestions | .confidence_scores = $confidence' \
       "$analysis_report" > "${analysis_report}.tmp" && mv "${analysis_report}.tmp" "$analysis_report"
}

# 実行可能コマンド提案
suggest_executable_commands() {
    local analysis_report="$1"
    
    echo ""
    echo "🎯 **推奨アクション (実行準備完了)**"
    echo "================================="
    
    local suggestions
    suggestions=$(jq -r '.suggestions[] | "\(.priority)|\(.category)|\(.action)|\(.description)"' "$analysis_report")
    
    local counter=1
    while IFS='|' read -r priority category action description; do
        if [[ -n "$action" ]]; then
            local confidence_icon=""
            case "$priority" in
                1) confidence_icon="🚨 緊急" ;;
                2) confidence_icon="⚡ 重要" ;;
                3) confidence_icon="💡 推奨" ;;
                *) confidence_icon="🤔 任意" ;;
            esac
            
            echo ""
            echo "$confidence_icon **アクション $counter**"
            echo "📋 説明: $description"
            echo "🔧 実行コマンド:"
            echo "   $action"
            echo ""
            
            ((counter++))
        fi
    done <<< "$suggestions"
    
    if [[ $counter -eq 1 ]]; then
        echo "✅ **素晴らしい！** 現在特に問題は検出されませんでした。"
        echo ""
        echo "💡 **次のステップ:**"
        echo "   /use-case-status $(jq -r '.issue_numbers | join(",")' "$analysis_report")"
    fi
}

# 詳細分析結果表示
show_detailed_analysis() {
    local analysis_report="$1"
    
    echo ""
    echo "📊 **詳細分析結果**"
    echo "=================="
    echo ""
    
    # 環境状態
    echo "🔧 **環境状態:**"
    local uv_available=$(jq -r '.environment_status.uv_available' "$analysis_report")
    local gh_available=$(jq -r '.environment_status.gh_available' "$analysis_report")
    local gh_authenticated=$(jq -r '.environment_status.gh_authenticated // false' "$analysis_report")
    
    echo "   • uv: $(if [[ "$uv_available" == "true" ]]; then echo "✅ 利用可能"; else echo "❌ 未インストール"; fi)"
    echo "   • GitHub CLI: $(if [[ "$gh_available" == "true" ]]; then echo "✅ 利用可能"; else echo "❌ 未インストール"; fi)"
    echo "   • GitHub認証: $(if [[ "$gh_authenticated" == "true" ]]; then echo "✅ 認証済み"; else echo "❌ 未認証"; fi)"
    
    echo ""
    
    # メタデータ状態
    echo "📋 **メタデータ状態:**"
    local metadata_issues=$(jq -r '.metadata_status | keys[]' "$analysis_report")
    while IFS= read -r issue_num; do
        if [[ -n "$issue_num" ]]; then
            local exists=$(jq -r ".metadata_status.\"$issue_num\".exists" "$analysis_report")
            local valid=$(jq -r ".metadata_status.\"$issue_num\".valid" "$analysis_report")
            local phase=$(jq -r ".metadata_status.\"$issue_num\".current_phase // \"N/A\"" "$analysis_report")
            
            echo "   • Issue #$issue_num: $(if [[ "$exists" == "true" && "$valid" == "true" ]]; then echo "✅ 正常 (フェーズ: $phase)"; elif [[ "$exists" == "true" ]]; then echo "⚠️ 破損"; else echo "❌ 未作成"; fi)"
        fi
    done <<< "$metadata_issues"
    
    echo ""
    
    # Git状態
    echo "🌿 **Git状態:**"
    local is_git_repo=$(jq -r '.git_status.is_git_repo' "$analysis_report")
    if [[ "$is_git_repo" == "true" ]]; then
        local current_branch=$(jq -r '.git_status.current_branch' "$analysis_report")
        local has_changes=$(jq -r '.git_status.has_uncommitted_changes // false' "$analysis_report")
        
        echo "   • リポジトリ: ✅ Git リポジトリ"
        echo "   • 現在のブランチ: $current_branch"
        echo "   • 未コミット変更: $(if [[ "$has_changes" == "true" ]]; then echo "⚠️ あり"; else echo "✅ なし"; fi)"
    else
        echo "   • リポジトリ: ❌ Git リポジトリではありません"
    fi
    
    echo ""
    echo "⏰ **分析完了時刻:** $(jq -r '.analysis_timestamp' "$analysis_report")"
}

# 使用例表示
show_suggestion_examples() {
    echo "📚 **自動提案機能の使用例:**"
    echo ""
    echo "# 単一イシューの分析と提案"
    echo "suggest_next_actions 1"
    echo ""
    echo "# 複数イシューの分析と提案"  
    echo "suggest_next_actions 1 2 3"
    echo ""
    echo "# 環境変数でユーザータイプを設定して実行"
    echo "TDD_USER_TYPE=business suggest_next_actions 1"
    echo ""
    echo "📊 **提案される内容例:**"
    echo "• 🚨 緊急: GitHub認証設定 (gh auth login)"
    echo "• ⚡ 重要: 必要なユースケース仕様作成"  
    echo "• 💡 推奨: Git変更のコミット"
    echo "• 🤔 任意: パフォーマンス最適化"
}

echo "解決手順自動提案エンジンが読み込まれました"