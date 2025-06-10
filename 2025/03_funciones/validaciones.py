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

def validar_existencia(input_usuario, palabra_1, palabra_2, palabra_3):
    while not input_usuario.isalpha() or\
        (input_usuario != palabra_1 and input_usuario != palabra_2 and input_usuario != palabra_3):
        input_usuario = input(
            f'Ingrese un valor valido entre: [{palabra_1}, {palabra_2}, {palabra_3}]: ').capitalize()
    return input_usuario

def validar_numero_entre(numero, min, max):
    """
    Valida que el usuario ingrese un numero entre un rango determinado [min y max]
    Retorna el numero dentro del rango permitido, parseado a entero
    """
    while not numero.isdigit() or not (min < int(numero) < max):
        numero = input(f'Ingrese un numero valido entre {min} y {max}: ')
    numero_int = int(numero)
    return numero_int

# =====================================
