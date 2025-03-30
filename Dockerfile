FROM ubuntu:latest
LABEL authors="e180"

ENTRYPOINT ["top", "-b"]