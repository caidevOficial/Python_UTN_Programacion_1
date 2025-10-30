def sumar(op_a, op_b):
    """
    Suma los dos operandos y retorna el resultado.
    
    Args:
        op_a: Es el operando A
        op_b: Es el operando B
    
    Returns:
            Retorna la suma de ambos operandos
    """
    return op_a + op_b

def restar(op_a, op_b):
    """
    resta los dos operandos y retorna el resultado.
    
    Args:
        op_a: Es el operando A
        op_b: Es el operando B
    
    Returns:
            Retorna la resta de ambos operandos
    """
    return op_a - op_b

def aplicar_operacion(num_a, num_b, funcion):
    resultado = funcion(num_a, num_b)
    return resultado

def sumar_10(num_a, funcion):
    resultado = funcion(num_a, 10)
    return resultado

# print(sumar_10(100, sumar))



def ordenar_lista_personas(lista_personas, funcion):
    lista_personas.sort(key=funcion, reverse=True)
    return lista_personas

def get_edad(persona: dict):
    return persona.get('edad')


personas = [
    {
        "edad": 50
    },
    {
        "edad": 10
    },
    {
        "edad": 16
    },
    {
        "edad": 18
    },
    {
        "edad": 21
    }
]


# lista = ordenar_lista_personas(personas, get_edad)

# print(lista)

def filtrar_lista_personas_mayores(lista_personas, funcion):
    personas_filtradas = []
    for persona in lista_personas:
        if funcion(persona):
            personas_filtradas.append(persona)
    
    return personas_filtradas


def es_mayor(persona: dict):
    return persona.get('edad') >17


# personas_filtradas = filtrar_lista_personas_mayores(personas, es_mayor)
# print(personas_filtradas)


def crear_multiplicador_con_base(base: int):

    def multiplicar_con_base(numero: int):
        return numero * base
    return multiplicar_con_base


multiplicar_por_10 = crear_multiplicador_con_base(10)
multiplicar_por_4 = crear_multiplicador_con_base(4)

print(multiplicar_por_10(5))
print(multiplicar_por_4(5))
