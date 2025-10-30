"""
En matemáticas, un número primo es un número natural mayor que 1 
que tiene únicamente dos divisores positivos distintos: 
    él mismo y el 1. 
Por el contrario, los números compuestos son los números 
naturales que tienen algún divisor natural aparte de 
sí mismos y del 1, y, por lo tanto, pueden factorizarse

[ENUNCIADO]
A - Ingresar un número. 
B - Mostrar cada número primo que hay entre el 1 y el número ingresado. 
C - Informar cuántos números primos se encontraron.

"""

numero_ingresado_str = input('Ingrese un numero: ') # 17
numero_ingresado = int(numero_ingresado_str)
cantidad_primos = 0

for posible_primo in range(1, numero_ingresado + 1, 1):

    if posible_primo < 3:
        continue

    cantidad_divisores = 2
    es_primo = True

    for posible_divisor in range(2, posible_primo):
        if posible_primo % posible_divisor == 0:
            cantidad_divisores += 1

            if cantidad_divisores > 2:
                es_primo = False
                break
            
    if es_primo:
        cantidad_primos += 1
        mensaje =\
        f"""El número {posible_primo}, ¿Es primo?: {es_primo}"""
        print(mensaje)

mensaje_2 =\
f"""Se encontraron {cantidad_primos} número primos"""
print(mensaje_2)