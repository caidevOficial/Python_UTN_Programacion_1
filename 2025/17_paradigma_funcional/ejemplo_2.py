def crear_filtro(filtro: str):
    
    def get_nombre(persona: dict):
        "Obtiene el nombre"
        return persona.get('nombre')
    
    def get_edad(persona: dict):
        "Obtiene la edad"
        return persona.get('edad')
    
    def get_apellido(persona: dict):
        "Obtiene el apellido"
        return persona.get('apellido')
    
    match filtro:
        case 'edad':
            return get_edad
        case 'nombre':
            return get_nombre
        case 'apellido':
            return get_apellido


def ordenar_personas(lista_personas, funcion):
    lista_personas.sort(key=funcion, reverse=True)
    
    return lista_personas

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


filtro = crear_filtro('nombre')

personas_filtradas = ordenar_personas(personas, filtro)
print(personas_filtradas)