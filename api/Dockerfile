FROM python:3.14-slim

COPY --from=ghcr.io/astral-sh/uv:0.13.8 /uv /uvx /bin/

WORKDIR /code/api

COPY ./uv.lock ./uv.lock
COPY ./pyproject.toml ./pyproject.toml

COPY ./ .

RUN uv sync

ENV PATH=${PATH}:/code/api/.venv/bin

CMD ["fastapi", "dev", "src/api/main.py", "--port", "8080", "--host", "0.0.0.0"]
# CMD ["uv", "run" "fastapi", "dev", "--port", "8080"]
