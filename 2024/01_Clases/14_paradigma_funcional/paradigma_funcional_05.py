def poner_en_mayusculas(texto: str):
    return texto.upper()

def poner_en_minusculas(texto: str):
    return texto.lower()

def poner_en_capitalize(texto: str):
    return texto.capitalize()




def obtener_formateo():
    texto = input('Texto: ')
    modo = input('Modo de formateo [mayusculas, minusculas, capitalize]: ')

    modo_formateo = None

    match modo:
        case 'mayusculas':
            modo_formateo = poner_en_mayusculas
        case 'minusculas':
            modo_formateo = poner_en_minusculas
        case 'capitalize':
            modo_formateo = poner_en_capitalize
    
    print(
        modo_formateo(texto)
    )


obtener_formateo()