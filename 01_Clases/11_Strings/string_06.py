



texto = 'Esto es un texto de Java y necesito borrarlo'

# Esto es un texto y necesito borrarlo

# Usando find, slices, strip, f-string
a_borrar = 'de Java'
indice_inicio = texto.find(a_borrar)
cantidad_caracteres = len(a_borrar)

texto = texto.replace(a_borrar, '')

texto = f'{texto[0:indice_inicio].rstrip()}{texto[indice_inicio+cantidad_caracteres:].rstrip()}'



print(texto)