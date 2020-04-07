FROM jenkinsci/blueocean:latest

USER root

COPY jenkins-data /var/jenkins_home
COPY jenkins-docker-certs /certs/client

