
personas = [
    {
        "edad": 50,
        "apellido": 'Argento',
        "nombre": 'Pepe'
    },
    {
        "edad": 10,
        "apellido": 'Argento',
        "nombre": 'Fatiga'
    },
    {
        "edad": 16,
        "apellido": 'Argento',
        "nombre": 'Paola'
    },
    {
        "edad": 45,
        "apellido": 'Fuseneco',
        "nombre": 'Dardo'
    },
    {
        "edad": 48,
        "apellido": 'Argento',
        "nombre": 'Moni'
    }
]


get_edad = lambda x: x.get('edad')
get_nombre = lambda x: x.get('nombre')
get_apellido = lambda x: x.get('apellido')


def ordenar_personas(lista_personas, descendente, on_call):
    lista_personas.sort(key=on_call, reverse=descendente)
    
    return lista_personas


print(
    ordenar_personas(
    personas, False, get_nombre
)
)