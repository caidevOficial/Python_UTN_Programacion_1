from .game_features import Stage
from .players import HumanPlayer, AIPlayer
from .auxiliar import (
    cargar_configs, save_score, CONFIGS_PATH, SCORE_FILE_PATH, END_LEVEL_SOUND
)
from .sound import SoundManager
from UTN_Heroes_Dataset.utn_pp import clear_console, mostrar_matriz_texto_tabla
import datetime

class JuegoTest:
    
    def __init__(self):
        self.__actual_stage = None
        self.__player = None
        self.__actual_stage_number = 1
        self.__configs = cargar_configs(CONFIGS_PATH)
        self.__snd_manager = SoundManager()
        
    def __create_player(self):
        p_name = input('Ingresa tu nombre de jugador: ')
        self.__player = HumanPlayer(p_name.title())
    
    def __create_ai_player(self):
        self.__ai_player = AIPlayer('UTN_Bot')
    
    
    def __crear_nivel(self, stage_configs: dict):
        self.__actual_stage = Stage(self.__player, self.__ai_player, stage_configs)
    
    def __create_data_score(self):
        data = f'{self.__actual_stage.get_ganador().get_name()},'\
                f'{self.__actual_stage.get_ganador().get_movements()},'\
                f'{self.__actual_stage.get_ganador().get_total_movements()},'\
                f'{self.__actual_stage.get_stage_number()},{datetime.date.today().strftime(format='%Y-%m-%d')}\n'
        return data
    
    def __save_score_data(self):
        data = self.__create_data_score()
        save_score(SCORE_FILE_PATH, data)
    
    def __sort_matrix_double_criteria(self, matrix: list[list]):
        for index_row in range(len(matrix) - 1):
            for index_next_row in range(index_row + 1, len(matrix)):
                if int(matrix[index_row][3]) < int(matrix[index_next_row][3]) or\
                   matrix[index_row][3] == matrix[index_next_row][3] and\
                   int(matrix[index_row][1]) > int(matrix[index_next_row][1]):
                    
                    matrix[index_row], matrix[index_next_row] =\
                    matrix[index_next_row], matrix[index_row]
                
    def get_top(self, top_number: int):
        def get_matrix_top_5(matrix: list[list]):
            return matrix[:top_number]
        return get_matrix_top_5
    
    def __mostrar_score_table(self):
        with open(SCORE_FILE_PATH, 'r') as save_file:
            lines = save_file.read().split('\n')
        matrix = [
            line.split(',') for line in lines
            if line != ''
        ]
        
        top_10 = self.get_top(5)
        print(top_10(matrix))
        self.__sort_matrix_double_criteria(matrix)
        mostrar_matriz_texto_tabla(top_10(matrix), ['Ganador', 'Movimientos', 'Total Movimientos', 'Nivel', 'Fecha'])
    
    def mostrar_menu(self):
        texto =\
        """
        1 - Jugar
        2 - Ver Ranking
        3 - Salir
        """
        print(texto)
    
    def validar_input(self, minimo: int, maximo: int):
        opcion = input(f'Ingrese una opcion entre [{minimo}-{maximo}]: ')
        if not opcion.isdigit() or not (minimo <= int(opcion) <= maximo):
            return self.validar_input(minimo, maximo)
        return int(opcion)
    
    def __save_and_reset(self):
        self.__save_score_data()
        self.__actual_stage.reset_participants()
        self.__actual_stage_number += 1
        self.__actual_stage = None
    
    def __run_stage(self):
        while self.__actual_stage:
            self.__actual_stage.jugar()
            if self.__actual_stage.gano_alguien():
                self.__save_and_reset()

            elif self.__actual_stage.get_nivel_terminado():
                self.__actual_stage = None
    
    def __jugar(self):
        self.__create_player()
        self.__create_ai_player()
        for stage_level, stage_config in self.__configs.items():
            self.__crear_nivel(stage_config)
            self.__run_stage()
        self.__actual_stage = None
        self.__snd_manager.play_sound(END_LEVEL_SOUND)
        
    
    def init_juego(self):
        
        while True:
            self.mostrar_menu()
            opcion = self.validar_input(1,3)
            
            match opcion:
                case 1:
                    self.__jugar()
                case 2:
                    self.__mostrar_score_table()
                case 3:
                    break
            clear_console()
