def cargar_existencias(cantidad_elementos: int) -> list:
    lista_numeros = list(range(1, cantidad_elementos + 1))
    return lista_numeros
    
def sumar_cantidad_autos(lista_cantidad_autos: list) -> int:
    suma = 0
    for cantidad in lista_cantidad_autos:
        suma += cantidad
    
    return suma

def calcular_existencias_totales(lista_cantidad_autos: list):
    
    cantidad = sumar_cantidad_autos(lista_cantidad_autos)
    mensaje =\
        f"""
        La cantidad total de autos es: {cantidad} unidades.
        """
    print(mensaje)

def obtener_indice_menor_mayor(lista_algo: list, menor=True) -> int:
    indice_elegido = 0
    cantidad_seleccionada = None
    
    for indice_elemento in range(len(lista_algo)):
        if cantidad_seleccionada == None or (menor and lista_algo[indice_elemento] < cantidad_seleccionada) or\
            (not menor and lista_algo[indice_elemento] > cantidad_seleccionada):
            indice_elegido = indice_elemento
            cantidad_seleccionada = lista_algo[indice_elemento]
    return indice_elegido

def obtener_datos_menor_cantidad_autos(lista_garage: list, lista_marcas: list, lista_modelos: list, lista_cantidad: list, lista_precios: list, lista_ganancias: list):
    
    menor_cantidad = obtener_indice_menor_mayor(lista_cantidad)
    mensaje =\
        f"""
        Garage: {lista_garage[menor_cantidad]}
        Marca: {lista_marcas[menor_cantidad]}
        Modelo: {lista_modelos[menor_cantidad]}
        Precio: ${lista_precios[menor_cantidad]}
        Cantidad: {lista_cantidad[menor_cantidad]}
        Ganancia: {lista_ganancias[menor_cantidad]}
        """
    print(mensaje)


def obtener_indices_mayores_cantidad(lista_cantidad_autos: list):
    lista_aux_cantidad_elegida = []
    
    indice_valor_mayor = obtener_indice_menor_mayor(lista_cantidad_autos, menor=False)
    cantidad_elegida = lista_cantidad_autos[indice_valor_mayor]
    
    for indice_cantidad in range(len(lista_cantidad_autos)):
        if cantidad_elegida == lista_cantidad_autos[indice_cantidad]:
            lista_aux_cantidad_elegida.append(indice_cantidad)
    
    return lista_aux_cantidad_elegida


def mostrar_info_garages_maximos(lista_garage: list, lista_marcas: list, lista_modelos: list, lista_cantidad: list, lista_precios: list, lista_ganancias: list):
    lista_indices_garages = obtener_indices_mayores_cantidad(lista_cantidad)
    
    for indice in lista_indices_garages:
        mensaje =\
            f"""
            Garage: {lista_garage[indice]}
            Marca: {lista_marcas[indice]}
            Modelo: {lista_modelos[indice]}
            Precio: ${lista_precios[indice]}
            Cantidad: {lista_cantidad[indice]}
            Ganancia: {lista_ganancias[indice]}
            """
        print(mensaje)