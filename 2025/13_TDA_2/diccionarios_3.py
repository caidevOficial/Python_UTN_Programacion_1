from utn_fra.datasets import matriz_pokemones, matriz_bzrp, matriz_data_heroes

def intercambiar_columnas(matriz: list[list], primer_col: int, segunda_col: int):
    for indice_fila in range(len(matriz)):
        aux = matriz[indice_fila][primer_col]
        matriz[indice_fila][primer_col] = matriz[indice_fila][segunda_col]
        matriz[indice_fila][segunda_col] = aux

def actualizar_indice_col(matriz: list[list], indice_columna:int, indice_elegido: int, indice_fila_ordenar: int):
    for indice_prox_columna in range(indice_columna + 1, len(matriz[indice_fila_ordenar])):
        if matriz[indice_fila_ordenar][indice_prox_columna] > matriz[indice_fila_ordenar][indice_elegido]:
            indice_elegido = indice_prox_columna
    return indice_elegido

def ordenar_selection(matriz: list[list], indice_fila_ordenar: int) -> list[list]:
    
    for indice_columna in range(len(matriz[indice_fila_ordenar]) -1):
        indice_elegido = indice_columna
        indice_elegido = actualizar_indice_col(matriz, indice_columna, indice_elegido, indice_fila_ordenar)
                
        if indice_elegido != indice_columna:
            intercambiar_columnas(matriz, indice_columna, indice_elegido)
    return matriz

def generar_fila_traspuesta(matriz: list[list], matriz_traspuesta: list[list],indice_columna: int):
    datos_fila = []
    for indice_fila in range(len(matriz)):
        datos_fila.append(matriz[indice_fila][indice_columna])
    matriz_traspuesta.append(datos_fila)

def trasponer_matriz(matriz: list[list]) -> list[list]:
    traspuesta = []
    cant_cols = len(matriz[0])
    for indice_columna in range(cant_cols):
        generar_fila_traspuesta(matriz, traspuesta, indice_columna)
    return traspuesta

def generar_texto_fila(fila: list) -> str:
    nueva_fila = []
    for elemento in fila:
        nueva_fila.append(str(elemento))
    texto = ','.join(nueva_fila)
    return texto

def mostrar_info_traspuesta(matriz: list[list]):
    for fila in matriz:
        texto = generar_texto_fila(fila)
        print(texto)

diccionario_set_de_datos = {
    "pokemones": matriz_pokemones,
    "bzrp": matriz_bzrp,
    "heroes": matriz_data_heroes
}


ordenar_selection(diccionario_set_de_datos.get('pokemones'), 0)

# diccionario_set_de_datos['pokemones_T'] = trasponer_matriz(diccionario_set_de_datos.get('pokemones'))
# diccionario_set_de_datos['bzrp_T'] = trasponer_matriz(diccionario_set_de_datos.get('bzrp'))
# diccionario_set_de_datos['heroes_T'] = trasponer_matriz(diccionario_set_de_datos.get('heroes'))


claves = list(diccionario_set_de_datos.keys())


funcion = {
    "T" :trasponer_matriz
}

for key in claves:
    # print(valor)
    # diccionario_set_de_datos[f'{key}_T'] = trasponer_matriz(diccionario_set_de_datos.get(key))
    valor = diccionario_set_de_datos.get(key)
    diccionario_set_de_datos[f'{key}_T'] = funcion.get('T')(valor)




for k,v in diccionario_set_de_datos.items():
    print(f'{k} ############# {v}\n\n\n')


# mostrar_info_traspuesta(diccionario_set_de_datos.get('pokemones_T'))
# print('\n')
# mostrar_info_traspuesta(diccionario_set_de_datos.get('bzrp_T'))
# print('\n')
# mostrar_info_traspuesta(diccionario_set_de_datos.get('heroes_T'))

# print(dic_falopa)