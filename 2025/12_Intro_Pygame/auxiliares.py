import random as rd

def elegir_color_random(lista_colores: list[list]) -> list[list]:
    """
    Elige dos colores distintos de la lista de colores, uno para el fondo y otro para el texto.
    
    :param lista_colores: La matriz de colores de la cual tiene que elegir dos diferentes
    :returns: Retorna una matriz con dos colores distintos para usar en el fondo y el texto
    """
    color_fondo = rd.choice(lista_colores)
    color_texto = rd.choice(lista_colores)
    while color_fondo == color_texto:
        color_texto = rd.choice(lista_colores)
    return [color_fondo, color_texto]