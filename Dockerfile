FROM python:3

WORKDIR /home/app

COPY . . 

RUN pip install -r requirements.txt

ENV PYTHONPATH ="$PWD"

EXPOSE 5000