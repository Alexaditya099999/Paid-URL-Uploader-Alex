FROM python:3.10-slim-bookworm

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    aria2 \
    ffmpeg \
    wget \
    curl \
    unzip \
    p7zip-full \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Create necessary directories (for Railway volumes)
RUN mkdir -p /app/data /app/downloads /app/temp

# Give execution rights to scripts if any
RUN find /app -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true
RUN chmod +x /app/binary/linux/* 2>/dev/null || true

# Expose port if needed
EXPOSE 8080

# Start command
CMD ["python", "main.py"]
