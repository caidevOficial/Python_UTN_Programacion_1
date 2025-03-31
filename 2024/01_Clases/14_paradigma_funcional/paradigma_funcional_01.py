# ruta_del_archivo = '14_paradigma_funcional/personas.csv'

def sumar(numero_1, numero_2):
    return numero_1 + numero_2

def restar(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicar(numero_1, numero_2):
    return numero_1 * numero_2

# Al estar en un iterable, se puede recorrer
operaciones = (
    sumar, restar, multiplicar
)

operaciones_dic = {
    "suma": sumar,
    "multiplicacion": multiplicar
}

resultado = operaciones[2](4, 5)


mi_funcion = operaciones_dic.get('multiplicacion')
resultado = mi_funcion(5,5)
print(resultado)