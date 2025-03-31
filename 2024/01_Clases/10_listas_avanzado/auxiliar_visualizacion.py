
columnas = ['ID Original', 'ID Copia', 'Valor Original', 'Valor Copia']

def crear_matriz_visualizacion(lista_original, lista_copia):
    matriz_ids = []
    direccion_o = hex(id(lista_original))
    direccion_c = hex(id(lista_copia))
    matriz_ids.append([direccion_o, direccion_c, '', ''])

    for indice in range(len(lista_copia)):
        direccion_o = hex(id(lista_original[indice]))
        direccion_c = hex(id(lista_copia[indice]))
        valor_o = lista_original[indice]
        valor_c = lista_copia[indice]
        matriz_ids.append([direccion_o, direccion_c, valor_o, valor_c])
        
        if type(lista_original[indice]) == list:
            for indice_sub in range(len(lista_copia[indice])):
                direccion_o = hex(id(lista_original[indice][indice_sub]))
                direccion_c = hex(id(lista_copia[indice][indice_sub]))
                valor_o = lista_original[indice][indice_sub]
                valor_c = lista_copia[indice][indice_sub]
                matriz_ids.append([direccion_o, direccion_c, valor_o, valor_c])
    return matriz_ids