base-image:
	docker buildx build --file dockerfiles/base.Dockerfile --no-cache . --tag web-components-scan-base

base-shell:
	docker run -it -v ${CURDIR}:/app web-components-scan-base /bin/sh

package-image:
	docker buildx build --file dockerfiles/package.Dockerfile --no-cache . --tag web-components-scan-package

package-shell:
	docker run -it -v ${CURDIR}:/app web-components-scan-package /bin/sh

image:
	docker buildx build \
		--tag web-components-scan \
		--load \
		-f Dockerfile .

mypy:
	docker run -v ${CURDIR}:/app web-components-scan mypy --config-file /app/mypy.ini /app

flake:
	docker run -v ${CURDIR}:/app web-components-scan flake8 .

mypy-flake: mypy flake
