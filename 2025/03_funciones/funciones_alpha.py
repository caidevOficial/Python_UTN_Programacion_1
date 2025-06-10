
def calcular_precio_con_iva(precio_sin_iva, iva=21):
    """
    Le agrega el iva al precio sin iva (por defecto es el 21%) y retorna
    el precio con iva.
    """
    resultado_precio_iva = precio_sin_iva * (1 + (iva/100))
    return resultado_precio_iva


precio_sin_iva = 1000

precio_con_iva = calcular_precio_con_iva(precio_sin_iva)
precio_con_medio_iva = calcular_precio_con_iva(precio_sin_iva, iva=10.5)

print(
    f'El precio sin iva es: ${precio_sin_iva}',
    f'El precio con iva es: $ {precio_con_iva}',
    f'El precio con medio iva es: $ {precio_con_medio_iva}',
    sep='\n'
)
