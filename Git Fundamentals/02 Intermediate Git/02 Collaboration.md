# Git Fundamentals

## Intermediate Git - 02 Collaborating with Git

### Introduction to remotes

Local repo vs Remote repo

Benefits of remote repos:
- Everything is backed up
- Collaboration, regardless of location

### Cloning a repo

Repo copies on our local computer = local remotes

- Cloning local repo: `git clone <local-path-to-project-repo>`
- Clone remote repo: `git clone <URL-remote>`

### Creating a remote

When cloning, Git will automatically name the remote origin: `git remote add <remote-name> <URL-remote>`

1) Clone /home/repl/datacamp in your current directory

```
git clone /home/repl/datacamp
```

2) Add the name back-up for the /home/repl/datacamp repo

```
git remote add back-up /home/repl/datacamp
```

3) List all remotes including their URL

```
git remote -v
```

### Fetching from a remote

Fetch from the origin remote: `git fetch origin`

Doesn't merge the remote's contents into local repo

### Synchronizing content

Merge origin remote's default branch into the local repo's current branch: `git merge origin`

### Pulling from a remote

Fetch and merge from the remote's default: `git pull origin`

4) Run a command to find out the name(s) of remote repos linked to your project

```
git remote
```

5) Fetch from the remote origin repo into your local main branch

```
git fetch origin
```

6) Pull the remote origin repo's front-end branch into your current local branch

```
git pull origin front-end
```

7) Compare origin's main branch with your local branch

```
git diff origin main
```

### Pushing to a remote

Push into remote from local_branch: `git push remote-branch-name local_branch-name`

### Pushing a new local branch

Working in hotfix branch locally. hotfix does not exist in the remote.

```
git push origin hotfix
```

8) Push your local documentation branch to the origin remote repo.

```
git push origin documentation
```