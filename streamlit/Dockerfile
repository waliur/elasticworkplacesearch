# Use an official base image
FROM ubuntu:20.04

# Preset tzdata timezone to prevent need enter manually for smbclient package
ENV TZ=Europe/London
ENV DEBIAN_FRONTEND=noninteractive

# Install Git and other dependencies
RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y python3-pip && \
    apt-get install -y smbclient cifs-utils inetutils-ping && \
    apt-get install -y curl && \
    apt-get clean

# RUN curl -fsSL https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add -
# RUN echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list
# RUN apt-get update && apt-get install elasticsearch

# Install streamlit 
RUN pip install streamlit

# RUN git clone https://github.com/elastic/enterprise-search-network-drive-connector.git

# Install elasticsearch libarires
RUN pip install elasticsearch

# Copy the app code
COPY app.py /app/

# WORKDIR /app
# EXPOSE 8501 9200

# Start Elasticsearch and Streamlit in the background 
# CMD service elasticsearch start
    #&& streamlit run app.py
# CMD service elasticsearch start && /bin/bash

CMD streamlit run app.py