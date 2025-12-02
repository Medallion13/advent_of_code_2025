POETRY = poetry run
PYTHON = $(POETRY) python
PYTEST = $(POETRY) pytest
RUFF = $(POETRY) ruff
MYPY = $(POETRY) mypy

.PHONY: help test lint format typecheck check clean install
# Default target
help:
	@echo "Available commands:"
	@echo "  make install     - Install dependencies"
	@echo "  make test        - Run all tests"
	@echo "  make lint        - Run linting (ruff)"
	@echo "  make format      - Format code (ruff)"
	@echo "  make typecheck   - Run type checking (mypy)"
	@echo "  make check       - Run all checks (lint + typecheck + test)"
	@echo "  make clean       - Remove cache files"

install:
	poetry install
	@echo "Dependecies installed"

test:
	$(PYTEST)
	@echo "All test passed"

lint:
	$(RUFF) check .
	@echo "Linting passed"

format:
	$(RUFF) format .
	$(RUFF) check . --fix
	@echo "Code formatted"

typecheck:
	$(MYPY) .
	@echo "Type checking passed"

check: format lint typecheck test
	@echo "All checks passed"

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	find . -type f -name ".coverage" -delete
	@echo "Cache cleaned"
