# Use an official base image
FROM ubuntu:20.04

# Preset tzdata timezone to prevent need enter manually for cron package
ENV TZ=Europe/London
ENV DEBIAN_FRONTEND=noninteractive

# Install Git and other dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y git && \
    apt-get install -y python3-pip && \
    apt-get install -y python3.8 && \
    apt-get install -y cron && \
    apt-get install -y vim && \
    apt-get install -y tesseract-ocr && \
    apt-get install -y openjdk-8-jdk && \
    apt-get install -y python3.8-venv && \
    apt-get clean

# Install Connector
WORKDIR /app
RUN git clone https://github.com/elastic/enterprise-search-network-drive-connector.git /app
RUN make install_package ES_VERSION_V8=no
ENV PATH=/root/.local/bin/:$PATH

CMD tail -f /dev/null