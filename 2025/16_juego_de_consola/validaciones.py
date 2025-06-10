def validar_nombre_usuario(mensaje: str, minimo: int, maximo: int) -> str:
    """
    Solicita al usuario que ingrese un nombre que tenga una cantidad de caracteres
    dentro del rango de `minimo` y `maximo`. En caso de no cumplir con la cantidad,
    volverá a pedir el input.
    
    :param mensaje: El mensaje a mostrar para pedir el input del usuario
    :param minimo: La cantidad minima de caracteres que debe tener el nombre
    :param maximo: La cantidad maxima de caracteres que debe tener el nombre
    :returns: El nombre del usuario.
    """
    while True:
        nombre = input(mensaje)
        if minimo <= len(nombre) <= maximo:
            return nombre
        print(f'El nombre debe contener entre [{min}-{max}] caracteres.')