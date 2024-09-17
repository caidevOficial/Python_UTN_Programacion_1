


def suma_matrices(matriz_1: list[list], matriz_2: list[list]) -> list[list]:
    matriz_3 = []
    
    for fila in range(len(matriz_1)):
        fila_de_suma = []
        for columna in range(len(matriz_1[fila])):
            suma = matriz_1[fila][columna] + matriz_2[fila][columna]
            fila_de_suma.append(suma)
        matriz_3.append(fila_de_suma)
    return matriz_3

def mostrar_matriz(matriz: list[list]):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = matriz[fila][columna]
            print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')

matriz_1 = [
    [5, 4],
    [10, 15]
]

matriz_2 = [
    [15, 20],
    [50, -3]
]

matriz_3 = suma_matrices(matriz_1, matriz_2)
mostrar_matriz(matriz_3)