matriz_datos = [
    ["pepe", "moni", "dardo", "paola"], # F0
    [56,      42,     49,      18], # F1
    [175,     168,    180,     160] # F2
]


# matriz: Fila -> Columna
fila = 0
columna = 2
matriz_datos[fila][columna] = 'Coqui'


for fila in range(len(matriz_datos)):
    for columna in range(len(matriz_datos[fila])):
        dato = matriz_datos[fila][columna]
        print(f'Fila: {fila} | Columna: {columna} | Dato: {dato}')