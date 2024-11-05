from persona import Persona

ruta_del_archivo = '13_archivos/personas.csv'


# Crear archivo formato CSV
contador = 0
lista_personas = []

while contador < 2:
    nombre = input('Escriba su nombre: ')
    apellido = input('Escriba su apellido: ')

    persona_actual = Persona(apellido, nombre)
    
    lista_personas.append(persona_actual)
    contador += 1







#   .csv
with open(ruta_del_archivo, 'a') as archivo_csv:
    for persona in lista_personas:
        archivo_csv.write(f'{persona.en_formato_csv()}\n')
        