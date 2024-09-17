def mostrar_matriz(matriz: list[list]):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = matriz[fila][columna]
            print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')

def inicializar_matriz_de(filas: int, columnas: int) -> list[list]:
    matriz = []
    
    for _ in range(filas):
        fila = [0] * columnas
        matriz.append(fila)
    return matriz

def cargar_matriz_secuencialmente(matriz: list[list]):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            dato = int(input(f'Ingrese un dato para Fila {fila} Columna {columna}: '))
            matriz[fila][columna] = dato

if __name__ == '__main__':
    matriz = inicializar_matriz_de(2,2)
    mostrar_matriz(matriz)
    cargar_matriz_secuencialmente(matriz)
    mostrar_matriz(matriz)