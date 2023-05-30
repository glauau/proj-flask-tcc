FROM python:3.7.10-slim-stretch

RUN mkdir /app
COPY ./app/filmoteca.py /app
COPY ./app/models.py /app
COPY ./app/dao.py /app

RUN mkdir /app/templates
COPY ./app/templates/* /app/templates/

RUN mkdir /app/static
COPY ./app/static/* /app/static/

RUN mkdir -p /app/dbase/scripts
COPY ./dbase/scripts/* /app/dbase/scripts/

RUN apt-get update && apt-get install -y curl
RUN pip install --upgrade pip
RUN pip3 install flask==0.12.2
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN pip3 install mysqlclient
RUN pip3 install flask_mysqldb==0.2.0

WORKDIR /app
CMD [ "python", "filmoteca.py" ]

EXPOSE 5000
