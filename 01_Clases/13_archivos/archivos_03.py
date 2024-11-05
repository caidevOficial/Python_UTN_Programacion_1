from persona import Persona
import json

ruta_del_archivo = '13_archivos/personas.json'

# Crear archivo formato CSV
contador = 0
lista_personas = []
lista_personas_dict = []

while contador < 2:
    nombre = input('Escriba su nombre: ')
    apellido = input('Escriba su apellido: ')

    persona_actual = Persona(apellido.title(), nombre.title())
    
    lista_personas.append(persona_actual)
    contador += 1

for persona in lista_personas:
    lista_personas_dict.append(persona.en_diccionario())
    
print(lista_personas_dict)

datos = {
    "personas": lista_personas_dict
}

with open(ruta_del_archivo, 'w') as archivo_json:
    json.dump(datos, archivo_json, indent=4)