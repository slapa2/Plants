from plants import create_app, db
from plants.auth.models import User

if __name__ == '__main__':
    flask_app = create_app('dev')
    with flask_app.app_context():
        db.create_all()
        if not User.query.filter_by(email='user@test.pl').first():
            User.creata_user('user@test.pl', 'user')

    flask_app.run()