# Project Status Command

**Summary**: Provides comprehensive project overview and health metrics for the TDD/DDD/Layered Architecture development system.

**Description**: The `/project-status` command delivers a complete project overview distinct from `/use-case-status` by focusing on system-wide health, integration status, and overall development progress across all layers and phases.

**📖 Required Reading**: Before execution, this command MUST read the following files:
- `/workspace/.claude/context/current-command-context.json` - Current execution context
- `/workspace/.claude/context/project-context.json` - Overall project state and active sprint information  
- `/workspace/docs/metadata/project-state.json` - Integrated project status and health metrics
- `/workspace/docs/index.md` - Project dashboard for navigation context

This command MUST USE PROACTIVELY the specialized **17-project-status** subagent for optimal project overview generation and comprehensive system status analysis.

## Command Usage

```bash
/project-status [scope]
```

### Parameters
- `scope` (optional): Specific focus area (`health`, `architecture`, `sprint`, `quality`, `all`)
  - Default: `all` - Complete project overview

### Examples
```bash
# Complete project status overview
/project-status

# Focus on system health metrics
/project-status health

# Architecture layer completion status
/project-status architecture

# Current sprint progress overview
/project-status sprint

# Quality metrics and TDD compliance
/project-status quality
```

## Key Features

### 🎯 Comprehensive Project Overview
- **Project Health Score**: Overall system health (0-100)
- **Phase Progress**: Current implementation phase and completion rate
- **Architecture Status**: Layer-by-layer completion analysis
- **Sprint Management**: Active sprint progress and velocity metrics
- **Quality Dashboard**: TDD compliance and test coverage metrics

### 📊 System Integration Status
- **Command System Health**: Custom command operational status
- **Subagent Integration**: Specialized agent utilization metrics  
- **Context Management**: Project context file synchronization status
- **Metadata Integrity**: Cross-system data consistency verification

### 🔍 Differentiation from /use-case-status
| Aspect | /project-status | /use-case-status |
|--------|----------------|------------------|
| **Scope** | System-wide health & integration | Individual use case implementation |
| **Focus** | Architecture layers & project phases | Specific scenarios & acceptance criteria |
| **Metrics** | Health scores, velocity, quality | Test coverage per use case |
| **Audience** | Project managers, architects | Developers, testers |
| **Frequency** | Sprint reviews, health checks | Daily development tracking |

## Output Format

### Complete Overview Format
```markdown
# 📊 TDD/DDD/Layered Architecture Project Status

## 🎯 Project Health Overview
- **Overall Health Score**: 85/100 ✅
- **Current Phase**: Phase 2: Core Feature Enhancement  
- **Implementation Progress**: 75% (Domain: 60%, Application: 70%, Infrastructure: 80%, Presentation: 90%)
- **Active Sprint**: Sprint 2 (Day 8/14) - 57% complete

## 🏗️ Architecture Layer Status
- **Domain Layer**: 12 entities, 8 value objects (60% complete)
- **Application Layer**: 18 use cases implemented (70% complete)  
- **Infrastructure Layer**: 15 repositories, 6 external services (80% complete)
- **Presentation Layer**: 21 CLI commands, 12 API endpoints (90% complete)

## 📈 Sprint & Velocity Metrics
- **Current Sprint Velocity**: 8 story points/week
- **Completed Issues**: 24/32 tickets (75%)
- **Blocked Issues**: 2 tickets (infrastructure dependencies)
- **Sprint Goal Achievement**: On track (85% confidence)

## 🧪 Quality & TDD Compliance
- **Test Coverage**: Overall 82% (Unit: 85%, Integration: 75%, E2E: 70%)
- **TDD Cycles Completed**: 28 RED-GREEN-REFACTOR cycles
- **Code Quality Score**: 88/100 (Linting: 95%, Type Safety: 85%, Complexity: 85%)

## 🤖 System Integration Status
- **Custom Commands**: 21/21 operational (100%)
- **Subagent Integration**: 16/16 active (100%)  
- **Context Management**: Fully synchronized
- **Metadata Integrity**: All systems consistent

## ⚠️ Risk Indicators & Alerts
- **Medium Risk**: Infrastructure layer dependency on external APIs
- **Low Risk**: Test coverage below 80% in presentation layer
- **Action Required**: 2 blocked issues require stakeholder input

## 📋 Recommended Actions
1. **Immediate**: Resolve 2 blocked infrastructure issues
2. **This Sprint**: Increase E2E test coverage to 80%
3. **Next Sprint**: Plan Phase 3 advanced integration features
```

### Focused Scope Formats

#### Health Scope
```markdown
# 🏥 Project Health Status

## Overall Health: 85/100 ✅
- **System Stability**: Excellent (95/100)
- **Integration Quality**: Good (80/100)  
- **Development Velocity**: Good (85/100)
- **Technical Debt**: Low (10/100)

## Health Indicators
- 🟢 All core systems operational
- 🟡 Some integration dependencies pending
- 🟢 Test coverage above minimum thresholds
- 🟢 No critical blocking issues
```

## 🔄 **PHASE 3: ENHANCED INTEGRATION FEATURES**

### **Project State Updates**
This command updates project health metrics and system status:

```json
{
  "project_metadata": {
    "health_score": "RECALCULATE_BASED_ON_METRICS",
    "last_status_check": "UPDATE_TIMESTAMP"
  },
  "system_health": {
    "command_system": {
      "last_health_check": "UPDATE_TIMESTAMP",
      "health_score": "CALCULATE_SYSTEM_HEALTH"
    },
    "integration_status": {
      "last_status_verification": "UPDATE_TIMESTAMP"
    }
  },
  "recent_activity": {
    "last_command_executed": "17-project-status",
    "last_metadata_update": "UPDATE_TIMESTAMP"
  }
}
```

### **Context File Updates**
```json
{
  "current_state": {
    "last_command": "project-status",
    "last_command_timestamp": "UPDATE_TIMESTAMP"
  },
  "workflow_tracking": {
    "command_usage": {
      "project_status": "INCREMENT_USAGE_COUNT"
    }
  }
}
```

## Error Handling

### Missing Files Recovery
If required context files are missing or corrupted:

1. **Alert User**: Clear notification of missing dependencies
2. **Fallback Mode**: Generate status from available data sources
3. **Recovery Guidance**: Direct user to manual synchronization procedures
4. **Reference**: `/workspace/docs/maintenance/manual-sync-guide.md`

### Inconsistent Metadata Recovery
If cross-system metadata inconsistencies detected:

1. **Conflict Report**: Detailed inconsistency analysis
2. **Resolution Options**: Automatic vs manual conflict resolution
3. **Backup Recommendation**: Suggest creating restore point
4. **Repair Guidance**: Step-by-step consistency restoration

## Integration Points

### Dashboard Integration
- **Navigation**: Accessible from `/workspace/docs/index.md`
- **Quick Access**: Listed under "📊 Project Management" commands
- **Cross-Reference**: Links to detailed component status

### Command Dependencies
- **Prerequisite**: Project context system (`Phase 2+`)
- **Complementary**: `/use-case-status` for detailed use case tracking
- **Integration**: `/sprint-planning` for velocity planning
- **Follow-up**: `/apply-feedback` for improvement implementation

---

**🎯 Command Purpose**: This command provides essential project-wide visibility ensuring both "forest view" (system health) and integration with "tree view" (detailed implementation) for comprehensive project management in the TDD/DDD/Layered Architecture workflow.