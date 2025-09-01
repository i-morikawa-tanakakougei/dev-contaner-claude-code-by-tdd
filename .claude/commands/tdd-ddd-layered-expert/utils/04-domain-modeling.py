#!/usr/bin/env python3
"""
Domain Modeling Command - 改修版
ユースケースからドメインモデルを設計し、実行履歴を更新
"""

import json
import os
import sys
from datetime import datetime
from pathlib import Path

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status
)


def find_use_case_json(issue_number):
    """Issue番号からJSONファイルを検索"""
    use_cases_dir = Path("docs/use_cases")
    
    if not use_cases_dir.exists():
        return None
    
    # issue-{number}-*.json パターンで検索
    for json_file in use_cases_dir.glob(f"issue-{issue_number}-*.json"):
        return str(json_file)
    
    # 単純なissue-{number}.json も検索
    simple_path = use_cases_dir / f"issue-{issue_number}.json"
    if simple_path.exists():
        return str(simple_path)
    
    return None


def create_domain_directory():
    """ドメインモデル用ディレクトリを作成"""
    domain_dir = Path("docs/domain")
    domain_dir.mkdir(parents=True, exist_ok=True)
    return domain_dir


def analyze_scenarios_for_domain_concepts(scenarios):
    """シナリオからドメイン概念を分析・抽出"""
    domain_concepts = {
        "entities": [],
        "value_objects": [],
        "domain_services": [],
        "business_rules": [],
        "ubiquitous_language": {}
    }
    
    # 全シナリオを統合
    all_scenarios = []
    all_scenarios.extend(scenarios.get("main_scenarios", []))
    all_scenarios.extend(scenarios.get("alternative_scenarios", []))
    all_scenarios.extend(scenarios.get("exception_scenarios", []))
    
    # エンティティ候補の抽出
    entity_candidates = set()
    value_object_candidates = set()
    business_rules = []
    language_terms = {}
    
    for scenario in all_scenarios:
        scenario_text = f"{scenario.get('given', '')} {scenario.get('when', '')} {scenario.get('then', '')}"
        
        # よく使われる名詞を抽出（エンティティ候補）
        import re
        nouns = re.findall(r'\b[A-Z][a-z]+\b', scenario_text)
        for noun in nouns:
            if noun not in ['Given', 'When', 'Then', 'And', 'But']:
                entity_candidates.add(noun)
        
        # 値オブジェクト候補（IDやコードなど）
        ids_and_codes = re.findall(r'\b[A-Z][a-z]*(?:Id|Code|Number|Name|Email|Address)\b', scenario_text)
        for item in ids_and_codes:
            value_object_candidates.add(item)
        
        # ビジネスルール（shouldやmustを含む文）
        rule_patterns = [
            r'should\s+([^.]+)',
            r'must\s+([^.]+)',
            r'cannot\s+([^.]+)',
            r'is\s+required',
            r'validation\s+([^.]+)'
        ]
        
        for pattern in rule_patterns:
            matches = re.findall(pattern, scenario_text, re.IGNORECASE)
            for match in matches:
                business_rules.append({
                    "id": f"br_{len(business_rules) + 1}",
                    "description": match.strip(),
                    "scenario_id": scenario.get("id", "unknown")
                })
    
    # エンティティを定義
    for entity_name in sorted(entity_candidates):
        if len(entity_name) > 2:  # 短すぎる名前を除外
            domain_concepts["entities"].append({
                "name": entity_name,
                "description": f"{entity_name}エンティティ - ビジネス上重要な識別可能なオブジェクト",
                "properties": {
                    "id": {"type": "str", "required": True, "description": f"{entity_name}の一意識別子"},
                    "created_at": {"type": "datetime", "required": True, "description": "作成日時"},
                    "updated_at": {"type": "datetime", "required": True, "description": "更新日時"}
                },
                "invariants": [
                    f"{entity_name}のIDは空であってはならない",
                    f"{entity_name}は作成後に削除されるまで存在し続ける"
                ]
            })
    
    # 値オブジェクトを定義
    for vo_name in sorted(value_object_candidates):
        if len(vo_name) > 2:
            domain_concepts["value_objects"].append({
                "name": vo_name,
                "description": f"{vo_name}値オブジェクト - 不変な値を表現",
                "validation_rules": [
                    f"{vo_name}は不変でなければならない",
                    f"{vo_name}は値による等価性を持つ"
                ]
            })
    
    # ドメインサービス（複雑な業務ロジック）を推定
    if len(entity_candidates) > 1:
        main_entity = sorted(entity_candidates)[0] if entity_candidates else "Domain"
        domain_concepts["domain_services"].append({
            "name": f"{main_entity}DomainService",
            "description": f"{main_entity}に関連する複雑なビジネスロジックを処理",
            "responsibilities": [
                "複数のエンティティにまたがるビジネスルール実行",
                "複雑な計算やバリデーションロジック",
                "ドメイン固有の処理"
            ]
        })
    
    # ビジネスルールを設定
    domain_concepts["business_rules"] = business_rules
    
    # ユビキタス言語の構築
    all_terms = entity_candidates.union(value_object_candidates)
    for term in sorted(all_terms):
        if len(term) > 2:
            language_terms[term] = f"{term}はこのドメインにおいて重要な概念"
    
    domain_concepts["ubiquitous_language"] = language_terms
    
    return domain_concepts


def generate_domain_model_document(use_case_data, domain_concepts, issue_number):
    """ドメインモデル設計書を生成"""
    
    metadata = use_case_data.get("metadata", {})
    title = metadata.get("title", f"Issue {issue_number}")
    
    content = f"""# ドメインモデル設計 - Issue #{issue_number}

## 概要
**タイトル**: {title}
**Issue**: #{issue_number}
**作成日**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## ドメイン分析

### 識別されたドメイン概念

#### エンティティ ({len(domain_concepts['entities'])}個)
"""
    
    for entity in domain_concepts["entities"]:
        content += f"""
##### {entity['name']}
- **説明**: {entity['description']}
- **プロパティ**:
"""
        for prop_name, prop_info in entity.get("properties", {}).items():
            required = "必須" if prop_info.get("required") else "任意"
            content += f"  - `{prop_name}`: {prop_info.get('type', 'any')} ({required}) - {prop_info.get('description', '')}\n"
        
        content += "- **不変条件**:\n"
        for invariant in entity.get("invariants", []):
            content += f"  - {invariant}\n"
    
    content += f"""
#### 値オブジェクト ({len(domain_concepts['value_objects'])}個)
"""
    
    for vo in domain_concepts["value_objects"]:
        content += f"""
##### {vo['name']}
- **説明**: {vo['description']}
- **検証ルール**:
"""
        for rule in vo.get("validation_rules", []):
            content += f"  - {rule}\n"
    
    content += f"""
#### ドメインサービス ({len(domain_concepts['domain_services'])}個)
"""
    
    for service in domain_concepts["domain_services"]:
        content += f"""
##### {service['name']}
- **説明**: {service['description']}
- **責務**:
"""
        for responsibility in service.get("responsibilities", []):
            content += f"  - {responsibility}\n"
    
    content += f"""
#### ビジネスルール ({len(domain_concepts['business_rules'])}個)
"""
    
    for rule in domain_concepts["business_rules"]:
        content += f"""
##### {rule['id']}
- **説明**: {rule['description']}
- **関連シナリオ**: {rule.get('scenario_id', 'N/A')}
"""
    
    content += f"""
## ユビキタス言語

| 用語 | 定義 |
|------|------|
"""
    
    for term, definition in domain_concepts["ubiquitous_language"].items():
        content += f"| {term} | {definition} |\n"
    
    content += f"""
## アグリゲート設計

### 推奨アグリゲート境界

"""
    
    # エンティティが複数ある場合はアグリゲート提案
    entities = domain_concepts["entities"]
    if len(entities) > 1:
        main_entity = entities[0]["name"]
        content += f"""
#### {main_entity}アグリゲート
- **アグリゲートルート**: {main_entity}
- **含まれるエンティティ**: 
  - {main_entity} (ルート)
"""
        for entity in entities[1:3]:  # 最大3個まで表示
            content += f"  - {entity['name']}\n"
        
        content += f"""
- **整合性境界**: {main_entity}に関連する操作は単一のトランザクションで実行
- **リポジトリ**: {main_entity}Repository
"""
    else:
        content += "単一エンティティのため、シンプルなアグリゲート構造を推奨\n"
    
    content += f"""
## 実装ガイドライン

### 次のステップ
1. **TDD実装**: `/create-tests {issue_number}` でテスト作成
2. **ドメイン実装**: `/implement-domain {issue_number}` で実装
3. **アプリケーション層**: `/implement-usecase {issue_number}` で統合

### 設計原則
- **ドメイン純粋性**: 外部依存を持たない純粋なビジネスロジック
- **不変性**: 値オブジェクトの不変性を維持
- **カプセル化**: エンティティの内部状態を適切に保護
- **ユビキタス言語**: 開発者とドメインエキスパート間の共通言語使用

---
*このドキュメントは自動生成されました。ドメインエキスパートとのレビューを通じて改善してください。*
"""
    
    return content


def update_use_case_json_with_domain_model(json_file_path, domain_concepts):
    """ユースケースJSONにドメインモデル情報を更新"""
    
    use_case_data = load_use_case_json(json_file_path)
    
    # ドメインモデル情報を更新
    use_case_data["domain_model"] = domain_concepts
    
    # アーキテクチャ整合性情報を更新
    architecture = use_case_data.get("architecture_alignment", {})
    architecture.setdefault("layers", {})["domain"] = False  # まだ実装していない
    architecture.setdefault("patterns_used", []).extend([
        "Domain-Driven Design",
        "Entity-Value Object Pattern",
        "Aggregate Pattern"
    ])
    use_case_data["architecture_alignment"] = architecture
    
    # 保存
    save_use_case_json(json_file_path, use_case_data)
    
    return use_case_data


def main():
    """メイン処理"""
    
    # 引数チェック
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /domain-modeling <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    print(f"\n🏗️ Issue #{issue_number} のドメインモデル設計を開始します\n")
    
    # ユースケースJSONファイルを検索
    print("📁 ユースケースJSONファイルを検索中...")
    json_file_path = find_use_case_json(issue_number)
    
    if not json_file_path:
        print(f"❌ Issue #{issue_number} のユースケースJSONが見つかりません")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    
    print(f"✅ JSONファイルを発見: {json_file_path}")
    
    # ユースケースデータを読み込み
    print("📝 ユースケースデータを読み込み中...")
    use_case_data = load_use_case_json(json_file_path)
    
    # シナリオからドメイン概念を分析
    print("🔍 シナリオからドメイン概念を分析中...")
    scenarios = use_case_data.get("scenarios", {})
    domain_concepts = analyze_scenarios_for_domain_concepts(scenarios)
    
    print(f"✅ ドメイン概念分析完了:")
    print(f"  - エンティティ: {len(domain_concepts['entities'])}個")
    print(f"  - 値オブジェクト: {len(domain_concepts['value_objects'])}個")
    print(f"  - ドメインサービス: {len(domain_concepts['domain_services'])}個")
    print(f"  - ビジネスルール: {len(domain_concepts['business_rules'])}個")
    print(f"  - ユビキタス言語: {len(domain_concepts['ubiquitous_language'])}個")
    
    # ドメインモデル設計書を生成
    print("📋 ドメインモデル設計書を生成中...")
    domain_dir = create_domain_directory()
    
    domain_doc_content = generate_domain_model_document(use_case_data, domain_concepts, issue_number)
    domain_doc_path = domain_dir / f"issue-{issue_number}-domain-model.md"
    
    with open(domain_doc_path, 'w', encoding='utf-8') as f:
        f.write(domain_doc_content)
    
    print(f"✅ ドメインモデル設計書を作成: {domain_doc_path}")
    
    # ユースケースJSONにドメインモデル情報を更新
    print("📊 ユースケースJSONを更新中...")
    updated_data = update_use_case_json_with_domain_model(json_file_path, domain_concepts)
    
    # 実行履歴を更新
    update_execution_history(
        json_file_path,
        f"/domain-modeling {issue_number}",
        "success",
        [str(domain_doc_path)]
    )
    
    # 最新データを読み込んで表示
    final_data = load_use_case_json(json_file_path)
    
    # 実行状況を表示
    print("\n" + "="*60)
    print(format_execution_status(final_data))
    print("="*60)
    
    # サマリー表示
    print(f"\n📊 実行サマリー")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🏗️ ドメインモデル設計: 完了")
    print(f"✅ 分析シナリオ数: {len(scenarios.get('main_scenarios', [])) + len(scenarios.get('alternative_scenarios', [])) + len(scenarios.get('exception_scenarios', []))}")
    print(f"✅ 特定されたエンティティ: {len(domain_concepts['entities'])}個")
    print(f"✅ 特定された値オブジェクト: {len(domain_concepts['value_objects'])}個")
    print(f"✅ 抽出されたビジネスルール: {len(domain_concepts['business_rules'])}個")
    print(f"✅ ユビキタス言語用語: {len(domain_concepts['ubiquitous_language'])}個")
    
    print(f"\n📁 成果物")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"✅ {domain_doc_path}")
    print(f"✅ {json_file_path} (ドメインモデル情報更新)")
    
    print(f"\n⏭️ 次の推奨コマンド")
    print(f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"1. /create-tests {issue_number}")
    print(f"   → ドメインモデルベースのテスト作成（TDD RED Phase）")
    print(f"2. ドメインモデル設計書のレビュー")
    print(f"   → {domain_doc_path} をドメインエキスパートと確認")
    
    print(f"\n💡 ドメインモデル設計完了")
    print(f"設計書を確認し、必要に応じてドメインエキスパートとレビューしてください。")


if __name__ == "__main__":
    main()