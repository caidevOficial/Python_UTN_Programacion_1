from UTN_FRA.funciones.auxiliares import show_matrix_as_table

def crear_tablero(dimensiones: list[int], symbol: str = '-') -> dict:
    tablero = {
        "cant_filas": dimensiones[0],
        "cant_columnas": dimensiones[1],
        "matrix_tablero": [],
        "default_symbol": symbol
    }
    return tablero

def get_matrix_tablero(tablero: dict) -> list[list]:
    return tablero.get('matrix_tablero', [[]])

def clear_tablero(tablero: dict) -> None:
    tablero['matrix_tablero'].clear()
    return tablero

def init_tablero(tablero: dict) -> dict:
    return create_matrix_tablero(tablero)

def create_matrix_tablero(tablero: dict) -> dict:
    tablero['matrix_tablero'] = [
            [tablero.get('default_symbol') for _ in range(tablero.get('cant_columnas'))]
            for _ in range(tablero.get('cant_filas'))
        ]
    return tablero

def show_tablero(tablero: dict) -> None:
    show_matrix_as_table(tablero.get('matrix_tablero'), [])

def __hay_espacio(tablero: dict, fila_columna: tuple):
    if '-' in tablero.get('matrix_tablero')[fila_columna[0]][fila_columna[1]]:
        return True
    return False

def __validar_posicion_ficha(tablero: dict, fila_columna: tuple) -> bool:
    fila, columna = fila_columna
    if fila < len(tablero.get('matrix_tablero')) and\
        columna < len(tablero.get('matrix_tablero')[0]):
        return True
    return False

def __puede_mover(tablero: dict, fila_columna: tuple) -> bool:
    if __validar_posicion_ficha(tablero,fila_columna) and\
        __hay_espacio(tablero, fila_columna):
            return True
    return False

def insertar_ficha(tablero: dict, fila_columna: tuple, ficha: str):
    if __puede_mover(tablero, fila_columna):   
        fila, columna = fila_columna
        tablero['matrix_tablero'][fila][columna] = ficha
        show_tablero(tablero)
        return True
    else:
        print(f'Ya hay una ficha ubicada en la posicion: {fila_columna}')
        return False

def __hay_casillero_en_fila(fila: list[str]):
    if '-' in fila:
        return True
    return False

def hay_casilleros_disponibles(tablero: dict) -> bool:
    se_puede_jugar = False
    for fila in tablero.get('matrix_tablero'):
        if __hay_casillero_en_fila(fila):
            se_puede_jugar = True
        else: continue
    return se_puede_jugar