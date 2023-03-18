install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install dist/*.whl --force-reinstall

make lint:
	poetry run flake8 brain_games

make bpp:
	poetry build
	poetry publish --dry-run
	python -m pip install dist/*.whl --force-reinstall