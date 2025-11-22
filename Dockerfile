# Dockerfile
FROM ghcr.io/astral-sh/uv:latest AS base

# Set working directory
WORKDIR /app
COPY pyproject.toml .


RUN ["git", "clone", "--depth=1", "https://github.com/pratyay360/search-api.git"]
RUN ["uv", "pip", "install", "--from-requirements", "pyproject.toml"]
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]