Initialize project structure for TDD/DDD/Layered Architecture development.

Follow these steps:

1. **Create Directory Structure**:
   Create the following project structure:
   ```
   project_root/
   ├── domain/
   │   ├── entities/
   │   ├── value_objects/
   │   ├── services/
   │   ├── repositories/
   │   └── events/
   ├── application/
   │   ├── use_cases/
   │   ├── dtos/
   │   └── exceptions/
   ├── infrastructure/
   │   ├── repositories/
   │   ├── persistence/
   │   │   ├── models/
   │   │   └── mappers/
   │   ├── external/
   │   └── config/
   ├── presentation/
   │   ├── api/
   │   │   ├── controllers/
   │   │   ├── validators/
   │   │   └── serializers/
   │   ├── cli/
   │   └── web/
   ├── tests/
   │   ├── unit/
   │   │   ├── domain/
   │   │   │   ├── entities/
   │   │   │   └── value_objects/
   │   │   └── application/
   │   │       └── use_cases/
   │   ├── integration/
   │   │   └── repositories/
   │   └── e2e/
   │       └── api/
   └── docs/
       ├── use_cases/
       ├── domain/
       ├── application/
       └── test_plan/
   ```

2. **Create __init__.py Files**:
   - Add `__init__.py` to all Python package directories
   - This ensures proper module imports

3. **Create README Files**:
   - Add README.md to each layer explaining its purpose
   - Use JAPANESE for documentation:
   
   Example for domain/README.md:
   ```markdown
   # ドメイン層
   
   ビジネスロジックとビジネスルールを含む層です。
   
   ## ディレクトリ構成
   - entities/: エンティティ（識別子を持つオブジェクト）
   - value_objects/: 値オブジェクト（不変オブジェクト）
   - services/: ドメインサービス
   - repositories/: リポジトリインターフェース
   - events/: ドメインイベント
   ```

4. **Set Up Development Environment**:
   - Use `uv add` to install dependencies directly (avoid manual pyproject.toml editing due to version resolution issues)
   - Install necessary dependencies:
   ```bash
   uv add --dev pytest
   uv add --dev pytest-cov
   uv add --dev ruff
   uv add --dev pyright
   # Add framework-specific dependencies as needed
   # Example: uv add fastapi
   # Example: uv add sqlalchemy
   ```

5. **Create Configuration Files**:
   - `.gitignore` for Python projects
   - `pytest.ini` for test configuration
   - `ruff.toml` for linting rules
   - `.pre-commit-config.yaml` if using pre-commit

6. **Initialize Git Repository** (if not exists):
   ```bash
   git init
   git add .
   git commit -m "Initialize TDD/DDD/Layered Architecture structure"
   ```

7. **Create Initial Documentation**:
   - Create `docs/architecture.md` in JAPANESE explaining the architecture
   - Include diagrams if helpful

8. **Provide Next Steps**:
   - Display message in JAPANESE:
   ```
   プロジェクト構造の初期化が完了しました。
   
   次のステップ:
   1. GitHub issueを作成または選択
   2. /create-use-case <issue番号> でユースケース仕様を作成
   3. TDD/DDD/レイヤードアーキテクチャの開発フローに従って実装
   ```

Important Notes:
- This command sets up the entire project structure at once
- Useful for new projects or major refactoring
- Can be run safely on existing projects (won't overwrite files)
- All user-facing output must be in JAPANESE