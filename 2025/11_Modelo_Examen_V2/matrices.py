
# Ejercicio 1 ------------------------------------------------------------------------------------
def crear_matriz(lista_1: list, lista_2: list, lista_3: list, lista_4: list, lista_5: list) -> list[list]:
    """
    Crea una matriz en base a las listas pasadas por parametro y la retorna
    
    Args:
        lista_1 a lista_5: Listas para formar la matriz de la función
        
    Returns:
            Una matriz de 5 filas
    """
    matriz = [
        lista_1, 
        lista_2,
        lista_3, 
        lista_4,
        lista_5
    ]
    return matriz


"""id,nombre,tipo,poder,condición"""

# Ejercicio 2 ------------------------------------------------------------------------------------
def crear_texto_info_pokemon(matriz: list[list], indice_col: int):
    """
    Recorre la fila de la matriz en la columna especificada y crea un texto con la informacion
    de cada fila en esa misma columna.
    
    Args:
        matriz: La matriz de datos
        indice_col: El indice de la columna actual d donde se tienen que sacar los datos fila a fila
    Returns:
            La info de toda la columna de la matriz en un str
    """
    texto = ''
    for indice_fila in range(len(matriz)):
        texto += f'{matriz[indice_fila][indice_col]},'
    texto = texto[:-1]
    return texto

def mostrar_matriz(matriz: list[list]) -> None:
    """
    Muestra la info de la matriz con cada campo separado por coma.
    
    Args:
        La matriz de datos
    
    Returns:
            None
    """
    cant_columnas = len(matriz[0])
    
    for indice_col in range(cant_columnas):
        texto = crear_texto_info_pokemon(matriz, indice_col)
        print(texto)

# Ejercicio 3 ------------------------------------------------------------------------------------
def calcular_promedio(matriz: list[list], indice_fila: int) -> float:
    promedio = 0
    if matriz:
        cantidad = len(matriz[indice_fila])
        suma = 0
        
        for numero in matriz[indice_fila]:
            suma += numero
        
        promedio = suma / cantidad
    return promedio

def obtener_indices_legendarios(matriz: list[list], indice_fila: int) -> list[int]:
    promedio = calcular_promedio(matriz, indice_fila)
    lista_indices = []
    
    print(f'El promedio de Poder es: {promedio:6.2f}')
    for indice_col in range(len(matriz[indice_fila])):
        if matriz[indice_fila][indice_col] > promedio:
            lista_indices.append(indice_col)
    return lista_indices

def obtener_indices_promedio_superior_v2(matriz: list[list], indice_fila: int) -> list[int]:
    promedio = calcular_promedio(matriz, indice_fila)
    # lista_indices = []
    
    print(f'El promedio de Poder es: {promedio:6.2f}')
    for indice_col in range(len(matriz[indice_fila])):
        if matriz[indice_fila][indice_col] > promedio:
            texto = crear_texto_info_pokemon(matriz, indice_col)
            print(texto)

def obtener_elemento_matriz(matriz_base: list[list], matriz_filtro: list[list], indice_col: int):
    for indice_fila in range(len(matriz_base)):
        elemento = matriz_base[indice_fila][indice_col]
        matriz_filtro[indice_fila].append(elemento)

def filtrar_matriz_poder_superior(matriz: list[list], indice_fila: int) -> list[list]:
    indices_superadores = obtener_indices_legendarios(matriz, indice_fila)
    matriz_filtrada = [[], [], [], [], []]
    
    for columna in indices_superadores:
        obtener_elemento_matriz(matriz, matriz_filtrada, columna)
            
    return matriz_filtrada

def filtrar_matriz_poder_superior_V2(matriz: list[list], indice_fila: int) -> None:
    obtener_indices_promedio_superior_v2(matriz, indice_fila)

# Ejercicio 4 ---------------------------------------------------

def obtener_indices_col_filtrado(matriz: list[list], indice_fila: int, elemento_buscar: str) -> list[int]:
    lista_indices = []
    
    for indice_col in range(len(matriz[indice_fila])):
        if matriz[indice_fila][indice_col] == elemento_buscar:
            lista_indices.append(indice_col)
    return lista_indices

def filtrar_matriz_pokemons(matriz: list[list], indice_fila: int, elemento_buscar: str) -> list[list]:
    indices_superadores = obtener_indices_col_filtrado(matriz, indice_fila, elemento_buscar)
    matriz_filtrada = [[], [], [], [], []]
    
    for columna in indices_superadores:
        obtener_elemento_matriz(matriz, matriz_filtrada, columna)
            
    return matriz_filtrada

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

# Ejercicio 6 ---------------------------------------------------
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