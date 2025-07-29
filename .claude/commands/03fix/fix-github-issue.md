Please analyze and fix the GitHub issue: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  **Check the current branch**:

    - Verify that the current branch is neither `main` nor `master`, but a feature branch (e.g., `feature/*`).
    - If the current branch is `main` or `master`, terminate the process and prompt the user to create and switch to a new feature branch.
    - Suggest a branch name based on the issue number and title (e.g., `feature/issue-$ISSUE_NUMBER-$SHORT_TITLE`).
    - Provide instructions to create and switch to the branch using `git checkout -b <branch-name>`.

3.  Use `gh issue view` to get the issue details.
4.  Understand the problem described in the issue.
5.  Search the codebase for relevant files.
6.  Implement the necessary changes to fix the issue.
7.  Write and run tests to verify the fix.
8.  Ensure code passes linting and type checking.
9.  Create a descriptive commit message.

**Example prompt for invalid branch**:

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
