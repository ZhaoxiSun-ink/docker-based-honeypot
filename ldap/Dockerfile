FROM ubuntu:20.04

MAINTAINER qeeqbox

ENV DEBIAN_FRONTEND=noninteractive

# Install Python and other dependencies
RUN apt-get update && apt-get install -y python3 python3-pip syslog-ng

# Copy necessary files
COPY honeypots/ldap_server.py /app/
COPY honeypots/helper.py /app/
COPY honeypots/__main__.py /app/
COPY syslog-ng.conf /etc/syslog-ng/
# Install Python packages from setup.py
COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /var/log/syslog-ng/
# Set the entry point
ENTRYPOINT ["python3", "/app/__main__.py", "--setup", "ldap"]
