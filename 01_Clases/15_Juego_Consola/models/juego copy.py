from .tablero import Tablero
from .stage import Stage
from .player import Player
import json
import random as rd
from UTN_Heroes_Dataset.utn_pp import clear_console, mostrar_matriz_texto_tabla
from datetime import datetime

class Juego:
    
    def __init__(self):
        self.__tablero = None
        self.__dimensiones_tablero = (0,0)
        self.__cargar_configs()
        self.__create_player()
        self.__crear_nivel()
        self.__crear_tablero()
        self.__turno = 'Jugador'
        self.__gano_alguien = False
        self.__ganador = None
        self.__player_movements = 0
        self.__actual_stage = None
        self.__player = None
    
    def __create_player(self):
        p_name = input('Ingresa tu nombre de jugador: ')
        self.__player = Player(p_name)
    
    
    def __crear_nivel(self):
        self.__actual_stage = Stage(self.__player)
    
    def __cambiar_turno(self):
        self.__actual_stage.cambiar_turno()
    
    def __save_score(self):
        with open('./score.csv', 'a') as score_file:
            score_file.write(f'{self.__actual_stage.get_ganador()},{self.__player_movements},{datetime.now()}\n')
    
    def __mostrar_score_table(self):
        with open('./score.csv', 'r') as save_file:
            lines = save_file.read().split('\n')
        matrix = [
            line.split(',') for line in lines
        ]
        mostrar_matriz_texto_tabla(matrix, ['Ganador', 'Movimientos', 'Fecha'])
    
    def jugar(self):
        # self.__mostrar_score_table()
        self.__actual_stage.show_tablero()
        while not self.__actual_stage.gano_alguien():
            if self.__actual_stage.se_puede_jugar():
                self.__actual_stage.pedir_movimiento()
                # self.chequear_si_gano('X')
        clear_console()
        self.__actual_stage.show_tablero()
        print('Juego terminado!')
        print(f'Ganador: {self.__ganador}, Felicidades!')
