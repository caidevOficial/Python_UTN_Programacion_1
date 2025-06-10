# Capitalize - Title



def utn_title(texto: str) -> str:
    separador = ' '
    lista_palabras = texto.split(separador)
    
    for indice in range(len(lista_palabras)):
        # lista_palabras[indice] = f'{lista_palabras[indice][0].upper()}{lista_palabras[indice][1:].lower()}'
        lista_palabras[indice] = f'{lista_palabras[indice].capitalize()}'
    return separador.join(lista_palabras)


texto = 'anITa lAva lA tINa'
# texto = texto.replace(' ', '').upper()

# texto = texto.capitalize()
# texto = texto.title()
texto = utn_title(texto)

# texto = f'{texto[0].upper()}{texto[1:].lower()}'
print(texto)