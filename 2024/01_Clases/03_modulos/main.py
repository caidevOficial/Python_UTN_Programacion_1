from validaciones.validaciones_input import validar_input_entero
from numeros.funciones_auxiliares_primo import mostrar_numeros_primos_hasta



if __name__ == "__main__":

    numero_str = input('Ingrese un número para mostrar numeros primos hasta su numero ingresado: ')
    numero_int = validar_input_entero(numero_str)
    mostrar_numeros_primos_hasta(numero_int)
