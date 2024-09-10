
"""

La funcion de Ackermann se define de la siguiente manera
donde n, m y su resultado son todos valores enteros

A(m, n) = n + 1 SI m == 0
A(m, n) = A(m - 1, 1) SI m != 0 y n == 0
A(m, n) = A(m - 1, A(m, n - 1)) SI m != 0 y n != 0
"""

def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0 and m != 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


print(ackermann(4,1))