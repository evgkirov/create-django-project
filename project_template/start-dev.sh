#!/usr/bin/env bash

cp contrib/git-hooks/pre-commit .git/hooks/pre-commit
chmod +x .git/hooks/pre-commit

touch .env
docker-compose up &
./wait-for-it.sh 127.0.0.1:8000 -t 600
open "http://127.0.0.1:8000/"
