mi_texto = 'Estamos aprendiendo strings en la UTN'

# for caracter in mi_texto:
#     print(caracter, end='')

for indice in range(len(mi_texto)):
    mensaje = f'Indice: {indice:02} | Caracter: {mi_texto[indice]}'
    print(mensaje)