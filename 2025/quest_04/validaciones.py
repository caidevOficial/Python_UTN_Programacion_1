
def validar_input(min_str: str, max_str: str) -> str:
    opcion = input(f'Seleccione una opcion entre [{min_str} - {max_str}]: ').upper()
    
    while not (min_str <= opcion <= max_str):
        print('ERROR, elija una opcion correcta.')
        opcion = input(f'Seleccione una opcion entre [{min_str} - {max_str}]: ').upper()
    return opcion
    
    