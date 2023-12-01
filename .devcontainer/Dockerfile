FROM python:3.8-slim as pro

RUN apt-get -y update && apt-get install

RUN apt-get install cron
RUN apt-get install nano

ADD . /app
WORKDIR /app
RUN chmod -R 777 /app

RUN python -m pip install --upgrade pip
# RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt
ENTRYPOINT [ "/bin/bash" ]

