#!/usr/bin/env bash 

apt-get install -y python python-pip python-dev 

# configure Microsoft Azure driver for sql 
apt-get install python python-pip gcc g++ build-essential
curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
curl https://packages.microsoft.com/config/ubuntu/18.04/prod.list > /etc/apt/sources.list.d/mssql-release.list

apt-get update 
yes yes | ACCEPT_EULA=Y apt-get install msodbcsql17
echo Y | apt install unixodbc-dev
pip install pyodbc
pip install pytest-timeout

# install requirements 
pip install -r /autograder/source/requirements.txt