# Combinado con archivos:
ruta_del_archivo = '14_paradigma_funcional/personas.csv'

with open(ruta_del_archivo, 'r', encoding='utf-8') as file:
    contenido = file.readlines()


# Saneamiento de la informacion, para borrar el \n del final de linea
for indice_contenido in range(len(contenido)):
    contenido[indice_contenido] = contenido[indice_contenido].replace('\n', '')

# Filtramos por edades pares
def filtrar_edad_par(callback, lista_personas):
    personas = []
    for persona in lista_personas:
        if callback(persona):
            personas.append(persona)
    return personas

# Asignamos la funcion anonima a una variable
tiene_edad_par = lambda x: int(x.split(',')[2]) % 2 == 0

# usamos la funcion anonima que guardamos en una variable
edad_par_personas_filtradas = filtrar_edad_par(tiene_edad_par, contenido)

# usamos la funcion anonima directamente como argumento de nuestra funcion filtradora
edad_impar_personas_filtradas = filtrar_edad_par(lambda x: int(x.split(',')[2]) % 2 == 1, contenido)
print(edad_par_personas_filtradas)
print(edad_impar_personas_filtradas)
