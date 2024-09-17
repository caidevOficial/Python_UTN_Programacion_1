# [6,4,5,7,6]

def bubble_sort(lista_numerica: list[int]):
    for indice_1 in range(len(lista_numerica) - 1):
        for indice_2 in range(indice_1 + 1, len(lista_numerica)):
            if lista_numerica[indice_1] < lista_numerica[indice_2]:
                lista_numerica[indice_1], lista_numerica[indice_2] =\
                lista_numerica[indice_2], lista_numerica[indice_1]
    return lista_numerica
