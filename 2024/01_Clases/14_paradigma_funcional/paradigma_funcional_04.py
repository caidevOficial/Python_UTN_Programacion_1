def es_impar(numero):
    return numero % 2 == 1


def retornar_es_impar():
    return es_impar


mi_funcion = retornar_es_impar()

print(mi_funcion(4))


def crear_multiplicador_con_base():
    base = 10
    def multiplicar_con_base_10(numero: int):
        return base * numero
    
    return multiplicar_con_base_10

mi_funcion = crear_multiplicador_con_base()

print(
    mi_funcion(6)
)