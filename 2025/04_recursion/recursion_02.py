def validar_edad(edad_min: int, edad_max: int) -> int:
    edad_str = input(f'Ingrese su edad [{edad_min}-{edad_max}]: ')
    
    while not edad_str.isdigit() or not (edad_min <= int(edad_str) <= edad_max):
        edad_str = input(f'Error, le edad {edad_str} es inválida. Ingrese su edad [{edad_min}-{edad_max}]: ')
    edad_int = int(edad_str)
    return edad_int

def validar_edad_recursiva(edad_min: int, edad_max: int) -> int:
    edad_str = input(f'Ingrese su edad [{edad_min}-{edad_max}]: ')
    
    if not edad_str.isdigit() or not (edad_min <= int(edad_str) <= edad_max):
        print(f'Error, le edad {edad_str} es inválida.')
        edad_str = validar_edad_recursiva(edad_min, edad_max)
    
    if type(edad_str) == int:
        return edad_str
    else:
        edad_int = int(edad_str)
    return edad_int



edad = validar_edad_recursiva(18, 90)

print(f'Edad Correcta: {edad}')