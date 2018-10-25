FROM python:3.6-stretch

ENV PYTHONUNBUFFERED 1

VOLUME ["/code"]

WORKDIR /code

COPY . /code/

EXPOSE 8000

RUN apt-get update && apt-get install mysql-client -y

RUN pip install -r requirements.txt
