# Use the official Python image with Alpine Linux as the base image
FROM python:3.10.4-alpine3.15

# Set environment variable
ENV APP_HOME ./django_api
ENV PYTHONUNBUFFERED=1

WORKDIR ${APP_HOME}

RUN apk update \
    #&& apk add --no-cache \
    && pip install --upgrade pip

COPY ./requirements.txt ./

RUN pip install coreapi -r requirements.txt

COPY ./ ./ 

CMD ["python","./drf/manage.py","runserver","0.0.0.0:8000"]