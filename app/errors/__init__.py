"""
    app.errors
    --------

    Module creates a blueprint package (errors).
    And pass (handlers.py) module from its package which handles server response error codes for HTTP requests.
"""

from flask import Blueprint

errors = Blueprint('errors', __name__)

from . import handlers
