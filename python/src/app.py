from flask import Flask

# create the application object
app = Flask(__name__)


# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello, Salvador!"  # return

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')