FROM python:3.7-stretch

VOLUME ["/code"]

WORKDIR /code

COPY . /code/

RUN apt-get update && apt-get install mysql-client -y

RUN pip install -r requirements.txt

