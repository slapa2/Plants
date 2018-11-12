from plants import create_app

flask_app = create_app()
with flask_app.app_context():
    flask_app.run()