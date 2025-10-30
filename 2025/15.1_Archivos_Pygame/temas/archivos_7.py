import json


nombres = [
    {
        "nombre": 'Pepe',
        "apellido": 'Argento'
    },
    {
        "nombre": 'Moni',
        "apellido": 'Argento'
    },
    {
        "nombre": 'Fatiga',
        "apellido": 'Perrito'
    }
]

diccionario = {
    "nombres": [
        {
            "nombre": 'Pepe',
            "apellido": 'Argento'
        },
        {
            "nombre": 'Moni',
            "apellido": 'Argento'
        },
        {
            "nombre": 'Fatiga',
            "apellido": 'Perrito'
        }
    ]
}

with open('./personas.json', 'w', encoding='utf-8') as file:
    json.dump(diccionario, file, indent=4)


with open('./personas.json', 'r', encoding='utf-8') as file:
    datos = json.load(file)

nombres_2 = [
    {
        "nombre": 'Dardo',
        "apellido": 'Fuseneco'
    },
    {
        "nombre": 'Maria Elena',
        "apellido": 'Fuseneco'
    },
    {
        "nombre": 'La Nena',
        "apellido": 'Fuseneco'
    }
]
datos['nombres'].extend(nombres_2)
datos['gastos'] = [1,26,540,15400]
datos['anecdotas'] = 'Este mes se gasto mucho!'


with open('./personas.json', 'w', encoding='utf-8') as file:
    json.dump(datos, file, indent=4)