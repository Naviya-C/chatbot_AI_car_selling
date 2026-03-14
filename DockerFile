FROM python:3.12-slim

WORKDIR /app

# Install system dependencies for pyodbc
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    unixodbc-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Pre-download embedding model
RUN python -c "from sentence_transformers import SentenceTransformer; SentenceTransformer('all-MiniLM-L6-v2')"

# Expose API port
EXPOSE 8000

# Run FastAPI
CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8000"]
