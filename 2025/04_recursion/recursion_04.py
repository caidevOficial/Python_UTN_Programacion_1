
def maximo_comun_divisor(numero_a: int, numero_b: int) -> int:
    if numero_b == 0:
        return numero_a
    else:
        modulo_a_b = numero_a % numero_b
        return maximo_comun_divisor(numero_b, modulo_a_b)
    

maximo_comun_div = maximo_comun_divisor(3, 6)
print(
    maximo_comun_div
)