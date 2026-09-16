FROM ghcr.io/astral-sh/uv:python3.13-alpine AS build

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project

COPY . .
RUN uv sync --locked --no-dev

FROM python:3.13-alpine

WORKDIR /app

COPY --from=build /app /app

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["python", "./main.py"]
