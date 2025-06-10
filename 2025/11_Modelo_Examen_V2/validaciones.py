
def validar_input(min: int, max: int) -> int:
    """
    Valida el input del usuario para que este dentro de un rango comprendido entre min y max,
    en caso de ingresar un valor incorrecto, se pedira nuevamente que se ingrese un valor
    
    Args:
        min: Valor minimo a evaluar
        max: Valor maximo a evaluar
    
    Returns:
            El valor validado parseado a entero
    
    """
    opcion = input(f'Ingrese un numero entre [{min}-{max}]: ')
    
    if opcion.isdigit() and (min <= int(opcion) <=  max):
        opcion_int = int(opcion)
    else:
        print('ERROR, ingrese nuevamente un numero')
        opcion_int = validar_input(min, max)
    return opcion_int
