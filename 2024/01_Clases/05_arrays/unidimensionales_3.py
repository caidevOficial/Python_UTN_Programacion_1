def imprimir_estado_de_lista(lista_de_prueba: list):
    print(lista_de_prueba)
    print(hex(id(lista_de_prueba)))


lista_nombres_heroes = []

imprimir_estado_de_lista(lista_nombres_heroes)

lista_nombres_heroes = [
    "Deadpool", "Batman", "Spiderman", "Goku"
]

imprimir_estado_de_lista(lista_nombres_heroes)

lista_nombres_heroes[0] = "Shazam"
lista_nombres_heroes[-1] = "Vegeta"

# El append agrega elementos a la lista, siempre al final
lista_nombres_heroes.append("Saitama")

imprimir_estado_de_lista(lista_nombres_heroes)

print('\n\n')
for elemento in lista_nombres_heroes:
    print(hex(id(elemento)))


# for heroe in lista_nombres_heroes:
#     print(heroe)