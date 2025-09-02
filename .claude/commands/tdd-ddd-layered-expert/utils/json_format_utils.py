#!/usr/bin/env python3
"""
共通ユーティリティ関数
カスタムコマンド全体で使用するJSON操作とフォーマット変換機能
MCP統合により、思考・コンテキスト管理機能を提供
"""

import json
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any, Union


def update_execution_history(
    json_path: str,
    command_name: str,
    status: str = "success",
    files_affected: Optional[List[str]] = None,
    duration_ms: Optional[int] = None,
    error_message: Optional[str] = None
) -> None:
    """
    実行履歴を更新する共通関数
    
    Args:
        json_path: 更新対象のJSONファイルパス
        command_name: 実行されたコマンド名
        status: 実行ステータス (success/failed/partial)
        files_affected: 影響を受けたファイルのリスト
        duration_ms: 実行時間（ミリ秒）
        error_message: エラーメッセージ（エラー時のみ）
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # execution_historyセクションが存在しない場合は初期化
    if 'execution_history' not in data:
        data['execution_history'] = {
            "tdd_phases": {
                "RED": {"status": "not_started"},
                "GREEN": {"status": "not_started"},
                "REFACTOR": {"status": "not_started"}
            },
            "commands_executed": [],
            "last_command": None
        }
    
    # コマンド実行記録を追加
    execution_record = {
        "command": command_name,
        "executed_at": datetime.now().isoformat(),
        "status": status,
        "files_affected": files_affected or []
    }
    
    if duration_ms is not None:
        execution_record["duration_ms"] = duration_ms
    
    if error_message is not None:
        execution_record["error_message"] = error_message
    
    data['execution_history']['commands_executed'].append(execution_record)
    data['execution_history']['last_command'] = command_name
    
    # メタデータの更新日時を更新
    if 'metadata' in data:
        data['metadata']['updated_at'] = datetime.now().isoformat()
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def update_tdd_phase(
    json_path: str,
    phase: str,
    status: str,
    command: str,
    files_created: Optional[List[str]] = None,
    files_modified: Optional[List[str]] = None
) -> None:
    """
    TDDフェーズの状態を更新する
    
    Args:
        json_path: 更新対象のJSONファイルパス
        phase: TDDフェーズ (RED/GREEN/REFACTOR)
        status: フェーズステータス (not_started/in_progress/completed)
        command: 実行されたコマンド
        files_created: 作成されたファイルのリスト
        files_modified: 変更されたファイルのリスト
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    if 'execution_history' not in data:
        data['execution_history'] = {
            "tdd_phases": {
                "RED": {"status": "not_started"},
                "GREEN": {"status": "not_started"},
                "REFACTOR": {"status": "not_started"}
            },
            "commands_executed": [],
            "last_command": None
        }
    
    phase_data = {
        "status": status,
        "command": command
    }
    
    if status == "completed":
        phase_data["completed_at"] = datetime.now().isoformat()
    
    if files_created:
        phase_data["files_created"] = files_created
    
    if files_modified:
        phase_data["files_modified"] = files_modified
    
    data['execution_history']['tdd_phases'][phase] = phase_data
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_use_case_json(json_path: str) -> Dict[str, Any]:
    """
    新旧両フォーマットを読み込み、新フォーマットに正規化する
    
    Args:
        json_path: 読み込むJSONファイルパス
        
    Returns:
        新フォーマットに正規化されたデータ
    """
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # 旧フォーマットの検出と変換
    if 'use_case_metadata' in data:
        data['metadata'] = data.pop('use_case_metadata')
        # github_issue情報を適切な場所に移動
        if 'github_issue' in data['metadata']:
            github_info = data['metadata']['github_issue']
            data['metadata']['issue_id'] = github_info.get('number')
            data['metadata']['github_url'] = github_info.get('url')
            data['metadata']['labels'] = github_info.get('labels', [])
            data['metadata']['assignees'] = github_info.get('assignees', [])
    
    # シナリオセクションの正規化
    if 'scenarios' in data:
        scenarios = data['scenarios']
        if 'main_success' in scenarios:
            scenarios['main_scenarios'] = scenarios.pop('main_success')
        if 'alternative_flows' in scenarios:
            scenarios['alternative_scenarios'] = scenarios.pop('alternative_flows')
        if 'exception_flows' in scenarios:
            scenarios['exception_scenarios'] = scenarios.pop('exception_flows')
    
    # 必須セクションの初期化
    if 'execution_history' not in data:
        data['execution_history'] = {
            "tdd_phases": {
                "RED": {"status": "not_started"},
                "GREEN": {"status": "not_started"},
                "REFACTOR": {"status": "not_started"}
            },
            "commands_executed": [],
            "last_command": None
        }
    
    if 'domain_model' not in data:
        data['domain_model'] = {
            "entities": [],
            "value_objects": [],
            "domain_services": [],
            "business_rules": [],
            "ubiquitous_language": {}
        }
    
    return data


def save_use_case_json(json_path: str, data: Dict[str, Any]) -> None:
    """
    データを新フォーマットで保存する
    
    Args:
        json_path: 保存先のJSONファイルパス
        data: 保存するデータ
    """
    # メタデータの更新日時を更新
    if 'metadata' in data:
        data['metadata']['updated_at'] = datetime.now().isoformat()
    
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def get_next_recommended_commands(json_path: str) -> List[str]:
    """
    実行履歴から次に推奨されるコマンドを返す
    
    Args:
        json_path: JSONファイルパス
        
    Returns:
        推奨コマンドのリスト
    """
    data = load_use_case_json(json_path)
    executed_commands = set()
    
    if 'execution_history' in data and 'commands_executed' in data['execution_history']:
        for cmd in data['execution_history']['commands_executed']:
            if cmd['status'] == 'success':
                # コマンド名から番号部分を抽出
                cmd_parts = cmd['command'].split()
                if len(cmd_parts) > 0:
                    executed_commands.add(cmd_parts[0])
    
    # TDDフェーズの進捗を確認
    tdd_phases = data.get('execution_history', {}).get('tdd_phases', {})
    
    recommendations = []
    
    # フェーズに基づいた推奨
    if tdd_phases.get('RED', {}).get('status') != 'completed':
        if '/create-use-case' in executed_commands:
            if '/domain-modeling' not in executed_commands:
                recommendations.append('/domain-modeling')
            elif '/create-tests' not in executed_commands:
                recommendations.append('/create-tests')
    elif tdd_phases.get('GREEN', {}).get('status') != 'completed':
        if '/implement-domain' not in executed_commands:
            recommendations.append('/implement-domain')
        elif '/implement-usecase' not in executed_commands:
            recommendations.append('/implement-usecase')
        elif '/implement-infra' not in executed_commands:
            recommendations.append('/implement-infra')
        elif '/implement-presentation' not in executed_commands:
            recommendations.append('/implement-presentation')
    elif tdd_phases.get('REFACTOR', {}).get('status') != 'completed':
        recommendations.append('/refactor')
    
    return recommendations


def format_execution_status(data: Dict[str, Any]) -> str:
    """
    実行状況を見やすい形式でフォーマットする
    
    Args:
        data: ユースケースデータ
        
    Returns:
        フォーマットされた文字列
    """
    lines = []
    
    # TDD進捗
    lines.append("🎯 TDD進捗:")
    tdd_phases = data.get('execution_history', {}).get('tdd_phases', {})
    
    for phase, phase_data in tdd_phases.items():
        status = phase_data.get('status', 'not_started')
        if status == 'completed':
            completed_at = phase_data.get('completed_at', '')
            if completed_at:
                dt = datetime.fromisoformat(completed_at)
                lines.append(f"  {phase:<12}: ✅ 完了 ({dt.strftime('%Y-%m-%d %H:%M')})")
            else:
                lines.append(f"  {phase:<12}: ✅ 完了")
        elif status == 'in_progress':
            lines.append(f"  {phase:<12}: 🔄 進行中")
        else:
            lines.append(f"  {phase:<12}: ⏳ 未開始")
    
    # 実行済みコマンド
    lines.append("\n📝 実行済みコマンド:")
    commands = data.get('execution_history', {}).get('commands_executed', [])
    
    for cmd in commands[-10:]:  # 最新10件を表示
        executed_at = datetime.fromisoformat(cmd['executed_at'])
        status_icon = "✅" if cmd['status'] == 'success' else "❌" if cmd['status'] == 'failed' else "⚠️"
        lines.append(f"  {status_icon} {cmd['command']:<25} ({executed_at.strftime('%Y-%m-%d %H:%M')})")
    
    if len(commands) > 10:
        lines.append(f"  ... 他 {len(commands) - 10} 件")
    
    return "\n".join(lines)


# ==============================
# MCP Integration Functions
# ==============================

def create_mcp_session_context(
    json_path: str,
    session_id: str,
    project_analysis_data: Optional[Dict[str, Any]] = None,
    mcp_memories: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    MCPセッション初期化時のコンテキストをJSONに統合
    
    Args:
        json_path: 更新対象のJSONファイルパス
        session_id: MCPセッションID
        project_analysis_data: Serenaからのプロジェクト分析データ
        mcp_memories: 利用可能なMCPメモリのリスト
        
    Returns:
        更新されたコンテキストデータ
    """
    data = load_use_case_json(json_path)
    
    # MCPコンテキストセクションの初期化
    if 'mcp_context' not in data:
        data['mcp_context'] = {
            "session_info": {},
            "serena_analysis": {},
            "context7_cache": {},
            "design_rationale": {},
            "learning_outcomes": []
        }
    
    # セッション情報の更新
    data['mcp_context']['session_info'] = {
        "session_id": session_id,
        "initialized_at": datetime.now().isoformat(),
        "mcp_memories": mcp_memories or [],
        "status": "active"
    }
    
    # プロジェクト分析データの統合
    if project_analysis_data:
        data['mcp_context']['serena_analysis'] = {
            "project_structure": project_analysis_data.get("project_structure", {}),
            "symbols_discovered": project_analysis_data.get("symbols_count", 0),
            "architectural_patterns": project_analysis_data.get("patterns", []),
            "analysis_timestamp": datetime.now().isoformat()
        }
    
    save_use_case_json(json_path, data)
    return data


def update_design_rationale(
    json_path: str,
    decision_key: str,
    rationale: str,
    alternatives_considered: Optional[List[str]] = None,
    decision_maker: str = "mcp_enhanced"
) -> None:
    """
    設計判断の根拠をMCPコンテキストに記録
    
    Args:
        json_path: 更新対象のJSONファイルパス
        decision_key: 判断のキー識別子
        rationale: 判断の根拠
        alternatives_considered: 検討された代替案のリスト
        decision_maker: 判断者（mcp_enhanced等）
    """
    data = load_use_case_json(json_path)
    
    if 'mcp_context' not in data:
        data['mcp_context'] = {"design_rationale": {}}
    
    if 'design_rationale' not in data['mcp_context']:
        data['mcp_context']['design_rationale'] = {}
    
    data['mcp_context']['design_rationale'][decision_key] = {
        "rationale": rationale,
        "alternatives_considered": alternatives_considered or [],
        "decision_maker": decision_maker,
        "decided_at": datetime.now().isoformat()
    }
    
    save_use_case_json(json_path, data)


def add_learning_outcome(
    json_path: str,
    learning_type: str,
    content: str,
    source: str = "mcp_analysis",
    confidence: float = 0.8
) -> None:
    """
    MCPから得られた学習内容をコンテキストに追加
    
    Args:
        json_path: 更新対象のJSONファイルパス
        learning_type: 学習の種類（pattern, antipattern, best_practice等）
        content: 学習内容
        source: 学習の出典（serena_analysis, context7_docs等）
        confidence: 信頼度（0.0-1.0）
    """
    data = load_use_case_json(json_path)
    
    if 'mcp_context' not in data:
        data['mcp_context'] = {"learning_outcomes": []}
    
    if 'learning_outcomes' not in data['mcp_context']:
        data['mcp_context']['learning_outcomes'] = []
    
    learning_outcome = {
        "type": learning_type,
        "content": content,
        "source": source,
        "confidence": confidence,
        "learned_at": datetime.now().isoformat()
    }
    
    data['mcp_context']['learning_outcomes'].append(learning_outcome)
    
    save_use_case_json(json_path, data)


def update_context7_cache(
    json_path: str,
    library_id: str,
    documentation_data: Dict[str, Any],
    cache_expiry_hours: int = 24
) -> None:
    """
    Context7から取得したドキュメントをキャッシュ
    
    Args:
        json_path: 更新対象のJSONファイルパス
        library_id: Context7ライブラリID
        documentation_data: ドキュメントデータ
        cache_expiry_hours: キャッシュ有効期限（時間）
    """
    data = load_use_case_json(json_path)
    
    if 'mcp_context' not in data:
        data['mcp_context'] = {"context7_cache": {}}
    
    if 'context7_cache' not in data['mcp_context']:
        data['mcp_context']['context7_cache'] = {}
    
    from datetime import timedelta
    expiry_time = datetime.now() + timedelta(hours=cache_expiry_hours)
    
    data['mcp_context']['context7_cache'][library_id] = {
        "documentation": documentation_data,
        "cached_at": datetime.now().isoformat(),
        "expires_at": expiry_time.isoformat()
    }
    
    save_use_case_json(json_path, data)


def get_mcp_context_summary(json_path: str) -> Dict[str, Any]:
    """
    MCPコンテキストの概要を取得
    
    Args:
        json_path: JSONファイルパス
        
    Returns:
        MCPコンテキストの概要
    """
    data = load_use_case_json(json_path)
    mcp_context = data.get('mcp_context', {})
    
    summary = {
        "session_active": mcp_context.get('session_info', {}).get('status') == 'active',
        "session_id": mcp_context.get('session_info', {}).get('session_id'),
        "serena_symbols_count": mcp_context.get('serena_analysis', {}).get('symbols_discovered', 0),
        "design_decisions_count": len(mcp_context.get('design_rationale', {})),
        "learning_outcomes_count": len(mcp_context.get('learning_outcomes', [])),
        "context7_cache_count": len(mcp_context.get('context7_cache', {})),
        "last_updated": data.get('metadata', {}).get('updated_at')
    }
    
    return summary


def integrate_mcp_enhanced_execution(
    json_path: str,
    command_name: str,
    mcp_insights: Dict[str, Any],
    enhanced_outputs: Optional[List[str]] = None
) -> None:
    """
    MCP強化版コマンド実行時の追加情報を統合
    
    Args:
        json_path: 更新対象のJSONファイルパス
        command_name: 実行されたコマンド名
        mcp_insights: MCPから得られた洞察
        enhanced_outputs: 強化版で追加生成されたファイル
    """
    # 通常の実行履歴更新
    update_execution_history(
        json_path=json_path,
        command_name=command_name,
        status="success",
        files_affected=enhanced_outputs
    )
    
    # MCP固有の洞察を記録
    data = load_use_case_json(json_path)
    
    if 'mcp_context' not in data:
        data['mcp_context'] = {}
    
    if 'enhanced_executions' not in data['mcp_context']:
        data['mcp_context']['enhanced_executions'] = []
    
    enhanced_execution = {
        "command": command_name,
        "executed_at": datetime.now().isoformat(),
        "mcp_insights": mcp_insights,
        "enhanced_outputs": enhanced_outputs or []
    }
    
    data['mcp_context']['enhanced_executions'].append(enhanced_execution)
    
    save_use_case_json(json_path, data)


def create_session_checkpoint_data(json_path: str) -> Dict[str, Any]:
    """
    セッションチェックポイント用のデータを抽出
    
    Args:
        json_path: JSONファイルパス
        
    Returns:
        チェックポイント用のデータ
    """
    data = load_use_case_json(json_path)
    
    checkpoint_data = {
        "metadata": data.get('metadata', {}),
        "execution_history": data.get('execution_history', {}),
        "mcp_context": data.get('mcp_context', {}),
        "domain_model": data.get('domain_model', {}),
        "scenarios": data.get('scenarios', {}),
        "checkpoint_created_at": datetime.now().isoformat()
    }
    
    return checkpoint_data


def restore_from_checkpoint_data(
    json_path: str,
    checkpoint_data: Dict[str, Any]
) -> None:
    """
    チェックポイントデータからセッション状態を復元
    
    Args:
        json_path: 復元先のJSONファイルパス
        checkpoint_data: チェックポイントデータ
    """
    # チェックポイント作成時点の状態を復元
    restored_data = {
        "metadata": checkpoint_data.get('metadata', {}),
        "execution_history": checkpoint_data.get('execution_history', {}),
        "mcp_context": checkpoint_data.get('mcp_context', {}),
        "domain_model": checkpoint_data.get('domain_model', {}),
        "scenarios": checkpoint_data.get('scenarios', {})
    }
    
    # 復元時のメタデータを追加
    restored_data['metadata']['restored_at'] = datetime.now().isoformat()
    restored_data['metadata']['restored_from_checkpoint'] = checkpoint_data.get('checkpoint_created_at')
    
    save_use_case_json(json_path, restored_data)