"""
Necesito tomar por consola:
    # el nombre
    # la edad
    # género [m/f]

    Para saber si esta en condiciones de cobrar la jubilación.

# En caso de ser género f, la edad tiene que superar 60 años
# En caso de ser género m, la edad debe superar 65 años.
# En caso de no tener la edad minima para ninguna categoría, no se evaluará nada más

Mostrar un mensaje para cada uno de los casos.
"""

# Toma de datos
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
edad_int = int(edad)
genero = input('Ingrese su género [f/m]: ')
mensaje = ''

# Genero

puede_cobrar_msj = f'{nombre} Es género {genero} y esta en condiciones de cobrar la jubilación'
no_puede_cobrar_msj = f'{nombre} Es género {genero} y NO esta en condiciones de cobrar la jubilación'

match genero:
    case 'f':
        if edad_int > 59:
            # f-strings
            mensaje = puede_cobrar_msj
        else:
            mensaje = no_puede_cobrar_msj

    case 'm':
        if edad_int > 64:
            mensaje = puede_cobrar_msj
        else:
            mensaje = no_puede_cobrar_msj

print(mensaje)
