# FROM python:3.11
FROM public.ecr.aws/lambda/python:3.8

#RUN apt-get update && apt-get -y install libsnappy-dev && apt-get -y install python3-dev
RUN mkdir /app
# COPY execute.sh /app/execute.sh
COPY requirements.txt /app/requirements.txt
# RUN chmod 777 /app/execute.sh
RUN pip3 install -r /app/requirements.txt --target "${LAMBDA_TASK_ROOT}"
# COPY src/ /app/src/
COPY . ${LAMBDA_TASK_ROOT}
# EXPOSE 5000
# WORKDIR /app/
# ENTRYPOINT ["./execute.sh"]
CMD ["app.lambda_handler"]
