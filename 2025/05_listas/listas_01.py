# lista_de_nombres = []
lista_de_nombres = list()

for vuelta in range(3):
    nombre = input(f'Escribe el {vuelta+1}° nombre: ')
    lista_de_nombres.append(nombre)

print(lista_de_nombres)