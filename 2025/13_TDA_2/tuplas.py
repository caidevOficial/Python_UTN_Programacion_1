mi_tupla = ("Pepe", "Argento", 30)

barrio = ['Flores', 'CABA']

lista_tuplas = [
    ("Pepe", "Argento", 30),
    ("Moni", "Argento", 30),
    ("Paola", "Argento", 30),
    ("Fatiga", "Argento", 30)
]

# nombre, apellido, edad = mi_tupla
# print(nombre)
# print(apellido)
# print(edad)
# print(f'Tamaño tupla: {len(mi_tupla)}')

# for elemento in mi_tupla:
#     print(elemento)



def agregar_a_tupla(tupla_original: tuple, nuevo_elemento: any) -> tuple:
    lista_tupla = list(tupla_original)
    if type(nuevo_elemento) in (list, tuple):
        lista_tupla.extend(nuevo_elemento)
    else:
        lista_tupla.append(nuevo_elemento)
    
    # nueva_tupla = tupla_original + tuple(nuevo_elemento)
    return tuple(lista_tupla)

for indice_tupla_actual in range(len(lista_tuplas)):
    tupla_actual = lista_tuplas[indice_tupla_actual]
    nueva_tupla = agregar_a_tupla(tupla_actual, barrio)
    lista_tuplas[indice_tupla_actual] = nueva_tupla

for tupla in lista_tuplas:
    print(tupla)
    
