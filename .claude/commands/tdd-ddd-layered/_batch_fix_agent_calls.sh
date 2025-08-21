#!/bin/bash
#
# Batch fix AGENT_CALL sections in TDD/DDD/Layered commands
# This script replaces AGENT_CALL comment blocks with actual Task tool calls
#

# List of commands to fix
COMMANDS=(
    "00-create-vision"
    "02-sprint-planning"
    "03-create-use-case"
    "04-domain-modeling"
    "05-create-tests"
    "06-implement-domain"
    "07-implement-usecase"
    "11-refactor"
)

echo "🔧 Batch fixing Agent Call sections in ${#COMMANDS[@]} commands..."

for cmd in "${COMMANDS[@]}"; do
    echo "📝 Processing: $cmd.md"
    
    # Create temporary file for processing
    tmp_file="/tmp/${cmd}_temp.md"
    
    # Check if file exists
    if [[ ! -f "/workspace/.claude/commands/tdd-ddd-layered/$cmd.md" ]]; then
        echo "  ❌ File not found: $cmd.md"
        continue
    fi
    
    # Process the file
    sed '
    /cat <<'\''AGENT_CALL'\''/,/AGENT_CALL/{
        s/cat <<'\''AGENT_CALL'\''/# Task tool execution with comprehensive prompt\
   task_prompt="タスクを実行してください。\
\
## コンテキスト情報の取得\
1. 一時コンテキスト（プロジェクト情報）:\
   - \/workspace\/.claude\/context\/current-command-context.json を読み込み\
\
2. プロジェクト状況の確認:\
   - 必要な文書やファイルを確認\
   - 既存の実装や設計を参照\
\
## 実行タスク\
[コマンド固有のタスクを実行]\
\
## 重要: 標準化出力形式の遵守\
レポートは必ず以下の構造化セクションで終了してください：\
\
### 📊 実行サマリー\
各Critical Taskの完了状態を✅\/❌で明記\
\
### 📋 総合判定\
APPROVED\/CONDITIONAL_APPROVAL\/REJECTED\/COMPLETED のいずれかを明記\
\
### 💡 次のステップ\
判定に基づく具体的なアクションアイテムを列挙\
\
## 処理完了後\
- 実行結果の報告\
- 次のステップへの案内"\
\
   # Execute Task tool\
   Task \\\
     --subagent_type "'$cmd'" \\\
     --description "Execute '$cmd' task" \\\
     --prompt "$task_prompt"\
   \
   agent_exit_code=$?\
   echo "✅ 専用エージェント実行完了 (終了コード: $agent_exit_code)"/
        /AGENT_CALL/d
    }
    ' "/workspace/.claude/commands/tdd-ddd-layered/$cmd.md" > "$tmp_file"
    
    # Replace original file if processing was successful
    if [[ -s "$tmp_file" ]]; then
        mv "$tmp_file" "/workspace/.claude/commands/tdd-ddd-layered/$cmd.md"
        echo "  ✅ Successfully processed: $cmd.md"
    else
        echo "  ❌ Failed to process: $cmd.md"
        rm -f "$tmp_file"
    fi
done

echo "🎉 Batch processing completed!"
echo "Modified files:"
for cmd in "${COMMANDS[@]}"; do
    echo "  - ${cmd}.md"
done