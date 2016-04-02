FROM ubuntu:14.04

VOLUME /www/app
VOLUME /data
EXPOSE 8000

WORKDIR /www/app

RUN \
    apt-get update -y && \
    apt-get install -y python-dev python-pip && \
    pip install tornado pymongo==2.8 motor

CMD  python web.py

