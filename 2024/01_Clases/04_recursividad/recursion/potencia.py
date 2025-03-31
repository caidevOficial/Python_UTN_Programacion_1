import math

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        temporal = potencia(base, exponente // 2)
        return temporal * temporal
    else:
        return base * potencia(base, exponente - 1)
    
# print(potencia(2, 10))


for i in range(11):
    print(potencia(2, i))
    print(math.pow(2, i))
