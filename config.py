import os

class Config():
    DEBUG = True
    SECRET_KEY = 'd9c00b86f36f99cbd1f140b464bb36f1'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')

    if os.environ.get('ENV') == 'prod':
        DEBUG = False
        SECRET_KEY = os.environ['SECRET_KEY']
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
        SQLALCHEMY_TRACK_MODIFICATIONS = False