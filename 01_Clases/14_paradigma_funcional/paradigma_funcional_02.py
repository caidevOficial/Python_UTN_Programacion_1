def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def restar(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

def operacion_matematica(numero_1, numero_2, funcion_matematica):
    resultado = funcion_matematica(numero_1, numero_2)
    print(resultado)


operacion_matematica(4, 5, multiplicar)


frutas = [
    "Naranja", "Mandarina", "Pera"
]


def largo_cadena(cadena):
    return len(cadena)


def ordenar_lista(lista_a_ordenar: list, callback):
    lista_a_ordenar.sort(key=callback)

ordenar_lista(frutas, largo_cadena)

print(frutas)
