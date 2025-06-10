
def sanear_cadena(cadena: str) -> list[str]:
 
    input_min = cadena.lower()
    cadena = input_min.replace(' ', '')
    validacion_espacios = []
    
    for i in range(len(cadena)):
        validacion_espacios.append(cadena[i])

    return validacion_espacios

def identificar_palindromo(input: str) -> bool: 

    validacion_espacios = sanear_cadena(cadena=input)
    print(f"validacion_espacios: {validacion_espacios}")
    for i in range(len(validacion_espacios)):

        variable = (-1 - i)

        if validacion_espacios[i] != validacion_espacios[variable]:
            print("La oración no es palindromo")
            return False

    print(f"Frase correcta: {validacion_espacios}")
    return True

def utn_title(texto: str) -> str:
    lista_palabras = texto.split(' ')
    
    for indice in range(len(lista_palabras)):
        # lista_palabras[indice] = f'{lista_palabras[indice][0].upper()}{lista_palabras[indice][1:].lower()}'
        lista_palabras[indice] = f'{lista_palabras[indice].capitalize()}'
    separador = ' '
    return separador.join(lista_palabras)

def identificar_palindromo_list(listado_frases: list[str]) -> bool: 

    listado_validado = []

    for index in range(len(listado_frases)):
        variable = False
        if not listado_frases[index].isdigit():
            respuesta = identificar_palindromo(listado_frases[index])
            variable = respuesta
        listado_validado.append([listado_frases[index].title(), variable])
    return listado_validado

def visualizar_resultado(matriz_ordenada: list[list]) -> str:

    mensaje = ''
    print("\nEl resultado es: \n")
    for index in range(len(matriz_ordenada)):
        mensaje += f"Frase: {matriz_ordenada[index][0]:18} | Con valor: {matriz_ordenada[index][1]} \n"
    return mensaje


if __name__ == '__main__':
    lista_a = ["anita lava la tina","Raul", "Menem", "neuquen", "Radar", "mAfaldA", "zoOm", "49", "010"]
    resultado = identificar_palindromo_list(listado_frases=lista_a)
    visualizador = visualizar_resultado(matriz_ordenada=resultado)
    print(visualizador)
    # print(sanear_cadena('Hola Mundo'))