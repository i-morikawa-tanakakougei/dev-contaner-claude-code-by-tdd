#!/bin/bash

# メタデータ更新の標準パターン
# 全コマンドで一貫したメタデータ更新方式を提供

# 標準的なメタデータ更新関数（原子性確保）
update_phase_metadata() {
    local metadata_file="$1"
    local phase_name="$2"
    local status="$3"
    local additional_fields="${4:-}"
    
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    local jq_expression=".phases.${phase_name}.created = $status | 
                         .updated_at = \"$timestamp\" |
                         .phase = \"${phase_name}_$([ "$status" = "true" ] && echo "created" || echo "pending")\""
    
    if [[ -n "$additional_fields" ]]; then
        jq_expression="$jq_expression | $additional_fields"
    fi
    
    update_metadata_atomic "$metadata_file" "$jq_expression"
}

# フェーズ完了時のメタデータ更新
complete_phase_metadata() {
    local metadata_file="$1"
    local phase_name="$2"
    local additional_fields="${3:-}"
    
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    local jq_expression=".phases.${phase_name}.completed = true |
                         .phases.${phase_name}.completed_at = \"$timestamp\" |
                         .updated_at = \"$timestamp\" |
                         .phase = \"${phase_name}_completed\""
    
    if [[ -n "$additional_fields" ]]; then
        jq_expression="$jq_expression | $additional_fields"
    fi
    
    update_metadata_atomic "$metadata_file" "$jq_expression"
}

# 承認状態の更新
approve_phase_metadata() {
    local metadata_file="$1"
    local phase_name="$2"
    local approved="$3"
    
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    update_metadata_atomic "$metadata_file" "
        .phases.${phase_name}.approved = $approved |
        .phases.${phase_name}.approved_at = \"$timestamp\" |
        .updated_at = \"$timestamp\"
    "
}

# ファイル参照の追加
add_spec_file_reference() {
    local metadata_file="$1"
    local file_type="$2"
    local file_path="$3"
    
    local timestamp=$(date -u +%Y-%m-%dT%H:%M:%SZ)
    
    update_metadata_atomic "$metadata_file" "
        .spec_files.${file_type} = \"$file_path\" |
        .updated_at = \"$timestamp\"
    "
}

# 標準的なメタデータ照会
get_phase_status() {
    local metadata_file="$1"
    local phase_name="$2"
    local status_field="${3:-created}"
    
    jq -r ".phases.${phase_name}.${status_field} // false" "$metadata_file" 2>/dev/null
}

# 現在のフェーズ取得
get_current_phase() {
    local metadata_file="$1"
    
    jq -r '.phase // "unknown"' "$metadata_file" 2>/dev/null
}

echo "メタデータ標準パターン関数が読み込まれました"