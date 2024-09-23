
def selection_sort(lista_numeros: list[int], modo: str):
    lista_copia = lista_numeros.copy()
    for indice in range(len(lista_copia) - 1):
        indice_minimo = indice
        for sub_indice in range(indice + 1, len(lista_copia)):
            if (modo == 'ASC' and lista_copia[indice_minimo] > lista_copia[sub_indice] or 
                modo == 'DES' and lista_copia[indice_minimo] < lista_copia[sub_indice]):
                indice_minimo = sub_indice
        
        if indice_minimo != indice:
            lista_copia[indice_minimo], lista_copia[indice] =\
            lista_copia[indice], lista_copia[indice_minimo]
            
    return lista_copia

if __name__ == '__main__':
    print(selection_sort([5,2,6,1], 'ASC'))