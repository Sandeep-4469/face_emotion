FROM python:3.11
WORKDIR /code
COPY . /code
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y python3-opencv