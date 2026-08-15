# Contributing to BSERgg Rankings

First off, thank you for considering contributing to BSERgg! It's people like you that make the Brawl Stars esports community better.

## Coding Standards

To maintain consistency across the project, we follow specific standards:

### Conventional Commits
We use the [Conventional Commits](https://www.conventionalcommits.org/) specification for our commit messages:
- `feat:` for new features (e.g., adding a new game mode).
- `fix:` for bug fixes in the calculation logic.
- `refactor:` for code changes that neither fix a bug nor add a feature.
- `docs:` for documentation updates.
- `chore:` for maintenance tasks (updating dependencies, .gitignore).

### GitHub Flow
1. Fork the repository.
2. Create a new branch for your feature or fix: `git checkout -b feat/my-new-feature`.
3. Commit your changes following the conventional standards.
4. Push to the branch: `git push origin feat/my-new-feature`.
5. Open a Pull Request.

## Environment Setup
Ensure you have Python 3.10+ installed. Follow the installation steps in the `README.md` to set up your virtual environment and install dependencies via `pip install -r requirements.txt`.

## Reporting Bugs
Use the GitHub Issues tracker to report bugs. Please provide:
- A clear description of the issue.
- Sample where the rankings seemed incorrect.
- The expected vs. actual outcome.