from plants import create_app, db
from plants.models import User
from sqlalchemy.exc import IntegrityError


flask_app = create_app()
with flask_app.app_context():
    db.create_all()
    try:
        User.creata_user('user@test.pl', 'user')
    except IntegrityError :
        pass