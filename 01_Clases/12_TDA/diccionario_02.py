diccionario_02 = {
    "Nombre": "Pepe",
    "Universidades": ["UTN", 'UNQui', 'UBA'],
    
    "Notas": {
        "Progra1": 9,
        "Matematica": 8,
        "Ingles": 4
    }
}

# Acceder a una clave mediante get(), si no existe
# retorna un valor por defecto (None si no le pasamos un segundo argumento)
print(diccionario_02.get('Notas', "No se encontro la clave!"))

notas = diccionario_02.get('Notas')

# Modificar un diccionario anidado de nuestro diccionario principal
notas['Ingles'] = 10
print(notas)

# Actualizar nuestro diccionario principal
diccionario_02.update({"Notas": notas})

print(diccionario_02)