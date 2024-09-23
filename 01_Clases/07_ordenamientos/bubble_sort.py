
def bubble_sort(lista_numeros: list[int], modo: str): # ASC | DES
    lista_copia = lista_numeros.copy()
    for indice in range(len(lista_copia) - 1):
        for sub_indice in range(indice + 1, len(lista_copia)):
            
            if (modo == 'ASC' and lista_copia[indice] > lista_copia[sub_indice] or 
                modo == 'DES' and lista_copia[indice] < lista_copia[sub_indice]):
                lista_copia[indice], lista_copia[sub_indice] =\
                lista_copia[sub_indice], lista_copia[indice]

    return lista_copia


if __name__ == '__main__':
    print(bubble_sort([5,2,8,15], 'DES'))