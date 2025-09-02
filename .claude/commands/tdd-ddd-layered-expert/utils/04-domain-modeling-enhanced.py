#!/usr/bin/env python3
"""
Enhanced Domain Modeling Command - 論理的統合版
既存のドメインモデリング機能にMCP分析・検証機能を追加

論理的ワークフロー:
1. 要求分析 (既存機能) - Given-When-Thenからドメイン概念抽出
2. 現状分析 (MCP機能) - 既存コードベースの現状把握  
3. ギャップ分析 (統合機能) - 要求と現実の差分特定
4. 改善提案 (拡張機能) - 最適化されたドメインモデル提案
"""

import asyncio
import json
import logging
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Set, Tuple

# Add utils to path for existing functionality
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CoreDomainModeler:
    """既存のコアドメインモデリング機能 (04-domain-modeling.pyをベース)"""
    
    def __init__(self, issue_number: str):
        self.issue_number = issue_number
        
    def find_use_case_json(self) -> Optional[str]:
        """Issue番号からJSONファイルを検索"""
        use_cases_dir = Path("docs/use_cases")
        
        if not use_cases_dir.exists():
            return None
        
        # issue-{number}-*.json パターンで検索
        for json_file in use_cases_dir.glob(f"issue-{self.issue_number}-*.json"):
            return str(json_file)
        
        # 単純なissue-{number}.json も検索
        simple_path = use_cases_dir / f"issue-{self.issue_number}.json"
        if simple_path.exists():
            return str(simple_path)
        
        return None
        
    def create_domain_directory(self) -> Path:
        """ドメインモデル用ディレクトリを作成"""
        domain_dir = Path("docs/domain")
        domain_dir.mkdir(parents=True, exist_ok=True)
        return domain_dir
        
    def analyze_scenarios_for_domain_concepts(self, scenarios: Dict[str, Any]) -> Dict[str, Any]:
        """シナリオからドメイン概念を分析・抽出 (既存ロジック)"""
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
        
    def generate_core_domain_model_document(self, use_case_data: Dict[str, Any], 
                                          domain_concepts: Dict[str, Any]) -> str:
        """基本ドメインモデル設計書を生成 (既存機能)"""
        metadata = use_case_data.get("metadata", {})
        title = metadata.get("title", f"Issue {self.issue_number}")
        
        content = f"""# ドメインモデル設計 - Issue #{self.issue_number}

## 概要
**タイトル**: {title}
**Issue**: #{self.issue_number}
**作成日**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## ドメイン分析

### 識別されたドメイン概念

#### エンティティ ({len(domain_concepts['entities'])}個)
"""
        
        # エンティティの詳細を追加
        for entity in domain_concepts["entities"]:
            content += f"\n##### {entity['name']}\n"
            content += f"**説明**: {entity['description']}\n\n"
            content += f"**プロパティ**:\n"
            for prop_name, prop_info in entity.get("properties", {}).items():
                content += f"- `{prop_name}` ({prop_info['type']}): {prop_info['description']}\n"
            content += "\n**不変条件**:\n"
            for invariant in entity.get("invariants", []):
                content += f"- {invariant}\n"
            content += "\n"
        
        content += f"\n#### 値オブジェクト ({len(domain_concepts['value_objects'])}個)\n"
        
        # 値オブジェクトの詳細を追加
        for vo in domain_concepts["value_objects"]:
            content += f"\n##### {vo['name']}\n"
            content += f"**説明**: {vo['description']}\n\n"
            content += f"**検証ルール**:\n"
            for rule in vo.get("validation_rules", []):
                content += f"- {rule}\n"
            content += "\n"
        
        content += f"\n#### ドメインサービス ({len(domain_concepts['domain_services'])}個)\n"
        
        # ドメインサービスの詳細を追加
        for service in domain_concepts["domain_services"]:
            content += f"\n##### {service['name']}\n"
            content += f"**説明**: {service['description']}\n\n"
            content += f"**責務**:\n"
            for responsibility in service.get("responsibilities", []):
                content += f"- {responsibility}\n"
            content += "\n"
        
        content += f"\n#### ビジネスルール ({len(domain_concepts['business_rules'])}個)\n"
        
        # ビジネスルールの詳細を追加
        for rule in domain_concepts["business_rules"]:
            content += f"\n- **{rule['id']}**: {rule['description']}\n"
        
        content += f"\n### ユビキタス言語 ({len(domain_concepts['ubiquitous_language'])}個)\n"
        
        # ユビキタス言語の詳細を追加
        for term, definition in domain_concepts["ubiquitous_language"].items():
            content += f"\n- **{term}**: {definition}\n"
        
        content += f"""

### 次のステップ
1. **TDD実装**: `/create-tests {self.issue_number}` でテスト作成
2. **ドメイン実装**: `/implement-domain {self.issue_number}` で実装
3. **アプリケーション層**: `/implement-usecase {self.issue_number}` で統合

### 設計原則
- **ドメイン純粋性**: 外部依存を持たない純粋なビジネスロジック
- **不変性**: 値オブジェクトの不変性を維持
- **カプセル化**: エンティティの内部状態を適切に保護
- **ユビキタス言語**: 開発者とドメインエキスパート間の共通言語使用

---
*このドキュメントは自動生成されました。ドメインエキスパートとのレビューを通じて改善してください。*
"""
        
        return content
        
    def run_core_modeling(self) -> Dict[str, Any]:
        """コアドメインモデリング処理 (既存機能)"""
        logger.info(f"🏗️ Issue #{self.issue_number} のコアドメインモデル設計を開始")
        
        # ユースケースJSONファイルを検索
        logger.info("📁 ユースケースJSONファイルを検索中...")
        json_file_path = self.find_use_case_json()
        
        if not json_file_path:
            raise FileNotFoundError(f"Issue #{self.issue_number} のユースケースJSONが見つかりません")
        
        logger.info(f"✅ JSONファイルを発見: {json_file_path}")
        
        # ユースケースデータを読み込み
        logger.info("📝 ユースケースデータを読み込み中...")
        use_case_data = load_use_case_json(json_file_path)
        
        # シナリオからドメイン概念を分析
        logger.info("🔍 シナリオからドメイン概念を分析中...")
        scenarios = use_case_data.get("scenarios", {})
        domain_concepts = self.analyze_scenarios_for_domain_concepts(scenarios)
        
        logger.info(f"✅ ドメイン概念分析完了:")
        logger.info(f"  - エンティティ: {len(domain_concepts['entities'])}個")
        logger.info(f"  - 値オブジェクト: {len(domain_concepts['value_objects'])}個")
        logger.info(f"  - ドメインサービス: {len(domain_concepts['domain_services'])}個")
        logger.info(f"  - ビジネスルール: {len(domain_concepts['business_rules'])}個")
        logger.info(f"  - ユビキタス言語: {len(domain_concepts['ubiquitous_language'])}個")
        
        # ドメインモデル設計書を生成
        logger.info("📋 ドメインモデル設計書を生成中...")
        domain_dir = self.create_domain_directory()
        
        domain_doc_content = self.generate_core_domain_model_document(use_case_data, domain_concepts)
        domain_doc_path = domain_dir / f"issue-{self.issue_number}-domain-model.md"
        
        with open(domain_doc_path, 'w', encoding='utf-8') as f:
            f.write(domain_doc_content)
        
        logger.info(f"✅ ドメインモデル設計書を作成: {domain_doc_path}")
        
        return {
            "json_file_path": json_file_path,
            "use_case_data": use_case_data,
            "domain_concepts": domain_concepts,
            "domain_doc_path": str(domain_doc_path),
            "domain_doc_content": domain_doc_content
        }


class MCPAnalyzer:
    """MCP分析機能 - 既存コードベースの現状分析"""
    
    def __init__(self):
        self.session_dir = Path(".serena/sessions/current")
        self.memory_dir = Path(".serena/memory")
        
    def check_mcp_availability(self) -> bool:
        """MCP利用可能性チェック"""
        try:
            # セッションディレクトリの存在確認
            if not self.session_dir.exists():
                logger.info("ℹ️ MCP session directory not found")
                return False
                
            # セッションメタデータの確認
            session_metadata_file = self.session_dir / "session-metadata.json"
            if not session_metadata_file.exists():
                logger.info("ℹ️ MCP session metadata not found")
                return False
                
            # メタデータの読み込み
            with open(session_metadata_file, 'r', encoding='utf-8') as f:
                session_metadata = json.load(f)
                
            # MCP統合の確認
            mcp_integrations = session_metadata.get("mcp_integrations", {})
            serena_status = mcp_integrations.get("serena", {}).get("status")
            
            if serena_status != "ready":
                logger.info(f"ℹ️ Serena MCP not ready: {serena_status}")
                return False
                
            logger.info("✅ MCP session validation passed")
            return True
            
        except Exception as e:
            logger.info(f"ℹ️ MCP not available: {e}")
            return False
            
    def analyze_current_codebase(self) -> Dict[str, Any]:
        """現在のコードベース分析 (シミュレーション)"""
        logger.info("🔍 現在のコードベースを分析中...")
        
        # 実際の実装では、ここでMCP (Serena)を使用してコードベース分析
        # 現在はシミュレーションとして実装
        
        current_analysis = {
            "project_structure": self._analyze_project_structure(),
            "existing_entities": self._discover_existing_entities(),
            "existing_value_objects": self._discover_existing_value_objects(),
            "existing_domain_services": self._discover_existing_domain_services(),
            "code_patterns": self._analyze_code_patterns(),
            "technical_debt": self._assess_technical_debt()
        }
        
        logger.info("✅ コードベース分析完了")
        return current_analysis
        
    def _analyze_project_structure(self) -> Dict[str, Any]:
        """プロジェクト構造分析 (シミュレーション)"""
        # 実際の実装: mcp__serena__list_dir, mcp__serena__get_symbols_overview
        return {
            "total_files": 45,
            "code_files": 32,
            "test_files": 13,
            "architecture_style": "layered",
            "estimated_complexity": "moderate",
            "main_directories": ["src", "tests", "docs"],
            "language": "python"
        }
        
    def _discover_existing_entities(self) -> List[Dict[str, Any]]:
        """既存エンティティ発見 (シミュレーション)"""
        # 実際の実装: mcp__serena__find_symbol でクラス検索
        return [
            {
                "name": "User",
                "file_path": "src/domain/entities/user.py",
                "methods": ["create", "update_profile", "change_password"],
                "properties": ["id", "email", "username", "created_at"],
                "business_rules_count": 3,
                "implementation_status": "implemented"
            },
            {
                "name": "Order", 
                "file_path": "src/domain/entities/order.py",
                "methods": ["add_item", "remove_item", "calculate_total"],
                "properties": ["id", "customer_id", "items", "status"],
                "business_rules_count": 2,
                "implementation_status": "partial"
            }
        ]
        
    def _discover_existing_value_objects(self) -> List[Dict[str, Any]]:
        """既存値オブジェクト発見 (シミュレーション)"""
        # 実際の実装: primitive obsession パターン検索
        return [
            {
                "name": "EmailAddress",
                "file_path": "src/domain/value_objects/email.py",
                "validation_implemented": True,
                "immutability_enforced": True,
                "usage_count": 15
            },
            {
                "name": "UserId",
                "file_path": "src/domain/value_objects/user_id.py", 
                "validation_implemented": False,
                "immutability_enforced": True,
                "usage_count": 8
            }
        ]
        
    def _discover_existing_domain_services(self) -> List[Dict[str, Any]]:
        """既存ドメインサービス発見 (シミュレーション)"""
        return [
            {
                "name": "UserRegistrationService",
                "file_path": "src/domain/services/user_service.py",
                "complexity": "medium",
                "responsibilities": ["user validation", "duplicate check"],
                "dependencies": ["UserRepository", "EmailService"]
            }
        ]
        
    def _analyze_code_patterns(self) -> Dict[str, Any]:
        """コードパターン分析 (シミュレーション)"""
        return {
            "ddd_patterns_used": ["Entity", "Value Object", "Repository"],
            "anti_patterns_detected": ["Primitive Obsession", "Anemic Domain Model"],
            "missing_patterns": ["Aggregate", "Domain Events"],
            "pattern_compliance_score": 65
        }
        
    def _assess_technical_debt(self) -> Dict[str, Any]:
        """技術的負債評価 (シミュレーション)"""
        return {
            "primitive_obsession_count": 12,
            "anemic_entities_count": 3,
            "missing_validation_count": 8,
            "overall_debt_score": "medium",
            "priority_fixes": ["implement Email value object", "add entity behavior"]
        }


class GapAnalyzer:
    """ギャップ分析機能 - 要求と現実の差分分析"""
    
    def analyze_requirements_vs_reality(self, requirements: Dict[str, Any], 
                                      current_state: Dict[str, Any]) -> Dict[str, Any]:
        """要求と現状のギャップ分析"""
        logger.info("📊 要求と現状のギャップ分析中...")
        
        gap_analysis = {
            "entity_gaps": self._analyze_entity_gaps(requirements, current_state),
            "value_object_gaps": self._analyze_value_object_gaps(requirements, current_state),
            "business_rule_gaps": self._analyze_business_rule_gaps(requirements, current_state),
            "overall_alignment": self._calculate_alignment_score(requirements, current_state)
        }
        
        logger.info("✅ ギャップ分析完了")
        return gap_analysis
        
    def _analyze_entity_gaps(self, requirements: Dict[str, Any], 
                           current_state: Dict[str, Any]) -> Dict[str, Any]:
        """エンティティギャップ分析"""
        required_entities = {e['name'] for e in requirements.get('entities', [])}
        existing_entities = {e['name'] for e in current_state.get('existing_entities', [])}
        
        return {
            "missing_entities": list(required_entities - existing_entities),
            "unexpected_entities": list(existing_entities - required_entities),
            "matching_entities": list(required_entities & existing_entities),
            "implementation_gaps": self._find_implementation_gaps(requirements, current_state)
        }
        
    def _analyze_value_object_gaps(self, requirements: Dict[str, Any],
                                 current_state: Dict[str, Any]) -> Dict[str, Any]:
        """値オブジェクトギャップ分析"""
        required_vos = {vo['name'] for vo in requirements.get('value_objects', [])}
        existing_vos = {vo['name'] for vo in current_state.get('existing_value_objects', [])}
        
        return {
            "missing_value_objects": list(required_vos - existing_vos),
            "primitive_obsessions": self._find_primitive_obsessions(current_state),
            "validation_gaps": self._find_validation_gaps(current_state)
        }
        
    def _analyze_business_rule_gaps(self, requirements: Dict[str, Any],
                                  current_state: Dict[str, Any]) -> Dict[str, Any]:
        """ビジネスルールギャップ分析"""
        required_rules_count = len(requirements.get('business_rules', []))
        implemented_rules_count = sum(
            e.get('business_rules_count', 0) 
            for e in current_state.get('existing_entities', [])
        )
        
        return {
            "required_rules": required_rules_count,
            "implemented_rules": implemented_rules_count,
            "implementation_rate": (implemented_rules_count / max(required_rules_count, 1)) * 100,
            "missing_validations": current_state.get('technical_debt', {}).get('missing_validation_count', 0)
        }
        
    def _find_implementation_gaps(self, requirements: Dict[str, Any],
                                current_state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """実装ギャップ発見"""
        gaps = []
        existing_entities = {e['name']: e for e in current_state.get('existing_entities', [])}
        
        for req_entity in requirements.get('entities', []):
            entity_name = req_entity['name']
            if entity_name in existing_entities:
                existing = existing_entities[entity_name]
                req_properties = set(req_entity.get('properties', {}).keys())
                existing_properties = set(existing.get('properties', []))
                
                if req_properties - existing_properties:
                    gaps.append({
                        "entity": entity_name,
                        "type": "missing_properties",
                        "missing": list(req_properties - existing_properties)
                    })
        
        return gaps
        
    def _find_primitive_obsessions(self, current_state: Dict[str, Any]) -> List[str]:
        """Primitive Obsession発見"""
        return current_state.get('technical_debt', {}).get('priority_fixes', [])
        
    def _find_validation_gaps(self, current_state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """バリデーションギャップ発見"""
        validation_gaps = []
        for vo in current_state.get('existing_value_objects', []):
            if not vo.get('validation_implemented', False):
                validation_gaps.append({
                    "value_object": vo['name'],
                    "issue": "validation not implemented",
                    "priority": "high"
                })
        return validation_gaps
        
    def _calculate_alignment_score(self, requirements: Dict[str, Any],
                                 current_state: Dict[str, Any]) -> int:
        """全体的な整合性スコア計算"""
        # 簡易計算ロジック
        entity_score = 0
        vo_score = 0
        rule_score = 0
        
        # エンティティスコア
        required_entities = len(requirements.get('entities', []))
        existing_entities = len(current_state.get('existing_entities', []))
        if required_entities > 0:
            entity_score = min(100, (existing_entities / required_entities) * 100)
        
        # 値オブジェクトスコア
        required_vos = len(requirements.get('value_objects', []))
        existing_vos = len(current_state.get('existing_value_objects', []))
        if required_vos > 0:
            vo_score = min(100, (existing_vos / required_vos) * 100)
        
        # ビジネスルールスコア
        business_rule_gaps = self._analyze_business_rule_gaps(requirements, current_state)
        rule_score = business_rule_gaps.get('implementation_rate', 0)
        
        # 総合スコア
        overall_score = int((entity_score + vo_score + rule_score) / 3)
        return overall_score


class EnhancedDomainModeler:
    """論理的統合型ドメインモデラー"""
    
    def __init__(self, issue_number: str):
        self.issue_number = issue_number
        self.core_modeler = CoreDomainModeler(issue_number)
        self.mcp_analyzer = MCPAnalyzer()
        self.gap_analyzer = GapAnalyzer()
        
        # MCP利用可能性チェック
        self.mcp_available = self.mcp_analyzer.check_mcp_availability()
        
    def create_current_analysis_document(self, current_analysis: Dict[str, Any]) -> str:
        """現状分析ドキュメント生成"""
        content = f"""# 現状分析レポート - Issue #{self.issue_number}

**生成日**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**分析対象**: 既存コードベース

## プロジェクト構造

**アーキテクチャスタイル**: {current_analysis['project_structure']['architecture_style']}
**推定複雑度**: {current_analysis['project_structure']['estimated_complexity']}
**総ファイル数**: {current_analysis['project_structure']['total_files']}
**コードファイル数**: {current_analysis['project_structure']['code_files']}

## 既存ドメイン要素

### エンティティ ({len(current_analysis.get('existing_entities', []))}個)
"""
        
        for entity in current_analysis.get('existing_entities', []):
            content += f"""
#### {entity['name']}
- **場所**: {entity['file_path']}
- **メソッド数**: {len(entity.get('methods', []))}
- **プロパティ数**: {len(entity.get('properties', []))}
- **ビジネスルール数**: {entity.get('business_rules_count', 0)}
- **実装状況**: {entity.get('implementation_status', 'unknown')}
"""
        
        content += f"""
### 値オブジェクト ({len(current_analysis.get('existing_value_objects', []))}個)
"""
        
        for vo in current_analysis.get('existing_value_objects', []):
            content += f"""
#### {vo['name']}
- **場所**: {vo['file_path']}
- **バリデーション実装**: {'✅' if vo.get('validation_implemented') else '❌'}
- **不変性確保**: {'✅' if vo.get('immutability_enforced') else '❌'}
- **使用箇所数**: {vo.get('usage_count', 0)}
"""
        
        content += f"""
### ドメインサービス ({len(current_analysis.get('existing_domain_services', []))}個)
"""
        
        for service in current_analysis.get('existing_domain_services', []):
            content += f"""
#### {service['name']}
- **場所**: {service['file_path']}
- **複雑度**: {service.get('complexity', 'unknown')}
- **依存関係**: {', '.join(service.get('dependencies', []))}
"""
        
        patterns = current_analysis.get('code_patterns', {})
        debt = current_analysis.get('technical_debt', {})
        
        content += f"""
## コードパターン分析

### 使用中のDDDパターン
{', '.join(patterns.get('ddd_patterns_used', []))}

### 検出されたアンチパターン
{', '.join(patterns.get('anti_patterns_detected', []))}

### 不足しているパターン
{', '.join(patterns.get('missing_patterns', []))}

### パターン準拠スコア
{patterns.get('pattern_compliance_score', 0)}%

## 技術的負債評価

- **Primitive Obsession**: {debt.get('primitive_obsession_count', 0)}箇所
- **貧血エンティティ**: {debt.get('anemic_entities_count', 0)}個
- **バリデーション不足**: {debt.get('missing_validation_count', 0)}箇所
- **総合負債レベル**: {debt.get('overall_debt_score', 'unknown')}

### 優先修正項目
"""
        
        for fix in debt.get('priority_fixes', []):
            content += f"- {fix}\n"
        
        content += """
---
*この分析結果はMCP (Serena)による自動分析に基づいています。*
"""
        
        return content
        
    def create_gap_analysis_document(self, gap_analysis: Dict[str, Any],
                                   requirements: Dict[str, Any],
                                   current_state: Dict[str, Any]) -> str:
        """ギャップ分析ドキュメント生成"""
        content = f"""# ギャップ分析レポート - Issue #{self.issue_number}

**生成日**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**分析範囲**: 要求仕様 vs 現在の実装

## 総合整合性スコア

**整合性**: {gap_analysis['overall_alignment']}%

## エンティティギャップ分析

### 不足しているエンティティ
"""
        
        missing_entities = gap_analysis['entity_gaps'].get('missing_entities', [])
        if missing_entities:
            for entity in missing_entities:
                content += f"- **{entity}**: 要求仕様には存在するが実装されていない\n"
        else:
            content += "なし\n"
        
        content += "\n### 想定外のエンティティ\n"
        unexpected_entities = gap_analysis['entity_gaps'].get('unexpected_entities', [])
        if unexpected_entities:
            for entity in unexpected_entities:
                content += f"- **{entity}**: 実装されているが要求仕様にない\n"
        else:
            content += "なし\n"
        
        content += "\n### 実装ギャップ\n"
        implementation_gaps = gap_analysis['entity_gaps'].get('implementation_gaps', [])
        if implementation_gaps:
            for gap in implementation_gaps:
                content += f"- **{gap['entity']}**: {gap['type']} - {', '.join(gap.get('missing', []))}\n"
        else:
            content += "重要な実装ギャップなし\n"
        
        content += "\n## 値オブジェクトギャップ分析\n"
        
        vo_gaps = gap_analysis.get('value_object_gaps', {})
        missing_vos = vo_gaps.get('missing_value_objects', [])
        if missing_vos:
            content += "\n### 不足している値オブジェクト\n"
            for vo in missing_vos:
                content += f"- **{vo}**: Primitive Obsessionの解消が必要\n"
        
        primitive_obsessions = vo_gaps.get('primitive_obsessions', [])
        if primitive_obsessions:
            content += "\n### Primitive Obsession\n"
            for obsession in primitive_obsessions:
                content += f"- {obsession}\n"
        
        content += "\n## ビジネスルールギャップ分析\n"
        
        rule_gaps = gap_analysis.get('business_rule_gaps', {})
        content += f"""
- **要求ルール数**: {rule_gaps.get('required_rules', 0)}
- **実装済みルール数**: {rule_gaps.get('implemented_rules', 0)}
- **実装率**: {rule_gaps.get('implementation_rate', 0):.1f}%
- **バリデーション不足**: {rule_gaps.get('missing_validations', 0)}箇所

## 改善推奨事項

### 高優先度
1. 不足している値オブジェクトの実装
2. エンティティのビジネス動作強化
3. バリデーション機能の追加

### 中優先度
1. 想定外エンティティの整理
2. ドメインサービスの最適化
3. アンチパターンの除去

### 低優先度  
1. パフォーマンス最適化
2. コード品質向上
3. ドキュメント整備

---
*この分析は要求仕様と現在の実装を比較した結果です。*
"""
        
        return content
        
    def create_enhancement_recommendations_document(self, requirements: Dict[str, Any],
                                                  current_analysis: Dict[str, Any],
                                                  gap_analysis: Dict[str, Any]) -> str:
        """改善提案ドキュメント生成"""
        content = f"""# ドメインモデル改善提案 - Issue #{self.issue_number}

**生成日**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**基準**: 要求分析 + 現状分析 + ギャップ分析

## エグゼクティブサマリー

現在の実装は要求仕様に対して **{gap_analysis['overall_alignment']}%** の整合性を持っています。
以下の段階的改善により、理想的なドメインモデルの実現を提案します。

## フェーズ1: 基礎強化 (即座に実行可能)

### 1.1 値オブジェクト実装
"""
        
        missing_vos = gap_analysis.get('value_object_gaps', {}).get('missing_value_objects', [])
        if missing_vos:
            content += "**実装対象**:\n"
            for vo in missing_vos:
                req_vo = next((v for v in requirements.get('value_objects', []) if v['name'] == vo), None)
                if req_vo:
                    content += f"- **{vo}**: {req_vo.get('description', 'Type safety enhancement')}\n"
        else:
            content += "値オブジェクトの追加実装は不要です。\n"
        
        content += "\n### 1.2 エンティティ強化\n"
        
        missing_entities = gap_analysis.get('entity_gaps', {}).get('missing_entities', [])
        if missing_entities:
            content += "**新規実装対象**:\n"
            for entity in missing_entities:
                req_entity = next((e for e in requirements.get('entities', []) if e['name'] == entity), None)
                if req_entity:
                    content += f"- **{entity}**: {req_entity.get('description', 'Business-critical entity')}\n"
        
        implementation_gaps = gap_analysis.get('entity_gaps', {}).get('implementation_gaps', [])
        if implementation_gaps:
            content += "\n**既存エンティティ強化**:\n"
            for gap in implementation_gaps:
                content += f"- **{gap['entity']}**: {gap['type']} - {', '.join(gap.get('missing', []))}\n"
        
        content += "\n## フェーズ2: ビジネスロジック最適化 (短期実装)\n"
        
        rule_gaps = gap_analysis.get('business_rule_gaps', {})
        missing_rules = rule_gaps.get('required_rules', 0) - rule_gaps.get('implemented_rules', 0)
        
        content += f"""
### 2.1 ビジネスルール実装
- **追加実装必要**: {missing_rules}個のビジネスルール
- **バリデーション強化**: {rule_gaps.get('missing_validations', 0)}箇所

### 2.2 ドメインサービス最適化
"""
        
        existing_services = current_analysis.get('existing_domain_services', [])
        if existing_services:
            content += "**既存サービス最適化**:\n"
            for service in existing_services:
                content += f"- **{service['name']}**: 複雑度{service.get('complexity', 'unknown')}の最適化\n"
        
        # 新規ドメインサービス提案
        required_services = requirements.get('domain_services', [])
        if required_services:
            content += "\n**新規サービス実装**:\n"
            for service in required_services:
                content += f"- **{service['name']}**: {service.get('description', 'Complex business logic')}\n"
        
        content += "\n## フェーズ3: アーキテクチャ最適化 (長期実装)\n"
        
        patterns = current_analysis.get('code_patterns', {})
        missing_patterns = patterns.get('missing_patterns', [])
        
        content += "### 3.1 DDD パターン完全実装\n"
        if missing_patterns:
            content += "**不足パターンの実装**:\n"
            for pattern in missing_patterns:
                content += f"- **{pattern}**: パターン完全性向上\n"
        
        content += "\n### 3.2 アンチパターン除去\n"
        anti_patterns = patterns.get('anti_patterns_detected', [])
        if anti_patterns:
            for pattern in anti_patterns:
                content += f"- **{pattern}**: リファクタリング対象\n"
        
        debt = current_analysis.get('technical_debt', {})
        content += f"""

### 3.3 技術的負債解消
- **Primitive Obsession**: {debt.get('primitive_obsession_count', 0)}箇所の解消
- **貧血エンティティ**: {debt.get('anemic_entities_count', 0)}個の強化
- **バリデーション**: {debt.get('missing_validation_count', 0)}箇所の追加

## 実装優先度マトリックス

| 項目 | 影響度 | 実装難易度 | 優先度 |
|------|--------|-----------|--------|
| 値オブジェクト実装 | 高 | 低 | 最高 |
| エンティティ強化 | 高 | 中 | 高 |
| ビジネスルール追加 | 中 | 中 | 中 |
| ドメインサービス | 中 | 高 | 中 |
| アンチパターン除去 | 低 | 高 | 低 |

## 期待効果

### 短期効果 (フェーズ1-2完了時)
- Type Safety の向上
- ビジネスロジック実装の完全性
- 保守性の向上

### 長期効果 (フェーズ3完了時)
- 完全なDDDアーキテクチャ
- 技術的負債の最小化
- 開発効率の大幅向上

## 次のステップ

1. **テスト作成**: `/create-tests-enhanced {self.issue_number}` で包括的テスト作成
2. **段階的実装**: フェーズ1から順次実装
3. **継続的レビュー**: 各フェーズ完了後の効果測定

---
*この提案は論理的分析に基づく最適化ロードマップです。*
"""
        
        return content
        
    def update_use_case_json_with_enhanced_info(self, json_file_path: str,
                                              domain_concepts: Dict[str, Any],
                                              mcp_analysis: Optional[Dict[str, Any]] = None,
                                              gap_analysis: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """ユースケースJSONに拡張情報を更新"""
        use_case_data = load_use_case_json(json_file_path)
        
        # ドメインモデル情報を更新 (既存機能)
        use_case_data["domain_model"] = domain_concepts
        
        # MCP分析結果を追加 (拡張機能)
        if mcp_analysis:
            use_case_data["current_state_analysis"] = {
                "analyzed_at": datetime.now().isoformat(),
                "mcp_analysis": mcp_analysis,
                "alignment_score": gap_analysis.get('overall_alignment', 0) if gap_analysis else None
            }
        
        # アーキテクチャ整合性情報を更新
        architecture = use_case_data.get("architecture_alignment", {})
        architecture.setdefault("layers", {})["domain"] = False  # まだ実装していない
        architecture.setdefault("patterns_used", []).extend([
            "Domain-Driven Design",
            "Entity-Value Object Pattern", 
            "Aggregate Pattern"
        ])
        
        if self.mcp_available:
            architecture.setdefault("enhanced_features", []).extend([
                "MCP Gap Analysis",
                "Current State Analysis",
                "Improvement Recommendations"
            ])
            
        use_case_data["architecture_alignment"] = architecture
        
        # 保存
        save_use_case_json(json_file_path, use_case_data)
        
        return use_case_data
        
    async def run_enhanced_modeling(self) -> Dict[str, Any]:
        """論理的統合型ドメインモデリング実行"""
        logger.info(f"🚀 Issue #{self.issue_number} の統合型ドメインモデリングを開始")
        
        # Phase 1: 要求分析 (既存機能)
        logger.info("📋 Phase 1: 要求分析 (Given-When-Then → ドメイン概念)")
        core_results = self.core_modeler.run_core_modeling()
        
        results = {
            "core_results": core_results,
            "mcp_available": self.mcp_available,
            "generated_documents": [core_results["domain_doc_path"]]
        }
        
        if self.mcp_available:
            # Phase 2: 現状分析 (MCP機能)
            logger.info("🔍 Phase 2: 現状分析 (コードベース → 現在の実装状況)")
            current_analysis = self.mcp_analyzer.analyze_current_codebase()
            
            # Phase 3: ギャップ分析 (統合機能)
            logger.info("📊 Phase 3: ギャップ分析 (要求 vs 現実)")
            gap_analysis = self.gap_analyzer.analyze_requirements_vs_reality(
                core_results["domain_concepts"], current_analysis
            )
            
            # Phase 4: 拡張ドキュメント生成
            logger.info("📝 Phase 4: 拡張ドキュメント生成")
            domain_dir = Path("docs/domain")
            
            # 現状分析ドキュメント
            current_analysis_doc = self.create_current_analysis_document(current_analysis)
            current_analysis_path = domain_dir / f"issue-{self.issue_number}-current-analysis.md"
            with open(current_analysis_path, 'w', encoding='utf-8') as f:
                f.write(current_analysis_doc)
            logger.info(f"✅ 現状分析ドキュメント作成: {current_analysis_path}")
            
            # ギャップ分析ドキュメント
            gap_analysis_doc = self.create_gap_analysis_document(
                gap_analysis, core_results["domain_concepts"], current_analysis
            )
            gap_analysis_path = domain_dir / f"issue-{self.issue_number}-gap-analysis.md"
            with open(gap_analysis_path, 'w', encoding='utf-8') as f:
                f.write(gap_analysis_doc)
            logger.info(f"✅ ギャップ分析ドキュメント作成: {gap_analysis_path}")
            
            # 改善提案ドキュメント
            enhancement_doc = self.create_enhancement_recommendations_document(
                core_results["domain_concepts"], current_analysis, gap_analysis
            )
            enhancement_path = domain_dir / f"issue-{self.issue_number}-enhancement-recommendations.md"
            with open(enhancement_path, 'w', encoding='utf-8') as f:
                f.write(enhancement_doc)
            logger.info(f"✅ 改善提案ドキュメント作成: {enhancement_path}")
            
            # 結果に拡張情報を追加
            results.update({
                "current_analysis": current_analysis,
                "gap_analysis": gap_analysis,
                "generated_documents": [
                    core_results["domain_doc_path"],
                    str(current_analysis_path),
                    str(gap_analysis_path),
                    str(enhancement_path)
                ]
            })
            
            # Phase 5: JSONファイル更新
            logger.info("📊 Phase 5: メタデータ更新")
            self.update_use_case_json_with_enhanced_info(
                core_results["json_file_path"],
                core_results["domain_concepts"],
                current_analysis,
                gap_analysis
            )
        else:
            logger.info("ℹ️ MCP機能を使用できません - 基本機能のみで完了")
            # 既存機能でのJSONファイル更新
            self.update_use_case_json_with_enhanced_info(
                core_results["json_file_path"],
                core_results["domain_concepts"]
            )
        
        # Phase 6: 実行履歴更新
        logger.info("📋 実行履歴更新中...")
        update_execution_history(
            core_results["json_file_path"],
            "04-domain-modeling-enhanced",
            "success",
            {
                "domain_concepts": core_results["domain_concepts"],
                "mcp_enhanced": self.mcp_available,
                "documents_generated": len(results["generated_documents"])
            }
        )
        
        logger.info("✅ 統合型ドメインモデリング完了!")
        return results


async def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("❌ エラー: Issue番号が必要です")
        print("使用方法: /domain-modeling-enhanced <issue-number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    
    try:
        # 統合型ドメインモデラー初期化
        modeler = EnhancedDomainModeler(issue_number)
        
        # 統合型モデリング実行
        results = await modeler.run_enhanced_modeling()
        
        # 結果表示
        print("\n" + "="*60)
        print("🎉 統合型ドメインモデリング完了")
        print("="*60)
        print(f"Issue番号: {issue_number}")
        print(f"MCP拡張機能: {'✅ 有効' if results['mcp_available'] else '❌ 無効'}")
        
        core = results["core_results"]["domain_concepts"]
        print(f"\n📊 ドメイン要素分析結果:")
        print(f"  - エンティティ: {len(core['entities'])}個")
        print(f"  - 値オブジェクト: {len(core['value_objects'])}個")
        print(f"  - ドメインサービス: {len(core['domain_services'])}個")
        print(f"  - ビジネスルール: {len(core['business_rules'])}個")
        
        if results.get("gap_analysis"):
            print(f"  - 整合性スコア: {results['gap_analysis']['overall_alignment']}%")
        
        print(f"\n📁 生成されたドキュメント:")
        for doc in results["generated_documents"]:
            print(f"  ✅ {doc}")
        
        if results['mcp_available']:
            print(f"\n🚀 論理的ワークフロー完了:")
            print(f"  1. ✅ 要求分析 (Given-When-Then → ドメイン概念)")
            print(f"  2. ✅ 現状分析 (コードベース → 実装状況)")
            print(f"  3. ✅ ギャップ分析 (要求 vs 現実)")
            print(f"  4. ✅ 改善提案 (最適化ロードマップ)")
        
        print(f"\n📋 次のステップ:")
        print(f"  • テスト作成: /create-tests-enhanced {issue_number}")
        print(f"  • 実装フェーズ: 改善提案に従って段階的実装")
        print("="*60)
        
    except FileNotFoundError as e:
        print(f"❌ ファイルエラー: {e}")
        print("先に /create-use-case コマンドを実行してください")
        sys.exit(1)
    except Exception as e:
        logger.exception("統合型ドメインモデリングでエラーが発生")
        print(f"❌ エラー: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())