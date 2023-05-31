FROM python:3.11

#RUN apt-get update && apt-get -y install libsnappy-dev && apt-get -y install python3-dev
RUN mkdir /app
COPY execute.sh /execute.sh
COPY requirements.txt /requirements.txt
RUN chmod 777 /execute.sh
RUN pip install -r /requirements.txt
COPY src/ /src/
EXPOSE 5000
WORKDIR /app/
ENTRYPOINT ["./execute.sh"]