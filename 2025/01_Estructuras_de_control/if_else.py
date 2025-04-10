

"""
Necesito tomar el nombre y la edad de una persona y poder saber
si la persona esta en edad de cobrar la jubilación

En caso de estar en esa edad, cobrará de premio $2000000

Caso contrario, cobrará $500000
"""
# If/Else
nombre = input('Ingrese su nombre: ')
edad = int(input('Ingrese su edad: '))
genero = input('Ingrese su género: ')


premio = 2000000

if genero == 'm' and edad >= 65:
    pass
elif edad >= 60 and genero == 'f':
    pass
else:
    premio = 500000


if ((genero == 'm' and edad < 65) or 
   (genero == 'f' and edad < 60)):
    premio = 500000

texto = f'Su nombre es {nombre}, tu género es {genero} y tu edad es {edad}.'\
    f' Te corresponde el premio de ${premio}'

print(texto)




# Match

