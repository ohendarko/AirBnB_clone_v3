#!/usr/bin/python3
"""handles all default RESTFul API actions"""
from models.place import Place
from models.city import City
from api.v1.views import app_views
from models import storage
from flask import jsonify, abort
from flask import request


@app_views.route("/cities/<city_id>/places", strict_slashes=False, methods=['GET'])
def places(city_id):
    """the list of all User objects"""
    city = storage.get(City, city_id)
    if city is None:
        abort(404)
    plases = storage.all(Place).values()
    city_places = [place.to_dict() for place in plases if
                    place.city_id == city_id]
    return jsonify(city_places)


@app_views.route("places/<place_id>", strict_slashes=False, methods=['GET'])
def get_place(place_id):
    """Get a specific User object by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    return jsonify(place.to_dict())


@app_views.route("/places/<place_id>>", strict_slashes=False, methods=['DELETE'])
def delete_place(place_id):
    """Get a specific User object by ID"""
    place = storage.get(Place, place_id)
    if place is None:
        abort(404)
    storage.delete(place)
    return jsonify({}), 200


@app_views.route("/cities/<city_id>/places", strict_slashes=False, methods=['POST'])
def post_place(city_id):
    """Post a specific User object by ID"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    if 'email' not in data:
        abort(400, 'Missing email')
    if 'password' not in data:
        abort(400, 'Missing password')
    place_name = data['name']
    new_place = Place(name=place_name, city_id=city_id)
    storage.new(new_place)
    storage.save()
    return jsonify(new_place.to_dict()), 201


@app_views.route("/places/<place_id>", strict_slashes=False, methods=['PUT'])
def update_place(places_id):
    """Update a specific User object by ID"""
    data = request.get_json()
    if data is None:
        abort(400, 'Not a JSON')
    place = storage.get(Place, places_id)
    if place is None:
        abort(404)
    for key, value in data.items():
        if key not in ['id', 'created_at', 'updated_at']:
            setattr(place, key, value)
    storage.save()
    return jsonify(place.to_dict()), 200
