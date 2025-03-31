from .player import Player

class HumanPlayer(Player):
    
    def __init__(self, name: str, symbol: str = 'X'):
        super().__init__(name, symbol)
