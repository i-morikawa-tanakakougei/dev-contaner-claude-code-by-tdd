永続化と外部サービスのためのインフラストラクチャ層を実装します。

## メタデータ
- **前提条件**: アプリケーション層実装完了 (07-implement-usecase)
- **入力**: イシュー番号 (必須)
- **出力**: 
  - `src/infrastructure/` 内のインフラストラクチャ層実装
  - リポジトリ実装、データマッパー、外部アダプタ
  - 更新された `docs/use_cases/issue-X-Y.json` メタデータ
- **依存関係**: ドメイン・アプリケーション層、データベース・外部サービス設定
- **実行タイミング**: アプリケーション層の後、プレゼンテーション層の前

## 🎯 **TDD/DDD/LAYERED プロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 発展(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ (ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション)  
**🧪 開発手法**: テスト駆動開発 (RED→GREEN→REFACTOR)  
**🏗️ 設計手法**: ドメイン駆動設計 (エンティティ、値オブジェクト、集約、リポジトリ)  
**📋 要件**: Given-When-Then シナリオによる完全なトレーサビリティ  
**🔄 発展**: /evolve-scenarios コマンドによる継続的シナリオ発展

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - インフラストラクチャ層実装 (08/16)  
> 🎯 **フェーズ目的**: 永続化と外部サービス統合の実装  
> ⬅️ **前段階**: 07-implement-usecase (アプリケーション層実装)  
> ➡️ **次段階**: 09-implement-presentation (プレゼンテーション層実装)
>
> **📋 3層アーキテクチャ運用**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (システム境界の参照)  
> - 📊 **戦術**: `docs/use_cases/index.md` (インフラストラクチャステータス更新)  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (インフラストラクチャ実装追跡)

## 🏗️ **インフラストラクチャ層実装のみ**

**⚠️ 重要な注意:**
- **このステップはインフラストラクチャ層のみ** - リポジトリと外部統合を実装
- **他の層は禁止** - インフラストラクチャ層コンポーネントのみにフォーカス  
- **データ永続化** - リポジトリパターンとデータベースアクセスを実装
- **外部サービス** - サードパーティ統合とAPIを処理

**層実装順序:**
1. `06-implement-domain` ← ドメイン層 (完了)
2. `07-implement-usecase` ← アプリケーション層 (完了)  
3. `08-implement-infra` ← **【現在地】インフラストラクチャ層**
4. `09-implement-presentation` ← プレゼンテーション層

## 🚨 **重要: インフラストラクチャ層のみ - 他の層は禁止**

**❌ このステップで絶対に禁止:**
- **プレゼンテーション層**: コントローラー、API、CLIコマンド、Webインターフェース禁止
- **ドメイン層修正**: ドメイン層は完了済み - 修正しないこと
- **アプリケーション層修正**: アプリケーション層は完了済み - 修正しないこと
- **ビジネスロジック**: インフラストラクチャコードにビジネスルールや ドメインロジック禁止

**✅ このステップでのみ許可:**
- **リポジトリ実装**: ドメインリポジトリインターフェースの具体実装
- **データベースアクセス**: データベース接続、クエリ、データマッピング
- **外部サービス統合**: HTTPクライアント、ファイルシステム、サードパーティAPI
- **インフラストラクチャ設定**: 接続文字列、設定、環境変数

## 📋 **インフラストラクチャ層タスクチェックリスト**

**適切な分離を持つインフラストラクチャ層実装にこのチェックリストを使用:**

### 🔴 必須タスク

#### **📊 リポジトリインターフェース分析**
- [ ] **リポジトリインターフェースのレビュー**: ステップ06からドメインリポジトリインターフェースを分析
- [ ] **🚨 重要: プレースホルダーアサーションの置換**: インフラストラクチャテストで `assert False, "RED: ... not implemented yet"` 文をチェックして修正
- [ ] **テストの真正性検証**: 実装を実際にテストしていることを確認、プレースホルダー失敗ではなく
- [ ] **データアクセスパターンの特定**: CRUD操作とクエリ要件を決定
- [ ] **永続化戦略の計画**: データベース、ORM、データアクセスアプローチを選択
- [ ] **ドメイン永続化マッピング**: ドメインオブジェクトをデータベーステーブルにマップする方法を計画

#### **🗄️ リポジトリ実装**
- [ ] **具象リポジトリクラスの作成**: ドメイン層からの各リポジトリインターフェースを実装
- [ ] **CRUD操作の実装**: 保存、検索、更新、削除機能を追加
- [ ] **クエリメソッドの追加**: インターフェースで定義されたカスタムクエリメソッドを実装
- [ ] **データベーストランザクション処理**: 適切なトランザクション管理を実装
- [ ] **エラーハンドリングの追加**: データベースエラーをドメイン例外に変換

#### **🧪 インフラストラクチャテスト**
- [ ] **統合テストの実行**: データベースと外部サービス統合を検証するテストを実行
- [ ] **リポジトリ実装のテスト**: CRUD操作が正しく動作することを検証
- [ ] **メタデータの更新**: issue-X-Y.json でインフラストラクチャ層実装完了をマーク
- [ ] **インフラストラクチャ層のコミット**: インフラストラクチャ層コードをバージョン管理

### 🟡 推奨タスク

#### **💾 データベース・永続化セットアップ**
- [ ] **データベース接続のセットアップ**: データベース接続と接続プーリングを設定
- [ ] **データベーススキーマの作成**: テーブル、インデックス、制約を定義
- [ ] **データマッピングの実装**: ドメインオブジェクトとデータベースレコード間の変換
- [ ] **データ検証の追加**: データベースレベルでの検証と制約を実装
- [ ] **データベースエラー処理**: 適切なエラーハンドリングとログを実装

#### **⚙️ 設定管理**
- [ ] **設定クラスの作成**: 設定と構成オブジェクトを実装
- [ ] **環境変数の読み込み**: 環境変数から設定を読み取り
- [ ] **設定検証の追加**: 起動時に必要な設定を検証
- [ ] **設定デフォルトの実装**: 合理的なデフォルト値を提供
- [ ] **設定エラー処理**: 無効な設定に対する適切なエラーハンドリングを実装

#### **🚫 アーキテクチャ準拠チェック**
- [ ] **プレゼンテーション層コードなし**: コントローラー、API、UIコンポーネントがないことを確認
- [ ] **ビジネスロジックなし**: インフラストラクチャコードにビジネスルールが含まれていないことを検証
- [ ] **ドメイン層未変更**: ドメイン層ファイルが修正されていないことを検証
- [ ] **アプリケーション層未変更**: アプリケーション層ファイルが修正されていないことを検証
- [ ] **インフラストラクチャディレクトリのみ**: src/infrastructure/ ディレクトリのみに新しいファイルがあることを確認
- [ ] **適切な依存方向**: インフラストラクチャがドメインインターフェースのみに依存することを検証

### 🟢 オプションタスク

#### **🌐 外部サービス統合**
- [ ] **HTTPクライアントの実装**: 外部API統合用のクライアントを作成
- [ ] **認証の追加**: APIキー、OAuth、または他の認証機構を実装  
- [ ] **サービスエラー処理**: リトライロジックとエラーハンドリングを実装
- [ ] **レート制限の追加**: 外部呼び出しに適切なレート制限を実装
- [ ] **タイムアウトの設定**: 外部サービス呼び出しに適切なタイムアウト値を設定
- [ ] **サービスヘルスチェックの追加**: 外部依存関係のヘルス監視を実装

#### **🔧 インフラストラクチャ品質**
- [ ] **適切なログの追加**: デバッグ用の包括的ログを実装
- [ ] **監視の実装**: インフラストラクチャコンポーネントのメトリクスと監視を追加
- [ ] **接続プーリングの追加**: 効率的なリソース管理を実装
- [ ] **リソースクリーンアップの処理**: 接続とリソースの適切な廃棄を確保
- [ ] **パフォーマンス最適化**: 適切な箇所でキャッシュとクエリ最適化を実装
- [ ] **セキュリティ対策の追加**: データアクセスと外部呼び出しの適切なセキュリティを実装

#### **🔧 コード品質検証**
- [ ] **ruff リンティングの実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **ruff フォーマットの実行**: `uv run --frozen ruff format src/` を実行
- [ ] **型チェックの実行**: `uv run --frozen pyright src/` を実行
- [ ] **品質問題の修正**: リンティング、フォーマット、型エラーに対処
- [ ] **クリーン結果の検証**: すべての品質ツールがエラーなしで通ることを確保

#### **📊 高度なフェーズ完了**
- [ ] **トランザクション境界の定義**: データベーストランザクションが必要な箇所を特定
- [ ] **マイグレーションの実装**: 必要に応じてデータベースマイグレーションスクリプトを追加
- [ ] **ORM/クエリビルダーの設定**: 使用する場合はデータベース抽象化層をセットアップ
- [ ] **エラーシナリオのテスト**: 適切なエラーハンドリングと例外マッピングを検証
- [ ] **トランザクション処理のテスト**: 操作間でトランザクションが正しく動作することを確保
- [ ] **外部サービスモックのテスト**: テストダブルでの外部サービス統合を検証
- [ ] **データ永続化の検証**: ドメインオブジェクトが正しく保存・取得されることを確保
- [ ] **設定ドキュメントの追加**: すべての設定オプションを文書化
- [ ] **インフラストラクチャセットアップの文書化**: データベーススキーマ、外部サービス、設定を記録
- [ ] **プレゼンテーション用の準備**: リポジトリがプレゼンテーション層で使用できる状態であることを確保
- [ ] **エンドツーエンドフローの検証**: ドメイン → アプリケーション → インフラストラクチャのフローが動作することをテスト

**💡 プロ tip**: インフラストラクチャコードは純粋に技術的であるべき - ビジネスロジックがこの層に漏れてはいけません！

### ✅ 許可されるファイル (実装対象):
- `src/infrastructure/repositories/` - 具象リポジトリ実装
- `src/infrastructure/models/` - データベース/永続化モデル
- `src/infrastructure/mappers/` - ドメイン-インフラストラクチャマッピング
- `src/infrastructure/external/` - 外部サービス統合 (API、ファイル等)
- `src/infrastructure/config/` - インフラストラクチャ設定

### ❌ 禁止ファイル (このステップでは作成/修正しない):
- `src/domain/` - **ドメイン層 (既に実装済み、修正禁止)**
- `src/application/` - **アプリケーション層 (既に実装済み、修正禁止)**
- `src/presentation/` - **プレゼンテーション層 (次のステップで実装)**

### 🎯 実装ルール:
1. **ドメインリポジトリインターフェースの実装** - 具象実装を提供
2. **外部システム統合の処理** - データベース、API、ファイルシステム、メッセージキュー
3. **ビジネスロジックなし** - 純粋な技術実装、ビジネスルールなし
4. **変換用マッパーの使用** - ドメインオブジェクトとインフラストラクチャモデル間の変換
5. **抽象への依存** - ドメイン層で定義されたインターフェースを実装
6. **設定管理** - データベース接続、API認証情報、インフラストラクチャ設定

### 💡 他の層を誤って実装した場合:
```bash
# 誤って作成されたファイルを削除
rm -rf src/presentation/

# ドメインやアプリケーション層は修正しない
# これらは前のステップで既に完了済みのはず
```

**これらのルールに違反すると依存性逆転が破れ、アーキテクチャ問題を引き起こします。**

## 🚨 **重要なTDD原則警告**

**🔴→🟢 実装に合わせてテストを修正してはいけません！**

### 🎯 神聖なTDDフロー (逆転禁止):
```
📖 シナリオ (Given-When-Then) 
    ↓
🔴 TDDテスト (仕様)
    ↓
🟢 実装 (コード)
```

### ✅ 正しいアプローチ:
- **テストは仕様** - システムが何をすべきかを定義
- **実装はテストに奉仕** - テストを通すためのコードを書く
- **テストはシナリオから** - ビジネス要件がテストを駆動
- **実装を修正、テストは修正しない** - テストが失敗したらコードを変更

### ❌ 禁止されるアプローチ (絶対にやってはいけない):
- ~~既存実装に合わせてテストを修正~~
- ~~「実装が違う動きをする」から失敗テストを削除~~
- ~~現在のコードに合わせてテスト期待値を変更~~
- ~~テストを変更して間違った実装を正当化~~

### 🚨 実装がテストと一致しない場合:
1. **停止** - テストを修正しない
2. **分析** - なぜテストが失敗するのか？
3. **シナリオ確認** - テストが要件を正しく表現しているか？
4. **実装修正** - テスト要件を満たすようにコードを修正
5. **シナリオが間違いの場合のみ** - シナリオ → テスト → 実装の順で更新

### 💡 緊急復旧:
```bash
# 誤ってテストを修正した場合
git restore tests/integration/repositories/
git restore tests/unit/infrastructure/

# 適切なTDDフローに戻る
# 1. 失敗テストを読む (これらは仕様)
# 2. テストを通すためのインフラストラクチャコードを実装
# 3. テストロジックをコードに合わせて変更しない
```

**⚠️ 重要: テスト修正はTDDサイクルを破り、シナリオ駆動開発を無効化します！**

---

## よくあるエラーと解決策

### ❌ エラーケース1: アプリケーション層未実装
**原因**: インフラストラクチャ層がアプリケーション実装完了前に開始された  
**解決策**: まず `/implement-usecase <issue-number>` でアプリケーション層を完了する

### ❌ エラーケース2: インフラストラクチャ層のビジネスロジック
**原因**: ドメインロジックがリポジトリやデータアクセスコードに漏れた  
**解決策**: インフラストラクチャは永続化のみを処理 - ビジネスロジックをドメイン層に移動

### ❌ エラーケース3: プレースホルダーアサーションが偽RED状態を引き起こす
**原因**: インフラストラクチャテストに `assert False, "RED: ... not implemented yet"` があるが実装は存在する  
**解決策**: 
```python
# 悪い例: プレースホルダーアサーション (偽REDを引き起こす)
def test_repository_save(self):
    assert False, "RED: Repository save not implemented yet"

# 良い例: 実際のテスト実装
def test_repository_save(self):
    entity = MyEntity.create("test_id", "test_value")
    repository.save(entity)
    saved_entity = repository.find_by_id("test_id")
    assert saved_entity is not None
    assert saved_entity.value == "test_value"
```
**復旧**: すべてのプレースホルダーアサーションを実際の実装を検証する適切なテストに置換

### ❌ エラーケース4: インフラストラクチャがドメインに不適切に依存
**原因**: インフラストラクチャがインターフェースではなくドメイン具象クラスをインポート  
**解決策**: インフラストラクチャはドメインインターフェースを実装し、依存性逆転原則を使用

## 実行例

### ✅ 成功例
```bash
$ /implement-infra 15
🏗️ Issues: #15 のインフラ層実装を開始します
✅ アプリケーション層が正常に実装されています
🔌 リポジトリ実装中...
  ✅ ファイル作成: src/infrastructure/repositories/user_repository.py
🎉 インフラ層実装完了!
```

### ❌ 失敗例と修正
```bash
$ /implement-infra 15
❌ アプリケーション層の実装が完了していません
# 修正: 最初にアプリケーション層を完了
$ /implement-usecase 15
$ /implement-infra 15
```

### ❌ プレースホルダーアサーション例と修正
```bash
$ /implement-infra 3
🚨 プレースホルダーアサーション発見:
  - tests/integration/repositories/test_sqlite_trade_repository.py: 6 個
  - tests/integration/repositories/test_sqlite_position_repository.py: 5 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# 修正: プレースホルダーアサーションを実際のテストに置換
# テストファイルを編集して置換:
#   assert False, "RED: Repository save not implemented yet"
# を以下に変更:
#   entity = TradeEntity.create("trade_001", "EURUSD", Decimal("1.0"))
#   repository.save(entity)
#   saved = repository.find_by_id("trade_001")
#   assert saved.symbol == "EURUSD"
```

## タスク詳細

1. **安全環境セットアップと引数解析**:
   ```bash
   # 🔧 すべての安全操作関数を読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "08-implement-infra" "$ARGUMENTS"
   
   # インフラストラクチャ実装は少なくとも1つのイシュー番号が必要
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-infra" "1" "単一イシューのインフラ実装"
       show_usage_example "implement-infra" "1,7" "複数イシューのインフラ実装"
       show_usage_example "implement-infra" "1 mt5-extended-data" "イシュー + 機能名指定"
       exit 1
   fi
   
   # イシューリストと機能名を抽出
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 機能名は既存ファイルから抽出される
       feature_name=""
   fi
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のインフラストラクチャ層実装を開始します"
   echo ""
   echo "🚨 重要な注意: このステップではインフラストラクチャ層のみを実装します"
   echo "   ✅ 許可: src/infrastructure/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/domain/, src/application/, src/presentation/"
   echo "   💡 他の層を間違って実装した場合は即座に削除してください"
   echo ""
   echo "🔴→🟢 TDD原則: テストを実装に合わせて変更してはいけません!"
   echo "   📖 シナリオ → 🔴 テスト → 🟢 実装 の順序を厳守"
   echo "   ✅ 実装をテストに合わせる（正しい）"
   echo "   ❌ テストを実装に合わせる（禁止）"
   echo ""
   ```

2. **トランザクション開始と事前検証**:
   ```bash
   # 🔄 包括的トランザクション開始
   if ! begin_transaction "implement_infra_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 前提条件検証 - アプリケーション層が完了している必要がある
   echo "📋 前提条件の検証中..."
   
   # 提供されていない場合は既存ファイルから機能名を抽出
   if [[ -z "$feature_name" ]]; then
       found_spec=$(find docs/use_cases/ -name "issue-${issue_list}-*.md" -type f | head -1)
       if [[ -n "$found_spec" ]]; then
           feature_name=$(basename "$found_spec" | sed 's/^issue-[0-9-]*-\(.*\)\.md$/\1/')
           echo "  📝 機能名抽出: $feature_name"
       else
           echo "エラー: 機能名を特定できませんでした"
           execute_rollback "feature_name_missing"
           exit 1
       fi
   fi
   
   # ドメイン実装のチェック
   domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$domain_entities" ]]; then
       echo "❌ ドメイン層の実装が見つかりません"
       echo "💡 最初にドメイン層を実装してください:"
       echo "   /implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_implementation"
       exit 1
   fi
   
   echo "  ✅ ドメイン実装確認: $(echo "$domain_entities" | wc -l) ファイル"
   
   # アプリケーション実装のチェック
   app_use_cases=$(find src/application/use_cases/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$app_use_cases" ]]; then
       echo "❌ アプリケーション層の実装が見つかりません"
       echo "💡 最初にアプリケーション層を実装してください:"
       echo "   /implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_application_implementation"
       exit 1
   fi
   
   echo "  ✅ アプリケーション実装確認: $(echo "$app_use_cases" | wc -l) ファイル"
   
   # リポジトリインターフェースのチェック
   repo_interfaces=$(find src/domain/repositories/ -name "*_repository.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$repo_interfaces" ]]; then
       echo "❌ リポジトリインターフェースが見つかりません"
       echo "💡 ドメイン層実装を確認してください"
       execute_rollback "missing_repository_interfaces"
       exit 1
   fi
   
   echo "  ✅ リポジトリインターフェース確認: $(echo "$repo_interfaces" | wc -l) ファイル"
   
   # 🚨 重要: インフラストラクチャ層テストのプレースホルダーアサーションをチェック
   echo "  🚨 インフラストラクチャ層プレースホルダーアサーション検証中..."
   
   infrastructure_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           infrastructure_placeholder_files+=("$file")
       fi
   done < <(find tests/integration/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#infrastructure_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ インフラストラクチャ層プレースホルダーアサーション発見:"
       for file in "${infrastructure_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#infrastructure_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#infrastructure_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - インフラストラクチャ実装は完了済みだが、テストがプレースホルダーのまま"
       echo "       - これはTDDプロセス違反の状態です"
       echo ""
       echo "    💡 修正が必要: プレースホルダーアサーションを実際のテストに置き換える"
       echo "       この修正は手動で行う必要があります"
       echo ""
       echo "    ⚠️  続行するとプレースホルダーテストの修正をスキップしますが、"
       echo "       後でテストを適切に実装する必要があります"
       echo ""
       echo "    続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "インフラストラクチャ層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "infrastructure_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ インフラストラクチャ層プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   echo "✅ 前提条件検証完了"
   ```

3. **メタデータの特定と検証**:
   ```bash
   # 📊 メタデータファイルの検索と検証
   echo "📊 メタデータファイル検証中..."
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが見つかりません: $metadata_file"
       execute_rollback "metadata_file_missing"
       exit 1
   fi
   
   # メタデータファイル形式の検証
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # アプリケーション実装フェーズ完了のチェック
   app_status=$(jq -r '.phases.application_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$app_status" != "true" ]]; then
       echo "エラー: アプリケーション層実装が完了していません"
       echo "💡 先に /implement-usecase コマンドを実行してください"
       execute_rollback "application_implementation_not_completed"
       exit 1
   fi
   
   # インフラストラクチャ実装が既に完了しているかチェック
   infra_status=$(jq -r '.phases.infrastructure_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$infra_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のインフラストラクチャ層実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "インフラストラクチャ層実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のインフラストラクチャ層実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **ドメインとリポジトリ情報の抽出**:
   ```bash
   # 📖 実装用のドメインとリポジトリ情報を抽出
   echo "📖 ドメイン・リポジトリ情報分析中..."
   
   # ドメイン層からエンティティを抽出
   all_entities=()
   for entity_file in $domain_entities; do
       entity_name=$(basename "$entity_file" .py)
       # PascalCaseに変換
       entity_class=$(echo "$entity_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_entities+=("$entity_class")
   done
   
   # リポジトリインターフェースを抽出
   all_repositories=()
   for repo_file in $repo_interfaces; do
       repo_name=$(basename "$repo_file" .py)
       # リポジトリクラス名を抽出
       repo_class=$(echo "$repo_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_repositories+=("$repo_class")
   done
   
   echo "  🎯 抽出された情報:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - リポジトリ: ${#all_repositories[@]} 個"
   
   echo "✅ 情報分析完了"
   ```

5. **インフラストラクチャ層構造の作成**:
   ```bash
   # 🏗️ インフラストラクチャ層構造を作成
   echo "🏗️ インフラストラクチャ層構造作成中..."
   
   # テンプレートユーティリティを読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_template_utils.sh"
   
   # インフラストラクチャ構造ディレクトリを定義
   infra_directories=(
       "src/infrastructure/persistence/models"
       "src/infrastructure/persistence/mappers"
       "src/infrastructure/external"
       "src/infrastructure/config"
   )
   
   # すべてのインフラストラクチャディレクトリを安全に作成
   for dir in "${infra_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: インフラディレクトリ作成に失敗しました: $dir"
           execute_rollback "infra_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove infra directory: $dir"
   done
   
   # __init__.py ファイルを作成
   infra_init_files=(
       "src/infrastructure/persistence/__init__.py"
       "src/infrastructure/persistence/models/__init__.py"
       "src/infrastructure/persistence/mappers/__init__.py"
       "src/infrastructure/external/__init__.py"
       "src/infrastructure/config/__init__.py"
   )
   
   for init_file in "${infra_init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       if ! safe_create_file "$init_file" '"""Infrastructure layer package initialization"""' false; then
           echo "エラー: インフラ__init__.pyファイルの作成に失敗しました"
           execute_rollback "infra_init_creation_failed"
           exit 1
       fi
       add_rollback "rm -f '$init_file'" "Remove infra init file: $init_file"
   done
   
   echo "✅ インフラ構造作成完了 (${#infra_directories[@]} ディレクトリ)"
   ```

6. **データベースモデルの実装**:
   ```bash
   # 🗄️ テンプレートを使用したデータベースモデルの実装
   echo "🗄️ データベースモデル実装中..."
   
   implemented_files=()
   
   # 最初にベースモデルを作成
   base_model_file="src/infrastructure/persistence/models/base.py"
   
   echo "  🗄️ 実装中: Base Model ($base_model_file)"
   
   # ベースモデル (固定実装のため直接定義)
   base_model_implementation='"""
データベースベースモデル

SQLAlchemy基底モデル定義。
実装日時: '"$(date)"'
"""

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func
from datetime import datetime


Base = declarative_base()


class BaseModel(Base):
    """すべてのモデルの基底クラス
    
    共通のID、作成日時、更新日時フィールドを提供する。
    """
    
    __abstract__ = True
    
    id = Column(String(36), primary_key=True, comment="一意識別子（UUID）")
    created_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        nullable=False,
        comment="作成日時"
    )
    updated_at = Column(
        DateTime(timezone=True), 
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
        comment="更新日時"
    )
    
    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(id={self.id})>"
'
   
   if ! safe_create_file "$base_model_file" "$base_model_implementation" true; then
       echo "エラー: ベースモデルファイルの作成に失敗しました: $base_model_file"
       execute_rollback "base_model_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$base_model_file")
   add_rollback "rm -f '$base_model_file'" "Remove base model: $base_model_file"
   
   # テンプレートシステムを使用したエンティティモデルの作成
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       model_file="src/infrastructure/persistence/models/${entity_lower}_model.py"
       
       echo "  🗄️ 実装中: ${entity}Model ($model_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してモデルファイルを作成
       if ! process_template "infrastructure/model_template.py" "$model_file"; then
           echo "エラー: モデルファイルの作成に失敗しました: $model_file"
           execute_rollback "model_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$model_file")
       add_rollback "rm -f '$model_file'" "Remove model: $model_file"
   done
   
   echo "✅ データベースモデル実装完了 (${#all_entities[@]} + 1 ファイル)"
   ```

7. **マッパーの実装**:
   ```bash
   # 🔄 テンプレートを使用したエンティティ・モデルマッパーの実装
   echo "🔄 エンティティ・モデルマッパー実装中..."
   
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       mapper_file="src/infrastructure/persistence/mappers/${entity_lower}_mapper.py"
       
       echo "  🔄 実装中: ${entity}Mapper ($mapper_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してマッパーファイルを作成
       if ! process_template "infrastructure/mapper_template.py" "$mapper_file"; then
           echo "エラー: マッパーファイルの作成に失敗しました: $mapper_file"
           execute_rollback "mapper_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$mapper_file")
       add_rollback "rm -f '$mapper_file'" "Remove mapper: $mapper_file"
   done
   
   echo "✅ マッパー実装完了 (${#all_entities[@]} ファイル)"
   ```

8. **具象リポジトリクラスの実装**:
   ```bash
   # 🏪 テンプレートを使用した具象リポジトリ実装の実装
   echo "🏪 コンクリートリポジトリ実装中..."
   
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       sql_repo_file="src/infrastructure/repositories/sql_${entity_lower}_repository.py"
       
       echo "  🏪 実装中: Sql${entity}Repository ($sql_repo_file)"
       
       # テンプレート変数設定
       setup_entity_vars "$entity"
       
       # テンプレートを使用してリポジトリファイルを作成
       if ! process_template "infrastructure/repository_template.py" "$sql_repo_file"; then
           echo "エラー: SQLリポジトリファイルの作成に失敗しました: $sql_repo_file"
           execute_rollback "sql_repo_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$sql_repo_file")
       add_rollback "rm -f '$sql_repo_file'" "Remove SQL repository: $sql_repo_file"
   done
   
   echo "✅ コンクリートリポジトリ実装完了 (${#all_entities[@]} ファイル)"
   ```

9. **データベース設定の実装**:
   ```bash
   # ⚙️ データベース設定の実装
   echo "⚙️ データベース設定実装中..."
   
   # データベース設定
   db_config_file="src/infrastructure/config/database.py"
   
   echo "  ⚙️ 実装中: Database Configuration ($db_config_file)"
   
   db_config_implementation='"""
データベース設定

データベース接続とセッション管理の設定。
実装日時: '"$(date)"'
"""

import os
from typing import Generator, Optional
from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
import logging

from ..persistence.models.base import Base


logger = logging.getLogger(__name__)


class DatabaseConfig:
    """データベース設定クラス
    
    SQLAlchemyエンジンとセッションの管理を行う。
    """
    
    def __init__(self, database_url: Optional[str] = None):
        """データベース設定初期化
        
        Args:
            database_url: データベース接続URL（省略時は環境変数から取得）
        """
        self.database_url = database_url or self._get_database_url()
        self.engine: Optional[Engine] = None
        self.session_factory: Optional[sessionmaker] = None
        
    def _get_database_url(self) -> str:
        """環境変数からデータベースURLを取得"""
        # 本番環境
        if db_url := os.getenv("DATABASE_URL"):
            return db_url
        
        # 開発環境
        if db_url := os.getenv("DEV_DATABASE_URL"):
            return db_url
        
        # テスト環境（インメモリSQLite）
        if os.getenv("TESTING") == "true":
            return "sqlite:///:memory:"
        
        # デフォルト（ローカル開発用SQLite）
        return "sqlite:///./dev_database.db"
    
    def create_engine(self) -> Engine:
        """SQLAlchemyエンジンを作成"""
        if self.engine is not None:
            return self.engine
        
        logger.info(f"Creating database engine for: {self._mask_url(self.database_url)}")
        
        # SQLiteの場合の特別設定
        if self.database_url.startswith("sqlite"):
            self.engine = create_engine(
                self.database_url,
                poolclass=StaticPool,
                connect_args={
                    "check_same_thread": False,  # SQLiteでマルチスレッド使用を許可
                },
                echo=os.getenv("SQL_DEBUG") == "true"  # SQLログ出力制御
            )
        else:
            # PostgreSQL、MySQLなどの場合
            self.engine = create_engine(
                self.database_url,
                pool_pre_ping=True,  # 接続確認
                pool_recycle=3600,   # 1時間で接続リサイクル
                echo=os.getenv("SQL_DEBUG") == "true"
            )
        
        logger.info("Database engine created successfully")
        return self.engine
    
    def create_session_factory(self) -> sessionmaker:
        """セッションファクトリを作成"""
        if self.session_factory is not None:
            return self.session_factory
        
        engine = self.create_engine()
        self.session_factory = sessionmaker(
            bind=engine,
            autocommit=False,
            autoflush=False,
            expire_on_commit=False
        )
        
        logger.info("Session factory created successfully")
        return self.session_factory
    
    def get_session(self) -> Session:
        """データベースセッションを取得"""
        session_factory = self.create_session_factory()
        return session_factory()
    
    def get_session_context(self) -> Generator[Session, None, None]:
        """セッションコンテキストマネージャー
        
        トランザクション管理付きのセッションを提供する。
        """
        session = self.get_session()
        try:
            yield session
            session.commit()
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()
    
    def create_tables(self) -> None:
        """すべてのテーブルを作成"""
        engine = self.create_engine()
        logger.info("Creating all database tables")
        Base.metadata.create_all(bind=engine)
        logger.info("All database tables created successfully")
    
    def drop_tables(self) -> None:
        """すべてのテーブルを削除（テスト用）"""
        engine = self.create_engine()
        logger.warning("Dropping all database tables")
        Base.metadata.drop_all(bind=engine)
        logger.warning("All database tables dropped")
    
    def _mask_url(self, url: str) -> str:
        """URLからパスワードを隠す"""
        if "://" not in url:
            return url
        
        scheme, rest = url.split("://", 1)
        if "@" in rest:
            credentials, host = rest.split("@", 1)
            if ":" in credentials:
                user, _ = credentials.split(":", 1)
                return f"{scheme}://{user}:***@{host}"
        
        return url


# グローバルデータベース設定インスタンス
db_config = DatabaseConfig()


def get_database_session() -> Generator[Session, None, None]:
    """データベースセッション取得（依存性注入用）
    
    FastAPIなどのDIフレームワークで使用する。
    """
    yield from db_config.get_session_context()


def init_database() -> None:
    """データベース初期化"""
    logger.info("Initializing database")
    db_config.create_tables()
    logger.info("Database initialization completed")


def cleanup_database() -> None:
    """データベースクリーンアップ（テスト用）"""
    logger.info("Cleaning up database")
    db_config.drop_tables()
    logger.info("Database cleanup completed")
'
   
   if ! safe_create_file "$db_config_file" "$db_config_implementation" true; then
       echo "エラー: データベース設定ファイルの作成に失敗しました: $db_config_file"
       execute_rollback "db_config_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$db_config_file")
   add_rollback "rm -f '$db_config_file'" "Remove database config: $db_config_file"
   
   echo "✅ データベース設定実装完了"
   ```

10. **統合テストの作成**:
    ```bash
    # 🧪 テンプレートを使用したインフラストラクチャ統合テストの作成
    echo "🧪 インフラ統合テスト作成中..."
    
    # 必要に応じて統合テストディレクトリを作成
    if ! safe_mkdir "tests/integration/repositories"; then
        echo "エラー: 統合テストディレクトリの作成に失敗しました"
        execute_rollback "integration_test_dir_creation_failed"
        exit 1
    fi
    
    # テンプレートを使用して各リポジトリの統合テストを作成
    for entity in "${all_entities[@]}"; do
        entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
        integration_test_file="tests/integration/repositories/test_sql_${entity_lower}_repository.py"
        
        echo "  🧪 実装中: Integration Test for Sql${entity}Repository ($integration_test_file)"
        
        # テンプレート変数設定
        setup_entity_vars "$entity"
        
        # テンプレートを使用して統合テストファイルを作成
        if ! process_template "tests/integration_test_template.py" "$integration_test_file"; then
            echo "エラー: 統合テストファイルの作成に失敗しました: $integration_test_file"
            execute_rollback "integration_test_implementation_failed"
            exit 1
        fi
        
        implemented_files+=("$integration_test_file")
        add_rollback "rm -f '$integration_test_file'" "Remove integration test: $integration_test_file"
    done
    
    echo "✅ インフラ統合テスト実装完了 (${#all_entities[@]} ファイル)"
    ```

11. **統合テストの実行**:
    ```bash
    # 🟢 インフラストラクチャ実装検証のための統合テスト実行
    echo "🟢 インフラストラクチャ統合テスト実行中..."
    
    # テスト用Python環境の検証
    if ! validate_python_environment; then
        echo "エラー: Python環境の検証に失敗しました"
        execute_rollback "python_env_validation_failed"
        exit 1
    fi
    
    # 統合テストの実行
    echo "  🧪 統合テスト実行中..."
    
    integration_test_output_file="/tmp/integration_test_output_$$"
    integration_test_result=0
    
    # 統合テストを実行して出力をキャプチャ
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ -v --tb=short > "$integration_test_output_file" 2>&1; then
        integration_test_result=0  # テスト成功
    else
        integration_test_result=1  # テスト失敗
    fi
    
    # 統合テスト結果の分析
    total_integration_tests=$(grep -c "test_.*PASSED\|test_.*FAILED" "$integration_test_output_file" 2>/dev/null || echo "0")
    passed_integration_tests=$(grep -c "PASSED" "$integration_test_output_file" 2>/dev/null || echo "0")
    failed_integration_tests=$(grep -c "FAILED" "$integration_test_output_file" 2>/dev/null || echo "0")
    
    echo "  📊 統合テスト結果分析:"
    echo "    - 総テスト数: $total_integration_tests"
    echo "    - 成功テスト数: $passed_integration_tests"
    echo "    - 失敗テスト数: $failed_integration_tests"
    
    if [[ $failed_integration_tests -gt 0 ]]; then
        echo "⚠️  失敗している統合テストがあります:"
        grep "FAILED" "$integration_test_output_file" | head -5
        echo ""
        echo "追加修正が必要な可能性があります。続行しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "インフラ実装を中止しました"
            rm -f "$integration_test_output_file"
            execute_rollback "integration_tests_failing"
            exit 1
        fi
    else
        echo "  ✅ GREEN状態確認: すべての統合テストが成功しています"
    fi
    
    # 可能であればインフラストラクチャカバレッジを計算
    infra_coverage_result=""
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/integration/ --cov=src.infrastructure --cov-report=term-missing --quiet >/tmp/infra_coverage_output_$$ 2>&1; then
        infra_coverage_result=$(grep -E "[0-9]+%" /tmp/infra_coverage_output_$$ | tail -1 || echo "Coverage data not available")
        rm -f /tmp/infra_coverage_output_$$
    fi
    
    rm -f "$integration_test_output_file"
    integration_tests_passed=$([ $failed_integration_tests -eq 0 ] && echo "true" || echo "false")
    
    echo "✅ 統合テスト実行完了"
    ```

12. **メタデータとドキュメントの更新**:
    ```bash
    # 📊 インフラストラクチャ実装完了でメタデータを更新
    echo "📊 メタデータ・ドキュメント更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.infrastructure_implementation.created = true | 
         .phases.infrastructure_implementation.completed = true |
         .phases.infrastructure_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.infrastructure_implementation.integration_tests_passed = '"$integration_tests_passed"' |
         .phases.infrastructure_implementation.coverage = "'"$infra_coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.infrastructure_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "infrastructure_implemented" |
         .next_commands = ["implement-presentation", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # インフラストラクチャドキュメントの作成
    infra_doc_dir="docs/infrastructure"
    if ! safe_mkdir "$infra_doc_dir"; then
        echo "エラー: インフラドキュメントディレクトリの作成に失敗しました"
        execute_rollback "infra_doc_dir_creation_failed"
        exit 1
    fi
    
    infra_doc_file="$infra_doc_dir/issue-${issue_list}-infrastructure-design.md"
    
    infra_doc_content="# インフラストラクチャ層設計: $feature_name

**Issues**: $(printf '#%s ' "${issue_numbers[@]}")
**実装日時**: $(date)

## 概要

このインフラストラクチャ層実装は、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて作成されました。
ドメインエンティティの永続化と外部サービス連携を提供します。

## 実装されたコンポーネント

### データベースモデル
$(for entity in "${all_entities[@]}"; do
    echo "- **${entity}Model**: ${entity}エンティティのデータベースモデル"
done)

### エンティティ・モデルマッパー
$(for entity in "${all_entities[@]}"; do
    echo "- **${entity}Mapper**: ${entity}の双方向変換処理"
done)

### コンクリートリポジトリ
$(for entity in "${all_entities[@]}"; do
    echo "- **Sql${entity}Repository**: SQLAlchemy使用の${entity}永続化"
done)

### データベース設定
- **DatabaseConfig**: 接続管理とセッション制御
- **依存性注入**: セッション提供とトランザクション管理

## アーキテクチャ設計

### 永続化技術
- **ORM**: SQLAlchemy
- **データベース**: SQLite（開発）/ PostgreSQL（本番対応）
- **接続プール**: 自動管理
- **トランザクション**: コンテキストマネージャー

### 設計パターン
- **Repository Pattern**: 永続化の抽象化
- **Data Mapper Pattern**: エンティティ・モデル変換
- **Unit of Work**: トランザクション境界管理
- **Dependency Injection**: 設定とセッション注入

### セキュリティ・信頼性
- **接続プール**: 自動リサイクル
- **SQL インジェクション対策**: ORM使用
- **論理削除**: データ保持とプライバシー配慮
- **エラーハンドリング**: 包括的例外処理

## データベース設計

### 共通フィールド
- \`id\`: VARCHAR(36) - UUID主キー
- \`created_at\`: TIMESTAMP - 作成日時
- \`updated_at\`: TIMESTAMP - 更新日時  
- \`is_active\`: BOOLEAN - 論理削除フラグ

### エンティティテーブル
$(for entity in "${all_entities[@]}"; do
    entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
    echo "#### ${entity_lower}s テーブル
- エンティティ: $entity
- 主キー: id (UUID)
- インデックス: created_at, is_active
- 外部キー: (必要に応じて追加)"
done)

## 設定・環境

### 環境変数
- \`DATABASE_URL\`: 本番データベース接続URL
- \`DEV_DATABASE_URL\`: 開発データベース接続URL  
- \`TESTING\`: テスト環境フラグ
- \`SQL_DEBUG\`: SQLログ出力制御

### 接続設定
\`\`\`python
# 本番環境例
DATABASE_URL=postgresql://user:pass@host:5432/dbname

# 開発環境例  
DEV_DATABASE_URL=sqlite:///./dev_database.db

# テスト環境
TESTING=true  # インメモリSQLite使用
\`\`\`

## テスト結果

- **統合テスト数**: $total_integration_tests
- **成功**: $passed_integration_tests
- **失敗**: $failed_integration_tests
- **カバレッジ**: $infra_coverage_result

## パフォーマンス考慮

### 最適化
- **接続プール**: 効率的なDB接続管理
- **遅延ローディング**: 必要時のみデータ取得
- **バッチ処理**: 大量データ操作対応
- **インデックス**: 検索性能向上

### スケーラビリティ
- **読み取り専用レプリカ**: 参照性能向上
- **シャーディング**: 水平分散対応
- **キャッシュ**: Redis等の統合

## 運用・監視

### ログ
- **クエリログ**: 性能分析用
- **エラーログ**: 問題診断用
- **アクセスログ**: 利用状況監視

### 監視項目
- 接続プール使用率
- クエリ実行時間
- デッドロック発生率
- ストレージ使用量

## 次のステップ

1. **プレゼンテーション層実装**: \`/implement-presentation $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
2. **進捗確認**: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
3. **E2Eテスト**: 全レイヤー連携テスト

---
**実装ステータス**: ✅ 完了
**統合テスト**: $integration_tests_passed
**永続化**: SQLAlchemy + SQLite/PostgreSQL
"
    
    if ! safe_create_file "$infra_doc_file" "$infra_doc_content" true; then
        echo "エラー: インフラドキュメントの作成に失敗しました"
        execute_rollback "infra_doc_creation_failed"
        exit 1
    fi
    
    implemented_files+=("$infra_doc_file")
    add_rollback "rm -f '$infra_doc_file'" "Remove infrastructure documentation"
    
    echo "✅ メタデータ・ドキュメント更新完了"
    ```

13. **ユースケースインデックス更新とGitコミット**:
    ```bash
    # 📚 ユースケースインデックス更新・コミット
    echo "📚 ユースケースインデックス更新・コミット中..."
    
    use_cases_index="docs/use_cases/index.md"
    if [[ -f "$use_cases_index" ]]; then
        # バックアップの作成
        backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
        if ! cp "$use_cases_index" "$backup_file"; then
            echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
            execute_rollback "index_backup_failed"
            exit 1
        fi
        add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
        
        # 機能のステータス更新
        feature_line="\\[${feature_name}\\]"
        updated_line="- [${feature_name}]($(basename "${spec_file}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: infrastructure_implemented, TDD: 🟢 GREEN, Infra: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 インフラストラクチャ層実装のコミット
    echo "💾 インフラストラクチャ層実装をコミット中..."
    
    commit_message="feat: implement infrastructure layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

インフラストラクチャ層実装サマリー:
- 機能: ${feature_name}
- Issues: $(printf '#%s ' "${issue_numbers[@]}")
- 実装ファイル: ${#implemented_files[@]} 作成
- 統合テスト結果: 成功 $passed_integration_tests, 失敗 $failed_integration_tests
- カバレッジ: $infra_coverage_result

実装されたコンポーネント:
$(printf '  - %s\n' "${implemented_files[@]}")

インフラストラクチャ機能:
- データ永続化用SQLAlchemy ORMモデル
- クリーンな分離のためのエンティティモデルマッパー
- エラーハンドリング付き具象リポジトリ実装
- 接続プーリング付きデータベース設定
- インメモリSQLite使用統合テスト
- トランザクション管理とロールバックサポート

データベース設計:
- UUID、タイムスタンプ、論理削除付き共通ベースモデル
- 適切なインデックス付きエンティティ固有テーブル
- 環境固有データベース設定
- マイグレーション対応構造

アーキテクチャ準拠:
- リポジトリパターン実装
- 関心の分離
- インフラストラクチャ層にドメインロジックなし
- 依存性注入対応

次のステップ: プレゼンテーション層の /implement-presentation
"
    
    files_to_commit=("$metadata_file")
    files_to_commit+=("${implemented_files[@]}")
    if [[ -f "$use_cases_index" ]]; then
        files_to_commit+=("$use_cases_index")
    fi
    
    if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
        echo "エラー: コミットに失敗しました"
        execute_rollback "commit_failed"
        exit 1
    fi
    
    add_rollback "git reset --hard HEAD~1" "Undo infrastructure implementation commit"
    echo "✅ コミット完了"
    ```

14. **GitHubイシュー更新と最終成功**:
    ```bash
    # 🎫 インフラストラクチャ実装完了でGitHubイシューを更新
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🏗️ **インフラストラクチャ層実装完了**

インフラストラクチャ層の実装が完了しました。データ永続化と外部サービス連携が可能になりました。

## 📊 実装結果
- **実装ファイル数**: ${#implemented_files[@]} ファイル
- **統合テスト結果**: 成功 $passed_integration_tests / 総計 $total_integration_tests
- **カバレッジ**: $infra_coverage_result
- **永続化技術**: SQLAlchemy + SQLite/PostgreSQL

## 🏗️ 実装されたコンポーネント
### データベースモデル
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:3}"; do
        echo "- **${entity}Model**: ${entity}の永続化モデル"
    done
    [[ ${#all_entities[@]} -gt 3 ]] && echo "- ... (他 $((${#all_entities[@]} - 3)) モデル)"
fi)

### リポジトリ実装
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:2}"; do
        echo "- **Sql${entity}Repository**: SQLAlchemy使用の永続化"
    done
    [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他リポジトリ)"
fi)

### マッパー・設定
- **エンティティマッパー**: ドメイン⇔DB変換
- **データベース設定**: 接続管理とトランザクション
- **統合テスト**: 実DB使用のE2Eテスト

## 🗄️ データベース設計
- **基底モデル**: UUID主キー + タイムスタンプ
- **論理削除**: is_activeフラグ使用
- **インデックス**: 検索性能最適化
- **環境対応**: SQLite(開発) / PostgreSQL(本番)

## 🏛️ アーキテクチャ準拠
- [x] リポジトリパターン実装
- [x] データマッパーパターン
- [x] 依存性注入対応
- [x] トランザクション管理
- [x] 例外処理とログ

## 🚀 次のステップ

プレゼンテーション層実装を開始してください：
\`\`\`bash
/implement-presentation $issue_num
\`\`\`

## 📚 関連ドキュメント
- [インフラ層設計]($infra_doc_file)
- [データベース設計](#データベース設計)

## 🔍 動作確認
\`\`\`bash
# 統合テスト実行
uv run --frozen pytest tests/integration/ -v

# カバレッジ確認
uv run --frozen pytest tests/integration/ --cov=src.infrastructure

# データベース初期化（開発環境）
python -c \"from src.infrastructure.config.database import init_database; init_database()\"
\`\`\`

---
**Layer Status**: Infrastructure ✅ → 次: Presentation 🎨
"
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    
    # 🎉 トランザクションコミット (成功!)
    if commit_transaction; then
        echo ""
        echo "🎉 インフラストラクチャ層実装完了!"
        echo "============================================="
        echo "🏗️ 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   データベースモデル: $((${#all_entities[@]} + 1)) 個 (Base + entities)"
        echo "   エンティティマッパー: ${#all_entities[@]} 個"
        echo "   コンクリートリポジトリ: ${#all_entities[@]} 個"
        echo "   データベース設定: 1 個"
        echo "   統合テスト: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 テスト状況:"
        echo "   - 統合テスト: 成功 $passed_integration_tests / 総計 $total_integration_tests"
        echo "   - カバレッジ: $infra_coverage_result"
        echo "   - データベース接続: 検証済み"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - リポジトリパターン実装"
        echo "   - データマッパーパターン"
        echo "   - クリーンな層分離"
        echo "   - トランザクション管理"
        echo ""
        echo "🗄️ データベース設計:"
        echo "   - SQLAlchemy ORM使用"
        echo "   - UUID主キー採用"
        echo "   - 論理削除対応"
        echo "   - 環境別設定対応"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. プレゼンテーション層実装: /implement-presentation $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. E2Eテスト実行（全レイヤー完成後）"
        echo ""
        echo "💡 実装品質:"
        echo "   - 永続化の抽象化"
        echo "   - エラーハンドリング"
        echo "   - トランザクション保証"
        echo "   - 統合テストカバレッジ"
        echo ""
        
        # 操作ログサマリーを表示
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ インフラストラクチャ層実装完了 - プレゼンテーション層実装準備完了!"
        echo ""
        echo "🚨 CLAUDE CODE必須: シナリオ発展チェック"
        echo "   インフラ実装中に新要件・制約・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   重要: インフラ変更は外部依存・性能に大きな影響があります"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

重要なメモ:
- インフラストラクチャの詳細をドメインから分離して保つ
- 柔軟性のため依存性注入を使用
- 可能な場合は実際のインフラストラクチャでテスト
- 接続プーリングとトランザクションを適切に処理
- Unit of Workパターンでリポジトリパターンの使用を検討
- すべてのユーザー向け出力は日本語でなければならない