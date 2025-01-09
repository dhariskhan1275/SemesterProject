# Use Python 3.10 slim image
FROM python:3.10-slim

WORKDIR /app

# Copy project files
COPY requirements.txt ./
COPY main.py ./
COPY backend.py ./
COPY .env ./
COPY chromadb ./chromadb

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port (optional, for clarity)
EXPOSE 7860

# Default command
CMD ["python", "main.py"]
