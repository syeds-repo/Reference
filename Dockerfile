FROM ubuntu:18.04
WORKDIR /app
RUN apt-get -y update --fix-missing && apt-get install -y curl apt-utils python3 iputils-ping vim python3-pip
RUN pip3 install flask
COPY powerManagement.py /app
COPY start.sh /app
ENTRYPOINT ["sh", "/app/start.sh"]
