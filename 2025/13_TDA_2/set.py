lista_tuplas = [
    ("Pepe", "Argento", 30),
    ("Moni", "Argento", 30),
    ("Paola", "Argento", 30),
    ("Fatiga", "Argento", 30)
]

nuevo_valor = 'Fatiga'

def agregar_a_tupla(tupla_original: tuple, nuevo_elemento: any) -> tuple:
    lista_tupla = list(tupla_original)
    if type(nuevo_elemento) in (list, tuple):
        lista_tupla.extend(nuevo_elemento)
    else:
        lista_tupla.append(nuevo_elemento)
    return tuple(lista_tupla)

for indice_tupla in range(len(lista_tuplas)):
    
    tupla_actual = agregar_a_tupla(lista_tuplas[indice_tupla], nuevo_valor)
    set_actual = set(tupla_actual)
    print(f'Tupla Actual {tupla_actual} | Set Actual {set_actual}')
    
    