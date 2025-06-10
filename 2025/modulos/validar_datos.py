def validar_edad(edad):
    """
    Reciba una edad en formato string, valida que este formada por numeros y que 
    numericamente sea mayor o igual a 18. En caso de cumplir, 
    retorna la edad parseada a entero.
    """
    while not edad.isdigit() or (int(edad) < 18):
        edad = input(f'Ingrese la edad del cliente [Solo mayores de 18 años]: ')
    edad_int = int(edad)
    return edad_int

def validar_numero_entre(numero, min, max):
    """
    Valida que el usuario ingrese un numero entre un rango determinado [min y max]
    Retorna el numero dentro del rango permitido, parseado a entero
    """
    while not numero.isdigit() or not (min <= int(numero) <= max):
        numero = input(f'Ingrese un numero valido entre {min} y {max}: ')
    numero_int = int(numero)
    return numero_int

def validar_nombre_o_apellido(nombre_o_apellido: str, mensaje: str) -> str:
    """
    Valida que el nombre o apellido contenga solamente letras.
    
    Args:
        nombre_o_apellido: la palabra a evaluar
        mensaje: El texto a mostrar en caso de error
    Returns:
        La palabra validada en caso de exito.
    """
    while not nombre_o_apellido.isalpha():
        nombre_o_apellido = input(mensaje)
    return nombre_o_apellido