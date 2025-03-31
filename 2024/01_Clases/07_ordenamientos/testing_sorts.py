from random import shuffle
from test_sorts import test_sort
from bubble_sort import bubble_sort
from selection_sort import selection_sort
from quick_sort import quick_sort


if __name__ == '__main__':
    cantidad_numeroes = 10000 # Decidimos la cantidad de numeros a generar
    lista_numeros = list(range(cantidad_numeroes)) # Creamos una lista de números
    shuffle(lista_numeros) # Desordenamos la lista de números
    print(lista_numeros[:20])
    
    """
    Para llamar a las funciones de la manera clásica será:
    
    modo = 'ASC' # (o sinó) modo = 'DES'
    lista_ordenada = bubble_sort(lista_numeros, modo)
    lista_ordenada = selection_sort(lista_numeros, modo)
    lista_ordenada = quick_sort(lista_numeros, modo)
    
    
    De forma que se vean los tiempos de ejecución, llamare a las funciones
    mediante la funcion test_sort, la cual se encarga de calcular el tiempo
    que tardan los ordenamientos.
    """
    
    test_sort(bubble_sort, lista_numeros, 'ASC', sort_name='Bubble-Sort')
    test_sort(selection_sort, lista_numeros, 'ASC', sort_name='Selection-Sort')
    test_sort(quick_sort, lista_numeros, sort_name='Quick-Sort')
    # quick_sort(lista_numeros)
