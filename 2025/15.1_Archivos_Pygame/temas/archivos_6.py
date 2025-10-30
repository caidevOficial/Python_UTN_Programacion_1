lista_campos = ['nombre', 'apellido', 'puntaje', 'puntaje_final', 'estatus']

def crear_diccionario(lista_str: list[str]):
    dict = {}
    
    for indice_campo in range(len(lista_campos)):
        dict[lista_campos[indice_campo]] = lista_str[indice_campo]
    
    return dict

texto = []
texto_dic = []
with open('./personas.csv', 'r', encoding='utf-8') as file:
    
    
    lista_lineas = file.readlines()
    for linea in lista_lineas:
        
        if lista_lineas.index(linea) == 0:
            continue
        
        
        contenido = linea.replace('\n', '')
        
        contenido_linea = contenido.split(',')
        print(contenido_linea)
        texto.append(contenido_linea)
        
        dict = crear_diccionario(contenido_linea)
        
        texto_dic.append(dict)
        
print(texto)
print(texto_dic)