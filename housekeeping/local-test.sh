#!/bin/sh

PROJECT_NAME=testproject

rm -rf $PROJECT_NAME

docker build . -t evgkirov/create-django-project:latest

docker run -e PROJECT_NAME=$PROJECT_NAME --mount type=bind,src=$PWD,dst=/projects evgkirov/create-django-project:latest

cd $PROJECT_NAME
docker-compose down
docker volume rm "$PROJECT_NAME_postgres"

#./start-dev.sh
