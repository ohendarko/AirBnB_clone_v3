#!/usr/bin/python3
"""Pending documentation"""
from api.v1.views import app_views


@app_views.route("/status", methods=['GET'])
def status():
    """return OK status"""
    return {"status": "OK"}


@app_views.route("/stats", methods=['GET'])
def stats():
    """return OK status"""
    return {"status": "OK"}
