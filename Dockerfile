# Use the official Python image with Alpine Linux as the base image
FROM python:3.10.4-alpine3.15

# Set environment variable
ENV PYTHONUNBUFFERED=1

# Create a dir
WORKDIR /django_api

# Updates for alpine package keeper and pip
RUN apk update \
    && apk add --no-cache build-base mariadb-dev mariadb-connector-c-dev\
    && pip install --upgrade pip

# Set the environemnt
COPY ./requirements.txt ./
RUN pip install -r ./requirements.txt

# Pass the Django rest framework and dockerfile
COPY ./drf ./drf
COPY Dockerfile ./

# Run Django
CMD ["python","./drf/manage.py","runserver","0.0.0.0:8000"]