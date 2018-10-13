install:
	pip install --quiet --upgrade pip
	pip install --quiet --requirement requirements.txt

test:
	python -m pytest -vv --cov=mymusiclib tests/*.py
	python -m pytest --nbval *.ipynb


lint:
	pylint --disable=R,C mymusiclib cli web

all: install lint test
