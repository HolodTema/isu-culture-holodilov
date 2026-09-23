FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock ./
# --only flag means to install only prod-dependencies, not dev-dependencies
#
# --no-root means not to install current project as pip package
# (by default poetry makes pip install -e (editable mode) for current project)
RUN pip install poetry && poetry install --only main --no-root

COPY src/app ./app

CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

