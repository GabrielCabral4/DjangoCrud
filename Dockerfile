FROM python:3.10-slim

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools==58.0.4 wheel cython
RUN pip install numpy==1.24.4
RUN pip install django==5.1.7
RUN pip install gunicorn==23.0.0
RUN pip install psycopg2-binary==2.9.10

WORKDIR /app

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install pyyaml==5.4.1

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
    cython \
    && apt-get clean

COPY . .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myCrud.wsgi:application"]
