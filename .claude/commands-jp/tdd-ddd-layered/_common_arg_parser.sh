#!/bin/bash

# =============================================================================
# 共通引数解析関数
# =============================================================================
# 
# このスクリプトは、カスタムコマンドで複数の引数を処理するための共通ライブラリです。
#
# 主な機能:
# 1. カンマ区切り引数の解析（例: "1,7,feature-name,option"）
# 2. 数値と文字列の自動分類
#    - 数値 → issue_numbers配列（GitHubイシュー番号として使用）
#    - 文字列 → other_args配列（機能名、オプションとして使用）
# 3. 引数数の検証
# 4. 使用例の表示
#
# 使用方法:
#   source "$(dirname "${BASH_SOURCE[0]}")/_common_arg_parser.sh"
#   parse_arguments "$ARGUMENTS"
#   validate_arguments <min_issues> <max_issues> <required_other_count>
# 
# =============================================================================

# カンマ区切りの引数を解析し、数値はissue_numbers配列に、文字列はother_args配列に分類
parse_arguments() {
    local input="$1"
    
    # グローバル配列を初期化
    issue_numbers=()
    other_args=()
    
    if [[ -z "$input" ]]; then
        return 1
    fi
    
    # カンマで分割してループ処理
    local remaining="$input"
    while [[ -n "$remaining" ]]; do
        # 最初のカンマまでを取得
        if [[ "$remaining" == *","* ]]; then
            arg="${remaining%%,*}"
            remaining="${remaining#*,}"
        else
            arg="$remaining"
            remaining=""
        fi
        
        # 前後の空白を削除
        arg=$(echo "$arg" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//')
        
        if [[ "$arg" =~ ^[0-9]+$ ]]; then
            # 数値の場合はissue_numbersに追加
            issue_numbers=("${issue_numbers[@]}" "$arg")
        elif [[ -n "$arg" ]]; then
            # 非空文字列の場合はother_argsに追加  
            other_args=("${other_args[@]}" "$arg")
        fi
    done
    
    return 0
}

# 引数検証関数
validate_arguments() {
    local min_issues="$1"
    local max_issues="$2"
    local required_other_count="$3"
    
    local issue_count=${#issue_numbers[@]}
    local other_count=${#other_args[@]}
    
    # イシュー番号数のチェック
    if [[ -n "$min_issues" ]] && [[ $issue_count -lt $min_issues ]]; then
        echo "エラー: 最低${min_issues}個のイシュー番号が必要です（現在: ${issue_count}個）"
        return 1
    fi
    
    if [[ -n "$max_issues" ]] && [[ $issue_count -gt $max_issues ]]; then
        echo "エラー: イシュー番号は最大${max_issues}個までです（現在: ${issue_count}個）"
        return 1
    fi
    
    # その他引数数のチェック
    if [[ -n "$required_other_count" ]] && [[ $other_count -ne $required_other_count ]]; then
        echo "エラー: ${required_other_count}個の追加引数が必要です（現在: ${other_count}個）"
        return 1
    fi
    
    return 0
}

# 引数情報表示関数（デバッグ用）
show_parsed_arguments() {
    echo "=== 解析された引数 ==="
    echo "イシュー番号: ${issue_numbers[*]}"
    echo "その他の引数: ${other_args[*]}"
    echo "===================="
}

# 使用例表示関数
show_usage_example() {
    local command_name="$1"
    local example_args="$2"
    local description="$3"
    
    echo "使用法: /$command_name $example_args"
    echo "説明: $description"
    echo ""
    echo "引数解析の仕組み:"
    echo "  - 数値（例: 1, 7, 15）→ issue_numbers配列に格納"
    echo "  - 文字列（例: feature-name）→ other_args配列に格納"
    echo "  - 区切り: カンマ(,)で複数指定可能"
    echo "  - 空白は自動的に除去される"
    echo ""
    echo "解析例:"
    echo "  /$command_name 1                    # issue_numbers=[1], other_args=[]"
    echo "  /$command_name 1,feature            # issue_numbers=[1], other_args=[feature]"
    echo "  /$command_name 1,7,15               # issue_numbers=[1,7,15], other_args=[]"
    echo "  /$command_name 1,7,feature,option   # issue_numbers=[1,7], other_args=[feature,option]"
    echo "  /$command_name feature,1,option,7   # issue_numbers=[1,7], other_args=[feature,option]"
    echo ""
    echo "注意: 引数の順序は自動的に整理されます（数値と文字列が分離される）"
}