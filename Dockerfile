FROM python:3
LABEL maintainer="Michael Quinn <michael@cherrysoft.com>"

RUN mkdir /app

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY config.ini /app
COPY main.py /app

ENTRYPOINT [ "python", "-u", "./main.py" ]
