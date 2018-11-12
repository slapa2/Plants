import os

class Config():
    DEBUG = False
    SECRET_KEY = 'd9c00b86f36f99cbd1f140b464bb36f1'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False