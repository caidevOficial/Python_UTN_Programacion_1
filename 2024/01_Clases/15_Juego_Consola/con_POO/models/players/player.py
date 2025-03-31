

class Player:
    
    def __init__(self, name: str, symbol: str = 'X'):
        self.__name = name
        self.__movements = 0
        self.__total_movements = 0
        self.__symbol = symbol
        self.__has_win = False
    
    def reset_stats(self):
        self.__movements = 0
        self.__has_win = False
    
    def increase_movements(self, amount: int):
        self.__movements += amount
    
    def get_name(self):
        return self.__name
    
    def get_movements(self):
        return self.__movements
    
    def get_win(self):
        return self.__has_win
    
    def get_symbol(self):
        return self.__symbol
    
    def get_total_movements(self):
        return self.__total_movements
    
    def update_total_movements(self):
        self.__total_movements += self.__movements