# Git Fundamentals

## Introduction to Git - 02 Version History

Shows commits from newest to oldest:

```
git log

git log -3 # Restrict to the 3 most recent commits

git log report.md # To only look at the commit history of one file
```

Customizing the date range:

```
git log --since='YYYY-MM-DD' --until='YYYY-MM-DD'
```

Finding a particular commit:

```
git show "hash"
```

1) View information about the last two commits only

```
git log -2
```

2) View information about the last two commits made for report.md only

```
git log -2 report.md
```

### Comparing versions

**git diff**: Difference between versions

Compare last committed version of report.md with the version in the staging area:

```
git add report.md
git diff --staged report.md
```

State in latest commit = HEAD.

Compare second most recent (~1) with the most recent commit

git diff HEAD~1 HEAD

3) Run a command to compare the last committed version of mental_health_survey.csv against the version in the staging area

```
git diff --staged mental_health_survey.csv
```

4) Find out what changes occurred between the most recent and the second most recent commits.

```
git diff HEAD~1 HEAD
```

### Reverting files

**git revert**: Restoring a repo to the state prior to the previous commit

Revert without committing (bring files into the staging area):

git revert -n HEAD

**git revert** works on commits, not individual files. To revert a single file:

git checkout HEAD~1/HASH -- report.md

### Unstaging a file

To unstage a single file:

```
git restore --staged summary_statistics.csv
```

5) Move mental_health_survey.csv out of the staging area

```
git restore --staged summary_statistics.csv
```

6) Revert mental_health_survey.csv to the state in the last commit, using an appropriate flag to avoid opening the text editor

```
git revert --no-edit HEAD~1 mental_health_survey.csv
```