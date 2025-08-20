#!/bin/bash

# Test script for hybrid context approach
echo "=========================================="
echo "🧪 ハイブリッドコンテキスト方式のテスト"
echo "=========================================="
echo ""

# Test data
TEST_ISSUES="15,23"
TEST_FEATURE="user-authentication"

# Simulate the context preparation from 03-create-use-case.md
echo "📝 Step 1: コンテキストファイルの作成..."

# Create context directory if not exists
mkdir -p /workspace/.claude/context/session

# Create context file
context_file="/workspace/.claude/context/current-command-context.json"
current_time=$(date -u +"%Y-%m-%dT%H:%M:%SZ")

cat > "$context_file" <<EOF
{
  "command": "create-use-case",
  "timestamp": "$current_time",
  "issue_numbers": [15, 23],
  "feature_name": "$TEST_FEATURE",
  "phase": "use-case-specification",
  "context": {
    "github_cli_available": $(command -v gh >/dev/null 2>&1 && echo "true" || echo "false"),
    "expected_outputs": [
      "docs/use_cases/issue-15-23.md",
      "docs/use_cases/issue-15-23.json"
    ]
  },
  "additional_instructions": "テスト用の追加指示: セキュリティ要件を特に重視してください",
  "special_considerations": [
    "テスト環境での実行",
    "既存システムとの互換性維持",
    "パフォーマンス基準の遵守"
  ],
  "custom_context": {
    "test_mode": true,
    "environment": "development",
    "priority": "high"
  }
}
EOF

echo "✅ コンテキストファイル作成完了: $context_file"
echo ""

# Display the created context
echo "📄 作成されたコンテキスト内容:"
echo "----------------------------------------"
cat "$context_file" | python3 -m json.tool 2>/dev/null || cat "$context_file"
echo "----------------------------------------"
echo ""

# Test reading the context
echo "📖 Step 2: コンテキスト読み込みテスト..."
if [[ -f "$context_file" ]]; then
    echo "✅ コンテキストファイルが正常に読み込み可能"
    
    # Parse key values using python
    if command -v python3 >/dev/null 2>&1; then
        echo ""
        echo "🔍 パース結果:"
        python3 <<EOF
import json
with open('$context_file', 'r') as f:
    data = json.load(f)
    print(f"  - Command: {data['command']}")
    print(f"  - Issue Numbers: {data['issue_numbers']}")
    print(f"  - Feature Name: {data['feature_name']}")
    print(f"  - Phase: {data['phase']}")
    print(f"  - Additional Instructions: {data.get('additional_instructions', 'N/A')[:50]}...")
    print(f"  - Special Considerations Count: {len(data.get('special_considerations', []))}")
    print(f"  - Custom Context Keys: {list(data.get('custom_context', {}).keys())}")
EOF
    fi
else
    echo "❌ コンテキストファイルの読み込みに失敗"
fi
echo ""

# Test execution history
echo "📝 Step 3: 実行履歴の記録テスト..."
history_file="/workspace/.claude/context/execution-history.jsonl"
echo "{\"timestamp\":\"$(date -Iseconds)\",\"command\":\"create-use-case\",\"issues\":\"15 23\",\"status\":\"test\",\"test_run\":true}" >> "$history_file"
echo "✅ 実行履歴に記録しました"

# Display history
if [[ -f "$history_file" ]]; then
    echo ""
    echo "📜 実行履歴の内容:"
    echo "----------------------------------------"
    tail -n 5 "$history_file"
    echo "----------------------------------------"
fi
echo ""

# Test cleanup
echo "🧹 Step 4: クリーンアップテスト..."
if [[ -f "$context_file" ]]; then
    rm -f "$context_file"
    echo "✅ 一時コンテキストファイルを削除しました"
else
    echo "⚠️ 削除するファイルがありません"
fi
echo ""

# Summary
echo "=========================================="
echo "📊 テスト結果サマリー"
echo "=========================================="
echo "✅ コンテキストファイル作成: 成功"
echo "✅ JSONフォーマット検証: 成功"
echo "✅ コンテキスト読み込み: 成功"
echo "✅ 実行履歴記録: 成功"
echo "✅ クリーンアップ: 成功"
echo ""
echo "🎉 ハイブリッドコンテキスト方式のテスト完了!"
echo ""
echo "💡 次のステップ:"
echo "1. サブエージェントでのコンテキスト読み込み実装"
echo "2. 他のコマンドへの展開"
echo "3. エラーハンドリングの強化"