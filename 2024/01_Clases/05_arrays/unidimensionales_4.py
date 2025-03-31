
numeros_de_la_quiniela = [0, 87, 5, 14, 48, 91]

# Sumarlos y sacar su promedio

def suma_numeros_lista(lista: list) -> int:
    suma = 0
    for numero in lista:
        suma += numero
    return suma


def promedio(lista: list) -> float:
    cantidad_numeros = len(lista)
    suma = suma_numeros_lista(lista)
    promedio = suma / cantidad_numeros
    
    return promedio


promedio_numeros = promedio(numeros_de_la_quiniela)

print(promedio)
