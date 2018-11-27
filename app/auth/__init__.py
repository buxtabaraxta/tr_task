"""
    app.auth
    --------

    Module creates a blueprint package (auth) for a authorization part of app.
    And pass (view) module from its package
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)

from . import views
