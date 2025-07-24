Please review the local changes based on the GitHub issue: $ARGUMENTS.

Follow these steps:

1.  Check if `$ARGUMENTS` is provided. If `$ARGUMENTS` is not given, terminate the process immediately. When terminating, prompt the user to pass the issue number argument.
2.  Check the changes of the local branch compared with the main branch
3.  Use `gh` to get the issue details: $ARGUMENTS
4.  Understand the problem described in the issue
5.  Review the changes of the local branch
6.  Write down review feedback to `/reviews` directory in Japanese

Remember to use the GitHub CLI (`gh`) for all GitHub-related tasks.
