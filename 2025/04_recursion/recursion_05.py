

def potencia_recursiva(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    elif exponente % 2 == 0:
        temporal = potencia_recursiva(base, exponente // 2)
        return temporal * temporal
    else:
        return base * potencia_recursiva(base, exponente - 1)


resultado = potencia_recursiva(2, 8)

print(
    resultado
)