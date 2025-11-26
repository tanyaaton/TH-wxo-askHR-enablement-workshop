# ---- Base Image ----
FROM python:3.11-slim

# ---- Set Work Directory ----
WORKDIR /app

# ---- Install OS Dependencies ----
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# ---- Copy Project Files ----
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# ---- Expose Port ----
EXPOSE 8000

# # ---- Environment Variables Placeholders ----
# # (These will be overridden by cloud deployment environment settings)
# ENV ASTRA_TOKEN=""
# ENV ORG_ID=""

# ---- Start the FastAPI Service ----
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
