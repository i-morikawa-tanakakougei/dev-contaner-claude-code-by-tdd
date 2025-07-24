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
6.  After creating all ticket issues, add a comment to the implementation plan issue (#$ARGUMENTS) listing all new ticket issue numbers for reference.
7.  Close the implementation plan issue (#$ARGUMENTS) as it is no longer needed after ticket breakdown.
8.  Ensure all actions are performed using the GitHub CLI (`gh`).

Example:

- Original issue: #123
- Implementation plan issue: #124 (titled "<original title>[実装計画]")
- New ticket issues: #125, #126, etc. (titled "<original title>[チケット:<specific ticket>]")

Note: Clearly reference the original issue number (#$ARGUMENTS) in all new ticket issues.
