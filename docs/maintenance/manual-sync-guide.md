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

### 4. 緊急対応によるドキュメント・コード不整合
- バグ修正などで直接コードを修正した場合
- 標準のTDD/DDDプロセスをバイパスした実装
- ドキュメント（Given-When-Then、ドメインモデル）が実装と乖離
- テストが未整備または不完全な状態

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

## 🚨 緊急対応後のドキュメント・コード整合性回復

### 緊急対応検出手順
```bash
# 標準プロセスを経ていない変更の検出
echo "=== 緊急対応による変更検出 ==="

# 最近のコミットでドキュメント更新がない場合を検出
recent_commits=$(git log --oneline -10)
for commit in $(git log --format="%H" -10); do
    doc_changes=$(git diff-tree --no-commit-id --name-only -r $commit | grep -E "(docs/|tests/)" | wc -l)
    src_changes=$(git diff-tree --no-commit-id --name-only -r $commit | grep -E "src/" | wc -l)
    
    if [[ $src_changes -gt 0 && $doc_changes -eq 0 ]]; then
        echo "⚠️ Commit $commit: ソース変更あり、ドキュメント変更なし"
        git log --oneline -1 $commit
    fi
done
```

### ドキュメント・コード不整合の分析
```bash
# 変更されたソースファイルの特定
echo "=== 変更ソースファイル分析 ==="
modified_files=$(git diff --name-only HEAD~5..HEAD | grep -E "\.py$|\.ts$|\.js$")

for file in $modified_files; do
    echo "File: $file"
    
    # 対応するテストファイルの存在確認
    test_file=$(echo $file | sed 's|src/|tests/|' | sed 's|\.\w*$|_test.py|')
    if [[ -f "$test_file" ]]; then
        echo "  ✅ Test exists: $test_file"
        # テスト更新日時チェック
        if [[ $(stat -f "%m" "$file") -gt $(stat -f "%m" "$test_file") ]]; then
            echo "  ⚠️ テストがソースより古い"
        fi
    else
        echo "  ❌ Test missing: $test_file"
    fi
    
    # 対応するドキュメントの存在確認
    base_name=$(basename "$file" | cut -d. -f1)
    doc_pattern="docs/*/**/*${base_name}*.md"
    if ls $doc_pattern >/dev/null 2>&1; then
        echo "  ✅ Doc exists"
    else
        echo "  ❌ Doc missing"
    fi
done
```

### 復旧アプローチの選択
```bash
# 復旧方法の判定
echo "=== 復旧アプローチ判定 ==="

# 変更規模の算出
lines_changed=$(git diff --stat HEAD~5..HEAD | tail -1 | awk '{print $4}')
files_changed=$(git diff --name-only HEAD~5..HEAD | wc -l)

echo "変更規模: ${files_changed}ファイル, ${lines_changed}行"

if [[ $files_changed -le 3 ]]; then
    echo "推奨: 個別復旧アプローチ（99-X番台コマンド）"
    echo "  1. /emergency-recovery (99-1) --mode analysis で現状分析"
    echo "  2. /create-retroactive-issue (99-2) --commit HEAD でIssue作成"
    echo "  3. /sync-documentation (99-3) <issue> で個別ドキュメント同期"
    echo "  4. /retroactive-test (99-4) <issue> でテスト補完"
    echo "  5. /validate-emergency-fix (99-5) <issue> で検証"
    echo "  6. /reconcile-metadata (99-6) --scope issue でメタデータ更新"
    echo "  7. /review-emergency-recovery (99-7) <issue> で最終レビュー"
elif [[ $files_changed -le 10 ]]; then
    echo "推奨: 部分復旧アプローチ（99-X番台コマンド）"
    echo "  1. /emergency-recovery (99-1) --mode partial で部分復旧"
    echo "  2. 重要な機能から順次 /validate-emergency-fix (99-5)"
    echo "  3. /review-emergency-recovery (99-7) --detail-level summary で状況確認"
else
    echo "推奨: 完全復旧アプローチ（99-X番台コマンド）"
    echo "  1. /emergency-recovery (99-1) --mode full で全体復旧"
    echo "  2. /reconcile-metadata (99-6) --scope project でメタデータ再構築"
    echo "  3. /review-emergency-recovery (99-7) --detail-level full で総合レビュー"
fi
```

### ドキュメント逆生成手順
```bash
# Given-When-Thenシナリオの逆生成
echo "=== シナリオ逆生成 ==="

# 関数やクラスからシナリオを推論
source_file="src/domain/cart.py"
if [[ -f "$source_file" ]]; then
    echo "Analyzing: $source_file"
    
    # クラスメソッドの抽出
    methods=$(grep -E "def\s+\w+\(" "$source_file" | sed 's/def //' | cut -d'(' -f1)
    
    for method in $methods; do
        echo ""
        echo "Method: $method"
        echo "推論されるシナリオ:"
        echo "  Given: [初期状態]"
        echo "  When: $method が実行される"
        echo "  Then: [期待される結果]"
    done
fi
```

### テスト補完テンプレート
```python
# 緊急対応後のテスト補完用テンプレート
import pytest
from datetime import datetime

class TestEmergencyFix:
    """緊急対応 <commit-hash> に対する補完テスト"""
    
    @pytest.fixture
    def setup(self):
        """テスト環境のセットアップ"""
        # TODO: 実装に基づいてセットアップを記述
        pass
    
    def test_emergency_fix_core_functionality(self, setup):
        """緊急修正の主要機能テスト"""
        # Given: 緊急対応前の状態
        # TODO: 初期状態の設定
        
        # When: 修正された機能を実行
        # TODO: 修正機能の呼び出し
        
        # Then: 期待される動作を検証
        # TODO: アサーション追加
        assert True
    
    def test_emergency_fix_edge_cases(self, setup):
        """緊急修正のエッジケーステスト"""
        # TODO: エッジケースの実装
        pass
    
    def test_emergency_fix_regression(self, setup):
        """緊急修正によるリグレッションテスト"""
        # TODO: 既存機能への影響確認
        pass
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

### Level 4: 緊急対応後の復旧（99-X番台コマンド）
1. `/emergency-recovery` (99-1) `--mode analysis` で現状分析
2. `/create-retroactive-issue` (99-2) `--commit <hash>` で必要なIssue作成（範囲指定も可能: `--since`, `--from`, `--range`, `--last`）
3. `/sync-documentation` (99-3) `<issue>` `--type all` でドキュメント同期
4. `/retroactive-test` (99-4) `<issue>` `--coverage-target 80` でテスト補完
5. `/validate-emergency-fix` (99-5) `<issue>` `--strict` で妥当性検証
6. `/reconcile-metadata` (99-6) `--scope project` でプロジェクト状態の整合性確保
7. `/review-emergency-recovery` (99-7) `--detail-level summary` で最終確認

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

### 緊急対応の場合（追加項目）
**緊急対応の理由**: 
**標準プロセスをバイパスした範囲**: 
**影響を受けたファイル**: 
**ドキュメントとの乖離箇所**: 
**復旧に使用したコマンド**: 
**復旧完了確認**: 
  [ ] (99-1) emergency-recovery実行
  [ ] (99-2) create-retroactive-issue実行
  [ ] (99-3) sync-documentation実行
  [ ] (99-4) retroactive-test実行
  [ ] (99-5) validate-emergency-fix実行
  [ ] (99-6) reconcile-metadata実行
  [ ] (99-7) review-emergency-recovery実行
```

## 💡 ベストプラクティス

1. **定期チェック**: 重要なマイルストーンでの状態確認
2. **バックアップ**: 重要な変更前のコミット
3. **ログ保存**: エラー発生時の詳細ログ保存
4. **段階実行**: 大きな処理は段階的に実行し確認
5. **文書更新**: トラブル解決後は本ガイドの更新
6. **緊急対応記録**: 緊急対応時は必ず理由と範囲を記録
7. **速やかな復旧**: 緊急対応後は48時間以内に標準プロセスへ復帰
8. **チームへの通知**: 緊急対応実施時はチームに即座に通知

## 📚 関連リソース

- [README.md](../README.md) - プロジェクト概要
- [QUICKSTART.md](../../.claude/commands/tdd-ddd-layered/QUICKSTART.md) - クイックスタート
- [TASK_VERIFICATION_GUIDE.md](../../.claude/commands/tdd-ddd-layered/TASK_VERIFICATION_GUIDE.md) - タスク確認ガイド
- [EMERGENCY-RECOVERY-GUIDE.md](../../.claude/commands/tdd-ddd-layered/EMERGENCY-RECOVERY-GUIDE.md) - 緊急復旧コマンドの完全ガイド（99-X番台、438行の包括的な使用手順）
- [緊急対応復旧コマンド提案 v1.1](../../reviews/emergency-recovery-workflow-commands-proposal-v1.1.md) - 緊急対応後の標準フロー復帰コマンド提案書（99-X番台、設計思想）

---

このガイドは継続的に更新され、実際のトラブルシューティング経験を反映します。