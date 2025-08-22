# TDD/DDD/レイヤードアーキテクチャ コマンド（サブエージェント統合）

このディレクトリには、テスト駆動開発（TDD）、ドメイン駆動設計（DDD）、およびレイヤードアーキテクチャを実装する16個のカスタムコマンドが含まれており、高度なサブエージェント統合と自動化されたタスク検証機能を備えています。

**🚀 最新版**: メタデータ駆動タスク検証システム付きサブエージェント統合コマンド

## 🎯 **コアイノベーション: サブエージェント統合**

### **✨ サブエージェント強化コマンド**
すべてのコマンドが複雑な分析と意思決定のために特化したAIサブエージェントを活用します：

- **専門知識**: 各フェーズでドメイン特化サブエージェントを使用
- **品質保証**: クリティカルタスクの自動検証
- **構造化出力**: 標準化されたレポート形式
- **再試行メカニズム**: 問題検出時の自動改善

### **🔧 タスク検証システム**
高度なメタデータ駆動検証により品質を保証：

```bash
# すべてのコマンド後の自動検証
✅ クリティカルタスクの確認
✅ 標準化された出力検証  
✅ 改善ガイダンス付き自動再試行
✅ 包括的品質ゲート
```

## 📋 **完全コマンドリスト（16コマンド）**

### **🎯 初期フェーズ**

| コマンド | ステータス | サブエージェント | 主要機能 |
|---------|---------|----------|--------|
| `/create-vision` | ✅ | 00-create-vision | ビジョン文書生成、コアシナリオ抽出 |
| `/review-vision` | ✅ | 00.5-review-vision | ステークホルダー整合性検証、品質評価 |
| `/init-project-structure` | ✅ | 01-init-project-structure | Python環境セットアップ、依存関係解決 |
| `/sprint-planning <sprint>` | ✅ | 02-sprint-planning | GitHub統合、自動issue作成 |
| `/review-sprint-plan <sprint>` | ✅ | 02.5-review-sprint-plan | スプリント計画検証、キャパシティプランニング |

### **🚀 スプリント実行フェーズ**

| コマンド | ステータス | サブエージェント | 主要機能 |
|---------|---------|----------|--------|
| `/create-use-case <issue>` | ✅ | 03-create-use-case | Given-When-Thenシナリオ作成 |
| `/domain-modeling <issue>` | ✅ | 04-domain-modeling | DDD準拠ドメインモデル設計 |
| `/review-domain-design <issue>` | ✅ | 04.5-review-domain-design | **クリティカルタスク検証、DDD準拠性チェック** |
| `/create-tests <issue>` | ✅ | 05-create-tests | TDD REDフェーズテスト生成 |
| `/review-test-design <issue>` | ✅ | 05.5-review-test-design | **TDDテスト品質検証、シナリオカバレッジ** |
| `/implement-domain <issue>` | ✅ | 06-implement-domain | TDD GREENフェーズドメイン実装 |
| `/implement-usecase <issue>` | ✅ | 07-implement-usecase | アプリケーション層実装 |
| `/implement-infra <issue>` | ✅ | 08-implement-infra | インフラストラクチャ層実装 |
| `/implement-presentation <issue>` | ✅ | 09-implement-presentation | プレゼンテーション層実装 |
| `/run-all-tests <issue>` | ✅ | 10-run-all-tests | 包括的テスト実行 |
| `/review-test-results <issue>` | ✅ | 10.5-review-test-results | **テスト結果分析、品質メトリクス** |
| `/refactor <issue>` | ✅ | 11-refactor | TDD REFACTORフェーズ品質改善 |

### **🔄 レビュー・管理フェーズ**

| コマンド | ステータス | サブエージェント | 主要機能 |
|---------|---------|----------|--------|
| `/evolve-scenarios <feature>` | ✅ | 12-evolve-scenarios | フィードバック駆動シナリオ発展 |
| `/review-issue <issue>` | ✅ | 13-review-issue | 包括的issue分析 |
| `/apply-feedback <issue>` | ✅ | 14-apply-feedback | 体系的改善適用 |
| `/create-pr <issue>` | ✅ | 15-create-pr | 品質ゲート付きPR作成 |
| `/use-case-status <issue>` | ✅ | 16-use-case-status | 進捗追跡と推奨事項 |

## 🎯 **高度機能**

### **1. メタデータ駆動タスク検証**

各コマンドは知的検証のためにJSONメタデータを使用：

```json
{
  "command": "04.5-review-domain-design",
  "critical_tasks": [
    "ddd_compliance_check",
    "aggregate_boundary_validation", 
    "business_rules_placement"
  ],
  "critical_patterns": [
    "✅.*DDD準拠性",
    "✅.*集約境界",
    "(APPROVED|CONDITIONAL_APPROVAL|REJECTED)"
  ]
}
```

### **2. 標準化サブエージェント出力**

すべてのサブエージェントは構造化レポート形式に従います：

```markdown
## 📊 実行サマリー
- ✅/❌ クリティカルタスク1: 完了状況
- ✅/❌ クリティカルタスク2: 完了状況

## 📋 総合判定
**ステータス: APPROVED/CONDITIONAL_APPROVAL/REJECTED**

## 💡 次のステップ
1. 具体的なアクション項目
2. 次の推奨コマンド
```

### **3. 自動品質ゲート**

#### **APPROVED**: 次フェーズ準備完了
- すべてのDDD原則が適切に適用
- 完全なシナリオカバレッジ
- 品質メトリクスが基準内

#### **CONDITIONAL_APPROVAL**: 軽微な改善が必要
- コア要件は満たしている
- オプション強化が提案
- 監視しながら進行

#### **REJECTED**: クリティカルな問題があり修正が必要
- 根本的問題が検出
- 再設計または再作業が必要
- 次フェーズへ進行不可

## 🚀 **開発ワークフロー**

### **プロジェクト初期化**
```bash
# 1. プロジェクトビジョンとコアシナリオ作成
/create-vision

# 2. ステークホルダー整合性のためのビジョンレビュー
/review-vision

# 3. プロジェクト構造初期化
/init-project-structure

# 4. 最初のスプリント計画
/sprint-planning 1

# 5. スプリント計画レビュー
/review-sprint-plan 1
```

### **機能開発（TDD/DDDサイクル）**
```bash
# ステップ1: 要件と設計
/create-use-case 123 feature-name
/domain-modeling 123
/review-domain-design 123      # ← サブエージェント品質チェック

# ステップ2: TDD実装
/create-tests 123
/review-test-design 123        # ← サブエージェント検証
/implement-domain 123
/implement-usecase 123
/implement-infra 123
/implement-presentation 123

# ステップ3: 品質保証
/run-all-tests 123
/review-test-results 123       # ← サブエージェント分析
/refactor 123

# ステップ4: レビューと納品
/review-issue 123
/apply-feedback 123
/create-pr 123
```

### **継続的改善**
```bash
# スプリント中のシナリオ発展
/evolve-scenarios new-requirement

# 進捗監視
/use-case-status 123
```

## 🔧 **システムアーキテクチャ**

### **サブエージェント統合**
```
ホストコマンド ──┐
               ├─→ コンテキスト準備
               ├─→ サブエージェント実行（Taskツール経由）
               ├─→ 結果検証（_task_verification.sh）
               ├─→ クリティカルタスクチェック（メタデータ駆動）
               └─→ 必要時再試行（自動改善）
```

### **検証ライブラリ**
```bash
# 共通検証関数
source "_task_verification.sh"

load_task_metadata "command-name"
verify_critical_tasks "command-name" "$report_file"
show_verification_results "command-name"
```

### **ディレクトリ構造**
```
.claude/commands/tdd-ddd-layered/
├── 00-16 コマンドファイル（16ファイル）
├── _task_verification.sh              # 共通検証ライブラリ
├── _validate_structure.sh             # 構造検証
├── task-definitions/                  # メタデータ定義
│   ├── 00-create-vision.json
│   ├── 04.5-review-domain-design.json
│   └── ... （21メタデータファイル）
├── test-automation-system.sh          # テスト自動化
├── ci-cd-verification.sh              # CI/CD検証
├── TASK_VERIFICATION_GUIDE.md         # 詳細使用ガイド
├── QUICKSTART.md                      # クイックスタートガイド
└── README.md                          # このファイル
```

## 🛠️ **高度統合パターン**

### **パターン1: フルAIガイド開発**
```bash
# すべてのステップでAI検証付き完全ワークフロー
/create-use-case 123 feature-name
/domain-modeling 123

# AI設計検証
/review-domain-design 123
# → 改善提案または次フェーズ承認

/create-tests 123

# AIテスト検証  
/review-test-design 123
# → 実装前のTDD準拠保証

/implement-domain 123
/implement-usecase 123
/implement-infra 123
/implement-presentation 123

/run-all-tests 123

# AI結果分析
/review-test-results 123
# → パフォーマンスと品質インサイト

/refactor 123
/create-pr 123
```

### **パターン2: 品質ゲート開発**
```bash
# クリティカル品質ゲートでのみAI検証を使用
/create-use-case 123 feature-name
/domain-modeling 123
/review-domain-design 123    # クリティカル: 設計品質ゲート

/create-tests 123
/implement-domain 123
/run-all-tests 123
/review-test-results 123     # クリティカル: 品質評価ゲート

/create-pr 123
```

### **パターン3: AIによる問題解決**
```bash
# 問題発生時、AIを活用して解決
/use-case-status 123         # AI診断と推奨事項

# AI応答例:
# "問題検出: ドメイン設計がDDD原則に違反"
# "推奨: /review-domain-design 123 で具体的ガイダンス"
# "代替案: /domain-modeling 123 で再設計"

# 解決のためのAIガイダンスに従う
```

## 🎯 **高度サブエージェント機能**

### **専門サブエージェントの役割**

- **ドメイン設計レビュアー**: DDD準拠性とアーキテクチャ品質を検証
- **テスト設計バリデーター**: TDD原則とシナリオカバレッジを保証
- **テスト結果アナライザー**: 品質メトリクスとパフォーマンスインサイト提供
- **Issueレビュアー**: 包括的品質評価を実施
- **スプリントプランナー**: 最適化された開発計画を作成
- **ビジョンレビュアー**: プロジェクト整合性とステークホルダーニーズを検証

### **学習機能付き自動再試行**

AIが問題を検出すると、システムは再試行のための強化コンテキストを自動準備：

```bash
# 最初の試行が失敗 → AIが具体的フィードバック提供
# 再試行コンテキストに含まれるもの:
- 前回遭遇した問題
- 改善のための具体的焦点領域
- 避けるべき一般的パターン
- メタデータからのターゲット指導
```

### **AI駆動品質ゲート**

#### **設計レビュー品質ゲート**
```bash
# /review-domain-design 123
# APPROVED → /create-tests準備完了
# CONDITIONAL_APPROVAL → 軽微改善後に進行
# REJECTED → 重大問題、/domain-modelingに戻る
```

#### **テスト設計品質ゲート**
```bash
# /review-test-design 123
# APPROVED → /implement-domain準備完了
# CONDITIONAL_APPROVAL → テスト改善推奨
# REJECTED → テスト修正、/create-testsに戻る
```

#### **テスト結果品質ゲート**
```bash
# /review-test-results 123
# APPROVED → /refactor準備完了
# CONDITIONAL_APPROVAL → 軽微最適化提案
# REJECTED → クリティカル問題、進行前に修正
```

## 🚀 **チーム統合とベストプラクティス**

### **AIとのチーム協業**
```bash
# チーム間でのAIインサイト共有:
/review-issue 123  # 包括的品質評価
# → 4軸評価結果の共有
# → AI推奨事項に基づくチーム基準確立
```

### **マルチIssue統合**
```bash
# 複雑なマルチissueシナリオをAIが処理
/create-use-case 1,2,3 integrated-feature
/review-domain-design 1,2,3  # issue間統合を検証
/create-pr 1,2,3             # 一貫性のあるプルリクエスト作成
```

### **AIによるシナリオ発展**
```bash
# AI駆動要件発展
/evolve-scenarios payment-enhancement

# AI分析内容:
- 既存ドメインモデルへの影響
- 統合要件
- テスト戦略更新
- リスク評価
```

## 🔧 **高度トラブルシューティング**

### **AIアシスト問題解決**

| 問題 | AI検出 | AI解決策 |
|------|--------|---------|
| DDD違反 | 設計レビュー時自動検出 | 具体的境界修正 |
| テストカバレッジギャップ | テスト結果分析時検出 | ターゲットテスト追加 |
| パフォーマンス問題 | ボトルネック特定 | 最適化提案 |
| アーキテクチャ違反 | 継続的監視 | リファクタリングガイダンス |

### **回復パターン**
```bash
# あらゆる状態からのAIガイド回復
/use-case-status 123  # 診断分析

# 回復ガイダンス例:
# "現在: ドメイン結合によるテスト失敗"
# "根本原因: 集約境界違反" 
# "解決策: /review-domain-design 123"
# "代替案: 最終正常状態へのロールバック"
```

## 📊 **パフォーマンスメトリクスと成功指標**

### **開発品質メトリクス**
- **AI承認率**: 初回90%以上
- **品質ゲート成功率**: 95%以上の通過率
- **欠陥削減**: 本番問題70%以上削減
- **開発速度**: AIガイダンスで50%以上高速化

### **チーム生産性メトリクス**
- **学習曲線**: オンボーディング時間80%削減
- **一貫性**: 基準遵守95%以上
- **知識共有**: 自動化されたベストプラクティス
- **継続的改善**: AI駆動最適化

### **システムパフォーマンス監視**
```bash
# システムパフォーマンス監視
- サブエージェント成功率: 95%以上目標
- 品質ゲート通過率: 90%以上目標
- 自動再試行成功率: 80%以上目標
- 平均分析時間: <2秒
```

## 🎯 **主要原則**

### **設計哲学**
- **ビジョン駆動**: 常に全体プロジェクトビジョンと整合
- **品質第一**: TDD/DDD原則への厳格な遵守
- **自動化品質**: サブエージェント駆動検証
- **段階的**: 複雑システムの段階的構築
- **追跡可能**: すべての決定の完全監査証跡

### **開発プロセス**
- **コアシナリオ優先**: 80%カバレッジでコアユースケース
- **段階的拡張**: 後のスプリントでエッジケース追加
- **継続的検証**: 各フェーズでの品質ゲート
- **フィードバック統合**: 体系的改善適用

### **技術基準**
- **TDD準拠**: 厳格なRED→GREEN→REFACTORサイクル
- **DDD純粋性**: ドメイン層独立性とカプセル化
- **クリーンアーキテクチャ**: 適切な依存方向
- **包括的テスト**: 意味のあるテストで高カバレッジ

## 📊 **品質保証**

### **自動検証**
- **クリティカルタスク完了**: メタデータ駆動検証
- **アーキテクチャ準拠**: DDD/クリーンアーキテクチャ検証
- **テスト品質**: TDD準拠とシナリオカバレッジ
- **コード品質**: 静的分析とメトリクス

### **品質ゲート**
- **設計フェーズ**: 実装前のDDD準拠
- **テストフェーズ**: GREENフェーズ前のREDフェーズ準拠
- **実装**: 開発中のアーキテクチャ検証
- **レビューフェーズ**: 包括的品質評価

### **テストシステム**
```bash
# 自動テスト
./test-automation-system.sh basic      # 基本機能
./test-automation-system.sh all        # 完全テストスイート

# CI/CD検証  
./ci-cd-verification.sh dev quick      # 開発環境
./ci-cd-verification.sh prod full      # 本番検証
```

## 🎓 **使用例**

### **シンプル機能開発**
```bash
# 単一機能の完全ワークフロー
/create-use-case 1 user-login
/domain-modeling 1
/review-domain-design 1    # 自動品質チェック
/create-tests 1
/implement-domain 1
/run-all-tests 1
/create-pr 1
```

### **レビュー付き複雑機能**
```bash
# 品質レビュー付き開発
/create-use-case 7 payment-processing
/domain-modeling 7
/review-domain-design 7         # REJECTED時再設計が必要な場合あり
/create-tests 7
/review-test-design 7           # テスト品質検証
/implement-domain 7
/run-all-tests 7
/review-test-results 7          # 結果分析
/refactor 7
/create-pr 7
```

### **マルチIssue開発**
```bash
# 複数関連issueの処理
/create-use-case 1,2,3 integrated-feature
/domain-modeling 1,2,3
/review-domain-design 1,2,3
# ... 実装継続
/create-pr 1,2,3
```

## 🔄 **移行と互換性**

### **以前のバージョンから**
- 既存のコマンド構文はすべてサポート継続
- メタデータ形式は後方互換
- サブエージェント機能の段階的採用可能

### **統合ポイント**
- GitHub IssuesとPull Requests
- 既存プロジェクト文書構造
- CI/CDパイプラインと品質ゲート
- チーム協業ワークフロー

## 📋 **クイックリファレンス**

### **必須コマンド**
```bash
# プロジェクト開始
/create-vision && /init-project-structure

# スプリント計画  
/sprint-planning 1

# 機能開発
/create-use-case 123 feature-name
/domain-modeling 123
/create-tests 123
/implement-domain 123
/create-pr 123

# 進捗監視
/use-case-status 123
```

### **品質コマンド**
```bash
# クリティカル品質チェック（サブエージェント付き）
/review-domain-design 123      # 実装前
/review-test-design 123        # GREENフェーズ前
/review-test-results 123       # リファクタリング前
```

### **システムコマンド**
```bash
# システム検証
./test-automation-system.sh basic
./ci-cd-verification.sh dev quick
```

## 🎉 **メリット**

### **開発者向け**
- **ガイド付き開発**: 各フェーズでの明確な次ステップ
- **品質保証**: 自動問題検出
- **エラー削減**: サブエージェント駆動検証
- **高速フィードバック**: 即座の品質評価

### **チーム向け**
- **一貫プロセス**: 標準化開発ワークフロー
- **知識共有**: 包括的文書化
- **品質基準**: 統一品質ゲート
- **進捗可視化**: リアルタイム状況追跡

### **プロジェクト向け**
- **高品質**: エンタープライズグレードコード品質
- **保守性**: クリーンアーキテクチャと包括テスト
- **追跡可能性**: 完全監査証跡
- **スケーラビリティ**: 複雑システムの実証パターン

---

## 🚀 **始め方**

1. **クイックスタート**: 即座のハンズオン体験のため[QUICKSTART.md](QUICKSTART.md)を読む
2. **詳細ガイド**: 包括的使用方法は[TASK_VERIFICATION_GUIDE.md](TASK_VERIFICATION_GUIDE.md)をチェック
3. **最初のコマンド**: `/create-vision`を実行してジャーニーを開始

**サブエージェント統合TDD/DDD/レイヤードアーキテクチャコマンドは、自動化インテリジェンスと包括品質保証により最高品質の開発体験を提供します。**