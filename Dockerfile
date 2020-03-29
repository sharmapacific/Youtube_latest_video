# Dockerfile

# Pull base image
FROM python:3.6.7

LABEL maintainer="Prashant Kumar Sharma  <sharma.pacific1@gmail.com>"

ARG RUNTIME_DEPS='wget axel vim python-dev libsm6 libxext6'
RUN apt-get update -y && \
    apt-get install -y ${RUNTIME_DEPS}

# Added separately so that layers get cached
ARG BUILD_DEPS='apt-utils unzip cmake build-essential pkg-config  build-essential'

COPY requirements.txt .
RUN apt-get install -y ${BUILD_DEPS} && \
    pip install -r requirements.txt && \
    apt-get purge -y --auto-remove $BUILD_DEPS

# set workdir
WORKDIR /var/app

# copy code into image
COPY . /var/app/

EXPOSE 8000

# entrypoint
ENTRYPOINT ["python"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]
