import validaciones

def crear_jugador():
    """
    Crea el diccionario inicial del jugador, con los siguientes requisitos:
        Inicializa el puntaje en 0
        Inicializa el nombre con un string vacío (para cambiarlo luego)
        Inicializa las vidas en 6
        Inicializa las partidas jugadas en 0
        Inicializa las partidas ganadas en 0
        
    :returns: El diccionario del jugador
    """
    diccionario_jugador = {
        "nombre": '',
        "puntaje": 0,
        "vidas": 6,
        "partidas_jugadas": 0,
        "partidas_ganadas": 0,
    }
    return diccionario_jugador

def asignar_nombre(dict_jugador: dict):
    """
    Asigna el nombre validado del usuario en la clave 'nombre' del diccionario dict_jugador
    
    :param dict_jugador: Diccionario que representa a un jugador.
    
    Nota:
        Debe usar la funcion `validar_nombre_usuario` para realizar la accion de validar y agregar el nombre validado a la clave `nombre`
    """
    dict_jugador['nombre'] = validaciones.validar_nombre_usuario("Ingresa tu nombre: ", "Nombre inválido.", 3, 20)

def modificar_puntaje(diccionario_jugador: dict, nuevo_puntaje: int) -> bool:
    """
    La función `modificar_puntaje` actualiza la puntuación de un jugador en un 
    diccionario si la clave puntaje existe en el diccionario.
    
    :param diccionario_jugador: Diccionario que representa a un jugador.
    :param nuevo_puntaje: El puntaje nuevo que se guardara en la clave `puntaje`
    :return: Retorna True si modifico el puntaje, False caso contrario
    """
    if "puntaje" in diccionario_jugador:
        diccionario_jugador["puntaje"] = nuevo_puntaje
        return True
    return False