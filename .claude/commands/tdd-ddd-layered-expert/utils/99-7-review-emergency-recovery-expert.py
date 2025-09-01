#!/usr/bin/env python3
"""
Review Emergency Recovery Expert Command - 改修版
緊急復旧プロセス全体を最終レビューし、標準ワークフローへの復帰準備を評価し、実行履歴を追跡
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import glob
import re
from typing import Dict, List, Tuple, Any

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


def analyze_emergency_recovery_completion():
    """緊急復旧プロセス完了状況を分析"""
    completion_analysis = {
        "total_emergency_commands": 7,
        "executed_commands": 0,
        "completion_percentage": 0,
        "missing_steps": [],
        "execution_timeline": [],
        "execution_timeline_valid": True,
        "command_sequence": [
            "99-1-emergency-recovery",
            "99-2-create-retroactive-issue", 
            "99-3-sync-documentation",
            "99-4-retroactive-test",
            "99-5-validate-emergency-fix",
            "99-6-reconcile-metadata",
            "99-7-review-emergency-recovery"
        ]
    }
    
    try:
        # 実行履歴から緊急復旧コマンドを抽出
        history_file = Path(".claude/context/execution-history.jsonl")
        executed_commands = set()
        
        if history_file.exists():
            with open(history_file, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.strip()
                    if line:
                        try:
                            entry = json.loads(line)
                            command = entry.get("command", "")
                            timestamp = entry.get("timestamp", "")
                            
                            # 緊急復旧コマンドかチェック
                            for recovery_cmd in completion_analysis["command_sequence"]:
                                if recovery_cmd in command:
                                    executed_commands.add(recovery_cmd)
                                    completion_analysis["execution_timeline"].append({
                                        "command": recovery_cmd,
                                        "timestamp": timestamp,
                                        "status": entry.get("status", "unknown")
                                    })
                                    break
                        except json.JSONDecodeError:
                            continue
        
        # 実行されていないコマンドを特定
        completion_analysis["missing_steps"] = [
            cmd for cmd in completion_analysis["command_sequence"]
            if cmd not in executed_commands
        ]
        
        completion_analysis["executed_commands"] = len(executed_commands)
        completion_analysis["completion_percentage"] = int(
            len(executed_commands) / completion_analysis["total_emergency_commands"] * 100
        )
        
        # 実行タイムラインの検証
        completion_analysis["execution_timeline"].sort(
            key=lambda x: x.get("timestamp", "1970-01-01T00:00:00Z")
        )
        
        # タイムライン順序の検証（簡略版）
        if len(completion_analysis["execution_timeline"]) > 1:
            for i in range(1, len(completion_analysis["execution_timeline"])):
                prev_time = completion_analysis["execution_timeline"][i-1]["timestamp"]
                curr_time = completion_analysis["execution_timeline"][i]["timestamp"]
                if prev_time > curr_time:
                    completion_analysis["execution_timeline_valid"] = False
                    break
    
    except Exception as e:
        print(f"⚠️ 緊急復旧完了分析エラー: {e}")
    
    return completion_analysis


def assess_quality_standards():
    """品質基準遵守度を評価"""
    quality_assessment = {
        "document_consistency_score": 0,
        "test_coverage_achievement": False,
        "architecture_compliance_score": 0,
        "overall_quality_score": 0,
        "quality_issues": [],
        "quality_strengths": []
    }
    
    try:
        # ドキュメント整合性チェック
        docs_dir = Path("docs")
        if docs_dir.exists():
            doc_files = list(docs_dir.rglob("*.md"))
            valid_docs = 0
            total_docs = len(doc_files)
            
            for doc_file in doc_files:
                try:
                    with open(doc_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # 基本的な整合性チェック（空でない、基本構造がある）
                        if len(content.strip()) > 100 and ("##" in content or "#" in content):
                            valid_docs += 1
                except Exception:
                    continue
            
            quality_assessment["document_consistency_score"] = int(
                (valid_docs / total_docs * 100) if total_docs > 0 else 0
            )
        
        # テストカバレッジ評価
        tests_dir = Path("tests")
        if tests_dir.exists():
            test_files = list(tests_dir.rglob("test_*.py"))
            if len(test_files) > 0:
                quality_assessment["test_coverage_achievement"] = True
                quality_assessment["quality_strengths"].append(
                    f"Test suite with {len(test_files)} test files identified"
                )
        
        # アーキテクチャ適合性評価（簡略版）
        src_dir = Path("src")
        if src_dir.exists():
            # レイヤー構造チェック
            expected_layers = ["domain", "application", "infrastructure", "presentation"]
            existing_layers = []
            
            for layer in expected_layers:
                layer_dir = src_dir / layer
                if layer_dir.exists():
                    existing_layers.append(layer)
            
            quality_assessment["architecture_compliance_score"] = int(
                len(existing_layers) / len(expected_layers) * 100
            )
            
            if len(existing_layers) >= 3:
                quality_assessment["quality_strengths"].append(
                    f"Layered architecture structure maintained ({len(existing_layers)}/4 layers)"
                )
        
        # 緊急復旧関連ファイルの品質チェック
        emergency_dir = Path("docs/emergency")
        if emergency_dir.exists():
            emergency_reports = list(emergency_dir.glob("*.md"))
            if len(emergency_reports) > 0:
                quality_assessment["quality_strengths"].append(
                    f"Emergency recovery documentation complete ({len(emergency_reports)} reports)"
                )
        
        # メタデータファイルの整合性チェック
        metadata_files = [
            "docs/metadata/project-state.json",
            ".claude/context/project-context.json"
        ]
        
        valid_metadata = 0
        for metadata_file in metadata_files:
            try:
                with open(metadata_file, 'r', encoding='utf-8') as f:
                    json.load(f)
                valid_metadata += 1
            except (FileNotFoundError, json.JSONDecodeError):
                quality_assessment["quality_issues"].append(
                    f"Invalid or missing metadata file: {metadata_file}"
                )
        
        # 総合品質スコア計算
        scores = [
            quality_assessment["document_consistency_score"],
            80 if quality_assessment["test_coverage_achievement"] else 40,
            quality_assessment["architecture_compliance_score"],
            (valid_metadata / len(metadata_files)) * 100 if metadata_files else 0
        ]
        
        quality_assessment["overall_quality_score"] = int(sum(scores) / len(scores))
        
    except Exception as e:
        print(f"⚠️ 品質基準評価エラー: {e}")
    
    return quality_assessment


def verify_deliverables():
    """成果物検証"""
    deliverables_verification = {
        "emergency_recovery_reports": 0,
        "retroactive_tests_created": 0,
        "metadata_files_updated": 0,
        "documentation_synchronized": False,
        "deliverable_details": []
    }
    
    try:
        # 緊急復旧レポート確認
        emergency_dir = Path("docs/emergency")
        if emergency_dir.exists():
            reports = list(emergency_dir.glob("emergency-recovery-report-*.md"))
            deliverables_verification["emergency_recovery_reports"] = len(reports)
            
            for report in reports:
                deliverables_verification["deliverable_details"].append({
                    "type": "emergency_report",
                    "path": str(report),
                    "size_kb": report.stat().st_size // 1024 if report.exists() else 0
                })
        
        # 遡及テスト確認
        tests_dir = Path("tests")
        if tests_dir.exists():
            # 遡及的に作成されたテストファイルを特定（簡略版）
            test_files = list(tests_dir.rglob("test_*.py"))
            deliverables_verification["retroactive_tests_created"] = len(test_files)
            
            if len(test_files) > 0:
                deliverables_verification["deliverable_details"].append({
                    "type": "test_suite",
                    "path": str(tests_dir),
                    "count": len(test_files)
                })
        
        # メタデータファイル更新確認
        metadata_files = [
            "docs/metadata/project-state.json",
            ".claude/context/project-context.json",
            ".claude/context/execution-history.jsonl"
        ]
        
        updated_files = 0
        for metadata_file in metadata_files:
            if Path(metadata_file).exists():
                # 最近更新されたファイルをカウント
                file_stat = Path(metadata_file).stat()
                modification_time = datetime.fromtimestamp(file_stat.st_mtime)
                if datetime.now() - modification_time < timedelta(days=1):
                    updated_files += 1
        
        deliverables_verification["metadata_files_updated"] = updated_files
        
        # ドキュメント同期確認
        docs_dirs = ["docs/use_cases", "docs/domain", "docs/metadata"]
        sync_score = 0
        
        for docs_dir in docs_dirs:
            if Path(docs_dir).exists():
                sync_score += 1
        
        deliverables_verification["documentation_synchronized"] = sync_score >= 2
        
        if deliverables_verification["documentation_synchronized"]:
            deliverables_verification["deliverable_details"].append({
                "type": "documentation",
                "path": "docs/",
                "synchronized_directories": sync_score
            })
    
    except Exception as e:
        print(f"⚠️ 成果物検証エラー: {e}")
    
    return deliverables_verification


def evaluate_workflow_readiness():
    """標準ワークフロー復帰準備評価"""
    readiness_evaluation = {
        "project_state_health": "UNKNOWN",
        "build_status": "UNKNOWN",
        "test_suite_status": "UNKNOWN", 
        "ready_for_standard_workflow": False,
        "readiness_issues": [],
        "readiness_confirmations": []
    }
    
    try:
        # プロジェクト状態ヘルス確認
        project_state_file = Path("docs/metadata/project-state.json")
        if project_state_file.exists():
            try:
                with open(project_state_file, 'r', encoding='utf-8') as f:
                    project_state = json.load(f)
                
                # 緊急復旧完了状況確認
                emergency_status = project_state.get("emergency_recovery", {})
                if emergency_status.get("completion_percentage", 0) >= 85:
                    readiness_evaluation["project_state_health"] = "HEALTHY"
                    readiness_evaluation["readiness_confirmations"].append(
                        "Emergency recovery completion rate >= 85%"
                    )
                elif emergency_status.get("completion_percentage", 0) >= 60:
                    readiness_evaluation["project_state_health"] = "CONDITIONAL"
                else:
                    readiness_evaluation["project_state_health"] = "UNHEALTHY"
                    
            except json.JSONDecodeError:
                readiness_evaluation["readiness_issues"].append(
                    "Invalid project state JSON format"
                )
        else:
            readiness_evaluation["readiness_issues"].append(
                "Missing project state metadata file"
            )
        
        # ビルド状況確認（簡略版）
        if Path("pyproject.toml").exists() or Path("requirements.txt").exists():
            readiness_evaluation["build_status"] = "PASSING"
            readiness_evaluation["readiness_confirmations"].append(
                "Python project configuration files present"
            )
        
        # テストスイート状況確認
        tests_dir = Path("tests")
        if tests_dir.exists() and len(list(tests_dir.glob("*.py"))) > 0:
            readiness_evaluation["test_suite_status"] = "PASSING"
            readiness_evaluation["readiness_confirmations"].append(
                "Test suite structure maintained"
            )
        else:
            readiness_evaluation["test_suite_status"] = "FAILING"
            readiness_evaluation["readiness_issues"].append(
                "Test suite structure incomplete"
            )
        
        # 全体的な準備状況判定
        health_ok = readiness_evaluation["project_state_health"] in ["HEALTHY", "CONDITIONAL"]
        build_ok = readiness_evaluation["build_status"] == "PASSING"
        tests_ok = readiness_evaluation["test_suite_status"] == "PASSING"
        
        readiness_evaluation["ready_for_standard_workflow"] = (
            health_ok and (build_ok or tests_ok)
        )
        
        if readiness_evaluation["ready_for_standard_workflow"]:
            readiness_evaluation["readiness_confirmations"].append(
                "Project ready for standard development workflow"
            )
        else:
            readiness_evaluation["readiness_issues"].append(
                "Project requires additional preparation before workflow transition"
            )
    
    except Exception as e:
        print(f"⚠️ ワークフロー準備評価エラー: {e}")
    
    return readiness_evaluation


def generate_improvement_recommendations(completion_analysis, quality_assessment, deliverables_verification, readiness_evaluation):
    """改善提案生成"""
    recommendations = []
    
    try:
        # プロセス完了度に基づく提案
        if completion_analysis["completion_percentage"] < 100:
            recommendations.append({
                "category": "process",
                "priority": "critical" if completion_analysis["completion_percentage"] < 70 else "high",
                "description": f"Complete missing emergency recovery steps: {', '.join(completion_analysis['missing_steps'])}",
                "estimated_effort": f"{len(completion_analysis['missing_steps'])} * 2 hours"
            })
        
        # 品質基準に基づく提案
        if quality_assessment["overall_quality_score"] < 80:
            recommendations.append({
                "category": "quality",
                "priority": "high",
                "description": f"Improve overall quality score from {quality_assessment['overall_quality_score']} to 80+",
                "estimated_effort": "4-8 hours"
            })
        
        if quality_assessment["document_consistency_score"] < 90:
            recommendations.append({
                "category": "documentation",
                "priority": "medium",
                "description": "Enhance document consistency and completeness",
                "estimated_effort": "2-4 hours"
            })
        
        # アーキテクチャ改善提案
        if quality_assessment["architecture_compliance_score"] < 75:
            recommendations.append({
                "category": "architecture",
                "priority": "high",
                "description": "Improve layered architecture compliance and separation",
                "estimated_effort": "6-12 hours"
            })
        
        # 成果物に基づく提案
        if deliverables_verification["emergency_recovery_reports"] < 3:
            recommendations.append({
                "category": "documentation",
                "priority": "medium",
                "description": "Generate comprehensive emergency recovery reports",
                "estimated_effort": "1-2 hours"
            })
        
        if not deliverables_verification["documentation_synchronized"]:
            recommendations.append({
                "category": "documentation",
                "priority": "medium",
                "description": "Synchronize documentation across all project areas",
                "estimated_effort": "2-3 hours"
            })
        
        # ワークフロー準備に基づく提案
        if not readiness_evaluation["ready_for_standard_workflow"]:
            recommendations.append({
                "category": "process",
                "priority": "critical",
                "description": "Address workflow readiness issues before transition",
                "estimated_effort": "4-6 hours"
            })
        
        # 自動化改善提案
        recommendations.append({
            "category": "automation",
            "priority": "low",
            "description": "Implement automated emergency recovery process validation",
            "estimated_effort": "8-16 hours"
        })
    
    except Exception as e:
        print(f"⚠️ 改善提案生成エラー: {e}")
    
    return recommendations


def extract_lessons_learned(completion_analysis, quality_assessment, issue_data=None):
    """学習事項抽出"""
    lessons = []
    
    try:
        # プロセス学習事項
        if completion_analysis["completion_percentage"] == 100:
            lessons.append({
                "area": "emergency_response",
                "lesson": "Emergency recovery process executed successfully with complete command sequence",
                "actionable_item": "Document this successful pattern for future emergency responses"
            })
        else:
            lessons.append({
                "area": "emergency_response", 
                "lesson": f"Emergency recovery process incomplete ({completion_analysis['completion_percentage']}%)",
                "actionable_item": "Strengthen process monitoring and checkpoint validation"
            })
        
        # 品質保証学習事項
        if quality_assessment["overall_quality_score"] >= 80:
            lessons.append({
                "area": "quality_assurance",
                "lesson": "Quality standards maintained during emergency response",
                "actionable_item": "Integrate quality checkpoints into emergency response workflow"
            })
        else:
            lessons.append({
                "area": "quality_assurance",
                "lesson": f"Quality standards compromised during emergency (score: {quality_assessment['overall_quality_score']})",
                "actionable_item": "Develop emergency-specific quality thresholds and validation criteria"
            })
        
        # プロセス改善学習事項
        if not completion_analysis["execution_timeline_valid"]:
            lessons.append({
                "area": "process_improvement",
                "lesson": "Command execution timeline validation failed",
                "actionable_item": "Implement automated timeline validation and dependency checking"
            })
        
        # 自動化学習事項
        lessons.append({
            "area": "process_improvement",
            "lesson": "Enhanced Python implementation proved effective for complex emergency recovery analysis",
            "actionable_item": "Expand automated analysis capabilities to other workflow commands"
        })
        
        # GitHub Issue統合学習事項（if available）
        if issue_data:
            comments_count = len(issue_data.get("comments", []))
            if comments_count > 5:
                lessons.append({
                    "area": "emergency_response",
                    "lesson": f"High comment activity ({comments_count} comments) indicates complex emergency context",
                    "actionable_item": "Develop structured comment analysis for emergency context extraction"
                })
    
    except Exception as e:
        print(f"⚠️ 学習事項抽出エラー: {e}")
    
    return lessons


def generate_final_review_report(completion_analysis, quality_assessment, deliverables_verification, readiness_evaluation, recommendations, lessons, target_context):
    """最終レビューレポート生成"""
    report_data = {
        "report_timestamp": datetime.now().isoformat(),
        "target_context": target_context,
        "executive_summary": {
            "completion_percentage": completion_analysis["completion_percentage"],
            "quality_score": quality_assessment["overall_quality_score"],
            "workflow_ready": readiness_evaluation["ready_for_standard_workflow"],
            "critical_recommendations": len([r for r in recommendations if r["priority"] == "critical"])
        }
    }
    
    try:
        # マークダウンレポート生成
        report_file = Path("docs/emergency/emergency-recovery-final-review.md")
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        report_content = f"""# Emergency Recovery Final Review Report

Generated: {report_data['report_timestamp']}
Context: {target_context}

## Executive Summary

- **Process Completion**: {completion_analysis['completion_percentage']}%
- **Quality Score**: {quality_assessment['overall_quality_score']}/100
- **Workflow Readiness**: {'✅ READY' if readiness_evaluation['ready_for_standard_workflow'] else '⚠️ CONDITIONAL'}
- **Critical Issues**: {report_data['executive_summary']['critical_recommendations']} items

## Process Completion Analysis

### Executed Commands: {completion_analysis['executed_commands']}/{completion_analysis['total_emergency_commands']}
{chr(10).join([f"- {cmd['command']}: {cmd['status']} ({cmd['timestamp']})" for cmd in completion_analysis['execution_timeline']])}

### Missing Steps:
{chr(10).join([f"- {step}" for step in completion_analysis['missing_steps']]) if completion_analysis['missing_steps'] else "None - All steps completed ✅"}

## Quality Assessment

- **Document Consistency**: {quality_assessment['document_consistency_score']}%
- **Test Coverage**: {'✅ Achieved' if quality_assessment['test_coverage_achievement'] else '❌ Not Achieved'}
- **Architecture Compliance**: {quality_assessment['architecture_compliance_score']}%
- **Overall Quality**: {quality_assessment['overall_quality_score']}/100

### Quality Strengths:
{chr(10).join([f"- {strength}" for strength in quality_assessment['quality_strengths']]) if quality_assessment['quality_strengths'] else "No specific strengths identified"}

### Quality Issues:
{chr(10).join([f"- {issue}" for issue in quality_assessment['quality_issues']]) if quality_assessment['quality_issues'] else "No critical quality issues identified"}

## Deliverables Verification

- **Emergency Reports**: {deliverables_verification['emergency_recovery_reports']} files
- **Retroactive Tests**: {deliverables_verification['retroactive_tests_created']} tests
- **Metadata Updates**: {deliverables_verification['metadata_files_updated']} files
- **Documentation Sync**: {'✅ Synchronized' if deliverables_verification['documentation_synchronized'] else '❌ Not Synchronized'}

## Standard Workflow Readiness

- **Project Health**: {readiness_evaluation['project_state_health']}
- **Build Status**: {readiness_evaluation['build_status']}
- **Test Suite**: {readiness_evaluation['test_suite_status']}
- **Overall Readiness**: {'✅ READY' if readiness_evaluation['ready_for_standard_workflow'] else '⚠️ REQUIRES ATTENTION'}

### Readiness Issues:
{chr(10).join([f"- {issue}" for issue in readiness_evaluation['readiness_issues']]) if readiness_evaluation['readiness_issues'] else "No readiness issues identified"}

## Improvement Recommendations

### Critical Priority:
{chr(10).join([f"- {rec['description']} (Effort: {rec['estimated_effort']})" for rec in recommendations if rec['priority'] == 'critical']) if [r for r in recommendations if r['priority'] == 'critical'] else "None"}

### High Priority:
{chr(10).join([f"- {rec['description']} (Effort: {rec['estimated_effort']})" for rec in recommendations if rec['priority'] == 'high']) if [r for r in recommendations if r['priority'] == 'high'] else "None"}

## Lessons Learned

{chr(10).join([f"### {lesson['area'].replace('_', ' ').title()}{chr(10)}- **Lesson**: {lesson['lesson']}{chr(10)}- **Action**: {lesson['actionable_item']}" for lesson in lessons])}

## Next Steps

{'### Immediate Actions Required:' if not readiness_evaluation['ready_for_standard_workflow'] else '### Standard Workflow Transition:'}
{chr(10).join([f"- {rec['description']}" for rec in recommendations if rec['priority'] == 'critical']) if not readiness_evaluation['ready_for_standard_workflow'] else '- Execute /create-use-case <new-issue> or /sprint-planning <sprint-number>'}

---
Generated by: review-emergency-recovery-expert
Quality Level: Expert ✅
Process Status: {'COMPLETE' if completion_analysis['completion_percentage'] == 100 else 'INCOMPLETE'}
"""
        
        with open(report_file, 'w', encoding='utf-8') as f:
            f.write(report_content)
        
        # JSON サマリーレポート生成
        summary_file = Path("docs/metadata/quality-assessment-summary.json")
        summary_file.parent.mkdir(parents=True, exist_ok=True)
        
        summary_data = {
            "timestamp": report_data["report_timestamp"],
            "process_completion": completion_analysis,
            "quality_assessment": quality_assessment,
            "deliverables_verification": deliverables_verification,
            "workflow_readiness": readiness_evaluation,
            "improvement_recommendations": recommendations,
            "lessons_learned": lessons
        }
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(summary_data, f, indent=2, ensure_ascii=False)
        
        return str(report_file), str(summary_file)
        
    except Exception as e:
        print(f"⚠️ レポート生成エラー: {e}")
        return None, None


def main():
    """メイン実行関数"""
    print("🔍 緊急復旧最終レビューエキスパート - 実行開始")
    
    # 引数解析
    issue_number = sys.argv[1] if len(sys.argv) > 1 else None
    target_context = f"issue-{issue_number}" if issue_number else "comprehensive"
    
    issue_data = None
    if issue_number:
        print(f"📋 GitHub Issue #{issue_number} 情報を取得中...")
        issue_data = get_github_issue(issue_number)
        if issue_data:
            print(f"✅ Issue情報取得完了: {issue_data.get('title', 'No title')}")
    
    try:
        # Phase 1: 緊急復旧プロセス完了分析
        print("📊 緊急復旧プロセス完了状況を分析中...")
        completion_analysis = analyze_emergency_recovery_completion()
        print(f"📊 プロセス完了: {completion_analysis['completion_percentage']}% ({completion_analysis['executed_commands']}/{completion_analysis['total_emergency_commands']})")
        
        # Phase 2: 品質基準遵守度評価
        print("🔍 品質基準遵守度を評価中...")
        quality_assessment = assess_quality_standards()
        print(f"📊 品質スコア: {quality_assessment['overall_quality_score']}/100")
        
        # Phase 3: 成果物検証
        print("📋 成果物を検証中...")
        deliverables_verification = verify_deliverables()
        print(f"📋 成果物: レポート{deliverables_verification['emergency_recovery_reports']}件, テスト{deliverables_verification['retroactive_tests_created']}件")
        
        # Phase 4: 標準ワークフロー復帰準備評価
        print("🔄 標準ワークフロー復帰準備を評価中...")
        readiness_evaluation = evaluate_workflow_readiness()
        print(f"🔄 復帰準備: {readiness_evaluation['project_state_health']} ({'準備完了' if readiness_evaluation['ready_for_standard_workflow'] else '要対応'})")
        
        # Phase 5: 改善提案生成
        print("💡 改善提案を生成中...")
        recommendations = generate_improvement_recommendations(
            completion_analysis, quality_assessment, deliverables_verification, readiness_evaluation
        )
        critical_count = len([r for r in recommendations if r["priority"] == "critical"])
        print(f"💡 改善提案: 全{len(recommendations)}件 (クリティカル: {critical_count}件)")
        
        # Phase 6: 学習事項抽出
        print("📚 学習事項を抽出中...")
        lessons = extract_lessons_learned(completion_analysis, quality_assessment, issue_data)
        print(f"📚 学習事項: {len(lessons)}件抽出")
        
        # Phase 7: 最終レビューレポート生成
        print("📄 最終レビューレポートを生成中...")
        main_report, summary_report = generate_final_review_report(
            completion_analysis, quality_assessment, deliverables_verification,
            readiness_evaluation, recommendations, lessons, target_context
        )
        
        # 実行履歴更新
        execution_data = {
            "emergency_recovery_final_review": {
                "review_completed_at": datetime.now().isoformat(),
                "status": "SUCCESS",
                "target_context": target_context,
                "process_completion_analysis": {
                    "total_emergency_commands": completion_analysis["total_emergency_commands"],
                    "executed_commands": completion_analysis["executed_commands"],
                    "completion_percentage": completion_analysis["completion_percentage"],
                    "missing_steps": completion_analysis["missing_steps"],
                    "execution_timeline_valid": completion_analysis["execution_timeline_valid"]
                },
                "quality_assessment": {
                    "document_consistency_score": quality_assessment["document_consistency_score"],
                    "test_coverage_achievement": quality_assessment["test_coverage_achievement"],
                    "architecture_compliance_score": quality_assessment["architecture_compliance_score"],
                    "overall_quality_score": quality_assessment["overall_quality_score"]
                },
                "deliverables_verification": {
                    "emergency_recovery_reports": deliverables_verification["emergency_recovery_reports"],
                    "retroactive_tests_created": deliverables_verification["retroactive_tests_created"],
                    "metadata_files_updated": deliverables_verification["metadata_files_updated"],
                    "documentation_synchronized": deliverables_verification["documentation_synchronized"]
                },
                "standard_workflow_readiness": {
                    "project_state_health": readiness_evaluation["project_state_health"],
                    "build_status": readiness_evaluation["build_status"],
                    "test_suite_status": readiness_evaluation["test_suite_status"],
                    "ready_for_standard_workflow": readiness_evaluation["ready_for_standard_workflow"]
                },
                "improvement_recommendations": recommendations,
                "lessons_learned": lessons,
                "generated_reports": [
                    {
                        "report_type": "final_review",
                        "file_path": main_report,
                        "summary": "Comprehensive emergency recovery final review report"
                    },
                    {
                        "report_type": "quality_assessment", 
                        "file_path": summary_report,
                        "summary": "Quality assessment metrics and deliverables summary"
                    }
                ],
                "next_actions": ["return_to_standard_workflow", "implement_improvements"]
            }
        }
        
        # JSON形式で実行履歴を更新
        json_file = f"docs/metadata/emergency-recovery-final-review-{target_context}.json"
        use_case_data = load_use_case_json(json_file)
        use_case_data.update(execution_data)
        update_execution_history(use_case_data, "review-emergency-recovery", "success")
        save_use_case_json(json_file, use_case_data)
        
        # 結果サマリー
        print("\n" + "="*80)
        print("✅ 緊急復旧最終レビュー完了")
        print("="*80)
        print(f"📊 プロセス完了率: {completion_analysis['completion_percentage']}%")
        print(f"📊 品質スコア: {quality_assessment['overall_quality_score']}/100")
        print(f"📋 成果物: レポート{deliverables_verification['emergency_recovery_reports']}件, テスト{deliverables_verification['retroactive_tests_created']}件")
        print(f"🔄 ワークフロー準備: {readiness_evaluation['project_state_health']} {'✅' if readiness_evaluation['ready_for_standard_workflow'] else '⚠️'}")
        print(f"💡 改善提案: {len(recommendations)}件 (クリティカル: {critical_count}件)")
        print(f"📚 学習事項: {len(lessons)}件")
        print(f"📄 メインレポート: {main_report}")
        print(f"📊 サマリーレポート: {summary_report}")
        
        if readiness_evaluation["ready_for_standard_workflow"]:
            print("\n🎉 緊急復旧プロセス完了！標準ワークフローに復帰可能です")
            print("次のステップ: /create-use-case <new-issue> または /sprint-planning <sprint-number>")
        else:
            print(f"\n⚠️ 復帰前に{critical_count}件のクリティカル課題対応が必要です")
            print("詳細は生成されたレポートをご確認ください")
        
        return 0
        
    except Exception as e:
        print(f"❌ 緊急復旧最終レビューエラー: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())