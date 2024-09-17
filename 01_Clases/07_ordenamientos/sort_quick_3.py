
def quick_sort(lista_numerica: list[int]):
    
    if len(lista_numerica) < 2:
        return lista_numerica
    
    pivot = lista_numerica.pop()
    mas_chicos = []
    mas_grandes = []
    
    for numero in lista_numerica:
        if numero <= pivot:
            mas_chicos.append(numero)
        else:
            mas_grandes.append(numero)
    
    return quick_sort(mas_chicos) + [pivot] + quick_sort(mas_grandes)