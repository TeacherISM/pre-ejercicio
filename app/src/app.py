from flask import Flask
import aws_lambda_wsgi 

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hola Andreina'

def lambda_handler(event, context):
    return aws_lambda_wsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)