FROM python:3

WORKDIR /home/app

COPY . . 

RUN pip install -r requirements.txt

EXPOSE 5000