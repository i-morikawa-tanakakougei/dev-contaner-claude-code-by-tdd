# TDD/DDD/レイヤードアーキテクチャ コマンド

このディレクトリには、テスト駆動開発（TDD）、ドメイン駆動設計（DDD）、レイヤードアーキテクチャを使用して機能を実装するためのカスタムコマンドが含まれています。

## 開発プロセス: ビジョンからチケット作成フロー（オプション 3）

このプロジェクトは**「コアシナリオを事前に作成し、スプリント中に追加・拡張する」**アプローチを採用しています。

### 全体のフロー

- 初期フェーズ
  - 00: ビジョン定義とコアシナリオ作成
  - 01: プロジェクト構造初期化
  - 02: スプリント計画とチケット作成
- スプリント実行フェーズ
  - 03-09: ユースケース仕様 → ドメイン設計 → TDD 実装（RED→GREEN） → 各レイヤー実装
  - 10: 全テスト実行
  - 11: リファクタリング（REFACTOR）
- シナリオ進化・レビューフェーズ
  - 12: シナリオ進化（スプリントフィードバックに基づく）
  - 13: イシューレビュー実施
  - 14: フィードバック反映
  - 15: PR 作成とイシュークローズ

### 初期フェーズコマンド

1. **`/create-vision`** - プロジェクトビジョンとコアシナリオを定義（80%カバレッジ）
2. **`/sprint-planning <sprint-number>`** - コアシナリオからスプリントを計画しチケットを作成
3. **`/init-project-structure`** - プロジェクト構造を初期化

### スプリント実行コマンド

4. **`/create-use-case <issue-number>`** - イシューから Given-When-Then 仕様を作成
5. **`/domain-modeling <issue-number>`** - ドメインモデルを設計
6. **`/create-tests <issue-number>`** - TDD テストを作成（RED フェーズ）
7. **`/implement-domain <issue-number>`** - ドメイン層を実装（GREEN フェーズ）
8. **`/implement-usecase <issue-number>`** - アプリケーション層を実装
9. **`/implement-infra <issue-number>`** - インフラストラクチャ層を実装
10. **`/implement-presentation <issue-number>`** - プレゼンテーション層を実装
11. **`/refactor <issue-number>`** - コードをリファクタリング（REFACTOR フェーズ）

### シナリオ進化コマンド

12. **`/evolve-scenarios <feature-name>`** - スプリントフィードバックに基づいてシナリオを追加/拡張
13. **`/run-all-tests <issue-number>`** - すべてのテストを実行しレポートを生成

## 共通ガイドライン

### GitHub イシューを参照する場合:

- 常に最新のコメントを古いコメントや元のイシュー説明より優先する
- イシュー内容と新しいコメントの間に矛盾がある場合は、新しいコメントを優先する
- `gh issue view <issue-number>`を使用して、すべてのコメントを含む完全なイシュー詳細を取得する

### 出力言語:

- コマンド指示は英語
- ユーザー向け出力（仕様、設計書、エラーメッセージ）は日本語で行う必要があります

### ファイル組織:

- ビジョンドキュメント: `docs/vision/`
- コアシナリオ: `docs/use_cases/core/`
- ユースケース仕様: `docs/use_cases/`
- 進化シナリオ: `docs/use_cases/evolved/`
- スプリント計画: `docs/sprints/`
- ドメインモデル: `docs/domain/`
- テスト計画: `docs/test_plan/`
- テストレポート: `docs/test_report/`

## 使用例

### プロジェクト初期化

```bash
# ビジョンとコアシナリオを定義
/create-vision

# 最初のスプリントを計画
/sprint-planning 1

# プロジェクト構造を初期化
/init-project-structure
```

### スプリント実行

```bash
# スプリント計画からのGitHubイシューで開始
/create-use-case 123

# TDD/DDDワークフローに従う
/domain-modeling 123
/create-tests 123
/implement-domain 123
/implement-usecase 123
/implement-infra 123
/implement-presentation 123
/refactor 123
/run-all-tests 123
```

### シナリオ進化（スプリント中）

```bash
# 新しい要件が出現したとき
/evolve-scenarios cart-management

# 新しいイシューで続行
/create-tests 456
# ... 実装を続ける
```

## 主要な原則

- **ビジョンの維持**: 常に全体的なビジョンを念頭に置く
- **コアシナリオの選択**: 主要なユースケースの 80%カバレッジに焦点を当てる
- **漸進的拡張**: エッジケースは後のスプリントで追加
- **チケット粒度**: 1 シナリオ = 1 チケット（ベースラインとして）
- **継続的改善**: 各スプリントで仕様をレビュー
