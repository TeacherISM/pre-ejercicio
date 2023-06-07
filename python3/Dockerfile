FROM public.ecr.aws/lambda/python:3.11

WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .

CMD [ "handler.handler" ]