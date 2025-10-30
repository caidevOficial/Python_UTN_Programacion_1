import variables as var

nuevo_texto = 'Hola Mundo'
archivo = open(file='./mi_texto_2.txt', mode='w', encoding='UTF-8')


texto = archivo.write('Hola minions!')
print(f'Escribio {texto} caracteres')

archivo.close()