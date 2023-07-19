.PHONY: clean-pyc clean-build docs clean

# Browser Tools
define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"
VERSION := $$(cat VERSION)

help:
	@echo "clean - remove all build, test, coverage and Python artifacts"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test and coverage artifacts"
	@echo "lint - check style with flake8"
	@echo "test - run tests quickly with the default Python"
	@echo "test-all - run tests on every Python version with tox"
	@echo "coverage - check code coverage quickly with the default Python"
	@echo "dist - package"
	@echo "install - install the package to the active Python's site-packages"

# unit test
test: clean
	pytest

test-cov: clean
	pytest --cov=uspeedo/core tests

test-cov-html:
	pytest --cov=uspeedo/core tests --cov-report html
	$(BROWSER) htmlcov/index.html

test-acc: clean
	USDKACC=1 pytest --cov=uspeedo

test-all: clean
	tox

lint:
	@flake8 --exclude=uspeedo/services uspeedo --ignore=E501,F401

fmt:
	@black -l 80 `find uspeedo tests examples -name "*.py"`

dev:
	@pip install -e .[dev]

clean: clean-build clean-pyc clean-test

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

build:
	echo "version = \"$(VERSION)\"" > uspeedo/version.py
