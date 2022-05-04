#!/bin/sh
docker build . -t evgkirov/create-django-project:latest
docker push evgkirov/create-django-project:latest
