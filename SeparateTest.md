name: Tests - Unit Tests

on:
  push:
    branches:
      - develop
      - main
  pull_request:
    branches:
      - develop
      - main

jobs:
  test:
    name: Run Unit Tests
    runs-on: ubuntu-latest

    steps:
      # Step 1: Checkout code
      - name: Checkout code
        uses: actions/checkout@v4

      # Step 2: Set up Python
      - name: Set up Python 3.11
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      # Step 3: Install dependencies
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[test]"

      # Step 4: Run tests
      - name: Run tests
        run: pytest -v

      # Step 5: Generate coverage report
      - name: Generate coverage report
        run: pytest --cov=src --cov-report=xml --cov-report=term-missing

      # Step 6: Upload coverage to Codecov (optional)
      - name: Upload coverage to Codecov
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
          fail_ci_if_error: false
