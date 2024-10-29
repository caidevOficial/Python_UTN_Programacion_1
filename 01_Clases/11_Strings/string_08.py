
texto = 'Hoy fue un día muy caluroso con temperaturas que alcanzaron los 29°C"\
    " y posiblemente hubo cortes de luz en algunas zonas del conurbano'

# 1 - reemplazar zonas por areas

# texto = texto.split('zonas')[0] + 'areas' + texto.split('zonas')[1]
texto = texto.replace('zonas', 'areas')

# 2 - Cortar/remover del texto donde aparece: posiblemente
# NO USAR REPLACE

texto = texto.split('posiblemente ')[0] + texto.split('posiblemente ')[1]

# 3 - imprimir el texto palabra por palabra 

palabras = texto.split()

for palabra in palabras:
    print(palabra)

