FROM python:3.12-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

COPY ./src .
COPY ./pyproject.toml .
COPY ./uv.lock .

RUN uv sync

EXPOSE 8000
CMD ["uv", "run", "fastapi", "run"]
