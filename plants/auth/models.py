from datetime import datetime

from plants import db, bcrypt, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f'User (id: {self.id}, email: {self.email})'

    @classmethod
    def creata_user(cls, email, password):
        password_hash = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=password_hash)
        db.session.add(user)
        db.session.commit()
        return user