#!/bin/bash
# Template Utilities for TDD/DDD/Layered Architecture Commands
# テンプレート処理用ユーティリティ関数

# テンプレート変数置換関数
substitute_template_vars() {
    local template_file="$1"
    local output_content="$2"
    
    # 各変数を置換
    output_content=$(echo "$output_content" | sed "s/{{IMPLEMENTATION_DATE}}/$implementation_date/g")
    output_content=$(echo "$output_content" | sed "s/{{ENTITY_NAME}}/$entity_name/g")
    output_content=$(echo "$output_content" | sed "s/{{ENTITY_LOWER}}/$entity_lower/g")
    output_content=$(echo "$output_content" | sed "s/{{TABLE_NAME}}/$table_name/g")
    output_content=$(echo "$output_content" | sed "s/{{FEATURE_NAME}}/$feature_name/g")
    output_content=$(echo "$output_content" | sed "s/{{FEATURE_NAME_SNAKE}}/$feature_name_snake/g")
    output_content=$(echo "$output_content" | sed "s/{{FEATURE_NAME_TITLE}}/$feature_name_title/g")
    output_content=$(echo "$output_content" | sed "s/{{API_ENDPOINT}}/$api_endpoint/g")
    
    # 複雑な置換処理
    if [[ -n "$entity_imports" ]]; then
        output_content=$(echo "$output_content" | sed "s|{{ENTITY_IMPORTS}}|$entity_imports|g")
    fi
    if [[ -n "$repository_imports" ]]; then
        output_content=$(echo "$output_content" | sed "s|{{REPOSITORY_IMPORTS}}|$repository_imports|g")
    fi
    if [[ -n "$repository_constructor_params" ]]; then
        output_content=$(echo "$output_content" | sed "s|{{REPOSITORY_CONSTRUCTOR_PARAMS}}|$repository_constructor_params|g")
    fi
    if [[ -n "$repository_constructor_docs" ]]; then
        output_content=$(echo "$output_content" | sed "s|{{REPOSITORY_CONSTRUCTOR_DOCS}}|$repository_constructor_docs|g")
    fi
    if [[ -n "$repository_assignments" ]]; then
        output_content=$(echo "$output_content" | sed "s|{{REPOSITORY_ASSIGNMENTS}}|$repository_assignments|g")
    fi
    
    echo "$output_content"
}

# テンプレートファイル読み込み
load_template() {
    local template_path="$1"
    local template_dir="$(dirname "${BASH_SOURCE[0]}")/templates"
    local full_path="$template_dir/$template_path"
    
    if [[ ! -f "$full_path" ]]; then
        echo "エラー: テンプレートファイルが見つかりません: $full_path"
        return 1
    fi
    
    cat "$full_path"
}

# 名前変換ユーティリティ
to_snake_case() {
    local input="$1"
    echo "$input" | sed 's/-/_/g' | tr '[:upper:]' '[:lower:]'
}

to_title_case() {
    local input="$1"
    # ハイフンとアンダースコアを削除してタイトルケースに
    echo "$input" | sed 's/[-_]\([a-z]\)/\U\1/g' | sed 's/^./\U&/'
}

to_lower_case() {
    local input="$1"
    echo "$input" | tr '[:upper:]' '[:lower:]'
}

# エンティティベースの変数設定
setup_entity_vars() {
    local entity="$1"
    
    entity_name="$entity"
    entity_lower=$(to_lower_case "$entity")
    table_name="${entity_lower}s"
    implementation_date=$(date)
}

# フィーチャーベースの変数設定
setup_feature_vars() {
    local feature="$1"
    
    feature_name="$feature"
    feature_name_snake=$(to_snake_case "$feature")
    feature_name_title=$(to_title_case "$feature")
    api_endpoint=$(echo "$feature" | sed 's/-/\//g')
    implementation_date=$(date)
}

# マルチエンティティサポート用
generate_entity_imports() {
    local entities=("$@")
    local imports=""
    
    for entity in "${entities[@]}"; do
        entity_lower=$(to_lower_case "$entity")
        imports+="from src.domain.entities.${entity_lower} import ${entity}\\n"
    done
    
    echo -e "$imports"
}

generate_repository_imports() {
    local entities=("$@")
    local imports=""
    
    for entity in "${entities[@]}"; do
        entity_lower=$(to_lower_case "$entity")
        imports+="from src.domain.repositories.${entity_lower}_repository import ${entity}Repository\\n"
    done
    
    echo -e "$imports"
}

generate_repository_constructor() {
    local entities=("$@")
    local params=""
    local docs=""
    local assignments=""
    
    for entity in "${entities[@]}"; do
        entity_lower=$(to_lower_case "$entity")
        params+=", ${entity_lower}_repository: ${entity}Repository"
        docs+="            ${entity_lower}_repository: ${entity}Repository インスタンス\\n"
        assignments+="        self._${entity_lower}_repository = ${entity_lower}_repository\\n"
    done
    
    repository_constructor_params="$params"
    repository_constructor_docs=$(echo -e "$docs")
    repository_assignments=$(echo -e "$assignments")
}

# テンプレート処理のメイン関数
process_template() {
    local template_path="$1"
    local output_file="$2"
    
    # テンプレート読み込み
    local template_content
    template_content=$(load_template "$template_path")
    if [[ $? -ne 0 ]]; then
        return 1
    fi
    
    # 変数置換
    local processed_content
    processed_content=$(substitute_template_vars "$template_path" "$template_content")
    
    # 出力
    if ! safe_create_file "$output_file" "$processed_content" true; then
        echo "エラー: 処理済みテンプレートファイルの作成に失敗しました: $output_file"
        return 1
    fi
    
    return 0
}