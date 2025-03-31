numeros = [
    1,2,3,4,5,6,7
]


def es_impar(numero):
    return numero % 2 == 1

def es_par(numero):
    return numero % 2 == 0

def filtrar_numeros(lista_numeros: list, callback):
    lista_filtrada = []
    
    for elemento in lista_numeros:
        if callback(elemento):
            lista_filtrada.append(elemento)
    
    print(lista_filtrada)



filtrar_numeros(numeros, es_impar)
filtrar_numeros(numeros, es_par)