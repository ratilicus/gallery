FROM ubuntu:14.04

VOLUME /data
VOLUME /www/app

EXPOSE 8000

COPY ./requirements.txt /tmp
WORKDIR /www/app

RUN \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:nginx/stable && \
    apt-get update -y && \
    apt-get install -y python-dev python-pip && \
    pip install -r /tmp/requirements.txt

CMD python web.py

