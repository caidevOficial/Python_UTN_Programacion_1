
cantidad_de_vueltas = 2
extra = 1
total_numeros = cantidad_de_vueltas + extra # 3

# [0,1,2,3,4,5]

for numero in range(total_numeros):
    print(f'===== Dato de la {numero + 1}° Persona =====')

    nombre = None
    while nombre == None:
        nombre = input('Ingrese su nombre: ')
