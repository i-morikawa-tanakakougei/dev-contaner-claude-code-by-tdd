# タスクメタデータ駆動型確認システム 使用方法・運用ガイド

## 📖 概要

このシステムは、TDD/DDD/Layered Architecture 開発プロセスにおいて、各コマンドの実行結果を自動的に検証し、品質を保証するための統合システムです。

### 🎯 主要機能

- **メタデータ駆動検証**: JSON ファイルに基づく動的なタスク確認
- **Critical Tasks 確認**: 最重要項目の確実な検証
- **自動再試行機能**: 問題検出時の改善指示付き再実行
- **標準化出力**: サブエージェントの統一された構造化レポート
- **包括的テスト自動化**: 継続的品質保証

## 🚀 クイックスタート

### 1. システム状態確認

```bash
# 基本機能テスト
.claude/commands/tdd-ddd-layered/test-automation-system.sh basic

# 全機能テスト
.claude/commands/tdd-ddd-layered/test-automation-system.sh all
```

### 2. CI/CD 確認

```bash
# 開発環境でクイックチェック
.claude/commands/tdd-ddd-layered/ci-cd-verification.sh dev quick

# 本番環境でフルチェック
.claude/commands/tdd-ddd-layered/ci-cd-verification.sh prod full
```

### 3. コマンド実行（自動検証付き）

```bash
# ドメイン設計レビュー（自動検証あり）
/review-domain-design 15

# テスト設計レビュー（自動検証あり）
/review-test-design 15

# テスト結果レビュー（自動検証あり）
/review-test-results 15
```

## 🔧 システム構成

### ライブラリ構造

```
.claude/commands/tdd-ddd-layered/
├── _task_verification.sh          # 共通検証ライブラリ
├── task-definitions/               # メタデータ定義
│   ├── 04.5-review-domain-design.json
│   ├── 05.5-review-test-design.json
│   ├── 10.5-review-test-results.json
│   └── 12-evolve-scenarios.json
├── test-automation-system.sh      # テスト自動化
├── ci-cd-verification.sh          # CI/CD検証
└── [各コマンド].md                 # 拡張済みコマンド
```

### サブエージェント拡張

```
.claude/agents/
├── 04.5-review-domain-design.md   # 標準化出力対応
├── 05.5-review-test-design.md     # 標準化出力対応
└── 10.5-review-test-results.md    # 標準化出力対応
```

## 📋 使用方法

### ライブラリの使用方法

#### 基本的な使用パターン

```bash
# コマンドファイル内での使用例
source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"

# 1. 基本検証
if basic_verification "$report_file" "command-name"; then
    echo "✅ 基本検証完了"
fi

# 2. Critical Tasks確認
if verify_critical_tasks "04.5-review-domain-design" "$report_file"; then
    echo "✅ Critical tasks確認完了"
fi

# 3. 検証結果表示
show_verification_results "command-name"

# 4. 再試行コンテキスト準備
prepare_retry_context "command-name" "1" "問題1" "問題2"
```

#### メタデータ駆動確認

```bash
# メタデータ読み込み
load_task_metadata "04.5-review-domain-design"

# 自動的に以下が設定される:
# - critical_tasks[]
# - critical_patterns[]
# - success_indicators[]
# - failure_indicators[]
```

### メタデータファイルの構造

```json
{
  "command": "04.5-review-domain-design",
  "description": "Domain model design review",
  "phase": "domain-design-review",
  "critical_tasks": [
    "ddd_compliance_check",
    "aggregate_boundary_validation",
    "business_rules_placement"
  ],
  "output_requirements": {
    "critical_patterns": [
      "✅.*DDD準拠性",
      "✅.*集約境界",
      "(APPROVED|CONDITIONAL_APPROVAL|REJECTED)"
    ],
    "success_indicators": ["ドメイン設計レビュー完了", "✅.*適切"],
    "failure_indicators": ["DDD違反", "設計修正が必要"]
  },
  "retry_context": {
    "focus_areas": ["DDD compliance validation", "Aggregate boundary design"],
    "common_issues": [
      "Direct entity references across aggregates",
      "Business rules in wrong layer"
    ]
  }
}
```

## 🎯 運用ガイド

### 日常運用

#### 開発者向け運用

```bash
# 毎日の開発開始時
.claude/commands/tdd-ddd-layered/test-automation-system.sh basic

# コマンド実行後の確認
# 自動的に検証が実行される - 追加作業不要

# 問題が検出された場合
# システムが自動的に再実行指示を提供
```

#### チームリーダー向け運用

```bash
# 週次品質確認
.claude/commands/tdd-ddd-layered/ci-cd-verification.sh dev full

# スプリント開始前確認
.claude/commands/tdd-ddd-layered/test-automation-system.sh integration

# 月次セキュリティチェック
.claude/commands/tdd-ddd-layered/ci-cd-verification.sh prod security
```

### トラブルシューティング

#### よくある問題と解決方法

**Q1: Critical tasks 確認で問題が検出される**

```bash
# 問題確認
grep -n "verification_issues" /workspace/.claude/test-automation/test-automation.log

# メタデータ確認
jq '.critical_patterns' .claude/commands/tdd-ddd-layered/task-definitions/[command].json

# 再実行
/[command-name] [parameters]
```

**Q2: サブエージェントの出力形式が不適切**

- サブエージェントファイルで `STANDARDIZED OUTPUT REQUIREMENTS` セクションを確認
- 以下の構造が含まれているか確認:
  - `📊 実行サマリー`
  - `📋 総合判定`
  - `💡 次のステップ`

**Q3: メタデータファイルが見つからない**

```bash
# メタデータディレクトリ確認
ls .claude/commands/tdd-ddd-layered/task-definitions/

# 新しいメタデータファイル作成（テンプレートベース）
cp .claude/commands/tdd-ddd-layered/task-definitions/04.5-review-domain-design.json \
   .claude/commands/tdd-ddd-layered/task-definitions/[new-command].json
```

### パフォーマンス最適化

#### 高速化のヒント

1. **メタデータキャッシュ**: 同じコマンドの連続実行では自動キャッシュ
2. **並列実行**: 複数のテスト実行時は並列実行可能
3. **選択的テスト**: 必要な部分のみテスト実行

```bash
# 並列テスト実行例
.claude/commands/tdd-ddd-layered/test-automation-system.sh basic &
.claude/commands/tdd-ddd-layered/ci-cd-verification.sh dev quick &
wait
```

## 📊 監視とメトリクス

### 成功指標

#### システムレベル

- **検証成功率**: 95%以上
- **自動修正率**: 80%以上
- **平均確認時間**: 2 秒以内

#### 開発プロセス

- **エラー検出率**: 早期発見 30%向上
- **再作業時間**: 50%削減
- **品質指標**: クリティカル問題 0 件

### ログとレポート

#### ログファイル

```bash
# テスト自動化ログ
/workspace/.claude/test-automation/test-automation.log

# CI/CDログ
/workspace/.claude/ci-reports/ci-cd-[timestamp].log
```

#### レポートファイル

```bash
# テストレポート
/workspace/.claude/test-automation/reports/

# CI/CDレポート
/workspace/.claude/ci-reports/
```

## 🔄 拡張方法

### 新しいコマンドの追加

1. **メタデータファイル作成**

```bash
# テンプレートをコピー
cp .claude/commands/tdd-ddd-layered/task-definitions/04.5-review-domain-design.json \
   .claude/commands/tdd-ddd-layered/task-definitions/[new-command].json

# 内容を編集
vim .claude/commands/tdd-ddd-layered/task-definitions/[new-command].json
```

2. **コマンドファイル更新**

```bash
# Agent Result Verification セクションに追加
source "$(dirname "${BASH_SOURCE[0]}")/_task_verification.sh"
verify_critical_tasks "[new-command]" "$latest_report"
show_verification_results "[new-command]"
```

3. **サブエージェント更新**（該当する場合）

```markdown
## 🎯 **STANDARDIZED OUTPUT REQUIREMENTS**

### **📊 実行サマリー**

### **📋 総合判定**

### **💡 次のステップ**
```

### カスタムメタデータの追加

```json
{
  "command": "custom-command",
  "custom_fields": {
    "specific_validation": true,
    "performance_threshold": 1000,
    "business_rules": ["rule1", "rule2"]
  }
}
```

## 🛡️ セキュリティとベストプラクティス

### セキュリティガイドライン

1. **機密情報の除外**: メタデータファイルに機密情報を含めない
2. **実行権限**: 必要最小限の実行権限のみ付与
3. **ログのサニタイゼ**: ログファイルから機密情報を除外

### ベストプラクティス

1. **定期的なメタデータ更新**: 要件変更に応じたメタデータの更新
2. **テストの自動実行**: CI/CD パイプラインへの統合
3. **チーム共有**: メトリクスとレポートの共有
4. **継続的改善**: 定期的な効果測定と改善

## 🤝 サポートとコミュニティ

### 問題報告

- システムの問題や改善提案
- パフォーマンス問題の報告
- 新機能のリクエスト

### ドキュメント更新

このガイドは継続的に更新されます。最新版は常にプロジェクトルートで確認してください。

---

**最終更新**: 2025-08-20  
**バージョン**: 1.0.0  
**次回レビュー**: 2025-09-20
