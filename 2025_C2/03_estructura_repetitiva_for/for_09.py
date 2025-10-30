
"""
Ingresar un número. Determinar si el número es primo o no.
"""

numero_ingresado_str = input('Ingrese un numero: ')
numero_ingresado = int(numero_ingresado_str)

cantidad_divisores = 2
es_primo = True

for posible_divisor in range(2, numero_ingresado, 1):
    if numero_ingresado % posible_divisor == 0:
        cantidad_divisores += 1

        if cantidad_divisores > 2:
            es_primo = False
            break

mensaje =\
    f"""
    El numero {numero_ingresado}, ¿Es primo?: {es_primo}
    """
print(mensaje)