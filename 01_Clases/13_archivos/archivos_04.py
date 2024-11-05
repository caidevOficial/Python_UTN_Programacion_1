from persona import Persona
import json

ruta_del_archivo = '13_archivos/personas.json'

elemento = None
with open(ruta_del_archivo, 'r') as archivo_json:
    elemento = json.load(archivo_json)
    
    


lista_personas = []


for persona_json in list(elemento.values())[0]:
    
    print('Cargando JSON -> Objeto Persona')
    persona_obj = Persona(persona_json.get('apellido'), persona_json.get('nombre'))
    lista_personas.append(persona_obj)
    

print('Mostrando Objetos Persona')
for persona_objeto in lista_personas:
    print(persona_objeto.en_formato_csv())