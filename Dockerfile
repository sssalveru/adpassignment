# Dockerfile, Image, Container

FROM python:3.8-alpine

WORKDIR /Deve

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app


CMD ["python", "./app/main.py"]
