# app/auth/__init__.py
from flask import Blueprint, url_for

auth = Blueprint('auth', __name__, template_folder='templates')
from plants.auth import routes