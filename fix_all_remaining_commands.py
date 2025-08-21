#!/usr/bin/env python3
"""
Batch fix AGENT_CALL sections in ALL remaining TDD/DDD/Layered commands
"""

import os
import re

# All remaining commands
COMMANDS = [
    "00.5-review-vision",
    "01-init-project-structure", 
    "02.5-review-sprint-plan",
    "08-implement-infra",
    "09-implement-presentation",
    "10-run-all-tests",
    "13-review-issue",
    "14-apply-feedback",
    "15-create-pr",
    "16-use-case-status"
]

BASE_PATH = "/workspace/.claude/commands/tdd-ddd-layered"

def fix_agent_call(content, command_name):
    """Replace AGENT_CALL comment block with actual Task tool call"""
    
    # Pattern to match the AGENT_CALL block
    pattern = r"cat <<'AGENT_CALL'.*?AGENT_CALL"
    
    # Replacement template
    replacement = f'''# Task tool execution with comprehensive prompt
   task_prompt="タスクを実行してください。

## コンテキスト情報の取得
1. 一時コンテキスト（プロジェクト情報）:
   - /workspace/.claude/context/current-command-context.json を読み込み

2. プロジェクト状況の確認:
   - 必要な文書やファイルを確認
   - 既存の実装や設計を参照

## 実行タスク
[{command_name}固有のタスクを実行]

## 重要: 標準化出力形式の遵守
レポートは必ず以下の構造化セクションで終了してください：

### 📊 実行サマリー
各Critical Taskの完了状態を✅/❌で明記

### 📋 総合判定
APPROVED/CONDITIONAL_APPROVAL/REJECTED/COMPLETED のいずれかを明記

### 💡 次のステップ
判定に基づく具体的なアクションアイテムを列挙

## 処理完了後
- 実行結果の報告
- 次のステップへの案内"

   # Execute Task tool
   Task \\
     --subagent_type "{command_name}" \\
     --description "Execute {command_name} task" \\
     --prompt "$task_prompt"
   
   agent_exit_code=$?
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"'''
    
    # Replace the AGENT_CALL block
    modified_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    return modified_content

def main():
    print(f"🔧 Fixing AGENT_CALL sections in {len(COMMANDS)} remaining commands...")
    
    success_count = 0
    not_found_count = 0
    no_agent_call_count = 0
    
    for cmd in COMMANDS:
        file_path = f"{BASE_PATH}/{cmd}.md"
        
        if not os.path.exists(file_path):
            print(f"  ❌ File not found: {cmd}.md")
            not_found_count += 1
            continue
            
        try:
            # Read the file
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check if AGENT_CALL exists
            if "AGENT_CALL" not in content:
                print(f"  ⚠️ No AGENT_CALL found in: {cmd}.md")
                no_agent_call_count += 1
                continue
            
            # Fix the AGENT_CALL section
            modified_content = fix_agent_call(content, cmd)
            
            # Write back the modified content
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            
            print(f"  ✅ Successfully processed: {cmd}.md")
            success_count += 1
            
        except Exception as e:
            print(f"  ❌ Failed to process {cmd}.md: {e}")
    
    print("\n🎉 Batch processing completed!")
    print(f"  ✅ Successfully processed: {success_count}")
    print(f"  ⚠️ No AGENT_CALL found: {no_agent_call_count}")
    print(f"  ❌ File not found: {not_found_count}")

if __name__ == "__main__":
    main()