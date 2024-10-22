# Copyright (C) 2024 <UTN FRA>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame.mixer as mixer
import time


DEBUG = False

def limpiar_pantalla():
    """
    The function `limpiar_pantalla` clears the console screen and waits for user input to continue.
    """
    import os
    _ = input("\nPresiona Enter para continuar...")
    os.system('cls' if os.name in ['nt', 'dos'] else 'clear')

def play_sound():
    """
    The `play_sound` function initializes the mixer, loads a sound file, sets the volume to 0.4, and
    plays the sound.
    """
    mixer.init()
    mixer.music.load('./assets/snd/select.mp3')
    mixer.music.set_volume(0.4)
    mixer.music.play()
    time.sleep(0.4)

def obtener_maximo(lista_numerica: list, debug: bool=False) -> float:
    """_summary_ Itera una lista numerica y encuentra el numero mas grande 
    de la lista

    Args:
        lista_numerica (list): _description_ Una lista numerica la cual tiene que iterar
        para encontrar el numero mas grande

    Returns:
        float: _description_ El numero mas grande de la lista, parseado a flotante
    """
    maximo = None
    for numero in lista_numerica:
        if not maximo or maximo < numero:
            maximo = numero
            if debug: 
                print(f'Nuevo Máximo: {maximo}')
    
    
    # for indice in range(len(lista_numerica)):
    #     if not maximo or maximo < lista_numerica[indice]:
    #         maximo = lista_numerica[indice]
    
    return float(maximo)

def imprimir_datos_heroe(indice: int, lista_nombre: list, lista_identidad: list, lista_genero: list, lista_poder: list, lista_altura: list):
    mensaje = f'{lista_nombre[indice]:15} | {lista_identidad[indice]:20}'\
            f' | {lista_genero[indice]:15} | {lista_poder[indice]:03} | {lista_altura[indice]:08.1f}'
    print(mensaje)

def promedio(lista_numeros: list) -> float:
    cantidad = len(lista_numeros)
    suma = 0
    for numero in lista_numeros:
        suma += numero
    
    promedio_num = suma / cantidad
    return promedio_num

def obtener_mitad_de_maximo(lista_numerica: list):
    maximo = obtener_maximo(lista_numerica)
    mitad_maximo = maximo / 2
    return mitad_maximo

def bubble_sort(lista_numeros: list[int], modo: str): # ASC | DES
    
    for indice in range(len(lista_numeros) - 1):
        for sub_indice in range(indice + 1, len(lista_numeros)):
            
            if (modo == 'ASC' and lista_numeros[indice] > lista_numeros[sub_indice] or 
                modo == 'DES' and lista_numeros[indice] < lista_numeros[sub_indice]):
                lista_numeros[indice], lista_numeros[sub_indice] =\
                lista_numeros[sub_indice], lista_numeros[indice]

    return lista_numeros

def recorrer_y_mostrar(comparador, lista_comparacion, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura):
    for indice in range(len(lista_comparacion)):
        if lista_comparacion[indice] == comparador:
            imprimir_datos_heroe(indice, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)


if __name__ == '__main__':
    lista_testing = [1,5,3,8,20,19]
    numero = obtener_maximo(lista_testing)
    print(numero)