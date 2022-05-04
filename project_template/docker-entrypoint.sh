#!/usr/bin/env bash

set -e
./wait-for-it.sh db:5432 --timeout=90

case "$1" in
    bash)
      bash
    ;;
    python)
        "$@"
    ;;
    *)
        python manage.py "$@"
    ;;
esac
