# Contributing to BSERgg Rankings

First off, thank you for considering contributing to BSERgg! It's people like you that make the Brawl Stars esports community better.

## Coding Standards

To maintain consistency across the project, we follow specific standards:

### Conventional Commits
We use the [Conventional Commits](https://www.conventionalcommits.org/) specification for our commit messages:
- `feat:` for new features to the codebase.
- `fix:` for bug fixes in the code.
- `refactor:` for code changes that neither fix a bug nor add a feature.
- `docs:` for documentation updates and additions.
- `chore:` for maintenance tasks (updating dependencies, adding auxiliary tools).
- `style`: for code style changes, formatting, without altering logic. 
- `BREAKING CHANGE`: for changes that make the previous version incompatible with the current one.

### GitHub Flow
1. Fork the repository.
2. Create a new branch for your feature or fix: `git checkout -b feat/my-new-feature`.
3. Commit your changes following the conventional standards.
4. Push to the branch: `git push origin feat/my-new-feature`.
5. Open a Pull Request.

## Environment Setup
Ensure you have Python 3.7+ installed. Follow the installation steps in the `README.md` to set up your virtual environment and install dependencies via `winget install Python.Python.3.7`.

## Reporting Bugs
Use the GitHub Issues tracker to report bugs. Please provide:
- A clear description of the issue.
- Sample where the rankings math seemed incorrect.
- The expected vs. actual outcome.