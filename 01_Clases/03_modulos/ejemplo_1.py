nombre = 'UTN'


def calcular_precio_con_iva(precio_sin_iva: float, iva=21) -> float:
    """Calcula el IVA de un precio, con un valor 
    por defecto del 21% y retorna el precio con IVA.

    precio_sin_iva (float): _description_ El Precio del producto 
        sin IVA agregado
    iva (int, optional): _description_. El IVA a sumar, por defecto 
        es opcional y 21.

    Retorna el precio base con el iva agregado, para cumplir con la ley.
    """
    print(nombre)
    resultado = precio_sin_iva * (1 + iva/100)
    return resultado

def calcular_medio_aguinaldo(salario: float) -> float:
    """Calcula medio aguinaldo en base al salario ingresado
    por parámetro y lo retorna.

    Args:
        salario (float): _description_ Es el salario de la persona trabajadora
            que se usara para calcular el medio aguinaldo

    Returns:
        _type_: _description_ El aguinaldo calculado en base al salario.
    """
    print(nombre)
    resultado = salario / 2
    return resultado


# Toma de dato
medio_iva = 10.5
precio_combo_whooper_doble = 9500.0
# precio_sin_iva = float(
#     input(f'Ingrese un valor para calcular el IVA del {iva}%: $'))
# Transformacion de datos
precio_con_iva = calcular_precio_con_iva(iva=medio_iva, precio_sin_iva=precio_combo_whooper_doble)

# Creando un output
mensaje = f'El valor con IVA del {medio_iva}% de ${precio_combo_whooper_doble} es de: ${precio_con_iva}'

# Mostrando al usuario la salida
print(mensaje)
