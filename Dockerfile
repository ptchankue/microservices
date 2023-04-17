# set the base image
FROM python:3.9
# File Author / Maintainer
MAINTAINER Patrick Tchankue

RUN apt-get update && apt-get install -y build-essential

ENV APP_HOME /microservices

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

COPY requirements.txt $APP_HOME
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=3000

# NGINX config
#COPY nginx.conf /etc/nginx/conf.d/delivery.conf

ADD . $APP_HOME
