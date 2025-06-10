

def buscar_nombre_si_existe(lista_de_nombres: list, nombre_a_buscar: str) -> bool:
    
    for nombre in lista_de_nombres:
        if nombre == nombre_a_buscar:
            return True
    return False

def buscar_pares(lista_numeros: list) -> list:
    
    lista_auxiliar = []
    
    for numero in lista_numeros:
        if numero % 2 == 0:
            lista_auxiliar.append(numero)
    return lista_auxiliar



# ==================================
lista_nombres_vecinos = ["Goku", "Vegeta", "Pepe", "Dardo", "Moni"]
numeros = [
    1,2,3,4,5,6,7,8,9,10
]

# nombre_buscar = input('Ingrese un nombre para buscar: ')
# existe = buscar_nombre_si_existe(lista_de_nombres=lista_nombres_vecinos, nombre_a_buscar=nombre_buscar)


print(
    buscar_pares(numeros)
)


# print(
#     f'El nombre {nombre_buscar} existe? {existe}'
# )