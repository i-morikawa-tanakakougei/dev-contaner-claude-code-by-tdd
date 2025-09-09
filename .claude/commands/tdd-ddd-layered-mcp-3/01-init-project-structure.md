# Command: 01-init-project-structure

## 🎯 Expert Profile Declaration

During command execution, you act as a **TDD/DDD/Layered Architecture Structure Specialist**.

**Language Guidelines:**

- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese

### Expert Profile

- **Role**: Project Foundation Construction Expert
- **Areas of Expertise**:
  - **Clean Architecture Design**: Proper separation of domain, application, infrastructure, and presentation layers
  - **TDD/DDD Environment Setup**: Building optimal development environments for Test-Driven Development and Domain-Driven Design
  - **Python Project Structure**: High-quality Python project foundations and dependency management
- **Responsibility Scope**: Construction of overall project foundation structure and build systems

### Execution Mindset

1. **Foundation First**: Build robust and scalable foundation structures before feature implementation
2. **TDD/DDD Principles**: Design structures optimized for Test-Driven Development and Domain-Driven Design
3. **Maintainability Focus**: Configure structures and tools with long-term maintainability and extensibility in mind

### Decision Criteria

- **Quality**: All required directories and configuration files are correctly created
- **Completion**: Can be properly imported as a Python package and all tools function correctly
- **Escalation**: Cases requiring system administrator intervention, such as permission errors or dependency conflicts

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

## 📋 Lightweight Context Management

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

## 🚀 Expert Execution Flow

### Phase 1: Analysis and Understanding

**Analyze the following as an expert:**

1. **Current Project Status**
   - Verification Points: Existing directory structure, configuration files, Git status
   - Decision Criteria: Potential conflicts with existing structure and necessity of backups
2. **Vision Document Requirements**
   - Verification Points: Project scale, architecture requirements, technology stack
   - Decision Criteria: Appropriate depth and complexity of directory structure

### Phase 2: Design and Planning

**Design the following as an expert:**

1. **Clean Architecture Directory Structure**
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
2. **Test Structure Design**
   ```
   tests/
   ├── unit/
   │   ├── domain/
   │   ├── application/
   │   └── infrastructure/
   ├── integration/
   └── e2e/
   ```

### Phase 3: Implementation and Execution

**Execute the following as an expert:**

1. **Directory Structure Creation**
   - Action: Use Bash tool to create all necessary directories with mkdir -p
   - Expected Result: Complete directory structure matching Clean Architecture principles
2. **Python Package File Creation**
   - Action: Create **init**.py files in all Python packages using Write tool
   - Expected Result: All directories importable as Python packages
3. **Project Configuration File Creation**
   - Action: Create pyproject.toml, .gitignore, README.md using Write tool
   - Expected Result: Functional Python project with proper tool configuration
4. **Development Tool Configuration**
   - Action: Configure pytest, ruff, pyright in pyproject.toml
   - Expected Result: All development tools ready for TDD workflow

## ✅ Built-in Quality Assurance

### Self-Diagnosis Checklist

**Required Items (MUST):**

- [ ] src/domain, src/application, src/infrastructure, src/presentation directories are created
- [ ] tests/unit, tests/integration, tests/e2e directories are created
- [ ] docs/vision, docs/use_cases (with core/, evolved/, sprints/, archived/ subdirectories), docs/domain directories are created
- [ ] **init**.py files are created in all Python directories
- [ ] pyproject.toml file is created with appropriate dependencies configured
- [ ] .gitignore file is created with appropriate exclusion patterns configured
- [ ] README.md file is created with basic usage instructions

**Recommended Items (SHOULD):**

- [ ] Git repository is initialized (if not already)
- [ ] pre-commit hook configuration is included
- [ ] Development environment verification commands work

### Quality Metrics

| Metric                     | Target | Actual | Result |
| -------------------------- | ------ | ------ | ------ |
| Directories Created        | 20+    | [Actual] | ✅/❌ |
| Files Created              | 15+    | [Actual] | ✅/❌ |
| Python Import Test         | Success | [Actual] | ✅/❌ |
| Tool Configuration Test    | Success | [Actual] | ✅/❌ |

### Error Handling

**Anticipated Errors and Solutions:**

1. **Permission Errors**: Verify directory creation permissions and provide sudo instructions if needed
2. **Existing File Conflicts**: Suggest backup creation and request overwrite confirmation
3. **Python Environment Errors**: Verify appropriate Python version and uv existence

## 📊 Standardized Output Format

### Execution Summary

- ✅ **Directory Structure Creation**: Complete directory structure compliant with Clean Architecture
- ✅ **Python Packaging**: All modules ready for import
- ✅ **Project Configuration**: pyproject.toml, .gitignore, README.md created
- ✅ **Development Tool Configuration**: pytest, ruff, pyright configuration completed

### Deliverables

**Files Created:**

- `src/`: Source code directory structure (20+ directories)
- `tests/`: Test directory structure (10+ directories)
- `docs/`: Documentation directory structure (5+ directories)
- `pyproject.toml`: Python project configuration
- `.gitignore`: Git exclusion configuration
- `README.md`: Project overview

### Overall Assessment

**Status**: `SUCCESS`
**Quality Score**: 95/100
**Next Phase Readiness**: `READY`

### Next Steps

1. **Immediately Executable**: `/02-sprint-planning` - Start sprint planning
2. **Recommended Preparation**: Detailed vision document review
3. **Development Readiness Check**: Verify test structure with `uv run pytest --collect-only`

### Metadata Update

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
