lista = [2,4,6,3,8,10,7,5,7,9,12]

set_primero = set(lista)

lista_sets = []


for i in range(5):
    lista_sets.append(set_primero.union(set("hola")))

lista_sets.sort()


for elemento in lista_sets:
    print(elemento)
