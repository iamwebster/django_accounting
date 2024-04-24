FROM python:3.11-slim

RUN apt-get upgrade -y
RUN apt-get update && apt-get install -y dos2unix

WORKDIR /usr/src/app 

ENV PYTHONUNBUFFERED 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 8000

RUN dos2unix entrypoint.sh

ENTRYPOINT [ "sh", "entrypoint.sh" ]