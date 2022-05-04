FROM python:3.10

ENV PROJECT_NAME myproject
ENV PORT 8000

RUN mkdir /app
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

ENTRYPOINT ["./docker-entrypoint.sh"]
