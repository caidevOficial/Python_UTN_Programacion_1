
# for num_a in range(10):

#     uso_break = False
#     for num_b in range(40):

#         if num_b % 2 != 0:
#             uso_break = True
#             break
#         print(f'Numero del segundo FOR: {num_b}')
    
#     if uso_break:
#         break

"""
A - Ingresar un número. 
B - Mostrar todos los divisores que hay desde el 1 
    hasta el número ingresado (inclusive). 
C - Mostrar la cantidad de divisores encontrados.
"""
# for posible_divisor in range(numero_ingresado + 1):
#     if posible_divisor == 0:
#         continue

numero_ingresado_str = input('Ingrese un numero: ')
numero_ingresado = int(numero_ingresado_str)
cantidad_divisores = 0


for posible_divisor in range(1, numero_ingresado + 1, 1):
    if numero_ingresado % posible_divisor == 0:
        cantidad_divisores += 1

mensaje =\
    f"""
    El número {numero_ingresado} tiene {cantidad_divisores} divisores
    """
print(mensaje)






