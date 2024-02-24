#!/usr/bin/python3
"""Pending documentation"""
from api.v1.views import app_views
from models.engine import db_storage
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
    klass = db_storage.classes
    counts = {}
    for key in klass:
        value = klass[key]
        counts[key.lower()] = storage.count(value)
    return counts
