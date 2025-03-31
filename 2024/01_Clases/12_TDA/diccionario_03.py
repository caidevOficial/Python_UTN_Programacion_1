

diccionario_02 = {
    "Matematica": 8,
    "Universidades": ["UTN", 'UNQui', 'UBA'],
    "Notas": {
        "Progra1": 9,
        "Matematica": 8,
        "Ingles": 4
    }
}

# Al quitar una clave, retorna su valor
elemento = diccionario_02.pop('Universidades')

print(diccionario_02)

# Shallow copy del diccionario
diccionario_03 = diccionario_02.copy()
diccionario_03.pop('Matematica')

print(diccionario_02)
print(diccionario_03)

# Modificación de valores del diccionario copia
diccionario_03['Notas']['Progra1'] = 6
diccionario_03['Notas']['AySO'] = 8

# diccionario_03['Notas']['Matematica']
diccionario_03.pop('Notas')


print(diccionario_02)
print(diccionario_03)