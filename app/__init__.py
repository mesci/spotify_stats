from flask import Flask
from config import Config
from flask_session import Session

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from app import routes
    app.register_blueprint(routes.bp)

    Session(app)

    return app
