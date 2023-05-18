# api service dockerfile

FROM python:3.10-slim-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /netorc

COPY ./requirements.txt /netorc/requirements.txt

RUN pip install --no-cache-dir -r /netorc/requirements.txt

COPY ./ /netorc

RUN adduser netorc

USER netorc