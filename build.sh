#!/bin/bash

APPPATH=$(dirname $(readlink -f "$0"))

cd $APPPATH

docker build -t rat/mongo mongo
docker build -t rat/app app

