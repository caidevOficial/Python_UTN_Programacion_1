from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
import copy
columnas = ['ID Original', 'ID Copia']
lista_e_mutable = [[1,2], [3,4], [5,6]]
lista_e_mutable_copy = copy.deepcopy(lista_e_mutable)

"""
O: [[1,2], [3,4], [5,6]]
C: [[1,2], [3,4]]
CD: [[1,2], [3,4]]


"""
matriz_ids = []
direccion_o = hex(id(lista_e_mutable))
direccion_c = hex(id(lista_e_mutable_copy))
matriz_ids.append([direccion_o, direccion_c])

for indice in range(len(lista_e_mutable)):
    direccion_o = hex(id(lista_e_mutable[indice]))
    direccion_c = hex(id(lista_e_mutable_copy[indice]))
    matriz_ids.append([direccion_o, direccion_c])
    for indice_sub in range(len(lista_e_mutable[indice])):
        direccion_o = hex(id(lista_e_mutable[indice][indice_sub]))
        direccion_c = hex(id(lista_e_mutable_copy[indice][indice_sub]))
        matriz_ids.append([direccion_o, direccion_c])

mostrar_matriz_texto_tabla(matriz_ids, columnas)

matriz_ids = []
lista_e_mutable_copy.pop()

print(lista_e_mutable)
print(lista_e_mutable_copy)

direccion_o = hex(id(lista_e_mutable))
direccion_c = hex(id(lista_e_mutable_copy))
matriz_ids.append([direccion_o, direccion_c])

for indice in range(len(lista_e_mutable_copy)):
    direccion_o = hex(id(lista_e_mutable[indice]))
    direccion_c = hex(id(lista_e_mutable_copy[indice]))
    matriz_ids.append([direccion_o, direccion_c])
    for indice_sub in range(len(lista_e_mutable[indice])):
        direccion_o = hex(id(lista_e_mutable[indice][indice_sub]))
        direccion_c = hex(id(lista_e_mutable_copy[indice][indice_sub]))
        matriz_ids.append([direccion_o, direccion_c])

mostrar_matriz_texto_tabla(matriz_ids, columnas)