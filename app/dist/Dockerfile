# FROM scratch
# FROM alpine:3.20
# FROM debian:bookworm-slim
#FROM ubuntu:23.04
#FROM hello-world

#WORKDIR /app
#COPY app .
#CMD ["/bin/bash", "-c ./app"]


#FROM ubuntu:24.04 AS builder
#RUN apt-get update && apt-get install -y python3 python3-pip python3-venv build-essential && rm -rf /var/lib/apt/lists/*
#WORKDIR /app
#COPY . .
#RUN pip3 install pyinstaller
#RUN pyinstaller --onefile app.py
#
#FROM ubuntu:24.04
#COPY --from=builder /app/dist/app /app
#CMD ["/app"]


#FROM python:3.12-slim AS builder
#
#WORKDIR /app
#
#RUN apt-get update && apt-get install -y --no-install-recommends \
#    binutils \
#    patchelf \
#    && rm -rf /var/lib/apt/lists/*
#
#COPY requirements.txt .
#RUN pip install --no-cache-dir -r requirements.txt
#
#COPY . .
#
#RUN pip install --no-cache-dir pyinstaller staticx && \
#    pyinstaller --onefile app.py && \
#    staticx dist/app app.static
#
#FROM scratch
#COPY --from=builder /tmp /tmp
#COPY --from=builder /app/app.static /app
#CMD ["/app"]

FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    binutils \
    patchelf \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN pip install --no-cache-dir pyinstaller staticx && \
    pyinstaller --onefile app.py && \
    staticx dist/app app.static

# Use a small image with shell for debugging
FROM alpine:latest

RUN apk add --no-cache bash

COPY --from=builder /app/app.static /app
CMD ["/app"]
