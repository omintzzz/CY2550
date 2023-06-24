# Makefile for Python project

# Variables
PYTHON = python
PIP = pip

# Targets
.PHONY: install run clean

install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) xkcdpwgen.py

clean:
	rd /s /q __pycache__
