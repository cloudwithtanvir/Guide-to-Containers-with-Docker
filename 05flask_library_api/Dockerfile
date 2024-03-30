# Use the official Python base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libsqlite3-dev

# Install Poetry
RUN pip install poetry

# Copy only the poetry.lock and pyproject.toml to install dependencies
COPY pyproject.toml ./

# Install dependencies
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-interaction --no-ansi

# Copy the FastAPI application code into the container
COPY 05flask_library_api ./05flask_library_api

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
CMD ["uvicorn", "05flask_library_api.main:app", "--host", "0.0.0.0", "--port", "8000"]
