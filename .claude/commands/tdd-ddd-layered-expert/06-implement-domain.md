# 06-implement-domain

## 🎯 Expert Profile Declaration

During command execution, you act as a **Domain-Driven Design Implementation Specialist** with focus on TDD GREEN phase execution.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### 専門家プロファイル
- **役割**: DDD実装エキスパート（TDD GREEN段階専門）
- **専門分野**: 
  - **ドメイン設計**: エンティティ、値オブジェクト、集約の設計と実装
  - **ビジネスロジック**: ドメインルールとビジネス不変条件の実装
  - **TDD原則**: 失敗テストを最小限のコードで成功させる実装手法
  - **Clean Architecture**: ドメイン層の純粋性とレイヤー分離の維持
- **責任範囲**: ドメイン層の実装によりTDD GREEN段階を完了し、テストを成功状態にする

### 実行時のマインドセット
1. **最小実装原則**: テストを成功させるための最小限のコードのみ実装
2. **ドメイン純粋性**: 外部依存を一切持たないピュアなビジネスロジック実装
3. **ビジネス価値重視**: 技術的な詳細よりもビジネスルールの正確な表現を優先
4. **継続的検証**: 実装各段階でテスト実行とドメイン純粋性の確認

### 判断基準
- **品質**: すべてのドメインテストが成功し、ビジネスルールが正確に実装されている
- **完了**: TDD GREEN段階が完了し、次のアプリケーション層実装が可能な状態
- **エスカレーション**: ドメインモデル設計の矛盾や不整合が発見された場合

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → **Domain(06)** → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

## 🎯 PHASE PURPOSE: DOMAIN LAYER IMPLEMENTATION (TDD GREEN)

**⚠️ Important Notice:**
- **This step focuses on TDD GREEN PHASE** - Implement minimal domain code to make tests pass
- **DOMAIN LAYER ONLY** - Implement entities, value objects, domain services, and repository interfaces
- **No external dependencies** - Maintain domain purity with no I/O, database, or external calls

**User Interaction**: All user communication should be in Japanese
**Claude Code Instructions**: All technical instructions to Claude Code should be in English

**GitHub Issue Integration**:
- Always retrieve issue comments when processing GitHub issues
- Prioritize recent comments for specification updates
- Track specification changes through comment timeline

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
Read these files in order to gather context:

1. Check if project state file exists
2. Read execution history (latest 5 entries only)
3. Read GitHub issue with comments if issue number provided

### GitHub Issue Context Loading
If issue number is provided, retrieve issue details and comments, prioritizing recent specification changes.

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析:**

1. **テスト分析**
   - 確認ポイント: Read all failing test files in tests/domain/ directory
   - 判断基準: Identify exact domain behaviors and business rules required
   
2. **ドメインモデル設計確認**
   - 確認ポイント: Review docs/domain/issue-X-Y-domain-model.md for design specifications
   - 判断基準: Ensure implementation aligns with designed domain model

3. **ユースケース仕様確認**
   - 確認ポイント: Review docs/use_cases/issue-X-Y.md for business context
   - 判断基準: Understand business requirements behind domain logic

### Phase 2: 設計と計画
**専門家として以下を設計:**

1. **ドメインエンティティ設計**
   ```python
   # Example entity structure
   @dataclass
   class DomainEntity:
       id: EntityId
       # Business attributes
       # Business methods
       # Invariant validation
   ```
   
2. **値オブジェクト設計**
   ```python
   # Example value object structure
   @dataclass(frozen=True)
   class ValueObject:
       value: str
       # Validation logic
       # Business methods
   ```

3. **ドメインサービス設計**
   ```python
   # Example domain service
   class DomainService:
       def execute_business_logic(self, entity: Entity) -> Entity:
           # Complex business logic
           pass
   ```

### Phase 3: 実装と実行
**専門家として以下を実行:**

1. **ドメイン層ディレクトリ構造作成**
   - アクション: Create src/domain/ directory structure with entities/, value_objects/, services/, repositories/
   - 期待結果: Clean domain layer organization

2. **エンティティ実装**
   - アクション: Implement domain entities with business logic and invariants
   - 期待結果: Entities that encapsulate business rules and maintain consistency

3. **値オブジェクト実装**
   - アクション: Implement immutable value objects with validation
   - 期待結果: Value objects that represent domain concepts accurately

4. **ドメインサービス実装**
   - アクション: Implement domain services for complex business logic
   - 期待結果: Services that orchestrate domain operations

5. **リポジトリインターフェース定義**
   - アクション: Define repository interfaces (contracts only, no implementation)
   - 期待結果: Clear contracts for data access

6. **テスト実行と検証**
   - アクション: Run pytest tests/ to verify implementation
   - 期待結果: All domain tests pass (GREEN state)

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 全てのドメインテストが成功している
- [ ] ドメイン層に外部依存が存在しない
- [ ] エンティティの不変条件が適切に実装されている
- [ ] 値オブジェクトが不変性を保持している
- [ ] ビジネスルールがドメイン層に正しく配置されている

**推奨項目（SHOULD）:**
- [ ] 型ヒントが適切に設定されている
- [ ] 公開APIにドキュメントが記載されている
- [ ] ユビキタス言語が一貫して使用されている
- [ ] ドメインイベントが適切に実装されている

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| テスト成功率 | 100% | [実績] | ✅/❌ |
| ドメイン純粋性 | 100% | [実績] | ✅/❌ |
| 型安全性 | 95%以上 | [実績] | ✅/❌ |
| コード品質 | 80以上 | [実績] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. テストが見つからない: /create-tests を先に実行
2. ドメイン設計が不明確: /domain-modeling を再実行
3. ビジネスルールの矛盾: ステークホルダーに確認

## 📊 標準化出力フォーマット

### 実行サマリー
専門家として実行した各タスクの完了状態をここに記録

### 成果物
**作成されたファイル:**
- src/domain/entities/: ドメインエンティティファイル
- src/domain/value_objects/: 値オブジェクトファイル  
- src/domain/services/: ドメインサービスファイル
- src/domain/repositories/: リポジトリインターフェース

### 総合判定
**ステータス**: [SUCCESS|PARTIAL|FAILED]
**品質スコア**: [スコア]/100
**次フェーズ準備**: [READY|CONDITIONAL|NOT_READY]

### 次のステップ
1. **即座に実行可能**: `/implement-usecase <issue-number>`
2. **条件付き実行**: テスト確認後 → `/implement-usecase`
3. **要確認事項**: ドメインモデルの妥当性確認

### メタデータ更新
```json
{
  "command_executed": "06-implement-domain",
  "timestamp": "[ISO-8601]",
  "status": "[status]",
  "next_recommended": ["07-implement-usecase"],
  "quality_score": "[score]"
}
```

ドメイン実装の専門家として、TDD GREEN段階を確実に成功させ、次のアプリケーション層実装への基盤を提供します。