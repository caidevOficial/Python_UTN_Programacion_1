

frutas = [
    "kiwi",
    "naranja",
    "mandarina",
    "manzana",
    "melon",
    "manzana",
    "pera"
]


# frutas_copia = frutas.copy()
# frutas_copia[0] = 'sandia'

# frutas.append('tomate')

# frutas_copia.remove('manzana')

# print(frutas)
# print(frutas_copia)

# numeros = [
#     2,4,6,8,10,12
# ]

# numeros_copia = numeros.copy()


# numeros_copia[0] = 100
# print(numeros)


# print(numeros_copia)

matriz = [
    [56, 12],
    [14, 90],
    [48, -25],
    [38, -12]
]

matriz_copia = matriz.copy()

# matriz[0][0] = 100
# matriz_copia[0] = ['Pepe', 'Moni']

# matriz_copia.append(['Pepe', 'Moni'])
# del matriz_copia[3]
# matriz_copia[3][0] = 'Paola'

import copy


matriz_deepcopy = copy.deepcopy(matriz)

matriz.sort()


print('ORIGNAL ', matriz)
print('COPIA ', matriz_copia)

# for indice_fila in range(len(matriz)):
    
#     dir_mem_ori = hex(id(matriz[indice_fila]))
#     dir_mem_cop = hex(id(matriz_copia[indice_fila]))
#     dir_mem_deep = hex(id(matriz_deepcopy[indice_fila]))
    
#     print(f'Direccion memoria FILA: {dir_mem_ori} | {dir_mem_cop} | {dir_mem_deep}')
#     for indice_columna in range(len(matriz[indice_fila])):
        
#         dir_mem_ori_col = hex(id(matriz[indice_fila][indice_columna]))
#         dir_mem_cop_col = hex(id(matriz_copia[indice_fila][indice_columna]))
#         dir_mem_deep_col = hex(id(matriz_deepcopy[indice_fila][indice_columna]))
        
#         print(f'Direccion memoria COLU: {dir_mem_ori_col} | {dir_mem_cop_col} | {dir_mem_deep_col}')



# print(matriz)
# print(matriz_deepcopy)

# matriz_copia[0][0] = 100

# print(matriz)
# print(matriz_deepcopy)

# print(
#     hex(id(matriz)),
#     hex(id(matriz_copia)),
#     hex(id(matriz_deepcopy)), sep='\n'
# )