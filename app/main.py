""" Basic Flask application for CI/CD exercise """

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """ Application entrypoint """
    name = "John Doe"
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
    