import json
from UTN_Heroes_Dataset.utn_listas_complejas import lista_diccionario_heroes

# pip install UTN-Heroes-Dataset=='1.1.53'

# print(lista_diccionario_heroes[0:3])
ruta_del_archivo = '13_archivos/heroes.json'
with open(ruta_del_archivo, 'w') as file:
    json.dump(
        {"Heroes": lista_diccionario_heroes}, 
        file, 
        indent=4)