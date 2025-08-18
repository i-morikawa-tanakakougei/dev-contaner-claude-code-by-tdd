#!/bin/bash

# レイヤードアーキテクチャ検証機能
# DDD/Clean Architecture の依存関係とレイヤー純粋性を検証

set -euo pipefail

# レイヤー依存関係の定義
declare -A ALLOWED_DEPENDENCIES=(
    # Domain層: 外部依存なし（標準ライブラリのみ）
    ["domain"]="datetime,uuid,enum,dataclasses,typing,abc,json"
    
    # Application層: Domain層のみ依存可能
    ["application"]="domain,datetime,uuid,enum,dataclasses,typing,abc,json"
    
    # Infrastructure層: Domain, Application層依存可能
    ["infrastructure"]="domain,application,sqlalchemy,requests,boto3,redis,asyncpg,psycopg2,fastapi,uvicorn"
    
    # Presentation層: Application層のみ依存可能（Domain直接依存は禁止）
    ["presentation"]="application,fastapi,pydantic,uvicorn,click,typer,starlette"
)

# 禁止されている依存関係の定義
declare -A FORBIDDEN_DEPENDENCIES=(
    # Domain層: あらゆる外部ライブラリ、フレームワーク依存を禁止
    ["domain"]="sqlalchemy,requests,fastapi,flask,django,boto3,redis,asyncpg,psycopg2,celery,pydantic,click,typer"
    
    # Application層: インフラストラクチャ、プレゼンテーション依存を禁止
    ["application"]="sqlalchemy,requests,fastapi,flask,django,boto3,redis,asyncpg,psycopg2,celery,click,typer,uvicorn"
    
    # Presentation層: Domain直接依存、Infrastructure依存を禁止
    ["presentation"]="domain,sqlalchemy,requests,boto3,redis,asyncpg,psycopg2,celery"
)

# Python ファイルから import 文を抽出
extract_imports() {
    local file_path="$1"
    
    if [[ ! -f "$file_path" ]]; then
        return 1
    fi
    
    # from文とimport文の両方を抽出
    grep -E "^(from|import)\s+" "$file_path" 2>/dev/null | \
    sed -E 's/^from\s+([^.\s]+)(\.[^.\s]+)*\s+import.*/\1/' | \
    sed -E 's/^import\s+([^.\s]+)(\.[^.\s]+)*/\1/' | \
    grep -v "^#" | \
    sort -u || true
}

# レイヤーの特定
determine_layer() {
    local file_path="$1"
    
    case "$file_path" in
        */domain/*)
            echo "domain"
            ;;
        */application/*)
            echo "application"
            ;;
        */infrastructure/*)
            echo "infrastructure"
            ;;
        */presentation/*)
            echo "presentation"
            ;;
        *)
            echo "unknown"
            ;;
    esac
}

# 依存関係の検証
validate_layer_dependencies() {
    local file_path="$1"
    local layer="$2"
    local violations=()
    
    echo "レイヤー検証: $layer - $file_path"
    
    # ファイルから import を抽出
    local imports
    imports=$(extract_imports "$file_path")
    
    if [[ -z "$imports" ]]; then
        echo "  ✅ import文が見つかりません"
        return 0
    fi
    
    # 禁止依存関係のチェック
    local forbidden="${FORBIDDEN_DEPENDENCIES[$layer]:-}"
    if [[ -n "$forbidden" ]]; then
        IFS=',' read -ra FORBIDDEN_LIST <<< "$forbidden"
        
        for import_module in $imports; do
            for forbidden_module in "${FORBIDDEN_LIST[@]}"; do
                if [[ "$import_module" == "$forbidden_module" ]] || 
                   [[ "$import_module" == *".$forbidden_module"* ]]; then
                    violations+=("❌ 禁止依存: $import_module ($forbidden_module)")
                fi
            done
        done
    fi
    
    # 相対インポートのチェック（レイヤー間の直接依存）
    while read -r line; do
        if [[ -n "$line" ]]; then
            case "$layer" in
                "domain")
                    # Domain層は他のレイヤーに依存してはいけない
                    if [[ "$line" =~ (application|infrastructure|presentation) ]]; then
                        violations+=("❌ レイヤー違反: Domain層が他レイヤーに依存 - $line")
                    fi
                    ;;
                "application")
                    # Application層はInfrastructure, Presentationに依存してはいけない
                    if [[ "$line" =~ (infrastructure|presentation) ]]; then
                        violations+=("❌ レイヤー違反: Application層が下位レイヤーに依存 - $line")
                    fi
                    ;;
                "presentation")
                    # Presentation層はDomainに直接依存してはいけない
                    if [[ "$line" =~ domain ]] && [[ ! "$line" =~ application ]]; then
                        violations+=("❌ レイヤー違反: Presentation層がDomain層に直接依存 - $line")
                    fi
                    if [[ "$line" =~ infrastructure ]]; then
                        violations+=("❌ レイヤー違反: Presentation層がInfrastructure層に依存 - $line")
                    fi
                    ;;
            esac
        fi
    done <<< "$imports"
    
    # 結果表示
    if [[ ${#violations[@]} -eq 0 ]]; then
        echo "  ✅ レイヤー依存関係OK"
        return 0
    else
        echo "  ❌ レイヤー依存関係違反が発見されました:"
        for violation in "${violations[@]}"; do
            echo "    $violation"
        done
        return 1
    fi
}

# ドメインモデルの純粋性チェック
validate_domain_purity() {
    local domain_dir="src/domain"
    local violations=()
    
    echo "ドメイン層純粋性検証..."
    
    if [[ ! -d "$domain_dir" ]]; then
        echo "  ⚠️  Domain層ディレクトリが存在しません: $domain_dir"
        return 0
    fi
    
    # ドメイン層のPythonファイルをチェック
    while IFS= read -r -d '' file; do
        echo "  チェック中: $file"
        
        # I/O操作の検出
        if grep -q -E "(open\(|with\s+open|requests\.|urllib|socket)" "$file"; then
            violations+=("❌ I/O操作検出: $file")
        fi
        
        # データベース関連の検出
        if grep -q -E "(session\.|Session|sqlalchemy|psycopg|asyncpg)" "$file"; then
            violations+=("❌ データベース操作検出: $file")
        fi
        
        # 外部API呼び出しの検出
        if grep -q -E "(requests\.|httpx\.|aiohttp)" "$file"; then
            violations+=("❌ 外部API呼び出し検出: $file")
        fi
        
        # フレームワーク依存の検出
        if grep -q -E "(fastapi|flask|django|click|typer)" "$file"; then
            violations+=("❌ フレームワーク依存検出: $file")
        fi
        
        # 非同期I/O操作の検出
        if grep -q -E "(asyncio\.sleep|aiofiles|async\s+def.*\s+(read|write|fetch|post|get))" "$file"; then
            violations+=("❌ 非同期I/O操作検出: $file")
        fi
        
    done < <(find "$domain_dir" -name "*.py" -type f -print0)
    
    # 結果表示
    if [[ ${#violations[@]} -eq 0 ]]; then
        echo "  ✅ ドメイン層純粋性OK"
        return 0
    else
        echo "  ❌ ドメイン層純粋性違反が発見されました:"
        for violation in "${violations[@]}"; do
            echo "    $violation"
        done
        return 1
    fi
}

# アグリゲート境界の検証
validate_aggregate_boundaries() {
    local domain_dir="src/domain"
    local violations=()
    
    echo "アグリゲート境界検証..."
    
    if [[ ! -d "$domain_dir/entities" ]]; then
        echo "  ⚠️  Entitiesディレクトリが存在しません"
        return 0
    fi
    
    # エンティティ間の直接参照をチェック
    while IFS= read -r -d '' entity_file; do
        local entity_name
        entity_name=$(basename "$entity_file" .py)
        
        # 他のエンティティを直接importしているかチェック
        while IFS= read -r -d '' other_entity; do
            local other_name
            other_name=$(basename "$other_entity" .py)
            
            if [[ "$entity_name" != "$other_name" ]] && \
               grep -q "from.*entities.*import.*$other_name" "$entity_file"; then
                violations+=("⚠️  エンティティ間直接参照: $entity_name -> $other_name")
            fi
        done < <(find "$domain_dir/entities" -name "*.py" -type f -print0)
        
    done < <(find "$domain_dir/entities" -name "*.py" -type f -print0)
    
    # 結果表示
    if [[ ${#violations[@]} -eq 0 ]]; then
        echo "  ✅ アグリゲート境界OK"
        return 0
    else
        echo "  ⚠️  アグリゲート境界の問題が発見されました:"
        for violation in "${violations[@]}"; do
            echo "    $violation"
        done
        return 1
    fi
}

# リポジトリパターンの検証
validate_repository_pattern() {
    local violations=()
    
    echo "リポジトリパターン検証..."
    
    # Domain層のリポジトリインターフェース確認
    local domain_repo_dir="src/domain/repositories"
    local infra_repo_dir="src/infrastructure/repositories"
    
    if [[ ! -d "$domain_repo_dir" ]]; then
        echo "  ⚠️  Domain層リポジトリディレクトリが存在しません"
        return 0
    fi
    
    # Domain層リポジトリがabstractクラスかチェック
    while IFS= read -r -d '' repo_file; do
        if [[ -f "$repo_file" ]]; then
            if ! grep -q "@abstractmethod\|ABC\|Protocol" "$repo_file"; then
                local repo_name
                repo_name=$(basename "$repo_file" .py)
                violations+=("⚠️  リポジトリインターフェースが抽象クラスではありません: $repo_name")
            fi
        fi
    done < <(find "$domain_repo_dir" -name "*.py" -type f -print0)
    
    # Infrastructure層の実装確認
    if [[ -d "$infra_repo_dir" ]]; then
        while IFS= read -r -d '' impl_file; do
            local impl_name
            impl_name=$(basename "$impl_file" .py)
            
            # 対応するDomain層インターフェースが存在するかチェック
            local interface_file="$domain_repo_dir/${impl_name%.py}.py"
            interface_file="${interface_file//_impl/}"
            
            if [[ ! -f "$interface_file" ]]; then
                violations+=("⚠️  リポジトリ実装に対応するインターフェースがありません: $impl_name")
            fi
        done < <(find "$infra_repo_dir" -name "*.py" -type f -print0)
    fi
    
    # 結果表示
    if [[ ${#violations[@]} -eq 0 ]]; then
        echo "  ✅ リポジトリパターンOK"
        return 0
    else
        echo "  ⚠️  リポジトリパターンの問題が発見されました:"
        for violation in "${violations[@]}"; do
            echo "    $violation"
        done
        return 1
    fi
}

# 包括的なアーキテクチャ検証
validate_architecture() {
    echo "🏗️  レイヤードアーキテクチャ検証を開始します..."
    echo "=================================================="
    
    local total_violations=0
    local src_dir="src"
    
    if [[ ! -d "$src_dir" ]]; then
        echo "❌ srcディレクトリが存在しません。プロジェクト構造を確認してください。"
        return 1
    fi
    
    # 1. レイヤー依存関係の検証
    echo ""
    echo "📋 1. レイヤー依存関係検証"
    echo "------------------------"
    
    while IFS= read -r -d '' file; do
        local layer
        layer=$(determine_layer "$file")
        
        if [[ "$layer" != "unknown" ]]; then
            if ! validate_layer_dependencies "$file" "$layer"; then
                ((total_violations++))
            fi
        fi
    done < <(find "$src_dir" -name "*.py" -type f -print0)
    
    # 2. ドメイン層純粋性の検証
    echo ""
    echo "🏛️  2. ドメイン層純粋性検証"
    echo "------------------------"
    
    if ! validate_domain_purity; then
        ((total_violations++))
    fi
    
    # 3. アグリゲート境界の検証
    echo ""
    echo "🔗 3. アグリゲート境界検証"
    echo "----------------------"
    
    if ! validate_aggregate_boundaries; then
        ((total_violations++))
    fi
    
    # 4. リポジトリパターンの検証
    echo ""
    echo "🗃️  4. リポジトリパターン検証"
    echo "-------------------------"
    
    if ! validate_repository_pattern; then
        ((total_violations++))
    fi
    
    # 結果サマリー
    echo ""
    echo "=================================================="
    echo "🏗️  アーキテクチャ検証結果"
    echo "=================================================="
    
    if [[ $total_violations -eq 0 ]]; then
        echo "✅ アーキテクチャ検証: 問題なし"
        echo "   レイヤードアーキテクチャが正しく実装されています"
        return 0
    else
        echo "❌ アーキテクチャ検証: $total_violations 個の問題が発見されました"
        echo ""
        echo "🔧 修正推奨事項:"
        echo "1. ドメイン層から外部依存を除去してください"
        echo "2. レイヤー間の適切な依存関係を確保してください"
        echo "3. リポジトリパターンを正しく実装してください"
        echo "4. アグリゲート境界を明確に定義してください"
        return 1
    fi
}

# 特定レイヤーのみの検証
validate_specific_layer() {
    local layer="$1"
    local src_dir="src/$layer"
    
    echo "🔍 $layer 層の検証を実行中..."
    
    if [[ ! -d "$src_dir" ]]; then
        echo "⚠️  $layer 層ディレクトリが存在しません: $src_dir"
        return 0
    fi
    
    local violations=0
    
    while IFS= read -r -d '' file; do
        if ! validate_layer_dependencies "$file" "$layer"; then
            ((violations++))
        fi
    done < <(find "$src_dir" -name "*.py" -type f -print0)
    
    if [[ $violations -eq 0 ]]; then
        echo "✅ $layer 層: 問題なし"
        return 0
    else
        echo "❌ $layer 層: $violations 個の問題が発見されました"
        return 1
    fi
}