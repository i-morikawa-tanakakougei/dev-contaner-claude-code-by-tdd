# 手動同期ガイド - TDD/DDD/Layered Architecture システム

## 概要

このガイドは、TDD/DDD/Layered Architectureプロセス実行中に発生する可能性があるイレギュラー対応時の手動チェックリストとテンプレートを提供します。

## 🔧 手動同期が必要な状況

### 1. エージェント実行失敗
- サブエージェントが期待通りに動作しない
- タスク確認（Critical Tasks）で問題が検出される
- 出力ファイルが正常に生成されない

### 2. プロセス中断・復旧
- 実行途中での中断からの復旧
- 並行作業による状態不整合
- Git状態の不一致

### 3. カスタム要件対応
- 標準プロセス外の特別な処理が必要
- 外部システムとの連携が必要
- 複雑なマージ・リファクタリング

## 📋 手動同期チェックリスト

### Phase 1: 状況確認

```bash
# 現在の状態確認
echo "=== 現在のプロジェクト状態確認 ==="
echo "Git branch: $(git branch --show-current)"
echo "Git status:"
git status --porcelain

echo ""
echo "=== ドキュメント構造確認 ==="
find docs/ -name "*.md" -o -name "*.json" | head -20

echo ""
echo "=== 最新のメタデータ確認 ==="
find docs/use_cases/ -name "*.json" -exec ls -la {} \; | tail -5
```

### Phase 2: 整合性チェック

#### ✅ ビジョンレベル整合性
- [ ] `docs/vision/project-vision.md` - プロジェクトビジョン存在確認
- [ ] `docs/use_cases/core/index.md` - コアシナリオ整合性
- [ ] `docs/steering/*.md` - ステアリング文書一貫性

#### ✅ スプリントレベル整合性
- [ ] `docs/sprints/sprint-X-plan.md` - スプリント計画
- [ ] `docs/sprints/sprint-X-backlog.md` - スプリントバックログ
- [ ] GitHubイシューとスプリント文書の同期

#### ✅ 実装レベル整合性
- [ ] `docs/use_cases/issue-X-Y.md` - 仕様文書
- [ ] `docs/use_cases/issue-X-Y.json` - メタデータ追跡
- [ ] `docs/domain/issue-X-Y-domain-model.md` - ドメインモデル
- [ ] テストファイル存在（`tests/`）
- [ ] 実装ファイル存在（`src/`）

#### ✅ レビューレベル整合性
- [ ] `docs/reviews/` - 各段階のレビューレポート存在
- [ ] レビューステータス（APPROVED/CONDITIONAL_APPROVAL/REJECTED）
- [ ] メタデータにレビュー結果反映

### Phase 3: 手動修復手順

#### A. 不完全な実行の復旧
```bash
# 最後に実行したコマンドの確認
echo "=== 最終実行コマンド確認 ==="
if [[ -f "/workspace/.claude/context/current-command-context.json" ]]; then
    cat /workspace/.claude/context/current-command-context.json | jq '.command, .timestamp'
fi

# 不完全な出力ファイルのクリーンアップ
echo "=== 不完全ファイルのクリーンアップ ==="
# 例：空のレビューファイル削除
find docs/reviews/ -name "*.md" -size 0 -delete
find docs/use_cases/ -name "*.json" -size 0 -delete
```

#### B. メタデータ修復
```bash
# メタデータ再生成テンプレート
issue_num="3"  # 対象イシュー番号
feature_name="example-feature"  # フィーチャー名

cat > "docs/use_cases/issue-${issue_num}-${feature_name}.json" <<EOF
{
  "issue_number": $issue_num,
  "feature_name": "$feature_name",
  "status": "pending",
  "created_at": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "use_case_specification": {
    "status": "completed",
    "file": "docs/use_cases/issue-${issue_num}-${feature_name}.md"
  },
  "domain_modeling": {
    "status": "pending"
  }
}
EOF
```

#### C. レビューステータス修復
```bash
# レビューレポートのステータス確認
echo "=== レビューステータス確認 ==="
for review_file in docs/reviews/*.md; do
    if [[ -f "$review_file" ]]; then
        echo "File: $(basename "$review_file")"
        grep -E "(APPROVED|CONDITIONAL_APPROVAL|REJECTED)" "$review_file" || echo "  Status: UNKNOWN"
        echo ""
    fi
done
```

## 🔄 プロセス復旧テンプレート

### 1. ビジョンフェーズ復旧
```bash
# ビジョン段階での中断からの復旧
if [[ ! -f "docs/vision/project-vision.md" ]]; then
    echo "ビジョン作成から再開が必要"
    echo "実行コマンド: /create-vision"
fi
```

### 2. スプリント計画復旧
```bash
sprint_num="1"
# スプリント計画復旧
if [[ ! -f "docs/sprints/sprint-${sprint_num}-plan.md" ]]; then
    echo "スプリント計画から再開が必要"
    echo "実行コマンド: /sprint-planning $sprint_num"
fi
```

### 3. 実装フェーズ復旧
```bash
issue_num="3"
# 各段階の完了状況確認
echo "=== Issue #$issue_num 実装状況確認 ==="

phases=(
    "use_case:docs/use_cases/issue-$issue_num-*.md:/create-use-case"
    "domain_design:docs/domain/issue-$issue_num-*-domain-model.md:/domain-modeling" 
    "tests:tests/:**test**.py:/create-tests"
    "domain_impl:src/domain/:/implement-domain"
)

for phase_info in "${phases[@]}"; do
    IFS=':' read -r phase_name file_pattern command <<< "$phase_info"
    
    if ls $file_pattern >/dev/null 2>&1; then
        echo "✅ $phase_name - 完了"
    else
        echo "❌ $phase_name - 未完了"
        echo "   復旧コマンド: $command $issue_num"
    fi
done
```

## 🛠️ 緊急時修復コマンド集

### Git状態修復
```bash
# 不要なファイル削除
git clean -fd

# 作業ディレクトリリセット
git checkout -- .

# 最新コミットからの復旧
git reset --hard HEAD
```

### ディレクトリ構造再構築
```bash
# 必要なディレクトリを再作成
mkdir -p {docs/{vision,use_cases,domain,reviews,sprints,analysis,maintenance,test_plan,test_report},src/{domain,application,infrastructure,presentation},tests/{unit,integration,e2e}}

# 基本的なインデックスファイル作成
echo "# Use Cases Index" > docs/use_cases/index.md
echo "# Core Scenarios" > docs/use_cases/core/index.md
```

### メタデータ一括確認
```bash
# 全メタデータファイルの健全性確認
echo "=== メタデータ健全性確認 ==="
for json_file in docs/use_cases/*.json; do
    if [[ -f "$json_file" ]]; then
        echo "Checking: $(basename "$json_file")"
        if jq empty "$json_file" 2>/dev/null; then
            echo "  ✅ Valid JSON"
        else
            echo "  ❌ Invalid JSON - 修復が必要"
        fi
    fi
done
```

## 📞 エスカレーション手順

### Level 1: 自動復旧
1. 上記チェックリストの実行
2. 基本的な修復コマンドの実行
3. プロセス再実行

### Level 2: 手動介入
1. ログファイルの詳細分析
2. 個別コマンドの段階実行
3. 問題箇所の特定と修正

### Level 3: システム再構築
1. プロジェクトディレクトリの完全リセット
2. ビジョンフェーズからの完全再実行
3. データ移行・マージ作業

## 📝 トラブルシューティング記録テンプレート

```markdown
## トラブルシューティング記録

**日時**: $(date)
**発生状況**: 
**エラー内容**: 
**試行した解決策**: 
**最終解決方法**: 
**予防策**: 
**備考**: 
```

## 💡 ベストプラクティス

1. **定期チェック**: 重要なマイルストーンでの状態確認
2. **バックアップ**: 重要な変更前のコミット
3. **ログ保存**: エラー発生時の詳細ログ保存
4. **段階実行**: 大きな処理は段階的に実行し確認
5. **文書更新**: トラブル解決後は本ガイドの更新

## 📚 関連リソース

- [README.md](../README.md) - プロジェクト概要
- [QUICKSTART.md](../../.claude/commands/tdd-ddd-layered/QUICKSTART.md) - クイックスタート
- [TASK_VERIFICATION_GUIDE.md](../../.claude/commands/tdd-ddd-layered/TASK_VERIFICATION_GUIDE.md) - タスク確認ガイド

---

このガイドは継続的に更新され、実際のトラブルシューティング経験を反映します。