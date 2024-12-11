FROM python:3.12

WORKDIR /app

COPY requirements.txt .
COPY init.py .
COPY ./app .

RUN pip install -r requirements.txt

RUN python3 init.py







