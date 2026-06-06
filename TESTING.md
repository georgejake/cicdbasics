# Unit Testing Guide

This project includes unit tests to ensure code quality before merging. All tests must pass before code can be merged to the main branch.

## Running Tests Locally

### Setup
First, install the test dependencies:

```bash
pip install -e ".[test]"
```

### Run All Tests
Execute all tests with pytest:

```bash
pytest
```

### Run Tests with Coverage Report
See code coverage metrics:

```bash
pytest --cov=src --cov-report=html --cov-report=term-missing
```

This generates an HTML coverage report in `htmlcov/index.html`.

### Run Specific Test File
```bash
pytest tests/test_main.py
```

### Run Specific Test Class or Function
```bash
pytest tests/test_main.py::TestRootEndpoint
pytest tests/test_main.py::TestRootEndpoint::test_read_root_status_code
```

### Run Tests in Verbose Mode
```bash
pytest -v
```

## Test Structure

- **conftest.py**: Contains shared fixtures, including the `client` fixture that provides a TestClient for FastAPI
- **test_main.py**: Contains all endpoint tests organized into test classes

## Before Merging

Make sure to:
1. Run all tests locally: `pytest`
2. Ensure all tests pass with no failures
3. Check code coverage is acceptable: `pytest --cov=src`
4. Fix any failing tests before pushing

## CI/CD Integration

Tests are automatically run in GitHub Actions before merge. See `.github/workflows/` for CI/CD pipeline configuration.
