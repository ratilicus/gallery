FROM ubuntu:14.04

VOLUME /data
EXPOSE 27017

RUN \
    mkdir -p /data/db && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
    echo "deb http://repo.mongodb.org/apt/ubuntu "$(lsb_release -sc)"/mongodb-org/3.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.0.list && \
    apt-get update -y && \
    apt-get install -y mongodb-org=3.0.1 mongodb-org-server=3.0.1 mongodb-org-shell=3.0.1 mongodb-org-mongos=3.0.1 mongodb-org-tools=3.0.1

CMD ["mongod", "--directoryperdb", "--smallfiles", "--logpath", "/data/mongodb.log"]

