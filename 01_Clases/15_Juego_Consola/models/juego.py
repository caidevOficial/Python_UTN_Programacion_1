from .tablero import Tablero
from .stage import Stage
import json
import random as rd
from UTN_Heroes_Dataset.utn_pp import clear_console, mostrar_matriz_texto_tabla
from datetime import datetime

class Juego:
    
    def __init__(self):
        self.__tablero = None
        self.__dimensiones_tablero = (0,0)
        self.__cargar_configs()
        self.__crear_tablero()
        self.__turno = 'Jugador'
        self.__gano_alguien = False
        self.__ganador = None
        self.__player_movements = 0
        self.__actual_stage = None
    
    def __cargar_configs(self):
        with open('./config.json', 'r') as config:
            self.__dimensiones_tablero =\
                json.load(config).get('dimension_tablero')
    
    def __crear_tablero(self):
        self.__tablero = Tablero(self.__dimensiones_tablero)
        self.__tablero.inicializar_tablero()
    
    def __cambiar_turno(self):
        if self.__turno == 'Jugador':
            self.__turno = 'PC'
        else: self.__turno = 'Jugador'
    
    def __obtener_coordenadas(self):
        while True:
            coordenadas = input('Ingresa coordenadas de tu ficha [Fila-Columna]: ')
            if self.__validar_input(coordenadas):
                lista_coord = coordenadas.split('-')
                return int(lista_coord[0]), int(lista_coord[1])
            print("Coordenadas inválidas. Inténtalo de nuevo.")

    def __pedir_movimiento(self):
        if self.__turno == 'Jugador':
            while True:
                coordenadas_nov = self.__obtener_coordenadas()
                if coordenadas_nov:
                    print(f'Tu Jugada: {coordenadas_nov}')
                    if self.__tablero.insertar_ficha(coordenadas_nov, 'X'):
                        self.__player_movements += 1
                        self.__chequear_si_gano('X')
                        break
                # Si las coordenadas son inválidas o no se puede insertar la ficha, el bucle se repite.
        else:
            self.__mover_ia()
    
    def __validar_input(self, coordenadas: str):
        coordenadas = tuple(coordenadas.split('-'))
        if coordenadas[0].isdigit() and coordenadas[1].isdigit():
            return True
        return False
    
    def __mover_ia(self):
        fila = rd.randint(0, self.__dimensiones_tablero[0]-1)
        columna = rd.randint(0, self.__dimensiones_tablero[1]-1)
        coordenadas = (fila, columna)
        
        
        if not self.__tablero.puede_mover(coordenadas):
            return self.__mover_ia()
        else:
            print(f'Jugada de la AI: {coordenadas}')
            self.__tablero.insertar_ficha(coordenadas, 'O')
            self.__chequear_si_gano('O')
    
    def __se_puede_jugar(self):
        return not self.__gano_alguien and self.__tablero.hay_casilleros_disponibles()
    
    def __revisar_jugadas(self, symbol: str):
        lista_jugadas = []
        matrix = self.__tablero.obtener_matriz()
        for index_row in range(len(matrix)):
            for index_column in range(len(matrix[index_row])):
                if matrix[index_row][index_column] == symbol:
                    lista_jugadas.append((index_row, index_column))
        return lista_jugadas
    
    def __sort_jugadas(self, jugadas: list[tuple[int,int]]):
        for actual_index in range(len(jugadas)-1):
            for next_index in range(actual_index + 1, len(jugadas)):
                if jugadas[actual_index][0] > jugadas[next_index][0]:
                    jugadas[actual_index][0], jugadas[next_index][0] =\
                    jugadas[next_index][0], jugadas[actual_index][0]
        return jugadas
    
    def __check_jugada(self, jugadas: list[tuple[int,int]], index_jugada: int):
        uniques_rows = dict()
        for jugada in jugadas:
            uniques_rows[jugada[index_jugada]] = uniques_rows.get(jugada[index_jugada], 0) + 1
        for k, v in uniques_rows.items():
            if v == 3:
                if index_jugada == 0:
                    message = f'En la fila {k} hay {v} fichas'
                else: message = f'En la columna {k} hay {v} fichas'
                print(message)
                return True
        return False
    
    def __check_row_column(self, jugadas: list[tuple[int,int]], row_column: str = 'row'):
        win = False
        match row_column:
            case 'row':
                win = self.__check_jugada(jugadas, 0)
            case 'column':
                win = self.__check_jugada(jugadas, 1)
        return win
    
    def __chequear_si_gano(self, symbol: str):
        jugadas = self.__revisar_jugadas(symbol)
        jugadas = self.__sort_jugadas(jugadas)
        win_by_row = self.__check_row_column(jugadas, 'row')
        win_by_column = self.__check_row_column(jugadas, 'column')
        print(jugadas)
        print(f'Win by row: {win_by_row} | Win by column: {win_by_column}')
        if win_by_row or win_by_column:
            self.__ganador = self.__turno
            self.__gano_alguien = True
            self.__save_score()
            self.__mostrar_score_table()
        else:
            self.__cambiar_turno()
    
    def __save_score(self):
        with open('./score.csv', 'a') as score_file:
            score_file.write(f'{self.__ganador},{self.__player_movements},{datetime.now()}\n')
    
    def __mostrar_score_table(self):
        with open('./score.csv', 'r') as save_file:
            lines = save_file.read().split('\n')
        matrix = [
            line.split(',') for line in lines
        ]
        mostrar_matriz_texto_tabla(matrix, ['Ganador', 'Movimientos'])
    
    def jugar(self):
        self.__mostrar_score_table()
        self.__tablero.mostrar_tablero()
        while not self.__gano_alguien:
            if self.__se_puede_jugar():
                self.__pedir_movimiento()
                # self.chequear_si_gano('X')
        clear_console()
        self.__tablero.mostrar_tablero()
        print('Juego terminado!')
        print(f'Ganador: {self.__ganador}, Felicidades!')
