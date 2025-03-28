FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt  

COPY . .

CMD ["gunicorn", "myCrud.wsgi:application", "--bind", "0.0.0.0:$PORT"]