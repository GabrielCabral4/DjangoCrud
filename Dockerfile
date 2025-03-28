FROM python:3.10-slim

WORKDIR /app

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
    libffi-dev \
    && apt-get clean

RUN pip install --upgrade pip
RUN pip install cython 
RUN pip install -r requirements.txt  

COPY . .

CMD ["python", "app.py"]
