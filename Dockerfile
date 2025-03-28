FROM python:3.10-slim

# Instala dependências do sistema
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Define diretório de trabalho
WORKDIR /app

# Cria e ativa ambiente virtual
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Copia requirements primeiro
COPY requirements.txt .

# Instala dependências no ambiente virtual
RUN pip install --upgrade pip \
    && pip install setuptools wheel \
    && pip install -r requirements.txt

# Copia o resto do projeto
COPY . .

# Define comando de execução
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myCrud.wsgi:application"]