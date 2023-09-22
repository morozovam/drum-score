FROM python:3.10

SHELL ["/bin/bash", "-c"]

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUBBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip
RUN apt-get update && apt-get apt-get install gcc libc-dev linux-headers

COPY ./ ./

RUN pip install --no-cache-dir -r /requirements.txt
