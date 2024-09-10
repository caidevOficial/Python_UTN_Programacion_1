

def factorial(numero: int):
    if numero == 0 or numero == 1:
        return 1
    else:
        anterior = numero - 1
        return numero * factorial(anterior)
    

print(factorial(500))