FROM ubuntu:latest

LABEL G. Singh, adapted by B. Hartl

RUN apt update -y
RUN apt install -y python3-pip
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD python3 app.py
