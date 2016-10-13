FROM ubuntu:latest
LABEL ansible_management=v1.0
RUN echo "Installing ansible"
RUN apt-get update -y
RUN apt-get install software-properties-common -y
RUN apt-add-repository ppa:ansible/ansible -y
RUN apt-add-repository universe -y
RUN apt-add-repository main -y
RUN apt-get update -y
RUN apt-get install ansible -y
RUN apt-get install python-pip python-dev build-essential -y
RUN apt-get install python-selinux -y
RUN apt-get install rsync -y 
RUN pip install --upgrade pip
RUN pip install configparser
RUN pip install requests
RUN pip install pyproxmox
ENTRYPOINT  ./start.py
