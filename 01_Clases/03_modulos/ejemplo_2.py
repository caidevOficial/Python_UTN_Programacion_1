# Ejemplo 2 de funciones con parámetros

primer_numero_original = 5
segundo_numero_original = 10

def sumar(numero_1, numero_2):
    print(hex(id(numero_1)))
    numero_1 += numero_2
    print(numero_1)
    print(hex(id(numero_1)))
    return numero_1


print('Antes de la suma')
print(primer_numero_original)
# Vemos la direccion de memoria antes de la modificación
print(hex(id(primer_numero_original))) 

print('-----------------------')

primer_numero_original = sumar(primer_numero_original, segundo_numero_original)

print('-----------------------')
print('despues de la suma')
print(primer_numero_original)
# Vemos la direccion de memoria despues de la modificación
print(hex(id(primer_numero_original)))