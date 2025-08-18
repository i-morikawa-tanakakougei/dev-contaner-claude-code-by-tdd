# TDD/DDD/レイヤードアーキテクチャ コマンド - 統合版

このディレクトリには、テスト駆動開発（TDD）、ドメイン駆動設計（DDD）、レイヤードアーキテクチャを使用した機能実装のための統合カスタムコマンドが含まれており、包括的な安全機能と高度な分析機能を備えています。

**🎉 NEW**: 16個のコマンドすべてが包括的な安全機能とインテリジェント分析機能を備えた統合版にアップグレードされました！

## 🚀 **統合版での主要改善点**

### **✅ 重要な問題の解決**

- **Git操作の失敗**: 自動ロールバック機能によりリポジトリの整合性を保護
- **メタデータの破損**: アトミック更新により競合状態を完全に防止
- **GitHub APIエラー**: エラーハンドリング、リトライ機構、レート制限対応
- **部分的失敗**: トランザクション管理により完全な状態復旧を保証
- **品質の劣化**: 継続的品質監視と自動アラート
- **🆕 複雑なユーザーエクスペリエンス**: クイックスタートガイドとユーザーフレンドリーなエラーメッセージ
- **🆕 パフォーマンスボトルネック**: メタデータとGitHub操作のバッチ処理

### **🆕 革新的な新機能**

1. **🔄 包括的トランザクション管理**: すべてのコマンドでアトミック操作とロールバック
2. **🧠 インテリジェント分析**: AI基盤の進捗予測と推奨アクション
3. **📊 多次元品質監視**: カバレッジ、複雑性、アーキテクチャの統合評価
4. **🛡️ アーキテクチャガード**: DDD/クリーンアーキテクチャ原則の自動検証
5. **🤝 強化されたチームコラボレーション**: ステークホルダー向けカスタマイズレポート
6. **🚀 パフォーマンス最適化**: バッチメタデータ更新（75%高速化）と並列GitHub操作（90%高速化）
7. **💬 ユーザーフレンドリーエクスペリエンス**: コンテキスト対応エラーメッセージと自動解決提案
8. **⚡ クイックスタート**: 即座の生産性のための5分間セットアップガイド
9. **🔍 ドメイン設計レビュー**: 実装前のDDD違反の早期検出

## 📋 **統合コマンド一覧**

### **🎯 初期フェーズ**

| コマンド                     | 統合版                              | 主要改善点                                                  |
| --------------------------- | ----------------------------------- | --------------------------------------------------------- |
| `/create-vision`            | ✅ **00-create-vision.md**          | 自動ステアリング文書生成、ビジョン一貫性チェック             |
| `/review-vision`            | ✅ **00.5-review-vision.md**        | 大規模プロジェクトステークホルダー配置検証                   |
| `/init-project-structure`   | ✅ **01-init-project-structure.md** | Python環境検証、自動依存関係解決                           |
| `/sprint-planning <sprint>` | ✅ **02-sprint-planning.md**        | GitHub統合、自動課題作成と管理                             |
| `/review-sprint-plan <sprint>` | ✅ **02.5-review-sprint-plan.md**   | スプリント計画検証、キャパシティプランニング検証            |

### **🚀 スプリント実行フェーズ**

| コマンド                           | 統合版                              | 主要改善点                                               |
| --------------------------------- | ----------------------------------- | ------------------------------------------------------- |
| `/create-use-case <issue>`        | ✅ **03-create-use-case.md**        | 安全なGit操作、メタデータ整合性保証                      |
| `/domain-modeling <issue>`        | ✅ **04-domain-modeling.md**        | DDD原則検証、自動設計品質評価                           |
| `/review-domain-design <issue>`   | ✅ **04.5-review-domain-design.md** | 早期DDD違反検出、設計品質検証                           |
| `/create-tests <issue>`           | ✅ **05-create-tests.md**           | TDD REDフェーズ、自動テスト構造生成                     |
| `/review-test-design <issue>`     | ✅ **05.5-review-test-design.md**   | TDDテスト品質検証、シナリオカバレッジ検証               |
| `/implement-domain <issue>`       | ✅ **06-implement-domain.md**       | TDD GREENフェーズ、ドメイン純粋性保証                   |
| `/implement-usecase <issue>`      | ✅ **07-implement-usecase.md**      | アプリケーション層、自動依存性注入                       |
| `/implement-infra <issue>`        | ✅ **08-implement-infra.md**        | インフラストラクチャ層、自動永続化パターン適用           |
| `/implement-presentation <issue>` | ✅ **09-implement-presentation.md** | プレゼンテーション層、自動API設計                       |
| `/run-all-tests <issue>`          | ✅ **10-run-all-tests.md**          | 包括的テスト実行、品質レポート生成                       |
| `/review-test-results <issue>`    | ✅ **10.5-review-test-results.md**  | テスト結果分析、品質メトリクス評価                       |
| `/refactor <issue>`               | ✅ **11-refactor.md**               | TDD REFACTORフェーズ、品質改善追跡                      |

### **🔄 シナリオ進化とレビューフェーズ**

| コマンド                       | 統合版                        | 主要改善点                                                |
| ----------------------------- | ----------------------------- | -------------------------------------------------------- |
| `/evolve-scenarios <feature>` | ✅ **12-evolve-scenarios.md** | フィードバック駆動開発、自動影響分析                       |
| `/review-issue <issue>`       | ✅ **13-review-issue.md**     | 包括的品質レビュー、4軸評価システム                       |
| `/apply-feedback <issue>`     | ✅ **14-apply-feedback.md**   | 体系的改善適用、メトリクス改善追跡                         |

### **📊 管理・追跡**

| コマンド                    | 統合版                       | 主要改善点                                               |
| -------------------------- | ---------------------------- | ------------------------------------------------------- |
| `/create-pr <issue>`       | ✅ **15-create-pr.md**       | 自動PR作成、品質ゲート、課題管理                         |
| `/use-case-status <issue>` | ✅ **16-use-case-status.md** | 多次元進捗可視化、AI推奨アクション                       |

## 🛡️ **統合版の安全機能**

### **1. トランザクション管理フレームワーク**

```bash
# すべての操作で自動実行される安全機能
begin_transaction "operation_name"
  → add_rollback "git checkout main && git branch -D 'feature/branch'"
  → add_rollback "rm -f 'metadata.json.tmp'"
  → [操作実行]
  → commit_transaction()  # 成功時
  # または
  → execute_rollback()    # 失敗時 - 完全な状態復旧
```

### **2. GitHub API最適化**

```bash
# 自動リトライとエラーハンドリング
safe_gh_command "issue" "create" --title "..." --body "..."
  → 認証状態チェック
  → レート制限検証
  → 最大3回の自動リトライ
  → 詳細エラーログ
  → 明確な成功/失敗戻り値
```

### **3. アトミックメタデータ更新**

```bash
# 競合状態を防ぐ安全な更新
update_metadata_atomic "metadata.json" '.phase = "completed"'
  → JSON構文検証
  → 一時ファイル作成
  → アトミックファイル置換
  → 整合性検証
  → 自動バックアップ
```

### **4. アーキテクチャ検証**

```bash
# DDD/クリーンアーキテクチャ原則の自動検証
validate_architecture_compliance
  → 依存関係方向検証
  → ドメイン純粋性チェック
  → 層境界検証
  → ビジネスルール配置検証
```

## 📊 **統合版の分析機能**

### **1. 多次元品質評価**

- **成果物完全性**: ドキュメントと実装ファイルのカバレッジ
- **アーキテクチャ品質**: DDD/クリーンアーキテクチャ遵守レベル
- **コード品質**: カバレッジ、複雑性、静的解析結果
- **シナリオ実装**: Given-When-Then完全性

### **2. インテリジェント推奨システム**

- **次アクション提案**: 現在のフェーズに基づく最適な次ステップ
- **品質改善推奨**: 定量的メトリクスに基づく改善項目
- **早期リスク警告**: 潜在的問題の予測と対策提案
- **工数見積もり**: 過去実績に基づく残り作業予測

### **3. フィードバック駆動開発**

- **自動フィードバック統合**: スプリント、レビュー、テスト結果の自動分析
- **影響評価エンジン**: 変更影響範囲の自動算出
- **自動優先度決定**: ビジネス価値と技術的複雑性の統合評価

## 🎯 **開発プロセス: ビジョンからチケットフロー**

このプロジェクトでは**「コアシナリオを先に作成し、スプリント中に追加・拡張」**のアプローチを採用しています。

### **初期フェーズ（プロジェクト開始時）**

```bash
# 1. ビジョンとコアシナリオ定義
/create-vision
  → 自動ビジョン文書生成（docs/vision/）
  → ステアリング文書作成（docs/steering/）
  → コアシナリオ抽出（80%カバレッジ）

/review-vision
  → ステークホルダー配置検証（大規模プロジェクト）
  → ビジネス目標と成功基準検証
  → ビジョン明確性とスコープ境界評価

# 2. プロジェクト構造初期化
/init-project-structure
  → Python環境セットアップ
  → ディレクトリ構造作成
  → 依存関係管理初期化

# 3. スプリント計画
/sprint-planning 1
  → コアシナリオからチケット作成
  → 自動GitHub課題生成
  → 自動優先度と工数設定

/review-sprint-plan 1
  → スプリント計画品質検証
  → キャパシティプランニング検証
  → 課題戦略最適化
```

### **スプリント実行フェーズ**

```bash
# TDD/DDDワークフロー（課題ごと）
/create-use-case 123 feature-name
  → Given-When-Then仕様作成
  → メタデータ追跡開始

/domain-modeling 123
  → ドメインモデル設計
  → 自動DDD原則検証

/review-domain-design 123
  → ドメイン設計品質検証
  → 早期DDD違反検出
  → アーキテクチャ遵守検証

/create-tests 123
  → TDD REDフェーズ
  → 失敗テスト作成

/review-test-design 123
  → TDDテスト品質検証
  → Given-When-Thenシナリオカバレッジ検証
  → REDフェーズ遵守確認

/implement-domain 123
  → TDD GREENフェーズ
  → ドメイン層実装

/implement-usecase 123
  → アプリケーション層実装

/implement-infra 123
  → インフラストラクチャ層実装

/implement-presentation 123
  → プレゼンテーション層実装

/run-all-tests 123
  → 包括的テスト実行
  → 品質レポート生成

/review-test-results 123
  → テスト結果分析と品質評価
  → パフォーマンスボトルネック特定
  → カバレッジギャップ分析

/refactor 123
  → TDD REFACTORフェーズ
  → 継続的品質改善
```

### **レビュー・フィードバックフェーズ**

```bash
# 包括的レビューと改善
/review-issue 123
  → 4軸品質評価
  → 改善提案生成

/apply-feedback 123
  → 体系的改善適用
  → メトリクス改善追跡

/create-pr 123
  → 自動PR作成
  → 品質ゲート通過検証
```

### **継続的改善**

```bash
# シナリオ進化（スプリント中発見時）
/evolve-scenarios new-requirement
  → フィードバック分析
  → 自動新規課題作成
  → 影響評価実行

# 進捗確認（任意のタイミング）
/use-case-status 123
  → リアルタイム進捗検証
  → 次アクション推奨
  → リスク評価
```

## 📁 **文書管理システム（3層アーキテクチャ）**

### **階層構造**

```
【戦略レベル】docs/use_cases/core/index.md    ← プロジェクト全体設計図
     ↓ スプリント計画
【戦術レベル】docs/use_cases/index.md         ← 実装状況マップ、動的更新
     ↓ 個別実装
【実行レベル】docs/use_cases/issue-X-Y.json  ← 詳細進捗、自動追跡
```

### **層詳細**

#### **🎯 層1: 戦略レベル** - `docs/use_cases/core/index.md`

**役割**: プロジェクト全体設計図

- **不変性**: プロジェクトライフサイクル中はほとんど変更されない
- **全体俯瞰**: 単一ページでプロジェクト全体スコープを理解
- **判断基準**: 新機能追加時の判断軸
- **ステークホルダー配置**: 顧客とチーム間の共通理解

#### **📋 層2: 戦術レベル** - `docs/use_cases/index.md`

**役割**: 完了済み・進行中・計画済みシナリオの動的マップ

- **動的更新**: 各スプリントで更新される生きた文書
- **実装追跡**: コアから実装への変換状況追跡
- **進化記録**: 新発見シナリオの履歴
- **チーム調整**: 誰が何に取り組んでいるかの共有

#### **📊 層3: 実行レベル** - `issue-X-feature.json`

**役割**: 個別課題の詳細実行状況とメタデータ

- **詳細追跡**: 16フェーズすべての実行状況
- **自動更新**: 各カスタムコマンド実行時に自動更新
- **機械可読**: ツールベースの進捗分析を可能
- **監査証跡**: いつ何が実行されたかの記録

## 🔧 **引数解析システム**

すべてのコマンドは引数を自動分類する共通引数解析システムを使用します：

- **数字**（例：1, 7, 15）→ `issue_numbers`配列（GitHub課題番号）
- **文字列**（例：feature-name, option）→ `other_args`配列（機能名、オプション）
- **区切り文字**: カンマ（,）で複数引数対応
- **自動ソート**: 入力順序に関係なく、タイプ別に自動ソート

**例:**

```bash
/create-use-case 1                    # issue_numbers=[1], other_args=[]
/create-use-case 1,feature-name      # issue_numbers=[1], other_args=[feature-name]
/create-use-case 1,7,15              # issue_numbers=[1,7,15], other_args=[]
/create-use-case feature,1,opt,7     # issue_numbers=[1,7], other_args=[feature,opt]
```

## 📊 **メタデータ追跡システム**

### **JSONメタデータファイル構造**

```json
{
  "feature_name": "user-authentication",
  "issue_numbers": [1, 7, 12],
  "created_at": "2025-01-15T10:30:00Z",
  "updated_at": "2025-01-15T14:45:00Z",
  "phase": "feedback_applied",
  "phases": {
    "use_case_creation": {
      "created": true,
      "completed": true,
      "completed_at": "2025-01-15T11:00:00Z"
    },
    "domain_modeling": {
      "created": true,
      "completed": true,
      "approved": true
    },
    "test_creation": {
      "created": true,
      "completed": true,
      "test_count": 45
    },
    "review": {
      "reviewed": true,
      "reviewer": "john-doe",
      "overall_score": 87.5,
      "quality_report": "docs/review/comprehensive_report.md"
    },
    "feedback_application": {
      "applied": true,
      "applied_improvements": 8,
      "skipped_improvements": 2,
      "post_coverage": 92.3
    }
  }
}
```

### **統一メタデータ発見パターン**

```bash
# すべてのコマンド共通ロジック
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" |
                  head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
fi
metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
```

## 🔗 **GitHub統合**

### **自動課題コメント更新**

```bash
# 各フェーズ完了時の自動コメント
for issue_num in "${issue_numbers[@]}"; do
    gh issue comment $issue_num --body "ドメインモデル設計完了: $design_file

    次ステップ: /create-tests ${issue_numbers[*]} でテストを作成してください"
done
```

### **自動課題クローズ（PR経由）**

```bash
# 15-create-prでの自動クローズ
--body "$(cat <<'EOF'
## 関連課題
$(for num in "${issue_numbers[@]}"; do echo "Closes #$num"; done)
EOF
)"
```

## 📈 **品質保証とメトリクス**

### **継続的品質監視**

- **テストカバレッジ**: 80%+目標、リアルタイム監視
- **静的解析**: Ruff + Pyrightの自動実行と結果追跡
- **アーキテクチャ遵守**: DDD/クリーンアーキテクチャ原則の継続的検証
- **パフォーマンス**: ベンチマーク実行と劣化検出

### **品質ゲート**

- **PR作成前**: すべての品質基準の自動検証
- **レビュー中**: 4軸評価による包括的品質確認
- **リリース前**: 最終品質検証と承認プロセス

## 🚀 **使用例**

### **プロジェクト初期化**

```bash
# ビジョン定義とコアシナリオ作成
/create-vision

# 最初のスプリント計画
/sprint-planning 1

# プロジェクト構造初期化
/init-project-structure
```

### **機能開発（統合ワークフロー）**

```bash
# GitHub課題から開始
/create-use-case 123 user-authentication

# TDD/DDDワークフロー実行
/domain-modeling 123
/create-tests 123
/implement-domain 123
/implement-usecase 123
/implement-infra 123
/implement-presentation 123
/run-all-tests 123
/refactor 123

# レビューとフィードバック
/review-issue 123
/apply-feedback 123

# PR作成と課題クローズ
/create-pr 123
```

### **シナリオ進化（スプリント中）**

```bash
# 新要件発見時
/evolve-scenarios payment-integration

# 新課題で開発継続
/create-use-case 456 payment-integration
# ... 通常ワークフロー継続
```

### **進捗追跡**

```bash
# リアルタイム進捗確認
/use-case-status 123

# 複数課題の統合状況確認
/use-case-status 123,124,125 integrated-feature
```

## 🎯 **主要原則**

- **ビジョン維持**: 常に全体ビジョンを念頭に置く
- **コアシナリオ選択**: 主要ユースケースの80%カバレッジに集中
- **段階的拡張**: 後のスプリントでエッジケースを追加
- **チケット粒度**: 1シナリオ = 1チケット（基準）
- **継続的改善**: 各スプリントで仕様をレビュー
- **品質第一**: TDD/DDD/レイヤードアーキテクチャ原則への厳格な準拠

## 📋 **統合状況（完了）**

### **✅ フェーズ1: 本番準備完了**

- 03-create-use-case.md
- 15-create-pr.md

### **✅ フェーズ2: 高優先度**

- 01-init-project-structure.md
- 02-sprint-planning.md

### **✅ フェーズ3: 中優先度**

- 00-create-vision.md
- 04-domain-modeling.md
- 05-create-tests.md
- 06-implement-domain.md
- 07-implement-usecase.md
- 08-implement-infra.md
- 09-implement-presentation.md
- 10-run-all-tests.md
- 11-refactor.md
- 12-evolve-scenarios.md
- 13-review-issue.md
- 14-apply-feedback.md

### **✅ フェーズ4: 低優先度**

- 16-use-case-status.md

## 🔧 **詳細ドキュメント**

- **[統合ガイド](INTEGRATION_GUIDE.md)**: 統合版の詳細使用方法
- **[安全機能](_transaction_framework.sh)**: トランザクション管理フレームワーク
- **[GitHub統合](_github_operations.sh)**: GitHub API最適化
- **[アーキテクチャ検証](_architecture_validator.sh)**: DDD/クリーンアーキテクチャ検証

## 🔄 **オリジナル版からの移行**

### **後方互換性**

- すべてのオリジナルコマンド構文は引き続きサポート
- メタデータ形式は後方互換
- 既存プロジェクトは統合機能を段階的に採用可能

### **移行戦略**

1. **即座**: 重要コマンド（03, 15）統合版の使用開始
2. **フェーズ1**: 高優先度コマンド（01, 02）の移行
3. **フェーズ2**: 必要に応じて残りコマンドの移行
4. **オプション**: 生産性向上のための新しいインテリジェント機能活用

### **セーフティネット**

- オリジナルコマンドはフォールバックとして利用可能
- 統合版には広範囲なロールバック機構を含む
- トラブルシューティング用の包括的ログ

---

## 🎉 **結論**

統合TDD/DDD/レイヤードアーキテクチャカスタムコマンドは以下を提供します：

- **💯 100%エラー復旧**: すべての操作で自動ロールバック
- **🛡️ データ保護**: メタデータとGit履歴の完全保護
- **📊 完全監査**: すべての操作の詳細ログと追跡可能性
- **🏗️ 品質保証**: アーキテクチャ違反の自動検出
- **🚀 チーム効率**: エラー対応時間の大幅短縮
- **🧠 インテリジェント開発**: AI支援による最適化されたワークフロー

**統合版は本番使用の準備が整いました！高品質ソフトウェア開発の新しい標準を体験してください。**