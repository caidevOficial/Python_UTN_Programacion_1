
def ordenar_quick_sort(mi_lista: list) -> list:
    
    if len(mi_lista) < 2:
        return mi_lista
    
    pivot =  mi_lista.pop()
    mas_chicos = []
    mas_grandes = []
    
    for numero in mi_lista:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)
    
    return ordenar_quick_sort(mas_grandes) + [pivot] + ordenar_quick_sort(mas_chicos)

# =======================
import random
from test_sorts import test_sort

cantidad = 4000000
mi_lista_test = list(range(cantidad))
random.shuffle(mi_lista_test)

test_sort(ordenar_quick_sort, mi_lista_test, sort_name='Quick Sort')