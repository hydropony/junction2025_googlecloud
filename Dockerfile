FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code and data needed for the substitution service
COPY services ./services
COPY Data ./Data
COPY Docs ./Docs
COPY analysis ./analysis
COPY training ./training

EXPOSE 8000

# Default DB connection (points to warehouse-db postgres via host.docker.internal:6000 on Docker Desktop)
ENV WAREHOUSE_DB_HOST=host.docker.internal
ENV WAREHOUSE_DB_PORT=6000
ENV WAREHOUSE_DB_NAME=warehouse
ENV WAREHOUSE_DB_USER=warehouse_user
ENV WAREHOUSE_DB_PASSWORD=warehouse_pass

CMD ["uvicorn", "services.substitution_service.main:app", "--host", "0.0.0.0", "--port", "8000"]


