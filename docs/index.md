# TDD/DDD/Layered Architecture Project Dashboard

**Project Management Hub** - プロジェクトの全体像と詳細情報への統一アクセスポイント

## 🎯 Project Overview

This project implements a comprehensive TDD/DDD/Layered Architecture development workflow with custom commands and specialized subagents for systematic software development.

### Current Status
- **Project Phase**: Development Enhancement (Phase 2)
- **Architecture**: Test-Driven Development + Domain-Driven Design + Layered Architecture
- **Command System**: 21 custom commands with specialized subagents
- **Documentation**: Comprehensive multilingual (Japanese/English) documentation

## 📁 Project Structure

### 🏗️ Core Architecture Documents
```
docs/
├── 📋 [Project Vision](vision/) - Overall project vision and bounded contexts
├── 📖 [Use Cases](use_cases/) - Detailed use case specifications and scenarios
├── 🏛️ [Domain Models](domain/) - Domain entity designs and aggregate boundaries  
├── 🧪 [Test Plans](test_plan/) - Test strategies and coverage plans
├── 📊 [Test Reports](test_report/) - Test execution results and metrics
└── 📚 [Application Layer](application/) - Use case orchestration documentation
```

### 🔧 Development Workflow
```
.claude/
├── 📞 [Custom Commands](../claude/commands/tdd-ddd-layered/) - 21 workflow automation commands
├── 🤖 [Specialized Agents](../claude/agents/) - Dedicated subagents for each phase
└── 🗂️ [Context Management](../claude/context/) - Project state and context files
```

### 📝 Implementation Tracking
```
src/
├── 🏛️ domain/ - Business logic and domain entities
├── 🔄 application/ - Use case implementations
├── 🔌 infrastructure/ - External service integrations
└── 🖥️ presentation/ - API endpoints and user interfaces
```

## 🚀 Quick Navigation

### 📋 Development Phases
| Phase | Status | Commands | Documentation |
|-------|--------|----------|---------------|
| **Vision & Planning** | ✅ | `/create-vision`, `/sprint-planning` | [Vision Docs](vision/) |
| **Use Case Design** | ✅ | `/create-use-case`, `/domain-modeling` | [Use Cases](use_cases/) |
| **Test Creation** | ✅ | `/create-tests`, `/review-test-design` | [Test Plans](test_plan/) |
| **Implementation** | 🔄 | `/implement-domain`, `/implement-usecase` | [Domain Docs](domain/) |
| **Integration** | ⏳ | `/implement-infra`, `/implement-presentation` | [Application Docs](application/) |
| **Quality Assurance** | ⏳ | `/run-all-tests`, `/refactor` | [Test Reports](test_report/) |

### 🎯 Command Categories

#### 🏁 Project Initialization
- `/init-project-structure` - Set up TDD/DDD/Layered architecture
- `/create-vision` - Define project vision and core scenarios

#### 📋 Sprint Management  
- `/sprint-planning <number>` - Plan and create sprint tickets
- `/review-sprint-plan <number>` - Validate sprint planning quality

#### 📖 Specification Phase
- `/create-use-case <issue>` - Create detailed Given-When-Then scenarios
- `/domain-modeling <issue>` - Design domain entities and aggregates
- `/review-domain-design <issue>` - Validate domain model quality

#### 🧪 Test-Driven Development
- `/create-tests <issue>` - Create failing tests (TDD RED)
- `/review-test-design <issue>` - Validate test coverage and quality

#### 🏗️ Implementation Phase
- `/implement-domain <issue>` - Implement business logic (TDD GREEN)
- `/implement-usecase <issue>` - Create application layer orchestration
- `/implement-infra <issue>` - Implement infrastructure and persistence
- `/implement-presentation <issue>` - Create user interfaces and APIs

#### 🔄 Quality & Integration
- `/run-all-tests <issue>` - Execute comprehensive test suite
- `/review-test-results <issue>` - Analyze test execution results
- `/refactor <issue>` - Improve code quality (TDD REFACTOR)

#### 📊 Project Management
- `/review-issue <issue>` - Analyze GitHub issue requirements
- `/use-case-status` - Track implementation progress across use cases
- `/evolve-scenarios <feature>` - Add new scenarios during sprints
- `/apply-feedback <source>` - Apply sprint review feedback
- `/create-pr <issue>` - Create comprehensive pull requests

## 🔍 Status Tracking

### 📊 Implementation Progress
- **Domain Layer**: Track business logic implementation
- **Application Layer**: Monitor use case orchestration
- **Infrastructure Layer**: Follow persistence and integration progress
- **Presentation Layer**: Observe user interface development

### 🧪 Quality Metrics
- **Test Coverage**: Comprehensive test suite coverage tracking
- **TDD Compliance**: RED-GREEN-REFACTOR cycle adherence
- **Domain Purity**: Business logic isolation verification
- **Architecture Boundaries**: Layer separation maintenance

## 🔧 Maintenance & Troubleshooting

### 📋 Operational Guides
- **[Manual Sync Guide](./maintenance/manual-sync-guide.md)** - Manual synchronization procedures for irregular workflow situations
- **[Implementation Reports](./maintenance/)** - Detailed implementation status and progress reports

### ⚠️ Error Handling
When encountering issues outside standard workflow:
1. **Consult Manual Sync Guide**: [docs/maintenance/manual-sync-guide.md](./maintenance/manual-sync-guide.md)
2. **Check Project Status**: Use `/use-case-status` for current state assessment
3. **Review Context**: Examine `.claude/context/current-command-context.json`

### 🛠️ Recovery Procedures
```bash
# Quick status check
/use-case-status

# Manual synchronization guide
docs/maintenance/manual-sync-guide.md

# Context verification
.claude/context/current-command-context.json
```

## 📚 Reference Documentation

### 🏛️ Architectural Principles
- **TDD (Test-Driven Development)**: RED-GREEN-REFACTOR cycle implementation
- **DDD (Domain-Driven Design)**: Ubiquitous language and bounded contexts
- **Layered Architecture**: Clear separation of concerns across layers

### 📖 Key Documents
- **[Development Approach Overview](./TDD、DDD、レイヤードアーキテクチャで開発を進めるアプローチ完成版.md)** - Comprehensive methodology guide
- **[Process Design Workflow](./プロセス設計_ビジョンからチケット作成フロー.md)** - Vision to ticket creation flow
- **[Git Worktree Guide](./Git%20Worktree%20の典型的な開発の流れ.md)** - Git workflow best practices

### 🔗 External References
- **[CLAUDE.md](../CLAUDE.md)** - Development guidelines and project instructions
- **[README.md](../README.md)** - Project setup and getting started guide

## 🎯 Next Actions

### ⏭️ Recommended Workflow
1. **Start with Vision**: `/create-vision` to establish project foundation
2. **Plan Sprints**: `/sprint-planning 1` for systematic ticket creation
3. **Follow TDD/DDD**: Use implementation commands in sequence
4. **Monitor Progress**: Regular `/use-case-status` checks
5. **Quality Focus**: Complete with `/refactor` and `/create-pr`

### 📈 Continuous Improvement
- **Sprint Reviews**: Use `/apply-feedback` for systematic improvements
- **Scenario Evolution**: Apply `/evolve-scenarios` for requirement changes
- **Quality Gates**: Leverage review commands for consistent quality

---

**🔧 System Information**: This dashboard provides comprehensive navigation for the TDD/DDD/Layered Architecture development system. For detailed command usage, refer to individual command documentation in `.claude/commands/tdd-ddd-layered/`.

**📅 Last Updated**: 2025-08-27  
**🏷️ Version**: 2.0 - Phase 2 Implementation  
**👥 Maintainer**: System Architecture Team