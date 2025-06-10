frutas = [
    "kiwi",
    "naranja",
    "mandarina",
    "manzana",
    "melon",
    "manzana",
    "pera"
]


# fruta_elegida = 'pera'


# for indice in range(frutas.index(fruta_elegida)):
    
#     if frutas[indice] == 'kiwi':
#         fruta_elegida = frutas[indice + 2]
#     print(frutas[indice])

print(frutas)

# frutas.reverse()

indice_a_borrar = frutas.index("manzana")
del frutas[0:3]
# # frutas.remove('naranja')

for i in range(3):
    frutas.pop(0)
    
    
# frutas.pop(indice_a_borrar)

print(frutas)