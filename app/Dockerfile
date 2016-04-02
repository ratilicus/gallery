FROM ubuntu:14.04

VOLUME /data
EXPOSE 8000

COPY . /www/app
WORKDIR /www/app

RUN \
    mkdir -p /data/uploads && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:nginx/stable && \
    apt-get update -y && \
    apt-get install -y python-dev python-pip && \
    pip install -r /www/app/requirements.txt

CMD python web.py

