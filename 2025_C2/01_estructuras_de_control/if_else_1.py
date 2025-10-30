"""
Necesito tomar por consola:
    # el nombre
    # la edad
    # si tiene analítico secundario [s/n]

    Para saber si esta en condiciones de arrancar con el curso de Python.

En caso de ser mayor de 18 años, tengo que verificar que tenga titulo.
En caso de tener titulo, mostrar en consola que esta en condiciones de realizar el curso.
    Caso contrario, mostrar en consola que cosa le falta.

En caso de ser menor, no tengo que averiguar si tiene titulo.
"""

# Toma de datos
nombre = input('Ingrese su nombre: ')
edad = input('Ingrese su edad: ')
edad_int = int(edad)
tiene_analitico = input('Posee analitico secundario? [s/n]: ')
mensaje = ''

# Analisis de datos

# Version 1
if edad_int >= 18 and tiene_analitico == 's':
    mensaje = 'Esta en condiciones de anotarse al curso de Python.'
elif edad_int >= 18:
    mensaje = 'El analítico es requisito indispensable para anotarse al curso de Python.'
else:
    mensaje = 'Debes ser mayor de edad y tener el titulo analítico para anotarse al curso de Python.'

# Vista de mensajes
print(mensaje)
