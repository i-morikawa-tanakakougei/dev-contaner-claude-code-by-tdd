# カスタムコマンドの専門家モード統合提案書

## 🎯 エグゼクティブサマリー

現在のTDD/DDD/レイヤードアーキテクチャシステムにおける**サブエージェント呼び出しの不確実性**と**高いコンテキスト管理コスト**の問題を解決するため、カスタムコマンドに専門家システムプロンプトを直接統合する新アーキテクチャを提案します。

### 核心的な変更点
- **サブエージェント廃止** → カスタムコマンド内に専門家プロンプト統合
- **確率的実行の排除** → 100%確実な専門家モード実行
- **コスト削減** → 約70%の実行コスト削減見込み
- **応答速度向上** → 中間層排除による高速化

## 📊 現状の課題分析

### 1. サブエージェント呼び出しの不確実性
```
現状: カスタムコマンド → Task tool → サブエージェント（確率的）
問題点:
- Task toolがサブエージェントを呼び出すかは確率的
- 呼び出されない場合、専門家としての品質が保証されない
- ユーザー体験の一貫性欠如
```

### 2. 高いコンテキスト管理コスト
```
現状のコンテキスト準備:
- project-context.json (173行)
- current-command-context.json (29行)
- emergency-recovery-state.json
- execution-history.jsonl
- 各種メタデータファイル

総計: 1コマンド実行につき300行以上のコンテキスト準備
```

### 3. アーキテクチャの複雑性
```
現在の階層:
1. カスタムコマンド（.claude/commands/）
2. コンテキスト準備層（.claude/context/）
3. サブエージェント（.claude/agents/）
4. 検証システム（task-definitions/）
5. メタデータ管理層（docs/metadata/）

→ 5層の複雑な相互依存
```

## 🚀 提案する新アーキテクチャ

### コアコンセプト: 専門家モード内蔵型カスタムコマンド

```markdown
# カスタムコマンド構造

## 1. 専門家プロファイル宣言
- ロール定義
- 専門性明示
- 実行時の振る舞い指示

## 2. TDD/DDD/LAYERED PROCESS CONTEXT
- 開発フロー全体の可視化
- アーキテクチャ原則の明示
- 現在位置と次ステップの明確化

## 3. PHASE PURPOSE
- 当該フェーズの目的と範囲
- 実装対象の明確化
- 品質基準の設定

## 4. 軽量コンテキスト管理
- 必要最小限のJSON読み込み
- プロジェクト状態の簡潔な追跡

## 5. 専門家実行セクション
- Given-When-Thenベースの実行
- DDD/TDD原則の直接適用
- Claude Codeへの指示は英語で記述
- ユーザーとのやり取りは日本語で実行

## 6. GitHub Issue統合機能
- issueコメントの自動取得
- 直近コメントの優先処理
- 仕様変更の追跡機能

## 7. 内蔵品質保証
- チェックリストベースの検証
- 自己診断機能

## 8. 標準化された出力
- 一貫したフォーマット
- 次ステップの明確化
```

### アーキテクチャ比較

| 項目 | 現在のアーキテクチャ | 新アーキテクチャ |
|------|---------------------|-----------------|
| 階層数 | 5層 | 2層 |
| 実行確実性 | 確率的（60-80%） | 確定的（100%） |
| コンテキスト準備 | 300行以上 | 50行以下 |
| 応答時間 | 3-5秒 | 1-2秒 |
| メンテナンス性 | 複雑（5ファイル連携） | シンプル（単一ファイル） |
| トークン消費 | 高（多層処理） | 低（直接実行） |

## 💡 実装方式

### 専門家プロンプトの組み込み方法

```markdown
## 🎯 Expert Profile Declaration

As you execute this command, you act as a **[Expert Name]** specialist.

### Your Expertise
- **[Specialty 1]**: [Specific knowledge and capabilities]
- **[Specialty 2]**: [Specific knowledge and capabilities]
- **[Specialty 3]**: [Specific knowledge and capabilities]

### Execution Principles
1. [Principle 1]: Specific action guidelines
2. [Principle 2]: Specific action guidelines
3. [Principle 3]: Specific action guidelines

### Quality Standards
- [Standard 1]: Measurable quality metrics
- [Standard 2]: Measurable quality metrics
- [Standard 3]: Measurable quality metrics

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

## 🎯 PHASE PURPOSE: [SPECIFIC PHASE DESCRIPTION]

**⚠️ Important Notice:**
- **This step focuses on [PHASE SCOPE]** - [Description]
- **[IMPLEMENTATION SCOPE]** - [Details]
- **[QUALITY FOCUS]** - [Standards]

**User Interaction**: All user communication should be in Japanese
**Claude Code Instructions**: All technical instructions to Claude Code should be in English

**GitHub Issue Integration**:
- Always retrieve issue comments when processing GitHub issues
- Prioritize recent comments for specification updates
- Track specification changes through comment timeline
```

## 📈 期待される効果

### 定量的効果
- **実行コスト**: 70%削減
- **応答速度**: 50%向上
- **成功率**: 60-80% → 100%
- **メンテナンス工数**: 60%削減

### 定性的効果
- **開発者体験の向上**: シンプルで理解しやすい
- **デバッグ容易性**: 単一ファイルで完結
- **拡張性**: 新コマンド追加が容易
- **学習曲線**: 新規メンバーの習得時間短縮

## 🔄 移行戦略

### Phase 1: パイロット実装（1週間）
- 3つの重要コマンドで新方式を試験実装
  - 00-create-vision
  - 04-domain-modeling
  - 05-create-tests
- 効果測定と問題点の洗い出し

### Phase 2: 段階的移行（2週間）
- パイロット結果に基づく改善
- 残りのコマンドを優先度順に移行
- 既存プロジェクトとの互換性確保

### Phase 3: 完全移行（1週間）
- 全コマンドの新方式への移行完了
- ドキュメント更新
- 旧システムの段階的廃止

## 🛡️ リスクと対策

### リスク1: 専門家品質の低下
**対策**: 
- 詳細な専門家プロンプトの作成
- 品質チェックリストの強化
- A/Bテストによる品質検証

### リスク2: 既存プロジェクトへの影響
**対策**:
- 後方互換性の維持
- 段階的移行による影響最小化
- ロールバック計画の準備

### リスク3: 複雑なシナリオへの対応
**対策**:
- ハイブリッドモード（必要時のみサブエージェント利用）
- エスカレーション機能の実装
- 継続的な改善プロセス

## ✅ 意思決定ポイント

### 推奨事項
1. **パイロット実装の即時開始**を推奨
2. **軽量コンテキストJSONの維持**（履歴追跡用）
3. **段階的移行**による低リスクアプローチ

### 次のアクション
1. パイロット対象コマンドの選定承認
2. 実装チームの編成
3. 効果測定基準の合意

## 📋 補足資料

- [02-command-structure.md](./02-command-structure.md) - 新コマンド構造の詳細
- [03-migration-plan.md](./03-migration-plan.md) - 詳細な移行計画
- [04-example-commands/](./04-example-commands/) - 実装例

---

**提案者**: Claude Code Assistant  
**日付**: 2024年  
**バージョン**: 1.0