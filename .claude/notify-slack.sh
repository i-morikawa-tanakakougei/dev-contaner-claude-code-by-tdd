#!/bin/bash

# Slack notification script for Claude Code hooks
# This script sends notifications to Slack when Claude Code events occur

# Debug: Log to file for troubleshooting
DEBUG_LOG="/workspace/.claude/notify-slack.log"
echo "$(date '+%Y-%m-%d %H:%M:%S') - Script executed" >> "$DEBUG_LOG"
echo "Environment variables:" >> "$DEBUG_LOG"
env | grep CLAUDE >> "$DEBUG_LOG" 2>&1

# Load environment variables from .env.dev if it exists
ENV_FILE="/workspace/.env.dev"
if [ -f "$ENV_FILE" ]; then
    echo "Loading environment variables from $ENV_FILE" >> "$DEBUG_LOG"
    # Source the .env.dev file to load environment variables
    set -a  # automatically export all variables
    source "$ENV_FILE"
    set +a  # stop automatically exporting
else
    echo "Warning: $ENV_FILE not found, using environment variables" >> "$DEBUG_LOG"
fi

# Get Slack Webhook URL (from .env.dev or environment variable)
SLACK_WEBHOOK_URL="${SLACK_WEBHOOK_URL}"

# Check if webhook URL is set
if [ -z "$SLACK_WEBHOOK_URL" ]; then
    echo "Error: SLACK_WEBHOOK_URL is not set in $ENV_FILE or environment variables" >> "$DEBUG_LOG"
    exit 1
fi

# Read hook data from stdin (JSON format)
HOOK_DATA=""
if [ -t 0 ]; then
    echo "No stdin data available" >> "$DEBUG_LOG"
    HOOK_TYPE="unknown"
else
    HOOK_DATA=$(cat)
    echo "Hook data from stdin: $HOOK_DATA" >> "$DEBUG_LOG"
    # Extract hook_event_name using jq or basic parsing
    if command -v jq >/dev/null 2>&1; then
        HOOK_TYPE=$(echo "$HOOK_DATA" | jq -r '.hook_event_name // "unknown"')
    else
        # Basic fallback parsing without jq
        HOOK_TYPE=$(echo "$HOOK_DATA" | grep -o '"hook_event_name":"[^"]*"' | cut -d'"' -f4)
        if [ -z "$HOOK_TYPE" ]; then
            HOOK_TYPE="unknown"
        fi
    fi
fi
echo "Hook type: $HOOK_TYPE" >> "$DEBUG_LOG"

# Determine notification type and message based on hook type
case "$HOOK_TYPE" in
    "PreToolUse")
        NOTIFICATION_TYPE="[ツール実行前] Claude Code"
        MESSAGE="Claude Codeがツールを実行しようとしています"
        ;;
    "PostToolUse")
        NOTIFICATION_TYPE="[ツール実行後] Claude Code"
        MESSAGE="Claude Codeがツールの実行を完了しました"
        ;;
    "UserPromptSubmit")
        NOTIFICATION_TYPE="[ユーザー入力] Claude Code"
        MESSAGE="ユーザーがプロンプトを送信しました"
        ;;
    "SessionStart")
        NOTIFICATION_TYPE="[セッション開始] Claude Code"
        MESSAGE="Claude Codeセッションが開始されました"
        ;;
    "SessionEnd")
        NOTIFICATION_TYPE="[セッション終了] Claude Code"
        MESSAGE="Claude Codeセッションが終了しました"
        ;;
    "Notification")
        NOTIFICATION_TYPE="[通知] Claude Code"
        MESSAGE="Claude Codeから通知があります"
        ;;
    "Stop")
        NOTIFICATION_TYPE="[停止] Claude Code"
        MESSAGE="Claude Codeセッションが停止しました"
        ;;
    *)
        NOTIFICATION_TYPE="[イベント] Claude Code"
        MESSAGE="Claude Codeイベントが発生しました (タイプ: $HOOK_TYPE)"
        ;;
esac

# Extract additional information from hook data
ADDITIONAL_INFO=""
if [ -n "$HOOK_DATA" ]; then
    if command -v jq >/dev/null 2>&1; then
        # Extract tool name if available (for PreToolUse/PostToolUse)
        TOOL_NAME=$(echo "$HOOK_DATA" | jq -r '.tool_name // empty')
        if [ -n "$TOOL_NAME" ]; then
            ADDITIONAL_INFO="ツール: $TOOL_NAME"
        fi
        
        # Extract prompt if available (for UserPromptSubmit)
        PROMPT=$(echo "$HOOK_DATA" | jq -r '.prompt // empty' | head -c 100)
        if [ -n "$PROMPT" ]; then
            ADDITIONAL_INFO="プロンプト: ${PROMPT}..."
        fi
        
        # Extract message if available (for Notification)
        HOOK_MESSAGE=$(echo "$HOOK_DATA" | jq -r '.message // empty')
        if [ -n "$HOOK_MESSAGE" ]; then
            ADDITIONAL_INFO="メッセージ: $HOOK_MESSAGE"
        fi
        
        # Extract session_id if available
        SESSION_ID=$(echo "$HOOK_DATA" | jq -r '.session_id // empty')
        if [ -n "$SESSION_ID" ]; then
            if [ -n "$ADDITIONAL_INFO" ]; then
                ADDITIONAL_INFO="$ADDITIONAL_INFO, セッションID: ${SESSION_ID:0:8}"
            else
                ADDITIONAL_INFO="セッションID: ${SESSION_ID:0:8}"
            fi
        fi
    fi
fi

# Include additional context if available
if [ -n "$ADDITIONAL_INFO" ]; then
    MESSAGE="$MESSAGE

詳細: $ADDITIONAL_INFO"
fi

# Add timestamp
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')
MESSAGE="$MESSAGE

時刻: $TIMESTAMP"

# Send notification to Slack using webhook
echo "Sending to Slack: $NOTIFICATION_TYPE" >> "$DEBUG_LOG"
echo "Message: $MESSAGE" >> "$DEBUG_LOG"

# Create formatted message for Slack
FORMATTED_MESSAGE="*$NOTIFICATION_TYPE*

$MESSAGE"

# Create JSON payload for Slack webhook
PAYLOAD=$(cat <<EOF
{
  "text": "$FORMATTED_MESSAGE"
}
EOF
)

echo "Payload: $PAYLOAD" >> "$DEBUG_LOG"

# Send to Slack webhook
CURL_RESPONSE=$(curl -X POST \
     -H "Content-Type: application/json" \
     --data "$PAYLOAD" \
     "$SLACK_WEBHOOK_URL" \
     --silent --show-error 2>&1)

echo "Curl response: $CURL_RESPONSE" >> "$DEBUG_LOG"
echo "Script completed" >> "$DEBUG_LOG"
echo "---" >> "$DEBUG_LOG"

# Exit with success status
exit 0