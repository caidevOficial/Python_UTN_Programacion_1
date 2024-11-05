

class Player:
    
    def __init__(self, name: str):
        self.__name = name
        self.__movements = 0
    
    def increase_movements(self, amount: int):
        self.__movements += amount
    
    def get_name(self):
        return self.__name
    
    def get_movements(self):
        return self.__movements