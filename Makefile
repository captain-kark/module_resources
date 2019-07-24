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

preview-deployment:
	python setup.py sdist
	python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/module-resources-0.0.$(TRAVIS_BUILD_NUMBER).tar.gz

virtualenv:
	virtualenv --python=python3.7 .venv
	. .venv/bin/activate && pip install -r requirements-dev.txt && pip install -r requirements-publish.txt

contributors:
	git log --format='%ae' | uniq > CONTRIBUTORS.txt

tag-%:
	git tag -a $(shell ./scripts/bump_tag.py $(subst tag-,,$@))

.PHONY: tests
