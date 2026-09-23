# Fibonacci Client–Server Demo

Small educational project that shows how to wrap Python application into
reproducible workflow with single `Makefile` entry point.

Project has two parts. `src/server.py` is FastAPI application that
returns first `n` Fibonacci numbers on `GET /fiblist?n=…` and health
check on `GET /health`. `src/client.py` fetches sequence with `requests`,
plots it with Matplotlib, and saves result to `output/fib.png`.

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

