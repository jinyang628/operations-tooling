# Operations Tooling Server

## Install Poetry

It is recommended to use Python virtual environment, so you don't pollute your system Python environment.

```bash
# Install dependencies
poetry install
```

```bash
# Activate Python Virtual Environment for Mac/Linux
eval "$(poetry env activate)"

# Activate Python Virtual Environment for Windows
.venv\Scripts\Activate.ps1
```

## Configure VSCode Python Interpreter to use Poetry's virtual environment

1. Close VSCode so that it is able to detect the newly created virtual environment. A lot of times, this alone is enough to fix the issue.
2. In the command palette, type `Python: Select Interpreter`
3. Type `poetry` in the search box
4. The first option should be what you want to use

## Set up environment variables

```bash
# Create .env file (by copying from .env.example)
cp .env.example .env
```

## Style Enforcement

```bash
black . # Check Python code style
isort . # Sort Python imports
```

## Quick Start

To spin up the server, run the following command at the `server` directory:

```bash
uvicorn app.api.main:app --reload --host 0.0.0.0 --port 8080 --env-file .env
```
