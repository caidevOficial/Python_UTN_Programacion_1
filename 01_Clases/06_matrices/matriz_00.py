nombres = ["pepe", "moni", "dardo"]
edades = [56, 42, 49]
altura_cm = [175, 168, 180]

matriz_datos = [
    ["pepe", "moni", "dardo", "paola"],
    [56,      42,     49,      18],
    [175,     168,    180,     160],
    ["Fatiga", 15, 60]
]

# for fila in matriz_datos:
#     print(fila)

for fila in range(len(matriz_datos)):
    columnas = len(matriz_datos[fila])
    
    for columna in range(columnas):
        print(matriz_datos[fila][columna], end=' | ')
    print(' ')