GitHub issue の分析と実装計画を作成してください: $ARGUMENTS。

以下の手順に従ってください:

1.  `$ARGUMENTS` が提供されているかを確認する。`$ARGUMENTS` が指定されていない場合は、即座にプロセスを終了する。終了時は、ユーザーに issue 番号の引数を渡すよう促す。
2.  `gh issue view` を使用して issue の詳細を取得する
3.  issue に記載されている問題を理解する
4.  関連するファイルについてコードベースを検索する
5.  issue を修正するために必要な変更を計画する
6.  常に「<元の issue タイトル> [実装計画]」というタイトルで新しい issue を日本語で作成し、適切なラベル（例：「enhancement」、「bug」）を適用する
7.  適切なラベルが存在しない場合は、`gh label create` を使用してラベルを作成する
8.  `gh issue close $ARGUMENTS` を使用して元の issue をクローズする

すべての GitHub 関連タスクには GitHub CLI（`gh`）を使用することを忘れずに。