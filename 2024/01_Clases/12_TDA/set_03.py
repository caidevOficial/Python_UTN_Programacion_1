class Persona:
    
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.__apellido = apellido

    def get_nombre(self):
        return self.__nombre
    
    def to_string(self):
        return f'{self.__apellido}, {self.__nombre}'


lista = [
    Persona('Pepe', 'Argento'),
    Persona('Pepe', 'Argento'),
    Persona('Moni', 'Argento')
]

# Al ser una referencia de un objeto existente
# sus referencias son iguales, el set se quedará con una
lista.append(lista[2])

for persona in set(lista):
    print(persona.to_string())