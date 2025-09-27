FROM python:3.13-alpine3.22
LABEL maintainer="prakash488"

ENV PYTHONUNBUFFERED=1


COPY ./app /app
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
WORKDIR /app
EXPOSE 8000
ARG DEV=false

RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    if [ $DEV=="true" ]; \
        then pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    adduser \
    --disabled-password \
    --no-create-home \
    app-user

USER app-user





