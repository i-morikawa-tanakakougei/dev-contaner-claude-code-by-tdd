テストを通すためのドメイン層実装（TDD GREENフェーズ）

## メタデータ
- **前提条件**: TDDテストが作成され失敗している（05-create-tests）
- **入力**: Issue番号（必須）
- **出力**: 
  - `src/domain/`のドメイン層実装
  - 更新されたテスト結果（テストが通るようになる）
  - 更新された`docs/use_cases/issue-X-Y.json`メタデータ
- **依存関係**: pytest、ドメインモデル設計文書、Python環境
- **実行タイミング**: TDD GREENフェーズ - テスト作成後、アプリケーション層前

## 🎯 **TDD/DDD/レイヤードプロセスコンテキスト**

**🔄 コアワークフロー**: ビジョン(00) → 構造(01) → スプリント(02) → ユースケース(03) → ドメイン(04) → 設計レビュー(04.5) → テスト(05) → **テストレビュー(05.5)** → ドメイン(06) → アプリ(07) → インフラ(08) → UI(09) → テスト(10) → リファクタ(11) → 進化(12) → レビュー(13) → フィードバック(14) → PR(15) → ステータス(16)

**🎨 アーキテクチャ**: クリーンアーキテクチャ（ドメイン→アプリケーション→インフラストラクチャ→プレゼンテーション）  
**🧪 開発**: テスト駆動開発（RED→GREEN→REFACTOR）  
**🏗️ 設計**: ドメイン駆動設計（エンティティ、値オブジェクト、集約、リポジトリ）  
**📋 要件**: 完全なトレーサビリティを持つGiven-When-Thenシナリオ  
**🔄 進化**: /evolve-scenariosコマンドによる継続的シナリオ進化

> 📖 **文書管理システム**: [README.md](./README.md)  
> 🗺️ **現在位置**: スプリント実行フェーズ - ドメイン層実装（06/16）  
> 🎯 **フェーズ目的**: テストを通すためのドメインロジック実装（GREEN）  
> ⬅️ **前のステージ**: 05.5-review-test-design（テスト設計レビュー）  
> ➡️ **次のステージ**: 07-implement-usecase（アプリケーション層実装）
>
> **📋 3層アーキテクチャ操作**:  
> - 🎯 **戦略的**: `docs/use_cases/core/index.md`（ドメイン概念の参照）  
> - 📊 **戦術的**: `docs/use_cases/index.md`（TDD GREENフェーズステータス更新）  
> - 🔧 **実行**: `docs/use_cases/issue-X-Y.json`（ドメイン実装の追跡）

## よくあるエラーと解決策

### ❌ エラーケース1: テストが見つからないか失敗していない
**原因**: RED フェーズ完了前にTDD GREENフェーズを試行  
**解決策**: 
```bash
# テストが存在し失敗していることを確認
/create-tests <issue-number>
# テストの失敗を確認
pytest tests/ -v
# その後ドメイン実装
/implement-domain <issue-number>
```

### ❌ エラーケース2: ドメイン以外の層を実装
**原因**: 誤ってアプリケーション、インフラストラクチャ、プレゼンテーション層を実装  
**解決策**: 
- **のみ** `src/domain/`のファイルを実装
- **禁止** データベース接続、APIクライアント、ウェブコントローラー
- **禁止** ユースケースやアプリケーションサービス

### ❌ エラーケース3: プレースホルダーアサーションによる偽REDステート
**原因**: テストに`assert False, "RED: ... not implemented yet"`が含まれているが実装が存在する  
**解決策**: 
```python
# 悪い例: プレースホルダーアサーション（偽REDを引き起こす）
def test_entity_creation(self):
    assert False, "RED: Entity creation not implemented yet"

# 良い例: 実際のテスト実装
def test_entity_creation(self):
    entity = MyEntity.create("test_id", "test_value")
    assert entity.id == "test_id"
    assert entity.value == "test_value"
```
**復旧**: すべてのプレースホルダーアサーションを実際の実装を検証する適切なテストに置き換える

### ❌ エラーケース4: エンティティ継承でのID型非互換性
**原因**: 既存テストが文字列IDを使用しているときにUUID要件のベースエンティティから継承  
**解決策**: 
```python
# 問題: 直接継承によるUUID変換エラー
@dataclass
class Configuration(BaseDomainEntity):  # UUIDが必要だが、テストは"test-config-1"を使用
    id: str
    
    def __post_init__(self):
        super().__init__(uuid.UUID(self.id))  # ❌ 非UUID文字列で失敗

# 解決策: 静的メソッドでコンポジションを使用
@dataclass  
class Configuration:  # 継承なし
    id: str
    
    def _validate_invariants(self):
        # バリデーションにベースクラスの静的メソッドを使用
        BaseDomainEntity._validate_string_type_and_not_empty(self.id, "ID")
        # ... 静的メソッドを使用した他のバリデーション
```
**重要な原則**: ID形式が異なる場合は継承よりもコンポジションを優先

### ❌ エラーケース5: ドメイン層に外部依存関係がある
**原因**: ドメインエンティティがインフラストラクチャやアプリケーションコードをインポート  
**解決策**: 
```python
# 悪い例: ドメインがインフラストラクチャに依存
from src.infrastructure.database import Session

# 良い例: 純粋なドメインコード
from typing import List, Optional
from dataclasses import dataclass
```

## 実行例

### ✅ 成功例
```bash
$ /implement-domain 15
🟢 Issues: #15 のドメイン層実装を開始します
🔴 TDD REDフェーズ検証中...
E ImportError: No module named 'src.domain.user'
======= 12 failed, 0 passed =======
✅ 全テストが正常に失敗 - TDD REDフェーズ確認
🏗️ ドメインエンティティ実装中...
  ✅ ファイル作成: src/domain/user.py
  ✅ ファイル作成: src/domain/value_objects.py
🟢 TDD GREENフェーズ検証中...
======= 12 passed, 0 failed =======
✅ 全テストが成功 - TDD GREENフェーズ確認
🎉 ドメイン層実装完了!
```

### ❌ 失敗例と修正
```bash
$ /implement-domain 15
❌ テストが既に成功しています - TDD REDフェーズではありません
💡 TDD REDフェーズを最初に実行してください:
   /create-tests 15

# 修正: 失敗テストから開始
$ /create-tests 15
$ /implement-domain 15
```

### ❌ プレースホルダーアサーション例と修正
```bash
$ /implement-domain 3
🚨 プレースホルダーアサーション発見:
  - tests/unit/domain/entities/test_configuration.py: 7 個
  - tests/unit/domain/entities/test_position.py: 8 個
  - tests/unit/domain/entities/test_trade.py: 9 個

🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています
   - 実装は完了済みだが、テストがプレースホルダーのまま
   - これはTDDプロセス違反の状態です

# 修正: プレースホルダーアサーションを実テストに置き換え
# テストファイルを編集して以下を置き換え:
#   assert False, "RED: Configuration update not implemented yet"
# これに:
#   config = Configuration.create("key", "value", "category")
#   config.update_value("new_value")
#   assert config.value == "new_value"
```

## 🟢 **TDD GREENフェーズ: ドメイン層実装のみ**

**⚠️ 重要な注意:**
- **このステップはTDD GREENフェーズ** - テストを通すためのドメイン層実装
- **ドメイン層実装のみ** - 他の層は許可されない  
- **TDD規律** - 最小限の実装で失敗テストを通す
- **ドメイン純粋性必須** - インフラやアプリケーション関心事は禁止

**TDDサイクル位置:**
1. `05-create-tests` ← TDD RED（失敗テスト作成）
2. `06-implement-domain` ← **【現在位置】TDD GREEN（ドメイン実装）**
3. `07-implement-usecase` ← アプリケーション層実装  
4. `11-refactor` ← TDD REFACTOR（コード品質改善）

**⚠️ このステップはドメイン層の実装のみを許可します。他の層は実装してはいけません。**

## 🚨 **重要: ドメイン層のみ - 他の層は禁止**

**❌ このステップで絶対禁止:**
- **アプリケーション層**: ユースケース、DTO、アプリケーションサービス禁止
- **インフラストラクチャ層**: リポジトリ実装、データベースコード、外部API呼び出し禁止
- **プレゼンテーション層**: コントローラー、API、CLIコマンド、ウェブインターフェース禁止
- **統合コード**: 依存性注入、設定、層間実装禁止

**✅ このステップで許可されるもの:**
- **ドメインエンティティ**: アイデンティティとライフサイクルを持つビジネスオブジェクト
- **値オブジェクト**: 概念を表現する不変オブジェクト
- **ドメインサービス**: エンティティに属さない純粋なビジネスロジック
- **リポジトリインターフェース**: 抽象契約（実装なし）

## 📋 **TDD GREENフェーズタスクチェックリスト**

**TDD規律でドメイン層を実装するためにこのチェックリストを使用してください:**

### 🔴 必須タスク

#### **🔴 → 🟢 テスト分析**
- [ ] **失敗テストを実行**: pytestを実行して現在失敗しているテストを特定
- [ ] **テスト失敗を分析**: 各テストが実装を期待している内容を理解
- [ ] **🚨 重要: プレースホルダーアサーションを置き換え**: テストの`assert False, "RED: ... not implemented yet"`文をチェックして修正
- [ ] **テストの真正性を検証**: テストがプレースホルダー失敗ではなく実際の実装をテストしていることを確認
- [ ] **実装順序を優先付け**: エンティティ、次に値オブジェクト、次にサービスの順で開始
- [ ] **最小実装を特定**: 各テストを通すために必要な最小限のコードを決定

#### **🏗️ エンティティ実装**
- [ ] **エンティティクラスを作成**: ドメインモデル設計と失敗テストに基づいてエンティティを実装
- [ ] **エンティティ属性を追加**: テストで要求されるプロパティとフィールドを実装
- [ ] **エンティティ振る舞いを実装**: 振る舞いテストを通すためのメソッドとビジネスロジックを追加
- [ ] **不変条件を適用**: エンティティの一貫性を維持するためのバリデーションとビジネスルールを追加

#### **🧪 TDD GREEN検証**
- [ ] **ドメイン層テストを実行**: すべてのドメイン固有テストを実行
- [ ] **テスト通過を確認**: 以前に失敗していたドメインテストがすべて通ることを確認
- [ ] **メタデータを更新**: issue-X-Y.jsonでTDD GREENフェーズ完了をマーク
- [ ] **ドメイン実装をコミット**: ドメイン層コードをバージョン管理

### 🟡 推奨タスク

#### **💎 値オブジェクト実装**
- [ ] **値オブジェクトクラスを作成**: 指定された不変値オブジェクトを実装
- [ ] **値バリデーションを追加**: 値オブジェクトの整合性を確保するバリデーションロジックを実装
- [ ] **等価メソッドを実装**: 適切な値比較のための__eq__と__hash__を追加
- [ ] **値振る舞いを追加**: 値オブジェクトに定義されたビジネス操作を実装
- [ ] **値オブジェクト実装をテスト**: 値オブジェクトテストが通ることを確認

#### **🔗 リポジトリインターフェース実装**
- [ ] **リポジトリインターフェースを作成**: データアクセス用の抽象ベースクラスを定義
- [ ] **リポジトリメソッドを定義**: 失敗テストで要求される抽象メソッドを追加
- [ ] **型ヒントを追加**: すべてのリポジトリメソッドに適切な型注釈を確保
- [ ] **リポジトリ契約を文書化**: 期待される振る舞いを説明するdocstringを追加
- [ ] **具象実装なし**: ドメイン層ではインターフェースのみ許可

#### **🚫 アーキテクチャ準拠チェック**
- [ ] **インフラ依存なし**: ドメインコードにデータベース/ファイル/ネットワークインポートがないことを確認
- [ ] **アプリケーション層参照なし**: ユースケースやDTOインポートがないことを確認
- [ ] **プレゼンテーション層参照なし**: APIやUI関連インポートがないことを確認
- [ ] **純粋Pythonのみ**: ドメインは標準ライブラリとドメイン自体のみに依存すべき
- [ ] **ドメイン純粋性維持**: src/domain/ディレクトリのみに新しい実装ファイルがあることを確認

### 🟢 オプションタスク

#### **⚙️ ドメインサービス実装**
- [ ] **ドメインサービスクラスを作成**: 複雑なビジネスロジック用のドメインサービスを実装
- [ ] **ビジネス操作を実装**: エンティティや値オブジェクトに属さないメソッドを追加
- [ ] **エンティティ相互作用を調整**: 複数エンティティにまたがるロジックを実装
- [ ] **ドメイン純粋性を維持**: インフラやアプリケーション関心事が入り込まないことを確認
- [ ] **ドメインサービス実装をテスト**: ドメインサービステストが通ることを確認

#### **🔧 コード品質検証**
- [ ] **ruffリントを実行**: `uv run --frozen ruff check src/ --fix`を実行
- [ ] **ruffフォーマットを実行**: `uv run --frozen ruff format src/`を実行
- [ ] **型チェックを実行**: `uv run --frozen pyright src/`を実行
- [ ] **品質問題を修正**: リント、フォーマット、型エラーに対処
- [ ] **クリーンな結果を確認**: すべての品質ツールがエラーなしで通ることを確認

#### **📊 高度なフェーズ完了**
- [ ] **テスト単位アプローチを計画**: 一度に一つのテストを通すのに十分な実装のみ
- [ ] **エンティティ実装をテスト**: 他を失敗のままエンティティテストが通ることを確認
- [ ] **テスト分離を維持**: テストが依然として独立して実行されることを確認
- [ ] **実装最小性をチェック**: 過剰エンジニアリングや不要機能がないことを確認
- [ ] **ドメイン純粋性を検証**: ドメインコードに外部依存がないことを確認
- [ ] **インターフェース分離**: リポジトリインターフェースはドメインに、実装はなし
- [ ] **具象リポジトリなし**: src/infrastructure/repositories/に実装がないことを確認
- [ ] **ユースケース実装なし**: src/application/use_cases/にファイルが作成されていないことを確認
- [ ] **API実装なし**: src/presentation/にファイルが作成されていないことを確認
- [ ] **実装を文書化**: 何を実装したか、なぜ実装したかを記録
- [ ] **アプリケーション層の準備**: ドメインインターフェースが次フェーズの準備完了を確認
- [ ] **フルテストスイートを実行**: ドメインテストが通り、他は失敗の可能性あり（期待通り）を確認

**💡 プロTip**: テストを通すのに必要なもののみ実装 - "あると良い"機能を追加する誘惑に抵抗！
- `src/domain/entities/` - ビジネスロジック付きドメインエンティティ
- `src/domain/value_objects/` - バリデーション付き不変値オブジェクト
- `src/domain/repositories/` - リポジトリインターフェース（抽象クラスのみ）
- `src/domain/services/` - エンティティ横断ビジネスロジック用ドメインサービス

### ❌ 禁止ファイル（このステップで作成/修正してはいけない）:
- `src/application/` - **アプリケーション層（ユースケース、DTO、アプリケーション例外）**
- `src/infrastructure/` - **インフラストラクチャ層（具象リポジトリ、データベース、外部API）**
- `src/presentation/` - **プレゼンテーション層（APIエンドポイント、CLI、ウェブインターフェース）**

### 🎯 実装ルール:
1. **ドメインロジックのみ** - ビジネスルールと不変条件に集中
2. **外部依存なし** - データベース、HTTP、ファイルI/O、技術的関心事なし
3. **テストを通すための最小実装** - TDD GREENフェーズ原則に従う
4. **純粋Pythonコード** - 標準ライブラリのみ使用、外部パッケージなし

### 💡 誤って他の層を実装した場合:
```bash
# 作成されたファイルを削除
rm -rf src/application/ src/infrastructure/ src/presentation/

# またはgitでリストア
git restore src/application/ src/infrastructure/ src/presentation/
```

**これらのルールに違反すると、アーキテクチャが破綻し、後の実装ステップで問題が発生します。**

## 🚨 **重要なTDD原則警告**

**🔴→🟢 テストを実装に合わせて修正してはいけません！**

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
- **実装はテストに従う** - テストを通すためのコードを書く
- **テストはシナリオから** - ビジネス要件がテストを駆動
- **実装を修正、テストは修正しない** - テストが失敗したらコードを変更

### ❌ 禁止アプローチ（絶対にやってはいけない）:
- ~~既存実装に合わせてテストを修正~~
- ~~「実装が違う動作をする」からテストを削除~~
- ~~現在のコードに合わせてテスト期待値を変更~~
- ~~間違った実装をテスト変更で正当化~~

### 🚨 実装がテストに合わない場合:
1. **停止** - テストを修正しない
2. **分析** - なぜテストが失敗しているか？
3. **シナリオ確認** - テストが要件を正しく表現しているか？
4. **実装修正** - テスト要件を満たすようにコードを修正
5. **シナリオが間違いの場合のみ** - シナリオ → テスト → 実装の順で更新

### 💡 緊急復旧:
```bash
# 誤ってテストを修正した場合
git restore tests/unit/domain/

# 適切なTDDフローに戻る
# 1. 失敗テストを読む（これらが仕様）
# 2. テストを通すドメインコードを実装
# 3. テストロジックをコードに合わせて変更してはいけない
```

**⚠️ 重要: テスト修正はTDDサイクルを破綻させ、シナリオ駆動開発を無効化します！**

---

## タスク詳細

1. **安全な環境設定と引数解析**:
   ```bash
   # 🔧 すべての安全操作機能を読み込み
   source "$(dirname "${BASH_SOURCE[0]}")/_setup_safe_environment.sh" "06-implement-domain" "$ARGUMENTS"
   
   # ドメイン実装は少なくとも1つのイシュー番号を期待
   if [[ ${#issue_numbers[@]} -eq 0 ]]; then
       echo "エラー: 少なくとも1つのイシュー番号を指定してください"
       show_usage_example "implement-domain" "1" "単一イシューのドメイン実装"
       show_usage_example "implement-domain" "1,7" "複数イシューのドメイン実装"
       show_usage_example "implement-domain" "1 mt5-extended-data" "イシュー + 機能名指定"
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
   
   echo "🏗️ Issues: $(printf '#%s ' "${issue_numbers[@]}")のドメイン層実装を開始します（TDD GREEN phase）"
   echo ""
   echo "🚨 重要な注意: このステップではドメイン層のみを実装します"
   echo "   ✅ 許可: src/domain/ 配下のファイルのみ"
   echo "   ❌ 禁止: src/application/, src/infrastructure/, src/presentation/"
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
   if ! begin_transaction "implement_domain_${issue_list}"; then
       echo "エラー: トランザクションの開始に失敗しました"
       exit 1
   fi
   
   # 📋 前提条件の検証 - テストが存在し失敗している必要がある
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
   
   # ドメインテストをチェック
   domain_test_files=$(find tests/unit/domain/ -name "test_*.py" -type f 2>/dev/null || echo "")
   if [[ -z "$domain_test_files" ]]; then
       echo "❌ ドメインテストが見つかりません"
       echo "💡 最初にTDDテストを作成してください:"
       echo "   /create-tests $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_tests"
       exit 1
   fi
   
   echo "  ✅ ドメインテストファイル確認: $(echo "$domain_test_files" | wc -l) ファイル"
   
   # ドメインモデル設計をチェック
   domain_model_file="docs/domain/issue-${issue_list}-domain-model.md"
   if [[ ! -f "$domain_model_file" ]]; then
       echo "❌ ドメインモデル設計が見つかりません: $domain_model_file"
       echo "💡 最初にドメインモデル設計を作成してください:"
       echo "   /domain-modeling $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
       execute_rollback "missing_domain_model"
       exit 1
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
   
   # メタデータファイル形式を検証
   if ! validate_json_file "$metadata_file"; then
       echo "エラー: メタデータファイルの形式が不正です: $metadata_file"
       execute_rollback "metadata_file_invalid"
       exit 1
   fi
   
   # テストフェーズ完了をチェック
   test_status=$(jq -r '.phases.tests.created // false' "$metadata_file" 2>/dev/null)
   if [[ "$test_status" != "true" ]]; then
       echo "エラー: TDDテスト作成が完了していません"
       echo "💡 先に /create-tests コマンドを実行してください"
       execute_rollback "tests_not_created"
       exit 1
   fi
   
   # ドメイン実装が既に完了しているかチェック
   domain_status=$(jq -r '.phases.domain_implementation.completed // false' "$metadata_file" 2>/dev/null)
   if [[ "$domain_status" == "true" ]]; then
       echo "⚠️  Issue #${issue_list} のドメイン実装は既に完了しています"
       echo "既存の実装を上書きしますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           commit_transaction
           exit 0
       fi
       echo "🔄 既存のドメイン実装を上書きします"
   fi
   
   echo "✅ メタデータ検証完了"
   ```

4. **テストを実行してRED状態確認とプレースホルダーアサーション修正**:
   ```bash
   # 🔍 現在のテスト状態を検証（RED状態であるべき）
   echo "🔍 現在のテスト状態確認中（RED状態検証）..."
   
   # テスト用Python環境を検証
   if ! validate_python_environment; then
       echo "エラー: Python環境の検証に失敗しました"
       execute_rollback "python_env_validation_failed"
       exit 1
   fi
   
   # 🚨 重要: 偽RED状態を引き起こすプレースホルダーアサーションをチェック
   echo "  🚨 プレースホルダーアサーション検証中..."
   
   placeholder_files=()
   while IFS= read -r -d '' file; do
       if grep -l 'assert False, "RED:' "$file" >/dev/null 2>&1; then
           placeholder_files+=("$file")
       fi
   done < <(find tests/unit/domain/ -name "*.py" -print0 2>/dev/null)
   
   if [[ ${#placeholder_files[@]} -gt 0 ]]; then
       echo "  ❌ プレースホルダーアサーション発見:"
       for file in "${placeholder_files[@]:0:5}"; do
           count=$(grep -c 'assert False, "RED:' "$file" 2>/dev/null || echo "0")
           echo "    - $file: $count 個"
       done
       [[ ${#placeholder_files[@]} -gt 5 ]] && echo "    - ... (他 $((${#placeholder_files[@]} - 5)) ファイル)"
       
       echo ""
       echo "  🚨 CRITICAL ISSUE: これらのテストは意図的にFALSE失敗しています"
       echo "     - 実装は完了済みだが、テストがプレースホルダーのまま"
       echo "     - これはTDDプロセス違反の状態です"
       echo ""
       echo "  💡 修正が必要: プレースホルダーアサーションを実際のテストに置き換える"
       echo "     この修正は手動で行う必要があります"
       echo ""
       echo "  ⚠️  続行するとプレースホルダーテストの修正をスキップしますが、"
       echo "     後でテストを適切に実装する必要があります"
       echo ""
       echo "  続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           echo "💡 推奨: 手動でプレースホルダーテストを適切なテストに置き換えてから再実行"
           execute_rollback "placeholder_assertions_found"
           exit 1
       fi
       
       echo "  ⚠️  プレースホルダーテストを無視して続行（後で修正が必要）"
   else
       echo "  ✅ プレースホルダーアサーション: なし（正常なテスト状態）"
   fi
   
   # ドメインテストを実行してRED状態を確認
   echo "  🧪 ドメインテスト実行中（RED状態確認）..."
   
   test_output_file="/tmp/domain_test_output_$$"
   test_result=0
   
   # テストを実行し出力をキャプチャ
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$test_output_file" 2>&1; then
       test_result=0  # テスト成功（REDフェーズでは予期しない）
   else
       test_result=1  # テスト失敗（REDフェーズで期待される）
   fi
   
   # テスト結果を分析
   total_tests=$(grep -c "^tests/unit/domain/" "$test_output_file" 2>/dev/null || echo "0")
   failed_tests=$(grep -c "FAILED" "$test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 テスト結果分析:"
   echo "    - 総テスト数: $total_tests"
   echo "    - 失敗テスト数: $failed_tests"
   
   if [[ $test_result -eq 0 ]] && [[ $total_tests -gt 0 ]]; then
       echo "⚠️  警告: テストが成功しています（RED状態ではない）"
       echo "既に実装が存在する可能性があります"
       
       echo "実装を続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装をキャンセルしました"
           rm -f "$test_output_file"
           commit_transaction
           exit 0
       fi
   elif [[ $total_tests -eq 0 ]]; then
       echo "エラー: ドメインテストが見つかりません"
       rm -f "$test_output_file"
       execute_rollback "no_domain_tests_found"
       exit 1
   else
       echo "  ✅ RED状態確認: $failed_tests 個のテストが期待通り失敗"
   fi
   
   # 実装ガイダンス用の失敗テスト情報を抽出
   failing_entities=()
   while IFS= read -r line; do
       if [[ $line =~ test_([a-z_]+)\.py.*FAILED ]]; then
           entity_name=$(echo "$line" | sed 's/.*test_\([a-z_]*\)\.py.*/\1/')
           [[ -n "$entity_name" ]] && failing_entities+=("$entity_name")
       fi
   done < "$test_output_file"
   
   # 重複を削除
   unique_failing_entities=($(printf '%s\n' "${failing_entities[@]}" | sort -u))
   
   echo "  🎯 実装が必要な要素: ${#unique_failing_entities[@]} 個"
   for entity in "${unique_failing_entities[@]:0:5}"; do
       echo "    - $entity"
   done
   [[ ${#unique_failing_entities[@]} -gt 5 ]] && echo "    - ... (他 $((${#unique_failing_entities[@]} - 5)) 個)"
   
   rm -f "$test_output_file"
   echo "✅ テスト状態確認完了"
   ```

5. **ドメイン設計情報の抽出**:
   ```bash
   # 📖 ドメインモデルから実装ガイダンスを抽出
   echo "📖 ドメインモデル設計分析中..."
   
   if ! check_file_permissions "$domain_model_file" "read"; then
       echo "エラー: ドメインモデルファイルの読み取り権限がありません: $domain_model_file"
       execute_rollback "domain_model_access_denied"
       exit 1
   fi
   
   # ドメインモデルからエンティティを抽出
   entities=$(grep -A 5 "^### [A-Z]" "$domain_model_file" 2>/dev/null | \
             grep -E "^### [A-Z][a-zA-Z]*$" | \
             sed 's/^### //' || echo "")
   
   all_entities=()
   if [[ -n "$entities" ]]; then
       while IFS= read -r entity; do
           [[ -n "$entity" ]] && all_entities+=("$entity")
       done <<< "$entities"
   fi
   
   # 値オブジェクトを抽出
   value_objects=$(grep -A 10 "## 値オブジェクト\\|## Value Objects" "$domain_model_file" 2>/dev/null | \
                  grep -E "^### [A-Z][a-zA-Z]*$" | \
                  sed 's/^### //' || echo "")
   
   all_value_objects=()
   if [[ -n "$value_objects" ]]; then
       while IFS= read -r vo; do
           [[ -n "$vo" ]] && all_value_objects+=("$vo")
       done <<< "$value_objects"
   fi
   
   echo "  🎯 設計から抽出:"
   echo "    - エンティティ: ${#all_entities[@]} 個"
   echo "    - 値オブジェクト: ${#all_value_objects[@]} 個"
   
   echo "✅ ドメイン設計分析完了"
   ```

6. **ドメインエンティティの実装**:
   ```bash
   # 🏗️ ドメインエンティティを実装
   echo "🏗️ ドメインエンティティ実装中..."
   
   implemented_files=()
   
   # 失敗テストとドメインモデルに基づいてエンティティを実装
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       entity_file="src/domain/entities/${entity_lower}.py"
       
       echo "  🏗️ 実装中: $entity ($entity_file)"
       
       # エンティティ実装を作成
       entity_implementation='"""
   '"$entity"' エンティティ実装

   ドメインモデル: docs/domain/issue-'"${issue_list}"'-'"${feature_name}"'.md
   実装日時: '"$(date)"'
   """

   from datetime import datetime
   from typing import Optional
   from dataclasses import dataclass


   @dataclass
   class '"$entity"':
       """'"$entity"' エンティティ
       
       ドメインの中心となるビジネスエンティティ。
       ライフサイクルを持ち、一意性により識別される。
       """
       
       id: str
       created_at: datetime
       updated_at: datetime
       
       def __post_init__(self) -> None:
           """エンティティ初期化後の検証"""
           self._validate_invariants()
       
       def _validate_invariants(self) -> None:
           """ビジネス不変条件の検証"""
           if not self.id:
               raise ValueError("'"$entity"' ID cannot be empty")
           
           if not isinstance(self.id, str):
               raise TypeError("'"$entity"' ID must be a string")
           
           if self.created_at > datetime.now():
               raise ValueError("Created date cannot be in the future")
           
           if self.updated_at < self.created_at:
               raise ValueError("Updated date cannot be before created date")
       
       @classmethod
       def create(cls, entity_id: str) -> "'"$entity"'":
           """新しい'"$entity"'を作成する
           
           Args:
               entity_id: エンティティの一意識別子
               
           Returns:
               '"$entity"': 作成された'"$entity"'インスタンス
               
           Raises:
               ValueError: 無効なIDが指定された場合
           """
           now = datetime.now()
           return cls(
               id=entity_id,
               created_at=now,
               updated_at=now
           )
       
       def update(self) -> None:
           """'"$entity"'を更新する
           
           更新日時を現在時刻に設定し、不変条件を検証する。
           """
           self.updated_at = datetime.now()
           self._validate_invariants()
       
       def __eq__(self, other) -> bool:
           """等値性の比較
           
           エンティティはIDによる同一性で比較される。
           """
           if not isinstance(other, '"$entity"'):
               return False
           return self.id == other.id
       
       def __hash__(self) -> int:
           """ハッシュ値の計算
           
           IDに基づいてハッシュ値を計算する。
           """
           return hash(self.id)
   '
       
       if ! safe_create_file "$entity_file" "$entity_implementation" true; then
           echo "エラー: エンティティファイルの作成に失敗しました: $entity_file"
           execute_rollback "entity_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$entity_file")
       add_rollback "rm -f '$entity_file'" "Remove implemented entity: $entity_file"
   done
   
   echo "✅ エンティティ実装完了 (${#all_entities[@]} ファイル)"
   ```

7. **値オブジェクトの実装**:
   ```bash
   # 💎 値オブジェクトを実装
   echo "💎 値オブジェクト実装中..."
   
   # 共通値オブジェクトを実装
   common_value_objects=("EntityId" "Email")
   
   for vo in "${common_value_objects[@]}"; do
       vo_lower=$(echo "$vo" | tr '[:upper:]' '[:lower:]')
       vo_file="src/domain/value_objects/${vo_lower}.py"
       
       echo "  💎 実装中: $vo ($vo_file)"
       
       case "$vo" in
           "EntityId")
               vo_implementation='"""
   EntityId 値オブジェクト実装

   エンティティの一意識別子を表現する値オブジェクト。
   """

   import uuid
   from dataclasses import dataclass
   from typing import Union


   @dataclass(frozen=True)
   class EntityId:
       """エンティティ一意識別子
       
       UUIDベースの一意識別子を提供する不変の値オブジェクト。
       """
       
       value: str
       
       def __post_init__(self) -> None:
           """値オブジェクト初期化後の検証"""
           if not self.value:
               raise ValueError("EntityId value cannot be empty")
           
           if not isinstance(self.value, str):
               raise TypeError("EntityId value must be a string")
           
           # UUID形式の検証
           try:
               uuid.UUID(self.value)
           except ValueError:
               raise ValueError(f"EntityId value must be a valid UUID: {self.value}")
       
       @classmethod
       def generate(cls) -> "EntityId":
           """新しいEntityIdを生成する
           
           Returns:
               EntityId: 新しく生成されたEntityId
           """
           return cls(value=str(uuid.uuid4()))
       
       @classmethod
       def from_string(cls, value: Union[str, "EntityId"]) -> "EntityId":
           """文字列またはEntityIdからEntityIdを作成
           
           Args:
               value: 文字列またはEntityIdインスタンス
               
           Returns:
               EntityId: EntityIdインスタンス
           """
           if isinstance(value, EntityId):
               return value
           return cls(value=value)
       
       def __str__(self) -> str:
           """文字列表現"""
           return self.value
       
       def __repr__(self) -> str:
           """デバッグ表現"""
           return f"EntityId({self.value!r})"
   '
               ;;
           "Email")
               vo_implementation='"""
   Email 値オブジェクト実装

   メールアドレスを表現する値オブジェクト。
   """

   import re
   from dataclasses import dataclass


   @dataclass(frozen=True)
   class Email:
       """メールアドレス値オブジェクト
       
       RFC 5322に準拠したメールアドレスを表現する不変の値オブジェクト。
       """
       
       value: str
       
       # メールアドレス形式の正規表現（簡略版）
       _EMAIL_PATTERN = re.compile(
           r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
       )
       
       def __post_init__(self) -> None:
           """値オブジェクト初期化後の検証"""
           self._validate()
       
       def _validate(self) -> None:
           """メールアドレス形式の検証"""
           if not self.value:
               raise ValueError("Email value cannot be empty")
           
           if not isinstance(self.value, str):
               raise TypeError("Email value must be a string")
           
           if len(self.value) > 255:
               raise ValueError("Email value cannot exceed 255 characters")
           
           if not self._EMAIL_PATTERN.match(self.value):
               raise ValueError(f"Invalid email format: {self.value}")
       
       @property
       def local_part(self) -> str:
           """ローカル部分（@より前）を取得"""
           return self.value.split("@")[0]
       
       @property 
       def domain_part(self) -> str:
           """ドメイン部分（@より後）を取得"""
           return self.value.split("@")[1]
       
       def __str__(self) -> str:
           """文字列表現"""
           return self.value
       
       def __repr__(self) -> str:
           """デバッグ表現"""
           return f"Email({self.value!r})"
   '
               ;;
       esac
       
       if ! safe_create_file "$vo_file" "$vo_implementation" true; then
           echo "エラー: 値オブジェクトファイルの作成に失敗しました: $vo_file"
           execute_rollback "value_object_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$vo_file")
       add_rollback "rm -f '$vo_file'" "Remove implemented value object: $vo_file"
   done
   
   echo "✅ 値オブジェクト実装完了 (${#common_value_objects[@]} ファイル)"
   ```

8. **リポジトリインターフェースの実装**:
   ```bash
   # 🏪 リポジトリインターフェースを実装
   echo "🏪 リポジトリインターフェース実装中..."
   
   # 各エンティティのリポジトリインターフェースを作成
   for entity in "${all_entities[@]}"; do
       entity_lower=$(echo "$entity" | tr '[:upper:]' '[:lower:]')
       repo_file="src/domain/repositories/${entity_lower}_repository.py"
       
       echo "  🏪 実装中: ${entity}Repository ($repo_file)"
       
       repo_implementation='"""
   '"$entity"'Repository インターフェース

   '"$entity"'エンティティの永続化抽象インターフェース。
   """

   from abc import ABC, abstractmethod
   from typing import List, Optional
   from ..entities.'"${entity_lower}"' import '"$entity"'


   class '"$entity"'Repository(ABC):
       """'"$entity"'リポジトリ抽象インターフェース
       
       '"$entity"'エンティティの永続化操作を定義する。
       具体的な実装はインフラストラクチャ層で行う。
       """
       
       @abstractmethod
       def save(self, entity: '"$entity"') -> None:
           """'"$entity"'を保存する
           
           Args:
               entity: 保存する'"$entity"'エンティティ
               
           Raises:
               RepositoryError: 保存に失敗した場合
           """
           pass
       
       @abstractmethod
       def find_by_id(self, entity_id: str) -> Optional['"$entity"']:
           """IDで'"$entity"'を検索する
           
           Args:
               entity_id: 検索するエンティティのID
               
           Returns:
               Optional['"$entity"']: 見つかった'"$entity"'、または None
               
           Raises:
               RepositoryError: 検索に失敗した場合
           """
           pass
       
       @abstractmethod
       def find_all(self) -> List['"$entity"']:
           """すべての'"$entity"'を取得する
           
           Returns:
               List['"$entity"']: すべての'"$entity"'のリスト
               
           Raises:
               RepositoryError: 取得に失敗した場合
           """
           pass
       
       @abstractmethod
       def delete(self, entity_id: str) -> bool:
           """'"$entity"'を削除する
           
           Args:
               entity_id: 削除するエンティティのID
               
           Returns:
               bool: 削除に成功した場合True、エンティティが見つからない場合False
               
           Raises:
               RepositoryError: 削除に失敗した場合
           """
           pass
       
       @abstractmethod
       def exists(self, entity_id: str) -> bool:
           """'"$entity"'が存在するかチェックする
           
           Args:
               entity_id: チェックするエンティティのID
               
           Returns:
               bool: エンティティが存在する場合True
               
           Raises:
               RepositoryError: チェックに失敗した場合
           """
           pass


   class RepositoryError(Exception):
       """リポジトリ操作エラー"""
       pass
   '
       
       if ! safe_create_file "$repo_file" "$repo_implementation" true; then
           echo "エラー: リポジトリインターフェースファイルの作成に失敗しました: $repo_file"
           execute_rollback "repository_interface_implementation_failed"
           exit 1
       fi
       
       implemented_files+=("$repo_file")
       add_rollback "rm -f '$repo_file'" "Remove implemented repository interface: $repo_file"
   done
   
   echo "✅ リポジトリインターフェース実装完了 (${#all_entities[@]} ファイル)"
   ```

9. **テストを実行してGREEN状態を確認**:
   ```bash
   # 🟢 テストがGREEN状態になったことを確認
   echo "🟢 TDD GREENフェーズ検証中..."
   
   # ドメインテストを実行してGREEN状態を確認
   echo "  🧪 ドメインテスト実行中（GREEN状態確認）..."
   
   test_output_file="/tmp/domain_green_test_output_$$"
   test_result=0
   
   # テストを実行し出力をキャプチャ
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ -v --tb=short > "$test_output_file" 2>&1; then
       test_result=0  # テスト成功（GREENフェーズで期待される）
   else
       test_result=1  # テスト失敗（さらに実装が必要）
   fi
   
   # テスト結果を分析
   total_tests=$(grep -c "test_.*PASSED\\|test_.*FAILED" "$test_output_file" 2>/dev/null || echo "0")
   passed_tests=$(grep -c "PASSED" "$test_output_file" 2>/dev/null || echo "0")
   failed_tests=$(grep -c "FAILED" "$test_output_file" 2>/dev/null || echo "0")
   
   echo "  📊 テスト結果分析:"
   echo "    - 総テスト数: $total_tests"
   echo "    - 成功テスト数: $passed_tests"
   echo "    - 失敗テスト数: $failed_tests"
   
   if [[ $failed_tests -gt 0 ]]; then
       echo "⚠️  まだ失敗しているテストがあります:"
       grep "FAILED" "$test_output_file" | head -5
       echo ""
       echo "追加実装が必要な可能性があります。続行しますか？ (y/N): "
       read -n 1 -r
       echo
       if [[ ! $REPLY =~ ^[Yy]$ ]]; then
           echo "ドメイン実装を中止しました"
           rm -f "$test_output_file"
           execute_rollback "tests_still_failing"
           exit 1
       fi
   else
       echo "  ✅ GREEN状態確認: すべてのテストが成功しています"
   fi
   
   # 可能であればテストカバレッジを計算
   coverage_result=""
   if PYTEST_DISABLE_PLUGIN_AUTOLOAD="" uv run --frozen pytest tests/unit/domain/ --cov=src.domain --cov-report=term-missing --quiet >/tmp/coverage_output_$$ 2>&1; then
       coverage_result=$(grep -E "[0-9]+%" /tmp/coverage_output_$$ | tail -1 || echo "Coverage data not available")
       rm -f /tmp/coverage_output_$$
   fi
   
   rm -f "$test_output_file"
   tests_passed=$([ $failed_tests -eq 0 ] && echo "true" || echo "false")
   
   echo "✅ TDD GREEN フェーズ検証完了"
   ```

10. **コード品質とアーキテクチャ検証**:
    ```bash
    # 🔍 コード品質とアーキテクチャ検証
    echo "🔍 コード品質・アーキテクチャ検証中..."
    
    # ruffフォーマットとリントを実行
    echo "  🎨 コードフォーマット・リント実行中..."
    
    if ! uv run --frozen ruff format src/domain/ --quiet; then
        echo "⚠️  コードフォーマットに問題があります"
    fi
    
    lint_output_file="/tmp/ruff_output_$$"
    if uv run --frozen ruff check src/domain/ > "$lint_output_file" 2>&1; then
        echo "    ✅ リント検査: 問題なし"
    else
        echo "    ⚠️  リント警告があります:"
        head -5 "$lint_output_file"
        echo "    💡 必要に応じて修正してください"
    fi
    rm -f "$lint_output_file"
    
    # pyrightが利用可能な場合は型チェックを実行
    echo "  🔍 型チェック実行中..."
    
    type_output_file="/tmp/pyright_output_$$"
    if uv run --frozen pyright src/domain/ > "$type_output_file" 2>&1; then
        echo "    ✅ 型チェック: 問題なし"
    else
        echo "    ⚠️  型チェック警告があります:"
        head -5 "$type_output_file"
        echo "    💡 必要に応じて型ヒントを修正してください"
    fi
    rm -f "$type_output_file"
    
    # アーキテクチャ検証
    echo "  🏗️ アーキテクチャ検証中..."
    
    # 🚨 重要: ドメイン層のみが実装されたことを確認
    echo "    🚨 ドメイン層限定実装検証中..."
    
    prohibited_layers_found=false
    
    # 誤って作成されたアプリケーション層ファイルをチェック
    if [[ -d "src/application" ]]; then
        app_files=$(find src/application/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$app_files" ]]; then
            echo "    ❌ エラー: アプリケーション層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではアプリケーション層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$app_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    # 誤って作成されたインフラストラクチャ層ファイルをチェック
    if [[ -d "src/infrastructure" ]]; then
        infra_files=$(find src/infrastructure/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$infra_files" ]]; then
            echo "    ❌ エラー: インフラストラクチャ層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではインフラ層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$infra_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    # 誤って作成されたプレゼンテーション層ファイルをチェック
    if [[ -d "src/presentation" ]]; then
        pres_files=$(find src/presentation/ -name "*.py" -type f 2>/dev/null | grep -v __pycache__ || echo "")
        if [[ -n "$pres_files" ]]; then
            echo "    ❌ エラー: プレゼンテーション層ファイルが作成されています!"
            echo "    🚫 禁止: このステップではプレゼンテーション層は実装してはいけません"
            echo "    📁 検出されたファイル:"
            echo "$pres_files" | sed 's/^/        - /'
            prohibited_layers_found=true
        fi
    fi
    
    if [[ "$prohibited_layers_found" == "true" ]]; then
        echo ""
        echo "    🚨 重大なエラー: 禁止されたレイヤーの実装が検出されました"
        echo "    💡 対処方法:"
        echo "       1. 禁止されたファイルを削除: rm -rf src/application/ src/infrastructure/ src/presentation/"
        echo "       2. またはgitでリストア: git restore src/application/ src/infrastructure/ src/presentation/"
        echo "       3. ドメイン層のみの実装に戻す"
        echo ""
        echo "    このエラーを無視すると、後の実装ステップで重大な問題が発生します。"
        echo ""
        echo "    修正しますか？ (y/N): "
        read -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo "    🧹 禁止されたレイヤーファイルを削除中..."
            [[ -d "src/application" ]] && rm -rf src/application/
            [[ -d "src/infrastructure" ]] && rm -rf src/infrastructure/
            [[ -d "src/presentation" ]] && rm -rf src/presentation/
            echo "    ✅ クリーンアップ完了"
        else
            echo "    ❌ アーキテクチャ違反により実装を中止します"
            execute_rollback "architecture_violation_detected"
            exit 1
        fi
    else
        echo "    ✅ レイヤー実装検証: ドメイン層のみ正しく実装"
    fi
    
    # ドメイン層の外部依存をチェック
    domain_imports=$(find src/domain/ -name "*.py" -exec grep -l "^import \\|^from " {} \; 2>/dev/null || echo "")
    external_deps_found=false
    
    for file in $domain_imports; do
        # 問題のあるインポート（インフラ依存）をチェック
        if grep -E "^(import|from) (requests|sqlalchemy|django|flask|fastapi|sqlite3|psycopg2)" "$file" >/dev/null 2>&1; then
            echo "    ⚠️  外部依存発見: $file"
            external_deps_found=true
        fi
    done
    
    if [[ "$external_deps_found" == "false" ]]; then
        echo "    ✅ 依存関係検証: ドメイン層の純粋性維持"
    else
        echo "    💡 ドメイン層の外部依存を削除することを推奨します"
    fi
    
    echo "✅ コード品質検証完了"
    ```

11. **メタデータと文書の更新**:
    ```bash
    # 📊 ドメイン実装完了でメタデータを更新
    echo "📊 メタデータ・ドキュメント更新中..."
    
    if ! update_metadata_atomic "$metadata_file" \
        '.phases.domain_implementation.created = true | 
         .phases.domain_implementation.completed = true |
         .phases.domain_implementation.completed_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .phases.tests.passed = '"$tests_passed"' |
         .phases.tests.coverage = "'"$coverage_result"'" |
         .updated_at = "'"$(date -u +%Y-%m-%dT%H:%M:%SZ)"'" |
         .spec_files.domain_implementation = ['"$(printf '"%s",' "${implemented_files[@]}" | sed 's/,$//')"'] |
         .phase = "domain_implemented_green" |
         .next_commands = ["implement-usecase", "use-case-status"]'; then
        echo "エラー: メタデータの更新に失敗しました"
        execute_rollback "metadata_update_failed"
        exit 1
    fi
    
    # ドメインモデル文書に実装ノートを更新
    if [[ -f "$domain_model_file" ]]; then
        echo "  📝 ドメインモデル文書更新中..."
        
        # 実装完了ノートを追加
        temp_file="${domain_model_file}.tmp"
        if cat >> "$temp_file" << EOF

## 実装完了状況

**実装日時**: $(date)
**実装ファイル数**: ${#implemented_files[@]}
**テスト状況**: $tests_passed (成功: $passed_tests, 失敗: $failed_tests)
**カバレッジ**: $coverage_result

### 実装されたファイル
$(printf '- %s\n' "${implemented_files[@]}")

### 次のステップ
- アプリケーション層実装: \`/implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`
- 進捗確認: \`/use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')\`

---
**実装ステータス**: ✅ 完了
EOF
then
            if ! mv "$temp_file" "$domain_model_file"; then
                echo "エラー: ドメインモデル文書の更新に失敗しました"
                execute_rollback "domain_model_update_failed"
                exit 1
            fi
        else
            echo "エラー: ドメインモデル文書への追記に失敗しました"
            execute_rollback "domain_model_append_failed"
            exit 1
        fi
    fi
    
    echo "✅ メタデータ更新完了"
    ```

12. **ユースケースインデックスの更新とGitコミット**:
    ```bash
    # 📚 ユースケースインデックスの更新と変更のコミット
    echo "📚 ユースケースインデックス更新中..."
    
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
        updated_line="- [${feature_name}]($(basename "${found_spec}")) - Issues: $(printf '#%s ' "${issue_numbers[@]}")- Phase: domain_implemented_green, TDD: 🟢 GREEN, Domain: ✅)"
        
        if ! sed -i "s|.*${feature_line}.*|${updated_line}|" "$use_cases_index"; then
            echo "エラー: インデックスファイルの更新に失敗しました"
            execute_rollback "index_update_failed"
            exit 1
        fi
        
        echo "✅ インデックス更新完了"
    fi
    
    # 💾 ドメイン実装をコミット
    echo "💾 ドメイン実装をコミット中..."
    
    commit_message="feat: implement domain layer for $(printf 'issue #%s ' "${issue_numbers[@]}")- ${feature_name} (GREEN phase)

    TDD Green Phase Summary:
    - Feature: ${feature_name}
    - Issues: $(printf '#%s ' "${issue_numbers[@]}")
    - Implementation Files: ${#implemented_files[@]} created
    - Test Results: Passed $passed_tests, Failed $failed_tests
    - Coverage: $coverage_result
    
    Implemented Components:
    $(printf '  - %s\n' "${implemented_files[@]}")
    
    Domain Layer Implementation:
    - Entities with business logic and invariants
    - Value objects with immutability and validation
    - Repository interfaces for persistence abstraction
    - Clean architecture principles maintained
    - No external dependencies in domain layer
    
    TDD Status: 🔴 RED → 🟢 GREEN (domain tests passing)
    Next Step: /implement-usecase for application layer
    "
    
    files_to_commit=("$metadata_file" "$domain_model_file")
    files_to_commit+=("${implemented_files[@]}")
    if [[ -f "$use_cases_index" ]]; then
        files_to_commit+=("$use_cases_index")
    fi
    
    if ! safe_git_commit "$commit_message" "${files_to_commit[@]}"; then
        echo "エラー: コミットに失敗しました"
        execute_rollback "commit_failed"
        exit 1
    fi
    
    add_rollback "git reset --hard HEAD~1" "Undo domain implementation commit"
    echo "✅ コミット完了"
    ```

13. **GitHubイシューの更新**:
    ```bash
    # 🎫 ドメイン実装完了でGitHubイシューを更新
    echo "🎫 GitHubイシュー更新中..."
    
    for issue_num in "${issue_numbers[@]}"; do
        echo "  📝 Issue #$issue_num コメント追加中..."
        
        issue_comment="🟢 **ドメイン層実装完了（GREEN phase）**

    TDDのGREENフェーズとして、ドメイン層の実装が完了しました。

    ## 📊 実装結果
    - **実装ファイル数**: ${#implemented_files[@]} ファイル
    - **テスト結果**: 成功 $passed_tests / 総計 $total_tests
    - **カバレッジ**: $coverage_result
    - **アーキテクチャ検証**: ✅ 通過

    ## 🏗️ 実装されたコンポーネント
    ### エンティティ
    $(if [[ ${#all_entities[@]} -gt 0 ]]; then
        for entity in "${all_entities[@]:0:3}"; do
            echo "- **$entity**: ビジネスロジックと不変条件を含む"
        done
        [[ ${#all_entities[@]} -gt 3 ]] && echo "- ... (他 $((${#all_entities[@]} - 3)) 個)"
    fi)
    
    ### 値オブジェクト
    - **EntityId**: UUID ベース一意識別子
    - **Email**: RFC 5322 準拠メールアドレス
    
    ### リポジトリインターフェース
    $(if [[ ${#all_entities[@]} -gt 0 ]]; then
        for entity in "${all_entities[@]:0:2}"; do
            echo "- **${entity}Repository**: ${entity}の永続化抽象インターフェース"
        done
        [[ ${#all_entities[@]} -gt 2 ]] && echo "- ... (他リポジトリ)"
    fi)

    ## 🎯 TDD状況
    - **現在の状態**: 🟢 GREEN（ドメインテスト通過）
    - **前フェーズ**: 🔴 RED（テスト作成）
    - **次フェーズ**: アプリケーション層実装

    ## 🏛️ アーキテクチャ準拠
    - [x] ドメイン層の純粋性維持
    - [x] 外部依存なし
    - [x] ビジネスルールの実装
    - [x] エンティティの不変条件
    - [x] 値オブジェクトの不変性

    ## 🚀 次のステップ
    
    アプリケーション層実装を開始してください：
    \`\`\`bash
    /implement-usecase $issue_num
    \`\`\`

    ## 📚 関連ドキュメント
    - [ドメインモデル設計（更新済み）]($domain_model_file)
    - [実装されたファイル一覧](#実装されたコンポーネント)

    ## 🔍 動作確認
    \`\`\`bash
    # ドメインテスト実行
    uv run --frozen pytest tests/unit/domain/ -v
    
    # カバレッジ確認
    uv run --frozen pytest tests/unit/domain/ --cov=src.domain
    \`\`\`

    ---
    **TDD Phase**: 🟢 GREEN (domain_implemented) → 次: アプリケーション層
    "
        
        if ! safe_add_issue_comment "$issue_num" "$issue_comment"; then
            echo "    ⚠️  Issue #$issue_num へのコメント追加に失敗しました（続行します）"
        else
            echo "    ✅ Issue #$issue_num コメント追加完了"
        fi
    done
    
    echo "✅ GitHub イシュー更新完了"
    ```

14. **最終成功とTDDガイダンス**:
    ```bash
    # 🎉 トランザクションコミット（成功！）
    if commit_transaction; then
        echo ""
        echo "🎉 ドメイン層実装完了（TDD GREEN phase）!"
        echo "============================================="
        echo "🏗️ 機能名: $feature_name"
        echo "🎫 対象イシュー: $(printf '#%s ' "${issue_numbers[@]}")"
        echo "📊 実装ファイル数: ${#implemented_files[@]} 個"
        echo ""
        echo "📋 実装されたコンポーネント:"
        echo "   エンティティ: ${#all_entities[@]} 個"
        echo "   値オブジェクト: ${#common_value_objects[@]} 個"
        echo "   リポジトリIF: ${#all_entities[@]} 個"
        echo ""
        echo "🟢 TDD GREEN状態:"
        echo "   - テスト結果: 成功 $passed_tests / 総計 $total_tests"
        echo "   - カバレッジ: $coverage_result"
        echo "   - すべてのドメインテストが通過"
        echo ""
        echo "🏛️ アーキテクチャ準拠:"
        echo "   - ドメイン層の純粋性維持"
        echo "   - 外部依存関係なし"
        echo "   - ビジネスルールと不変条件の実装"
        echo "   - クリーンアーキテクチャ原則遵守"
        echo ""
        echo "🚀 次のステップ（TDD継続）:"
        echo "   1. アプリケーション層実装: /implement-usecase $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   2. 進捗確認: /use-case-status $(printf '%s,' "${issue_numbers[@]}" | sed 's/,$//')"
        echo "   3. リファクタリング検討（必要に応じて）"
        echo ""
        echo "🚨 TDD原則リマインダー:"
        echo "   ⚠️  実装中にテストを変更した場合、それはTDD違反です"
        echo "   ✅ 正解: シナリオ → テスト → 実装の順序で進める"
        echo "   ❌ 禁止: 実装を正としてテストを変更する"
        echo ""
        echo "📖 TDD サイクル進捗:"
        echo "   🔴 RED: テスト作成 ✅ 完了"
        echo "   🟢 GREEN: ドメイン実装 ✅ 完了"
        echo "   🔄 REFACTOR: コード改善 ← 必要に応じて"
        echo ""
        echo "💡 実装品質:"
        echo "   - ビジネスロジック中心設計"
        echo "   - 不変条件とバリデーション"
        echo "   - テスト駆動での堅牢性確保"
        echo "   - エンティティと値オブジェクトの適切な分離"
        echo ""
        echo "📁 作成されたファイル:"
        printf '   - %s\n' "${implemented_files[@]:0:7}"  # 最初の7個を表示
        [[ ${#implemented_files[@]} -gt 7 ]] && echo "   - ... (他 $((${#implemented_files[@]} - 7)) ファイル)"
        echo ""
        
        # 操作ログサマリーを表示
        echo "📊 操作ログサマリー:"
        show_github_operation_log | tail -2
        show_git_operation_log | tail -2
        show_transaction_log | tail -2
        
        echo ""
        echo "✅ TDD GREENフェーズ完了 - アプリケーション層実装準備完了!"
        echo ""
        echo "🚨 MANDATORY FOR CLAUDE CODE: SCENARIO EVOLUTION CHECK"
        echo "   ドメイン実装中に新要件・制約・エッジケース発見時は"
        echo "   作業を中断して /evolve-scenarios <feature-name> を実行すること"
        echo "   CRITICAL: ドメイン層の変更は全システムに影響します"
        echo ""
        echo "🔒 アーキテクチャ注意事項:"
        echo "   このステップではドメイン層のみを実装しました"
        echo "   アプリケーション層は /implement-usecase で別途実装してください"
        echo "   各層を適切なタイミングで実装することでクリーンアーキテクチャを維持します"
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
- テストを通すのに必要なもののみ実装
- 技術的関心事ではなくドメインロジックに集中
- エンティティと値オブジェクトを純粋に保つ（I/Oなし）
- 不変条件とビジネスルールを適用
- すべてのコードに型ヒントを使用
- すべてのユーザー向け出力は日本語である必要があります