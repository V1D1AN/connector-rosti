# Contributing to OpenCTI MISP Feed Connector (Rosti)

First off, thank you for considering contributing to this project! 🎉

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Pull Requests](#pull-requests)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Messages](#commit-messages)

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to the project maintainers.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues to avoid duplicates.

**When reporting a bug, include:**

- A clear and descriptive title
- Steps to reproduce the issue
- Expected behavior vs actual behavior
- Your environment (OpenCTI version, Python version, OS)
- Relevant log output
- Screenshots if applicable

**Use this template:**

```markdown
## Bug Description
A clear and concise description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What you expected to happen.

## Actual Behavior
What actually happened.

## Environment
- OpenCTI Version: [e.g., 6.0.0]
- Connector Version: [e.g., 1.0.0]
- Python Version: [e.g., 3.11]
- OS: [e.g., Ubuntu 22.04]

## Logs
```
Paste relevant logs here
```

## Additional Context
Any other context about the problem.
```

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues.

**When suggesting an enhancement, include:**

- A clear and descriptive title
- A detailed description of the proposed functionality
- Why this enhancement would be useful
- Possible implementation approach (optional)

### Pull Requests

1. **Fork the repository** and create your branch from `main`
2. **Install development dependencies**: `pip install -r requirements-dev.txt`
3. **Make your changes** following the style guidelines
4. **Add tests** if applicable
5. **Run the test suite**: `pytest tests/`
6. **Run linting**: `flake8 src/` and `black src/`
7. **Update documentation** if needed
8. **Commit your changes** with a descriptive commit message
9. **Push to your fork** and submit a pull request

## Development Setup

### Prerequisites

- Python 3.10+
- Docker (optional, for testing)
- Access to an OpenCTI instance

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/connector-rosti.git
cd connector-rosti

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements-dev.txt

# Copy configuration
cp src/config.yml.sample src/config.yml
# Edit src/config.yml with your test environment settings

# Run the connector
cd src
python main.py
```

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test file
pytest tests/test_connector.py

# Run specific test
pytest tests/test_connector.py::TestDateFiltering
```

### Code Formatting

```bash
# Format code with Black
black src/ tests/

# Sort imports with isort
isort src/ tests/

# Check linting with flake8
flake8 src/ tests/

# Type checking with mypy
mypy src/
```

## Style Guidelines

### Python Style

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://black.readthedocs.io/) for code formatting
- Use [isort](https://pycqa.github.io/isort/) for import sorting
- Maximum line length: 100 characters
- Use type hints where possible

### Documentation Style

- Use docstrings for all public functions and classes
- Follow [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html) for docstrings
- Keep README and documentation up to date

## Commit Messages

Follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

### Types

- `feat`: A new feature
- `fix`: A bug fix
- `docs`: Documentation only changes
- `style`: Code style changes (formatting, missing semi-colons, etc)
- `refactor`: Code change that neither fixes a bug nor adds a feature
- `perf`: Performance improvement
- `test`: Adding missing tests or correcting existing tests
- `chore`: Changes to build process or auxiliary tools

### Examples

```
feat(filtering): add support for custom date formats

fix(manifest): handle empty manifest response gracefully

docs(readme): update configuration table

refactor(config): simplify settings validation logic

test(dedup): add tests for UUID deduplication
```

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

Thank you for contributing! 🙏
