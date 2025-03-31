from .auxiliares import (
    obtener_maximo, imprimir_datos_heroe, promedio, obtener_mitad_de_maximo,
    recorrer_y_mostrar, bubble_sort
)


def utn_mostrar_nombres_heroes(lista_nombres: list) -> None:
    """_summary_ Itera una lista de strings y los imprime en consola

    Args:
        lista_nombres (list): _description_ Lista de strings
    """
    for nombre in lista_nombres:
        print(nombre)

def utn_mostrar_identidades_heroes(lista_identidad: list) -> None:
    for identidad in lista_identidad:
        print(identidad)
        
def utn_mostrar_heroe_mayor_altura(lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura, debug):
    maximo = obtener_maximo(lista_altura, debug)
    recorrer_y_mostrar(maximo, lista_altura, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)

def utn_mostrar_heroes_mas_fuertes(lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura) -> None:
    max_poder = obtener_maximo(lista_poder)
    recorrer_y_mostrar(max_poder, lista_poder, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)
    

def utn_filtrar_heroes_genero(lista_nombre: list, lista_identidad: list, lista_genero: list, lista_poder: list, lista_altura: list, genero: str) -> None:
    recorrer_y_mostrar(genero, lista_genero, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)


def utn_mostrar_heroes_poder_superior_promedio(lista_nombre: list, lista_identidad: list, lista_genero: list, lista_poder: list, lista_altura: list) -> None:
    promedio_poder = promedio(lista_poder)
    
    print(f'Promedio de poder: {promedio_poder:06.2f} UF')
    for indice in range(len(lista_poder)):
        if lista_poder[indice] > promedio_poder:
            imprimir_datos_heroe(indice, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)

def utn_mostrar_heroes_mas_debiles(lista_nombre: list, lista_identidad: list, lista_genero: list, lista_poder: list, lista_altura: list) -> None:
    mitad_de_maximo = obtener_mitad_de_maximo(lista_poder)
    
    print(f'Mitad de poder del mas fuerte: {mitad_de_maximo:06.2f} UF')
    for indice in range(len(lista_poder)):
        if lista_poder[indice] <= mitad_de_maximo:
            imprimir_datos_heroe(indice, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)

# 10 - Ordenar los heroes por poder ascendente y mostrarlos.
def utn_ordenar_poder_ascendente(lista_nombre: list, lista_identidad: list, lista_genero: list, lista_poder: list, lista_altura: list):
    bubble_sort(lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura, 'ASC')
    for indice in range(len(lista_nombre)):
        imprimir_datos_heroe(indice, lista_nombre, lista_identidad, lista_genero, lista_poder, lista_altura)