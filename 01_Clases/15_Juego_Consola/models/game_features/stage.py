from .tablero import Tablero
from ..players import (
    Player, HumanPlayer, AIPlayer
)
import json
import random as rd
from UTN_Heroes_Dataset.utn_pp import clear_console


class Stage:
    
    def __init__(self, player: HumanPlayer, enemy: AIPlayer, configs: dict):
        self.__stage_number = configs.get('nivel')
        self.__player = player
        self.__contrincant = enemy
        self.__tablero = None
        self.__dimensiones_tablero = configs.get('dimension_tablero')
        # self.__cargar_configs()
        self.__crear_tablero()
        self.__turno = player.get_name()
        self.__gano_alguien = False
        self.__ganador = None
        self.__nivel_terminado = False
    
    def show_tablero(self):
        self.__tablero.mostrar_tablero()
    
    def gano_alguien(self):
        return self.__gano_alguien
    
    def get_ganador(self):
        return self.__ganador
    
    def get_nivel_terminado(self):
        return self.__nivel_terminado

    def get_stage_number(self):
        return self.__stage_number
    
    def __cargar_configs(self):
        with open('./config_test.json', 'r') as config:
            self.__dimensiones_tablero =\
                json.load(config)\
                    .get(f'nivel_{self.__stage_number}')\
                    .get('dimension_tablero')
    
    def __crear_tablero(self):
        self.__tablero = Tablero(self.__dimensiones_tablero)
        self.__tablero.inicializar_tablero()
    
    def __cambiar_turno(self):
        if self.__turno != self.__contrincant.get_name():
            self.__turno = self.__contrincant.get_name()
        else: self.__turno = self.__player.get_name()
        print(f'Turno de: {self.__turno}')
    
    def __obtener_coordenadas(self):
        while True:
            coordenadas = input('Ingresa coordenadas de tu ficha [Fila-Columna]: ')
            if self.__validar_input(coordenadas):
                lista_coord = coordenadas.split('-')
                return int(lista_coord[0]), int(lista_coord[1])
            print("Coordenadas inválidas. Inténtalo de nuevo.")

    def pedir_movimiento(self):
        if self.__turno == self.__player.get_name():
            while True:
                coordenadas_nov = self.__obtener_coordenadas()
                if coordenadas_nov:
                    print(f'Tu Jugada: {coordenadas_nov}')
                    if self.__tablero.insertar_ficha(coordenadas_nov, self.__player.get_symbol()):
                        self.__player.increase_movements(1)
                        self.__chequear_si_gano(self.__player)
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
            self.__tablero.insertar_ficha(coordenadas, self.__contrincant.get_symbol())
            self.__contrincant.increase_movements(1)
            self.__chequear_si_gano(self.__contrincant)
    
    def se_puede_jugar(self):
        return not self.__gano_alguien and\
               self.__tablero.hay_casilleros_disponibles() and\
               not self.__nivel_terminado
    
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
            if v == self.__dimensiones_tablero[0]:
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
    
    def __extraer_datos(self, participant: Player) -> dict:
        jugadas = self.__sort_jugadas(
                self.__revisar_jugadas(participant.get_symbol())
            )
        datos = {
            "jugadas": jugadas,
            "gana_fila": self.__check_row_column(jugadas, 'row'),
            "gana_columna": self.__check_row_column(jugadas, 'column')
        }
        return datos
    
    def __chequear_si_gano(self, participant: Player):
        datos = self.__extraer_datos(participant)
        print(datos.get('jugadas'))
        print(f'Win by row: {datos.get('gana_fila')} | Win by column: {datos.get('gana_columna')}')
        if datos.get('gana_fila') or datos.get('gana_columna'):
            self.__ganador = participant
            self.__gano_alguien = True
            self.__nivel_terminado = True
        else:
            self.__cambiar_turno()
    
    def reset_participants(self):
        self.__player.reset_stats()
        self.__contrincant.reset_stats()
    
    def __mensaje_ganador(self):
        if self.gano_alguien():
            mensaje = f'Ganador: {self.__ganador.get_name()}, Felicidades!'
        else: 
            mensaje = f'El nivel {self.__stage_number} Queda invicto!'
        self.__nivel_terminado = True
        print(mensaje)
    
    def jugar(self):
        print(f'### Nivel {self.__stage_number} ###')
        self.__tablero.mostrar_tablero()
        while self.se_puede_jugar():
            self.pedir_movimiento()
        debug = {
            "Gano_Alguien": self.gano_alguien(),
            "Nivel_terminado": self.__nivel_terminado
        }
        print(debug)
        clear_console()
        self.__tablero.mostrar_tablero()
        print(f'Nivel {self.__stage_number} terminado!')
        self.__mensaje_ganador()