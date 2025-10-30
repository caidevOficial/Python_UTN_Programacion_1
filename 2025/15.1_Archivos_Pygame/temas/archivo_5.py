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


lista_textos = []

for persona in nombres:
    
    texto = f'{persona.get("nombre")},{persona.get("apellido")}'
    lista_textos.append(texto)


contenido = '\n'.join(lista_textos)
contenido = 'Nombre,Apellido\n' + contenido


with open('./personas.csv', 'w', encoding='utf-8') as file:
    file.write(contenido)
    # file.writelines(nombres)
    