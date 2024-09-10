
def validar_atributo(minimo: int, maximo: int, tipo_attr: str) -> int:
    atributo = None
    
    while (not atributo or not atributo.isdigit() or 
            (int(atributo) > maximo or int(atributo) < minimo)):
        atributo = input(f'Ingrese el {tipo_attr} del pokemon: ')
    
    atributo_int = int(atributo)
    return atributo_int