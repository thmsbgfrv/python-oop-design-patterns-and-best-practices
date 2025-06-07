# Advanced Python Patterns & Practices

[![Build Status](https://github.com/thmsbgfrv/python-study/actions/workflows/checkup.yaml/badge.svg)](https://github.com/thmsbgfrv/python-study/actions/workflows/checkup.yaml)
![Latest Release](https://img.shields.io/badge/version-0.3.8-green)
![License](https://img.shields.io/badge/license-GPL%20v3-yellow)
![Python](https://img.shields.io/badge/python-3.12%2B-blue)

## Overview

**Advanced Python Patterns & Practices** is a comprehensive codebase focused on modern Python development and best practices. This repository demonstrates advanced design patterns, idiomatic object-oriented programming, and clean code principles tailored for professional software engineering.

## Features

- Real-world implementations of major design patterns (Creational, Structural, Behavioral)
- Modular and readable code structure
- Automated testing with Pytest for reliability
- Poetry-managed dependencies and modern dev tooling
- Pre-configured CI/CD workflows with GitHub Actions
- Docker-based development environment

## Project Structure

```
.
├── src/                 # Core source code
│   ├── oop/             # Object-oriented patterns/examples
│   └── advance/         # Advanced Python concepts
├── tests/               # Unit and integration tests
├── .github/             # GitHub workflow configs
├── .devcontainer/       # Dev container setup for VS Code
├── pyproject.toml       # Project config and dependencies
├── poetry.lock          # Poetry lockfile
└── README.md            # Project documentation
```

## Getting Started

### Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/) (for dependency management)

### Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/thmsbgfrv/python-study.git
cd python-study
poetry install
```

(Optional) For a pre-configured development environment, open the project in VS Code with Dev Containers.

### Running Tests

```bash
poetry run pytest
```

### Code Quality & Linting

```bash
poetry run pre-commit run --all-files
poetry run black .
poetry run isort .
poetry run flake8 .
poetry run pylint .
poetry run mypy .
```

## Usage

Explore the `src/` directory for well-documented code samples and pattern implementations. Each module is independently testable and includes usage examples in the `tests/` directory.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the GPL v3 License.
