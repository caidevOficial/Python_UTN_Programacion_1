"""

Necesito tomar datos para una veterinaria
    nombre mascota
    tipo mascota
    tamaño (cm)

con estos datos, determinar si es apto para un canil de altura 50cm

mostrar mensaje si la mascota es apta o no.
"""

es_acuatico = input('es acuatico? [s/n]: ')
nombre = input('nombre mascota: ')
altura = input('altura mascota (cm): ')
altura_int = int(altura)

mensaje = ''

if es_acuatico == 's' or altura_int > 50:
    mensaje = 'La mascota NO es apta'
else:
    mensaje = 'La mascota ES apta'

print(mensaje)