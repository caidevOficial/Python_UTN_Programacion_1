"""
Necesito tomar el nombre y la edad de una persona y poder saber
si la persona esta en edad de cobrar la jubilación

En caso de estar en esa edad, cobrará de premio $2000000

Caso contrario, cobrará $500000
"""

premio = 2000000


# Toma de datos y validación
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: ')) # 60 -> 110
genero = input('Ingrese su género: ')

"""
if ((genero == 'm' and edad < 65) or 
   (genero == 'f' and edad < 60) or
   (genero == 'nb' and edad < 60)):
    premio = 500000
"""


# Procesamiento
match genero:
    case 'm':
        if edad < 65:
            premio = 500000
    case 'f':
        if edad < 60:
            premio = 500000
    case _:
        print('Por favor ingrese una opcion entre m y f porque no puedo procesar mas opciones.')


# Informes
texto = f'Su nombre es {nombre}, tu género es {genero} y tu edad es {edad}.'\
    f' Te corresponde el premio de ${premio}'

print(texto)