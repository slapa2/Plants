import os

class Config():
    DEBUG = True
    SECRET_KEY = 'd9c00b86f36f99cbd1f140b464bb36f1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    if os.environ.get('ENV') == 'prod':
        DEBUG = False
        SECRET_KEY = os.environ['SECRET_KEY']
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        SQLALCHEMY_TRACK_MODIFICATIONS = False