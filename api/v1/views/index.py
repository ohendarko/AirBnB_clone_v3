#!/usr/bin/python3
"""Pending documentation"""
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


@app_views.route("/status", methods=['GET'])
def status():
    """return OK status"""
    return {"status": "OK"}


@app_views.route("/stats", methods=['GET'])
def stats():
    """ retrieves the number of each objects by type"""
    return {
        "amenities": storage.count(Amenity),
        "cities": storage.count(City),
        "places": storage.count(Place),
        "reviews": storage.count(Review),
        "states": storage.count(State),
        "users": storage.count(User)
    }
