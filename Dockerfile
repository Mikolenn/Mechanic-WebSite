# Definimos la imagen base
FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /WebSite

ADD . /WebSite

COPY ./requirements.txt /WebSite/requirements.txt

RUN pip install -r requirements.txt

COPY . /WebSite 

EXPOSE 8000

