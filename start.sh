#!/bin/bash

CD=$(dirname $(readlink -f "$0"))
DATAVOL=$CD/data:/data
APPVOL=$CD/app:/www/app

cd $CD
mkdir -p $CD/data/db
mkdir -p $CD/data/log
mkdir -p $CD/data/uploads

(docker run -d -v $DATAVOL --name db rat/mongo) &&
(docker run -d -v $DATAVOL -v $APPVOL -p 8000:8000 --name app --link db rat/app) &&
(docker ps) &&
(echo "OK: app started!  (browse to locahost:8000 to see app)") ||
(echo "FAIL: app run failedstarted! (did you run build.sh?)")

