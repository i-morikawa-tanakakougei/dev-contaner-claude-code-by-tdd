# 緊急復旧コマンドガイド v1.0

## 📋 **概要**

TDD/DDD/レイヤードアーキテクチャの標準プロセスをバイパスした緊急対応後に、プロジェクトを標準ワークフローに復帰させるための専用コマンド群です。

**コマンド番号**: 99-1 ～ 99-7 (緊急対応復旧専用番号体系)  
**実行順序**: 単一バグフィックス実行手順に沿った論理的な順序  
**統合**: 既存の標準コマンド（00-16）とシームレスに連携

## 🚨 **使用場面**

### **こんな時に使用**
- ✅ 本番障害で緊急修正を直接コミット
- ✅ ホットフィックスでTDD/DDDプロセスをスキップ
- ✅ 緊急対応後にドキュメントとコードが乖離
- ✅ テストが不十分または未作成
- ✅ GitHub Issueが未作成または不完全
- ✅ プロジェクトメタデータの不整合

### **使用しない場面**
- ❌ 通常の開発作業（00-16コマンドを使用）
- ❌ 予定された機能開発
- ❌ リファクタリング作業

## 🔄 **基本ワークフロー**

### **標準実行順序**
```bash
# Step 1: 現状分析
/emergency-recovery --mode full

# Step 2: Issue作成
/create-retroactive-issue --commit <hash>

# Step 3: ドキュメント同期
/sync-documentation <issue> --type all

# Step 4: テスト作成
/retroactive-test <issue>

# Step 5: 妥当性検証
/validate-emergency-fix <issue>

# Step 6: メタデータ調整
/reconcile-metadata --scope project

# Step 7: 最終レビュー
/review-emergency-recovery
```

## 📚 **コマンドリファレンス**

### **99-1: emergency-recovery** - 緊急復旧統括
**用途**: 緊急修正の分析と復旧計画作成

```bash
/emergency-recovery [OPTIONS]

OPTIONS:
  --mode <full|partial|analysis>    復旧モード (default: full)
  --issue <issue-number>           特定Issueに対する復旧
  --branch <branch-name>           分析対象ブランチ

EXAMPLES:
  /emergency-recovery --mode analysis     # 分析のみ実行
  /emergency-recovery --mode full         # 完全復旧計画作成
  /emergency-recovery --issue 123         # Issue固有の復旧
```

**出力**:
- 復旧分析レポート
- 優先順位付きアクションプラン
- 推定作業時間

---

### **99-2: create-retroactive-issue** - 事後Issue作成
**用途**: 緊急修正コミット（単一・範囲）に対するGitHub Issue作成

```bash
/create-retroactive-issue [COMMIT_SPECIFICATION] [OPTIONS]

COMMIT_SPECIFICATION (相互排他、いずれか必須):
  --commit <hash>                  単一コミット（従来通り）
  --since <hash>                   指定コミット以降（含まない）
  --from <hash>                    指定コミット以降（含む）
  --range <start>..<end>           Git範囲指定
  --last <number>                  最新N個のコミット

OPTIONS:
  --type <bug|hotfix|emergency>    Issue分類 (default: emergency)
  --strategy <individual|consolidated|interactive>  複数コミット処理戦略
  --update                         既存Issue更新モード

SINGLE COMMIT EXAMPLES:
  /create-retroactive-issue --commit a1b2c3d --type bug
  /create-retroactive-issue --commit abc123 --update

RANGE SPECIFICATION EXAMPLES:
  /create-retroactive-issue --since hotfix-start --strategy individual
  /create-retroactive-issue --from emergency-branch --strategy consolidated  
  /create-retroactive-issue --range abc123..def456 --strategy interactive
  /create-retroactive-issue --last 3 --strategy individual
```

**処理戦略**:
- **individual**: 各コミットに個別Issue作成（デフォルト）
- **consolidated**: 複数コミットを1つのIssueに統合
- **interactive**: コミット毎に作成/スキップを選択

**範囲指定詳細**:
| パラメータ | Git相当 | 基準コミット含む |
|-----------|---------|----------------|
| `--since <hash>` | `<hash>..HEAD` | ❌ 含まない |
| `--from <hash>` | `<hash>~1..HEAD` | ✅ 含む |
| `--range <start>..<end>` | `<start>..<end>` | start❌, end✅ |
| `--last <number>` | `HEAD~<N>..HEAD` | 最新から数える |

**出力**:
- GitHub Issue (新規作成/更新)
- Issue-コミット間のトレーサビリティリンク

---

### **99-3: sync-documentation** - ドキュメント同期
**用途**: コードからドキュメントへの逆生成・同期

```bash
/sync-documentation <issue-number> [OPTIONS]

REQUIRED:
  <issue-number>                   対象Issue番号

OPTIONS:
  --type <use-case|domain|all>     同期対象 (default: all)
  --force                          競合時の強制上書き

EXAMPLES:
  /sync-documentation 123 --type use-case   # ユースケース文書のみ
  /sync-documentation 456 --type domain     # ドメインモデルのみ
  /sync-documentation 789 --type all        # 全文書同期
```

**処理内容**:
- Given-When-Thenシナリオの逆生成
- ドメインモデル文書の更新
- 既存文書との差分マージ

---

### **99-4: retroactive-test** - 遡及的テスト作成
**用途**: 緊急修正に対する後付けテスト作成

```bash
/retroactive-test <issue-number> [OPTIONS]

REQUIRED:
  <issue-number>                   対象Issue番号

OPTIONS:
  --coverage-target <percentage>   目標カバレッジ (default: 80)
  --test-type <unit|integration|all> テスト種類 (default: all)

EXAMPLES:
  /retroactive-test 123 --coverage-target 90
  /retroactive-test 456 --test-type unit
  /retroactive-test 789 --test-type integration
```

**処理内容**:
- 変更コードの分析
- 必要テストケースの特定
- TDD準拠テストの作成
- カバレッジ確認

---

### **99-5: validate-emergency-fix** - 緊急修正検証
**用途**: 緊急対応の妥当性検証とリファクタリング提案

```bash
/validate-emergency-fix <issue-number> [OPTIONS]

REQUIRED:
  <issue-number>                   対象Issue番号

OPTIONS:
  --strict                         厳格な検証モード
  --focus <ddd|architecture|quality> 検証焦点

EXAMPLES:
  /validate-emergency-fix 123 --strict
  /validate-emergency-fix 456 --focus ddd
  /validate-emergency-fix 789 --focus architecture
```

**検証項目**:
- DDD原則適合性チェック
- レイヤードアーキテクチャ違反検出
- リファクタリング提案生成
- 技術的負債評価

---

### **99-6: reconcile-metadata** - メタデータ調整
**用途**: プロジェクトメタデータの整合性回復

```bash
/reconcile-metadata [OPTIONS]

OPTIONS:
  --scope <project|sprint|issue>   調整範囲 (default: project)
  --verify                         調整前の整合性確認

EXAMPLES:
  /reconcile-metadata --scope project      # プロジェクト全体
  /reconcile-metadata --scope sprint       # 現在スプリント
  /reconcile-metadata --scope issue        # Issue単位
```

**処理内容**:
- project-state.json更新
- context情報再構築
- ステータス整合性確保

---

### **99-7: review-emergency-recovery** - 最終レビュー
**用途**: 緊急復旧プロセスの完了確認

```bash
/review-emergency-recovery [OPTIONS]

OPTIONS:
  --issue <issue-number>           特定Issue対象
  --detail-level <summary|full>    レポート詳細度 (default: summary)
  --approval-required              明示的承認要求 (default: true)

EXAMPLES:
  /review-emergency-recovery --issue 123
  /review-emergency-recovery --detail-level full
  /review-emergency-recovery --approval-required false
```

**レビュー項目**:
1. **ドキュメント整合性**: Given-When-Then完全性
2. **テストカバレッジ**: 修正箇所の網羅率
3. **アーキテクチャ準拠**: DDD/Layered原則
4. **プロセス準拠**: 標準ワークフローとの差異

## 🎯 **実用的シナリオ**

### **シナリオ1: 単純なバグフィックス**
```bash
# 状況: 本番で null pointer exception発生、直接修正
git log --oneline -1
# a1b2c3d Fix payment validation null pointer exception

# 復旧手順
/emergency-recovery --mode analysis
/create-retroactive-issue --commit a1b2c3d --type bug
/sync-documentation 342 --type all
/retroactive-test 342 --coverage-target 85
/validate-emergency-fix 342
/reconcile-metadata --scope issue
/review-emergency-recovery --issue 342
```

### **シナリオ2: 複数コミットの緊急修正（範囲指定版）**
```bash
# 状況: データベース問題で3つのコミットによる修正
git log --oneline -3
# c3d4e5f Update connection pool settings
# b2c3d4e Fix query timeout configuration  
# a1b2c3d Add database retry logic

# 復旧手順
/emergency-recovery --mode full --branch hotfix/db-issues

# 方法A: 範囲指定で一括Issue作成（推奨）
/create-retroactive-issue --last 3 --strategy individual
# 結果: 3つの個別Issueが自動作成される

# 方法B: 統合Issueとして作成
/create-retroactive-issue --since hotfix-base --strategy consolidated
# 結果: 1つの統合Issue（3コミット全てリンク）

# 方法C: インタラクティブ選択
/create-retroactive-issue --range hotfix-base..HEAD --strategy interactive
# 結果: 各コミットごとに作成/スキップを選択

# 従来方式も継続サポート
/create-retroactive-issue --commit a1b2c3d --type bug
/create-retroactive-issue --commit b2c3d4e --type hotfix
/create-retroactive-issue --commit c3d4e5f --type emergency

# 後続処理（作成されたIssueに対して）
/sync-documentation <created-issue> --type all
/retroactive-test <created-issue>
/validate-emergency-fix <created-issue> --focus architecture
/reconcile-metadata --scope project
/review-emergency-recovery --detail-level full
```

### **シナリオ3: 既存Issueの更新**
```bash
# 状況: 緊急時に簡易Issueを作成済み、詳細化が必要
gh issue view 340
# #340 "Emergency fix" (minimal info)

# 詳細化実行
/create-retroactive-issue --commit a1b2c3d --update
/sync-documentation 340 --type all
/review-emergency-recovery --issue 340 --detail-level summary
```

### **シナリオ4: 複雑な緊急修正ブランチ**
```bash
# 状況: 長期間の緊急修正ブランチ、複数の関連修正
git log --oneline emergency-branch
# j1k2l3m Fix final integration issue
# h1i2j3k Update authentication flow  
# g1h2i3j Resolve data consistency problem
# f1g2h3i Add emergency logging
# e1f2g3h Initial emergency response
# emergency-start Emergency branch created

# 範囲指定での効率的処理
/emergency-recovery --branch emergency-branch --mode analysis

# インタラクティブでの選択的Issue作成
/create-retroactive-issue --from emergency-start --strategy interactive
# → 各コミットを確認し、重要なもののみIssue化

# 関連修正の統合Issue作成  
/create-retroactive-issue --range e1f2g3h..g1h2i3j --strategy consolidated --type emergency
# → データ整合性関連の修正を1つのIssueに統合

# 最終修正は個別Issue
/create-retroactive-issue --commit j1k2l3m --type bug

# 後続処理
/sync-documentation <integration-issue> --type all
/retroactive-test <integration-issue>
/review-emergency-recovery --detail-level full
```

## ⚠️ **注意事項とベストプラクティス**

### **実行前の確認**
1. **Git状態確認**: `git status` でuncommitted changesなし
2. **ブランチ確認**: 正しいブランチで実行
3. **GitHub認証**: `gh auth status` で認証確認
4. **バックアップ**: 重要なコンテキストファイルのバックアップ

### **実行中の注意点**
- **順序遵守**: 99-1→99-7の順序で実行
- **中断時の対処**: `/use-case-status --emergency-recovery` で状況確認
- **エラー時**: エラーメッセージとCommon Errorsセクションを参照

### **実行後の確認**
- **GitHub Issues**: 作成されたIssueの内容確認
- **ドキュメント整合性**: 更新されたドキュメントのレビュー
- **テスト実行**: `pytest` で全テストの動作確認
- **メタデータ確認**: `docs/metadata/project-state.json`の妥当性

## 🔧 **トラブルシューティング**

### **よくある問題**

#### **Q1: コミットハッシュが見つからない**
```bash
# 解決方法
git log --oneline    # コミット一覧確認
git show <hash>      # コミット詳細確認
# 完全ハッシュを使用する
```

#### **Q2: GitHub API権限エラー**
```bash
# 解決方法
gh auth login                    # 再認証
gh auth status                   # 認証状況確認
export GITHUB_TOKEN=<token>      # トークン設定
```

#### **Q3: Issue重複エラー**
```bash
# 解決方法
gh issue list --search "commit:<hash>"  # 既存Issue確認
/create-retroactive-issue --commit <hash> --update  # 更新モード
```

#### **Q4: メタデータ不整合**
```bash
# 解決方法
/reconcile-metadata --verify --scope project  # 事前確認
# 手動同期ガイド参照: docs/maintenance/manual-sync-guide.md
```

## 📈 **期待効果**

### **定量的効果**
- **復旧時間**: 4-6時間 → 30-45分 (85%短縮)
- **ドキュメント整合率**: 60-70% → 90-95%
- **テストカバレッジ**: 40-60% → 80-85%
- **プロセス準拠率**: 20-30% → 90-95%

### **定性的効果**
- チームの緊急対応への信頼性向上
- 技術的負債の体系的管理
- 標準プロセス遵守の文化醸成
- 品質基準の一貫性確保

## 🔗 **関連ドキュメント**

- **[提案書](../../reviews/emergency-recovery-workflow-commands-proposal-v1.1.md)**: 設計思想と要件
- **[実装レビュー](../../reviews/emergency-recovery-commands-implementation-review-v1.0.md)**: 品質評価結果
- **[手動同期ガイド](../../docs/maintenance/manual-sync-guide.md)**: 異常時の復旧手順
- **[メインREADME](./README.md)**: TDD/DDD/Layeredシステム全体概要

## 📞 **サポート**

### **実行時サポート**
- **ヘルプ表示**: 各コマンドで `--help` オプション
- **状況確認**: `/use-case-status --emergency-recovery`
- **詳細ガイド**: 各コマンドファイル内の「Common Errors」セクション

### **緊急時連絡**
- **システム異常**: docs/maintenance/manual-sync-guide.md参照
- **予期しないエラー**: GitHub Issues作成推奨

---

**作成日**: 2025-08-28  
**バージョン**: v1.0  
**対応コマンド**: 99-1 ～ 99-7  
**メンテナー**: TDD/DDD/Layered Architecture System Team