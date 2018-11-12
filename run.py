from plants import create_app, db
from plants.auth.models import User
from sqlalchemy import exc

flask_app = create_app()
with flask_app.app_context():
    flask_app.run()