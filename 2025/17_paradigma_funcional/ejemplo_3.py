


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

def ordenar_personas(lista_personas, descendente, on_call):
    lista_personas.sort(key=on_call, reverse=descendente)
    
    return lista_personas

# mi_funcion_anonima = lambda persona: persona.get('edad')

# print(
#     ordenar_personas(
#         lista_personas=personas,
#         descendente=False,
#         on_call=lambda persona: persona.get('edad')
#     )
# )

mi_filtro = lambda persona: persona.get('apellido') == 'Argento' and  (5 <= persona.get('edad') <= 18)

filtradas = list(filter(
    mi_filtro,
    personas
))

print(filtradas)