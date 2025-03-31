import copy
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from auxiliar_visualizacion import (
    columnas, crear_matriz_visualizacion
)

lista_e_mutable = [[1,2], [3,4], [5,6]]
lista_e_mutable_copy = copy.deepcopy(lista_e_mutable)

matriz_ids = crear_matriz_visualizacion(lista_e_mutable, lista_e_mutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)


# Sacamos el primer elemento de la lista copia
lista_e_mutable_copy.pop(0)
matriz_ids = crear_matriz_visualizacion(lista_e_mutable, lista_e_mutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)