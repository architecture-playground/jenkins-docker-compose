FROM jenkinsci/blueocean:latest

USER root

COPY jenkins-data /var/jenkins_home
COPY jenkins-docker-certs /certs/client

RUN apk upgrade --no-cache \
  && apk add --no-cache \
    musl \
    build-base \
    python3\
    libc-dev \
    bash \
    git \
  && pip3 install --no-cache-dir --upgrade pip \
  && rm -rf /var/cache/* \
  && rm -rf /root/.cache/*

RUN cd /usr/bin \
  && ln -sf python3 python \
  && ln -sf pip3 pipcd

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/jenkins_home
RUN chmod +x git_add_commit_push.sh
COPY ./git_push.py ./
RUN ["python", "git_push.py"]
