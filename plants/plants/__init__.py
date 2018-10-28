from flask import Blueprint, url_for

plants = Blueprint('plants', __name__, template_folder='templates')
from plants.plants import routes