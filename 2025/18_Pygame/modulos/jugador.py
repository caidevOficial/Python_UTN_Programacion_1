import modulos.carta as carta

def inicializar_jugador():
    jugador_actual = {}
    jugador_actual['puntaje_actual'] = 0
    jugador_actual['puntaje_total'] = 0
    jugador_actual['nombre'] = 'Player'
    
    return jugador_actual



def sumar_puntaje_actual(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['puntaje_actual'] += nuevo_puntaje

def sumar_puntaje_carta_actual(jugador_actual: dict, carta_actual: dict):
    jugador_actual['puntaje_actual'] += carta.get_puntaje_carta(carta_actual)

def actualizar_puntaje_total(jugador_actual: dict):
    jugador_actual['puntaje_total'] += jugador_actual.get('puntaje_actual')

# Getters
def get_puntaje_actual(jugador_actual: dict):
    return jugador_actual.get('puntaje_actual')

def get_puntaje_total(jugador_actual: dict):
    return jugador_actual.get('puntaje_total')

def get_nombre(jugador_actual: dict):
    return jugador_actual.get('nombre')

# Setters
def set_puntaje_actual(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['puntaje_actual'] = nuevo_puntaje

def set_puntaje_total(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['puntaje_total'] = nuevo_puntaje

def set_nombre(jugador_actual: dict, nuevo_puntaje: int):
    jugador_actual['nombre'] = nuevo_puntaje