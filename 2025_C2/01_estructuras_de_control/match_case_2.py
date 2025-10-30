"""
Necesito tomar por consola para MercadoUTN para calcular costos de envío:
    # la provincia
    # el partido
    # la localidad

Costo base de envío AR$ 6000

Si la provincia es BSAS El costo se incrementa un 25%
    Si el partido/ciudad es CABA el costo aumenta un 13%

Si la provincia es Córdoba el costo aumenta un 12%
    Si la localidad es Capital incrementa un 2%

Para el resto de provincias el costo es del 8%  
"""

provincia = input('Ingrese provincia: ')
partido = input('Ingrese partido: ')
localidad = input('Ingrese localidad: ')

costo_base = 6000

match provincia:
    case 'buenos aires':
        costo = costo_base * 1.25
        if partido == 'caba':
            costo = costo * 1.13

    case 'cordoba':
        costo = costo_base * 1.12
        if localidad == 'capital':
            costo = costo * 1.02

    case _:
        costo = costo_base * 1.08


mensaje = f'El envio a {provincia},{partido},{localidad} es de ${costo}'

print(mensaje)