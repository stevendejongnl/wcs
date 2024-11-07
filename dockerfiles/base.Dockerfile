FROM python:3.13-alpine

ENV POETRY_VENV_PATH=/poetry_env
ENV POETRY_VIRTUALENVS_CREATE=false

RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-dev
RUN python3 -m venv $POETRY_VENV_PATH
RUN $POETRY_VENV_PATH/bin/pip install -U pip setuptools
RUN $POETRY_VENV_PATH/bin/pip install poetry==1.8.0
RUN ln -s $POETRY_VENV_PATH/bin/poetry /usr/bin/poetry

WORKDIR /srv

COPY pyproject.toml poetry.lock ./

RUN poetry install

