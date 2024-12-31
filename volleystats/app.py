from flask import Flask

from volleystats.api.auth.auth import auth_bp
from volleystats.api.game.game import game_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)
    app.register_blueprint(game_bp)
    return app