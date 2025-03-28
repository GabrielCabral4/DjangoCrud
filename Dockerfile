FROM python:3.10-slim

# Atualiza e instala dependências com mais tolerância
RUN apt-get update -y || apt-get update --fix-missing \
    && apt-get install -y --no-install-recommends \
    pkg-config \
    libcairo2-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Configura diretório de trabalho
WORKDIR /app

# Copia e instala dependências Python
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copia o resto do projeto
COPY . .

# Comando para rodar a aplicação
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]