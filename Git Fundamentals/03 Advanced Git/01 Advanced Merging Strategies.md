# Git Fundamentals

## Advanced Git - 01 Advanced Merging Strategies

Git Merge Command: `git merge`
- Combines changes from one branch into another
- Finds the common base between two branches
- Use **different merge strategies**

### Fast-forward merge

- Keep a simple, straight history
- Ideal for short-lived branches with simple changes

Git Merge has Fast Forward as **Default**.

Force Git Merge Fast Forward: `git merge <branch> --ff-only`

### Recursive merge

- Creates a merge commit **with two parents**
- **Preserve the entire project history**
- Ideal for long-lived branches
- Maintain branching structure

Recursive Merge Command: `git merge --no-ff <branch>`

Summary:
- Fast forward merges keeps history simple and linear
- Recursive merges preserves historical context
- Recursive merges are better for more complex development

1) Write the Git command to ensure that a fast-forward merge is performed while merging the data-validation branch into the main branch

```
git merge data-validation --ff-only
```

2) Write the Git command to perform a recursive merge of the etl-update branch into the main branch, forcing a merge commit

```
git merge --no-ff etl-update
```

### Git squash merging

Simplifies history, **combines multiple commits into one**. Use squash merges for a clean, simplified history.

- Creates a single new commit on the target branch
- Combines all changes from the source branch
    - Adds a regular commit with one parent (unlike recursive strategy)
- Added to target branch (not feature branch)
    - Doesn't preserve the detailed commit history of the source branch

- Checkout the main branch: `git checkout main`
- Create a squash commit of all feature-branch changes: `git merge --squash feature-branch`
- Commit the squash commit to main branch history: `git commit -m "Implement and optimize data cleanup"`

### Git octopus merge

- Merges **three or more branches at once**
- Creates a single merge commit with multiple parents
- Best used when branches don't conflict with each other

Git Octopus Merge Command: `git merge -s octopus branch1 branch2 branch3`

3) You've been working on a feature branch called data-cleanup with multiple commits. You want to merge these changes into the main branch as a single, clean commit.

```
git merge --squash data-cleanup
git commit -m "Integrate data-cleanup feature"
```

4) You're working on a data pipeline project where three independent feature branches (ingest, transform, and load) need to be merged into the main branch simultaneously.

```
git merge -s octopus ingest, transform, load
```

### Git Rebasing

- Method to integrate changes
- Different from merge
- Removes merge commits for a cleaner history
- Maintains a linear commit graph for clarity

- Checkout your data-cleanup feature branch: `git checkout data-cleanup`
- Rebase main branch onto data-cleanup branch: `git rebase main`

5) You decide to use interactive rebase to combine your commits into a single, comprehensive commit that clearly describes all the changes made for a feature.

```
git log -2
git rebase -i HEAD~2
```

6) While you were working on your feature branch feature_transform, a colleague pushed an update to the data ingestion function on the main branch to accommodate a new data source. To keep your feature branch up-to-date and maintain a clean project history, you need to rebase your changes on top of the latest main branch.

In a single command, review the last three commits in the log on themain branch.

```
git log main -3
```

Review the last 3 commits on the feature_transform branch using git log.

```
git log -3
```

Rebase the main branch onto feature_transform branch

```
git rebase main
```