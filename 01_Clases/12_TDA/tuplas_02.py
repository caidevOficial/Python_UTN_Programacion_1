
sub_lista = ["Universidad", "UTN"]
mi_lista = [sub_lista, "Pepe", 55, "Buenos Aires", 1.70, 55, 55, 'Pepe']

tupla_auxiliar = (4, 5, 8)

# input_usuario = input('Escriba una palabra: ')

indice = mi_lista.index("Buenos Aires")
cantidad = mi_lista.count(55)
# print(cantidad)

mi_otra_tupla = tuple(mi_lista)

mi_otra_tupla[0][1] = "Facultad"

print(mi_otra_tupla)
