Please analyze and update the GitHub issue: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  Use `gh issue view` to get the issue details
3.  Understand the problem described in the issue
4.  BE EXTRA CAREFUL with the word "＜再検討＞". You should ALWAYS update this placeholder to rethink the plan
5.  Search the codebase for relevant files
6.  Plan the necessary changes to fix the issue
7.  ALWAYS update the existing issue $ARGUMENTS. NEVER create a new issue.

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
