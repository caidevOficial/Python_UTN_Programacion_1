import copy
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from auxiliar_visualizacion import (
    columnas, crear_matriz_visualizacion
)

# COMPORTAMIENTO DEL SHALLOW COPY CON LISTAS QUE TIENEN ELEMENTOS MUTABLES

# Listas MUTABLES
lista_e_mutable = [[1,2], [3,4], [5,6]]
lista_e_mutable_copy = copy.copy(lista_e_mutable)

matriz_ids = crear_matriz_visualizacion(lista_e_mutable, lista_e_mutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)

lista_e_mutable_copy[0][1] = 500
print(lista_e_mutable)
print(lista_e_mutable_copy)

matriz_ids = crear_matriz_visualizacion(lista_e_mutable, lista_e_mutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)
