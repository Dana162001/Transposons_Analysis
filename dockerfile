# syntax=docker/dockerfile:1
FROM ubuntu:latest
RUN apt update &&  \
    apt upgrade -y &&  \
    apt-get update &&  \
    apt-get upgrade -y && \
    apt install python3-pip -y

WORKDIR /p_SA

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .