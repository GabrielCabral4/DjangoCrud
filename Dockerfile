FROM python:3.10-slim

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install --upgrade setuptools wheel \
    && pip install numpy==2.2.3 \
    && pip install django==5.1.7 \
    && pip install gunicorn==23.0.0 \
    && pip install psycopg2-binary==2.9.10 \
    && pip install -r requirements.txt \
    || (echo "Erro na instalação de dependências" \
    && pip list \
    && python --version \
    && exit 1)

COPY . .

# Comando de execução
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myCrud.wsgi:application"]