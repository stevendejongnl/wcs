image:
	docker buildx build \
		--tag web-components-scan \
		--load \
		-f Dockerfile .

sync:
	uv sync

test:
	uv run pytest

mypy:
	uv run mypy --config-file mypy.ini .

flake:
	uv run flake8 .

mypy-flake: mypy flake

lint: mypy-flake
