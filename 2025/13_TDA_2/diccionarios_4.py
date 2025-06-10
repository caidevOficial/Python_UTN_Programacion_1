# from utn_fra.datasets import lista_bzrp_nombres


# texto = ' '.join(lista_bzrp_nombres)


# cantidad_letras = {}


# for caracter in texto:
#     caracter = caracter.lower()
    
#     # Version Disney
#     if caracter in cantidad_letras.keys():
#         cantidad_letras[caracter] = cantidad_letras.get(caracter) + 1
#     else:
#         cantidad_letras[caracter] = 1
    
#     # Version Tim Burton
#     cantidad_letras[caracter] = cantidad_letras.get(caracter, 0) + 1



# for caracter, cantidad in cantidad_letras.items():
#     print(f'Caracter: {caracter:2} | Cantidad: {cantidad:3}')
    

configs = {
    "cartas": [
        {
            "id": 12,
            "img_path": '././....  .png',
            "atk": 500,
            "def": 150
        },
        {
            "id": 16,
            "img_path": '././....  .png',
            "atk": 510,
            "def": 120
        },
        {
            "id": 21,
            "img_path": '././....  .png',
            "atk": 810,
            "def": 20
        }
    ]
}


for clave in configs.keys():
    
    if type(configs.get(clave)) == list:
        lista_de_cartas = configs.get(clave)
        
        for carta in lista_de_cartas:
            print(carta, '\n')
            
            texto = ''
            for clave, valor in carta.items():
                texto += f'{clave}-{valor},'
            texto = texto[:-1]
            print(texto)