"""
Enunciado:
pedir un número. mostrar los números divisores desde el 1 al número ingresado, 
y mostrar la cantidad de números divisores encontrados.
"""

numero_usuario = None
while numero_usuario == None or (not numero_usuario.isdigit()):
    numero_usuario = input(f'Ingrese un numero: ')

numero_usuario_int = int(numero_usuario)

cantidad_divisores = 0

for posible_divisor in range(1, numero_usuario_int + 1, 1):
    
    if numero_usuario_int % posible_divisor == 0:
        cantidad_divisores +=1
        print(f'El {posible_divisor} es divisor de {numero_usuario_int}')
