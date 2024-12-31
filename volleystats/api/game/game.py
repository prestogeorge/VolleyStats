from flask import Blueprint

game_bp = Blueprint('game', __name__)

@game_bp.get('/game/<game_id>')
def get_game(game_id):
    return game_id