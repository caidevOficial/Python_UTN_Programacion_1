
def calcular_factorial_de(numero: int) -> int:
    if numero == 0 or numero == 1:
        return 1
    else:
        anterior = numero - 1
        resultado = numero * calcular_factorial_de(anterior)
        return resultado


def calcular_factorial_recursivo(numero: int) -> int:
    limite = 20
    
    if numero > limite:
        numero_a = limite
        numero_b = limite - numero
        
        fact_a = calcular_factorial_de(numero_a)
        fact_b = calcular_factorial_de(numero_b)
        
        print(f'Factorial A: {fact_a}')
        print(f'Factorial B: {fact_b}')
        


numero = 30
calcular_factorial_recursivo(numero)
# print(
#     f'El resultado de {numero}! = {resultado_factorial}'
# )