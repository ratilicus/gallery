#!/bin/bash

CD=$(dirname $(readlink -f "$0"))

cd $CD

(docker build -t rat/mongo mongo) &&
(docker build -t rat/app app) &&
(echo "OK: build successful!") ||
(echo "FAIL: build failed!")

