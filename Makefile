image:
	docker buildx build \
		--tag webcomponents-scan \
		--load \
		-f Dockerfile .

mypy:
	docker run -v ${CURDIR}:/app webcomponents-scan mypy --config-file /app/mypy.ini /app

flake:
	docker run -v ${CURDIR}:/app webcomponents-scan flake8 .

mypy-flake: mypy flake

shell:
	docker run -it -v ${CURDIR}:/app webcomponents-scan /bin/sh

check-installable:
	docker run -v ${CURDIR}:/app webcomponents-scan pip install -e .
