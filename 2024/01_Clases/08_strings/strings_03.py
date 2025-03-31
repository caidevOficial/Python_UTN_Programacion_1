mi_texto = 'Estamos aprendiendo strings'
nuevo_texto = 'en la UTN'

# Estamos aprendiendo strings en la UTN

cantidad_de_caracteres = len(mi_texto)
print(cantidad_de_caracteres)

# Usar la concatenacion mediante el operador +
# Usar la concatenacion mediante el operador %s
# Usar la concatenacion con el metodo format
# Usar la concatenacion mediante la interpolación de strings / f-string

# Con operador +
texto_concatenado = mi_texto + nuevo_texto

# Con mascaras
texto_concatenado = '%s %s %s' % (mi_texto, nuevo_texto, 'y es el 2024')

# # Con metodo format
texto_concatenado = '{1} {0} {2}'.format(nuevo_texto, mi_texto, 'y es el año 2024')
texto_concatenado = '{texto_1} {texto_2} {texto_3}'.format(texto_1=mi_texto, texto_2=nuevo_texto, texto_3='y es el año 2024')

# Con interpolación de string / f-strings
# 'y es el año 2024'
texto_concatenado = f'{mi_texto} {nuevo_texto} {"y es el año 2024"}'

print(texto_concatenado)