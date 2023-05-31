# import the Flask class from the flask module
# from flask import Flask, render_template, request, jsonify
import requests

# create the application object
# app = Flask(_name_)


#comentario
# use decorators to link the function to a url
# @app.route('/')
# def home():
#     return "Hola, A01029422"  # return a string

def lambda_handler(event, context):
    # r = requests.get('https://api.github.com/events')
    return {
        "Hola, Mateo"
    }

# @app.route('/welcome')
# def welcome():
#     return render_template('welcome.html')  # render a template


# countries = [
#     {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
#     {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
#     {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
# ]


# def _find_next_id():
#     return max(country["id"] for country in countries) + 1


# @app.get("/countries")
# def get_countries():
#     return jsonify(countries)


# @app.post("/countries")
# def add_country():
#     if request.is_json:
#         country = request.get_json()
#         country["id"] = _find_next_id()
#         countries.append(country)
#         return country, 201
#     return {"error": "Request must be JSON"}, 415


# start the server with the 'run()' method
# if _name_ == "_main_":
#     app.run(debug=True, host='0.0.0.0')