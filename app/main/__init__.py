"""
    app.main
    --------

    Module creates a blueprint package (main).
    Pass (views) module which handles application routes
"""

from flask import Blueprint

main = Blueprint('main', __name__)

from . import views
