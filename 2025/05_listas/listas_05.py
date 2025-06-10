lista_nombres = [
    "Pepe", "Fatiga", "Moni", "Mario Bross", "El Luigi"
]


# indice = 4
# while indice >= 0:
#     print(lista_nombres[indice])
#     indice -= 1

cantidad_elementos = len(lista_nombres)
print(cantidad_elementos)


largo_de_lista = len(lista_nombres)
for indice in range(largo_de_lista):
    texto = f"{lista_nombres[indice]}"
    print(texto)
    

for nombre in lista_nombres:
    print(nombre)