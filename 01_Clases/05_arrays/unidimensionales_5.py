lista_nombres = []


def cargar_lista_nombres(lista_de_nombres: list) ->None:
    if type(lista_de_nombres) == list:
        for i in range(3):
            nombre= input(f'Decime el {i+1}° nombre a cargar: ')
            lista_de_nombres.append(nombre)
    else:
        print('No puedo modificar algo que no sea una lista')


print(lista_nombres)
cargar_lista_nombres(lista_nombres)

_ = input('...')

print(lista_nombres)

