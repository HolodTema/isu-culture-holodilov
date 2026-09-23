.PHONY: help install install-dev run-server run-client clean

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
UVICORN := $(VENV)/bin/uvicorn

HOST := 127.0.0.1
PORT := 8000

help:
	@echo "Welcome to fibonacci client-server app! Targets:"
	@echo ""


$(PY):
	python3 -m venv $(VENV)

install: $(PY) requirements.txt setup.py
	$(PIP) install -r requirements.txt
	$(PIP) install -e .


install-dev: install requirements-dev.txt
	$(PIP) install -r requirements-dev.txt
	
run-server: install
	$(UVICORN) fibdemo.server:app --host $(HOST) --port $(PORT)

run-client: install
	$(PY) -m client.py

clean:
	rm -rf $(VENV)

