
def selection_sort(lista_numerica: list[int]):
    for indice in range(len(lista_numerica)- 1):
        indice_minimo = indice

        for indice_2 in range(indice + 1, len(lista_numerica)):
            if lista_numerica[indice_2] < lista_numerica[indice_minimo]:
                indice_minimo = indice_2

        if indice_minimo != indice:
            lista_numerica[indice_minimo], lista_numerica[indice] =\
            lista_numerica[indice], lista_numerica[indice_minimo]
    return lista_numerica