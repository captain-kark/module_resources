clean:
	find . \( -type d -name __pycache__ -o -name .pytest_cache \) | xargs rm -r
	rm -rf .mypy_cache
	rm -rf .coverage

prereqs prerequisites:
	./scripts/setup_prerequisites.sh

tests: lint ftests mypy bandit ftests

make test-%:
	. .venv/bin/activate && python -m $(subst test-,,$@) module_resources/

lint: test-pylint
mypy: test-mypy
bandit: test-bandit\ -r

ftests functional_tests:
	. .venv/bin/activate && python -m pytest -vv tests/functional/

virtualenv:
	virtualenv --python=python3.7 .venv
	. .venv/bin/activate && pip install -r requirements-dev.txt

.PHONY: tests
