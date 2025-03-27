from .player import Player

class AIPlayer(Player):
    
    def __init__(self, name: str, symbol: str = 'O'):
        super().__init__(name, symbol)
