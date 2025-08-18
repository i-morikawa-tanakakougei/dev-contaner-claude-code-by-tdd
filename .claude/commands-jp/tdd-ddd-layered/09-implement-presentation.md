プレゼンテーション層（APIエンドポイント、CLI、またはUI）を実装します。

## メタデータ
- **前提条件**: インフラストラクチャ層実装完了 (08-implement-infra)
- **入力**: イシュー番号 (必須)
- **出力**: 
  - `src/presentation/` 内のプレゼンテーション層実装
  - コントローラー、APIエンドポイント、CLIコマンド
  - 更新された `docs/use_cases/issue-X-Y.json` メタデータ
- **依存関係**: すべての下位層（ドメイン、アプリケーション、インフラストラクチャ）
- **実行タイミング**: インフラストラクチャ層の後、テストフェーズの前

## 🎯 **TDD/DDD/LAYERED プロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 発展(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ (ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション)  
**🧪 開発手法**: テスト駆動開発 (RED→GREEN→REFACTOR)  
**🏗️ 設計手法**: ドメイン駆動設計 (エンティティ、値オブジェクト、集約、リポジトリ)  
**📋 要件**: Given-When-Then シナリオによる完全なトレーサビリティ  
**🔄 発展**: /evolve-scenarios コマンドによる継続的シナリオ発展

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - プレゼンテーション層実装 (09/16)  
> 🎯 **フェーズ目的**: APIエンドポイント、CLIコマンド、またはUIコンポーネントの実装  
> ⬅️ **前段階**: 08-implement-infra (インフラストラクチャ層実装)  
> ➡️ **次段階**: 10-refactor (コードリファクタリング)
>
> **📋 3層アーキテクチャ運用**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (ユーザーインタラクションの参照)  
> - 📊 **戦術**: `docs/use_cases/index.md` (プレゼンテーション層ステータス更新)  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (プレゼンテーション実装追跡)

## 🖼️ **プレゼンテーション層実装のみ**

**⚠️ 重要な注意:**
- **このステップはプレゼンテーション層のみ** - APIエンドポイント、CLI、またはUIコンポーネントを実装
- **他の層は禁止** - プレゼンテーション層コンポーネントのみにフォーカス  
- **ユーザーインターフェース** - APIエンドポイント、CLIコマンド、またはWebインターフェースを処理
- **入力検証** - ユーザー入力検証とレスポンス形式を処理

**層実装順序:**
1. `06-implement-domain` ← ドメイン層 (完了)
2. `07-implement-usecase` ← アプリケーション層 (完了)
3. `08-implement-infra` ← インフラストラクチャ層 (完了)  
4. `09-implement-presentation` ← **【現在地】プレゼンテーション層**

## 🚨 **重要: プレゼンテーション層のみ - 他の層は禁止**

**❌ このステップで絶対に禁止:**
- **ドメイン層修正**: ドメイン層は完了済み - 修正しないこと
- **アプリケーション層修正**: アプリケーション層は完了済み - 修正しないこと  
- **インフラストラクチャ層修正**: インフラストラクチャ層は完了済み - 修正しないこと
- **ビジネスロジック**: プレゼンテーションコードにビジネスルールやドメインロジック禁止

**✅ このステップでのみ許可:**
- **APIコントローラー**: REST/GraphQLエンドポイントとHTTPリクエスト処理
- **CLIコマンド**: コマンドラインインターフェース実装
- **Web UIコンポーネント**: フロントエンドインターフェースとユーザーインタラクション
- **入力検証**: リクエスト検証、シリアライゼーション、レスポンス形式

## 📋 **プレゼンテーション層タスクチェックリスト**

**適切な統合を持つプレゼンテーション層実装にこのチェックリストを使用:**

### 🔴 必須タスク

#### **🎯 ユースケースからエンドポイントへのマッピング**
- [ ] **Given-When-Thenをエンドポイントにマップ**: シナリオをAPIエンドポイントまたはCLIコマンドに変換
- [ ] **🚨 重要: プレースホルダーアサーションの置換**: プレゼンテーションテストで `assert False, "RED: ... not implemented yet"` 文をチェックして修正
- [ ] **テストの真正性検証**: 実装を実際にテストしていることを確認、プレースホルダー失敗ではなく
- [ ] **リクエスト/レスポンスモデルの定義**: 各エンドポイントの入力/出力モデルを作成
- [ ] **認証要件の計画**: どのエンドポイントが認証を必要とするか特定
- [ ] **エラーレスポンス形式の設計**: 一貫性のあるエラーレスポンス構造を定義

#### **🌐 APIコントローラー実装**
- [ ] **APIコントローラーの作成**: 各ユースケース用のRESTコントローラーを実装
- [ ] **エンドポイントルーティングの追加**: URLルーティングとHTTPメソッドを設定
- [ ] **リクエスト処理の実装**: 受信リクエストの解析と検証
- [ ] **アプリケーションサービスの呼び出し**: アプリケーション層のユースケースと統合
- [ ] **レスポンスの形式**: アプリケーションDTOをAPIレスポンス形式に変換

#### **🧪 エンドツーエンドテスト**
- [ ] **e2eテストの実行**: プレゼンテーション層を通した完全なエンドツーエンドテストを実行
- [ ] **すべてのエンドポイントのテスト**: 各APIエンドポイントが正しく動作することを検証
- [ ] **メタデータの更新**: issue-X-Y.json でプレゼンテーション層実装完了をマーク
- [ ] **プレゼンテーション層のコミット**: プレゼンテーション層コードをバージョン管理

### 🟡 推奨タスク

#### **✅ 入力検証・シリアライゼーション**
- [ ] **リクエスト検証の追加**: すべての受信リクエストを検証
- [ ] **フィールド検証の実装**: 必須フィールド、形式、制約をチェック
- [ ] **サニタイゼーションの追加**: インジェクション攻撃を防ぐためユーザー入力をサニタイズ
- [ ] **検証エラーの処理**: 明確な検証エラーメッセージを返す
- [ ] **リクエストシリアライゼーションの実装**: リクエストをアプリケーションDTOに変換
- [ ] **レスポンスシリアライゼーションの追加**: アプリケーションDTOをレスポンス形式に変換

#### **🔒 認証・認可**
- [ ] **認証の実装**: ログイン/ログアウト機能を追加
- [ ] **認可チェックの追加**: ロールベースアクセス制御を実装
- [ ] **認証エラーの処理**: 明確な認証失敗メッセージを提供
- [ ] **セッション管理の追加**: 必要に応じてセッション処理を実装
- [ ] **機密エンドポイントの保護**: 重要な操作への適切な保護を確保

#### **🚫 アーキテクチャ準拠チェック**
- [ ] **ビジネスロジックなし**: プレゼンテーションコードにビジネスルールが含まれていないことを検証
- [ ] **ドメイン層未変更**: ドメイン層ファイルが修正されていないことを検証
- [ ] **アプリケーション層未変更**: アプリケーション層ファイルが修正されていないことを検証
- [ ] **インフラストラクチャ層未変更**: インフラストラクチャ層ファイルが修正されていないことを検証
- [ ] **プレゼンテーションディレクトリのみ**: src/presentation/ ディレクトリのみに新しいファイルがあることを確認
- [ ] **適切な依存関係使用**: アプリケーションサービスのみが呼び出され、ドメインに直接アクセスしていないことを検証

### 🟢 オプションタスク

#### **⚡ CLIコマンド実装**
- [ ] **CLIコマンドの作成**: 各ユースケース用のコマンドラインインターフェースを実装
- [ ] **引数解析の追加**: コマンドライン引数とオプションを解析
- [ ] **コマンドロジックの実装**: CLIコマンドをアプリケーションサービスに接続
- [ ] **ヘルプドキュメントの追加**: 使用方法のヘルプと例を提供
- [ ] **CLIエラーの処理**: ユーザーフレンドリーなエラーメッセージを実装
- [ ] **進捗インジケーターの追加**: 長時間実行される操作の進捗を表示

#### **📱 ユーザーエクスペリエンス・ドキュメント**
- [ ] **APIドキュメントの追加**: OpenAPI/Swaggerドキュメントを作成
- [ ] **使用例の作成**: 各エンドポイントの明確な使用例を提供
- [ ] **CLIヘルプの追加**: 包括的なヘルプシステムを実装
- [ ] **ユーザーガイドの作成**: ユーザー向けドキュメントを作成
- [ ] **ログの追加**: デバッグ用のリクエスト/レスポンスログを実装
- [ ] **パフォーマンス最適化**: レスポンシブなユーザーエクスペリエンスを確保

#### **🔧 本番環境対応**
- [ ] **ヘルスチェックの追加**: ヘルスチェックエンドポイントを実装
- [ ] **メトリクスの追加**: 監視とメトリクス収集を実装
- [ ] **CORSの設定**: 適切なクロスオリジンリソース共有を設定
- [ ] **レート制限の追加**: 必要に応じてAPIレート制限を実装
- [ ] **セキュリティヘッダー**: 適切なセキュリティヘッダーを追加
- [ ] **環境設定**: 異なる環境（dev/staging/prod）をサポート

#### **🔧 コード品質検証**
- [ ] **ruff リンティングの実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **ruff フォーマットの実行**: `uv run --frozen ruff format src/` を実行
- [ ] **型チェックの実行**: `uv run --frozen pyright src/` を実行
- [ ] **品質問題の修正**: リンティング、フォーマット、型エラーに対処
- [ ] **クリーン結果の検証**: すべての品質ツールがエラーなしで通ることを確保

#### **📊 高度なフェーズ完了**
- [ ] **エンドポイント整理の計画**: 関連エンドポイントを論理的にグループ化
- [ ] **エラーハンドリングの追加**: 適切なHTTPエラーレスポンスを実装
- [ ] **エラーシナリオのテスト**: 適切なエラーハンドリングとレスポンスを検証
- [ ] **認証フローのテスト**: 認証/認可が正しく動作することを確保
- [ ] **入力検証のテスト**: 検証が無効な入力をキャッチすることを検証
- [ ] **統合のテスト**: すべての層が適切に連携することを確認
- [ ] **認証ミドルウェアの追加**: 再利用可能な認証コンポーネントを実装
- [ ] **APIの文書化**: すべてのエンドポイント、コマンド、使用パターンを記録
- [ ] **完全システムのテスト**: 完全なエンドツーエンド機能を検証
- [ ] **テスト用の準備**: システムが包括的なテストフェーズの準備ができていることを確保

**💡 プロ tip**: プレゼンテーション層は薄くあるべき - すべてのビジネスロジックをアプリケーションサービスに委譲せよ！

### ✅ 許可されるファイル (実装対象):
- `src/presentation/api/` - REST APIエンドポイント、コントローラー
- `src/presentation/cli/` - コマンドラインインターフェースコマンド
- `src/presentation/web/` - Web UIコンポーネント、ビュー、テンプレート
- `src/presentation/serializers/` - 入力/出力シリアライゼーション
- `src/presentation/validators/` - リクエスト検証
- `src/presentation/middleware/` - HTTPミドルウェア、リクエスト処理

### ❌ 禁止ファイル (このステップでは作成/修正しない):
- `src/domain/` - **ドメイン層 (既に実装済み、修正禁止)**
- `src/application/` - **アプリケーション層 (既に実装済み、修正禁止)**
- `src/infrastructure/` - **インフラストラクチャ層 (既に実装済み、修正禁止)**

### 🎯 実装ルール:
1. **ユーザーインターフェースのみ処理** - APIエンドポイント、CLIコマンド、Webページ
2. **ビジネスロジックなし** - すべてのビジネス操作をアプリケーション層に委譲
3. **入力検証とシリアライゼーション** - 入力を検証し、出力をシリアライズ
4. **依存性注入** - アプリケーションユースケースを注入、作成しない
5. **HTTP/CLI関心事のみ** - リクエスト処理、レスポンス形式、エラーハンドリング
6. **薄いコントローラー** - プレゼンテーションロジックを最小限に

### 💡 他の層を誤って実装した場合:
```bash
# 他の層は修正しない
# すべての他の層は前のステップで既に完了済みのはず

# 間違った場所にファイルを作成した場合:
# ファイルパスを注意深く確認し、src/presentation/ に移動する
```

**これらのルールに違反するとクリーンアーキテクチャが破れ、密結合が発生します。**

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
git restore tests/e2e/api/
git restore tests/unit/presentation/

# 適切なTDDフローに戻る
# 1. 失敗テストを読む (これらは仕様)
# 2. テストを通すためのプレゼンテーションコードを実装
# 3. テストロジックをコードに合わせて変更しない
```

**⚠️ 重要: テスト修正はTDDサイクルを破り、シナリオ駆動開発を無効化します！**

---

## よくあるエラーと解決策

### ❌ エラーケース1: インフラストラクチャ層未実装
**原因**: インフラストラクチャ完了前にプレゼンテーション層が開始された  
**解決策**: まず `/implement-infra <issue-number>` でインフラストラクチャ層を完了する

### ❌ エラーケース2: コントローラーのビジネスロジック
**原因**: APIコントローラーやUIハンドラーにビジネスロジックが実装された  
**解決策**: コントローラーはHTTP/UI関心事のみを処理 - アプリケーション層に委譲

### ❌ エラーケース3: プレースホルダーアサーションが偽RED状態を引き起こす
**原因**: プレゼンテーションテストに `assert False, "RED: ... not implemented yet"` があるが実装は存在する  
**解決策**: 
```python
# 悪い例: プレースホルダーアサーション (偽REDを引き起こす)
def test_api_endpoint(self):
    assert False, "RED: API endpoint not implemented yet"

# 良い例: 実際のテスト実装
def test_api_endpoint(self):
    response = client.post("/api/entities", json={"name": "test"})
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.json()["name"] == "test"
```
**復旧**: すべてのプレースホルダーアサーションを実際の実装を検証する適切なテストに置換

### ❌ エラーケース4: プレゼンテーションからドメインへの直接アクセス
**原因**: プレゼンテーション層がアプリケーション層をバイパス  
**解決策**: プレゼンテーション層からは常にアプリケーション層のユースケースを使用

## 実行例

### ✅ 成功例
```bash
$ /implement-presentation 15
🖥️ Issues: #15 のプレゼンテーション層実装を開始します
✅ インフラ層が正常に実装されています
🌐 APIエンドポイント実装中...
  ✅ ファイル作成: src/presentation/api/user_controller.py
🎉 プレゼンテーション層実装完了!
```

### ❌ 失敗例と修正
```bash
$ /implement-presentation 15
❌ インフラ層の実装が完了していません
# 修正: 最初にインフラストラクチャ層を完了
$ /implement-infra 15
$ /implement-presentation 15
```

### ❌ プレースホルダーアサーション例と修正
```bash
$ /implement-presentation 3
🚨 プレースホルダーアサーション発見:
  - tests/e2e/api/test_data_persistence_api.py: 8 個
  - tests/e2e/api/test_connections_api.py: 6 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# 修正: プレースホルダーアサーションを実際のテストに置換
# テストファイルを編集して置換:
#   assert False, "RED: API endpoint not implemented yet"
# を以下に変更:
#   response = client.post("/api/trades", json={"symbol": "EURUSD", "quantity": "1.0"})
#   assert response.status_code == 201
#   assert response.json()["trade_id"] is not None
```

## タスク詳細

1. **安全環境セットアップと引数解析**:
   ```bash
   # 🔧 すべての安全操作関数とテンプレートユーティリティを読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "09-implement-presentation" "$ARGUMENTS"
   source "$(dirname "${BASH_SOURCE[0]}")/templates/_template_utils.sh"
   
   # プレゼンテーション実装は少なくとも1つのイシュー番号が必要
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-presentation" "1" "単一イシューのプレゼンテーション実装"
       show_usage_example "implement-presentation" "1,7" "複数イシューのプレゼンテーション実装"
       show_usage_example "implement-presentation" "1 api" "イシュー + API指定"
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
   
   echo "🎨 Issues: $(printf '#%s ' "${issue_numbers[@]}")のプレゼンテーション層実装を開始します"
   echo ""
   echo "🚨 重要な注意: このステップではプレゼンテーション層のみを実装します"
   echo "   ✅ 許可: src/presentation/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/domain/, src/application/, src/infrastructure/"
   echo "   💡 他の層を間違って実装した場合は即座に削除してください"
   echo ""
   echo "🔴→🟢 TDD原則: テストを実装に合わせて変更してはいけません!"
   echo "   📖 シナリオ → 🔴 テスト → 🟢 実装 の順序を厳守"
   echo "   ✅ 実装をテストに合わせる（正しい）"
   echo "   ❌ テストを実装に合わせる（禁止）"
   echo ""
   ```

2. **トランザクション開始と前提条件検証**:
   ```bash
   # 🔄 包括的トランザクション開始
   if ! begin_transaction "implement_presentation_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 前提条件検証 - 他のすべての層が完了している必要がある
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
   
   # 必要なすべての層が実装されているか検証
   validate_layer_implementations() {
       local domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       local app_use_cases=$(find src/application/use_cases/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       local infra_repos=$(find src/infrastructure/repositories/ -name "sql_*.py" -type f 2>/dev/null | grep -v __pycache__ | wc -l)
       
       if [[ $domain_entities -eq 0 ]]; then
           echo "❌ ドメイン層の実装が見つかりません"
           echo "💡 先に /implement-domain を実行してください"
           return 1
       fi
       
       if [[ $app_use_cases -eq 0 ]]; then
           echo "❌ アプリケーション層の実装が見つかりません"
           echo "💡 先に /implement-usecase を実行してください"
           return 1
       fi
       
       if [[ $infra_repos -eq 0 ]]; then
           echo "❌ インフラストラクチャ層の実装が見つかりません"
           echo "💡 先に /implement-infra を実行してください"
           return 1
       fi
       
       echo "  ✅ すべてのレイヤー実装確認完了"
       return 0
   }
   
   if ! validate_layer_implementations; then
       execute_rollback "missing_layer_implementations"
       exit 1
   fi
   
   # 🚨 重要: プレゼンテーション層テストのプレースホルダーアサーションをチェック
   echo "  🚨 プレゼンテーション層プレースホルダーアサーション検証中..."
   
   presentation_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           presentation_placeholder_files+=("$file")
       fi
   done < <(find tests/e2e/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#presentation_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ プレゼンテーション層プレースホルダーアサーション発見:"
       for file in "${presentation_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#presentation_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#presentation_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - プレゼンテーション実装は完了済みだが、テストがプレースホルダーのまま"
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
           echo "プレゼンテーション層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "presentation_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ プレゼンテーション層プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   echo "✅ 前提条件検証完了"
   ```

3. **テンプレート変数のセットアップ**:
   ```bash
   # 📝 コード生成用のテンプレート変数をセットアップ
   echo "📝 テンプレート変数設定中..."
   
   # 機能ベースの変数をセットアップ
   setup_feature_vars "$feature_name"
   
   # ドメイン層からエンティティを抽出
   all_entities=()
   for entity_file in $(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__); do
       entity_name=$(basename "$entity_file" .py)
       entity_class=$(to_title_case "$entity_name")
       all_entities+=("$entity_class")
   done
   
   echo "  🎯 テンプレート変数設定:"
   echo "    - 機能名: $feature_name"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   
   echo "✅ テンプレート変数設定完了"
   ```

4. **プレゼンテーション層構造の作成**:
   ```bash
   # 🎨 プレゼンテーション層構造を作成
   echo "🎨 プレゼンテーション層構造作成中..."
   
   # プレゼンテーション構造ディレクトリを定義
   presentation_directories=(
       "src/presentation/api/controllers"
       "src/presentation/api/validators"
       "src/presentation/api/serializers"
       "src/presentation/api/middleware"
       "src/presentation/cli"
       "src/presentation/web"
   )
   
   # すべてのプレゼンテーションディレクトリを安全に作成
   for dir in "${presentation_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: プレゼンテーションディレクトリ作成に失敗しました: $dir"
           execute_rollback "presentation_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove presentation directory: $dir"
   done
   
   echo "✅ プレゼンテーション構造作成完了"
   ```

5. **テンプレートを使用したAPIコンポーネント生成**:
   ```bash
   # ✅ テンプレートを使用したAPIコンポーネント生成
   echo "✅ APIコンポーネント生成中..."
   
   implemented_files=()
   
   # APIバリデーター生成
   validator_file="src/presentation/api/validators/${feature_name_snake}_validator.py"
   echo "  ✅ 生成中: API Validator ($validator_file)"
   
   if ! process_template "presentation/validator_template.py" "$validator_file"; then
       echo "エラー: バリデーターテンプレート処理に失敗しました"
       execute_rollback "validator_template_failed"
       exit 1
   fi
   
   implemented_files+=("$validator_file")
   add_rollback "rm -f '$validator_file'" "Remove generated validator"
   
   # APIシリアライザー生成
   serializer_file="src/presentation/api/serializers/${feature_name_snake}_serializer.py"
   echo "  📄 生成中: API Serializer ($serializer_file)"
   
   if ! process_template "presentation/serializer_template.py" "$serializer_file"; then
       echo "エラー: シリアライザーテンプレート処理に失敗しました"
       execute_rollback "serializer_template_failed"
       exit 1
   fi
   
   implemented_files+=("$serializer_file")
   add_rollback "rm -f '$serializer_file'" "Remove generated serializer"
   
   # APIコントローラー生成
   controller_file="src/presentation/api/controllers/${feature_name_snake}_controller.py"
   echo "  🎮 生成中: API Controller ($controller_file)"
   
   if ! process_template "presentation/controller_template.py" "$controller_file"; then
       echo "エラー: コントローラーテンプレート処理に失敗しました"
       execute_rollback "controller_template_failed"
       exit 1
   fi
   
   implemented_files+=("$controller_file")
   add_rollback "rm -f '$controller_file'" "Remove generated controller"
   
   echo "✅ APIコンポーネント生成完了"
   ```

6. **FastAPIアプリケーション生成**:
   ```bash
   # 🚀 FastAPIアプリケーション生成
   echo "🚀 FastAPI アプリケーション生成中..."
   
   app_file="src/presentation/api/app.py"
   echo "  🚀 生成中: FastAPI Application ($app_file)"
   
   # カスタムFastAPIアプリテンプレート内容を作成（今は直接定義）
   app_template_content='"""
   '"$feature_name"' FastAPI Application

   '"$feature_name"' 機能のREST API サーバー。
   実装日時: '"$(date)"'
   """

   from fastapi import FastAPI, HTTPException, Depends, Query, Path
   from fastapi.middleware.cors import CORSMiddleware
   from fastapi.responses import JSONResponse
   from pydantic import BaseModel, Field
   from typing import Dict, Any, Optional
   import logging
   import os

   from src.application.use_cases.'"${feature_name_snake}"'_use_case import '"${feature_name_title}"'UseCase
   from src.infrastructure.config.database import get_database_session
   from .controllers.'"${feature_name_snake}"'_controller import '"${feature_name_title}"'Controller

   # FastAPI アプリケーション初期化
   app = FastAPI(
       title="'"$feature_name"' API",
       description="'"$feature_name"' 機能のREST API",
       version="1.0.0"
   )

   # CORS設定
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )

   # ヘルスチェックエンドポイント
   @app.get("/health")
   async def health_check():
       return {"status": "healthy", "service": "'"$feature_name"'"}

   # TODO: コントローラーを使った実際のAPIエンドポイントを追加
   '
   
   if ! safe_create_file "$app_file" "$app_template_content" true; then
       echo "エラー: FastAPIアプリケーションファイルの作成に失敗しました"
       execute_rollback "app_creation_failed"
       exit 1
   fi
   
   implemented_files+=("$app_file")
   add_rollback "rm -f '$app_file'" "Remove FastAPI app"
   
   echo "✅ FastAPI アプリケーション生成完了"
   ```

7. **E2Eテストの生成**:
   ```bash
   # 🧪 プレゼンテーション層用E2Eテスト生成
   echo "🧪 E2Eテスト生成中..."
   
   # 必要に応じてE2Eテストディレクトリを作成
   if ! safe_mkdir "tests/e2e/api"; then
       echo "エラー: E2Eテストディレクトリの作成に失敗しました"
       execute_rollback "e2e_test_dir_creation_failed"
       exit 1
   fi
   
   e2e_test_file="tests/e2e/api/test_${feature_name_snake}_api.py"
   echo "  🧪 生成中: E2E API Test ($e2e_test_file)"
   
   if ! process_template "tests/e2e_test_template.py" "$e2e_test_file"; then
       echo "エラー: E2Eテストテンプレート処理に失敗しました"
       execute_rollback "e2e_test_template_failed"
       exit 1
   fi
   
   implemented_files+=("$e2e_test_file")
   add_rollback "rm -f '$e2e_test_file'" "Remove generated E2E test"
   
   echo "✅ E2Eテスト生成完了"
   ```

8. **E2Eテスト実行とメタデータ更新**:
   ```bash
   # 🟢 プレゼンテーション層検証のためのE2Eテスト実行
   echo "🟢 E2Eテスト実行中..."
   
   # テスト用Python環境の検証
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # E2Eテストの実行
   e2e_test_output_file="/tmp/e2e_test_output_$$"
   e2e_test_result=0
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/e2e/ -v --tb=short > "$e2e_test_output_file" 2>&1; then
       e2e_test_result=0
   else
       e2e_test_result=1
   fi
   
   # テスト結果の分析
   total_e2e_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   passed_e2e_tests=$(grep -c "PASSED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   failed_e2e_tests=$(grep -c "FAILED" "$e2e_test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 E2Eテスト結果:"
   echo "    - 総テスト数: $total_e2e_tests"
   echo "    - 成功: $passed_e2e_tests"
   echo "    - 失敗: $failed_e2e_tests"
   
   rm -f "$e2e_test_output_file"
   e2e_tests_passed=$([ $failed_e2e_tests -eq 0 ] && echo "true" || echo "false")
   
   # 📊 プレゼンテーション実装完了でメタデータを更新
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if ! update_metadata_atomic "$metadata_file" \
       '.phases.presentation_implementation.completed = true |
        .phases.presentation_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .phases.presentation_implementation.e2e_tests_passed = '"$e2e_tests_passed"' |
        .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
        .spec_files.presentation_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
        .phase = "presentation_implemented" |
        .next_commands = ["refactor", "run-all-tests", "use-case-status"]'; then
       echo "エラー: メタデータの更新に失敗しました"
       execute_rollback "metadata_update_failed"
       exit 1
   fi
   
   echo "✅ E2Eテスト実行・メタデータ更新完了"
   ```

9. **変更のコミットとGitHubイシュー更新**:
   ```bash
   # 📚 変更のコミットとGitHubイシュー更新
   echo "📚 変更のコミットとGitHubイシュー更新中..."
   
   # コミットメッセージの作成
   commit_message="feat: implement presentation layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

   プレゼンテーション層実装サマリー:
   - 機能: ${feature_name}
   - Issues: $(printf '#%s ' "${issue_numbers[@]}")
   - 生成ファイル: ${#implemented_files[@]} テンプレート使用ファイル
   - E2Eテスト結果: 成功 $passed_e2e_tests, 失敗 $failed_e2e_tests
   
   生成されたコンポーネント:
   $(printf '  - %s\n' "${implemented_files[@]}")
   
   テンプレートベース実装:
   - 包括的入力検証付きAPIバリデーター
   - 一貫した出力形式のレスポンスシリアライザー
   - 適切なエラーハンドリング付きコントローラー
   - OpenAPIドキュメント付きFastAPIアプリケーション
   - 完全なAPIカバレッジ用E2Eテスト
   
   次のステップ: /refactor または /run-all-tests
   "
   
   files_to_commit=("$metadata_file")
   files_to_commit+=("${implemented_files[@]}")
   
   if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
       echo "エラー: コミットに失敗しました"
       execute_rollback "commit_failed"
       exit 1
   fi
   
   # GitHubイシューの更新
   for issue_num in "${issue_numbers[@]}"; do
       issue_comment="🎨 **プレゼンテーション層実装完了**

   プレゼンテーション層の実装が完了しました。テンプレートベースの自動生成により、一貫性のあるREST APIが構築されました。

   ## 📊 実装結果
   - **生成ファイル数**: ${#implemented_files[@]} ファイル
   - **E2Eテスト結果**: 成功 $passed_e2e_tests / 総計 $total_e2e_tests
   - **実装方式**: テンプレートベース自動生成

   ## 🎨 生成されたコンポーネント
   - **APIバリデーター**: 入力データの検証とサニタイゼーション
   - **APIシリアライザー**: レスポンス形式の統一化
   - **APIコントローラー**: HTTP リクエスト処理
   - **FastAPIアプリ**: REST APIサーバー
   - **E2Eテスト**: API動作検証

   ## 🚀 次のステップ
   \`\`\`bash
   /refactor $issue_num      # コード品質向上
   /run-all-tests $issue_num # 全テスト実行
   \`\`\`

   ---
   **Phase**: presentation_implemented ✅ → 次: refactor 🔧"
       
       safe_add_issue_comment "$issue_num" "$issue_comment" || true
   done
   
   echo "✅ コミット・GitHub更新完了"
   ```

10. **最終成功**:
    ```bash
    # 🎉 トランザクションコミットと最終成功メッセージ
    if commit_transaction; then
        echo ""
        echo "🎉 プレゼンテーション層実装完了!"
        echo "============================================="
        echo "🎨 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 生成ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 生成されたコンポーネント:"
        echo "   - APIバリデーター: 入力検証"
        echo "   - APIシリアライザー: レスポンス変換"
        echo "   - APIコントローラー: HTTP処理"
        echo "   - FastAPIアプリ: REST APIサーバー"
        echo "   - E2Eテスト: API検証"
        echo ""
        echo "🟢 テンプレートベース実装の利点:"
        echo "   - 一貫性のあるコード構造"
        echo "   - 保守性の向上"
        echo "   - 開発速度の向上"
        echo "   - エラーの削減"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. リファクタリング: /refactor $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 全テスト実行: /run-all-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo ""
        echo "✅ テンプレートベース・プレゼンテーション層実装完了!"
        echo ""
        echo "🚨 CLAUDE CODE必須: シナリオ発展チェック"
        echo "   プレゼンテーション実装中に新要件・UI変更・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   重要: UI変更はユーザー体験に直接影響します"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

重要なメモ:
- テンプレートベース実装により一貫性と保守性を確保
- すべてのコードテンプレートは別途保存され再利用可能
- 変数置換により異なる機能に対応したカスタマイゼーションが可能
- コード重複の削減と開発速度の向上
- すべてのユーザー向け出力は日本語でなければならない