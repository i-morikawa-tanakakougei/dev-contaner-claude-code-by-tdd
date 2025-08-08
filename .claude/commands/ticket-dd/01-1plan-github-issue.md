Please analyze and plan the implementation for the GitHub issue: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  Use `gh issue view` to get the issue details
3.  Understand the problem described in the issue
4.  Search the codebase for relevant files
5.  Plan the necessary changes to fix the issue
6.  Always create a new issue titled "<original issue title> [実装計画]" in Japanese, and apply appropriate labels (e.g., "enhancement", "bug")
7.  If no suitable label exists, create one using `gh label create`
8.  Close the original issue using `gh issue close $ARGUMENTS`

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
