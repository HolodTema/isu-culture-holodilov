.PHONY: help install install-dev run-server run-client clean

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
# here not working
	$(UVICORN) server:app --host $(HOST) --port $(PORT)

run-client: install
	$(PY) -m client

demo: install
	$(UVICORN) server:app --host $(HOST) --port $(PORT) & sleep 2 ; $(PY) -m client ; kill %1

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

