from datetime import datetime
from itsdangerous import JSONWebSignatureSerializer
from flask import current_app as app
from flask_login import UserMixin

from plants import db, bcrypt, login_manager


class Plant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    polish_name = db.Column(db.String(50), unique=True)
    latin_name = db.Column(db.String(50))
    light_level = db.Column(db.Integer)
    water_level = db.Column(db.Integer)
    spray = db.Column(db.Boolean)
    light_description = db.Column(db.Text)
    water_description = db.Column(db.Text)
    temperature = db.Column(db.Text)
    soil = db.Column(db.Text)
    fertilizing = db.Column(db.Text)
    transplanting = db.Column(db.Text)
    multiplication = db.Column(db.Text)
    image = db.Column(db.Text, nullable=False, default="../static/img/plant.png")

    def __repr__(self):
        return f'Plant {self.polish_name} {self.latin_name}'



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    activate = db.Column(db.Boolean)

    def __repr__(self):
        return f'User (id: {self.id}, email: {self.email})'

    @classmethod
    def creata_user(cls, email, password):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=password_hash, activate=False)
        db.session.add(user)
        db.session.commit()
        return user

    def activate(self):
        self.activate = 1
        db.session.add(self)
        db.session.commit()
        return user

    def get_user_token(self):
        s = JSONWebSignatureSerializer(app.config['SECRET_KEY'])
        return s.dumps(self.id).decode('utf-8')

    @staticmethod
    def verify_user_token(token):
        s = JSONWebSignatureSerializer(app.config['SECRET_KEY'])
        print('token:', token)
        try:
            user_id = s.loads(token)
            print(f'VERIFY -> user_id: {user_id}')
        except:
            return None
        return User.query.get(user_id)


