
# DES -> Mayor a Menor
def ordenar_selection_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):
        indice_de_elemento_mayor = indice
        
        for sub_indice in range(indice + 1, largo_lista):
            if mi_lista[indice_de_elemento_mayor] < mi_lista[sub_indice]:
                indice_de_elemento_mayor = sub_indice
        
        if indice_de_elemento_mayor != indice:
            auxiliar = mi_lista[indice_de_elemento_mayor]
            mi_lista[indice_de_elemento_mayor] = mi_lista[indice]
            mi_lista[indice] = auxiliar
    return mi_lista


# =======================
import random
from test_sorts import test_sort

cantidad = 20000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

test_sort(ordenar_selection_sort, mi_lista_test, sort_name='Selection Sort')