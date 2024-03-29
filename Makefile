install:
	poetry install

lint:
	poetry run flake8

selfcheck:
	poetry check

build:
	poetry build

packege-install:
	pip install --user dist/*.whl

.PHONY: install lint selfcheck build
