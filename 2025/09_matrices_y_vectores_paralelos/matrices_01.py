from utn_fra.datasets import (
    matriz_concesionaria
)


matriz_concesionaria[4] = [float(matriz_concesionaria[2][indice_col] * matriz_concesionaria[3][indice_col]) for indice_col in range(20)]

# matriz plana, sin trasponer
def buscar_en_matriz(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> int:
    indice_encontrado = -1
    indice = 0
    
    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            indice_encontrado = indice
            break
        indice += 1

    return indice_encontrado

def buscar_en_matriz_v2(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> list[int]:
    lista_indices_encontrados = []
    indice = 0
    
    while indice < len(matriz[indice_donde_buscar]):
        if matriz[indice_donde_buscar][indice] == valor_a_buscar:
            lista_indices_encontrados.append(indice)
            
        indice += 1

    return lista_indices_encontrados

def mostrar_informacion_de_autos(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str) -> None:
    lista_indices = buscar_en_matriz_v2(matriz, indice_donde_buscar, valor_a_buscar)
    
    for indice_columna in range(len(lista_indices)):
        
        indice_elegido = lista_indices[indice_columna]
        
        texto = ''
        for indice_fila in range(len(matriz)):
            
            dato = matriz[indice_fila][indice_elegido]
            if type(dato) == str:
                texto = f'{texto} | {dato:10}'
            elif type(dato) == int: # float
                texto = f'{texto} | {dato:07}'
            elif type(dato) == float: # float
                texto = f'{texto} | {dato:7.2}'
        texto = f'{texto} |'
        
        print(texto)

def inicializar_matriz(cant_filas: int, cant_columnas: int, valor_default: int) -> list[list]:
    """
    Crea una matriz de dimensiones cant_filas X cant_columnas y la inicializa con un valor
    definido por el usuario.
    
    Args:
        cant_filas: La cantidad de filas de la matriz
        cant_columnas: La cantidad de columnas de la matriz
        valor_default: El valor el cual estara dentro de cada celda de la matriz
    Returns:
            Retorna una matriz inicializada de tamaño cant_filas X cant_columnas
    """
    matriz_resultante = []
    
    for indice in range(cant_filas):
        
        # [True]
        fila = [valor_default] * cant_columnas # 4
        # [True, True, True, True]
        matriz_resultante.append(fila)
    return matriz_resultante

def crear_matriz_traspuesta(matriz_a: list[list]) -> list[list]:
    # Recorrer columnas X filas
    cant_columnas = len(matriz_a[0])
    cant_filas = len(matriz_a)
    matriz_resultante = inicializar_matriz(cant_columnas, cant_filas, None)
    
    for indice_columna in range(cant_columnas):
        for indice_fila in range(cant_filas):
            matriz_resultante[indice_columna][indice_fila] = matriz_a[indice_fila][indice_columna]

    return matriz_resultante

def ss_ordenar_matriz(matriz: list[list], indice_a_ordenar: int) -> list[list]:
    # Traspuesta
    
    for indice_fila in range(len(matriz) -1):
        indice_elemento_mas_grande = indice_fila
        
        for indice_sig_fila in range(indice_fila + 1, len(matriz)):
            if matriz[indice_elemento_mas_grande][indice_a_ordenar] < matriz[indice_sig_fila][indice_a_ordenar]:
                indice_elemento_mas_grande = indice_sig_fila
        
        if indice_elemento_mas_grande != indice_fila:
            auxiliar = matriz[indice_elemento_mas_grande]
            matriz[indice_elemento_mas_grande] = matriz[indice_fila]
            matriz[indice_fila] = auxiliar
    return matriz

def filtrar_matriz_por_valor(matriz_traspuesta: list[list], indice_donde_buscar: int, valor_a_buscar: str):
    matriz_resultante = []
    indice_fila_actual = 0
    
    while indice_fila_actual < len(matriz_traspuesta):
        
        if matriz_traspuesta[indice_fila_actual][indice_donde_buscar] == valor_a_buscar:
            matriz_resultante.append(matriz_traspuesta[indice_fila_actual])
        
        indice_fila_actual += 1
        
    # for fila in matriz_traspuesta:
    #     if fila[indice_donde_buscar] == valor_a_buscar:
    #         matriz_resultante.append(fila)
    
    return matriz_resultante

def buscar_en_matriz_v3(matriz: list[list], indice_donde_buscar: int, valor_a_buscar: str, indice_a_ordenar: int) -> list[list]:
    
    matriz_traspuesta = crear_matriz_traspuesta(matriz)
    matriz_traspuesta = ss_ordenar_matriz(matriz_traspuesta, indice_a_ordenar=indice_a_ordenar)
    matriz_resultante = filtrar_matriz_por_valor(matriz_traspuesta, indice_donde_buscar, valor_a_buscar)

    return matriz_resultante
    
def mostrar_matriz(matriz_t: list[list], valor_a_buscar: str = None) -> None:
    
    if not matriz_t:
        if valor_a_buscar:
            msj_error = f'ERROR, No se encontro {valor_a_buscar} en el set de datos.'
        else:
            msj_error = f'ERROR, No se encontro el valor en el set de datos.'
        print(msj_error)
    else:
    
        for fila in range(len(matriz_t)):
            texto = ''
            for columna in range(len(matriz_t[fila])):
                dato = matriz_t[fila][columna]
                if type(dato) == float: # float
                    texto = f'{texto} | {dato:08.1f}'
                elif type(dato) == str:
                    texto = f'{texto} | {dato:10}'
                elif type(dato) == int:
                    texto = f'{texto} | {dato:5}'
                else:
                    texto = f'{texto} | {dato}'
            texto = f'{texto} |'
            
            print(texto)
            

"""
def ordenar_selection_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):
        indice_de_elemento_mayor = indice
        
        for sub_indice in range(indice + 1, largo_lista):
            if mi_lista[indice_de_elemento_mayor] < mi_lista[sub_indice]:
                indice_de_elemento_mayor = sub_indice
        
        if indice_de_elemento_mayor != indice:
            auxiliar = mi_lista[indice_de_elemento_mayor]
            mi_lista[indice_de_elemento_mayor] = mi_lista[indice]
            mi_lista[indice] = auxiliar
    return mi_lista
"""


            
    
    
    
    

def buscar_y_mostrar_datos(matriz_base: list[list], indice_donde_buscar: int, valor_a_buscar: str, indice_a_ordenar: int = 4) -> None:
    matriz_filtrada = buscar_en_matriz_v3(matriz_base, indice_donde_buscar, valor_a_buscar, indice_a_ordenar)
    mostrar_matriz(matriz_filtrada, valor_a_buscar)




# print(buscar_en_matriz_v2(matriz_concesionaria, indice_donde_buscar=1, valor_a_buscar='Argo'))
# mostrar_informacion_de_autos(matriz_concesionaria, indice_donde_buscar=1, valor_a_buscar='Argo')

buscar_y_mostrar_datos(matriz_base=matriz_concesionaria, indice_donde_buscar=2, valor_a_buscar=8, indice_a_ordenar=4)

from utn_fra.datasets import matriz_data_heroes_small

"""
matriz_data_heroes_small = [
    lista_nombres_heroes_small,
    lista_identidades_heroes_small,
    lista_apodos_heroes_small,
    lista_generos_heroes_small,
    lista_poder_heroes_small,
    lista_alturas_heroes_small
]
"""