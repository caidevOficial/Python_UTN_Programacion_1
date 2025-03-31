

def pedir_nombre() -> str:
    nombre = None
    while not nombre or len(nombre) < 2:
        nombre = input('Ingrese el nombre del pokemon: ')
    
    return nombre
    