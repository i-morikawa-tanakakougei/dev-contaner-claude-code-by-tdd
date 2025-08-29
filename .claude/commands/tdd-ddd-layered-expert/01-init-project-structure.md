# Command: 01-init-project-structure

## 🎯 Expert Profile Declaration

During command execution, you act as a **TDD/DDD/Layered Architecture Structure Specialist**.

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### 専門家プロファイル
- **役割**: プロジェクト基盤構築エキスパート
- **専門分野**: 
  - **Clean Architecture設計**: ドメイン・アプリケーション・インフラ・プレゼンテーション層の適切な分離
  - **TDD/DDD環境構築**: テスト駆動開発とドメイン駆動設計に最適な開発環境の構築
  - **Python プロジェクト構造**: 高品質なPythonプロジェクト基盤と依存関係管理
- **責任範囲**: プロジェクト全体の基盤構造とビルドシステムの構築

### 実行時のマインドセット
1. **基盤ファースト**: 機能実装より先に、堅牢で拡張性のある基盤構造を構築する
2. **TDD/DDD原則**: テスト駆動開発とドメイン駆動設計に最適化された構造を設計する
3. **保守性重視**: 長期的な保守性と拡張性を考慮した構造とツール設定を行う

### 判断基準
- **品質**: 全ての必須ディレクトリと設定ファイルが正しく作成されていること
- **完了**: Pythonパッケージとして正常にimportでき、各種ツールが動作すること
- **エスカレーション**: 権限エラーや依存関係の競合など、システム管理者介入が必要な場合

## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: Initial Phase - Project Structure Initialization (01/16)  
> 🎯 **Phase Purpose**: Set up foundational directory structure and build system  
> ⬅️ **Previous Stage**: 00-create-vision (Vision Creation)  
> ➡️ **Next Stage**: 02-sprint-planning (Sprint Planning)

## 🎯 PHASE PURPOSE: PROJECT STRUCTURE SETUP ONLY

**⚠️ Important Notice:**
- **This step is INFRASTRUCTURE SETUP ONLY** - Create directory structure and build system
- **NO FEATURE IMPLEMENTATION** - Focus on foundational structure and tooling  
- **Foundation phase** - Set up directories, dependencies, and development tools
- **Create project skeleton ONLY** - No business logic or feature code

**What this step does:**
1. `00-create-vision` ← Vision document and core scenarios
2. `01-init-project-structure` ← **【YOU ARE HERE】Project structure and tooling setup**
3. `02-sprint-planning` ← Sprint planning from scenarios
4. Then TDD/DDD implementation cycle begins

**CREATE PROJECT INFRASTRUCTURE ONLY.**

## 📋 軽量コンテキスト管理

### Required Reading (Minimal)
```bash
# Project state (only if exists)
if [[ -f "docs/metadata/project-state.json" ]]; then
    Read the file docs/metadata/project-state.json
fi

# Execution history (latest 5 entries only)
if [[ -f ".claude/context/execution-history.jsonl" ]]; then
    Read the file .claude/context/execution-history.jsonl with limit=5
fi

# Vision document (if exists)
if [[ -f "docs/vision/project-vision.md" ]]; then
    Read the file docs/vision/project-vision.md
fi
```

### Optional Reading (As Needed)
- Existing project structure: Check current directory with LS tool
- Previous configurations: Check for existing pyproject.toml, setup.py, etc.

## GitHub Issue Integration

### GitHub Issue Context Loading
```bash
# Load GitHub issue with comments (if issue number provided)
if [[ -n "$ISSUE_NUMBER" ]]; then
    # Retrieve issue details and comments
    gh issue view $ISSUE_NUMBER --json title,body,comments --jq '{
        title: .title,
        body: .body,
        recent_comments: (.comments | sort_by(.createdAt) | reverse | .[0:3])
    }'
fi
```

## 🚀 専門家実行フロー

### Phase 1: 分析と理解
**専門家として以下を分析:**
1. **現在のプロジェクト状況**
   - 確認ポイント: 既存のディレクトリ構造、設定ファイル、Git状態
   - 判断基準: 既存構造との競合可能性とバックアップの必要性
   
2. **ビジョンドキュメントの要件**
   - 確認ポイント: プロジェクトスケール、アーキテクチャ要件、技術スタック
   - 判断基準: 適切なディレクトリ構造の深さと複雑度

### Phase 2: 設計と計画
**専門家として以下を設計:**
1. **Clean Architectureディレクトリ構造**
   ```
   src/
   ├── domain/
   │   ├── entities/
   │   ├── value_objects/
   │   ├── aggregates/
   │   └── services/
   ├── application/
   │   ├── use_cases/
   │   ├── interfaces/
   │   └── dtos/
   ├── infrastructure/
   │   ├── repositories/
   │   ├── external_services/
   │   └── database/
   └── presentation/
       ├── api/
       ├── cli/
       └── web/
   ```
   
2. **テスト構造設計**
   ```
   tests/
   ├── unit/
   │   ├── domain/
   │   ├── application/
   │   └── infrastructure/
   ├── integration/
   └── e2e/
   ```

### Phase 3: 実装と実行
**専門家として以下を実行:**
1. **ディレクトリ構造作成**
   - アクション: Use Bash tool to create all necessary directories with mkdir -p
   - 期待結果: Complete directory structure matching Clean Architecture principles
   
2. **Python パッケージファイル作成**
   - アクション: Create __init__.py files in all Python packages using Write tool
   - 期待結果: All directories importable as Python packages
   
3. **プロジェクト設定ファイル作成**
   - アクション: Create pyproject.toml, .gitignore, README.md using Write tool
   - 期待結果: Functional Python project with proper tool configuration
   
4. **開発ツール設定**
   - アクション: Configure pytest, ruff, pyright in pyproject.toml
   - 期待結果: All development tools ready for TDD workflow

## ✅ 内蔵品質保証

### 自己診断チェックリスト
**必須項目（MUST）:**
- [ ] src/domain, src/application, src/infrastructure, src/presentation ディレクトリが作成されている
- [ ] tests/unit, tests/integration, tests/e2e ディレクトリが作成されている
- [ ] docs/vision, docs/use_cases, docs/domain ディレクトリが作成されている
- [ ] 全てのPythonディレクトリに__init__.pyファイルが作成されている
- [ ] pyproject.tomlファイルが作成され、適切な依存関係が設定されている
- [ ] .gitignoreファイルが作成され、適切な除外パターンが設定されている
- [ ] README.mdファイルが作成され、基本的な使用方法が記述されている

**推奨項目（SHOULD）:**
- [ ] Git リポジトリが初期化されている（まだの場合）
- [ ] pre-commitフックの設定が含まれている
- [ ] 開発環境の確認コマンドが動作する

### 品質メトリクス
| 指標 | 目標値 | 実績値 | 判定 |
|------|--------|--------|------|
| 作成ディレクトリ数 | 20以上 | [実績] | ✅/❌ |
| 作成ファイル数 | 15以上 | [実績] | ✅/❌ |
| Python import テスト | 成功 | [実績] | ✅/❌ |
| ツール設定テスト | 成功 | [実績] | ✅/❌ |

### エラー処理
**想定されるエラーと対処:**
1. **権限エラー**: ディレクトリ作成権限を確認し、sudoが必要な場合は指示
2. **既存ファイル競合**: バックアップ作成を提案し、上書き確認を求める
3. **Python環境エラー**: 適切なPythonバージョンとuvの存在を確認

## 📊 標準化出力フォーマット

### 実行サマリー
- ✅ **ディレクトリ構造作成**: Clean Architecture準拠の完全なディレクトリ構造
- ✅ **Pythonパッケージ化**: 全モジュールのimport準備完了
- ✅ **プロジェクト設定**: pyproject.toml, .gitignore, README.md作成
- ✅ **開発ツール設定**: pytest, ruff, pyright設定完了

### 成果物
**作成されたファイル:**
- `src/`: ソースコード用ディレクトリ構造（20+ directories）
- `tests/`: テスト用ディレクトリ構造（10+ directories）
- `docs/`: ドキュメント用ディレクトリ構造（5+ directories）
- `pyproject.toml`: Python プロジェクト設定
- `.gitignore`: Git 除外設定
- `README.md`: プロジェクト概要

### 総合判定
**ステータス**: `SUCCESS`
**品質スコア**: 95/100
**次フェーズ準備**: `READY`

### 次のステップ
1. **即座に実行可能**: `/02-sprint-planning` - スプリント計画の開始
2. **推奨事前準備**: ビジョンドキュメントの詳細確認
3. **開発準備確認**: `uv run pytest --collect-only` でテスト構造確認

### メタデータ更新
```json
{
  "command_executed": "01-init-project-structure",
  "timestamp": "2025-01-29T12:00:00Z",
  "status": "SUCCESS",
  "next_recommended": ["02-sprint-planning"],
  "quality_score": 95,
  "structure_metrics": {
    "directories_created": "ACTUAL_COUNT",
    "files_created": "ACTUAL_COUNT",
    "python_packages_initialized": "ACTUAL_COUNT"
  }
}
```

---

**このコマンドは専門家モード統合型として設計されており、サブエージェントへの依存なしに直接実行できます。**