
def quick_sort(lista_numeros: list[int]) -> list[int]:
    lista_copia = lista_numeros.copy()
    if len(lista_copia) < 2:
        return lista_copia
    
    pivot = lista_copia.pop()
    mas_chicos = []
    mas_grandes = []
    
    for numero in lista_copia:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)
    
    return quick_sort(mas_chicos) + [pivot] + quick_sort(mas_grandes)

# if __name__ == '__main__':
#     print(quick_sort([5,2,6,1], 'ASC'))