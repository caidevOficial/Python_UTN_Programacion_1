import copy
from UTN_Heroes_Dataset.utn_pp import mostrar_matriz_texto_tabla
from auxiliar_visualizacion import (
    columnas, crear_matriz_visualizacion
)


# COMPORTAMIENTO DEL SHALLOW COPY CON LISTAS QUE TIENEN ELEMENTOS INMUTABLES

# Listas INMUTABLES
lista_e_inmutable = ["pepe", "moni", "fatiga"]
lista_e_inmutable_copy = copy.copy(lista_e_inmutable)
lista_e_inmutable_copy = lista_e_inmutable.copy()
lista_e_inmutable_copy = lista_e_inmutable[:]


matriz_ids = crear_matriz_visualizacion(lista_e_inmutable, lista_e_inmutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)

lista_e_inmutable_copy[0] = 'Dardo'
matriz_ids = crear_matriz_visualizacion(lista_e_inmutable, lista_e_inmutable_copy)
mostrar_matriz_texto_tabla(matriz_ids, columnas)
