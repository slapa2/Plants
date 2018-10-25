# app/__init__.py
import os

from flask import Flask, url_for

def create_app(config_type): # dev, test, prod
    app = Flask(__name__)
    configuration = os.path.join(os.getcwd(), 'config', config_type + '.py')
    app.config.from_pyfile(configuration)


    from app.auth import authentication
    app.register_blueprint(authentication)

    return app

