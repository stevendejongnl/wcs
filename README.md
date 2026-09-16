# Web Components Scan

WCS is a Python application that scans HTML files within a specified directory based on the `@custom-elements-manifest/analyzer` npm package.
This npm packages generates a `custom-elements.json` file containing information about custom HTML tags.
With this file we can scan html files for implementations.

# Installation
Clone this repository to your local machine.

Dependencies are managed with [uv](https://docs.astral.sh/uv/). Install them with:
```bash
uv sync
```

# Usage
Run the analyzer script with the following command:
```bash
uv run python main.py --scan-path <path_to_directory> --manifest-path <path_to_manifest>
```

Replace `<path_to_directory>` with the path to the directory containing your HTML files.
And `<path_to_manifest>` with the path to your `custom-elements.json`.

Or run it via the published Docker image:
```bash
docker run --rm -v "$PWD":/data stevendejong/wcs --scan-path /data --manifest-path /data/custom-elements.json
```

# Development
```bash
make sync   # install dependencies
make test   # run the test suite
make lint   # run mypy + flake8
```

# Releases
Versioning, changelogs, PyPI and Docker Hub publishing are automated with
[python-semantic-release](https://python-semantic-release.readthedocs.io/), driven by
[Conventional Commits](https://www.conventionalcommits.org/) on `main` (`fix:`, `feat:`,
`feat!:`/`BREAKING CHANGE:`, etc.). Merging a commit with a release-worthy prefix to `main`
triggers `.github/workflows/release.yaml`, which bumps the version, tags the release, and
publishes the package to PyPI and the image to Docker Hub as `stevendejong/wcs:<version>`
and `stevendejong/wcs:latest`.

# License
This project is licensed under the MIT License - see the LICENSE file for details.
