あなたの提案する「Given-When-Then」の概念を採用し、Markdown 形式で仕様を明確化し、それを基に TDD、DDD、レイヤードアーキテクチャで開発を進めるアプローチは、非常に現実的かつ効果的だと考えます。この方法は、BDD（ビヘイビア駆動開発）のフルスタックフレームワーク（例: `pytest-bdd`や`Cucumber`）の導入に伴うオーバーヘッドを軽減しつつ、BDD の強みである仕様の明確さと可読性を活かし、TDD、DDD、レイヤードアーキテクチャと組み合わせるのに適しています。以下に、このアプローチの評価、具体的な進め方、メリット、課題、そして私の意見を詳しく説明します。

---

### 1. **提案の評価と相性**

「Given-When-Then」を Markdown ドキュメントとして仕様を記述し、それを基に TDD、DDD、レイヤードアーキテクチャで開発を進めるアプローチは、以下のように各手法と相性が良いです：

- **DDD との相性**:
  - 「Given-When-Then」は、DDD のユビキタス言語やユースケースを自然言語に近い形で表現するため、ドメインの仕様を明確化し、ビジネスステークホルダーとの共通理解を促進します。
  - Markdown 形式のドキュメントは、ユースケースやエンティティの振る舞いを整理し、ドメイン設計の基盤として機能します。
- **TDD との相性**:
  - Markdown の「Given-When-Then」ドキュメントは、TDD のテストケースの設計指針となり、テストファーストのプロセスをスムーズにします。仕様をテストコードに変換する手順が明確になります。
  - 例: 「Given: カートが空、When: 商品を追加、Then: カートに商品が含まれる」を直接テストケースにマッピング。
- **レイヤードアーキテクチャとの相性**:
  - レイヤードアーキテクチャの各層（プレゼンテーション、アプリケーション、ドメイン、インフラストラクチャ）に対して、Markdown の仕様を基に層ごとのテストを記述可能。ユースケースがアプリケーション層の中心となり、ドメイン層やインフラストラクチャ層の実装を導きます。
- **BDD フレームワークを避ける利点**:
  - `pytest-bdd`や`Cucumber`は強力ですが、設定や学習コスト、テストのメンテナンス負担が課題。Markdown ベースの「Given-When-Then」は、軽量で柔軟性が高く、チームの技術スタックに依存しない。

このアプローチは、BDD のエッセンス（仕様の明確化、振る舞い駆動）を活かしつつ、ツールの複雑さを排除し、TDD のシンプルさと DDD の構造化された設計を最大限に活用できます。

---

### 2. **具体的な進め方**

以下は、提案のアプローチを実践するためのステップと具体例です。オンラインショップの「カートに商品を追加する」ユースケースを例にします。

#### (1) **Markdown で「Given-When-Then」形式の仕様を記述**

- **仕様ドキュメントの作成**:

  - 各ユースケースを Markdown ファイル（例: `cart.md`）に記述。
  - ユビキタス言語を使用して、ドメインの概念（カート、商品、数量など）を明確に。
  - 例:

    # ユースケース: カートに商品を追加する

    ## シナリオ: ユーザーがカートに商品を追加する

    - **Given**: カートが空である
    - **When**: ユーザーが商品 "Book" を数量 2 で追加する
    - **Then**: カートには商品 "Book" が数量 2 で含まれている

    ## シナリオ: 同じ商品を追加すると数量が更新される

    - **Given**: カートに商品 "Book" が数量 1 で含まれている
    - **When**: ユーザーが商品 "Book" を数量 2 で追加する
    - **Then**: カートには商品 "Book" が数量 3 で含まれている

    ## シナリオ: 在庫がない場合エラーを返す

    - **Given**: 商品 "Book" の在庫が 0 である
    - **When**: ユーザーが商品 "Book" を数量 1 で追加する
    - **Then**: 在庫不足エラーが返される

- **ドキュメントの管理**:
  - Markdown ファイルを`docs/`フォルダに整理（例: `docs/use_cases/cart.md`）。
  - バージョン管理（Git など）で変更を追跡し、仕様の進化を記録。

#### (2) **フォルダ構成**

- 前回の提案を踏襲し、テスト用フォルダを追加。BDD フレームワークを使わないため、通常の TDD テストフォルダに整理。
  ```
  project_root/
  ├── docs/                     # 仕様ドキュメント
  │   ├── use_cases/
  │   │   ├── cart.md
  │   │   └── order.md
  ├── domain/
  │   ├── entities/
  │   │   ├── cart.py
  │   │   └── product.py
  │   ├── value_objects/
  │   │   ├── quantity.py
  │   │   └── money.py
  │   ├── repositories/
  │   │   ├── cart_repository.py
  ├── application/
  │   ├── use_cases/
  │   │   ├── add_item_to_cart.py
  │   └── dtos/
  │       ├── cart_dto.py
  ├── infrastructure/
  │   ├── repositories/
  │   │   ├── sql_cart_repository.py
  │   │   └── mock_cart_repository.py
  ├── presentation/
  │   ├── api/
  │   │   └── cart_controller.py
  ├── tests/
  │   ├── unit/                # 単体テスト
  │   │   ├── test_cart.py
  │   │   └── test_add_item_to_cart.py
  │   ├── integration/         # 統合テスト
  │   │   └── test_sql_cart_repository.py
  │   └── e2e/                # E2Eテスト
  │       └── test_cart_api.py
  ```

#### (3) **TDD でテストを実装**

- **Markdown を基にテストを書く**:

  - `cart.md`の各シナリオを TDD のテストケースに変換。
  - Python の`pytest`を使用して、「Given-When-Then」の構造をコメントや関数名で反映。
  - 例:

    ```python
    import pytest
    from domain.entities.cart import Cart
    from domain.entities.product import Product
    from domain.value_objects.quantity import Quantity
    from application.use_cases.add_item_to_cart import AddItemToCartUseCase
    from infrastructure.repositories.mock_cart_repository import MockCartRepository

    def test_add_item_to_cart():
        # Given: カートが空である
        cart = Cart(id=1, items=[])
        repo = MockCartRepository()
        repo.save(cart)

        # When: ユーザーが商品 "Book" を数量2で追加する
        use_case = AddItemToCartUseCase(repo)
        product = Product(id=1, name="Book", price=1000)
        use_case.execute(cart_id=1, product_id=1, quantity=2)

        # Then: カートには商品 "Book" が数量2で含まれている
        cart = repo.get_cart(1)
        assert len(cart.items) == 1
        assert cart.items[0].product.name == "Book"
        assert cart.items[0].quantity.value == 2

    def test_add_same_item_updates_quantity():
        # Given: カートに商品 "Book" が数量1で含まれている
        cart = Cart(id=1, items=[CartItem(Product(id=1, name="Book", price=1000), Quantity(1))])
        repo = MockCartRepository()
        repo.save(cart)

        # When: ユーザーが商品 "Book" を数量2で追加する
        use_case = AddItemToCartUseCase(repo)
        use_case.execute(cart_id=1, product_id=1, quantity=2)

        # Then: カートには商品 "Book" が数量3で含まれている
        cart = repo.get_cart(1)
        assert len(cart.items) == 1
        assert cart.items[0].product.name == "Book"
        assert cart.items[0].quantity.value == 3
    ```

- **実装（グリーン）**:

  - テストをパスする最小限のコードを書く。例:

    ```python
    # domain/entities/cart.py
    class Cart:
        def __init__(self, id, items=None):
            self.id = id
            self.items = items or []

        def add_item(self, product, quantity):
            for item in self.items:
                if item.product.id == product.id:
                    item.quantity = Quantity(item.quantity.value + quantity.value)
                    return
            self.items.append(CartItem(product, quantity))

    class CartItem:
        def __init__(self, product, quantity):
            self.product = product
            self.quantity = quantity

    # application/use_cases/add_item_to_cart.py
    class AddItemToCartUseCase:
        def __init__(self, cart_repository):
            self.cart_repository = cart_repository

        def execute(self, cart_id, product_id, quantity):
            cart = self.cart_repository.get_cart(cart_id)
            product = Product(id=product_id, name="Book", price=1000)  # 仮実装
            cart.add_item(product, Quantity(quantity))
            self.cart_repository.save(cart)
    ```

- **リファクタリング**:
  - テストがパスすることを確認しながら、コードを整理（例: `Product`の取得をリポジトリ経由に変更）。
  - 新しいシナリオ（例: 在庫不足エラー）を追加し、仕様を拡張。

#### (4) **レイヤーごとのテスト**

- **ドメイン層**:
  - エンティティ（`Cart`, `Product`）や値オブジェクト（`Quantity`）のテストを「Given-When-Then」のコメントで構造化。
- **アプリケーション層**:
  - ユースケース（`AddItemToCartUseCase`）のテストを Markdown のシナリオに基づいて記述。
- **インフラストラクチャ層**:
  - リポジトリ実装（例: `SqlCartRepository`）のテストは、モック DB を使って通常の TDD で記述。
- **プレゼンテーション層**:
  - API エンドポイント（例: `/cart/add`）の E2E テストを、必要に応じて「Given-When-Then」形式で記述。

#### (5) **仕様の進化と同期**

- 仕様変更時、Markdown ファイルを更新し、対応するテストと実装を調整。
- 例: 在庫チェックのシナリオを追加する場合、`cart.md`に新しいシナリオを追加し、テストと実装を更新。

---

### 3. **メリット**

このアプローチのメリットは以下の通りです：

- **軽量で柔軟**:
  - `pytest-bdd`などの BDD フレームワークの設定やメンテナンスが不要。Markdown はシンプルで、どんなチームでも扱いやすい。
- **仕様の可読性**:
  - 「Given-When-Then」の Markdown は、非技術者（プロダクトオーナーやビジネスアナリスト）がレビューしやすい。ユビキタス言語として機能。
- **TDD とのスムーズな統合**:
  - Markdown のシナリオを直接テストケースに変換でき、TDD のレッド・グリーン・リファクターサイクルを効率的に回せる。
- **DDD との連携**:
  - ユースケースやエンティティの振る舞いを Markdown で整理し、ドメイン設計を明確化。仕様とコードのギャップを最小化。
- **レイヤードアーキテクチャのサポート**:
  - 各層の役割を Markdown で定義したユースケースに紐づけ、関心の分離を維持。
- **バージョン管理**:
  - Markdown ファイルは Git で管理しやすく、仕様の変更履歴を追跡可能。

---

### 4. **課題と注意点**

- **仕様とテストの同期**:
  - Markdown の仕様とテストコードが乖離しないよう、定期的なレビューが必要。ドキュメントの更新を忘れると、仕様が陳腐化するリスク。
- **非技術者とのコラボレーション**:
  - Markdown は読みやすいが、非技術者が積極的に編集に参加するには、トレーニングやガイドラインが必要。
- **テストの粒度**:
  - 「Given-When-Then」のシナリオが大きすぎると、テストが複雑になる。1 シナリオあたり 3 ～ 5 ステップに抑える。
- **自動化の欠如**:
  - `pytest-bdd`のようなツールを使わないため、仕様（Markdown）とテストコードの自動リンクがない。手動で対応するシナリオをテストに反映する必要。
- **オーバーヘッド**:
  - 小規模プロジェクトでは、Markdown での仕様記述が過剰になる場合がある。簡易的なユースケースには、直接テストコードで仕様を表現するのも有効。

---

### 5. **私の意見**

このアプローチは、**BDD のエッセンスを軽量に取り入れ、TDD、DDD、レイヤードアーキテクチャの強みを最大限に活かす優れた方法**だと考えます。特に以下の点で推奨します：

- **実用性とバランス**:
  - `pytest-bdd`や`Cucumber`の導入は、学習コストや設定の負担が大きい場合があります。Markdown ベースの「Given-When-Then」は、ツールに依存せず、チームのスキルセットに合わせて柔軟に適用可能。
  - 小～中規模プロジェクトや、BDD フレームワークに慣れていないチームに特に適しています。
- **仕様の明確化**:
  - Markdown の「Given-When-Then」は、ユビキタス言語を強化し、ビジネスステークホルダーとのコミュニケーションを円滑にします。仕様書がテストの基盤となり、コードとの整合性が保たれます。
- **TDD との親和性**:
  - テストコードに「Given-When-Then」をコメントや構造で反映することで、テストの意図が明確になり、保守性が向上します。
- **プロジェクト規模への適応**:
  - 大規模プロジェクトでは、Markdown を仕様の正式ドキュメントとして活用し、必要に応じて BDD フレームワークに移行するステップを検討。
  - 小規模プロジェクトでは、Markdown を簡略化（例: 主要ユースケースのみ記述）し、TDD をメインに。

**推奨事項**：

- **ドキュメントの標準化**: Markdown のテンプレートを用意し、ユースケースごとの記述形式を統一（例: シナリオ名、Given-When-Then、補足説明）。
- **レビュープロセス**: スプリントごとに Markdown ドキュメントをレビューし、仕様とテストの同期を確認。
- **テストの構造化**: テストコード内で「Given-When-Then」をコメントや関数名で明示し、読みやすさを確保。
- **段階的導入**: 最初は 1 ～ 2 のユースケースで試し、チームが慣れたら全ユースケースに展開。

**注意**：

- Markdown ドキュメントが単なる「書類」にならないよう、テストやコードと密接にリンクさせる運用ルールを定める。
- 仕様が頻繁に変更される場合、Markdown の更新とテストの修正を迅速に行うためのワークフローを確立。

---

### 6. **サンプルアーティファクト**

以下は、Markdown 仕様と対応するテストコードの例です。

# ユースケース: カートに商品を追加する

## シナリオ: ユーザーがカートに商品を追加する

- **Given**: カートが空である
- **When**: ユーザーが商品 "Book" を数量 2 で追加する
- **Then**: カートには商品 "Book" が数量 2 で含まれている

## シナリオ: 同じ商品を追加すると数量が更新される

- **Given**: カートに商品 "Book" が数量 1 で含まれている
- **When**: ユーザーが商品 "Book" を数量 2 で追加する
- **Then**: カートには商品 "Book" が数量 3 で含まれている

```python
import pytest
from domain.entities.cart import Cart
from domain.entities.product import Product
from domain.value_objects.quantity import Quantity
from application.use_cases.add_item_to_cart import AddItemToCartUseCase
from infrastructure.repositories.mock_cart_repository import MockCartRepository

def test_add_item_to_cart():
    # Given: カートが空である
    cart = Cart(id=1, items=[])
    repo = MockCartRepository()
    repo.save(cart)

    # When: ユーザーが商品 "Book" を数量2で追加する
    use_case = AddItemToCartUseCase(repo)
    product = Product(id=1, name="Book", price=1000)
    use_case.execute(cart_id=1, product_id=1, quantity=2)

    # Then: カートには商品 "Book" が数量2で含まれている
    cart = repo.get_cart(1)
    assert len(cart.items) == 1
    assert cart.items[0].product.name == "Book"
    assert cart.items[0].quantity.value == 2

def test_add_same_item_updates_quantity():
    # Given: カートに商品 "Book" が数量1で含まれている
    cart = Cart(id=1, items=[CartItem(Product(id=1, name="Book", price=1000), Quantity(1))])
    repo = MockCartRepository()
    repo.save(cart)

    # When: ユーザーが商品 "Book" を数量2で追加する
    use_case = AddItemToCartUseCase(repo)
    use_case.execute(cart_id=1, product_id=1, quantity=2)

    # Then: カートには商品 "Book" が数量3で含まれている
    cart = repo.get_cart(1)
    assert len(cart.items) == 1
    assert cart.items[0].product.name == "Book"
    assert cart.items[0].quantity.value == 3
```

---

### 7. **結論**

「Given-When-Then」を Markdown で仕様記述し、TDD、DDD、レイヤードアーキテクチャで開発を進めるアプローチは、軽量で柔軟、かつ効果的です。BDD フレームワークの複雑さを避けつつ、仕様の明確化、テストの構造化、ドメイン設計の整合性を確保できます。特に、中～大規模プロジェクトや、ビジネスステークホルダーとのコラボレーションが多い場合に適しています。小規模プロジェクトでは、Markdown の記述を簡略化し、クリティカルなユースケースに絞るのも有効です。

**私の意見**としては、この方法はチームのスキルセットやプロジェクトの規模に依存せず、広く適用可能で、仕様とコードの橋渡しを効率化します。運用ルール（例: ドキュメントとテストの同期）を明確にし、定期的なレビューを組み込むことで、長期的な保守性も確保できます。

もし、特定のユースケースの Markdown 例、テストコードの詳細、またはプロジェクト管理のワークフロー（例: Git でのドキュメント管理）についてさらに知りたい場合は、教えてください！また、使用する技術スタック（例: Python, Java）やチームの構成に応じた具体的なアドバイスも提供できます。

---

● TDD・DDD・レイヤードアーキテクチャに基づいた開発アプローチ用のカスタムコマンドを作成しました。

作成したカスタムコマンド

1. /init-project-structure - プロジェクト構造の初期化
2. /create-use-case <issue 番号> - Given-When-Then 仕様書作成
3. /domain-modeling <issue 番号> - ドメインモデル設計
4. /create-tests <issue 番号> - TDD テスト作成（RED phase）
5. /implement-domain <issue 番号> - ドメイン層実装（GREEN phase）
6. /implement-usecase <issue 番号> - アプリケーション層実装
7. /implement-infra <issue 番号> - インフラストラクチャ層実装
8. /implement-presentation <issue 番号> - プレゼンテーション層実装
9. /refactor <issue 番号> - リファクタリング（REFACTOR phase）
10. /run-all-tests <issue 番号> - 全テスト実行とレポート生成

CLAUDE.md への追記内容

開発ワークフローの手順を追記し、各コマンドの使用方法を説明しました。

使用方法

1. GitHub issue を作成
2. /create-use-case <issue 番号> で仕様を作成
3. 順番にコマンドを実行して開発を進める

各コマンドは英語で記述されていますが、ユーザーへの出力（仕様書、設計書、エラーメッセージなど）は日本語で表示されます。
