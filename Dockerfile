FROM python:3.10-slim

RUN pip install --upgrade pip setuptools wheel cython

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-cffi \
    python3-venv \
    python3-distutils \
    python3-yaml \
    && apt-get clean \
    && pip install --upgrade pip \
    && pip install --upgrade "setuptools==58.0.4" "wheel" "cython" \
    && pip install numpy==1.24.4 \
    && pip install django==5.1.7 \
    && pip install gunicorn==23.0.0 \
    && pip install psycopg2-binary==2.9.10 \
    && pip install -r requirements.txt




COPY . .

# Comando de execução
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myCrud.wsgi:application"]