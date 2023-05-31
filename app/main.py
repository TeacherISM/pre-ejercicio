""" Basic Python Flask API """


from datetime import date, timedelta
from flask import Flask, jsonify


app = Flask(__name__)

@app.route('/today', methods=['GET'])
def get_today():
    """ Endpoint that gets today's date """
    today = date.today()
    return jsonify({'date': str(today)})

@app.route('/tomorrow', methods=['GET'])
def get_tomorrow():
    """ Endpoint that gets tomorrow's date """
    tomorrow = date.today() + timedelta(days=1)
    return jsonify({'date': str(tomorrow)})

if __name__ == '__main__':
    app.run()
