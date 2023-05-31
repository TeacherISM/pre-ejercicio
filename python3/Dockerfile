# # use python 3.11
# FROM python:3.11 

# #RUN apt-get update && apt-get -y install libsnappy-dev && apt-get -y install python3-dev
# RUN mkdir /app
# COPY execute.sh /app/execute.sh
# COPY requirements.txt /app/requirements.txt
# RUN chmod 777 /app/execute.sh
# RUN pip install -r /app/requirements.txt
# COPY src/ /app/src/
# EXPOSE 5000
# WORKDIR /app/
# ENTRYPOINT ["./execute.sh"]

# Specify the base image with the desired Python version
FROM public.ecr.aws/lambda/python:3.8

# Copy the Lambda function code into the container
COPY lambda_function.py /app/lambda_function.py

# Install any required dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Set the working directory
WORKDIR /app

# Specify the command to execute the Lambda function
ENTRYPOINT ["lambda_function.lambda_handler"]

