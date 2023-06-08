# esto depende de lo que quieras hacer, este FROM es específico para lambdas
FROM public.ecr.aws/lambda/python:3.8 
# carpeta con los archivos
WORKDIR /python3 
COPY requirements.txt .
RUN pip install -r requirements.txt
# nombre del archivo con la app
COPY app.py .
# nombre de la función lambda, en este caso no tiene por ende,
CMD [ "handler.handler" ]