FROM python:2.7
ENV PYTHONUNBUFFERED 1

VOLUME /www/app
VOLUME /data
EXPOSE 8000

WORKDIR /www/app

RUN  pip install tornado pymongo==2.8 motor

CMD  python web.py

