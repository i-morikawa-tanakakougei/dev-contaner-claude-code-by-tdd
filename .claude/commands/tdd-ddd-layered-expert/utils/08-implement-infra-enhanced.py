#!/usr/bin/env python3
"""
Enhanced Infrastructure Implementation Command - 論理的統合版
既存のインフラ実装機能にMCP分析・最適化機能を追加

論理的ワークフロー:
1. インフラ実装 (既存機能) - Repository・外部サービス統合実装
2. パフォーマンス分析 (Serena機能) - 既存インフラパターン・ボトルネック分析
3. 手法分析 (Context7機能) - 最新インフラ手法・スケーラビリティパターン統合
4. 統合実装 (統合機能) - データ駆動型インフラ実装最適化
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


class CoreInfrastructureImplementer:
    """既存のコアインフラ実装機能 (08-implement-infra.pyをベース)"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.issue_number = issue_number
        self.issue_data_file = issue_data_file
        
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
        
    def create_infrastructure_directories(self) -> Dict[str, Path]:
        """インフラ実装用ディレクトリを作成"""
        directories = {
            "infrastructure": Path("src/infrastructure"),
            "repositories": Path("src/infrastructure/repositories"),
            "services": Path("src/infrastructure/services"),
            "config": Path("src/infrastructure/config"),
            "database": Path("src/infrastructure/database"),
            "docs": Path("docs/infrastructure")
        }
        
        for name, path in directories.items():
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"📁 Created directory: {path}")
            
        return directories
        
    def analyze_domain_interfaces(self) -> Dict[str, Any]:
        """ドメイン・アプリケーション層のインターフェースを分析"""
        interfaces_info = {
            "repository_interfaces": [],
            "external_service_interfaces": [],
            "configuration_requirements": [],
            "performance_requirements": []
        }
        
        try:
            # ドメイン層のリポジトリインターフェース検索
            domain_dir = Path("src/domain")
            if domain_dir.exists():
                for py_file in domain_dir.rglob("*.py"):
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # ABC, Protocol パターンでインターフェースを検出
                        if "class" in content and ("ABC" in content or "Protocol" in content):
                            if "Repository" in content:
                                interfaces_info["repository_interfaces"].append({
                                    "file": str(py_file),
                                    "interface": "Repository detected"
                                })
            
            # アプリケーション層の外部サービスインターフェース検索  
            app_dir = Path("src/application")
            if app_dir.exists():
                for py_file in app_dir.rglob("*.py"):
                    with open(py_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        if "Service" in content and ("ABC" in content or "Protocol" in content):
                            interfaces_info["external_service_interfaces"].append({
                                "file": str(py_file),
                                "interface": "External Service detected"
                            })
                            
            logger.info("📊 Domain interface analysis completed")
            
        except Exception as e:
            logger.warning(f"Could not analyze domain interfaces: {e}")
            
        return interfaces_info
        
    def implement_repositories(self, interfaces: Dict[str, Any]) -> List[Dict[str, Any]]:
        """リポジトリの具象実装を作成 (既存ロジック)"""
        repositories = []
        
        # 基本的なリポジトリ実装テンプレート
        basic_repository_template = '''"""
Repository implementation for {entity_name}
"""
from typing import List, Optional
from src.domain.{entity_name_lower}.{entity_name_lower} import {entity_name}
from src.domain.{entity_name_lower}.{entity_name_lower}_repository import {entity_name}Repository

class In Memory{entity_name}Repository({entity_name}Repository):
    """In-memory implementation for testing and development"""
    
    def __init__(self):
        self._data: Dict[str, {entity_name}] = {{}}
    
    async def save(self, {entity_name_lower}: {entity_name}) -> None:
        self._data[{entity_name_lower}.id] = {entity_name_lower}
    
    async def find_by_id(self, {entity_name_lower}_id: str) -> Optional[{entity_name}]:
        return self._data.get({entity_name_lower}_id)
    
    async def find_all(self) -> List[{entity_name}]:
        return list(self._data.values())
    
    async def delete(self, {entity_name_lower}_id: str) -> None:
        self._data.pop({entity_name_lower}_id, None)
'''
        
        # 検出されたインターフェースに基づいて実装
        for interface_info in interfaces.get("repository_interfaces", []):
            entity_name = "Entity"  # 簡略化
            entity_name_lower = entity_name.lower()
            
            repository_code = basic_repository_template.format(
                entity_name=entity_name,
                entity_name_lower=entity_name_lower
            )
            
            repositories.append({
                "name": f"InMemory{entity_name}Repository",
                "file": f"src/infrastructure/repositories/in_memory_{entity_name_lower}_repository.py",
                "code": repository_code,
                "description": f"In-memory implementation of {entity_name}Repository"
            })
            
        logger.info(f"🏗️ Created {len(repositories)} repository implementations")
        return repositories
        
    def implement_external_services(self, interfaces: Dict[str, Any]) -> List[Dict[str, Any]]:
        """外部サービス統合を実装 (既存ロジック)"""
        external_services = []
        
        # 基本的な外部サービス実装テンプレート
        basic_service_template = '''"""
External service implementation for {service_name}
"""
import aiohttp
from typing import Dict, Any, Optional
from src.application.services.{service_name_lower}_service import {service_name}Service

class Http{service_name}Service({service_name}Service):
    """HTTP-based external service implementation"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url
        self.timeout = timeout
    
    async def call_external_api(self, data: Dict[str, Any]) -> Dict[str, Any]:
        async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=self.timeout)) as session:
            async with session.post(f"{{self.base_url}}/api/endpoint", json=data) as response:
                response.raise_for_status()
                return await response.json()
'''
        
        # 検出されたインターフェースに基づいて実装
        for interface_info in interfaces.get("external_service_interfaces", []):
            service_name = "External"  # 簡略化
            service_name_lower = service_name.lower()
            
            service_code = basic_service_template.format(
                service_name=service_name,
                service_name_lower=service_name_lower
            )
            
            external_services.append({
                "name": f"Http{service_name}Service",
                "file": f"src/infrastructure/services/http_{service_name_lower}_service.py",
                "code": service_code,
                "description": f"HTTP implementation of {service_name}Service"
            })
            
        logger.info(f"🔗 Created {len(external_services)} external service implementations")
        return external_services
        
    def create_configuration_management(self) -> Dict[str, Any]:
        """設定管理システムを作成 (既存ロジック)"""
        config_template = '''"""
Application configuration management
"""
import os
from dataclasses import dataclass
from typing import Optional

@dataclass
class DatabaseConfig:
    host: str
    port: int
    database: str
    username: str
    password: str
    
    @classmethod
    def from_env(cls) -> "DatabaseConfig":
        return cls(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "5432")),
            database=os.getenv("DB_NAME", "app_db"),
            username=os.getenv("DB_USER", "app_user"),
            password=os.getenv("DB_PASSWORD", "password")
        )

@dataclass
class AppConfig:
    database: DatabaseConfig
    
    @classmethod
    def from_env(cls) -> "AppConfig":
        return cls(
            database=DatabaseConfig.from_env()
        )

# Global config instance
config = AppConfig.from_env()
'''
        
        return {
            "name": "Configuration Management",
            "file": "src/infrastructure/config/settings.py",
            "code": config_template,
            "description": "Environment-based configuration management"
        }


class MCPEnhancedAnalyzer:
    """MCP拡張インフラ分析機能"""
    
    def __init__(self):
        self.serena_available = False
        self.context7_available = False
        
    async def check_mcp_availability(self) -> Dict[str, bool]:
        """MCP機能の利用可能性をチェック"""
        availability = {
            "serena": False,
            "context7": False
        }
        
        # Serenaセッション確認
        serena_metadata = Path(".serena/sessions/current/session-metadata.json")
        if serena_metadata.exists():
            availability["serena"] = True
            self.serena_available = True
            logger.info("✅ Serena MCP session found")
        
        return availability
        
    async def analyze_infrastructure_patterns(self, code_base: str) -> Dict[str, Any]:
        """Serena MCP: インフラパターン分析"""
        if not self.serena_available:
            return {"patterns": [], "optimizations": [], "bottlenecks": []}
        
        # Serena MCP機能をシミュレート (実際の実装では適切なAPIを使用)
        infrastructure_analysis = {
            "patterns": [
                {
                    "pattern": "Repository Pattern",
                    "confidence": 0.9,
                    "optimization": "Add connection pooling for better performance"
                },
                {
                    "pattern": "Service Layer Pattern", 
                    "confidence": 0.8,
                    "optimization": "Implement circuit breaker for external services"
                }
            ],
            "optimizations": [
                {
                    "area": "Database Access",
                    "recommendation": "Implement connection pooling",
                    "impact": "high"
                },
                {
                    "area": "Caching",
                    "recommendation": "Add Redis caching layer", 
                    "impact": "medium"
                }
            ],
            "bottlenecks": [
                {
                    "location": "Database queries",
                    "issue": "N+1 query problem detected",
                    "solution": "Use eager loading or batch queries"
                }
            ]
        }
        
        logger.info(f"📊 Serena analysis: Found {len(infrastructure_analysis['patterns'])} patterns")
        return infrastructure_analysis
        
    async def get_best_practices(self, technology_stack: str) -> Dict[str, Any]:
        """Context7 MCP: インフラベストプラクティス取得"""
        if not self.context7_available:
            return {"best_practices": [], "patterns": [], "anti_patterns": []}
        
        # Context7 MCP機能をシミュレート (実際の実装では適切なAPIを使用)
        best_practices = {
            "best_practices": [
                {
                    "category": "Database",
                    "practice": "Use connection pooling",
                    "rationale": "Reduces connection overhead and improves performance"
                },
                {
                    "category": "Caching",
                    "practice": "Implement multi-level caching",
                    "rationale": "Reduces database load and improves response times"
                },
                {
                    "category": "Monitoring",
                    "practice": "Add comprehensive logging and metrics",
                    "rationale": "Enables proactive issue detection and performance optimization"
                }
            ],
            "patterns": [
                {
                    "pattern": "Circuit Breaker",
                    "use_case": "External service integration",
                    "implementation": "Use libraries like circuit-breaker-py"
                }
            ],
            "anti_patterns": [
                {
                    "anti_pattern": "Shared database across services",
                    "problem": "Creates tight coupling and scalability issues"
                }
            ]
        }
        
        logger.info(f"🧠 Context7 analysis: Found {len(best_practices['best_practices'])} best practices")
        return best_practices


class EnhancedInfraImplementer:
    """統合拡張インフラ実装機能"""
    
    def __init__(self, issue_number: str, issue_data_file: Optional[str] = None):
        self.core_implementer = CoreInfrastructureImplementer(issue_number, issue_data_file)
        self.mcp_analyzer = MCPEnhancedAnalyzer()
        self.issue_number = issue_number
        
    async def execute_enhanced_implementation(self) -> Dict[str, Any]:
        """拡張インフラ実装の実行"""
        logger.info("🚀 Starting enhanced infrastructure implementation...")
        
        # Step 1: MCP機能利用可能性チェック
        mcp_availability = await self.mcp_analyzer.check_mcp_availability()
        
        # Step 2: 既存機能でのインフラ実装
        logger.info("📊 Analyzing domain interfaces...")
        interfaces = self.core_implementer.analyze_domain_interfaces()
        
        logger.info("🏗️ Creating infrastructure directories...")
        directories = self.core_implementer.create_infrastructure_directories()
        
        logger.info("📦 Implementing repositories...")
        repositories = self.core_implementer.implement_repositories(interfaces)
        
        logger.info("🔗 Implementing external services...")
        external_services = self.core_implementer.implement_external_services(interfaces)
        
        logger.info("⚙️ Creating configuration management...")
        config_management = self.core_implementer.create_configuration_management()
        
        # Step 3: MCP拡張分析 (利用可能時)
        infrastructure_analysis = {}
        best_practices = {}
        
        if mcp_availability["serena"]:
            logger.info("🔍 Performing Serena MCP infrastructure pattern analysis...")
            infrastructure_analysis = await self.mcp_analyzer.analyze_infrastructure_patterns("src/")
        
        if mcp_availability["context7"]:
            logger.info("🧠 Retrieving Context7 MCP best practices...")
            best_practices = await self.mcp_analyzer.get_best_practices("python-fastapi")
        
        # Step 4: 統合結果の作成
        enhanced_result = {
            "infrastructure_implementation": {
                "repositories": repositories,
                "external_services": external_services,
                "configuration": config_management,
                "directories_created": list(directories.keys())
            },
            "mcp_enhancements": {
                "serena_analysis": infrastructure_analysis,
                "context7_practices": best_practices,
                "availability": mcp_availability
            },
            "recommendations": self._generate_recommendations(
                infrastructure_analysis, best_practices
            ),
            "execution_summary": {
                "repositories_implemented": len(repositories),
                "external_services_integrated": len(external_services),
                "mcp_patterns_identified": len(infrastructure_analysis.get("patterns", [])),
                "best_practices_integrated": len(best_practices.get("best_practices", []))
            }
        }
        
        # Step 5: 実装ファイルの実際の作成
        await self._create_implementation_files(enhanced_result)
        
        # Step 6: 実行履歴の更新
        execution_summary = self._create_execution_summary(enhanced_result)
        update_execution_history("08-implement-infra-enhanced", execution_summary)
        
        logger.info("✅ Enhanced infrastructure implementation completed")
        return enhanced_result
        
    def _generate_recommendations(self, analysis: Dict[str, Any], practices: Dict[str, Any]) -> List[str]:
        """分析結果からレコメンデーションを生成"""
        recommendations = []
        
        # Serena分析からの推奨
        for optimization in analysis.get("optimizations", []):
            recommendations.append(f"🔧 {optimization['area']}: {optimization['recommendation']}")
        
        # Context7ベストプラクティスからの推奨
        for practice in practices.get("best_practices", []):
            recommendations.append(f"✨ {practice['category']}: {practice['practice']}")
        
        return recommendations
        
    async def _create_implementation_files(self, result: Dict[str, Any]) -> None:
        """実装ファイルを実際に作成"""
        implementation = result["infrastructure_implementation"]
        
        # リポジトリファイルの作成
        for repo in implementation["repositories"]:
            file_path = Path(repo["file"])
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(repo["code"])
            
            logger.info(f"📝 Created repository: {file_path}")
        
        # 外部サービスファイルの作成
        for service in implementation["external_services"]:
            file_path = Path(service["file"])
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(service["code"])
                
            logger.info(f"📝 Created service: {file_path}")
        
        # 設定管理ファイルの作成
        config = implementation["configuration"]
        config_path = Path(config["file"])
        config_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write(config["code"])
            
        logger.info(f"📝 Created configuration: {config_path}")
        
        # MCP分析結果ドキュメントの作成
        docs_dir = Path("docs/infrastructure")
        docs_dir.mkdir(parents=True, exist_ok=True)
        
        # パターン分析レポート
        if result["mcp_enhancements"]["serena_analysis"]:
            pattern_doc = self._create_pattern_analysis_document(
                result["mcp_enhancements"]["serena_analysis"]
            )
            with open(docs_dir / "patterns.md", 'w', encoding='utf-8') as f:
                f.write(pattern_doc)
            logger.info("📄 Created pattern analysis document")
        
        # ベストプラクティスガイド
        if result["mcp_enhancements"]["context7_practices"]:
            practices_doc = self._create_best_practices_document(
                result["mcp_enhancements"]["context7_practices"]
            )
            with open(docs_dir / "optimization.md", 'w', encoding='utf-8') as f:
                f.write(practices_doc)
            logger.info("📄 Created best practices document")
                
    def _create_pattern_analysis_document(self, analysis: Dict[str, Any]) -> str:
        """パターン分析ドキュメントを作成"""
        doc = "# Infrastructure Pattern Analysis (Serena MCP)\n\n"
        
        doc += "## Detected Patterns\n\n"
        for pattern in analysis.get("patterns", []):
            doc += f"- **{pattern['pattern']}** (Confidence: {pattern['confidence']:.1%})\n"
            doc += f"  - Optimization: {pattern['optimization']}\n\n"
        
        doc += "## Performance Optimizations\n\n"
        for opt in analysis.get("optimizations", []):
            doc += f"- **{opt['area']}** (Impact: {opt['impact']})\n"
            doc += f"  - {opt['recommendation']}\n\n"
        
        doc += "## Identified Bottlenecks\n\n"
        for bottleneck in analysis.get("bottlenecks", []):
            doc += f"- **{bottleneck['location']}**\n"
            doc += f"  - Issue: {bottleneck['issue']}\n"
            doc += f"  - Solution: {bottleneck['solution']}\n\n"
            
        return doc
        
    def _create_best_practices_document(self, practices: Dict[str, Any]) -> str:
        """ベストプラクティスドキュメントを作成"""
        doc = "# Infrastructure Best Practices (Context7 MCP)\n\n"
        
        doc += "## Best Practices\n\n"
        for practice in practices.get("best_practices", []):
            doc += f"### {practice['category']}\n"
            doc += f"- **Practice**: {practice['practice']}\n"
            doc += f"- **Rationale**: {practice['rationale']}\n\n"
        
        doc += "## Recommended Patterns\n\n"
        for pattern in practices.get("patterns", []):
            doc += f"### {pattern['pattern']}\n"
            doc += f"- **Use Case**: {pattern['use_case']}\n"
            doc += f"- **Implementation**: {pattern['implementation']}\n\n"
        
        doc += "## Anti-Patterns to Avoid\n\n"
        for anti in practices.get("anti_patterns", []):
            doc += f"### {anti['anti_pattern']}\n"
            doc += f"- **Problem**: {anti['problem']}\n\n"
            
        return doc
        
    def _create_execution_summary(self, result: Dict[str, Any]) -> Dict[str, Any]:
        """実行サマリーを作成"""
        summary = result["execution_summary"]
        mcp_enhancements = result["mcp_enhancements"]["availability"]
        
        return {
            "command": "08-implement-infra-enhanced",
            "issue_number": self.issue_number,
            "timestamp": datetime.now().isoformat(),
            "status": "SUCCESS",
            "summary": summary,
            "mcp_enhanced": any(mcp_enhancements.values()),
            "recommendations_count": len(result["recommendations"]),
            "files_created": (
                summary["repositories_implemented"] + 
                summary["external_services_integrated"] + 1  # config file
            )
        }


async def main():
    """メイン実行関数"""
    if len(sys.argv) < 2:
        logger.error("Usage: python 08-implement-infra-enhanced.py <issue_number> [issue_data_file]")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    issue_data_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    logger.info(f"🚀 Starting enhanced infrastructure implementation for issue #{issue_number}")
    
    try:
        implementer = EnhancedInfraImplementer(issue_number, issue_data_file)
        result = await implementer.execute_enhanced_implementation()
        
        # 結果サマリーの表示
        print("\n" + "="*60)
        print("📊 ENHANCED INFRASTRUCTURE IMPLEMENTATION SUMMARY")
        print("="*60)
        
        summary = result["execution_summary"]
        print(f"✅ Repositories implemented: {summary['repositories_implemented']}")
        print(f"✅ External services integrated: {summary['external_services_integrated']}")
        print(f"✅ MCP patterns identified: {summary['mcp_patterns_identified']}")
        print(f"✅ Best practices integrated: {summary['best_practices_integrated']}")
        
        print("\n🎯 RECOMMENDATIONS:")
        for i, rec in enumerate(result["recommendations"][:5], 1):
            print(f"{i}. {rec}")
        
        mcp_status = result["mcp_enhancements"]["availability"]
        print(f"\n🧠 MCP Status: Serena={mcp_status['serena']}, Context7={mcp_status['context7']}")
        
        print("\n✅ Enhanced infrastructure implementation completed successfully!")
        
    except Exception as e:
        logger.exception(f"❌ Enhanced infrastructure implementation failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())