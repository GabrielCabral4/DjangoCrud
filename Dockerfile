FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    pkg-config \
    libcairo2-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt -v --no-cache-dir || \
    (echo "Erro na instalação de dependências" && cat requirements.txt && pip list && exit 1)

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]