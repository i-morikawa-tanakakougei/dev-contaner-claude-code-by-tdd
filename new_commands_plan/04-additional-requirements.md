# Additional Requirements for New Command Architecture

## 🌐 Language Usage Guidelines

### Claude Code Instructions
- **Language**: English
- **Purpose**: Technical instructions, tool calls, system commands
- **Examples**:
  - `Read the file /workspace/docs/vision/project-vision.md`
  - `Use the Task tool with subagent_type='domain-modeling'`
  - `Execute git status to check repository state`

### User Interactions
- **Language**: Japanese
- **Purpose**: All communication with users, status updates, explanations
- **Examples**:
  - `🎯 プロジェクトビジョン作成を開始します`
  - `✅ ドメインモデル設計が完了しました`
  - `次のステップ: /implement-domain を実行してください`

## 🎯 Required Context Sections

### 1. Expert Profile Declaration
```markdown
## 🎯 Expert Profile Declaration

During command execution, you act as a **[Expert Title]** specialist.

### Your Expertise
- **[Domain 1]**: [Specific knowledge and capabilities in English]
- **[Domain 2]**: [Specific knowledge and capabilities in English]

### Execution Principles
1. [Principle 1]: [Action guidelines in English]
2. [Principle 2]: [Action guidelines in English]

**Language Guidelines:**
- All technical instructions to Claude Code should be written in English
- All user interactions and responses should be in Japanese
```

### 2. TDD/DDD/LAYERED PROCESS CONTEXT
```markdown
## 🎯 TDD/DDD/LAYERED PROCESS CONTEXT

**🔄 Core Workflow**: Vision(00) → Structure(01) → Sprint(02) → Use-Case(03) → Domain(04) → Tests(05) → Domain(06) → App(07) → Infra(08) → UI(09) → Test(10) → Refactor(11) → Evolve(12) → Review(13) → Feedback(14) → PR(15) → Status(16)

**🎨 Architecture**: Clean Architecture (Domain→Application→Infrastructure→Presentation)  
**🧪 Development**: Test-Driven Development (RED→GREEN→REFACTOR)  
**🏗️ Design**: Domain-Driven Design (Entity, Value Object, Aggregate, Repository)  
**📋 Requirements**: Given-When-Then scenarios with complete traceability  
**🔄 Evolution**: Continuous scenario evolution via /evolve-scenarios command

> 📖 **Document Management System**: [README.md](./README.md)  
> 🗺️ **Current Position**: [Current Phase] - [Description] ([X]/16)  
> 🎯 **Phase Purpose**: [Specific phase purpose description]  
> ➡️ **Next Stage**: [Next recommended command or phase]
```

### 3. PHASE PURPOSE Section
```markdown
## 🎯 PHASE PURPOSE: [SPECIFIC PHASE DESCRIPTION]

**⚠️ Important Notice:**
- **This step focuses on [PHASE SCOPE]** - [Detailed description]
- **[IMPLEMENTATION SCOPE]** - [What should/shouldn't be implemented]  
- **[QUALITY FOCUS]** - [Quality standards and validation criteria]

**What this step does:**
1. `[current-command]` ← **【YOU ARE HERE】[Description]**
2. `[previous-command]` ← [Previous step description]
3. `[next-command]` ← [Next step description]
4. Then [subsequent workflow description]

**[PHASE SPECIFIC INSTRUCTION IN CAPS].**
```

## 📋 GitHub Issue Integration Requirements

### Issue Comment Retrieval
All commands that process GitHub issues MUST:

1. **Retrieve Issue Comments**:
```bash
# Always fetch issue with comments
gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt

# Get comment timeline with timestamps
gh issue view $ISSUE_NUMBER --json comments --jq '.comments | sort_by(.createdAt) | reverse'
```

2. **Prioritize Recent Comments**:
   - Sort comments by creation date (most recent first)
   - Treat recent comments as specification updates
   - Consider comment recency in analysis weight
   - Flag specification conflicts between initial description and recent comments

3. **Specification Tracking**:
   - Track requirement changes through comment timeline
   - Identify contradictory specifications
   - Highlight latest authoritative requirements
   - Note specification evolution patterns

### Implementation Template
```markdown
## GitHub Issue Analysis

### Issue Retrieval Process
```bash
# Fetch issue with full context
if [[ -n "$ISSUE_NUMBER" ]]; then
    echo "Retrieving GitHub issue #$ISSUE_NUMBER with comments..."
    
    # Get issue details with comments
    ISSUE_DATA=$(gh issue view $ISSUE_NUMBER --json title,body,comments,updatedAt,createdAt)
    
    # Extract and prioritize recent comments
    RECENT_COMMENTS=$(echo "$ISSUE_DATA" | jq -r '.comments | sort_by(.createdAt) | reverse | .[0:5]')
    
    echo "Found $(echo "$ISSUE_DATA" | jq '.comments | length') comments"
    echo "Prioritizing latest 5 comments for specification analysis"
fi
```

### Comment Analysis Strategy
1. **Latest First**: Recent comments override earlier specifications
2. **Authority Recognition**: Identify specification authors vs. discussants  
3. **Change Tracking**: Monitor requirement evolution
4. **Conflict Detection**: Flag contradictory requirements
```

## 🔄 Structural Flow Requirements

### Command Structure Order
1. **Expert Profile Declaration** (English technical instructions)
2. **TDD/DDD/LAYERED PROCESS CONTEXT** (Process context and navigation)
3. **PHASE PURPOSE** (Phase-specific scope and limitations)
4. **Lightweight Context Management** (Minimal JSON loading)
5. **GitHub Issue Integration** (Issue and comment retrieval)
6. **Expert Execution Flow** (Implementation steps - Japanese user interaction)
7. **Built-in Quality Assurance** (Self-validation)
8. **Standardized Output Format** (Consistent reporting)

### Forest-to-Tree Approach
The structure follows a "forest-to-tree" information hierarchy:

1. **Expert Profile** (System prompt - establish expertise)
2. **Process Context** (Forest view - overall workflow understanding)  
3. **Phase Purpose** (Tree focus - current specific task)
4. **Context & Integration** (Supporting information gathering)
5. **Execution** (Detailed implementation with user interaction)
6. **Quality & Output** (Validation and standardized reporting)

This ensures Claude understands the broader context before diving into specific implementation details.

## ✅ Implementation Checklist

For each new command, verify:

- [ ] Expert profile declaration in English at the top
- [ ] TDD/DDD/LAYERED PROCESS CONTEXT section included
- [ ] PHASE PURPOSE section with clear scope definition
- [ ] GitHub issue integration with comment prioritization
- [ ] All Claude Code instructions in English
- [ ] All user interactions in Japanese
- [ ] Forest-to-tree information structure maintained
- [ ] Consistent section ordering followed
- [ ] Quality assurance mechanisms included
- [ ] Standardized output format implemented