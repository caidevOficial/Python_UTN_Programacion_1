
def calcular_fibonacci(numero: int) -> int:
    if numero == 0 or numero == 1:
        return numero
    else:
        ultimo = numero - 1
        penultimo = ultimo - 1
        fibo_ultimo = calcular_fibonacci(ultimo)
        fibo_penultimo = calcular_fibonacci(penultimo)
        suma_fibos = fibo_ultimo + fibo_penultimo
        return suma_fibos



limite = 40

for numero in range(0, limite):
    numero_fibonacci = calcular_fibonacci(numero)

    print(
        f'El {numero}° numero de la sucesion Fibonacci es: {numero_fibonacci}'
    )