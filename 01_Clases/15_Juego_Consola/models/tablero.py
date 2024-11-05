from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla

class Tablero:
    
    def __init__(self, dimensiones: list[int], default_simbol: str = '-'):
        self.__filas = dimensiones[0]
        self.__columnas = dimensiones[1]
        self.__matrix_tablero = []
        self.__default_simbol = default_simbol
    
    def obtener_matriz(self):
        return self.__matrix_tablero
    
    def limpiar_tablero(self):
        self.__matrix_tablero.clear()
    
    def inicializar_tablero(self):
        self.crear_matriz_tablero()
    
    def crear_matriz_tablero(self) -> list[list[int]]:
        self.__matrix_tablero = [
            [self.__default_simbol for _ in range(self.__columnas)]
            for _ in range(self.__filas)
        ]
    
    def mostrar_tablero(self):
        mostrar_matriz_texto_tabla(self.__matrix_tablero, [])
    
    def insertar_ficha(self, fila_columna: tuple, ficha: str):
        if self.puede_mover(fila_columna):   
            fila, columna = fila_columna
            self.__matrix_tablero[fila][columna] = ficha
            self.mostrar_tablero()
            return True
        else:
            print(f'Ya hay una ficha ubicada en la posicion: {fila_columna}')
            return False
    
    def puede_mover(self, fila_columna: tuple) -> bool:
        if self.validar_posicion_ficha(fila_columna) and\
            self.hay_espacio(fila_columna):
                return True
        return False
    
    def hay_espacio(self, fila_columna: tuple):
        if '-' in self.__matrix_tablero[fila_columna[0]][fila_columna[1]]:
            return True
        return False
    
    def validar_posicion_ficha(self, fila_columna: tuple) -> bool:
        fila, columna = fila_columna
        if fila < len(self.__matrix_tablero) and columna < len(self.__matrix_tablero[0]):
            return True
        return False
    
    def hay_casillero_en_fila(self, fila: list[str]):
        indice_inicial = 0
        if '-' in fila:
            return True
        return False
    
    def hay_casilleros_disponibles(self) -> bool:
        se_puede_jugar = False
        for fila in self.__matrix_tablero:
            if self.hay_casillero_en_fila(fila):
                se_puede_jugar = True
            else: continue
        return se_puede_jugar

# tablero = Tablero([3,3])
# tablero.inicializar_tablero()
# tablero.insertar_ficha((2,2), 'X')
# tablero.insertar_ficha((2,2), 'X')
