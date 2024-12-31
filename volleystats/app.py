from flask import Flask

from volleystats.api.auth.auth import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    return app