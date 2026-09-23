FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    DEBIAN_FRONTEND=noninteractive

# ---------- System dependencies ----------
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

# ---------- Python dependencies ----------
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ---------- Baaki code copy ----------
COPY . .

# ---------- Railway Volume ke liye folders ----------
RUN mkdir -p /app/data /app/downloads /app/temp

# ---------- Executable permissions ----------
RUN find /app -type f -name "*.sh" -exec chmod +x {} \; 2>/dev/null || true
RUN chmod +x /app/binary/linux/* 2>/dev/null || true

# ---------- Railway PORT (agar web server ho) ----------
EXPOSE 8080

# ---------- Start command ----------
CMD ["python", "main.py"]
