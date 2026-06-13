# Lightweight lightweight python environment
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory inside the container
WORKDIR /app

# Copy package configuration file to working directory inside container
COPY pyproject.toml /app

# Install dependencies inside the container
RUN pip install --no-cache-dir redis sqlalchemy uvicorn fastapi

# Copy the backend code
COPY backend /app/backend

EXPOSE 8000

# Run the application
CMD ["python", "-m", "uvicorn", "backend.app.main:app", "--host", "0.0.0.0", "--port", "8000"]