.PHONY: help install install-dev run-server run-client clean demo lint typecheck check-requirements check

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
UVICORN := $(VENV)/bin/uvicorn

HOST := 127.0.0.1
PORT := 8000

help:
	@echo "Welcome to fibonacci client-server app! Targets:"
	@echo "  install             Create .venv, install runtime dependencies, install the package in editable mode"
	@echo "  install-dev         Do the same as install, plus dev tools (ruff, mypy, types-requests)"
	@echo "  run-server          Start the FastAPI server with uvicorn on $(HOST):$(PORT)"
	@echo "  run-client          Run the client (the server must be running)"
	@echo "  demo                Start the server in the background, build the plot, then stop the server"
	@echo "  lint                Check code style with ruff (no files are changed)"
	@echo "  typecheck           Run static type checking with mypy"
	@echo "  check-requirements  Make sure every import is listed in the requirements files"
	@echo "  check               Run typecheck, lint and check-requirements together"
	@echo "  clean               Remove .venv, tool caches and the output/ folder"

$(PY):
	python3 -m venv $(VENV)

install: $(PY) requirements.txt setup.py
	$(PIP) install -r requirements.txt
	$(PIP) install -e .


install-dev: install requirements-dev.txt
	$(PIP) install -r requirements-dev.txt
	
run-server: install
	$(VENV)/bin/fib-server

run-client: install
	$(VENV)/bin/fib-client

demo: install
	$(VENV)/bin/fib-demo

lint: install-dev
	$(PY) -m ruff check src scripts

typecheck: install-dev
	$(PY) -m mypy src

check-requirements: install-dev
	$(PY) scripts/check_requirements.py

check: typecheck lint check-requirements
	@echo "All the checks are passed!"

clean:
	rm -rf $(VENV) output 

