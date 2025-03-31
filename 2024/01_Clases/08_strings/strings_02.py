

mi_texto = 'Estamos aprendiendo strings'

primera_palabra = mi_texto[0:7]
print(primera_palabra)

input_usuario = input('Escriba una palabra: ')

esta_presente = input_usuario in mi_texto

print('La palabra del usuario esta presente: ', esta_presente)