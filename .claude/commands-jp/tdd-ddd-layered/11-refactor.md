すべてのテストがGREEN（TDDのREFACTORフェーズ）になった後、包括的な安全機能でコードをリファクタリングします。

## メタデータ
- **前提条件**: すべてのテストが合格（10-run-all-tests）
- **入力**: イシュー番号（必須）
- **出力**: 
  - 品質が向上したリファクタリング済みコード
  - 維持されたテストカバレッジ
  - 更新された`docs/use_cases/issue-X-Y.json`メタデータ
- **依存関係**: すべてのテストがgreen、コード解析ツール
- **実行タイミング**: TDD REFACTORフェーズ - すべてのテストが合格した後

## 🎯 **TDD/DDD/LAYEREDプロセスコンテキスト**

**🔄 コアワークフロー**: Vision(00) → Structure(01) → Sprint(02) → Sprint Review(02.5) → Use-Case(03) → Domain(04) → Design Review(04.5) → Tests(05) → Test Review(05.5) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Test Results Review(10.5) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的なシナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - リファクタリング（11/16）  
> 🎯 **フェーズ目的**: テスト合格後のコード品質向上（REFACTOR）  
> ⬅️ **前段階**: 10.5-review-test-results（テスト結果レビュー）  
> ➡️ **次段階**: 12-evolve-scenarios（シナリオ進化）または13-review-issue（レビュー）
>
> **📋 3層アーキテクチャ操作**:
>
> - 🎯 **戦略**: `docs/use_cases/core/index.md`（リファクタリング目標の参照）
> - 📊 **戦術**: `docs/use_cases/index.md`（TDD REFACTORステータスの更新）
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json`（リファクタリングサイクルの追跡）

## 🔵 **TDD REFACTORフェーズ: 品質向上のみ**

**⚠️ 重要な注意:**
- **このステップはTDD REFACTORフェーズです** - 機能を維持しながらコード品質を向上させます
- **すべてのテストはGREENを維持する必要があります** - 既存の機能を壊してはいけません  
- **品質向上に焦点を当てる** - 重複の除去、可読性の向上、パフォーマンスの最適化
- **新機能なし** - 既存の実装を改善するのみ

**TDDサイクルの完了:**
1. `05-create-tests` ← TDD RED（失敗するテストを作成）
2. `06-09-implement-*` ← TDD GREEN（実装完了）
3. `10-run-all-tests` ← すべてのテスト合格確認
4. `11-refactor` ← **【あなたはここにいます】TDD REFACTOR（品質向上）**

**リファクタリングルール:**
- ✅ コード構造と可読性を向上させる
- ✅ リファクタリング中はすべてのテストがGREENを維持する
- ❌ 新機能や機能性は追加しない

## 🚨 **重要: ユーザー同意を得た段階的リファクタリング**

**⚠️ 必須ユーザー許可ポリシー:**
- **フェーズ1（イシューのみ）**: 自動実行 - 安全で範囲限定
- **フェーズ2（関連コード）**: ユーザー許可が必要 - 範囲を拡大
- **フェーズ3（グローバル統合）**: ユーザー許可が必要 - システム全体の変更
- **Claude Codeはフェーズ2/3の前に許可を求める必要があります - 自動実行は禁止**

## 📋 **TDD REFACTORタスクチェックリスト**

**システマティックなコード品質向上のためにこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **📖 現在のイシュー分析**
- [ ] **現在のイシューコードをレビュー**: ステップ06-09で実装された現在のイシューのコードを分析する
- [ ] **コードスメルを特定**: 重複、長いメソッド、複雑な条件分岐を見つける
- [ ] **テストカバレッジを評価**: リファクタリング前に現在のコードが十分にテストされていることを確認する
- [ ] **リファクタリング順序を計画**: 安全性と影響度によって改善の順序を決める

#### **🔧 コード品質向上**
- [ ] **共通メソッドの抽出**: 現在のイシューのコード内の重複を除去する
- [ ] **命名の改善**: より説明的な変数、メソッド、クラス名を使用する
- [ ] **複雑なメソッドの簡素化**: 大きなメソッドをより小さく、焦点を絞ったものに分割する
- [ ] **条件分岐の複雑度を削減**: 複雑なif/elseチェーンやswitch文を簡素化する

#### **🧪 継続的テスト**
- [ ] **各変更後にテストを実行**: リファクタリングのたびに`uv run --frozen pytest`を実行する
- [ ] **すべてのテストがGREENであることを確認**: 機能が壊れていないことを確認する
- [ ] **コード品質をチェック**: `uv run --frozen ruff check src/ --fix`を実行する
- [ ] **型安全性を検証**: `uv run --frozen pyright src/`を実行する

### 🟡 推奨タスク

#### **🏗️ 構造改善**
- [ ] **デザインパターンの適用**: 適切なパターン（Strategy、Factoryなど）を実装する
- [ ] **クラス構成の改善**: 単一責任原則を確保する
- [ ] **エラーハンドリングの強化**: 例外処理とエラーメッセージを改善する
- [ ] **データ構造の最適化**: より適切なデータ構造を使用する
- [ ] **インポートと依存関係の最適化**: 未使用のインポートと依存関係をクリーンアップする

#### **🔍 関連コード発見（フェーズ2）**
- [ ] **ドメイン層をスキャン**: 他の機能でsrc/domain/の類似パターンを見つける
- [ ] **アプリケーション層をスキャン**: src/application/で重複するユースケースパターンを特定する
- [ ] **インフラストラクチャ層をスキャン**: 繰り返されるリポジトリやサービスパターンを見つける
- [ ] **テストコードをスキャン**: 重複するテストセットアップとヘルパーコードを特定する
- [ ] **統合機会を文書化**: 潜在的な統合対象をリストアップする

### 🟢 オプションタスク

#### **🎯 フェーズ1: イシュー限定リファクタリング**
- [ ] **改善機会を文書化**: 特定のリファクタリング対象をリストアップする
- [ ] **アルゴリズム効率の改善**: パフォーマンスクリティカルなコードセクションを最適化する
- [ ] **パフォーマンスを検証**: リファクタリングがパフォーマンスを低下させないことを確認する

#### **🔗 安全な統合プロセス（フェーズ2）**
- [ ] **統合計画を作成**: 統合される内容と影響評価を文書化する
- [ ] **現在の状態をバックアップ**: ロールバックのためにgitワーキングディレクトリがクリーンであることを確認する
- [ ] **共有抽象化を抽出**: 共通のベースクラスやインターフェースを作成する
- [ ] **段階的にリファクタリング**: 一度に小さく、テスト可能な変更を行う
- [ ] **関連テストを更新**: 統合されたコードで動作するようにテストを修正する

#### **✅ 統合検証（フェーズ2）**
- [ ] **完全なテストスイートを実行**: すべてのテストを実行して統合が機能を壊さないことを確認する
- [ ] **関連機能を検証**: 統合されたコードを使用する機能をテストする
- [ ] **後方互換性をチェック**: 既存のAPIがまだ動作することを確認する
- [ ] **パフォーマンス影響を検証**: 統合によるパフォーマンス変化を測定する
- [ ] **ドキュメントを更新**: 統合の変更をドキュメントに反映する

### **🤔 フェーズ1完了チェックポイント**
```bash
echo "✅ フェーズ1（イシュー限定リファクタリング）完了"
echo ""
echo "🎯 フェーズ2: 関連コード統合について"
echo "   📋 内容: 同じドメイン・機能領域の重複コードをチェック・統合"
echo "   ⏱️  推定時間: 10-20分"
echo "   🚨 リスク: 変更範囲が拡大、予期しない副作用の可能性"
echo "   💡 メリット: 重複排除、保守性向上"
echo ""
echo "フェーズ2を実行しますか？ (y/N): "
```

### **🤔 フェーズ2完了チェックポイント**
```bash
echo "✅ フェーズ2（関連コード統合）完了"
echo ""
echo "🎯 フェーズ3: グローバル統合について"
echo "   📋 内容: プロジェクト全体の重複コードをチェック・統合"
echo "   ⏱️  推定時間: 20-40分"
echo "   🚨 リスク: システム全体への影響、大きな変更範囲"
echo "   💡 メリット: システム全体の品質向上、技術債務削減"
echo ""
echo "フェーズ3を実行しますか？ (y/N): "
```

### **🌍 フェーズ3: グローバル統合（ユーザー許可必須）**

**🚨 警告: ユーザーが明示的に確認した場合のみ実行（y/Y）**

#### **🔍 グローバルコード分析**
- [ ] **コードベース全体をスキャン**: すべてのソースコードで重複パターンを分析する
- [ ] **ドメイン横断パターンを特定**: 複数のドメインにまたがるパターンを見つける
- [ ] **アーキテクチャ改善を評価**: システム全体のアーキテクチャ拡張を特定する
- [ ] **グローバル機会を文書化**: 包括的な改善計画を作成する
- [ ] **影響と工数を見積もる**: グローバル変更の範囲とリスクを評価する

#### **🏗️ システム全体の改善**
- [ ] **共有ライブラリを作成**: 共通機能を共有モジュールに抽出する
- [ ] **パターンを標準化**: システム全体で一貫したパターンを実装する
- [ ] **横断的関心事を最適化**: ログ、エラーハンドリング、バリデーションパターンを改善する
- [ ] **設定を統合**: 設定管理を統合・標準化する
- [ ] **監視を強化**: システム全体の監視と観測性を改善する

#### **🧪 包括的検証**
- [ ] **完全なテストスイートを実行**: 安定性のためにすべてのテストを複数回実行する
- [ ] **統合テストを実行**: すべての主要なシステム統合をテストする
- [ ] **システムパフォーマンスを検証**: グローバル変更がパフォーマンスを低下させないことを確認する
- [ ] **システム安定性をチェック**: 変更によって導入された不安定性がないかを監視する
- [ ] **すべてのドキュメントを更新**: システム全体の変更をドキュメントに反映する

### **🔧 最終品質検証**
- [ ] **最終コード品質チェックを実行**: `uv run --frozen ruff check src/ --fix`を実行する
- [ ] **最終フォーマットを実行**: `uv run --frozen ruff format src/`を実行する
- [ ] **最終型チェックを実行**: `uv run --frozen pyright src/`を実行する
- [ ] **完全なテストスイートを実行**: `uv run --frozen pytest --cov=src`を実行する
- [ ] **すべてのテストがGREENであることを検証**: リファクタリング中に機能が壊れていないことを確認する

### **📊 リファクタリングドキュメント**
- [ ] **行った改善を文書化**: 何をリファクタリングしたか、なぜリファクタリングしたかを記録する
- [ ] **メタデータを更新**: issue-X-Y.jsonでリファクタリングフェーズを完了とマークする
- [ ] **リファクタリングレポートを作成**: メトリクス改善（複雑度、重複など）を文書化する
- [ ] **リファクタリング済みコードをコミット**: 明確なコミットメッセージですべての改善をバージョン管理する
- [ ] **レビューの準備**: コードが品質レビューフェーズの準備ができていることを確認する

**💡 プロのヒント: 恐れずにリファクタリングしつつ、継続的にテストする - グリーンテストがあなたの安全網です！**
- ✅ コードの重複を除去する  
- ✅ 動作を維持しながらパフォーマンスを最適化する
- ❌ 新機能を追加したり動作を変更したりしない
- ❌ 既存のテストを壊さない

**コード品質のみ向上させる - すべての機能性を維持する。**

## 🛡️ **統合版の主な改善点**

### **✅ 解決された問題**

- **リファクタリング中断リスク**: テスト失敗時の変更取り消し機能
- **メタデータ破損**: 原子的更新によるリファクタリング履歴保護
- **コード品質検証**: 自動的な品質メトリクス測定・比較
- **変更影響分析**: アーキテクチャ違反の自動検出
- **パフォーマンス劣化**: 最適化前後の性能比較

### **🆕 新機能**

1. **🔄 安全なリファクタリング**: ステップバイステップでの変更とテスト
2. **📊 品質メトリクス**: リファクタリング前後の品質指標比較
3. **🛡️ アーキテクチャ保護**: DDD/Clean Architecture原則の維持
4. **🔍 影響分析**: 変更による副作用の自動検出
5. **📈 パフォーマンス監視**: 最適化効果の定量化

## よくあるエラーと解決策

### ❌ エラーケース1: すべてのテストが合格していない
**原因**: GREENフェーズを達成する前にリファクタリングを試行  
**解決策**: 最初に`/run-all-tests <issue-number>`ですべてのテストが合格することを確認する

### ❌ エラーケース2: リファクタリングでテストが壊れる
**原因**: リファクタリング中に構造ではなく動作を変更している  
**解決策**: コード構造、デザインパターン、可読性のみに焦点を当てる

### ❌ エラーケース3: 大規模なリファクタリング範囲
**原因**: 一度に多くの変更を試行している  
**解決策**: 小さく段階的な変更を行い、頻繁にテストを実行する

### ❌ エラーケース4: エンティティ継承によるID型競合
**原因**: 異なるID要件を持つベースクラスからエンティティを継承するようにリファクタリングする  
**解決策**: 
```bash
# 例: Configuration エンティティでのUUID変換エラー
# 問題: BaseDomainEntityはUUIDを期待するが、既存のテストは"test-config-1"のような文字列IDを使用

# リファクタリング前: ID互換性を検証
grep -r "test.*config.*id" tests/  # 既存のテストID形式をチェック
grep -r "UUID" src/domain/entities/  # ベースクラス要件をチェック

# 解決策: 継承よりもコンポジションを使用
# - 後方互換性のために既存のID形式を保持
# - バリデーションのためにベースクラスの静的メソッドを使用
# - ID型が一致しない場合は直接継承を避ける
```
**重要**: 継承パターンを適用する前に必ずID型の互換性を検証する

## 実行例

### ✅ 成功例
```bash
$ /refactor 15
🔄 イシュー: #15のリファクタリングを開始します
🟢 テスト状態確認中...
✅ 全テストが成功しています
🎨 コード品質改善中...
  ✅ 重複コードの除去
  ✅ メソッドの分割と整理
🧪 リファクタリング後テスト実行...
======= 45 passed, 0 failed =======
✅ リファクタリング完了 - テスト維持
🎉 TDD REFACTORフェーズ完了!
```

### ❌ 失敗例と修正
```bash
$ /refactor 15
❌ リファクタリング後に2つのテストが失敗
💡 リファクタリングを元に戻してください
# 修正: 変更を元に戻し、より小さな改善を行う
git checkout HEAD~1
$ /refactor 15
```

## タスク詳細

## 1. **安全な環境のセットアップと引数解析**

```bash
# 🔧 自動引数解析と検証を含むすべての安全操作関数をロード
source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "11-refactor" "$ARGUMENTS"

# 引数はセットアップスクリプトによって既に解析・検証済み
# このコマンド特有の追加検証
if [[ ${#issue_numbers[@]} -eq 0 ]]; then
    echo "エラー: 最低1つのイシュー番号が必要です"
    show_usage_example "refactor" "1" "単一イシューのリファクタリング"
    show_usage_example "refactor" "1,7" "複数イシューのリファクタリング"
    show_usage_example "refactor" "1,feature-name" "イシュー + 機能名指定"
    exit 1
fi
```

## 2. **トランザクション管理セットアップ**

```bash
# リファクタリング用のアトミックトランザクションを開始
transaction_id="refactor_$(date +%s)_$(echo "${issue_numbers[*]}" | tr ' ' '_')"
begin_transaction "$transaction_id"

# ロールバックハンドラーをセットアップ
add_rollback_handler "git stash push -m 'Auto-stash before refactor rollback'"
add_rollback_handler "git checkout ."
add_rollback_handler "echo '🔄 リファクタリングをロールバックしました'"
```

## 3. **前提条件検証とメタデータ発見**

```bash
# すべてのテストが現在合格していることを検証
echo "📋 前提条件を確認中..."

# メタデータファイルを発見
issue_list=$(IFS=-; echo "${issue_numbers[*]}")
if [[ ${#other_args[@]} -gt 0 ]]; then
    feature_name="${other_args[0]}"
else
    feature_name=$(find docs/use_cases -name "issue-${issue_list}-*.md" | head -1 | sed 's/.*issue-[0-9-]*-\(.*\)\.md$/\1/')
    if [[ -z "$feature_name" ]]; then
        echo "❌ エラー: フィーチャー名を特定できませんでした"
        echo "💡 使用方法: /refactor $issue_list,<feature-name>"
        execute_rollback
        exit 1
    fi
fi

metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
spec_file="docs/use_cases/issue-${issue_list}-${feature_name}.md"

# 前提条件を検証
if [[ ! -f "$metadata_file" ]]; then
    echo "❌ エラー: メタデータファイルが見つかりません: $metadata_file"
    execute_rollback
    exit 1
fi

# 前のフェーズが完了していることをチェック
validate_phase_completion "$metadata_file" "presentation_implementation"

echo "✅ 前提条件チェック完了"
```

## 4. **リファクタリング前の品質ベースライン**

```bash
# リファクタリング前の品質ベースラインを確立
echo "📊 リファクタリング前の品質メトリクスを測定中..."

# ベースライン測定を作成
baseline_dir="$(mktemp -d)"
add_rollback_handler "rm -rf '$baseline_dir'"

# 包括的テストスイートを実行
echo "🧪 全テストスイートを実行中..."
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v --tb=short; then
    echo "❌ エラー: テストが失敗しています。リファクタリング前にテストを修正してください"
    execute_rollback
    exit 1
fi

# コード品質メトリクスを測定
echo "📏 コード品質メトリクスを測定中..."
{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --show-source --statistics || true
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright --stats || true
    echo ""
    echo "=== TEST COVERAGE ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=term-missing --cov-report=json:${baseline_dir}/coverage.json || true
} > "${baseline_dir}/quality_baseline.txt"

# 比較用にベースラインを保存
cp "${baseline_dir}/quality_baseline.txt" "${baseline_dir}/quality_before.txt"
echo "✅ 品質ベースライン確立"
```

## 5. **リファクタリング前のアーキテクチャ検証**

```bash
# 現在のアーキテクチャ状態を検証
echo "🏗️ アーキテクチャ状態を検証中..."

if ! validate_architecture_compliance; then
    echo "⚠️ 警告: 現在のコードにアーキテクチャ違反があります"
    echo "📋 詳細なレポートを確認し、リファクタリングで修正することを検討してください"
fi

# アーキテクチャスナップショットを作成
architecture_snapshot="${baseline_dir}/architecture_before.json"
create_architecture_snapshot > "$architecture_snapshot"
add_rollback_handler "echo '📊 アーキテクチャスナップショット: $architecture_snapshot'"
```

## 6. **安全なリファクタリング実行**

```bash
# 安全な段階的ステップでリファクタリングを実行
echo "🔧 安全なリファクタリングを開始中..."

# ドメイン層リファクタリング
echo "📦 ドメイン層のリファクタリング..."
refactor_domain_layer() {
    local changes_made=false

    # エンティティと値オブジェクトの重複を除去
    echo "  🔍 エンティティ・値オブジェクトの重複除去..."

    # 共通動作をベースクラスに抽出
    echo "  🏗️ 共通動作のベースクラス抽出..."

    # 複雑なメソッドを簡素化
    echo "  ⚡ 複雑メソッドの簡素化..."

    # ユビキタス言語の一貫性を確保
    echo "  📚 ユビキタス言語の一貫性確保..."

    # ドメイン変更後にテストを実行
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v; then
        echo "❌ ドメイン層テストが失敗しました"
        return 1
    fi

    echo "  ✅ ドメイン層リファクタリング完了"
    return 0
}

# アプリケーション層リファクタリング
refactor_application_layer() {
    echo "  🔍 ユースケース複雑度の削減..."
    echo "  🛡️ 共通バリデーションロジックの抽出..."
    echo "  📊 DTOコンバージョンの最適化..."

    # アプリケーション変更後にテストを実行
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/ -v; then
        echo "❌ アプリケーション層テストが失敗しました"
        return 1
    fi

    echo "  ✅ アプリケーション層リファクタリング完了"
    return 0
}

# インフラストラクチャ層リファクタリング
refactor_infrastructure_layer() {
    echo "  🗄️ データベースクエリの最適化..."
    echo "  🔗 接続処理の改善..."
    echo "  🗺️ 共通マッピングロジックの抽出..."

    # インフラストラクチャ変更後にテストを実行
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v; then
        echo "❌ インフラストラクチャ層テストが失敗しました"
        return 1
    fi

    echo "  ✅ インフラストラクチャ層リファクタリング完了"
    return 0
}

# プレゼンテーション層リファクタリング
refactor_presentation_layer() {
    echo "  🔗 エラーレスポンスの標準化..."
    echo "  ✅ 共通バリデーションパターンの抽出..."
    echo "  🎯 API一貫性の向上..."

    # プレゼンテーション変更後にテストを実行
    if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v; then
        echo "❌ プレゼンテーション層テストが失敗しました"
        return 1
    fi

    echo "  ✅ プレゼンテーション層リファクタリング完了"
    return 0
}

# ロールバック機能付きで各層のリファクタリングを実行
for layer_func in refactor_domain_layer refactor_application_layer refactor_infrastructure_layer refactor_presentation_layer; do
    echo "🔧 実行中: $layer_func"

    # 各層の前にチェックポイントを作成
    git add -A && git commit -m "Checkpoint before $layer_func" || true

    if ! $layer_func; then
        echo "❌ $layer_func でエラーが発生しました"
        git reset --hard HEAD~1 2>/dev/null || true
        execute_rollback
        exit 1
    fi

    # 層の変更をコミット
    git add -A && git commit -m "Refactor: $layer_func completed" || true
done
```

## 7. **横断的関心事のリファクタリング**

```bash
# 横断的関心事をリファクタリング
echo "🌐 横断的関心事のリファクタリング..."

# ログパターンを標準化
echo "  📝 ログパターンの標準化..."

# エラーメッセージを改善
echo "  💬 エラーメッセージの改善..."

# パフォーマンス監視フックを追加
echo "  📊 パフォーマンス監視フックの追加..."

# 命名規則の一貫性を確保
echo "  📛 命名規則の一貫性確保..."

# 横断的関心事の変更後に完全なテストスイートを実行
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v; then
    echo "❌ 横断的関心事のリファクタリング後のテストが失敗しました"
    execute_rollback
    exit 1
fi

echo "✅ 横断的関心事のリファクタリング完了"
```

## 8. **テストスイートリファクタリング**

```bash
# テストコードをリファクタリング
echo "🧪 テストコードのリファクタリング..."

# テストの重複を除去
echo "  🔄 テストの重複除去..."

# テストフィクスチャとビルダーを抽出
echo "  🏗️ テストフィクスチャとビルダーの抽出..."

# テスト名と構成を改善
echo "  📝 テスト名と構成の改善..."

# 不足しているエッジケーステストを追加
echo "  🎯 エッジケーステストの追加..."

# テストリファクタリングを検証
if ! PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest -v --tb=short; then
    echo "❌ テストリファクタリング後の検証が失敗しました"
    execute_rollback
    exit 1
fi

echo "✅ テストコードリファクタリング完了"
```

## 9. **リファクタリング後の品質検証**

````bash
# リファクタリング後の品質メトリクスを測定
echo "📊 リファクタリング後の品質メトリクスを測定中..."

{
    echo "=== RUFF ANALYSIS ==="
    uv run --frozen ruff check . --show-source --statistics || true
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright --stats || true
    echo ""
    echo "=== TEST COVERAGE ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest --cov=src --cov-report=term-missing --cov-report=json:${baseline_dir}/coverage_after.json || true
} > "${baseline_dir}/quality_after.txt"

# 品質比較レポートを生成
echo "📋 品質改善レポートを生成中..."
quality_report="${baseline_dir}/quality_comparison.md"

cat > "$quality_report" << EOF
# リファクタリング品質レポート

## フィーチャー
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **Date**: $(date -u +%Y-%m-%dT%H:%M:%SZ)

## 品質メトリクス改善

### Ruff (コード品質)
EOF

# Ruff比較を追加
echo "#### Before:" >> "$quality_report"
echo '```' >> "$quality_report"
grep -E "(Found|Fixed)" "${baseline_dir}/quality_before.txt" || echo "No issues found" >> "$quality_report"
echo '```' >> "$quality_report"

echo "#### After:" >> "$quality_report"
echo '```' >> "$quality_report"
grep -E "(Found|Fixed)" "${baseline_dir}/quality_after.txt" || echo "No issues found" >> "$quality_report"
echo '```' >> "$quality_report"

# 利用可能な場合はテストカバレッジ比較を追加
if [[ -f "${baseline_dir}/coverage.json" && -f "${baseline_dir}/coverage_after.json" ]]; then
    before_coverage=$(jq -r '.totals.percent_covered // "N/A"' "${baseline_dir}/coverage.json")
    after_coverage=$(jq -r '.totals.percent_covered // "N/A"' "${baseline_dir}/coverage_after.json")

    cat >> "$quality_report" << EOF

### Test Coverage
- **Before**: ${before_coverage}%
- **After**: ${after_coverage}%
EOF
fi

echo "✅ 品質レポート生成完了: $quality_report"
````

## 10. **アーキテクチャ遵守の再検証**

```bash
# リファクタリング後のアーキテクチャを再検証
echo "🏗️ リファクタリング後のアーキテクチャ検証..."

if ! validate_architecture_compliance; then
    echo "❌ エラー: リファクタリング後にアーキテクチャ違反が検出されました"
    echo "🔄 アーキテクチャ違反を修正してからコミットしてください"
    execute_rollback
    exit 1
fi

# リファクタリング後のアーキテクチャスナップショットを作成
architecture_after="${baseline_dir}/architecture_after.json"
create_architecture_snapshot > "$architecture_after"

echo "✅ アーキテクチャ検証完了"
```

## 11. **最終テストスイート実行**

```bash
# 包括的な最終テストスイートを実行
echo "🧪 最終テストスイートを実行中..."

test_results_file="${baseline_dir}/final_test_results.txt"

# すべてのテストカテゴリを実行
{
    echo "=== UNIT TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/ -v --tb=short
    echo ""
    echo "=== INTEGRATION TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v --tb=short
    echo ""
    echo "=== E2E TESTS ==="
    PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v --tb=short
    echo ""
    echo "=== LINTING ==="
    uv run --frozen ruff check . --show-source
    echo ""
    echo "=== TYPE CHECKING ==="
    uv run --frozen pyright
} > "$test_results_file" 2>&1

if [[ $? -ne 0 ]]; then
    echo "❌ エラー: 最終テストスイートが失敗しました"
    echo "📋 詳細: $test_results_file"
    execute_rollback
    exit 1
fi

echo "✅ 全テスト成功"
```

## 12. **アトミックメタデータ更新**

```bash
# メタデータをアトミックに更新
echo "📊 メタデータを更新中..."

if [[ -f "$metadata_file" ]]; then
    # リファクタリングサイクルをカウント
    current_count=$(jq '.phases.refactor.refactoring_count // 0' "$metadata_file")
    new_count=$((current_count + 1))

    # 包括的なリファクタリング情報でメタデータを更新
    update_metadata_atomic "$metadata_file" "
        .phases.refactor.completed = true |
        .phases.refactor.completed_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phases.refactor.refactoring_count = ${new_count} |
        .phases.refactor.quality_report = \"${quality_report}\" |
        .phases.refactor.test_results = \"${test_results_file}\" |
        .updated_at = \"$(date -u +%Y-%m-%dT%H:%M:%SZ)\" |
        .phase = \"refactored\"
    "

    echo "✅ メタデータ更新完了（リファクタリング回数: ${new_count}）"
else
    echo "⚠️ 警告: メタデータファイルが見つかりません: $metadata_file"
fi
```

## 13. **ドキュメント生成**

```bash
# 包括的なリファクタリングドキュメントを生成
echo "📚 リファクタリングドキュメントを生成中..."

refactoring_doc="docs/refactoring/issue-${issue_list}-${feature_name}-refactor-${new_count}.md"
mkdir -p "$(dirname "$refactoring_doc")"

cat > "$refactoring_doc" << EOF
# リファクタリング レポート #${new_count}

## 概要
- **Issues**: #$(IFS=' #'; echo "${issue_numbers[*]}")
- **Feature**: ${feature_name}
- **Refactoring Cycle**: ${new_count}
- **Date**: $(date -u +%Y-%m-%dT%H:%M:%SZ)

## 実行された改善

### ドメイン層
- エンティティ・値オブジェクトの重複除去
- 共通動作のベースクラス抽出
- 複雑メソッドの簡素化
- ユビキタス言語の一貫性確保

### アプリケーション層
- ユースケース複雑度の削減
- 共通バリデーションロジックの抽出
- DTOコンバージョンの最適化

### インフラストラクチャ層
- データベースクエリの最適化
- 接続処理の改善
- 共通マッピングロジックの抽出

### プレゼンテーション層
- エラーレスポンスの標準化
- 共通バリデーションパターンの抽出
- API一貫性の向上

### 横断的関心事
- ログパターンの標準化
- エラーメッセージの改善
- パフォーマンス監視フックの追加
- 命名規則の一貫性確保

### テストコード
- テストの重複除去
- テストフィクスチャとビルダーの抽出
- テスト名と構成の改善
- エッジケーステストの追加

## 品質改善結果

$(cat "$quality_report")

## テスト結果

全テストスイートが成功しました。詳細は以下を参照:
- テスト結果: \`${test_results_file}\`

## アーキテクチャ検証

✅ DDD/Clean Architecture原則に準拠
- アーキテクチャスナップショット（前）: \`${architecture_snapshot}\`
- アーキテクチャスナップショット（後）: \`${architecture_after}\`

## 次のステップ

1. 追加のリファクタリングが必要な場合は \`/refactor ${issue_list}\` を再実行
2. 他の機能の開発を続ける場合は \`/use-case-status ${issue_list}\` で状況確認
3. レビューを開始する場合は \`/review-issue ${issue_list}\`

EOF

echo "✅ リファクタリングドキュメント生成完了: $refactoring_doc"
```

## 14. **ユースケースインデックス更新**

```bash
# リファクタリングステータスでユースケースインデックスを更新
echo "📋 ユースケースインデックスを更新中..."

if [[ -f "docs/use_cases/index.md" ]]; then
    feature_line="- \\[${feature_name}\\]"

    # リファクタリングフェーズステータスとサイクル数で更新
    sed -i "s|${feature_line}.*|${feature_line}($(basename ${spec_file})) - Issues: #$(IFS=' #'; echo \"${issue_numbers[*]}\") (Phase: refactored, TDD: REFACTOR ✅, Cycles: ${new_count})|" docs/use_cases/index.md

    echo "✅ インデックス更新完了"
else
    echo "⚠️ 警告: ユースケースインデックスが見つかりません"
fi
```

## 15. **GitHubイシュー更新**

```bash
# リファクタリング完了でGitHubイシューを更新
echo "📢 GitHubイシューを更新中..."

refactoring_summary="🔧 **リファクタリング完了（サイクル #${new_count}）**

✅ **実行された改善**:
- ドメイン層: 重複除去、共通動作抽出、複雑度削減
- アプリケーション層: ユースケース最適化、バリデーション統一
- インフラ層: クエリ最適化、接続処理改善
- プレゼンテーション層: API一貫性向上、エラー処理標準化
- テストコード: 重複除去、構成改善

📊 **品質改善**: 詳細レポートは \`${quality_report}\` を参照

🧪 **テスト状況**: 全テストスイートが成功

🏗️ **アーキテクチャ**: DDD/Clean Architecture原則に準拠

📚 **詳細ドキュメント**: \`${refactoring_doc}\`"

for issue_num in "${issue_numbers[@]}"; do
    if safe_gh_command "issue" "comment" "$issue_num" --body "$refactoring_summary"; then
        echo "✅ Issue #$issue_num にコメント追加完了"
    else
        echo "⚠️ 警告: Issue #$issue_num のコメント追加に失敗"
    fi
done
```

## 16. **トランザクションコミットとクリーンアップ**

```bash
# すべての変更をコミットしてクリーンアップ
echo "💾 変更をコミット中..."

# すべての変更を追加
git add -A

# 包括的なコミットメッセージを作成
commit_message="refactor: TDD REFACTOR phase for issues #$(IFS=' #'; echo "${issue_numbers[*]}")

Refactoring cycle #${new_count} completed for feature: ${feature_name}

Improvements:
- Domain layer: Removed duplication, extracted common behavior
- Application layer: Reduced complexity, unified validation
- Infrastructure layer: Optimized queries, improved connections
- Presentation layer: Standardized responses, improved consistency
- Tests: Reduced duplication, improved organization

Quality metrics and test results available in:
- Quality report: ${quality_report}
- Test results: ${test_results_file}
- Documentation: ${refactoring_doc}

Architecture compliance: ✅ Validated
Test status: ✅ All tests passing"

# 適切なメッセージでコミット
if git commit -m "$commit_message"; then
    echo "✅ Gitコミット完了"
else
    echo "⚠️ 警告: Gitコミットに失敗しました"
fi

# トランザクションをコミット
commit_transaction

echo "🎉 リファクタリング完了!"
echo ""
echo "📊 **リファクタリング サマリー**:"
echo "   - Issues: #$(IFS=' #'; echo "${issue_numbers[*]}")"
echo "   - Feature: ${feature_name}"
echo "   - Cycle: ${new_count}"
echo "   - Quality Report: ${quality_report}"
echo "   - Documentation: ${refactoring_doc}"
echo ""
echo "🔍 **次のステップ**:"
echo "   - 追加リファクタリング: /refactor ${issue_list}"
echo "   - 状況確認: /use-case-status ${issue_list}"
echo "   - レビュー開始: /review-issue ${issue_list}"
echo ""
echo "✅ TDD REFACTORフェーズが正常に完了しました"
```

## 重要な注意事項

### **安全性原則**

- リファクタリング中は常にテストがGREENであることを維持
- 各レイヤーのリファクタリング後に関連テストを実行
- 失敗時は自動的に安全な状態にロールバック
- アーキテクチャ違反は即座に検出・修正

### **品質保証**

- リファクタリング前後の品質メトリクス比較
- テストカバレッジの維持・向上
- パフォーマンス劣化の検出
- ドキュメンテーションの自動更新

### **チーム協力**

- 全操作の詳細ログ記録
- GitHubイシューでの進捗共有
- アーキテクチャ遵守の可視化
- 継続的な品質改善の追跡

**統合版リファクタリングコマンドにより、安全で確実なコード品質向上が実現されます！**

## 🚨 CLAUDE CODEに必須: シナリオ進化チェック

リファクタリング中に新パターン・制約・改善案発見時は
作業を中断して `/evolve-scenarios <feature-name>` を実行すること
重要: リファクタリングは新たな設計洞察の重要な源です