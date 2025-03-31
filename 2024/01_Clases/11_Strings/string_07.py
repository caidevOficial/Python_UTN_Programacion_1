
texto = 'Esto es un texto de Java y necesito borrarlo'


a_borrar = 'de Java'
texto_spliteado = texto.split(a_borrar)
    
for indice in range(len(texto_spliteado)):
    texto_spliteado[indice] = texto_spliteado[indice].strip()

print(texto_spliteado)

texto = ' '.join(texto_spliteado)
texto = ' '.join([texto_spliteado[0].strip(), texto_spliteado[1].strip()])


print(texto)