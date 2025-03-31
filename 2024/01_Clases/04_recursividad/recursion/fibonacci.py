
def fibonacci(numero: int) -> int:
    if numero <= 1:
        return numero
    else:
        ultimo = numero - 1
        penultimo = numero - 2
        return fibonacci(ultimo) + fibonacci(penultimo)

print(fibonacci(17))