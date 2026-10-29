# Commit messages for Pharma-main

Run these inside the project folder. The first block makes sure your commits are
credited to the right GitHub account.

```sh
git init -b main
git config user.name "sowjanya-m025"
git config user.email "sowjanyamurgesh04@gmail.com"
```

## Commits

```sh
git add .gitignore
git commit -m "chore: add gitignore"

git add requirements.txt config
git commit -m "chore: add dependencies and settings file"

git add data reports
git commit -m "feat(data): add mock datasets and sample reports"

git add utils
git commit -m "feat(utils): add data loader, logger, summarizer and safe PDF report generator"

git add agents
git commit -m "feat(agents): add IQVIA, clinical, patent, EXIM, internal and web agents"

git add tools
git commit -m "feat(tools): add mock lookup tools for trials, patents, trade and market data"

git add master_agent.py app.py
git commit -m "feat: add master agent and Streamlit UI with empty-input check"

git add tests
git commit -m "test: add unit tests that run without Ollama"

git add README.md COMMIT_MESSAGES.md
git commit -m "docs: add README and commit message guide"
```

## Push

Create an empty repo on GitHub first, then:

```sh
git remote add origin https://sowjanya-m025@github.com/sowjanya-m025/<repo-name>.git
git push -u origin main
```

Use a Personal Access Token as the password.
