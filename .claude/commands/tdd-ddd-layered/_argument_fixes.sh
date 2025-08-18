#!/bin/bash

# 引数検証の修正パッチ
# 各コマンドで正しい引数検証を適用するための情報

# コマンドごとの正しい引数検証パラメータ
declare -A CORRECT_VALIDATIONS=(
    # Initial Phase Commands
    ["00-create-vision"]=""                           # 引数なし
    ["01-init-project-structure"]=""                  # 引数なし  
    ["02-sprint-planning"]="0 0 1"                    # イシューなし、スプリント番号1つ
    
    # Sprint Execution Commands  
    ["03-create-use-case"]="1 \"\" 0"                 # 最低1イシュー、上限なし、その他0
    ["04-domain-modeling"]="1 \"\" 0"                 # 最低1イシュー、上限なし、その他0
    ["05-create-tests"]="1 \"\" 0"                    # 最低1イシュー、上限なし、その他0
    ["06-implement-domain"]="1 \"\" 0"                # 最低1イシュー、上限なし、その他0
    ["07-implement-usecase"]="1 \"\" 0"               # 最低1イシュー、上限なし、その他0
    ["08-implement-infra"]="1 \"\" 0"                 # 最低1イシュー、上限なし、その他0
    ["09-implement-presentation"]="1 \"\" 0"          # 最低1イシュー、上限なし、その他0
    ["10-run-all-tests"]="1 \"\" 0"                   # 最低1イシュー、上限なし、その他0
    ["11-refactor"]="1 \"\" 0"                        # 最低1イシュー、上限なし、その他0
    
    # Scenario Evolution Commands
    ["12-evolve-scenarios"]="0 \"\" 1"                # イシューオプション、フィーチャー名1つ必須
    
    # Review Commands  
    ["13-review-issue"]="1 \"\" 0"                    # 最低1イシュー、上限なし、その他0
    ["14-apply-feedback"]="1 \"\" 0"                  # 最低1イシュー、上限なし、その他0
    ["15-create-pr"]="1 \"\" 0"                       # 最低1イシュー、上限なし、その他0
    
    # Status Command
    ["16-use-case-status"]="1 1 0"                    # イシュー1つだけ、その他0
)

# 各コマンドで使用する正しい使用例
declare -A USAGE_EXAMPLES=(
    ["02-sprint-planning"]='show_usage_example "sprint-planning" "1" "スプリント1の計画作成"
show_usage_example "sprint-planning" "2" "スプリント2の計画作成"'
    
    ["03-create-use-case"]='show_usage_example "create-use-case" "1" "単一イシューからユースケース仕様作成"
show_usage_example "create-use-case" "1,7" "複数イシューからユースケース仕様作成"  
show_usage_example "create-use-case" "1,mt5-data" "イシュー1 + 機能名'\''mt5-data'\''を指定"'
    
    ["12-evolve-scenarios"]='show_usage_example "evolve-scenarios" "feature-name" "新機能'\''feature-name'\''のシナリオ進化"
show_usage_example "evolve-scenarios" "1,feature-name" "イシュー1関連での'\''feature-name'\''シナリオ進化"
show_usage_example "evolve-scenarios" "1,7,mt5-extended-data" "複数イシュー(1,7)統合での'\''mt5-extended-data'\''シナリオ進化"'
    
    ["16-use-case-status"]='show_usage_example "use-case-status" "1" "イシュー1の進捗状況確認"
show_usage_example "use-case-status" "7" "イシュー7の進捗状況確認"'
)

# 引数検証の修正を適用する関数
fix_argument_validation() {
    local command_file="$1"
    local command_name=$(basename "$command_file" .md)
    
    echo "修正対象: $command_name"
    
    # 各コマンドごとの修正ロジック
    case "$command_name" in
        "02-sprint-planning")
            echo "02-sprint-planning: スプリント番号（文字列）の処理修正が必要"
            echo "現在の問題: issue_numbers[0]でスプリント番号を取得している"
            echo "修正案: other_args[0]でスプリント番号を取得し、数値検証を追加"
            ;;
        "12-evolve-scenarios")
            echo "12-evolve-scenarios: 引数検証は正しい"
            ;;
        "16-use-case-status")
            echo "16-use-case-status: イシュー1つのみの検証修正が必要"
            echo "現在の設定確認が必要"
            ;;
        *)
            local validation="${CORRECT_VALIDATIONS[$command_name]:-}"
            if [[ -n "$validation" ]]; then
                echo "$command_name: validate_arguments $validation"
            else
                echo "$command_name: 引数検証不要または未定義"
            fi
            ;;
    esac
}

# 修正が必要なコマンドファイルを特定
identify_problematic_commands() {
    echo "引数検証の問題があるコマンド:"
    echo "1. 02-sprint-planning.md - スプリント番号の取得方法"
    echo "2. 16-use-case-status.md - 引数検証パラメータ確認要"
    echo ""
    echo "その他のコマンドは基本的に正しい引数検証を使用している"
}

# スプリント番号用の特別な検証関数
validate_sprint_number() {
    local sprint_number="$1"
    
    if [[ -z "$sprint_number" ]]; then
        echo "エラー: スプリント番号が指定されていません"
        return 1
    fi
    
    if ! [[ "$sprint_number" =~ ^[0-9]+$ ]]; then
        echo "エラー: スプリント番号は数値である必要があります: $sprint_number"
        return 1
    fi
    
    if [[ "$sprint_number" -eq 0 ]]; then
        echo "エラー: スプリント番号は1以上である必要があります"
        return 1
    fi
    
    return 0
}