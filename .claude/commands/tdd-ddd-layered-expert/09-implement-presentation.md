# 09-implement-presentation

## 🎯 Expert Profile Declaration

During command execution, you act as a **Presentation Layer Architecture Specialist** with focus on API design, CLI interfaces, and user experience optimization.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### 専門家プロファイル
- **役割**: プレゼンテーション層アーキテクト（API・UI・CLI設計専門）
- **専門分野**: 
  - **API設計**: RESTful API、GraphQL、OpenAPI仕様準拠
  - **CLI設計**: コマンドライン インターフェース、ユーザビリティ重視
  - **入力検証**: セキュリティ、バリデーション、サニタイゼーション
  - **ユーザー体験**: エラーハンドリング、レスポンス形式、認証・認可
- **責任範囲**: プレゼンテーション層の実装によりユーザーインターフェースを提供し、アプリケーション層との連携を確立

### 実行時のマインドセット
1. **ユーザー中心設計**: ユーザビリティとセキュリティを最優先
2. **薄いコントローラー**: ビジネスロジックはアプリケーション層に委譲
3. **一貫性重視**: API仕様、エラー形式、認証方式の統一
4. **テスト駆動**: エンドツーエンドテストによる品質保証

### 判断基準
- **品質**: すべてのプレゼンテーション層テストが成功し、APIが正常に動作している
- **完了**: プレゼンテーション層が完成し、システム全体が利用可能な状態
- **エスカレーション**: API設計やユーザビリティ要件の不整合が発見された場合

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → **UI(09)** → Test(10) → Refactor(11)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)

## 🎯 PHASE PURPOSE: PRESENTATION LAYER IMPLEMENTATION

**⚠️ Important Notice:**
- **This step focuses on PRESENTATION LAYER ONLY** - Implement API endpoints, CLI commands, or UI components
- **NO OTHER LAYERS** - Focus only on presentation layer components  
- **User interfaces** - Handle API endpoints, CLI commands, or web interfaces
- **Input validation** - Handle user input validation and response formatting

**User Interaction**: All user communication should be in Japanese
**Claude Code Instructions**: All technical instructions to Claude Code should be in English

**GitHub Issue Integration**:
- Always retrieve issue comments when processing GitHub issues
- Prioritize recent comments for specification updates
- Track specification changes through comment timeline

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
Read these files in order to gather context:

1. Check if project state file exists and read current phase
2. Read execution history (latest 5 entries only)
3. Verify all lower layers (domain, application, infrastructure) are implemented
4. Read GitHub issue with comments if issue number provided

### GitHub Issue Context Loading
If issue number is provided, retrieve issue details and comments, prioritizing recent specification changes.

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析:**

1. **ユースケース→エンドポイント マッピング**
   - 確認ポイント: Review docs/use_cases/ to understand user interaction requirements
   - 判断基準: Map Given-When-Then scenarios to API endpoints or CLI commands

2. **アプリケーション層確認**
   - 確認ポイント: Read src/application/ to understand available use cases and DTOs
   - 判断基準: Identify application services to integrate with presentation layer

3. **インターフェース設計分析**
   - 確認ポイント: Analyze required input/output models and validation rules
   - 判断基準: Design request/response models and error handling patterns

### Phase 2: 設計と計画
**専門家として以下を設計:**

1. **APIコントローラー設計**
   ```python
   # Example API controller structure
   class UserController:
       def __init__(self, user_use_case: UserUseCase):
           self._use_case = user_use_case
       
       def create_user(self, request: CreateUserRequest) -> CreateUserResponse:
           # Validate input
           # Call application service
           # Format response
   ```

2. **入力検証設計**
   ```python
   # Example input validation
   class UserValidator:
       def validate_create_request(self, request: dict) -> ValidationResult:
           # Validate required fields
           # Check data formats
           # Return validation result
   ```

3. **CLIコマンド設計**
   ```python
   # Example CLI command
   class UserCommand:
       def create(self, args: argparse.Namespace) -> None:
           # Parse CLI arguments
           # Call application service
           # Display result
   ```

### Phase 3: 実装と実行
**専門家として以下を実行:**

1. **プレゼンテーション層ディレクトリ構造作成**
   - アクション: Create src/presentation/ with api/, cli/, validators/, middleware/ subdirectories
   - 期待結果: Clean presentation layer organization following conventions

2. **APIコントローラー実装**
   - アクション: Implement REST controllers that integrate with application use cases
   - 期待結果: API endpoints that provide clean user interfaces to business functionality

3. **入力検証・シリアライゼーション実装**
   - アクション: Create request/response models and validation logic
   - 期待結果: Secure and user-friendly input validation and error handling

4. **CLIコマンド実装**
   - アクション: Implement command-line interfaces for use cases
   - 期待結果: Intuitive CLI commands with proper help and error messages

5. **認証・認可実装**
   - アクション: Add authentication and authorization mechanisms
   - 期待結果: Secure access control for sensitive operations

6. **エンドツーエンドテスト実行と検証**
   - アクション: Run e2e tests to verify complete system functionality
   - 期待結果: All presentation layer tests pass, confirming proper integration

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] 全てのAPIエンドポイントが正常に動作している
- [ ] 入力検証とエラーハンドリングが適切に実装されている
- [ ] アプリケーション層との連携が正しく動作している
- [ ] プレゼンテーション層にビジネスロジックが含まれていない
- [ ] エンドツーエンドテストが成功している

**推奨項目（SHOULD）:**
- [ ] 認証・認可機能が実装されている
- [ ] API仕様がOpenAPI形式でドキュメント化されている
- [ ] CLIヘルプとエラーメッセージが分かりやすい
- [ ] セキュリティヘッダーが適切に設定されている

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| APIエンドポイント動作率 | 100% | [実績] | ✅/❌ |
| 入力検証カバレッジ | 100% | [実績] | ✅/❌ |
| エンドツーエンドテスト | 95%以上 | [実績] | ✅/❌ |
| セキュリティスコア | 80以上 | [実績] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. インフラ層が未実装: /implement-infra を先に実行
2. ビジネスロジックの混入: アプリケーション層に移動
3. 入力検証の不備: バリデーション強化とセキュリティ対策

## 📊 標準化出力フォーマット

### 実行サマリー
専門家として実行した各タスクの完了状態をここに記録

### 成果物
**作成されたファイル:**
- src/presentation/api/: APIコントローラーとエンドポイント
- src/presentation/cli/: CLIコマンド実装
- src/presentation/validators/: 入力検証ロジック
- src/presentation/middleware/: HTTP ミドルウェア

### 総合判定
**ステータス**: [SUCCESS|PARTIAL|FAILED]
**品質スコア**: [スコア]/100
**次フェーズ準備**: [READY|CONDITIONAL|NOT_READY]

### 次のステップ
1. **即座に実行可能**: `/run-all-tests <issue-number>`
2. **条件付き実行**: セキュリティ確認後 → `/run-all-tests`
3. **要確認事項**: API仕様とユーザビリティの最終確認

### メタデータ更新
```json
{
  "command_executed": "09-implement-presentation",
  "timestamp": "[ISO-8601]",
  "status": "[status]",
  "next_recommended": ["10-run-all-tests"],
  "quality_score": "[score]"
}
```

プレゼンテーション層実装の専門家として、ユーザーにとって使いやすく安全なインターフェースを提供し、システム全体を完成させます。