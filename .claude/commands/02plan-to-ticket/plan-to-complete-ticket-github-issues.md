Please break down the implementation plan from the GitHub issue: $ARGUMENTS into smaller tickets for team development and create individual ticket issues.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  Use `gh issue view $ARGUMENTS` to retrieve the details of the implementation plan issue titled "<original issue title>[実装計画]".
3.  Analyze the implementation plan described in the issue.
4.  Break down the plan into smaller, actionable tickets suitable for team development.
5.  For each ticket, create a new GitHub issue with:
    - Title: "<original issue title>[チケット:<ticket description>]"
    - Body: Include a clear description of the ticket, reference the original issue number (#$ARGUMENTS), and specify any dependencies or relevant files.
    - Labels: Add appropriate labels (e.g., `ticket`, `development`). If no suitable label exists, create one using `gh label create`
    - **Development Requirements**: Each ticket must follow the "Complete Deliverable Rule":
      - **docs/**: Specification and design documents (Markdown/PDF) must be created first
      - **tests/**: Test code must be written based on the specifications
      - **src/**: Implementation code must be developed to pass all tests
      - **README.md/CHANGELOG.md**: Update with relevant information
      - All these components must be included in a single commit when completing the ticket
6.  Include the following template in each ticket body:
    ```
    ## Ticket Description
    [Detailed description of the ticket]
    
    ## Reference
    - Original issue: #$ARGUMENTS
    - Dependencies: [List any dependent tickets]
    
    ## Complete Deliverable Checklist
    - [ ] Specification document created in `docs/`
    - [ ] Design document created in `docs/`
    - [ ] Test code written in `tests/`
    - [ ] Implementation code developed in `src/`
    - [ ] README.md updated (if needed)
    - [ ] CHANGELOG.md updated (if needed)
    - [ ] All components committed in a single commit
    
    ## Acceptance Criteria
    [List specific criteria for ticket completion]
    ```
7.  After creating all ticket issues, add a comment to the implementation plan issue (#$ARGUMENTS) listing all new ticket issue numbers for reference.
8.  Close the implementation plan issue (#$ARGUMENTS) as it is no longer needed after ticket breakdown.
9.  Ensure all actions are performed using the GitHub CLI (`gh`).

## Development Guidelines

Each ticket must adhere to the "Complete Deliverable Rule":

1. **Documentation First**: Create specifications and design documents in the `docs/` folder before implementation
2. **Test-Driven Development**: Write comprehensive test cases in the `tests/` folder based on specifications
3. **Implementation**: Develop code in the `src/` folder that satisfies all test cases
4. **Single Commit Rule**: All deliverables (docs, tests, src, and related updates) must be included in a single commit

This approach ensures:
- Clear understanding of requirements before coding
- Comprehensive test coverage
- Complete and reviewable deliverables
- Easier rollback if needed
- Better collaboration among team members

Example:

- Original issue: #123
- Implementation plan issue: #124 (titled "<original title>[実装計画]")
- New ticket issues: #125, #126, etc. (titled "<original title>[チケット:<specific ticket>]")

Note: Clearly reference the original issue number (#$ARGUMENTS) in all new ticket issues.