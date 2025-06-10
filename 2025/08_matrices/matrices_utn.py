
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
        fila = [valor_default] * cant_columnas # 4
        matriz_resultante.append(fila)
    return matriz_resultante

def mostrar_matriz(matriz: list[list]) -> None:
    """
    
    """
    
    for indice_fila in range(len(matriz)):
        
        lista_fila = matriz[indice_fila]
        for indice_columna in range(len(lista_fila)):
            
            # dato = matriz[indice_fila][indice_columna]
            dato = lista_fila[indice_columna]
            
            print(dato, end=' ')
        print("")

def buscar_valor_en_matriz(matriz: list[list], valor_a_buscar: int, unica_ocurrencia: bool = False) -> None:
    for indice_fila in range(len(matriz)):
        lista_fila = matriz[indice_fila]
        
        for indice_columna in range(len(lista_fila)):
            if lista_fila[indice_columna] == valor_a_buscar:
                mensaje =\
                    f"""El valor {valor_a_buscar} esta en la coordenada ({indice_fila},{indice_columna})"""
                print(mensaje)
                if unica_ocurrencia == True:
                    return

def validar_mismo_tamanio_matriz(matriz_a: list[list], matriz_b: list[list]) -> bool:
    
    # if len(matriz_a) > 0 and len(matriz_b) > 0:
    if matriz_a and matriz_b:
        filas_a = len(matriz_a)
        filas_b = len(matriz_b)
        igualdad_filas = filas_a == filas_b
        # Validar la cantidad de columnas de cada matriz
        return igualdad_filas
    else:
        return False
    
def sumar_matrices(matriz_a: list[list], matriz_b: list[list]) -> list[list]:
    
    matriz_resultante = []
    if validar_mismo_tamanio_matriz(matriz_a, matriz_b):
        matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_a[0]), None)
        for indice_fila in range(len(matriz_a)):
            for indice_columna in range(len(matriz_a[indice_fila])):
                resultado = matriz_a[indice_fila][indice_columna] + matriz_b[indice_fila][indice_columna]
                matriz_resultante[indice_fila][indice_columna] = resultado    
    else:
        print('ERROR: Las matrices no tienen el mismo tamaño.')

    return matriz_resultante

def multiplicar_matriz_por_escalar(matriz_a: list[list], escalar: int) -> list[list]:
    
    matriz_resultante = inicializar_matriz(len(matriz_a), len(matriz_a[0]), None)
    # Recorrer filas X columnas
    for indice_fila in range(len(matriz_a)):
        for indice_columna in range(len(matriz_a[indice_fila])):
            # resultado = matriz_a[indice_fila][indice_columna] + matriz_b[indice_fila][indice_columna]
            resultado = matriz_a[indice_fila][indice_columna] * escalar
            matriz_resultante[indice_fila][indice_columna] = resultado 

    return matriz_resultante
            

def crear_matriz_t(matriz_a: list[list]) -> list[list]:
    # Recorrer columnas X filas
    cant_columnas = len(matriz_a[0])
    cant_filas = len(matriz_a)
    matriz_resultante = inicializar_matriz(cant_columnas, cant_filas, None)
    
    for indice_columna in range(cant_columnas):
        for indice_fila in range(cant_filas):
            matriz_resultante[indice_columna][indice_fila] = matriz_a[indice_fila][indice_columna]

    return matriz_resultante

            



# matriz = inicializar_matriz(10, 9, 0)

# matriz[2][6] = 1
# matriz[5][4] = 1
# matriz[7][0] = 1
# matriz[0][0] = 1
# matriz[9][8] = 1

# mostrar_matriz(matriz)

# buscar_valor_en_matriz(matriz, valor_a_buscar=1, unica_ocurrencia=False)

matriz_1 = [
    [1,10,100],    # 0   ->
    [3,30,300],    # 1
    [5,50,500],    # 2
    [7,70,700]
]


matriz_2 = [
    [2,2,2],
    [4,4,10]
]



from utn_fra.datasets import (
    lista_autos_marcas,
    lista_autos_modelos,
    lista_autos_precios,
    lista_autos_cantidades
)

matriz_autos = [
    lista_autos_marcas,
    lista_autos_modelos,
    lista_autos_precios,
    lista_autos_cantidades
]


matriz_resultante = crear_matriz_t(matriz_autos)
matriz_resultante.insert(0, ['Marca', 'Modelo', 'Precio', 'Cantidad'])
mostrar_matriz(matriz_resultante)
