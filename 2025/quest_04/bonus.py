
paths = [
    "C://dir1/dir2/ID_10_HP_600_ATK_500_DEF_100.png",
    "C://dir1/dir2/ID_11_HP_600_ATK_500_DEF_100.png",
    "C://dir1/dir2/ID_12_HP_600_ATK_500_DEF_100.jpg",
    "C://dir1/dir2/ID_13_HP_600_ATK_500_DEF_100.jpg",
    "C://dir1/dir2/ID_14_HP_600_ATK_500_DEF_100.jpg",
    "C://dir1/dir2/ID_15_HP_600_ATK_500_DEF_100.jpeg",
    "C://dir1/dir2/ID_16_HP_600_ATK_500_DEF_100.jpeg",
    "C://dir1/dir2/ID_17_HP_600_ATK_500_DEF_100.jpeg",
    "C://dir1/dir2/ID_18_HP_600_ATK_500_DEF_100.bmp",
]


lista_diccionarios = []

for ruta in paths:
    nombre_archivo = ruta.split('/')[-1]
    nombre = nombre_archivo.split('.')[0]
    extension = nombre_archivo.split('.')[1]
    
    dir_2 = ruta.split('/')[-2]
    stats = nombre.split('_')
    
    diccionario = {
        "path": ruta,
        "nombre_imagen": nombre,
        "extension": f'.{extension}',
        "id": f'{dir_2}-{stats[1]}',
        "hp": stats[3],
        "atk": stats[5],
        "def": stats[7]
    }
    lista_diccionarios.append(diccionario)


for dicc in lista_diccionarios:
    print(dicc)