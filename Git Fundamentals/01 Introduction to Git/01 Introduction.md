# Git Fundamentals

## Introduction to Git - 01 Intro

Version control can:
- Track files in different states
- Combine different versions of files
- Identify a particular version
- Revert changes

Useful terminal commands:
- pwd
- ls
- cd

### Creating repos

Git repo = directory containing files and sub-directories

Benefits of repos:
- Systematically track versions
- Revert to previous versions
- Compare versions at different points in time
- Collaborate with colleagues

To create a new repo from scratch:

```
git init repo-name
cd repo-name
git status
```

Don't create a Git repo inside another Git repo > Known as nested repos!

### Staging and committing files

1. Edit and save files on our computer
2. Add the file(s) to the Git staging area
    - Tracks what has been modified
3. Commit the files
    - Git takes a snapshot of the files at the point in time
    - Allows us to compare and revert files

### Adding to the staging area

Adding a single file:

```
git add README.md
```

Adding all modified files:

```
git add .
```

### Making a commit

```
git commit -m "Adding a README."
```