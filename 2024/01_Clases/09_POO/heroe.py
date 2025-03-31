
"""
matriz_data_heroes = [
    lista_nombres_heroes,
    lista_identidades_heroes,
    lista_apodos_heroes,
    lista_generos_heroes,
    lista_poder_heroes,
    lista_alturas_heroes
]
"""

class Heroe:
    
    def __init__(self, nombre, identidad, apodo, genero, poder, altura):
        self.__nombre = nombre # Private
        self.__identidad = identidad # Private
        self.__alias = apodo # Private
        self.__genero = genero
        self.__poder = poder
        self.__altura = altura
        
        """
        
        public int poder = poder
        
        self._nombre -> Protected
        self.__nombre -> Private
        self.nombre -> Public
        
        """
    
    def __poner_en_mayusculas(self, texto: str) -> str:
        return texto.upper()
    
    def to_string(self):
        mensaje =\
        f'{self.__nombre} | {self.__identidad} | {self.__alias} | {self.__poder}'
        mensaje = self.__poner_en_mayusculas(mensaje)
        return mensaje
    
    def __validar_poder(self, nuevo_poder: int) -> bool:
        if nuevo_poder > 0 and nuevo_poder < 101:
            return True
        return False

    
    def get_nombre(self) -> str:
        return self.__nombre
    
    def get_alias(self) -> str:
        return self.__alias
    
    def get_identidad(self) -> str:
        return self.__identidad
    
    def get_poder(self) -> int:
        return self.__poder
    
    def set_poder(self, nuevo_poder: int) -> None:
        if self.__validar_poder(nuevo_poder):
            self.__poder = nuevo_poder