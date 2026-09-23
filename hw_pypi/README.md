# Fibonacci Client–Server Demo

Small educational project that shows how to wrap Python application into
reproducible workflow with single `Makefile` entry point.

Project has two parts. `src/fibapp/server.py` is FastAPI application that
returns first `n` Fibonacci numbers on `GET /fiblist?n=…` and health
check on `GET /health`. `src/fibapp/client.py` fetches sequence with `requests`,
plots it with Matplotlib, and saves result to `output/fib.png`.

## How to install from test.pypi.org

This project uses FastAPI, but test.pypi contains only fake-FastAPI package. That is why we need
to use --extra-index-url flag to persuade pip searching dependencies not only in test.pypi, but 
also in pypi.

Also only version 0.0.3 is correct. If pip tries to reduce the version of the library - it is no
use. That is why we say certain version fibap==0.0.3

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ fibapp==0.0.3
```

After successful installation, you can use fibapp CLI

## fibapp CLI

fibapp is not a classic library, it is CLI-application from test.pypi.

After installation you can use these commands in terminal:

```bash
# to run only server without client. It is like `make run-server` command
fib-server

# to run only client without server. It is like `make run-client` command
fib-client

# to run server and client together. It is like `make demo` command
fib-demo
```

## Goals

- Keep all source code under `src/` and install it in editable mode.

- Manage virtual environment without relying on `source activate`, which
  does not survive between Make recipe lines.

- Provide single entry point (`make`) for installation, running,
  linting, type checking and dependency verification.

- Show that `make` composes actions: `check` target depends on several
  smaller targets.

- Keep repository clean after run — `git status` must show no changes.

## Targets

- `install` — creates `.venv`, installs runtime deps, installs project
  in editable mode.
- `install-dev` — same as `install`, plus `ruff` and `mypy`.
- `run-server` — starts FastAPI server on `127.0.0.1:8000`.
- `run-client` — runs client (server must be running).
- `demo` — starts server in background, runs client, kills server.
- `lint` — `ruff check src scripts`, check only, no changes.
- `typecheck` — `mypy src`.
- `check-requirements` — verifies that every import is declared in
  `requirements.txt`.
- `check` — runs `typecheck`, `lint` and `check-requirements`.
- `clean` — removes `.venv` and `output/`.

## How to verify

From fresh clone:

```bash
make clean
make install-dev
make check
make demo
git status
```

## Used technologies

- FastAPI
- requests
- matplotlib
- make
- mypy
- ruff

## Links

- TestPyPI: https://test.pypi.org/project/fibapp/
- Repository: https://github.com/HolodTema/isu-culture-holodilov/tree/feature/hw/pypi

