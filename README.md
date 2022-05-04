# Create Django Project

Yet another opinionated Django project template that no one will ever use except me a couple times

## Prerequisites

* Linux or macOS (not tested with Windows)
* Docker & Docker Compose

## Usage

Replace **myproject** with your actual project name.

    docker run -e PROJECT_NAME=myproject --mount type=bind,src=$PWD,dst=/projects evgkirov/create-django-project:main

Then run the newly created project:

    cd myproject
    ./start-dev.sh