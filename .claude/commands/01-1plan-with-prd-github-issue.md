Please analyze and plan the implementation for the GitHub issue: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  Use `gh issue view` to get the issue details
3.  Understand the problem described in the issue
4.  Search the codebase for relevant files
5.  If the issue is complex or involves multiple stakeholders, create a PRD to clarify the issue's requirements, specifications, and scope. Include the following sections (as applicable):
    - Issue Overview
    - Objectives (what the issue aims to solve)
    - Functional Requirements (required features or behaviors)
    - Non-Functional Requirements (e.g., performance, security)
    - Constraints (technical or time-related)
    - Relevant Files or Code (from step 3)
    - Acceptance Criteria (definition of done)
      Review the PRD with stakeholders as needed and link it to the issue. For simple issues (e.g., minor bug fixes), document requirements directly in the issue comments or skip this step.
6.  Plan the necessary changes to fix the issue based on the PRD or issue comments.
7.  Create a new issue titled "<original issue title>[実装計画]" in Japanese using `gh issue create --title "<original issue title>[実装計画]" --body "Implementation plan for issue $ARGUMENTS"`, and apply appropriate labels (e.g., "enhancement", "bug").
8.  If no suitable label exists, create one using `gh label create`
9.  Close the original issue using `gh issue close $ARGUMENTS`

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
