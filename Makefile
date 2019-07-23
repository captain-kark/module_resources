clean:
	find . \( -type d -name __pycache__ -o -name .pytest_cache \) | xargs rm -r
	rm -rf .mypy_cache
	rm -rf .coverage

prereqs prerequisites:
	./scripts/setup_prerequisites.sh

tests: lint mypy bandit ftests

lint:
	python -m pylint module_resources/

mypy:
	python -m mypy module_resources/

bandit:
	python -m bandit -r .

ftests functional_tests:
	python -m pytest -vv tests/functional/

virtualenv:
	virtualenv --python=python3.7 .venv
	. .venv/bin/activate && pip install -r requirements-dev.txt

contributors:
	git log --format='%ae' | uniq > CONTRIBUTORS.txt

.PHONY: tests
