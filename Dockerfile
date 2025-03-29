FROM python:3.10-slim

WORKDIR /app

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir --no-build-isolation PyYAML==5.4.1
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["gunicorn", "myCrud.wsgi:application", "--bind", "0.0.0.0:10000"]