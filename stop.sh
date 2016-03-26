#!/bin/bash

docker stop $(docker ps --filter="name=db|app" -q)
docker rm $(docker ps --filter="name=db|app" -aq)
