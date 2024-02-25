#!/usr/bin/python3
"""handles all default RESTFul API actions"""
from models.state import State, City
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort
from flask import request


@app_views.route("/states/<state_id>/cities", methods=['GET'])
def cities():
    """the list of all City objects"""
    cities = storage.all(City).values()
    return jsonify([cities.to_dict() for city in cities])


@app_views.route("/states/cities/<city_id>", methods=['GET'])
def get_cities(city_id):
    """Get a specific City object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    return jsonify(city.to_dict())


@app_views.route("/cities/<city_id>", methods=['DELETE'])
def delete_state(city_id):
    """Get a specific State object by ID"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    storage.delete(city)
    return jsonify({}), 200


@app_views.route("/states/<state_id>/cities", methods=['POST'])
def post_state(state_id):
    """Post a specific State object by ID"""
    # Parse JSON data from request body
    data = request.get_json()
    # Check if request body is valid JSON
    if data is None:
        abort(400, 'Not a JSON')
    state = storage.get(State, state_id)
    if state is None:
        abort(404)
    # Check is 'name' key is in data(JSON data)
    if 'name' not in data:
        abort(400, 'Missing name')
    city_name = data['name']

    new_city = City(name=city_name)

    storage.new(new_city)
    storage.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route("cities/<city_id>", methods=['PUT'])
def update_state(city_id):
    """Update a specific State object by ID"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    # Get State with corresponding id
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(city, key, value)
    storage.save()
    return jsonify(city.to_dict()), 201
