# Git Fundamentals

## Intermediate Git - 01 Working with branches

Git uses branches to systematically track multiple versions of files.

- Live system = main
- Feature development = feature

Why use branches?
- Multiple developers can work on a project simultaneously
- Compare the state of a repo between branches
- Combine contents, pushing new features to a live system
- Each branch should have a specific purpose

Listing all branches: `git branch`

Move to a branch: `git switch branch-name`

1) Add the updated file main.py to the staging area

```
git add main.py
```

2) Make a commit with the log message "Update source code"

```
git commit -m "Update source code"
```

3) In a single command, create and move to a new branch called llm-upgrade

```
git switch -c llm-upgrade
```

### Comparing branches

Show changes between:
- all unstaged files and the latest commit: `git diff`
- an unstaged file and the latest commit: `git diff report.md`
- all staged files and the latest commit: `git diff --staged`
- two commits using hashes: `git diff 35f4b4d 186398f`

Renaming a branch: `git branch -m old-name new-name`

Deleting a branch:
- which has been merged: `git branch -d branch-name`
- with pending changes: `git branch -D branch-name`

4) Change the name of the txt branch to fw2959-text-bug

```
git branch -m txt fw2959-text-bug
```

5) Forcibly delete the llm-upgrade branch from your repo

```
git branch -D llm-upgrade
```

6) Execute a command to compare the front-end and documentation branches

```
git diff front-end documentation
```

### Merging branches

Each branch should have a particular purpose:
- Developing a new feature
- Debugging an error

Once the task is complete, we incorporate the changes into production

Merging branches:
- Move to the destination branch: `git switch main`
- `git merge feature-branch`

7) Merge the ai-assistant branch into the main branch

```
git merge ai-assistant
```