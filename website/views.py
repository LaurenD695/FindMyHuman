# view functions

# stores login, explore, etc each route a user can go to 
from flask import Blueprint, render_template, request, jsonify
from .pet_api import test_get_all_animals
from website import random_generate

#define name of views blueprint
views = Blueprint('views', __name__)

# route for homepage - in this case it will be an explore page 
@views.route('/home')
def home():
    # animals = test_get_all_animals()
    # return render_template('home.html', animals=animals)

    name = request.args.get('name')
    age = request.args.get('age')

    # Call the backend API route
    try:
        response = requests.get('http://localhost:5000/get_animals', params={'name': "", 'age': None, "page": 0, "offset": 0})
        response.raise_for_status()
        animals = response.json()
    except requests.RequestException as e:
        print(f"Error calling /get_animals: {e}")
        animals = []

    return render_template('home.html', animals=animals)
# route for login page