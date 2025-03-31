# Ejemplo:
"""
Dada una lista de palabras, usa un diccionario para contar la frecuencia de 
cada palabra. Ayudate de un bucle para poder iterar y contar.
"""

palabras = [
    "manzana", "banana", "manzana", "pera", "banana", "manzana",
    "pera","pera","pera","pera","pera","pera"
    ]
frecuencia = {}

"""
{
    "manzana": 3,
    "banana": 2,
    "pera": 7
}
"""

# Version Función
def contabilizar_elementos_lista(lista_elementos: list) -> dict:
    frecuencia = {}
    for elemento in lista_elementos:
        elem_minuscu = elemento.lower()
        if not elem_minuscu in frecuencia.keys():
            frecuencia[elem_minuscu] = 1
        else:
            frecuencia[elem_minuscu] += 1
    
    return frecuencia

def contabilizar_elementos_ninja_lista(lista_elementos: list) -> dict:
    frecuencia = {}
    for elemento in lista_elementos:
        frecuencia[elemento.lower()] = frecuencia.get(elemento.lower(), 0) + 1
    
    return frecuencia


texto = """Dada una lista de palabras, usa un diccionario para contar la frecuencia de 
cada palabra. Ayudate de un bucle para poder iterar y contar ."""

frecuencias = contabilizar_elementos_lista(texto.split(' '))


# Una manera de ordenar un diccionario
# Parseando a lista de tuplas, ordenar tuplas y luego parsear a diccionario
def ordenar_dicc(diccionario: dict):
    lista_ordenada = []
    for clave, valor in diccionario.items():
        lista_ordenada.append(
            (clave, valor)
        )
    
    for indice_tupla in range(len(lista_ordenada) - 1):
        
        for indice_siguiente_tupla in range(indice_tupla + 1, len(lista_ordenada)):
            
            if lista_ordenada[indice_tupla][1] > lista_ordenada[indice_siguiente_tupla][1]:
                lista_ordenada[indice_tupla], lista_ordenada[indice_siguiente_tupla] =\
                lista_ordenada[indice_siguiente_tupla], lista_ordenada[indice_tupla]
    diccionario_ordenado = dict(lista_ordenada)
    print(diccionario_ordenado)
        

ordenar_dicc(frecuencias)
