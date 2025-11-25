# ---- Base Image ----
FROM python:3.11-slim

# ---- Set work directory ----
WORKDIR /app

# ---- Install system dependencies (optional: curl) ----
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
 && rm -rf /var/lib/apt/lists/*

# ---- Copy project files ----
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt
COPY .env /app/.env  # Optional; remove if using cloud secrets only

# ---- Install Python dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- Expose port (only if running a server, remove if CLI only) ----
# EXPOSE 8080

# ---- Start the service ----
CMD ["python", "app.py"]
