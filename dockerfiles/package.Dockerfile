FROM web-components-scan-base

WORKDIR /srv

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

CMD ["poetry", "build"]
