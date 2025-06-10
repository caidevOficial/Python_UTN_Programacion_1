
# lista numeros
# [8,4,3,12,0] # DES

def ordenar_bubble_sort(mi_lista: list) -> list:
    
    largo_lista = len(mi_lista)
    for indice in range(largo_lista - 1):
        for sub_indice in range(indice + 1,largo_lista):
            if mi_lista[indice] < mi_lista[sub_indice]:
                auxiliar = mi_lista[indice]
                mi_lista[indice] = mi_lista[sub_indice]
                mi_lista[sub_indice] = auxiliar
    return mi_lista

# =======================
import random
from test_sorts import test_sort

cantidad = 15000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

test_sort(ordenar_bubble_sort, mi_lista_test, sort_name='Bubble Sort')
