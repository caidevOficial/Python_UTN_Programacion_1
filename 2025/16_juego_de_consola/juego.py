import random


def __elegir_palabra(matriz: list[list]) -> str:
    """
    Dada una matriz de palabras, elegirá de forma aleatoria
    una palabra de dicha matriz para retornarla
    
    :param matriz: La matriz de palabras del juego
    :returns: la palabra elegida
    Note:
        Cada fila de la matriz debe tener el mismo tamaño (cantidad de elementos) para que
        sea una matriz cuadrada, el algoritmo no debe romper independientemente del tamaño
        de la matriz, elgiendo siempre una palabra de forma correcta.
    """
    indices_filas = len(matriz) - 1
    indices_columnas = len(matriz[0]) - 1
    
    fila = random.randint(0, indices_filas)
    columna = random.randint(0, indices_columnas)
    palabra = matriz[fila][columna]
    return palabra

def inicializar_palabra_secreta(matriz_palabras: list[list], dic_juego: dict):
    """
    La funcion inicializa la palabra elegida y ademas una version oculta con "_" por cada caracter de esa palabra.
    Tambien inicializa las vidas del jugador en 6.
    
    :param matriz_palabras: La matriz de palabras del juego
    :param dic_juego: El parámetro `dic_juego` es un diccionario que almacena información relacionada con el juego. 
    En esta función, se utiliza para registrar la palabra secreta, 
    la versión oculta de la palabra y el número de vidas restantes del jugador.
    """
    palabra_secreta = __elegir_palabra(matriz_palabras)
    palabra_oculta = ["_"] * len(palabra_secreta)
    dic_juego["palabra"] = palabra_secreta
    dic_juego["palabra_oculta"] = palabra_oculta
    dic_juego['vidas'] = 6

def verificar_estado_juego(diccionario_juego: dict) -> bool:
    """Verifica si el juego sigue en curso verificando que la cantidad de vidas sea mayor a 0
    y que la palabra oculta aun tenga "_" visibles.
    
    :param dic_juego: El parámetro `dic_juego` es un diccionario que almacena información relacionada con el juego. 
    
    :returns bool: Retorna True si aun se puede seguir jugando, False caso contrario
    """
    return diccionario_juego["vidas"] > 0 and "_" in diccionario_juego["palabra_oculta"]

def mostrar_letra_oculta(diccionario_juego: dict, letra: str):
    """
    Recorre la palabra oculta verificando si algun caracter coincide con el ingresado por consola.
    En caso de coincidir, reemplaza el "_" por dicho caracter.
    
    :param dic_juego: El parámetro `dic_juego` es un diccionario que almacena información relacionada con el juego. 
    :param letra: El parámetro `letra` es la letra ingresada por el usuario para verificar si pertenece a la palabra oculta. 
    """
    palabra = diccionario_juego["palabra"]
    for index in range(len(palabra)):
        if palabra[index] == letra:
            diccionario_juego["palabra_oculta"][index] = letra

def modificar_dato(diccionario: dict, clave: str, dato_nuevo: any) -> bool:
    """Modifica el valor de una clave existente en el diccionario.
    
    :param diccionario: Es el diccionario en el cual se modificara el valor de una clave
    :param clave: Es la clave del diccionario la cual se modificará su valor
    :param dato_nuevo: Es el nuevo valor que tomara la clave del diccionario.
    
    :returns bool: Retornará True si pudo modificarse, False caso contrario
    """
    if clave in diccionario:
        diccionario[clave] = dato_nuevo
        return True
    return False

def __buscar_indice_superior(matrix: list[list], indice_inicial: int):
    """
    Busca el índice del elemento con el valor más alto en la segunda columna de una matriz 
    a partir de un índice inicial dado.
    
    :param matrix: Una lista de listas que representan una matriz donde cada lista interna contiene elementos
    :param indice_inicial: El parámetro `indice_inicial` es un entero que representa el índice inicial 
    desde el cual la función comenzará a buscar el elemento más alto de la matriz.
    :return: La función `__buscar_indice_superior` devuelve el índice del elemento de la matriz `matrix` 
    que tiene el valor más alto en la segunda posición de cada sublista, iniciando la búsqueda desde el índice `indice_inicial`.
    """
    indice_elem_alto = indice_inicial
    for indice_siguiente in range(indice_inicial + 1, len(matrix)):
        if matrix[indice_elem_alto][1] < matrix[indice_siguiente][1]:
            indice_elem_alto = indice_siguiente
    return indice_elem_alto

def __intercambiar_filas(matrix: list[list], indices: list):
    """
    La función `__intercambiar_filas` intercambia dos filas en una matriz basándose en los índices proporcionados.
    
    :param matrix: matriz de datos donde cada fila representa todos el conjunto de datos de un mismo registro
    :param indices: El parámetro `índices` es una lista que contiene dos elementos, 
        donde cada elemento representa el índice de una fila en la lista `matriz` que desea intercambiar,
        osea el indice de un elemento y el indice del otro el cual hay que intercambiarlos entre si
    """
    matrix[indices[0]], matrix[indices[1]] = matrix[indices[1]], matrix[indices[0]]
    
def ordenar_matrix(matrix: list):
    """
    La función `ordenar_matrix` ordena una matriz de puntajes intercambiando filas de forma DES usando el algoritmo SELECTION SORT.
    
    :param matrix: la matriz la cual hay que ordenar de forma DES segun el puntaje, usando dos funciones auxiliares:
    `__buscar_indice_superior` y `__intercambiar_filas`
    """
    for indice_actual in range(len(matrix) - 1):
        indice_elem_alto = __buscar_indice_superior(matrix, indice_actual)
        
        if indice_elem_alto != indice_actual:
            __intercambiar_filas(matrix, [indice_actual, indice_elem_alto])

def __crear_fila_dato(datos: list):
    """
    La función `__crear_fila_dato` crea una fila de datos formateada a partir de una lista de cadenas y números enteros.
    
    :param datos: La función `__crear_fila_dato` recibe una lista de datos como entrada. 
                    Itera sobre cada elemento de la lista y, según su tipo (ya sea una cadena o un entero), 
                    lo formatea y lo añade a la cadena `texto`. 
    
    :returns: Devuelve una cadena formateada que contiene los elementos de la lista de entrada `datos`. 
                El formato depende del tipo de cada elemento de la lista: 
                    si el elemento es una cadena, se formatea para ocupar 10 caracteres
                    si es un entero, se formatea para ocupar 8 caracteres. 
                Los elementos se separan con '|' y la cadena final termina con otro '|'
                Ejemplo:
                        | nombre    |     20 |     10 |     30 |
    """
    texto = ''
    for dato in datos:
        if type(dato) == str:
            texto += f' | {dato:10}'
        elif type(dato) == int:
            texto += f' | {dato:8}'
    texto += ' |'
    return texto

def mostrar_ranking_matrix(matrix_ranking: list[list]):
    """
    La función `mostrar_ranking_matrix` muestra una tabla de puntajes ordenada de forma DES y formateada basada en la matriz de entrada.
    
    :param matrix_ranking: La matriz la cual hay que ordenar y mostrar
    """
    ordenar_matrix(matrix_ranking)
    print(' | Nombre     | Puntaje  |  vidas   | Partidas | Ganadas  |\n'\
          ' ----------------------------------------------------------')
    for row in matrix_ranking:
        dato = __crear_fila_dato(row)
        print(dato)

def __crear_lista_puntaje(diccionario_jugador: dict):
    """
    La función `__crear_lista_puntaje` toma un diccionario del jugador y devuelve una lista con el valor de cada clave del diccionario.
    
    :param diccionario_jugador: un diccionario que posee el nombre y diversos puntajes del jugador como tambien la cantidad de vidas que le quedan
    :return: Retorna una lista con los valores de cada clave del diccionario
    `diccionario_jugador`.
    """
    lista_puntaje = []
    for clave, valor in diccionario_jugador.items():
        lista_puntaje.append(valor)
    return lista_puntaje

def guardar_puntuacion(diccionario_jugador: dict, lista_puntajes: list[dict]) -> bool:
    """
    La función `guardar_puntuacion` toma el diccionario de un jugador y una lista de puntuaciones, 
    añade la puntuación del jugador a la lista y devuelve True si no hubo errores.
    
    :param diccionario_jugador: Diccionario del jugador que posee el nombre, puntaje, cantidad de vidas, cantidad de movimientos y movimientos totales
    :param lista_puntajes: Una matriz donde cada fila es un record de cada jugador a modo de ranking
    :return: Retorna True si no hubo errores.
    """
    lista_puntajes.append(__crear_lista_puntaje(diccionario_jugador))
    return True

def terminar_juego(mensaje_final: str) -> None:
    """Imprime un mensaje para mostrar al final del juego."""
    print(mensaje_final)