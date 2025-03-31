# Crear diccionarios

diccionario_01 = dict(
    [("Nombre", "Facu"), ("Universidad", "UTN")]
)

diccionario_02 = {
    "Nombre": "Facu",
    "Universidades": ["UTN", 'UNQui', 'UBA'],
    "Notas": {
        "Progra1": 9,
        "Matematica": 8,
        "Ingles": 4
    }
}


# Modificar un valor de una clave existente
diccionario_02["Notas"]['Ingles'] = 6

# Recorrer valores segun su tipo

for elemento in diccionario_02.values():
    if type(elemento) == list:
        for sub_elemento in elemento:
            print(sub_elemento)
    elif type(elemento) == dict:
        print(elemento.keys())
        
# Imprimir claves de diccionario
print(diccionario_02.keys())
# Imprimir valores de diccionario
print(diccionario_02.values())

# Recorrer claves y valores en simultaneo mediente items()
for clave, valor in diccionario_02.items():
    print(clave, valor)