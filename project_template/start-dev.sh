#!/usr/bin/env bash

chmod -x contrib/git-hooks/*
git config core.hooksPath contrib/git-hooks

touch .env
docker compose up &
./wait-for-it.sh 127.0.0.1:8000 -t 600
docker compose run --rm web install
open "http://127.0.0.1:8000/"
