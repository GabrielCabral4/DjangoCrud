FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    libcairo2-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt || \
    (pip list && exit 1)

COPY . .

ENV DJANGO_SETTINGS_MODULE=myCrud.settings

EXPOSE $PORT

CMD gunicorn myCrud.wsgi:application --bind 0.0.0.0:$PORT
