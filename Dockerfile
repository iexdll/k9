FROM ubuntu:bionic

# Install locales python and uwsgi
RUN apt-get update \
  && apt-get install -y \
  locales \
  build-essential \
  python3 \
  python3-pip \
  python-dev

RUN locale-gen "en_US.UTF-8"

WORKDIR /app/
ADD --chown=daemon:daemon . .
RUN pip3 install --no-cache-dir -r /app/requirements.txt

ENTRYPOINT uwsgi --http :9090 --wsgi-file k9service/wsgi.py
EXPOSE 9090
