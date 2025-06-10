
import copy
from test_sorts import test_sort

def copiar_shallow(lista: list) -> list:
    lista_nueva = lista.copy()
    return lista_nueva

def copiar_deep(lista: list) -> list:
    lista_nueva = copy.deepcopy(lista)
    return lista_nueva

cantidad = 9000000
mi_lista_test = list(range(cantidad))


test_sort(copiar_shallow, mi_lista_test, sort_name='Shallow Copy')
test_sort(copiar_deep, mi_lista_test, sort_name='Deep Copy')