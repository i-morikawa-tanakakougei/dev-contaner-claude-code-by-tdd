GitHub issue を分析し更新してください: $ARGUMENTS。

以下の手順に従ってください:

1. **入力検証**: `$ARGUMENTS` が提供されているかを確認する。`$ARGUMENTS` が指定されていない場合は、即座にプロセスを終了し、ユーザーに issue 番号の引数を提供するよう促す。

2. **Issue 詳細の取得**: `gh issue view $ARGUMENTS` を使用して、指定した GitHub issue の詳細を取得する。

3. **問題の理解**: issue の説明を分析して、問題、要件、コンテキストを特定する。

4. **ドメインと機能分析**:

   - **イベントストーミング**技法を使用して、主要なユースケース、イベント、集約をマッピングし、issue に関連するドメインを特定する。
   - ドメインモデルとの整合性を確保するために、主要なユースケースとビジネスイベントを文書化する。
   - 機能を明確なドメイン固有の責任に分割する。

5. **レイヤードアーキテクチャ設計**:

   - 以下のレイヤーを持つレイヤードアーキテクチャを使用してソリューションを設計する:
     - **データレイヤー**: 各ドメインのデータモデル、リポジトリ、永続化ロジックを定義し、ドメイン固有のフォルダーでの分離を確保する（例：`src/domains/<domain>/data/`）。
     - **サービスレイヤー**: ビジネスロジックをドメイン固有のサービスにカプセル化し、ドメイン固有のフォルダーで整理する（例：`src/domains/<domain>/services/`）。
     - **コントローラーレイヤー**: 入出力、API エンドポイント、UI インタラクションを処理し、ドメイン固有のフォルダーで整理する（例：`src/domains/<domain>/controllers/`）。
   - 各レイヤーがモジュラーであり、大規模開発における拡張性と保守性をサポートするためにドメイン境界を尊重することを確保する。

6. **コードベース検索**: issue によって影響を受ける領域を特定するために、関連ファイル（例：既存のドメインモデル、サービス、コントローラー）についてコードベースを検索する。フォルダー構造 `src/domains/<domain>/*` を使用して検索をガイドする。

7. **変更計画**:

   - ドメインモデルとレイヤードアーキテクチャとの整合性を確保しながら、issue に対処する変更を提案する。
   - ドメインとレイヤーによって整理された新規または変更されたファイルを指定する（例：`src/domains/<domain>/data/<entity>.py`、`src/domains/<domain>/services/<service>.py`）。
   - 変更が関心の分離を維持し、拡張性を促進することを確保する。

8. **Issue 更新**: 既存の GitHub issue `$ARGUMENTS` を提案されたソリューションで更新し、以下を含める:
   - ドメインとユースケース分析の要約。
   - レイヤードアーキテクチャ設計の説明。
   - ファイルパスとその目的を含む計画された変更のリスト。
   - 更新を追加するには `gh issue comment $ARGUMENTS` を使用する。新しい issue は作成しない。

**追加ガイドライン**:

- 拡張性と明確性を確保するために、ドメイン駆動のフォルダー構造（例：`src/domains/<domain>/{data,services,controllers}`）でコードベースを整理する。
- 設計がドメイン駆動設計の原則に準拠し、大規模開発をサポートすることを検証する。
- すべての GitHub 関連操作には GitHub CLI（`gh`）を使用する。

**フォルダー構造の例**:

```
src/
    domains/
        user/
            data/
                UserRepository.py
                UserEntity.py
            services/
                UserService.py
            controllers/
                UserController.py
        order/
            data/
                OrderRepository.py
                OrderEntity.py
            services/
                OrderService.py
            controllers/
                OrderController.py
```