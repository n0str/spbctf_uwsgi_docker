FROM debian:stretch-slim

WORKDIR /home/web

RUN apt-get update && \
    apt-get -y install socat python3 python3-pip

COPY requirements.txt .
RUN pip3 install -r /home/web/requirements.txt