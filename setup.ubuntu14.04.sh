#!/bin/bash

echo "Setting up environment"

CWD=`dirname "$0"`
cd $CWD &&
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 &&
( echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list ) &&
sudo apt-get update &&
sudo apt-get install -y python-pip python-virtualenv &&
sudo apt-get install -y mongodb-org &&
virtualenv ve &&
source ve/bin/activate &&
pip install -r requirements.txt &&
mkdir -p uploads

echo "
- mongo installed
- pip installed
- virtualenv setup
- tornado installed
- motor installed

to run this app:
    cd $CWD
    source $CWD/ve/bin/activate
    ./app.py
"
