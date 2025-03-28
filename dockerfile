FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    pkg-config \
    libcairo2-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia os arquivos do projeto para o container
COPY . /app

# Atualiza o pip e instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define a variável de ambiente para o Django (ajuste conforme necessário)
ENV DJANGO_SETTINGS_MODULE=myCrud.settings

# Expõe a porta que o Render irá usar (Render define a variável $PORT)
EXPOSE $PORT

# Comando para iniciar a aplicação (exemplo usando gunicorn)
CMD gunicorn myCrud.wsgi:application --bind 0.0.0.0:$PORT
