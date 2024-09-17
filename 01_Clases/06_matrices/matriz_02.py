

def inicializar_matriz_de(filas: int, columnas: int) -> list[list]:
    matriz = []
    
    for _ in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz


matriz = inicializar_matriz_de(4,8)

for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        print(matriz[fila][columna], end=' ')
    print(' ')
