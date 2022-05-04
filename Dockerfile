FROM python:3.10-alpine

RUN pip install django~=3.2
RUN apk add --no-cache git

COPY create-django-project.sh /
COPY project_template /template

ENTRYPOINT [ "/create-django-project.sh" ]
