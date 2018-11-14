# app/main/__init__.py
from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates')
from plants.main import routes