# 13. Git and GitHub

## What is Git?
Git is a version control system. It remembers the state of your code at any moment (like game saves).

**`git init`** — creates a new repository (a `.git` folder) in the current project.

```bash
git init
```

**`git add .`** — stages all changed files for the next save.

```bash
git add .
```

**`git commit -m 'message'`** — saves changes with a comment.

```bash
git commit -m 'First commit'
```

## GitHub
GitHub is a cloud website for storing such repositories.

**`git push`** — sends your commits to GitHub.

```bash
git push origin main
```

**`git pull`** — downloads changes from GitHub to your computer.

```bash
git pull
```

## 📌 Remember

| What | Command |
|---|---|
| Create repo | `git init` |
| Stage files | `git add .` |
| Save | `git commit -m 'msg'` |
| Push to GitHub | `git push origin main` |
| Pull changes | `git pull` |
| History | `git log --oneline` |
| Undo changes | `git restore file` |