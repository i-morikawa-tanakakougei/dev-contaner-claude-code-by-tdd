スプリントフィードバックに基づいてシナリオを進化させます。

以下の手順に従います：

1. **引数の確認**：
   - `$ARGUMENTS`（機能名）が提供されていることを確認
   - 提供されていない場合は終了し、機能名を渡すようユーザーに促す

2. **フィードバック源の分析**：
   - `docs/sprints/`のスプリントレビューノートを確認
   - `docs/review/issue-*-review.md`のレビューレポートを確認
   - 最近のGitHubイシューコメントを確認
   - 以下から発見された新しい要件やエッジケースを特定：
     - スプリント振り返り
     - コードレビューフィードバック
     - テスト結果と実装中に発見されたエッジケース

3. **シナリオタイプの決定**：
   - **拡張**: 既存シナリオへの詳細追加
   - **エッジケース**: 特殊条件の処理
   - **エラーケース**: 新しいエラーハンドリング要求
   - **新機能**: 発見された全く新しい機能

4. **シナリオドキュメントの作成または更新**：
   - 既存機能の場合: `docs/use_cases/<feature>.md`を更新
   - 新しい側面の場合: `docs/use_cases/evolved/<feature>-<aspect>.md`を作成
   - 以下のテンプレートを使用（内容は日本語）：

```markdown
# 進化したユースケース: <Feature Name>

## 変更理由
- **発見時期**: Sprint <number>
- **フィードバック源**: <Sprint review/User feedback/Testing>
- **重要度**: <High/Medium/Low>

## 新規/更新シナリオ

### シナリオ<N>: <New Scenario Name>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>
- **追加理由**: <Why this scenario was added>

### シナリオ<N+1>: <Edge Case>
- **Given**: <Preconditions>
- **When**: <Action>
- **Then**: <Expected Result>
- **発見経緯**: <How this case was discovered>

## ドメインへの影響
- **新規概念**: <New domain concepts if any>
- **既存概念の変更**: <Changes to existing concepts>
- **ユビキタス言語の追加**:
  - <New term>: <Definition>

## 実装への影響
- **影響を受けるレイヤー**: <Domain/Application/Infrastructure/Presentation>
- **必要な変更**:
  - <Change 1>
  - <Change 2>
- **推定工数**: <Days>

## 関連するコアシナリオ
- [<Core scenario name>](../core/<filename>.md)
- 関係性: <How it relates>
```

5. **新しいシナリオのGitHubイシュー作成**：
   - シナリオ追加時に即座にイシューを作成
   - シナリオとチケットの一貫性を確保
   - コマンドの使用：
   ```bash
   gh issue create \
     --title "実装: <Scenario name>" \
     --body "## 概要\n<Description>\n\n## シナリオ\n- Given: <condition>\n- When: <action>\n- Then: <result>\n\n## 発見経緯\n<Discovery context>\n\n## 関連ドキュメント\n- [進化シナリオ](docs/use_cases/evolved/<filename>.md)" \
     --label "enhancement,evolved-scenario"
   ```

6. **シナリオインデックスの更新**：
   - 新しいシナリオで`docs/use_cases/index.md`を更新
   - トレーサビリティを維持（内容は日本語）：

```markdown
## 進化したシナリオ (Sprint <number>)
- [<Scenario name>](evolved/<filename>.md) - Issue #<number>
  - 追加理由: <Brief reason>
  - ステータス: <Pending/In Progress/Completed>
```

7. **一貫性の検証**：
   - 全体ビジョンとの整合性を確認
   - 既存シナリオとの競合がないことを確認
   - ユビキタス言語の一貫性を確認
   - 新しいシナリオのテスト可能性を確認

8. **スプリントドキュメントの更新**：
   - 新しいシナリオがどのスプリントに属するかを決定：
     - キャパシティが許可し、スプリント目標と整合する場合は現在のスプリント
     - 現在のスプリントが満杯またはシナリオの優先度が低い場合は次のスプリント
   - 適切なスプリントドキュメントを更新：
     
   a. **現在のスプリントの場合**：
      - `docs/sprints/sprint-<current>-backlog.md`に新しいイシューを追加
      - アクティブスプリント追跡に追加
   
   b. **将来のスプリントの場合**：
      - `docs/sprints/sprint-<next>-backlog.md`を作成/更新
      - "スプリント計画準備完了"としてマーク
   
   c. **進化レポートの作成**：
      - ファイル: `docs/sprints/sprint-<number>-evolution.md`

```markdown
# スプリント<number> シナリオ進化

## 追加されたシナリオ
1. <Scenario name> - Issue #<number>
   - 優先度: <Priority>
   - 実装タイミング: <This sprint/Next sprint>

## ビジョンへの影響
<Impact on overall vision if any>

## 学習事項
<What we learned that led to these additions>
```

9. **次のステップのガイド**：
   - 作成されたイシュー番号を表示
   - 次のコマンドを日本語で提案：
     - `/create-tests <issue-number>` - 新しいシナリオのテスト作成
     - `/sprint-planning <next-sprint>` - 新しいシナリオで次のスプリントを計画

重要な注意事項：
- イシューとシナリオドキュメントを常に一緒に作成
- フィードバックと変更間のトレーサビリティを維持
- 明確性のために進化したシナリオはコアから分離して保持
- コアシナリオを直接変更しない（根本的な変更でない限り）
- 既存実装への影響を考慮
- すべてのユーザー向け出力は日本語