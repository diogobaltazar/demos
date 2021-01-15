FROM ubuntu

RUN apt-get update
RUN  yes | apt install software-properties-common
run  add-apt-repository ppa:deadsnakes/ppa
run  apt update
run  apt install python3.8

RUN pip install flask
RUN pip install flask-mysql

COPY . /opt/source-code

ENTRYPOINT FLASK_APP=/opt/source-code/app.py flask run