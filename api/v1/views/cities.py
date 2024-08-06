#!/usr/bin/python3
"""New view for City objects that handles all default RestFul API actions
"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models import storage
from models.state import State
from models.city import City

