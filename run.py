from plants import create_app, db
from plants.models import User, Role
from sqlalchemy.exc import IntegrityError


flask_app = create_app()
with flask_app.app_context():
    db.create_all()

    try:
    	if not Role.query.filter_by(name='user').first():
	        role = Role(name='user')
	        db.session.add(role)
	        db.session.commit()
    except:
        pass
    try:
    	if not Role.query.filter_by(name='admin').first():
	        role = Role(name='admin')
	        db.session.add(role)
	        db.session.commit()
    except:
        pass

    try:
    	if not User.query.filter_by(email='admin@test.pl').first():
	        user = User.creata_user('admin@test.pl', 'admin')
	        user.roles.append(Role.query.get(2))
	        user.activate_user()
    except:
        pass

    try:
    	if not User.query.filter_by(email='user@test.pl').first():
	        user = User.creata_user('user@test.pl', 'user')
	        user.activate_user()
    except:
        pass
