
def poner_en_mayusculas(texto: str):
    return texto.upper()



poner_mayusculas = lambda texto: texto.upper()


print(
    poner_mayusculas('hola moe')
)


numeros = [
    1,2,3,4,5,6,7
]

def filtrar_numeros(callback, lista_iteradora: list):
    lista_filtrada = []
    
    for elemento in lista_iteradora:
        if callback(elemento):
            lista_filtrada.append(elemento)
    
    print(lista_filtrada)

filtrar_numeros(lambda x: x % 2 == 0, numeros)


def es_multiplo_de_3(numero):
    return numero % 3 == 0

multiplo_de_3 = lambda x: x % 3 == 0

print(
    list(
        filter(lambda x: x % 3 == 0, numeros)
        )
    )


