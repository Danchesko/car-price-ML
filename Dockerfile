FROM python:3

WORKDIR /home/app

COPY . . 

RUN pip install -r requirements.txt

ENV PYTHONPATH="/home/app"

EXPOSE 5000