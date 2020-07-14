#!/usr/bin/env bash

docker build . -t acn/flaskapp

docker run -p8080:8080 acn/flaskapp