# Every BaseCamp project has the same four commands: fmt, lint, test and check.
# The language plug-in's recipes follow.

fmt:
    uv run ruff format

lint:
    uv run ruff check

test:
    uv run pytest

# Checks everything without changing anything.
check:
    uv run ruff format --check
    uv run ruff check
    uv run pytest
