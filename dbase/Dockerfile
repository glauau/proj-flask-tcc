FROM mysql:5.7

RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y
RUN apt-get install python3-pip -y
RUN pip3 install mysqlclient
RUN pip3 install flask_mysqldb==0.2.0

#RUN mkdir -p /app/dbase/
COPY ./scripts/* /docker-entrypoint-initdb.d/
#WORKDIR /app/dbase

#RUN sleep 5
#RUN python3 prepara_banco.py


EXPOSE 3306
