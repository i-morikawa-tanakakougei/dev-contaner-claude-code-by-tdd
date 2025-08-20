# Claude Code サブエージェント コンテキスト受け渡し枠組み設計

**設計日**: 2025-08-19  
**基準テスト**: post-restart-test (SUCCESS)

## 🔍 現状分析

### ✅ 確認済み機能
1. **基本コンテキスト受け渡し**: promptパラメータで完全な情報伝達が可能
2. **サブエージェント認識**: 再起動後に.claude/agents/内のエージェントが自動認識
3. **ツールアクセス**: Read, Write, Grep, LSが正常動作
4. **ファイルシステム**: /workspace全体への完全アクセス

### ❌ 不足機能
1. **永続コンテキスト**: /workspace/.claude/context/ディレクトリ未実装
2. **実行履歴**: エージェント間の引き継ぎ情報記録なし
3. **標準化**: 統一されたコンテキスト受け渡し規約なし

## 🏗️ 解決枠組み設計

### Phase 1: 基本コンテキスト受け渡し機能

#### 1.1 promptパラメータ活用方式（即効性）
**現在利用可能**: Task tool の prompt パラメータで直接情報伝達

```bash
# カスタムコマンド内での実装例
/implement-usecase 15,23 user-auth

# 実際のサブエージェント呼び出し
Task subagent_type="07-implement-usecase" \
     description="Application layer implementation" \
     prompt="
     コンテキスト:
     - issue_numbers: [15, 23]
     - feature_name: user-auth
     - phase: application-layer
     - prerequisites: domain-layer-completed
     
     実行タスク:
     - ドメインロジック調整のユースケース実装
     - DTOクラスとアプリケーションサービスの作成
     - テスト実行による検証
     "
```

#### 1.2 構造化コンテキスト標準（推奨・柔軟性強化版）
**標準コンテキスト形式**:
```json
{
  "command": "implement-usecase",
  "timestamp": "2025-08-19T08:00:00Z",
  "issue_numbers": [15, 23],
  "feature_name": "user-authentication",
  "phase": "application-layer",
  "context": {
    "previous_command": "implement-domain",
    "prerequisites_met": true,
    "expected_outputs": ["src/application/", "tests/application/"]
  },
  "additional_instructions": "ユーザー認証機能では、既存のJWTライブラリを使用し、セキュリティベストプラクティスに従ってください。特に、トークンの有効期限とリフレッシュトークンの実装に注意。",
  "special_considerations": [
    "既存のユーザーモデルとの互換性維持",
    "マルチファクタ認証の将来的な追加を考慮した設計",
    "パフォーマンス要件: 認証処理は100ms以内"
  ],
  "custom_context": {
    "business_rules": "パスワードは最低8文字、大文字小文字数字を含む",
    "technical_constraints": "PostgreSQL 14以上が必要",
    "integration_points": "外部認証プロバイダー（Google OAuth）との連携"
  }
}
```

**柔軟性のポイント**:
- `additional_instructions`: 自由形式のテキストで特別な指示を記載
- `special_considerations`: 配列形式で複数の考慮事項を列挙
- `custom_context`: プロジェクト固有の任意のキー・バリューペア

### Phase 2: 永続コンテキスト機能（堅牢性向上）

#### 2.1 コンテキストディレクトリ構造（既存TDD/DDD構造と統合）

**既存構造を尊重した統合アプローチ:**

```
# 既存のTDD/DDDメタデータ構造（維持）
docs/use_cases/
├── core/index.md              # コアシナリオ定義（既存）
├── index.md                    # 実装状況管理（既存）
└── issue-X-Y.json             # 各イシューのメタデータ（既存・永続的）

# 新規：エージェント間コンテキスト共有専用
/workspace/.claude/context/
├── current-command-context.json    # 現在実行中のコマンドコンテキスト（一時的）
├── execution-history.jsonl         # エージェント実行履歴（新規価値）
└── session/                        # セッション固有の一時データ
    └── active-issues.json          # 現在作業中のイシューリスト
```

**役割分担の明確化:**
- **`docs/use_cases/issue-X-Y.json`**: 
  - TDD/DDDフェーズ追跡（RED/GREEN/REFACTOR）
  - 永続的なプロジェクト進捗管理
  - Given-When-Thenシナリオとの関連付け
  
- **`.claude/context/current-command-context.json`**: 
  - カスタムコマンド→サブエージェントの引数伝達
  - 一時的な実行パラメータ（issue_numbers, feature_name等）
  - コマンド実行後に削除可能

- **統合方針**: 両者を相互参照して完全な情報を構築

#### 2.2 コンテキスト受け渡しパターン

**Pattern A: ファイルベース受け渡し**
```bash
# 1. カスタムコマンドでコンテキスト保存
echo '{"issue_numbers":[15,23],"feature":"user-auth"}' > /workspace/.claude/context/current-command-context.json

# 2. サブエージェント呼び出し
Task subagent_type="07-implement-usecase" prompt="
コンテキストファイルを読み込んで作業を実行してください:
- ファイル: /workspace/.claude/context/current-command-context.json
- 必ず最初にこのファイルを読み込み、コンテキスト情報を取得
"

# 3. サブエージェント側でコンテキスト読み込み
# Read /workspace/.claude/context/current-command-context.json
```

**Pattern B: ハイブリッド方式（推奨・既存構造統合版）**
```bash
# promptパラメータ + 既存TDD/DDDメタデータ + 新規コンテキスト の併用
Task subagent_type="07-implement-usecase" \
     description="Application layer for issues 15,23" \
     prompt="
     直接コンテキスト: issue_numbers=[15,23], feature=user-auth
     
     参照すべきファイル:
     1. 一時コンテキスト:
        - /workspace/.claude/context/current-command-context.json
     
     2. 既存TDD/DDDメタデータ（永続的）:
        - docs/use_cases/issue-15-*.json
        - docs/use_cases/issue-23-*.json
        - docs/use_cases/index.md (実装状況確認)
     
     処理フロー:
     1. current-command-context.jsonから引数情報を取得
     2. docs/use_cases/issue-X-Y.jsonから現在のフェーズを確認
     3. 両方の情報を統合して適切な処理を実行
     4. 処理結果をdocs/use_cases/issue-X-Y.jsonに反映
     "
```

### Phase 3: エージェント統合標準化

#### 3.1 統一呼び出しパターン
全てのTDD/DDD/レイヤードアーキテクチャコマンド（00-16）に以下を適用:

```bash
# 1. Pre-execution Validation（引数解析とコンテキスト準備）
# 2. Context Preparation（コンテキストファイル作成）
# 3. Execute Agent（統一されたTask tool呼び出し）
# 4. Agent Result Verification（結果検証とコンテキスト更新）
```

#### 3.2 エージェント側標準対応
各専門エージェントに以下を追加:

```markdown
## コンテキスト処理標準

### 必須アクション
1. **コンテキスト読み込み**: `/workspace/.claude/context/current-command-context.json`を最初に読み込み
2. **パラメータ統合**: promptパラメータとファイルコンテキストを統合
3. **実行履歴更新**: 処理結果を`/workspace/.claude/context/execution-history.jsonl`に追記

### コンテキスト処理コード例
```bash
# 1. コンテキストファイル読み込み
if [[ -f "/workspace/.claude/context/current-command-context.json" ]]; then
    context_data=$(Read /workspace/.claude/context/current-command-context.json)
fi

# 2. パラメータ統合と作業実行
# ...

# 3. 実行結果記録
echo "{\"timestamp\":\"$(date -Iseconds)\",\"agent\":\"07-implement-usecase\",\"status\":\"completed\"}" >> /workspace/.claude/context/execution-history.jsonl
```

## 🚀 実装ロードマップ

### Step 1: 即効対応（今すぐ実装可能）
1. **コンテキストディレクトリ作成**: `/workspace/.claude/context/`
2. **1つのコマンドで試験実装**: 03-create-use-case.mdでハイブリッド方式を実装
3. **動作検証**: test-context-agentでの検証テスト実行

### Step 2: 段階展開（1-2コマンド毎）
1. **重要コマンドから順次適用**: 05-create-tests, 07-implement-usecase
2. **専門エージェントの更新**: コンテキスト処理標準の追加
3. **動作検証**: 各段階での動作確認

### Step 3: 全体統合（最終段階）
1. **全コマンド（00-16）への適用**: 統一パターンでの実装
2. **テスト自動化**: 定期的な回帰テスト
3. **ドキュメント化**: 実装ガイドとベストプラクティス

## 💡 推奨実装優先順位

### 🔥 緊急度：高
- [ ] コンテキストディレクトリ作成
- [ ] 1コマンドでの試験実装（03-create-use-case）
- [ ] promptパラメータでの基本コンテキスト受け渡し確立

### ⚡ 緊急度：中
- [ ] ファイルベース永続コンテキスト機能
- [ ] 重要コマンド（3-5個）への適用
- [ ] エージェント側標準処理の実装

### 📋 緊急度：低
- [ ] 全コマンドへの適用
- [ ] 実行履歴とトレーサビリティ機能
- [ ] 自動テストとモニタリング

---

**次のアクション**: Step 1の実装から開始し、段階的に機能を拡張していく