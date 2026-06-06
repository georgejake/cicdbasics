# 1. Base image
FROM python:3.11-slim

# 2. Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

# 3. Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# 4. Set working directory
WORKDIR /app

# 5. Copy dependency files first (for layer caching)
COPY pyproject.toml uv.lock ./

# 6. Install dependencies (without installing the project itself)
RUN uv sync --frozen --no-install-project --no-dev

# 7. Copy the rest of the app
COPY . .

# 8. Install the project
RUN uv sync --frozen --no-dev

# 9. Expose port
EXPOSE 8000

# 10. Run the application
# Production
CMD ["uv", "run", "fastapi", "run", "src/main.py", "--host", "0.0.0.0", "--port", "8000"]