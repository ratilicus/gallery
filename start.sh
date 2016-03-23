#!/bin/bash

APPPATH=$(dirname $(readlink -f "$0"))

cd $APPPATH
mkdir -p $APPPATH/data/db
mkdir -p $APPPATH/data/uploads

#docker run -v $APPPATH/data:/data -i --rm=true --name db rat/mongo &
#docker run -v $APPPATH/data:/data -i --rm=true -p 8000:8000 --name app --link db rat/app &

(docker run -v $APPPATH/data:/data -d --name db rat/mongo) &&
(docker run -v $APPPATH/data:/data -d -p 8000:8000 --name app --link db rat/app) &&
docker ps
