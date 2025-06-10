lista = [2,4,6,3,8,10,7,5,7,9,12]

set_primero = set(lista)
set_segundo = set([1,3,5,7,9])
set_nuevo = {12}

# set_tercero = set_primero.union(set_segundo)
# set_tercero = set_primero.intersection(set_segundo)
# set_primero.intersection_update(set_segundo, set_nuevo)
# set_tercero = set_primero.difference(set_segundo)
# elemento = set_primero.pop()



def set_pop(set_actual: set, index: int) -> tuple[set,any]:
    elemento_elegido = None
    indice_actual = 0
    nuevo_set = set()
    
    if index > (len(set_actual) -1):
        index = len(set_actual) -1
    elif index < 0:
        index = len(set_actual) + index
    # manejar indices negativos
    
    for elemento in set_actual:
        if indice_actual == index:
            elemento_elegido = elemento
        else:
            nuevo_set.add(elemento)
        indice_actual += 1
    return (nuevo_set, elemento_elegido)
    
print(set_primero)
print(set_pop(set_primero, 30))
