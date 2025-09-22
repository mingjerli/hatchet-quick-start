# Multi-stage build for Python Poetry
FROM python:3.13-slim as builder

# Install Poetry
RUN pip install poetry

# Set work directory
WORKDIR /app

# Copy Poetry files
COPY pyproject.toml poetry.lock ./

# Configure Poetry to not create virtual environment
RUN poetry config virtualenvs.create false

# Install dependencies
RUN poetry install --only=main

# Production stage
FROM python:3.13-slim

# Set environment variables
ENV HATCHET_ENV=production
ENV PYTHONPATH=/app/src

# Set work directory
WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /usr/local/lib/python3.13/site-packages /usr/local/lib/python3.13/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy application code
COPY . .

# Run the worker
CMD ["python", "-c", "from src.worker import main; main()"]