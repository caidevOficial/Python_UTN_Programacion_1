numeros = [
    1,2,3,4,5,6,7,8,9,10
]



# for numero in numeros:
#     numero = numero + 10
#     resultado = 7 * numero
#     print(f'7 X {numero} = {resultado}')

for indice in range(len(numeros)):
    numero = numeros[indice]
    numero = numero + 10
    numeros[indice] = numero
    resultado = 7 * numero
    print(f'7 X {numero} = {resultado}')

print(numeros)