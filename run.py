from plants import create_app, db
from plants.auth.models import User
from sqlalchemy import exc

flask_app = create_app()
with flask_app.app_context():
    db.create_all()
    try:
        if not User.query.filter_by(email='user@test.pl').first():
            User.creata_user('user@test.pl', 'user')
    except exc.IntegrityError:
        flask_app.run(host='0.0.0.0', port=80)