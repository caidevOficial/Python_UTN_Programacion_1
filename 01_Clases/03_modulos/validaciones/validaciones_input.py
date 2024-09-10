from .validar_entrada_numerica import validar_entrada_string_que_representa_numero

def validar_input_entero(numero: str) -> int:
    while not validar_entrada_string_que_representa_numero(numero):
        numero = input('Numero incorrecto, ingreselo nuevamente')
    numero_int = int(numero)
    return numero_int


