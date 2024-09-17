from sort_burbujeo_1 import bubble_sort
from sort_selection_2 import selection_sort
from sort_quick_3 import quick_sort
from random import shuffle
import time

if __name__ == '__main__':
    lista_numerica_original = list(range(12000))
    shuffle(lista_numerica_original)
    print(lista_numerica_original[0:10])

    inicio = time.time()

    # lista_ordenada = bubble_sort(lista_numerica_original) # 7.90
    # lista_ordenada = selection_sort(lista_numerica_original) # 5.42
    lista_ordenada = quick_sort(lista_numerica_original) # 0.03
    
    fin = time.time()
    total = fin - inicio
    
    print(lista_ordenada[:30])
    print(f'Se tardó {total} tiempo')