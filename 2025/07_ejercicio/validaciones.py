
def validar_numero(num_min: int, num_max: int) -> int:
    opcion_str = input(f'Ingrese su opción [{num_min}-{num_max}]: ')
    
    while not opcion_str.isdigit() or not (num_min <= int(opcion_str) <= num_max):
        opcion_str = input(f'Error, la opción {opcion_str} es inválida. Ingrese una opción [{num_min}-{num_max}]: ')
    opcion_int = int(opcion_str)
    return opcion_int