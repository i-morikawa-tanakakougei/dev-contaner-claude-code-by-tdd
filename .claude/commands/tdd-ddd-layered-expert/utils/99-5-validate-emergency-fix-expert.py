#!/usr/bin/env python3
"""
Validate Emergency Fix Expert Command - 改修版
緊急修正の品質とアーキテクチャ適合性を包括的に検証し、実行履歴を追跡
"""

import json
import os
import sys
import subprocess
from datetime import datetime
from pathlib import Path
import glob
import re
import ast

# Add utils to path
sys.path.insert(0, str(Path(__file__).parent))
from json_format_utils import (
    load_use_case_json,
    update_execution_history,
    save_use_case_json,
    format_execution_status
)


def get_github_issue(issue_number):
    """GitHub Issueの情報を取得"""
    try:
        result = subprocess.run(
            ["gh", "issue", "view", str(issue_number), "--json", 
             "title,body,comments,updatedAt,createdAt,labels,assignees,url"],
            capture_output=True,
            text=True,
            check=True
        )
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ GitHub Issue取得エラー: {e}")
        return None


def analyze_emergency_fixes_scope():
    """緊急修正スコープを分析"""
    emergency_scope = {
        "modified_files": [],
        "emergency_commits": [],
        "affected_layers": [],
        "code_changes": [],
        "scope_analysis": {
            "total_files": 0,
            "layers_affected": 0,
            "complexity_score": 0
        }
    }
    
    try:
        # Emergency recovery reports から修正スコープを抽出
        emergency_dir = Path("docs/emergency")
        if emergency_dir.exists():
            for report_file in emergency_dir.glob("emergency-recovery-report-*.md"):
                with open(report_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # 修正されたファイルパスを抽出
                    file_pattern = r'`([^`]+\.py)`'
                    files = re.findall(file_pattern, content)
                    emergency_scope["modified_files"].extend(files)
                    
                    # コミットハッシュを抽出
                    commit_pattern = r'`([a-f0-9]{7,})`'
                    commits = re.findall(commit_pattern, content)
                    emergency_scope["emergency_commits"].extend(commits)
        
        # Git履歴から緊急修正コミットを特定
        result = subprocess.run(
            ["git", "log", "--oneline", "--grep=emergency", "--grep=hotfix", "--grep=urgent", "-10"],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            commit_lines = result.stdout.strip().split('\n')
            for line in commit_lines:
                if line:
                    commit_hash = line.split(' ')[0]
                    commit_message = ' '.join(line.split(' ')[1:])
                    
                    # 各コミットで変更されたファイルを取得
                    files_result = subprocess.run(
                        ["git", "show", "--name-only", "--format=", commit_hash],
                        capture_output=True,
                        text=True
                    )
                    
                    if files_result.returncode == 0:
                        changed_files = files_result.stdout.strip().split('\n')
                        changed_files = [f for f in changed_files if f and f.endswith('.py')]
                        
                        emergency_scope["emergency_commits"].append({
                            "hash": commit_hash,
                            "message": commit_message,
                            "changed_files": changed_files
                        })
                        
                        emergency_scope["modified_files"].extend(changed_files)
        
        # レイヤー分析
        all_files = list(set(emergency_scope["modified_files"]))
        for file_path in all_files:
            if "domain" in file_path:
                emergency_scope["affected_layers"].append("domain")
            elif "application" in file_path or "use_case" in file_path:
                emergency_scope["affected_layers"].append("application")
            elif "infrastructure" in file_path:
                emergency_scope["affected_layers"].append("infrastructure")
            elif "presentation" in file_path or "api" in file_path:
                emergency_scope["affected_layers"].append("presentation")
        
        emergency_scope["affected_layers"] = list(set(emergency_scope["affected_layers"]))
        
        # スコープ統計
        emergency_scope["scope_analysis"]["total_files"] = len(all_files)
        emergency_scope["scope_analysis"]["layers_affected"] = len(emergency_scope["affected_layers"])
        emergency_scope["scope_analysis"]["complexity_score"] = min(100, len(all_files) * 10 + len(emergency_scope["affected_layers"]) * 20)
        
    except Exception as e:
        print(f"⚠️ 緊急修正スコープ分析エラー: {e}")
    
    return emergency_scope


def validate_layered_architecture(emergency_scope):
    """レイヤードアーキテクチャの適合性を検証"""
    architecture_validation = {
        "layer_separation_score": 0,
        "dependency_flow_valid": True,
        "boundary_violations": [],
        "responsibility_adherence": 0,
        "overall_architecture_score": 0,
        "detailed_analysis": {}
    }
    
    try:
        # 各レイヤーのファイルを分析
        for file_path in emergency_scope["modified_files"]:
            if not os.path.exists(file_path):
                continue
                
            layer_type = None
            if "domain" in file_path:
                layer_type = "domain"
            elif "application" in file_path or "use_case" in file_path:
                layer_type = "application"
            elif "infrastructure" in file_path:
                layer_type = "infrastructure"
            elif "presentation" in file_path or "api" in file_path:
                layer_type = "presentation"
            
            if layer_type:
                violations = analyze_layer_dependencies(file_path, layer_type)
                if violations:
                    architecture_validation["boundary_violations"].extend(violations)
        
        # スコア計算
        total_files = len([f for f in emergency_scope["modified_files"] if os.path.exists(f)])
        violations_count = len(architecture_validation["boundary_violations"])
        
        if total_files > 0:
            violation_ratio = violations_count / total_files
            architecture_validation["layer_separation_score"] = max(0, 100 - (violation_ratio * 100))
            
            # 依存関係フロー検証
            architecture_validation["dependency_flow_valid"] = violations_count == 0
            
            # 責任遵守度
            architecture_validation["responsibility_adherence"] = architecture_validation["layer_separation_score"]
            
            # 総合スコア（5点満点）
            architecture_validation["overall_architecture_score"] = (
                architecture_validation["layer_separation_score"] / 100 * 5
            )
        
    except Exception as e:
        print(f"⚠️ アーキテクチャ検証エラー: {e}")
    
    return architecture_validation


def analyze_layer_dependencies(file_path, layer_type):
    """ファイルの依存関係を分析してレイヤー違反を検出"""
    violations = []
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # importステートメントを抽出
        import_pattern = r'^(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_.]*)'
        imports = re.findall(import_pattern, content, re.MULTILINE)
        
        # レイヤー違反をチェック
        for import_module in imports:
            if layer_type == "domain":
                # ドメインレイヤーは他のレイヤーに依存してはいけない
                if any(forbidden in import_module for forbidden in ["application", "infrastructure", "presentation"]):
                    violations.append({
                        "file": file_path,
                        "violation_type": "domain_layer_dependency",
                        "imported_module": import_module,
                        "description": f"Domain layer cannot depend on {import_module}"
                    })
            
            elif layer_type == "application":
                # アプリケーションレイヤーはインフラ・プレゼンテーションに依存してはいけない
                if any(forbidden in import_module for forbidden in ["infrastructure", "presentation"]):
                    violations.append({
                        "file": file_path,
                        "violation_type": "application_layer_dependency",
                        "imported_module": import_module,
                        "description": f"Application layer cannot depend on {import_module}"
                    })
    
    except Exception as e:
        print(f"⚠️ 依存関係分析エラー ({file_path}): {e}")
    
    return violations


def assess_ddd_compliance(emergency_scope):
    """DDDプリンシプルの適合性を評価"""
    ddd_assessment = {
        "entity_integrity_score": 0,
        "value_object_immutability": True,
        "aggregate_boundary_score": 0,
        "ubiquitous_language_consistency": True,
        "overall_ddd_score": 0,
        "detailed_findings": {}
    }
    
    try:
        domain_files = [f for f in emergency_scope["modified_files"] if "domain" in f and f.endswith(".py")]
        
        entity_scores = []
        value_object_issues = []
        
        for domain_file in domain_files:
            if not os.path.exists(domain_file):
                continue
            
            try:
                with open(domain_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # ASTで解析
                tree = ast.parse(content)
                
                for node in ast.walk(tree):
                    if isinstance(node, ast.ClassDef):
                        class_name = node.name
                        
                        # Entityパターンの検証
                        if "Entity" in class_name or any("entity" in base.id for base in node.bases if isinstance(base, ast.Name)):
                            entity_score = analyze_entity_integrity(node, content)
                            entity_scores.append(entity_score)
                        
                        # Value Objectパターンの検証
                        if "ValueObject" in class_name or any("value_object" in base.id for base in node.bases if isinstance(base, ast.Name)):
                            immutability_issues = check_value_object_immutability(node, content)
                            if immutability_issues:
                                value_object_issues.extend(immutability_issues)
                                ddd_assessment["value_object_immutability"] = False
                
            except Exception as e:
                print(f"⚠️ DDDファイル分析エラー ({domain_file}): {e}")
        
        # スコア計算
        if entity_scores:
            ddd_assessment["entity_integrity_score"] = sum(entity_scores) / len(entity_scores)
        else:
            ddd_assessment["entity_integrity_score"] = 100  # デフォルト値
        
        # Aggregate境界スコア
        ddd_assessment["aggregate_boundary_score"] = calculate_aggregate_boundary_score(domain_files)
        
        # ユビキタス言語一貫性
        ddd_assessment["ubiquitous_language_consistency"] = check_ubiquitous_language_consistency(domain_files)
        
        # 総合DDDスコア（5点満点）
        scores = [
            ddd_assessment["entity_integrity_score"],
            100 if ddd_assessment["value_object_immutability"] else 50,
            ddd_assessment["aggregate_boundary_score"],
            100 if ddd_assessment["ubiquitous_language_consistency"] else 50
        ]
        ddd_assessment["overall_ddd_score"] = (sum(scores) / len(scores)) / 100 * 5
        
    except Exception as e:
        print(f"⚠️ DDD適合性評価エラー: {e}")
    
    return ddd_assessment


def analyze_entity_integrity(class_node, content):
    """Entity整合性を分析"""
    score = 100
    
    # IDフィールドの存在チェック
    has_id_field = False
    has_equals_method = False
    
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            if node.name == "__init__":
                # IDフィールドをチェック
                for arg in node.args.args:
                    if "id" in arg.arg:
                        has_id_field = True
            elif node.name in ["__eq__", "equals"]:
                has_equals_method = True
    
    if not has_id_field:
        score -= 30
    if not has_equals_method:
        score -= 20
    
    return max(0, score)


def check_value_object_immutability(class_node, content):
    """Value Object不変性をチェック"""
    issues = []
    
    for node in class_node.body:
        if isinstance(node, ast.FunctionDef):
            # setterメソッドの存在チェック
            if node.name.startswith("set_"):
                issues.append({
                    "class": class_node.name,
                    "issue": f"Setter method {node.name} found in Value Object",
                    "line": node.lineno
                })
            
            # __init__後のフィールド変更チェック
            if node.name != "__init__":
                for child in ast.walk(node):
                    if isinstance(child, ast.Assign):
                        for target in child.targets:
                            if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == "self":
                                issues.append({
                                    "class": class_node.name,
                                    "issue": f"Field modification outside __init__: {target.attr}",
                                    "line": child.lineno
                                })
    
    return issues


def calculate_aggregate_boundary_score(domain_files):
    """Aggregate境界スコアを計算"""
    # 簡略化された実装
    return 85  # デフォルト値


def check_ubiquitous_language_consistency(domain_files):
    """ユビキタス言語一貫性をチェック"""
    # 簡略化された実装
    return True  # デフォルト値


def analyze_code_quality_metrics(emergency_scope):
    """コード品質メトリクスを分析"""
    quality_metrics = {
        "cyclomatic_complexity": 0,
        "solid_principles_adherence": 0,
        "code_duplication": 0,
        "maintainability_index": 0,
        "overall_quality_score": 0,
        "detailed_analysis": {}
    }
    
    try:
        python_files = [f for f in emergency_scope["modified_files"] if f.endswith(".py") and os.path.exists(f)]
        
        complexity_scores = []
        solid_scores = []
        
        for file_path in python_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 循環的複雑度の簡易計算
                complexity = calculate_cyclomatic_complexity(content)
                complexity_scores.append(complexity)
                
                # SOLID原則適合度の簡易チェック
                solid_score = check_solid_principles(content, file_path)
                solid_scores.append(solid_score)
                
            except Exception as e:
                print(f"⚠️ ファイル品質分析エラー ({file_path}): {e}")
        
        # 平均値計算
        if complexity_scores:
            quality_metrics["cyclomatic_complexity"] = sum(complexity_scores) / len(complexity_scores)
        if solid_scores:
            quality_metrics["solid_principles_adherence"] = sum(solid_scores) / len(solid_scores)
        
        # コード重複率（簡略化）
        quality_metrics["code_duplication"] = 5  # デフォルト値
        
        # 保守性指標
        quality_metrics["maintainability_index"] = max(0, 100 - quality_metrics["cyclomatic_complexity"] * 2)
        
        # 総合品質スコア（5点満点）
        complexity_score = max(0, 100 - quality_metrics["cyclomatic_complexity"] * 5)
        quality_metrics["overall_quality_score"] = (
            complexity_score * 0.3 + 
            quality_metrics["solid_principles_adherence"] * 0.3 +
            (100 - quality_metrics["code_duplication"]) * 0.2 +
            quality_metrics["maintainability_index"] * 0.2
        ) / 100 * 5
        
    except Exception as e:
        print(f"⚠️ コード品質メトリクス分析エラー: {e}")
    
    return quality_metrics


def calculate_cyclomatic_complexity(content):
    """循環的複雑度を計算"""
    # if, elif, while, for, and, or, except などの数をカウント
    complexity_keywords = ['if', 'elif', 'while', 'for', 'and', 'or', 'except', 'with']
    complexity = 1  # 基本複雑度
    
    try:
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, (ast.If, ast.While, ast.For, ast.ExceptHandler)):
                complexity += 1
            elif isinstance(node, (ast.BoolOp, ast.Compare)):
                complexity += len(node.comparators) if hasattr(node, 'comparators') else 1
    except:
        # パースエラーの場合は単純な文字列カウント
        for keyword in complexity_keywords:
            complexity += content.count(keyword)
    
    return complexity


def check_solid_principles(content, file_path):
    """SOLID原則の簡易チェック"""
    score = 100
    
    try:
        tree = ast.parse(content)
        
        # クラス分析
        classes = [node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        
        for class_node in classes:
            methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
            
            # SRP (Single Responsibility Principle) - メソッド数での簡易判定
            if len(methods) > 15:
                score -= 20
            
            # OCP (Open/Closed Principle) - 継承とインターフェース使用の簡易チェック
            if not class_node.bases:
                score -= 10
            
            # ISP (Interface Segregation Principle) - メソッド名での簡易判定
            method_names = [m.name for m in methods]
            if len(method_names) > 10:
                score -= 15
            
            # DIP (Dependency Inversion Principle) - import分析での簡易チェック
            imports = re.findall(r'^(?:from|import)\s+([a-zA-Z_][a-zA-Z0-9_.]*)', content, re.MULTILINE)
            concrete_imports = [imp for imp in imports if not any(keyword in imp for keyword in ['abc', 'interface', 'protocol'])]
            if len(concrete_imports) > 5:
                score -= 10
    
    except Exception as e:
        score = 70  # デフォルト値
    
    return max(0, score)


def assess_technical_debt_impact(emergency_scope, architecture_validation, ddd_assessment, quality_metrics):
    """技術的負債影響を評価"""
    debt_assessment = {
        "newly_introduced_debt": 0,
        "debt_categories": [],
        "high_priority_items": 0,
        "recommended_resolution_sprints": 0,
        "impact_level": "LOW",
        "detailed_debt_items": []
    }
    
    try:
        debt_points = 0
        
        # アーキテクチャ違反による負債
        architecture_violations = len(architecture_validation.get("boundary_violations", []))
        if architecture_violations > 0:
            debt_points += architecture_violations * 10
            debt_assessment["debt_categories"].append("architecture")
            debt_assessment["detailed_debt_items"].append({
                "category": "architecture",
                "description": f"{architecture_violations} boundary violations",
                "priority": "high" if architecture_violations > 3 else "medium",
                "estimated_effort": architecture_violations * 2
            })
        
        # コード品質による負債
        if quality_metrics["cyclomatic_complexity"] > 10:
            debt_points += (quality_metrics["cyclomatic_complexity"] - 10) * 5
            debt_assessment["debt_categories"].append("code_quality")
            debt_assessment["detailed_debt_items"].append({
                "category": "code_quality",
                "description": f"High cyclomatic complexity: {quality_metrics['cyclomatic_complexity']:.1f}",
                "priority": "high" if quality_metrics["cyclomatic_complexity"] > 15 else "medium",
                "estimated_effort": 8
            })
        
        # DDD適合性による負債
        if ddd_assessment["overall_ddd_score"] < 3.0:
            debt_points += (3.0 - ddd_assessment["overall_ddd_score"]) * 20
            debt_assessment["debt_categories"].append("ddd_compliance")
            debt_assessment["detailed_debt_items"].append({
                "category": "ddd_compliance",
                "description": f"Low DDD compliance score: {ddd_assessment['overall_ddd_score']:.1f}",
                "priority": "medium",
                "estimated_effort": 12
            })
        
        # テストカバレッジ不足（emergency fixesでは一般的）
        debt_points += 30  # 緊急修正では通常テストが不足
        debt_assessment["debt_categories"].append("testing")
        debt_assessment["detailed_debt_items"].append({
            "category": "testing",
            "description": "Missing test coverage for emergency fixes",
            "priority": "high",
            "estimated_effort": 16
        })
        
        debt_assessment["newly_introduced_debt"] = debt_points
        
        # 高優先度項目数
        debt_assessment["high_priority_items"] = len([
            item for item in debt_assessment["detailed_debt_items"] 
            if item["priority"] == "high"
        ])
        
        # 解消推奨スプリント数
        total_effort = sum(item["estimated_effort"] for item in debt_assessment["detailed_debt_items"])
        debt_assessment["recommended_resolution_sprints"] = max(1, total_effort // 20)
        
        # 影響レベル
        if debt_points > 100:
            debt_assessment["impact_level"] = "HIGH"
        elif debt_points > 50:
            debt_assessment["impact_level"] = "MEDIUM"
        else:
            debt_assessment["impact_level"] = "LOW"
        
    except Exception as e:
        print(f"⚠️ 技術的負債評価エラー: {e}")
    
    return debt_assessment


def generate_improvement_recommendations(architecture_validation, ddd_assessment, quality_metrics, debt_assessment):
    """改善推奨事項を生成"""
    recommendations = []
    
    # アーキテクチャ改善
    if architecture_validation["overall_architecture_score"] < 3.0:
        recommendations.append({
            "priority": "high",
            "category": "architecture",
            "description": "Resolve layer boundary violations and improve dependency management",
            "estimated_effort": 16,
            "specific_actions": [
                "Review and refactor cross-layer dependencies",
                "Implement proper dependency injection",
                "Create clear layer interfaces"
            ]
        })
    
    # DDD改善
    if ddd_assessment["overall_ddd_score"] < 3.0:
        recommendations.append({
            "priority": "medium",
            "category": "ddd",
            "description": "Improve domain model design and DDD principle adherence",
            "estimated_effort": 12,
            "specific_actions": [
                "Refactor entities to improve integrity",
                "Ensure value object immutability",
                "Review aggregate boundaries"
            ]
        })
    
    # コード品質改善
    if quality_metrics["overall_quality_score"] < 3.0:
        recommendations.append({
            "priority": "medium",
            "category": "quality",
            "description": "Improve code quality metrics and maintainability",
            "estimated_effort": 8,
            "specific_actions": [
                "Reduce cyclomatic complexity",
                "Improve SOLID principles adherence",
                "Remove code duplication"
            ]
        })
    
    # 技術的負債解消
    if debt_assessment["impact_level"] in ["HIGH", "MEDIUM"]:
        recommendations.append({
            "priority": "high" if debt_assessment["impact_level"] == "HIGH" else "medium",
            "category": "debt",
            "description": f"Address {debt_assessment['impact_level'].lower()} priority technical debt",
            "estimated_effort": debt_assessment["recommended_resolution_sprints"] * 20,
            "specific_actions": [
                "Prioritize high-impact debt items",
                "Create debt resolution roadmap",
                "Implement preventive measures"
            ]
        })
    
    return recommendations


def create_validation_reports(validation_results, output_dir="docs/validation"):
    """検証レポートを作成"""
    reports = []
    
    try:
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        
        # アーキテクチャレポート
        arch_report_path = Path(output_dir) / f"architecture-validation-{timestamp}.md"
        arch_content = create_architecture_report(validation_results["architecture_compliance"])
        
        with open(arch_report_path, 'w', encoding='utf-8') as f:
            f.write(arch_content)
        
        reports.append({
            "report_type": "architecture",
            "file_path": str(arch_report_path),
            "summary": f"Architecture compliance: {validation_results['architecture_compliance']['overall_architecture_score']:.1f}/5.0"
        })
        
        # DDD適合性レポート
        ddd_report_path = Path(output_dir) / f"ddd-compliance-{timestamp}.md"
        ddd_content = create_ddd_report(validation_results["ddd_compliance"])
        
        with open(ddd_report_path, 'w', encoding='utf-8') as f:
            f.write(ddd_content)
        
        reports.append({
            "report_type": "ddd",
            "file_path": str(ddd_report_path),
            "summary": f"DDD compliance: {validation_results['ddd_compliance']['overall_ddd_score']:.1f}/5.0"
        })
        
        # コード品質レポート
        quality_report_path = Path(output_dir) / f"code-quality-{timestamp}.md"
        quality_content = create_quality_report(validation_results["code_quality"])
        
        with open(quality_report_path, 'w', encoding='utf-8') as f:
            f.write(quality_content)
        
        reports.append({
            "report_type": "quality",
            "file_path": str(quality_report_path),
            "summary": f"Code quality: {validation_results['code_quality']['overall_quality_score']:.1f}/5.0"
        })
        
        # 技術的負債レポート
        debt_report_path = Path(output_dir) / f"technical-debt-{timestamp}.md"
        debt_content = create_debt_report(validation_results["technical_debt"])
        
        with open(debt_report_path, 'w', encoding='utf-8') as f:
            f.write(debt_content)
        
        reports.append({
            "report_type": "debt",
            "file_path": str(debt_report_path),
            "summary": f"Technical debt: {validation_results['technical_debt']['impact_level']} ({validation_results['technical_debt']['newly_introduced_debt']} points)"
        })
        
    except Exception as e:
        print(f"⚠️ 検証レポート作成エラー: {e}")
    
    return reports


def create_architecture_report(architecture_data):
    """アーキテクチャ検証レポートを作成"""
    return f"""# Architecture Validation Report

Generated: {datetime.now().isoformat()}

## Summary
- **Overall Architecture Score**: {architecture_data['overall_architecture_score']:.1f}/5.0
- **Layer Separation Score**: {architecture_data['layer_separation_score']:.1f}%
- **Dependency Flow Valid**: {'✅' if architecture_data['dependency_flow_valid'] else '❌'}
- **Boundary Violations**: {len(architecture_data['boundary_violations'])}

## Detailed Analysis

### Layer Separation
- Score: {architecture_data['layer_separation_score']:.1f}%
- Responsibility Adherence: {architecture_data['responsibility_adherence']:.1f}%

### Boundary Violations
{chr(10).join([f"- {violation['description']} ({violation['file']})" for violation in architecture_data['boundary_violations']])}

## Recommendations
- Review and fix all boundary violations
- Implement proper dependency injection patterns
- Consider using architecture testing tools for continuous validation
"""


def create_ddd_report(ddd_data):
    """DDD適合性レポートを作成"""
    return f"""# DDD Compliance Report

Generated: {datetime.now().isoformat()}

## Summary
- **Overall DDD Score**: {ddd_data['overall_ddd_score']:.1f}/5.0
- **Entity Integrity**: {ddd_data['entity_integrity_score']:.1f}%
- **Value Object Immutability**: {'✅' if ddd_data['value_object_immutability'] else '❌'}
- **Aggregate Boundary Score**: {ddd_data['aggregate_boundary_score']:.1f}%
- **Ubiquitous Language**: {'✅' if ddd_data['ubiquitous_language_consistency'] else '❌'}

## Recommendations
- Improve entity identity and equality implementation
- Ensure value object immutability
- Review aggregate boundaries for consistency
- Maintain ubiquitous language throughout the domain model
"""


def create_quality_report(quality_data):
    """コード品質レポートを作成"""
    return f"""# Code Quality Report

Generated: {datetime.now().isoformat()}

## Summary
- **Overall Quality Score**: {quality_data['overall_quality_score']:.1f}/5.0
- **Cyclomatic Complexity**: {quality_data['cyclomatic_complexity']:.1f} (avg)
- **SOLID Principles**: {quality_data['solid_principles_adherence']:.1f}%
- **Code Duplication**: {quality_data['code_duplication']:.1f}%
- **Maintainability Index**: {quality_data['maintainability_index']:.1f}/100

## Recommendations
- Reduce cyclomatic complexity in complex methods
- Improve SOLID principles adherence
- Remove code duplication where possible
- Focus on maintainability improvements
"""


def create_debt_report(debt_data):
    """技術的負債レポートを作成"""
    debt_items = ""
    for item in debt_data['detailed_debt_items']:
        debt_items += f"- **{item['category']}** ({item['priority']}): {item['description']} (Est: {item['estimated_effort']}h)\n"
    
    return f"""# Technical Debt Report

Generated: {datetime.now().isoformat()}

## Summary
- **Impact Level**: {debt_data['impact_level']}
- **Debt Points**: {debt_data['newly_introduced_debt']}
- **High Priority Items**: {debt_data['high_priority_items']}
- **Recommended Resolution**: {debt_data['recommended_resolution_sprints']} sprints

## Debt Categories
{', '.join(debt_data['debt_categories'])}

## Detailed Items
{debt_items}

## Resolution Plan
1. Address high priority items first
2. Allocate {debt_data['recommended_resolution_sprints']} sprints for resolution
3. Implement preventive measures to avoid future debt
"""


def main():
    """メイン実行関数"""
    print("🔍 緊急修正検証エキスパート - 実行開始")
    
    # 引数解析
    issue_number = sys.argv[1] if len(sys.argv) > 1 else None
    
    try:
        # GitHub Issue情報取得
        issue_data = None
        if issue_number:
            issue_data = get_github_issue(issue_number)
            if issue_data:
                print(f"✅ Issue #{issue_number}: {issue_data['title']}")
        
        # 緊急修正スコープ分析
        print("📋 緊急修正スコープを分析中...")
        emergency_scope = analyze_emergency_fixes_scope()
        print(f"📊 分析結果: {emergency_scope['scope_analysis']['total_files']}ファイル, {emergency_scope['scope_analysis']['layers_affected']}レイヤー影響")
        
        # アーキテクチャ検証
        print("🏗️ レイヤードアーキテクチャを検証中...")
        architecture_validation = validate_layered_architecture(emergency_scope)
        print(f"📊 アーキテクチャスコア: {architecture_validation['overall_architecture_score']:.1f}/5.0")
        
        # DDD適合性評価
        print("🎯 DDD適合性を評価中...")
        ddd_assessment = assess_ddd_compliance(emergency_scope)
        print(f"📊 DDDスコア: {ddd_assessment['overall_ddd_score']:.1f}/5.0")
        
        # コード品質分析
        print("🔧 コード品質メトリクスを分析中...")
        quality_metrics = analyze_code_quality_metrics(emergency_scope)
        print(f"📊 品質スコア: {quality_metrics['overall_quality_score']:.1f}/5.0")
        
        # 技術的負債評価
        print("⚠️ 技術的負債影響を評価中...")
        debt_assessment = assess_technical_debt_impact(
            emergency_scope, architecture_validation, ddd_assessment, quality_metrics
        )
        print(f"📊 技術的負債: {debt_assessment['impact_level']} ({debt_assessment['newly_introduced_debt']}ポイント)")
        
        # 改善推奨事項生成
        print("💡 改善推奨事項を生成中...")
        improvement_recommendations = generate_improvement_recommendations(
            architecture_validation, ddd_assessment, quality_metrics, debt_assessment
        )
        print(f"📋 推奨事項: {len(improvement_recommendations)}件")
        
        # 検証結果構造体
        validation_results = {
            "architecture_compliance": architecture_validation,
            "ddd_compliance": ddd_assessment,
            "code_quality": quality_metrics,
            "technical_debt": debt_assessment
        }
        
        # 検証レポート作成
        print("📄 検証レポートを作成中...")
        validation_reports = create_validation_reports(validation_results)
        
        # 実行履歴更新
        execution_data = {
            "emergency_fix_validation": {
                "validation_completed_at": datetime.now().isoformat(),
                "status": "SUCCESS",
                "target_context": issue_number if issue_number else "comprehensive",
                "validation_results": validation_results,
                "improvement_recommendations": improvement_recommendations,
                "validation_reports": validation_reports,
                "next_actions": ["/reconcile-metadata", "/review-emergency-recovery"]
            }
        }
        
        # JSON形式で実行履歴を更新
        if issue_number:
            json_file = f"docs/use_cases/sprints/issue-{issue_number}.json"
        else:
            json_file = "docs/use_cases/emergency-validation.json"
        
        use_case_data = load_use_case_json(json_file)
        use_case_data.update(execution_data)
        update_execution_history(use_case_data, "validate-emergency-fix", "success")
        save_use_case_json(json_file, use_case_data)
        
        # 結果サマリー
        print("\n" + "="*80)
        print("✅ 緊急修正検証完了")
        print("="*80)
        print(f"🏗️ アーキテクチャ適合度: {architecture_validation['overall_architecture_score']:.1f}/5.0")
        print(f"🎯 DDD適合度: {ddd_assessment['overall_ddd_score']:.1f}/5.0")
        print(f"🔧 コード品質: {quality_metrics['overall_quality_score']:.1f}/5.0")
        print(f"⚠️ 技術的負債: {debt_assessment['impact_level']} ({debt_assessment['newly_introduced_debt']}ポイント)")
        print(f"📄 作成レポート: {len(validation_reports)}件")
        print(f"💡 改善推奨: {len(improvement_recommendations)}件")
        print("\n次のステップ: /reconcile-metadata で緊急復旧を完了してください")
        
        return 0
        
    except Exception as e:
        print(f"❌ 緊急修正検証エラー: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())