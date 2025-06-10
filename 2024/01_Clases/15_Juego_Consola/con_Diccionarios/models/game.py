import datetime
from utn_fra.funciones.auxiliares import (
    clear_console, show_matrix_as_table
)
from .auxiliar import (
    cargar_configs, save_score,
    CONFIGS_PATH, SCORE_FILE_PATH
)
from .players import (
    create_player, get_player_name, get_player_movements,
    get_player_total_movements
)
from .game_features import (
    crear_stage, get_ganador, get_stage_number, reset_participants,
    jugar as jugar_nivel, gano_alguien, get_nivel_terminado
)

def crear_juego() -> dict:
    juego = {
        "configs": cargar_configs(CONFIGS_PATH),
        "nivel": None,
        "human": None,
        "bot": None,
        "actual_stage_number": 1,
    }
    return juego

def create_human_player(juego: dict) -> dict:
    p_name = input('Ingresa tu nombre de jugador: ')
    juego['human'] = create_player(p_name)
    return juego

def create_ai_player(juego: dict) -> dict:
    juego['bot'] = create_player('UTN_BOT', symbol='O')
    return juego

def crear_playable_stage(juego: dict, stage_configs: dict) -> dict:
    juego['nivel'] = crear_stage(juego.get('human'), juego.get('bot'), stage_configs)
    return juego

def create_data_score(juego: dict) -> str:
    player_winner = get_ganador(juego.get("nivel"))
    data = f'{get_player_name(player_winner)},'\
            f'{get_player_movements(player_winner)},'\
            f'{get_player_total_movements(player_winner)},'\
            f'{get_stage_number(juego.get("nivel"))},{datetime.date.today().strftime(format='%Y-%m-%d')}\n'
    return data

def save_score_data(juego: dict):
    data = create_data_score(juego)
    save_score(SCORE_FILE_PATH, data)

def sort_matrix_double_criteria(matrix: list[list]):
    for index_row in range(len(matrix) - 1):
        for index_next_row in range(index_row + 1, len(matrix)):
            
            if int(matrix[index_row][3]) < int(matrix[index_next_row][3]) or\
                matrix[index_row][3] == matrix[index_next_row][3] and\
                int(matrix[index_row][2]) > int(matrix[index_next_row][2]):
                
                matrix[index_row], matrix[index_next_row] =\
                matrix[index_next_row], matrix[index_row]

def get_top(top_number: int):
    def get_matrix_top(matrix: list[list]):
        return matrix[:top_number]
    return get_matrix_top

def mostrar_score_table():
    with open(SCORE_FILE_PATH, 'r') as save_file:
        lines = save_file.read().split('\n')
    matrix = [
        line.split(',') for line in lines
        if line != ''
    ]
    
    top_10 = get_top(5)
    sort_matrix_double_criteria(matrix)
    top_10_matrix_filtered = top_10(matrix)
    
    show_matrix_as_table(
        top_10_matrix_filtered, 
        ['Ganador', 'Movimientos', 'Total Movimientos', 'Nivel', 'Fecha'])

def mostrar_menu():
    texto =\
    """
    1 - Jugar
    2 - Ver Ranking
    3 - Salir
    """
    print(texto)

def validar_input(minimo: int, maximo: int):
    opcion = input(f'Ingrese una opcion entre [{minimo}-{maximo}]: ')
    if not opcion.isdigit() or not (minimo <= int(opcion) <= maximo):
        return validar_input(minimo, maximo)
    return int(opcion)
    
def save_and_reset(juego: dict):
    save_score_data(juego)
    reset_participants(juego.get('nivel'))
    juego['nivel']['stage_number'] = juego.get('nivel').get('stage_number', 1) + 1
    juego['nivel'] = None

def run_stage(juego: dict):
    while juego.get('nivel'):
        jugar_nivel(juego.get('nivel'))
        if gano_alguien(juego.get('nivel')):
            save_and_reset(juego)

        elif get_nivel_terminado(juego.get('nivel')):
            juego['nivel'] = None

def jugar(juego: dict):
    juego = create_human_player(juego)
    juego = create_ai_player(juego)
    for stage_level, stage_config in juego.get('configs').items():
        juego = crear_playable_stage(juego, stage_config)
        run_stage(juego)
    juego['nivel'] = None

def init_juego():
    juego = crear_juego()
    correr_juego = True
    while correr_juego:
        mostrar_menu()
        opcion = validar_input(1,3)
        
        match opcion:
            case 1:
                jugar(juego)
            case 2:
                mostrar_score_table()
            case 3:
                correr_juego = False
        clear_console()