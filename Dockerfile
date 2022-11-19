FROM python:3.9-alpine
MAINTAINER Puiu Iulia - Pisoft Tech

ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
      gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
WORKDIR /app
COPY ./app/ /app

RUN mkdir -p /documents/recipe
RUN mkdir -p /static

RUN adduser -D user
RUN chown -R user:user /documents/
RUN chmod -R 755 /documents
USER user