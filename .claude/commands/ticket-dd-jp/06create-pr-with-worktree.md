メインブランチと比較したアクティブな Git worktree の現在の変更に基づいてプルリクエストを作成してください。

クローズする issue: $ARGUMENTS （カンマ区切りの issue 番号）

以下の手順に従ってください:

1.  **引数の存在確認**

    - `$ARGUMENTS` が提供されているかを確認する。
    - `$ARGUMENTS` が指定されていない場合は、即座にプロセスを終了する。
    - 終了時は、ユーザーに issue 番号の引数を渡すよう促す。

2.  **現在の変更の確認**

    - `git status` を使用して現在の worktree のステータスを確認する
    - `git diff origin/main` を使用して現在の worktree のブランチと `main` ブランチを比較する
    - PR に含めるステージまたは未ステージの変更があることを確認する
    - 変更が見つからない場合は、エラーメッセージと共に終了する

3.  **ブランチの準備**

    - `git rev-parse --abbrev-ref HEAD` を使用して worktree の現在のブランチを特定する
    - `git add .` ですべての変更をステージする
    - 変更を要約するメッセージでコミットする（例：「issues #$ARGUMENTS の変更を実装」）
    - `git push origin <現在のブランチ>` を使用してブランチをリモートリポジトリにプッシュする

4.  **プルリクエストの作成**

    - `gh pr create` を使用してプルリクエストを作成し、以下を含める:
      - 変更を要約するタイトル（例：「issues #$ARGUMENTS の修正を実装」）
      - 変更を要約する日本語の説明
      - $ARGUMENTS の各 issue に対して "Closes #<issue_number>" を含める
    - 現在のブランチをソース、`main` をターゲットブランチとして使用する

5.  **PR 説明の形式**
    - 変更を要約して日本語で説明を書く
    - $ARGUMENTS の各 issue に対して "Closes #<issue_number>" を含める
    - 例: $ARGUMENTS が "123,456" の場合、説明に "Closes #123" と "Closes #456" を含める

注意:

- $ARGUMENTS をカンマ区切りの issue 番号として解析する
- PR がマージされたときに issue を自動的にクローズするため "Closes #<number>" 形式を使用する
- 現在の worktree のブランチと `main` ブランチの比較に基づいて PR を作成する
- `gh` CLI が設定され認証されていることを確認する