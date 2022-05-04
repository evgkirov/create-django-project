#!/bin/sh

PROJECT_DIR="/projects/$PROJECT_NAME"

mkdir "$PROJECT_DIR"
cd "$PROJECT_DIR"

django-admin startproject "$PROJECT_NAME" . --template=/template --extension=py,md,yml
git init
