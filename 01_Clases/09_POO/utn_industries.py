from UTN_Heroes_Dataset.utn_matrices import matriz_data_heroes
from heroe import Heroe 

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


class ComicsStore:
    
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__matriz_heroes = []
        self.__lista_comics_heroes = list[Heroe]()
    
    def __transponer(self, matriz_heroes: list[list]) -> None:
        matriz_transpuesta = []
        cantidad_columnas = len(matriz_heroes[0])
        
        for indice_columna in range(cantidad_columnas):
            dato_heroe = []
            for indice_fila in range(len(matriz_heroes)):
                dato_heroe.append(matriz_heroes[indice_fila][indice_columna])
            matriz_transpuesta.append(dato_heroe)
        self.__matriz_heroes = matriz_transpuesta
    
    def __inicializar_comics_heroes(self):
        nueva_lista_heroes_obj = []
        self.__transponer(matriz_data_heroes)
        
        for lista in self.__matriz_heroes:
            # nuevo_heroe = Heroe(
            #     lista[0],
            #     lista[1],
            #     lista[2],
            #     lista[3],
            #     lista[4], # Poder
            #     lista[5]
            # )
            nuevo_heroe = Heroe(*lista)
            
            nueva_lista_heroes_obj.append(nuevo_heroe)
        self.__lista_comics_heroes = nueva_lista_heroes_obj
    
    def __ordenar_por_poder_asc(self) -> None:
        
        for indice_actual in range(len(self.__lista_comics_heroes) -1):
            for indice_proximo in range(indice_actual + 1, len(self.__lista_comics_heroes)):
                if self.__lista_comics_heroes[indice_actual].get_poder() >\
                   self.__lista_comics_heroes[indice_proximo].get_poder():
                    
                    self.__lista_comics_heroes[indice_actual], self.__lista_comics_heroes[indice_proximo] =\
                    self.__lista_comics_heroes[indice_proximo], self.__lista_comics_heroes[indice_actual]
    
    def mostrar_heroes_de_comics(self, cantidad: int) -> None:
        self.__inicializar_comics_heroes()
        self.__ordenar_por_poder_asc()
        
        print(f'{self.__nombre}`s Comics Store:')
        for heroe in self.__lista_comics_heroes[0:cantidad]:
            print(heroe.to_string())


