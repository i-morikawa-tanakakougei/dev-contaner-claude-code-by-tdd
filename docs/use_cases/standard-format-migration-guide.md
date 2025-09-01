# ユースケースJSON標準フォーマット移行ガイド

## 概要
このドキュメントは、既存のユースケースJSONファイルを新しい標準フォーマットに移行するためのガイドです。

## 標準フォーマットの主要な特徴

### 1. 実行履歴の追跡 (`execution_history`)
カスタムコマンドの実行状況を完全に追跡できる新しいセクション：

```json
"execution_history": {
  "tdd_phases": {
    "RED": {
      "status": "completed",
      "completed_at": "2024-01-15T10:30:00Z",
      "command": "/create-tests 2",
      "files_created": ["tests/test_database.py"]
    }
  },
  "commands_executed": [
    {
      "command": "/create-use-case 2",
      "executed_at": "2024-01-15T09:00:00Z",
      "status": "success",
      "duration_ms": 1500,
      "files_affected": ["docs/use_cases/issue-2-postgresql-database-environment.json"]
    }
  ],
  "last_command": "/create-tests 2"
}
```

### 2. 統一された命名規則
- `metadata` （`use_case_metadata`ではない）
- `main_scenarios` （`main_success`ではない）
- `alternative_scenarios` （`alternative_flows`ではない）
- `exception_scenarios` （`exception_flows`ではない）

### 3. ドメインモデル情報の統合 (`domain_model`)
DDD関連の情報を一箇所に集約：
- エンティティ
- 値オブジェクト
- ドメインサービス
- ビジネスルール
- ユビキタス言語

### 4. アーキテクチャ整合性の追跡 (`architecture_alignment`)
レイヤードアーキテクチャの実装状況を追跡

### 5. レビュー履歴 (`review_history`)
各フェーズのレビュー結果を記録

## 移行手順

### Step 1: 既存ファイルのバックアップ
```bash
cp docs/use_cases/issue-1.json docs/use_cases/issue-1.json.backup
cp docs/use_cases/issue-2-postgresql-database-environment.json docs/use_cases/issue-2-postgresql-database-environment.json.backup
```

### Step 2: ファイル名の標準化
```
旧: issue-1.json
新: issue-1-project-structure-initialization.json

旧: issue-2-postgresql-database-environment.json
新: そのまま（既に標準形式）
```

### Step 3: 構造の変換

#### issue-1.jsonの変換ポイント：
- `github_issue`セクションを`metadata`内に統合
- `scenarios`の構造はそのまま維持
- 新規追加：`execution_history`、`architecture_alignment`、`testing_strategy`

#### issue-2-postgresql-database-environment.jsonの変換ポイント：
- `use_case_metadata` → `metadata`に名称変更
- `main_success` → `main_scenarios`
- `alternative_flows` → `alternative_scenarios`
- `exception_flows` → `exception_scenarios`
- 新規追加：`domain_model`、`execution_history`

## カスタムコマンドへの影響

以下のコマンドが新しいフォーマットを使用するように更新が必要：

1. **作成系コマンド**
   - `03-create-use-case`: 新フォーマットでJSONを作成
   - `04-domain-modeling`: `domain_model`セクションを更新
   - `05-create-tests`: `execution_history.tdd_phases.RED`を更新

2. **実装系コマンド**
   - `06-implement-domain`: `execution_history.tdd_phases.GREEN`を更新
   - `07-implement-usecase`: `architecture_alignment.layers.application`を更新
   - `08-implement-infra`: `architecture_alignment.layers.infrastructure`を更新
   - `09-implement-presentation`: `architecture_alignment.layers.presentation`を更新

3. **レビュー系コマンド**
   - `10.5-review-test-results-expert`: `review_history`に結果を追加
   - `13-review-issue`: 全体的な進捗状況を確認

4. **ステータス系コマンド**
   - `16-use-case-status`: `execution_history`から進捗を表示
   - `17-project-status`: 全イシューの実行状況を集計

## 互換性の維持

移行期間中の互換性を保つため：
1. カスタムコマンドは新旧両フォーマットを読み込めるように実装
2. 新規作成は常に新フォーマットを使用
3. 既存ファイルは段階的に移行

## 実行履歴の可視化

新しい`execution_history`により以下が可能に：
- どのコマンドが実行済みか一目で確認
- 各TDDフェーズの完了状況を追跡
- コマンド実行時間とパフォーマンスの分析
- エラー発生時の原因追跡