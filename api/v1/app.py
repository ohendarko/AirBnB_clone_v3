#!/usr/bin/python3
"""main api program I think"""
from flask import Flask
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS


app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "0.0.0.0"}})
app.register_blueprint(app_views, url_prefix='/api/v1')


@app.teardown_appcontext
def remove_session(exc):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """returns a JSON-formatted 404 status code response."""
    return {"error": "Not found"}, 404


if __name__ == "__main__":
    host = os.getenv('HBNB_API_HOST', '0.0.0.0')
    port = int(os.getenv('HBNB_API_PORT', 5000))
    app.run(host=host, port=port, threaded=True)
