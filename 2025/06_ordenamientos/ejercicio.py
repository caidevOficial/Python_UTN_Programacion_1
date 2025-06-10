from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios
)


for indice in range(len(lista_autos_ganancias)):
    
    mensaje =\
        f"""
        Garaje N° {indice + 1}
        Marca: {lista_autos_marcas[indice]}
        Modelo: {lista_autos_modelos[indice]}
        Precio Unit: ${lista_autos_precios[indice]}
        Cantidad: {lista_autos_cantidades[indice]}
        Ganancias: {lista_autos_ganancias[indice]}
        """
        
    print(mensaje)