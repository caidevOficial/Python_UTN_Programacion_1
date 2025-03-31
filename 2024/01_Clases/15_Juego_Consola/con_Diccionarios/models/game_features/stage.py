from .tablero import (
    crear_tablero, show_tablero, init_tablero, get_matrix_tablero,
    insertar_ficha, __puede_mover, hay_casilleros_disponibles
)
from ..players import (
    get_player_name, get_player_symbol, increase_movements,
    update_player_total_movements, reset_status_player
)
import random as rd
from UTN_FRA.funciones.auxiliares import clear_console

def crear_stage(player: dict, enemy: dict, configs: dict) -> dict:
    stage = {
        "stage_number": configs.get('nivel'),
        "human_player": player,
        "AI_player": enemy,
        "tablero": None,
        "tablero_dimentions": configs.get('dimension_tablero'),
        "turno": get_player_name(player),
        "gano_alguien": False,
        "winner": None,
        "nivel_terminado": False
    }
    return stage

def show_nivel_tablero(stage: dict) -> None:
    show_tablero(stage.get('tablero'))

def gano_alguien(stage: dict) -> bool:
    return stage.get('gano_alguien')

def get_ganador(stage: dict) -> dict:
    return stage.get('winner')

def get_nivel_terminado(stage: dict) -> bool:
    return stage.get('nivel_terminado')

def get_stage_number(stage: dict) -> int:
    return stage.get('stage_number')

def crear_tablero_nivel(stage: dict) -> None:
    stage['tablero'] = crear_tablero(stage.get('dimensiones_tablero'))
    stage["tablero"] = init_tablero(stage.get('tablero'))
    return stage

def __cambiar_stage_turno(stage: dict):
    if stage.get('turno') != get_player_name(stage.get('AI_player')):
        stage['turno'] = get_player_name(stage.get('AI_player'))
    else:
        stage['turno'] = get_player_name(stage.get('human_player'))

def __validar_input(coordenadas: str):
    coordenadas = tuple(coordenadas.split('-'))
    if coordenadas[0].isdigit() and coordenadas[1].isdigit():
        return True
    return False

def __obtener_coordenadas():
    while True:
        coordenadas = input('Ingresa coordenadas de tu ficha [Fila-Columna]: ')
        if __validar_input(coordenadas):
            lista_coord = coordenadas.split('-')
            return int(lista_coord[0]), int(lista_coord[1])
        print("Coordenadas inválidas. Inténtalo de nuevo.")

def __sort_jugadas(jugadas: list[tuple[int,int]]):
    for actual_index in range(len(jugadas)-1):
        for next_index in range(actual_index + 1, len(jugadas)):
            if jugadas[actual_index][0] > jugadas[next_index][0]:
                jugadas[actual_index][0], jugadas[next_index][0] =\
                jugadas[next_index][0], jugadas[actual_index][0]
    return jugadas

def __revisar_jugadas(stage: dict, symbol: str) -> list[tuple[int,int]]:
        lista_jugadas = []
        matrix = get_matrix_tablero(stage.get('tablero'))
        for index_row in range(len(matrix)):
            for index_column in range(len(matrix[index_row])):
                if matrix[index_row][index_column] == symbol:
                    lista_jugadas.append((index_row, index_column))
        return lista_jugadas

def __check_jugada(stage: dict, jugadas: list[tuple[int,int]], index_jugada: int):
        uniques_rows = dict()
        for jugada in jugadas:
            uniques_rows[jugada[index_jugada]] = uniques_rows.get(jugada[index_jugada], 0) + 1
        for k, v in uniques_rows.items():
            if v == stage.get('tablero_dimentions')[0]:
                if index_jugada == 0:
                    message = f'En la fila {k} hay {v} fichas'
                else: message = f'En la columna {k} hay {v} fichas'
                print(message)
                return True
        return False

def __check_row_column(stage: dict, jugadas: list[tuple[int,int]], row_column: str = 'row'):
        win = False
        match row_column:
            case 'row':
                win = __check_jugada(stage, jugadas, 0)
            case 'column':
                win = __check_jugada(stage, jugadas, 1)
        return win

def __extraer_datos(stage: dict, participant: dict) -> dict:
    jugadas = __sort_jugadas(
            __revisar_jugadas(stage, get_player_symbol(participant))
        )
    datos = {
        "jugadas": jugadas,
        "gana_fila": __check_row_column(stage, jugadas, 'row'),
        "gana_columna": __check_row_column(stage, jugadas, 'column')
    }
    return datos

def __chequear_si_gano(stage: dict, participant: dict):
    datos = __extraer_datos(stage, participant)
    print(datos.get('jugadas'))
    print(f'Win by row: {datos.get('gana_fila')} | Win by column: {datos.get('gana_columna')}')
    if datos.get('gana_fila') or datos.get('gana_columna'):
        stage['winner'] = participant
        stage['gano_alguien'] = True
        stage['nivel_terminado'] = True
    else:
        __cambiar_stage_turno(stage)

def __mover_ia(stage: dict):
    fila = rd.randint(0, stage['tablero_dimentions'][0]-1)
    columna = rd.randint(0, stage['tablero_dimentions'][1]-1)
    coordenadas = (fila, columna)
    
    
    # if not self.__tablero.puede_mover(coordenadas):
    if not __puede_mover(stage['tablero'], coordenadas):
        return __mover_ia(stage)
    else:
        print(f'Jugada de la AI: {coordenadas}')
        insertar_ficha(stage['tablero'], coordenadas, get_player_symbol(stage['AI_player']))
        # self.__tablero.insertar_ficha(coordenadas, self.__contrincant.get_symbol())
        increase_movements(stage['AI_player'], 1)
        # self.__contrincant.increase_movements(1)
        __chequear_si_gano(stage, stage['AI_player'])
        # self.__chequear_si_gano(self.__contrincant)

def __pedir_movimiento(stage: dict):
    if stage['turno'] == get_player_name(stage['human_player']):
        while True:
            coordenadas_nov = __obtener_coordenadas()
            if coordenadas_nov:
                print(f'Tu Jugada: {coordenadas_nov}')
                if insertar_ficha(
                    stage.get('tablero'), coordenadas_nov, 
                    get_player_symbol(stage.get('human_player'))):
                # if self.__tablero.insertar_ficha(coordenadas_nov, self.__player.get_symbol()):
                    increase_movements(stage['human_player'], 1)
                    # self.__player.increase_movements(1)
                    __chequear_si_gano(stage, stage.get('human_player'))
                    # self.__chequear_si_gano(self.__player)
                    break
            # Si las coordenadas son inválidas o no se puede insertar la ficha, el bucle se repite.
    else:
        __mover_ia(stage)

def __se_puede_jugar(stage: dict):
    return not stage.get('gano_alguien') and\
            hay_casilleros_disponibles(stage['tablero']) and\
            not stage['nivel_terminado']

def __mensaje_ganador(stage: dict):
    if gano_alguien(stage):
        mensaje = f'Ganador: {get_player_name(stage.get('winner'))}, Felicidades!'
    else: 
        mensaje = f'El nivel {stage["stage_number"]} Queda invicto!'
    stage['nivel_terminado'] = True
    print(mensaje)

def __update_winner_movements(stage: dict):
        if stage.get('winner'):
            update_player_total_movements(stage.get('winner'))
            # self.__ganador.update_total_movements()

def reset_participants(stage: dict):
    stage['human_player'] = reset_status_player(stage.get('human_player'))
    stage['AI_player'] = reset_status_player(stage.get('AI_player'))


def jugar(stage: dict):
    print(f'### Nivel {stage.get("stage_number")} ###')
    stage['tablero'] = crear_tablero(stage['tablero_dimentions'])
    stage['tablero'] = init_tablero(stage['tablero'])
    # self.__play_music()
    show_tablero(stage.get('tablero'))
    # self.__tablero.mostrar_tablero()
    # while self.se_puede_jugar():
    while __se_puede_jugar(stage):
        __pedir_movimiento(stage)
        # self.pedir_movimiento()
    debug = {
        "Gano_Alguien": gano_alguien(stage),
        "Nivel_terminado": stage['nivel_terminado']
    }
    print(debug)
    __update_winner_movements(stage)
    # self.__update_winner_movements()
    # self.__sound_manager.stop_music()
    # self.__play_sound(self.__ganador)
    clear_console()
    show_tablero(stage.get('tablero'))
    # self.__tablero.mostrar_tablero()
    print(f'Nivel {stage.get("stage_number")} terminado!')
    # self.__mensaje_ganador()
    __mensaje_ganador(stage)