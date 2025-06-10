
import auxiliares
import jugador
import juego
import configs


def jugar_juego(diccionario_juego: dict, matriz_palabras: list[list], matriz_ranking: list[list]) -> None:
    """
    Funcion principal del juego. Aqui dentro se haran las siguientes cosas:
        - inicializará la palabra secreta en el diccionario_juego.
        - Se asignará un nombre al jugador
        
    Mientras aun se pueda jugar, se tiene que mostrar la palabra ocultando los caracteres que aun no fueron adivinados
    y mostrar los que si. Se pide un input al usuario para verificar si es caracter pertenece a la palabra oculta.
        En caso de pertenecer, se muestra un mensaje de exito al usuario y el caracter dejara de estar oculto, luego se sumara puntaje al jugador.
        En caso de no pertenecer, se motrara un mensaje de error y se descontara 1 vida al jugador
    
    Cuando no haya mas letras por descubrir, se actualizara el puntaje del jugador, partidas jugadas y partidas ganadas.
    Se motrara un mensaje de juego terminado y todos los puntajes del jugador se guardaran en el ranking.
    
    En caso de no tener mas vidas, se motrara un mensaje con la palabra en cuestion.
    
    :param diccionario_juego: Diccionario con parametros iniciales del juego
    :param matriz_palabras: Matriz con las posibles palabras a elegir en el juego
    :param matriz_ranking: Matriz con el ranking de puntajes de los jugadores
    """
    juego.inicializar_palabra_secreta(matriz_palabras, diccionario_juego)
    jugador.asignar_nombre(diccionario_juego.get('jugador'))
    
    while juego.verificar_estado_juego(diccionario_juego):
        print(" ".join(diccionario_juego.get("palabra_oculta")))
        letra = input("Ingresa una letra: ").lower()

        if letra in diccionario_juego.get("palabra"):
            juego.mostrar_letra_oculta(diccionario_juego, letra)
            print("¡Correcto!")
            jugador.modificar_puntaje(diccionario_juego.get('jugador'), diccionario_juego.get('jugador').get('puntaje') + 5)
        else:
            juego.modificar_dato(diccionario_juego, 'vidas', diccionario_juego.get('vidas') - 1)
            print(f"¡Incorrecto! Te quedan {diccionario_juego.get('vidas')} vidas.")
        auxiliares.clear_console()

    if "_" not in diccionario_juego.get('palabra_oculta'):
        diccionario_juego.get('jugador')["puntaje"] += configs.PUNTUACION 
        diccionario_juego.get('jugador')['vidas'] = diccionario_juego.get('vidas')
        juego.modificar_dato(diccionario_juego.get('jugador'), 'vidas', diccionario_juego.get('vidas'))
        juego.modificar_dato(diccionario_juego.get('jugador'), 'puntaje', diccionario_juego.get('jugador').get('puntaje') + configs.PUNTUACION)
        juego.modificar_dato(diccionario_juego.get('jugador'), 'partidas_jugadas', diccionario_juego.get('jugador').get('partidas_jugadas') + 1)
        juego.modificar_dato(diccionario_juego.get('jugador'), 'partidas_ganadas', diccionario_juego.get('jugador').get('partidas_ganadas') + 1)
        print("¡Felicidades! ¡Adivinaste la palabra!")
    else:
        print(f"¡Perdiste! La palabra era {diccionario_juego['palabra']}.")

    juego.guardar_puntuacion(diccionario_juego.get('jugador'), matriz_ranking)
    juego.terminar_juego("TERMINO EL JUEGO")

def adivina_la_palabra():
    """
    Esta e sla funcion de entrada de la aplicacion que debe ser ejecutada en el `main`. 
    Aqui se inicializara el diccionario del jugador y ese diccionario se agregará al diccionario del juego.
    
    El juego mostrará un menu donde se puede jugar, ver el ranking o salir.
    
    Al elegir ver el ranking, se tendra que ver el ranking de los mejores puntajes ordenados de forma DES segun el puntaje en consola
    Al elegir Jugar, se iniciara con el juego en cuestion (funcion `jugar_juego`)
    Al elegir Salir, se terminará la ejecución
    """

    diccionario_jugador = {
        "nombre": '',
        "puntaje": 0,
        "vidas": 6,
        "partidas_jugadas": 0,
        "partidas_ganadas": 0,
    }
    diccionario_juego = {
        "jugador": diccionario_jugador
    }


    corriendo = True
    while corriendo:
        opcion = input(f'1 - Ver Ranking\n2 - Jugar\n3 - Salir\n_____________\nSeleccion: ')
        
        match opcion:
            case '1':
                juego.mostrar_ranking_matrix(configs.puntajes)
            case '2':
                jugar_juego(diccionario_juego, configs.matriz_palabras, configs.puntajes)
            case '3':
                corriendo = False
        auxiliares.clear_console()
    

if __name__ == "__main__":
    adivina_la_palabra()