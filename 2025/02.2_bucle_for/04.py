"""
Enunciado 01:
Pedir al usuario que ingrese un numero, validarlo y mostrar cada número primo 
entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
"""

# numero_usuario = None
# while numero_usuario == None or (not numero_usuario.isdigit()):
#     numero_usuario = input(f'Ingrese un numero: ')

# numero_usuario_int = int(numero_usuario)
numero_usuario_int = 16000


for posible_primo in range(2, numero_usuario_int + 1, 1):
    
    cantidad_divisores = 2

    # Encontrar cantidad divisores para saber si es primo o no.
    for posible_divisor in range(2, posible_primo, 1):
        
        if posible_primo % posible_divisor == 0:
            cantidad_divisores +=1
            # print(f'El {posible_divisor} es divisor de {numero_usuario_int}')
    
            if cantidad_divisores > 2:
                break
    
    if cantidad_divisores == 2:
        print(f'El numero {posible_primo} es PRIMO')
    else:
        print(f'Este numero falopa tiene {cantidad_divisores} divisores')
    
