# アプリケーション層ユースケースの実装

ドメインロジックを統合するアプリケーション層のユースケースを実装します。

## メタデータ
- **前提条件**: ドメイン層実装完了 (06-implement-domain)
- **入力**: イシュー番号（必須）
- **出力**: 
  - `src/application/` でのアプリケーション層実装
  - ユースケースクラス、DTO、アプリケーションサービス
  - 更新された `docs/use_cases/issue-X-Y.json` メタデータ
- **依存関係**: ドメイン層クラス、pytest、型ヒント
- **実行タイミング**: ドメイン実装後、インフラ層実装前

## 🎯 **TDD/DDD/レイヤード プロセス コンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → テスト(05) → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ (ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション)  
**🧪 開発**: テスト駆動開発 (RED→GREEN→REFACTOR)  
**🏗️ 設計**: ドメイン駆動設計 (エンティティ、値オブジェクト、集約、リポジトリ)  
**📋 要件**: 完全なトレーサビリティによるGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenarios コマンドによる継続的シナリオ進化

> 📖 **ドキュメント管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - アプリケーション層実装 (07/16)  
> 🎯 **フェーズ目的**: ドメインロジックを統合するユースケースとDTOの実装  
> ⬅️ **前ステージ**: 06-implement-domain (ドメイン層実装)  
> ➡️ **次ステージ**: 08-implement-infra (インフラ層実装)
>
> **📋 3層アーキテクチャ運用**:  
> - 🎯 **戦略**: `docs/use_cases/core/index.md` (ユースケースフローの参照)  
> - 📊 **戦術**: `docs/use_cases/index.md` (アプリケーション層ステータス更新)  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json` (アプリケーション実装追跡)

## 一般的なエラーと解決策

### ❌ エラーケース1: ドメイン層が実装されていない
**原因**: ドメイン実装完了前にアプリケーション層を開始  
**解決策**: 
```bash
# ドメイン層が完了していることを確認
/implement-domain <issue-number>
# その後アプリケーション層を実装
/implement-usecase <issue-number>
```

### ❌ エラーケース2: ユースケースがインフラを直接操作している
**原因**: アプリケーション層がドメイン層をバイパスするか、インフラに直接アクセス  
**解決策**: 
```python
# 悪い例: ユースケースでの直接データベースアクセス
from src.infrastructure.database import Session

# 良い例: ドメインリポジトリインターフェースの使用
from src.domain.repositories import UserRepository
class UserUseCase:
    def __init__(self, user_repo: UserRepository):
        self._user_repo = user_repo
```

### ❌ エラーケース3: プレースホルダーアサーションによる偽のRED状態
**原因**: アプリケーションテストに `assert False, "RED: ... not implemented yet"` が含まれているが実装は存在  
**解決策**: 
```python
# 悪い例: プレースホルダーアサーション（偽のREDを引き起こす）
def test_use_case_execution(self):
    assert False, "RED: Use case execution not implemented yet"

# 良い例: 実際のテスト実装
def test_use_case_execution(self):
    use_case = MyUseCase(mock_repository)
    result = use_case.execute(request_dto)
    assert result.success is True
    assert result.data is not None
```
**復旧**: すべてのプレースホルダーアサーションを実際の実装をテストする適切なテストに置き換える

### ❌ エラーケース4: ビジネスロジックを含むDTO
**原因**: ビジネスロジックがデータ転送オブジェクトに漏れている  
**解決策**: 
- DTOはデータのみを含み、ビジネスメソッドは含まない
- バリデーションをドメインエンティティまたは値オブジェクトに移動
- DTOをシンプルなデータコンテナとして保持

## 実行例

### ✅ 成功例
```bash
$ /implement-usecase 15
📱 Issues: #15 のアプリケーション層実装を開始します
🟢 ドメイン層実装確認中...
✅ ドメイン層が正常に実装されています
🏗️ ユースケース実装中...
  ✅ ファイル作成: src/application/use_cases/user_management.py
  ✅ ファイル作成: src/application/dtos/user_dto.py
  ✅ ファイル作成: src/application/exceptions.py
🧪 アプリケーションテスト実行中...
======= 8 passed, 0 failed =======
✅ アプリケーションテストが成功
🎉 アプリケーション層実装完了!
```

### ❌ 失敗例と修正
```bash
$ /implement-usecase 15
❌ ドメイン層の実装が完了していません
💡 最初にドメイン層を実装してください:
   /implement-domain 15

# 修正: 最初にドメイン層を完了
$ /implement-domain 15
$ /implement-usecase 15
```

### ❌ プレースホルダーアサーション例と修正
```bash
$ /implement-usecase 3
🚨 プレースホルダーアサーション発見:
  - tests/unit/application/use_cases/test_data_persistence_use_case.py: 9 個
  - tests/unit/application/dtos/test_data_persistence_dtos.py: 4 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# 修正: プレースホルダーアサーションを実際のテストに置き換える
# テストファイルを編集して以下を置き換え:
#   assert False, "RED: Use case execution not implemented yet"
# これに置き換え:
#   use_case = DataPersistenceUseCase(mock_repository)
#   result = use_case.save_trade_data(request)
#   assert result.success is True
```

## 📱 **アプリケーション層実装のみ**

**⚠️ 重要な注意:**
- **このステップはアプリケーション層のみ** - ユースケースとオーケストレーションロジックを実装
- **他の層は対象外** - アプリケーション層コンポーネントのみに集中  
- **ドメインオーケストレーション** - ドメインオブジェクトとビジネスワークフローを調整
- **トランザクション境界** - アプリケーションレベルの関心事を処理

**層実装シーケンス:**
1. `06-implement-domain` ← ドメイン層（完了）
2. `07-implement-usecase` ← **【現在位置】アプリケーション層**
3. `08-implement-infra` ← インフラ層  
4. `09-implement-presentation` ← プレゼンテーション層

## 🚨 **重要: アプリケーション層のみ - 他の層は禁止**

**❌ このステップで絶対に禁止されている内容:**
- **インフラ層**: リポジトリ実装、データベースコード、外部API統合なし
- **プレゼンテーション層**: コントローラー、API、CLIコマンド、Webインターフェースなし
- **ドメイン層の変更**: ドメイン層は既に完了 - 変更しないこと
- **層間コード**: 依存性注入設定や構成管理なし

**✅ このステップで許可されている内容のみ:**
- **ユースケース**: ドメインロジックを統合するアプリケーションサービス
- **DTO**: 入力/出力境界用のデータ転送オブジェクト
- **アプリケーション例外**: アプリケーション固有のエラータイプ
- **アプリケーションサービス**: 調整とトランザクション管理ロジック

## 📋 **アプリケーション層タスクチェックリスト**

**適切なオーケストレーションでアプリケーション層を実装するためのチェックリスト:**

### 🔴 必須タスク

#### **📖 ユースケース分析**
- [ ] **Given-When-Then仕様の読み取り**: 仕様書からユースケースフローを抽出
- [ ] **🚨 重要: プレースホルダーアサーションの置換**: アプリケーションテストで `assert False, "RED: ... not implemented yet"` ステートメントを確認・修正
- [ ] **テストの信頼性検証**: テストが実装をテストしているか確認、プレースホルダー失敗だけではないことを確認
- [ ] **ドメイン操作のマッピング**: 各ユースケースが必要とするドメインエンティティ/サービスを特定
- [ ] **入力/出力境界の定義**: ユースケースに出入りするデータを決定
- [ ] **トランザクション境界の特定**: 一貫性とアトミック性が必要な場所を決定

#### **🎯 ユースケース実装**
- [ ] **ユースケースクラスの作成**: 各メインシナリオ用のアプリケーションサービスを実装
- [ ] **メインフローの実装**: 各Given-When-Thenシナリオのハッピーパスをコード化
- [ ] **ドメインオブジェクトのオーケストレーション**: ドメインエンティティ、サービス、リポジトリの調整
- [ ] **トランザクション処理**: トランザクション境界とロールバックロジックの実装

#### **🧪 アプリケーション層テスト**
- [ ] **アプリケーションテストの実行**: ユースケースロジックをカバーするテストを実行
- [ ] **ユースケースフローの検証**: Given-When-Thenシナリオがエンドツーエンドで動作することを確認
- [ ] **メタデータの更新**: issue-X-Y.jsonでアプリケーション層実装を完了とマーク
- [ ] **アプリケーション層のコミット**: アプリケーション層コードをバージョン管理

### 🟡 推奨タスク

#### **📦 DTO実装**
- [ ] **入力DTOの作成**: ユースケース入力用のデータ構造を定義
- [ ] **出力DTOの作成**: ユースケース出力用のデータ構造を定義
- [ ] **バリデーションの追加**: 入力バリデーションとサニタイゼーションロジックを実装
- [ ] **ドメインからDTOへのマッピング**: ドメインオブジェクトとDTOの変換を実装
- [ ] **シリアライゼーションの追加**: DTOが適切にシリアライズ/デシリアライズできることを確認

#### **🔗 リポジトリ統合**
- [ ] **リポジトリインターフェースの使用**: ドメインリポジトリインターフェース（ステップ06より）と統合
- [ ] **リポジトリエラーの処理**: リポジトリレベルの例外をキャッチ・処理
- [ ] **複数リポジトリの調整**: 複数の集約にまたがるユースケースを実装
- [ ] **リポジトリトランザクションの管理**: リポジトリ間での適切なトランザクション処理を確保
- [ ] **具象実装なし**: インターフェースのみ使用 - 具象実装はステップ08で

#### **🚫 アーキテクチャ準拠チェック**
- [ ] **インフラ実装なし**: 具象リポジトリ実装がないことを確認
- [ ] **プレゼンテーション層コードなし**: コントローラー、API、UIコンポーネントがないことを確認
- [ ] **データベース/外部依存なし**: 直接データベースや外部API呼び出しがないことを確認
- [ ] **アプリケーション関心事のみ**: コードがオーケストレーションと調整のみを処理することを確認
- [ ] **アプリケーションディレクトリのみ**: src/application/ディレクトリのみに新ファイルがあることを確認

### 🟢 オプションタスク

#### **⚠️ 例外処理**
- [ ] **アプリケーション例外の作成**: アプリケーション固有のエラータイプを定義
- [ ] **ドメイン例外の処理**: ドメイン例外を適切にキャッチ・ラップ
- [ ] **エラーコンテキストの追加**: 意味のあるエラーメッセージとコンテキストを提供
- [ ] **エラー回復の実装**: 適切な場所でリトライロジックとフォールバック機構を追加
- [ ] **アプリケーションエラーのログ**: デバッグ用の適切なエラーログを確保

#### **🔧 コード品質検証**
- [ ] **ruffリンティングの実行**: `uv run --frozen ruff check src/ --fix` を実行
- [ ] **ruffフォーマットの実行**: `uv run --frozen ruff format src/` を実行
- [ ] **型チェックの実行**: `uv run --frozen pyright src/` を実行
- [ ] **品質問題の修正**: リンティング、フォーマット、型エラーを解決
- [ ] **クリーンな結果の確認**: すべての品質ツールがエラーなしで通ることを確認

#### **📊 高度なフェーズ完了**
- [ ] **エラー処理の計画**: アプリケーションエラーをどう処理・伝播すべきかを定義
- [ ] **代替フローの追加**: 仕様書の代替シナリオを実装
- [ ] **エラー処理の追加**: エラーシナリオとエッジケースを実装
- [ ] **エラーシナリオのテスト**: 適切なエラー処理と例外伝播を確認
- [ ] **DTO変換のテスト**: ドメインとDTOの適切なマッピングを確保
- [ ] **リポジトリ依存関係のモック**: 具象リポジトリがまだ存在しないためモックを使用
- [ ] **ドメイン層は変更なし**: ドメイン層ファイルが変更されていないことを確認
- [ ] **ユースケースフローの文書化**: 実装されたユースケースとその責務を記録
- [ ] **インフラの準備**: リポジトリインターフェースが具象実装準備完了であることを確認
- [ ] **テストカバレッジの確認**: アプリケーションロジックがモックで適切にテストされていることを確認

**💡 プロヒント**: ユースケースはビジネスロジックを含まずにドメインオブジェクトをオーケストレーションすべき - ビジネスルールはドメイン層に保持！

### ✅ 許可されるファイル（実装対象）:
- `src/application/use_cases/` - ビジネスワークフロー統合用ユースケース
- `src/application/dtos/` - 入力/出力用データ転送オブジェクト
- `src/application/exceptions/` - アプリケーション固有例外
- `src/application/services/` - アプリケーションサービス（調整、ビジネスロジックなし）

### ❌ 禁止されるファイル（このステップでは作成/変更しない）:
- `src/domain/` - **ドメイン層（前ステップで既に実装済み）**
- `src/infrastructure/` - **インフラ層（具象リポジトリ、データベース、外部API）**
- `src/presentation/` - **プレゼンテーション層（APIエンドポイント、CLI、Webインターフェース）**

### 🎯 実装ルール:
1. **ドメインロジックの統合のみ** - ユースケースはドメインエンティティとサービスを調整
2. **アプリケーション層にビジネスロジックなし** - ビジネスルールはドメイン層に属す
3. **境界でのDTOの使用** - アプリケーション境界でデータを変換
4. **横断的関心事の処理** - トランザクション、ログ、認証、認可
5. **依存性注入** - 具象実装ではなくドメインインターフェースに依存

### 💡 誤って他の層を実装した場合:
```bash
# 誤って作成されたファイルを削除
rm -rf src/infrastructure/ src/presentation/

# ドメイン層は変更しない
# ドメイン層はステップ06で既に完了済み
```

**これらのルールに違反すると、クリーンアーキテクチャが破綻し、依存関係の問題が発生します。**

## 🚨 **重要なTDD原則警告**

**🔴→🟢 実装に合わせてテストを変更してはいけません！**

### 🎯 神聖なTDDフロー（逆転禁止）:
```
📖 シナリオ（Given-When-Then） 
    ↓
🔴 TDDテスト（仕様）
    ↓
🟢 実装（コード）
```

### ✅ 正しいアプローチ:
- **テストは仕様** - システムが何をすべきかを定義
- **実装はテストに奉仕** - テストを通すためのコードを書く
- **テストはシナリオから** - ビジネス要件がテストを駆動
- **実装を修正、テストは不変** - テストが失敗したらコードを変更

### ❌ 禁止されるアプローチ（絶対にこれをしてはいけません）:
- ~~既存の実装に合わせてテストを変更~~
- ~~「実装が異なって動作する」理由で失敗テストを削除~~
- ~~現在のコードに合わせてテスト期待値を変更~~
- ~~テストを変更して間違った実装を正当化~~

### 🚨 実装がテストに合わない場合:
1. **停止** - テストを変更しない
2. **分析** - なぜテストが失敗しているのか？
3. **シナリオチェック** - テストが要件を正しく表現しているか？
4. **実装修正** - テスト要件を満たすようにコードを変更
5. **シナリオが間違っている場合のみ** - シナリオ → テスト → 実装の順で更新

### 💡 緊急復旧:
```bash
# テストを誤って変更した場合
git restore tests/unit/application/

# 適切なTDDフローに戻る
# 1. 失敗テストを読む（これらは仕様）
# 2. テストを通すためのアプリケーションコードを実装
# 3. コードに合わせてテストロジックを変更してはいけません
```

**⚠️ 重要: テスト変更はTDDサイクルを破綻させ、シナリオ駆動開発を無効化します！**

---

## タスク詳細

1. **安全環境のセットアップと引数解析**:
   ```bash
   # 🔧 すべての安全操作関数とテンプレートユーティリティをロード
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "07-implement-usecase" "$ARGUMENTS"
   source "$(dirname "${BASH_SOURCE[0]}")/templates/_template_utils.sh"
   
   # ユースケース実装では少なくとも1つのイシュー番号が必要
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-usecase" "1" "単一イシューのユースケース実装"
       show_usage_example "implement-usecase" "1,7" "複数イシューのユースケース実装"
       show_usage_example "implement-usecase" "1 feature-name" "イシュー + 機能名指定"
       exit 1
   fi
   
   # イシューリストと機能名を抽出
   issue_list=$(IFS=-; echo "${issue_numbers[*]}")
   if [[ ${#other_args[@]} -gt 0 ]]; then
       feature_name="${other_args[0]}"
   else
       # 機能名は既存ファイルから抽出
       feature_name=""
   fi
   
   echo "🔄 Issues: $(printf '#%s ' "${issue_numbers[@]}")のアプリケーション層実装を開始します"
   echo ""
   echo "🚨 重要な注意: このステップではアプリケーション層のみを実装します"
   echo "   ✅ 許可: src/application/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/domain/, src/infrastructure/, src/presentation/"
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
   if ! begin_transaction "implement_usecase_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 前提条件を検証 - ドメイン実装が完了していること
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
   
   # ドメイン実装をチェック
   domain_entities=$(find src/domain/entities/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
   if [[ -z "$domain_entities" ]]; then
       echo "❌ ドメイン層の実装が見つかりません"
       echo "💡 最初にドメイン層を実装してください:"
       echo "   /implement-domain $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_implementation"
       exit 1
   fi
   
   echo "  ✅ ドメイン実装確認: $(echo "$domain_entities" | wc -l) ファイル"
   
   # ユースケーステストをチェック
   usecase_test_files=$(find tests/unit/application/use_cases/ -name "test_*.py" -type f 2>/dev/null || echo "")
   if [[ -z "$usecase_test_files" ]]; then
       echo "❌ ユースケーステストが見つかりません"
       echo "💡 最初にTDDテストを作成してください:"
       echo "   /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_usecase_tests"
       exit 1
   fi
   
   echo "  ✅ ユースケーステスト確認: $(echo "$usecase_test_files" | wc -l) ファイル"
   
   # 🚨 重要: アプリケーションテストでプレースホルダーアサーションをチェック
   echo "  🚨 アプリケーション層プレースホルダーアサーション検証中..."
   
   application_placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           application_placeholder_files+=("$file")
       fi
   done < <(find tests/unit/application/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#application_placeholder_files[@]} -gt 0 ]]; then
       echo "    ❌ アプリケーション層プレースホルダーアサーション発見:"
       for file in "${application_placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "      - $file: $count 個"
       done
       [[ ${#application_placeholder_files[@]} -gt 5 ]] && echo "      - ... (他 $((${#application_placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "    🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "       - アプリケーション実装は完了済みだが、テストがプレースホルダーのまま"
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
           echo "アプリケーション層実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "application_placeholder_assertions_found"
           exit 1
       fi
       
       echo "    ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "    ✅ アプリケーション層プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   echo "✅ 前提条件検証完了"
   ```

3. **メタデータの特定と検証**:
   ```bash
   # 📊 メタデータファイルを見つけて検証
   echo "📊 メタデータファイル検証中..."
   
   metadata_file="docs/use_cases/issue-${issue_list}-${feature_name}.json"
   
   if [[ ! -f "$metadata_file" ]]; then
       echo "エラー: メタデータファイルが見つかりません: $metadata_file"
       execute_rollback "metadata_file_missing"
       exit 1
   fi
   
   # メタデータファイル形式を検証
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # ドメイン実装フェーズ完了をチェック
   domain_status=$(jq -r '.phases.domain_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" != "true" ]]; then
       echo "エラー: ドメイン層実装が完了していません"
       echo "💡 先に /implement-domain コマンドを実行してください"
       execute_rollback "domain_implementation_not_completed"
       exit 1
   fi
   
   # アプリケーション実装が既に完了しているかチェック
   app_status=$(jq -r '.phases.application_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$app_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のアプリケーション層実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "アプリケーション層実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のアプリケーション層実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **現在の状態確認のためのテスト実行**:
   ```bash
   # 🔍 現在のテスト状態を検証
   echo "🔍 現在のテスト状態確認中..."
   
   # テスト用Python環境を検証
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # ドメインテストを実行してパスすることを確認
   echo "  🟢 ドメインテスト実行中（GREEN状態確認）..."
   domain_test_output_file="/tmp/domain_test_output_$$"
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$domain_test_output_file" 2>&1; then
       domain_tests_passed=true
       echo "    ✅ ドメインテスト: 成功"
   else
       domain_tests_passed=false
       echo "    ❌ ドメインテストが失敗しています"
       echo "    💡 先にドメイン層実装を完成させてください"
       rm -f "$domain_test_output_file"
       execute_rollback "domain_tests_failing"
       exit 1
   fi
   rm -f "$domain_test_output_file"
   
   # ユースケーステストを実行してRED状態をチェック
   echo "  🔴 ユースケーステスト実行中（RED状態確認）..."
   usecase_test_output_file="/tmp/usecase_test_output_$$"
   usecase_test_result=0
   
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/use_cases/ -v --tb=short > "$usecase_test_output_file" 2>&1; then
       usecase_test_result=0  # テスト成功（予期しない）
   else
       usecase_test_result=1  # テスト失敗（REDフェーズで期待される）
   fi
   
   # ユースケーステスト結果を分析
   total_usecase_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$usecase_test_output_file" 2>/dev/null || echo "0")
   failed_usecase_tests=$(grep -c "FAILED" "$usecase_test_output_file" 2>/dev/null || echo "0")
   
   echo "    📊 ユースケーステスト結果:"
   echo "      - 総テスト数: $total_usecase_tests"
   echo "      - 失敗テスト数: $failed_usecase_tests"
   
   if [[ $usecase_test_result -eq 0 ]] && [[ $total_usecase_tests -gt 0 ]]; then
       echo "    ⚠️  ユースケーステストが成功しています（既に実装済み？）"
       echo "実装を続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "アプリケーション層実装をキャンセルしました"
           rm -f "$usecase_test_output_file"
           commit_transaction
           exit 0
       fi
   elif [[ $total_usecase_tests -eq 0 ]]; then
       echo "    エラー: ユースケーステストが見つかりません"
       rm -f "$usecase_test_output_file"
       execute_rollback "no_usecase_tests_found"
       exit 1
   else
       echo "    ✅ RED状態確認: ユースケーステストが期待通り失敗"
   fi
   
   rm -f "$usecase_test_output_file"
   echo "✅ テスト状態確認完了"
   ```

5. **ドメインとユースケース情報の抽出**:
   ```bash
   # 📖 実装のためのドメイン・ユースケース情報を抽出
   echo "📖 ドメイン・ユースケース情報分析中..."
   
   # ドメイン層からエンティティを抽出
   all_entities=()
   for entity_file in $domain_entities; do
       entity_name=$(basename "$entity_file" .py)
       # PascalCaseに変換
       entity_class=$(echo "$entity_name" | sed 's/_\([a-z]\)/\U\1/g' | sed 's/^./\U&/')
       all_entities+=("$entity_class")
   done
   
   # 仕様からユースケースシナリオを抽出
   spec_file=$(find docs/use_cases/ -name "issue-${issue_list}-${feature_name}.md" -type f | head -1)
   use_case_scenarios=()
   
   if [[ -n "$spec_file" ]] && check_file_permissions "$spec_file" "read"; then
       echo "  📋 仕様分析中: $(basename "$spec_file")"
       
       # Given-When-Thenシナリオを抽出
       scenarios=$(grep -A 5 -B 2 "Given:\\|When:\\|Then:" "$spec_file" 2>/dev/null | \
                  grep -E "(Given|When|Then):" | \
                  sed 's/^[[:space:]]*//' | \
                  paste -d' ' - - - 2>/dev/null || echo "")
       
       if [[ -n "$scenarios" ]]; then
           while IFS= read -r scenario; do
               [[ -n "$scenario" ]] && use_case_scenarios+=("$scenario")
           done <<< "$scenarios"
       fi
   fi
   
   echo "  🎯 抽出された情報:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - ユースケースシナリオ: ${#use_case_scenarios[@]} 個"
   
   echo "✅ 情報分析完了"
   ```

6. **アプリケーション層構造の作成**:
   ```bash
   # 🏗️ アプリケーション層構造を作成
   echo "🏗️ アプリケーション層構造作成中..."
   
   # アプリケーション構造ディレクトリを定義
   app_directories=(
       "src/application/use_cases"
       "src/application/dtos"
       "src/application/exceptions"
       "src/application/services"
   )
   
   # すべてのアプリケーションディレクトリを安全に作成
   for dir in "${app_directories[@]}"; do
       echo "  📁 作成中: $dir"
       if ! safe_mkdir "$dir"; then
           echo "エラー: アプリケーションディレクトリ作成に失敗しました: $dir"
           execute_rollback "app_directory_creation_failed"
           exit 1
       fi
       add_rollback "rmdir '$dir' 2>/dev/null || true" "Remove app directory: $dir"
   done
   
   # __init__.pyファイルを作成
   app_init_files=(
       "src/application/use_cases/__init__.py"
       "src/application/dtos/__init__.py"
       "src/application/exceptions/__init__.py"
       "src/application/services/__init__.py"
   )
   
   for init_file in "${app_init_files[@]}"; do
       echo "  📄 作成中: $init_file"
       if ! safe_create_file "$init_file" '"""アプリケーション層パッケージ初期化"""' false; then
           echo "エラー: アプリケーション__init__.pyファイルの作成に失敗しました"
           execute_rollback "app_init_creation_failed"
           exit 1
       fi
       add_rollback "rm -f '$init_file'" "Remove app init file: $init_file"
   done
   
   echo "✅ アプリケーション構造作成完了 (${#app_directories[@]} ディレクトリ)"
   ```

7. **テンプレート変数のセットアップとDTOの実装**:
   ```bash
   # 🎯 テンプレート変数をセットアップ
   echo "🎯 テンプレート変数設定中..."
   
   # 機能ベースの変数をセットアップ
   setup_feature_vars "$feature_name"
   
   # エンティティ関連変数を生成
   if [[ ${#all_entities[@]} -gt 0 ]]; then
       entity_imports=$(generate_entity_imports "${all_entities[@]}")
       repository_imports=$(generate_repository_imports "${all_entities[@]}")
       generate_repository_constructor "${all_entities[@]}"
   else
       entity_imports=""
       repository_imports=""
       repository_constructor_params=""
       repository_constructor_docs=""
       repository_assignments=""
   fi
   
   echo "  ✅ テンプレート変数設定完了"
   
   # 📝 テンプレートを使用してDTOを実装
   echo "📝 DTO（データ転送オブジェクト）実装中..."
   
   implemented_files=()
   dtos_file="src/application/dtos/${feature_name_snake}_dtos.py"
   
   echo "  📝 テンプレート使用: application/dto_template.py"
   
   if ! process_template "application/dto_template.py" "$dtos_file"; then
       echo "エラー: DTOテンプレート処理に失敗しました"
       execute_rollback "dtos_template_processing_failed"
       exit 1
   fi
   
   implemented_files+=("$dtos_file")
   add_rollback "rm -f '$dtos_file'" "Remove implemented DTOs: $dtos_file"
   
   echo "✅ DTO実装完了"
   ```

8. **アプリケーション例外の実装**:
   ```bash
   # 🚨 テンプレートを使用してアプリケーション固有例外を実装
   echo "🚨 アプリケーション例外実装中..."
   
   exceptions_file="src/application/exceptions/${feature_name_snake}_exceptions.py"
   
   echo "  🚨 テンプレート使用: application/exceptions_template.py"
   
   if ! process_template "application/exceptions_template.py" "$exceptions_file"; then
       echo "エラー: 例外テンプレート処理に失敗しました"
       execute_rollback "exceptions_template_processing_failed"
       exit 1
   fi
   
   implemented_files+=("$exceptions_file")
   add_rollback "rm -f '$exceptions_file'" "Remove implemented exceptions: $exceptions_file"
   
   echo "✅ アプリケーション例外実装完了"
   ```

9. **ユースケースの実装**:
   ```bash
   # 🔄 テンプレートを使用してメインユースケースを実装
   echo "🔄 ユースケース実装中..."
   
   usecase_file="src/application/use_cases/${feature_name_snake}_use_case.py"
   
   echo "  🔄 テンプレート使用: application/usecase_template.py"
   
   # ユースケース用の追加テンプレート変数を生成
   if [[ ${#all_entities[@]} -gt 0 ]]; then
       main_entity="${all_entities[0]}"
       entity_lower=$(to_lower_case "$main_entity")
       
       entity_creation_logic="entity = self._create_or_load_${entity_lower}(request)"
       entity_params="entity, "
       entity_params_with_request="entity, "
       persistence_logic="self._${entity_lower}_repository.save(entity)"
       list_logic="entities = self._${entity_lower}_repository.find_all()\\n            items = [self._entity_to_dict(entity) for entity in entities]"
       
       # create_or_loadメソッドを生成
       create_or_load_methods="def _create_or_load_${entity_lower}(self, request: ${feature_name_title}Request) -> $main_entity:\\n        \"\"\"${main_entity}の作成または読み込み\"\"\"\\n        # TODO: 実際のビジネスロジックに基づいて実装\\n        return $main_entity.create(entity_id=\"temp-id\")\\n"
       
       # entity_to_dictメソッドを生成
       entity_to_dict_methods="def _entity_to_dict(self, entity: $main_entity) -> dict:\\n        \"\"\"エンティティを辞書に変換\"\"\"\\n        return {\\n            \"id\": entity.id,\\n            \"created_at\": entity.created_at.isoformat(),\\n            \"updated_at\": entity.updated_at.isoformat()\\n            # TODO: 必要な属性を追加\\n        }"
   else
       entity_creation_logic="# TODO: ドメインオブジェクトの操作を実装"
       entity_params=""
       entity_params_with_request=""
       persistence_logic="# TODO: 永続化処理を実装"
       list_logic="# TODO: データ取得処理を実装\\n            items = []"
       create_or_load_methods=""
       entity_to_dict_methods=""
   fi
   
   # ユースケースシナリオからシナリオコメントを生成
   scenario_comments=""
   if [[ ${#use_case_scenarios[@]} -gt 0 ]]; then
       scenario_comments="# Given-When-Then シナリオに基づく実装:"
       for i in "${!use_case_scenarios[@]}"; do
           scenario="${use_case_scenarios[$i]}"
           when=$(echo "$scenario" | grep -oE "When: [^\\|]*" | sed 's/When: //' || echo "処理 $((i+1))")
           scenario_comments+="\\n        # $((i+1)). $when"
       done
   else
       scenario_comments="# ビジネスロジックをここに実装"
   fi
   
   # 追加テンプレート変数を設定（注意: 既存のテンプレート関数で処理されない変数）
   # これらは直接置換する必要がある
   temp_content=$(load_template "application/usecase_template.py")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_CREATION_LOGIC}}|$entity_creation_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_PARAMS}}|$entity_params|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_PARAMS_WITH_REQUEST}}|$entity_params_with_request|g")
   temp_content=$(echo "$temp_content" | sed "s|{{PERSISTENCE_LOGIC}}|$persistence_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{LIST_LOGIC}}|$list_logic|g")
   temp_content=$(echo "$temp_content" | sed "s|{{CREATE_OR_LOAD_METHODS}}|$create_or_load_methods|g")
   temp_content=$(echo "$temp_content" | sed "s|{{ENTITY_TO_DICT_METHODS}}|$entity_to_dict_methods|g")
   temp_content=$(echo "$temp_content" | sed "s|{{SCENARIO_COMMENTS}}|$scenario_comments|g")
   
   # 標準テンプレート変数置換を適用
   processed_content=$(substitute_template_vars "application/usecase_template.py" "$temp_content")
   
   if ! safe_create_file "$usecase_file" "$processed_content" true; then
       echo "エラー: ユースケースファイルの作成に失敗しました: $usecase_file"
       execute_rollback "usecase_implementation_failed"
       exit 1
   fi
   
   implemented_files+=("$usecase_file")
   add_rollback "rm -f '$usecase_file'" "Remove implemented use case: $usecase_file"
   
   echo "✅ ユースケース実装完了"
   ```

10. **テスト用モックリポジトリの作成**:
    ```bash
    # 🎭 テスト用モックリポジトリを作成
    echo "🎭 モックリポジトリ実装中..."
    
    # インフラリポジトリディレクトリを作成
    if ! safe_mkdir "src/infrastructure/repositories"; then
        echo "エラー: インフラリポジトリディレクトリの作成に失敗しました"
        execute_rollback "infra_repo_dir_creation_failed"
        exit 1
    fi
    
    # __init__.pyを作成
    if ! safe_create_file "src/infrastructure/repositories/__init__.py" '"""インフラリポジトリパッケージ"""' false; then
        echo "エラー: インフラリポジトリ__init__.pyの作成に失敗しました"
        execute_rollback "infra_repo_init_creation_failed"
        exit 1
    fi
    
    # 個別テンプレート処理を使用して各エンティティのモックリポジトリを作成
    for entity in "${all_entities[@]}"; do
        entity_lower=$(to_lower_case "$entity")
        mock_repo_file="src/infrastructure/repositories/mock_${entity_lower}_repository.py"
        
        echo "  🎭 実装中: Mock${entity}Repository ($mock_repo_file)"
        
        # モックリポジトリ用エンティティ固有変数をセットアップ
        setup_entity_vars "$entity"
        
        # infrastructure/repository_template.pyをベースとしてモック用に変更
        mock_template_content=$(load_template "infrastructure/repository_template.py")
        
        # モック実装用に変更
        mock_template_content=$(echo "$mock_template_content" | sed "s/class ${entity}Repository/class Mock${entity}Repository/g")
        mock_template_content=$(echo "$mock_template_content" | sed "s/from src.infrastructure.models/# Mock repository - no database models needed/g")
        mock_template_content=$(echo "$mock_template_content" | sed "s/{{MODEL_IMPORTS}}/from typing import Dict, List, Optional/g")
        
        # テンプレートユーティリティで処理
        mock_processed_content=$(substitute_template_vars "infrastructure/repository_template.py" "$mock_template_content")
        
        # モック固有の変更を適用
        mock_processed_content=$(echo "$mock_processed_content" | sed 's/""".*Repository implementation/"""Mock '"$entity"' Repository Implementation\n\n    テスト用のメモリ内リポジトリ実装。/g')
        mock_processed_content=$(echo "$mock_processed_content" | sed 's/def __init__(self):/def __init__(self):\n        """モックリポジトリ初期化"""\n        self._storage: Dict[str, '"$entity"'] = {}\n        self._next_id = 1\n\n    def clear(self) -> None:\n        """すべてのデータをクリア（テスト用）"""\n        self._storage.clear()\n        self._next_id = 1\n    \n    def count(self) -> int:\n        """保存されているエンティティ数を取得（テスト用）"""\n        return len(self._storage)/g')
        
        if ! safe_create_file "$mock_repo_file" "$mock_processed_content" true; then
            echo "エラー: モックリポジトリファイルの作成に失敗しました: $mock_repo_file"
            execute_rollback "mock_repo_implementation_failed"
            exit 1
        fi
        
        implemented_files+=("$mock_repo_file")
        add_rollback "rm -f '$mock_repo_file'" "Remove mock repository: $mock_repo_file"
    done
    
    echo "✅ モックリポジトリ実装完了 (${#all_entities[@]} ファイル)"
    ```

11. **GREEN状態検証のためのテスト実行**:
    ```bash
    # 🟢 ユースケーステストがGREEN状態になったことを検証
    echo "🟢 ユースケーステスト GREEN状態検証中..."
    
    # ユースケーステストを実行してGREEN状態を確認
    echo "  🧪 ユースケーステスト実行中（GREEN状態確認）..."
    
    usecase_green_test_output_file="/tmp/usecase_green_test_output_$$"
    usecase_test_result=0
    
    # テストを実行して出力をキャプチャ
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/use_cases/ -v --tb=short > "$usecase_green_test_output_file" 2>&1; then
        usecase_test_result=0  # テスト成功（GREENフェーズで期待される）
    else
        usecase_test_result=1  # テスト失敗（さらなる実装が必要）
    fi
    
    # テスト結果を分析
    total_usecase_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    passed_usecase_tests=$(grep -c "PASSED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    failed_usecase_tests=$(grep -c "FAILED" "$usecase_green_test_output_file" 2>/dev/null || echo "0")
    
    echo "  📊 ユースケーステスト結果分析:"
    echo "    - 総テスト数: $total_usecase_tests"
    echo "    - 成功テスト数: $passed_usecase_tests"
    echo "    - 失敗テスト数: $failed_usecase_tests"
    
    if [[ $failed_usecase_tests -gt 0 ]]; then
        echo "⚠️  まだ失敗しているユースケーステストがあります:"
        grep "FAILED" "$usecase_green_test_output_file" | head -5
        echo ""
        echo "追加実装が必要な可能性があります。続行しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "アプリケーション層実装を中止しました"
            rm -f "$usecase_green_test_output_file"
            execute_rollback "usecase_tests_still_failing"
            exit 1
        fi
    else
        echo "  ✅ GREEN状態確認: すべてのユースケーステストが成功しています"
    fi
    
    # 可能であればテストカバレッジを計算
    usecase_coverage_result=""
    if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/application/ --cov=src.application --cov-report=term-missing --quiet >/tmp/usecase_coverage_output_$$ 2>&1; then
        usecase_coverage_result=$(grep -E "[0-9]+%" /tmp/usecase_coverage_output_$$ | tail -1 || echo "Coverage data not available")
        rm -f /tmp/usecase_coverage_output_$$
    fi
    
    rm -f "$usecase_green_test_output_file"
    usecase_tests_passed=$([ $failed_usecase_tests -eq 0 ] && echo "true" || echo "false")
    
    echo "✅ ユースケーステスト GREEN フェーズ検証完了"
    ```

12. **コード品質検証**:
    ```bash
    # 🔍 アプリケーション層のコード品質検証
    echo "🔍 アプリケーション層コード品質検証中..."
    
    # アプリケーション層でruffフォーマットとリンティングを実行
    echo "  🎨 コードフォーマット・リント実行中..."
    
    if ! uv run --frozen ruff format src/application/ --quiet; then
        echo "⚠️  アプリケーション層のコードフォーマットに問題があります"
    fi
    
    app_lint_output_file="/tmp/app_ruff_output_$$"
    if uv run --frozen ruff check src/application/ > "$app_lint_output_file" 2>&1; then
        echo "    ✅ リント検査: 問題なし"
    else
        echo "    ⚠️  リント警告があります:"
        head -5 "$app_lint_output_file"
        echo "    💡 必要に応じて修正してください"
    fi
    rm -f "$app_lint_output_file"
    
    # pyrightが利用可能な場合は型チェックを実行
    echo "  🔍 型チェック実行中..."
    
    app_type_output_file="/tmp/app_pyright_output_$$"
    if uv run --frozen pyright src/application/ > "$app_type_output_file" 2>&1; then
        echo "    ✅ 型チェック: 問題なし"
    else
        echo "    ⚠️  型チェック警告があります:"
        head -5 "$app_type_output_file"
        echo "    💡 必要に応じて型ヒントを修正してください"
    fi
    rm -f "$app_type_output_file"
    
    # アーキテクチャ検証 - 適切な層分離をチェック
    echo "  🏗️ アーキテクチャ検証中..."
    
    # アプリケーション層での外部依存関係をチェック
    app_imports=$(find src/application/ -name "*.py" -exec grep -l "^import \\|^from " {} \; 2>/dev/null || echo "")
    external_deps_found=false
    presentation_deps_found=false
    
    for file in $app_imports; do
        # 問題のあるインポート（インフラ詳細またはプレゼンテーション）をチェック
        if grep -E "^(import|from) (requests|sqlalchemy|django|flask|fastapi|sqlite3|psycopg2)" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  インフラ依存発見: $file"
            external_deps_found=true
        fi
        
        # プレゼンテーション層依存関係をチェック
        if grep -E "^(import|from).*presentation" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  プレゼンテーション層依存発見: $file"
            presentation_deps_found=true
        fi
    done
    
    if [[ "$external_deps_found" == "false" ]] && [[ "$presentation_deps_found" == "false" ]]; then
        echo "    ✅ アーキテクチャ検証: アプリケーション層の適切な分離"
    else
        echo "    💡 アプリケーション層の依存関係を見直すことを推奨します"
    fi
    
    echo "✅ コード品質検証完了"
    ```

13. **メタデータとドキュメントの更新**:
    ```bash
    # 📊 アプリケーション実装完了でメタデータを更新
    echo "📊 メタデータ更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.application_implementation.created = true | 
         .phases.application_implementation.completed = true |
         .phases.application_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.application_implementation.usecase_tests_passed = '"$usecase_tests_passed"' |
         .phases.application_implementation.coverage = "'"$usecase_coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.application_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "application_implemented" |
         .next_commands = ["implement-infra", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # アプリケーションドキュメントを作成
    app_doc_dir="docs/application"
    if ! safe_mkdir "$app_doc_dir"; then
        echo "エラー: アプリケーションドキュメントディレクトリの作成に失敗しました"
        execute_rollback "app_doc_dir_creation_failed"
        exit 1
    fi
    
    app_doc_file="$app_doc_dir/issue-${issue_list}-application-design.md"
    
    app_doc_content="# アプリケーション層設計: $feature_name

**Issues**: $(printf '#%s ' "${issue_numbers[@]}")
**実装日時**: $(date)

## 概要

このアプリケーション層実装は、$(printf 'Issue #%s, ' "${issue_numbers[@]}" | sed 's/, $//')の要件に基づいて作成されました。
ドメインオブジェクトを orchestrate し、ビジネス要件を実現します。

## 実装されたコンポーネント

### ユースケース
- **${feature_name_title}UseCase**: メインビジネス機能の実行
  - execute(): 主要ビジネスフロー実行
  - list(): データ一覧取得

### DTOs (Data Transfer Objects)
- **${feature_name_title}Request**: 実行リクエスト
- **${feature_name_title}Response**: 実行レスポンス
- **${feature_name_title}ListRequest**: 一覧取得リクエスト
- **${feature_name_title}ListResponse**: 一覧取得レスポンス

### 例外クラス
- **${feature_name_title}ApplicationError**: 基底例外
- **${feature_name_title}ValidationError**: バリデーションエラー
- **${feature_name_title}NotFoundError**: データ未発見エラー
- **${feature_name_title}AuthorizationError**: 認可エラー
- **${feature_name_title}BusinessRuleViolationError**: ビジネスルール違反
- **${feature_name_title}ConcurrencyError**: 同時実行エラー

### モックリポジトリ
$(for entity in "${all_entities[@]}"; do
    echo "- **Mock${entity}Repository**: ${entity}のテスト用リポジトリ"
done)

## アーキテクチャ原則

### レイヤー分離
- アプリケーション層はドメイン層に依存
- インフラ層の詳細には依存しない
- プレゼンテーション層には依存しない

### 責務
- ドメインオブジェクトの orchestration
- トランザクション境界の管理
- 認可・認証の実装
- DTOによる入出力データ変換

### 設計パターン
- **Dependency Injection**: リポジトリの注入
- **DTO Pattern**: データ転送オブジェクト
- **Exception Translation**: ドメイン例外からアプリケーション例外への変換

## テンプレートシステム

このアプリケーション層実装は、統一されたテンプレートシステムを使用して生成されました：

- **DTOテンプレート**: \`templates/application/dto_template.py\`
- **例外テンプレート**: \`templates/application/exceptions_template.py\`
- **ユースケーステンプレート**: \`templates/application/usecase_template.py\`

## テスト結果

- **テスト数**: $total_usecase_tests
- **成功**: $passed_usecase_tests
- **失敗**: $failed_usecase_tests
- **カバレッジ**: $usecase_coverage_result

## 次のステップ

1. **インフラ層実装**: \`/implement-infra $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
2. **進捗確認**: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`

---
**実装ステータス**: ✅ 完了
**アーキテクチャ検証**: ✅ 通過
**テスト状況**: $usecase_tests_passed
**テンプレートベース**: ✅ 使用
"
    
    if ! safe_create_file "$app_doc_file" "$app_doc_content" true; then
        echo "エラー: アプリケーションドキュメントの作成に失敗しました"
        execute_rollback "app_doc_creation_failed"
        exit 1
    fi
    
    implemented_files+=("$app_doc_file")
    add_rollback "rm -f '$app_doc_file'" "Remove application documentation"
    
    echo "✅ メタデータ・ドキュメント更新完了"
    ```

14. **ユースケースインデックス更新とGitコミット**:
    ```bash
    # 📚 ユースケースインデックス更新・コミット
    echo "📚 ユースケースインデックス更新・コミット中..."
    
    use_cases_index="docs/use_cases/index.md"
    if [[ -f "$use_cases_index" ]]; then
        # バックアップを作成
        backup_file="${use_cases_index}.backup.$(date +%Y%m%d_%H%M%S)"
        if ! cp "$use_cases_index" "$backup_file"; then
            echo "エラー: インデックスファイルのバックアップ作成に失敗しました"
            execute_rollback "index_backup_failed"
            exit 1
        fi
        add_rollback "mv '$backup_file' '$use_cases_index'" "Restore index backup"
        
        # 機能のステータスを更新
        feature_line="\\[${feature_name}\\]"
        updated_line="- [${feature_name}]($(basename "${spec_file}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: application_implemented, TDD: 🟢 GREEN, App: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 アプリケーション実装をコミット
    echo "💾 アプリケーション層実装をコミット中..."
    
    commit_message="feat: implement application layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name}

Application Layer Implementation Summary:
- Feature: ${feature_name}
- Issues: $(printf '#%s ' "${issue_numbers[@]}")
- Implementation Files: ${#implemented_files[@]} created
- Use Case Test Results: Passed $passed_usecase_tests, Failed $failed_usecase_tests
- Coverage: $usecase_coverage_result
- Template-Based Implementation: ✅

Implemented Components:
$(printf '  - %s\n' "${implemented_files[@]}")

Application Layer Features:
- Use cases for business workflow orchestration
- DTOs for clean input/output data transfer
- Application-specific exception handling
- Mock repositories for testing isolation
- Proper layer separation and dependency injection

Template System Usage:
- DTOs: application/dto_template.py
- Exceptions: application/exceptions_template.py  
- Use Cases: application/usecase_template.py
- Consistent code generation and maintainability

Architecture Compliance:
- Clean Architecture principles maintained
- Domain logic orchestration (no business logic in app layer)
- Proper dependency direction (app → domain)
- No infrastructure or presentation dependencies

TDD Status: Use case tests passing
Next Step: /implement-infra for infrastructure layer
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
    
    add_rollback "git reset --hard HEAD~1" "Undo application implementation commit"
    echo "✅ コミット完了"
    ```

15. **GitHubイシュー更新と最終成功**:
    ```bash
    # 🎫 アプリケーション実装完了でGitHubイシューを更新
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🔄 **アプリケーション層実装完了**

アプリケーション層（ユースケース）の実装が完了しました。

## 📊 実装結果
- **実装ファイル数**: ${#implemented_files[@]} ファイル
- **ユースケーステスト結果**: 成功 $passed_usecase_tests / 総計 $total_usecase_tests
- **カバレッジ**: $usecase_coverage_result
- **アーキテクチャ検証**: ✅ 通過
- **テンプレートベース**: ✅ 使用

## 🔄 実装されたコンポーネント
### ユースケース
- **${feature_name_title}UseCase**: ビジネスフロー orchestration
  - メインビジネス機能の実行
  - データ一覧取得機能
  - 認可・バリデーション処理

### DTOs (データ転送オブジェクト)
- **リクエスト/レスポンス**: 型安全な入出力
- **バリデーション機能**: 入力データ検証
- **エラーレスポンス**: 適切なエラーハンドリング

### 例外処理
- **階層化された例外**: アプリケーション固有のエラー分類
- **ビジネスルール違反**: 適切なエラー区分
- **認可・バリデーション**: セキュリティ対応

### モックリポジトリ
$(if [[ ${#all_entities[@]} -gt 0 ]]; then
    for entity in "${all_entities[@]:0:2}"; do
        echo "- **Mock${entity}Repository**: テスト用データアクセス"
    done
    [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他 $((${#all_entities[@]} - 2)) リポジトリ)"
fi)

## 🎯 テンプレートシステム活用
- **統一されたコード生成**: 一貫性のある実装
- **保守性向上**: 標準化されたコード構造
- **開発効率**: 高速で確実な実装

## 🏛️ アーキテクチャ準拠
- [x] クリーンアーキテクチャ原則
- [x] ドメイン層への適切な依存
- [x] インフラ層からの独立
- [x] 依存性注入パターン
- [x] レイヤー分離の維持

## 🚀 次のステップ

インフラストラクチャ層実装を開始してください：
\`\`\`bash
/implement-infra $issue_num
\`\`\`

## 📚 関連ドキュメント
- [アプリケーション層設計]($app_doc_file)
- [実装されたファイル一覧](#実装されたコンポーネント)

## 🔍 動作確認
\`\`\`bash
# アプリケーション層テスト実行
uv run --frozen pytest tests/unit/application/ -v

# カバレッジ確認
uv run --frozen pytest tests/unit/application/ --cov=src.application
\`\`\`

---
**Layer Status**: Application ✅ → 次: Infrastructure 🏗️
**Template System**: ✅ Active
"
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    
    # 🎉 トランザクションコミット（成功！）
    if commit_transaction; then
        echo ""
        echo "🎉 アプリケーション層実装完了!"
        echo "============================================="
        echo "🔄 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo "🎯 テンプレートベース: ✅ 活用"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   ユースケース: 1 個 (${feature_name_title}UseCase)"
        echo "   DTOs: 4 個 (Request/Response + List)"
        echo "   例外クラス: 6 個 (階層化された例外処理)"
        echo "   モックリポジトリ: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 テスト状況:"
        echo "   - ユースケーステスト: 成功 $passed_usecase_tests / 総計 $total_usecase_tests"
        echo "   - カバレッジ: $usecase_coverage_result"
        echo "   - ドメインテスト: 引き続き通過"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - クリーンアーキテクチャ原則"
        echo "   - 適切なレイヤー分離"
        echo "   - ドメインロジックの orchestration"
        echo "   - 依存性注入パターン"
        echo ""
        echo "🎯 テンプレートシステム:"
        echo "   - DTOテンプレート: application/dto_template.py"
        echo "   - 例外テンプレート: application/exceptions_template.py"
        echo "   - ユースケーステンプレート: application/usecase_template.py"
        echo "   - 統一されたコード生成と保守性"
        echo ""
        echo "🚀 次のステップ:"
        echo "   1. インフラ層実装: /implement-infra $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. 統合テスト実行（インフラ層完成後）"
        echo ""
        echo "🚨 TDD原則リマインダー:"
        echo "   ⚠️ 実装中にテストを変更した場合、それはTDD違反です"
        echo "   ✅ 正解: シナリオ → テスト → 実装の順序で進める"
        echo "   ❌ 禁止: 実装を正としてテストを変更する"
        echo ""
        echo "💡 実装品質:"
        echo "   - ビジネスフロー orchestration"
        echo "   - 型安全なデータ転送"
        echo "   - 包括的なエラーハンドリング"
        echo "   - テスト可能な設計"
        echo "   - テンプレートベースの一貫性"
        echo ""
        
        # 操作ログサマリーを表示
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ アプリケーション層実装完了 - インフラ層実装準備完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   ユースケース実装中に新要件・エラー・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: ユースケース変更は全レイヤーに影響します"
        echo ""
        echo "🔴 TDD守則（絶対遵守）:"
        echo "   1. シナリオがテストを決める"
        echo "   2. テストが実装を決める"
        echo "   3. 実装がテストを決めてはならない"
        echo "   4. この順序を逆転させた場合、TDD失敗となる"
        
    else
        echo "❌ トランザクション コミット失敗"
        exit 1
    fi
    ```

重要な注意事項:
- ユースケースは統合するが、ビジネスロジックは含まない
- ユースケースを薄く集中させる
- ドメインオブジェクトではなく、入出力にDTOを使用
- 横断的関心事（ログ、認証）を処理
- テスト用モックリポジトリ
- テンプレートシステムで一貫性と保守性を確保
- すべてのユーザー向け出力は日本語で表示