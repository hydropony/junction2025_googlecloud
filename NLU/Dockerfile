FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
  && rm -rf /var/lib/apt/lists/*

WORKDIR /app/NLU

COPY NLU/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY NLU /app/NLU
COPY Data /app/Data

ENV PYTHONPATH=/app/NLU

EXPOSE 6060

CMD ["python", "app.py"]


