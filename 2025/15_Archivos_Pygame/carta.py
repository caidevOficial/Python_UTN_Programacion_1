import pygame as pg
import auxiliar as aux

def inicializar_carta(carta_data: dict, coordenadas: tuple[int, int]) -> dict:
    """Inicializa los datos de una carta en el diccionario.

    Args:
        carta_data (dict): Diccionario para almacenar los datos de la carta.
        coordenadas (tuple[int, int]): Las coordenadas iniciales de la carta.
    """
    carta_dict = {}
    carta_dict['id'] = carta_data.get('id')
    carta_dict['nombre'] = carta_data.get('nombre')
    carta_dict['frase'] = carta_data.get('frase')
    carta_dict['visible'] = False
    carta_dict['path_imagen_frente'] = carta_data.get('path_imagen_frente')
    carta_dict['path_imagen_reverso'] = carta_data.get('path_imagen_reverso')
    carta_dict['imagen'] = aux.achicar_imagen_card(carta_data['path_imagen_frente'], 40)
    carta_dict['imagen_reverso'] = aux.achicar_imagen_card(carta_data['path_imagen_reverso'], 40)
    carta_dict['rect'] = carta_dict['imagen'].get_rect(topleft=coordenadas)
    carta_dict['rect'].x = coordenadas[0]
    carta_dict['rect'].y = coordenadas[1]
    carta_dict['rect_reverso'] = carta_dict['imagen_reverso'].get_rect(topleft=coordenadas)
    carta_dict['rect_reverso'].x = coordenadas[0]
    carta_dict['rect_reverso'].y = coordenadas[1]
    return carta_dict

def get_id_carta(carta_data: dict) -> int:
    """Devuelve el ID de la carta.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.

    Returns:
        int: El ID de la carta.
    """
    return carta_data.get('id')

def get_frase_carta(carta_data: dict) -> str:
    """Devuelve la frase de la carta.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.

    Returns:
        str: La frase de la carta.
    """
    return carta_data.get('frase')

def get_rect_carta(carta_data: dict) -> pg.Rect:
    """Devuelve el rectángulo de la imagen de la carta.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.

    Returns:
        pg.Rect: El rectángulo de la imagen.
    """
    return carta_data.get('rect')

def esta_visible_carta(carta_data: dict) -> bool:
    """Devuelve True si la carta es visible.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.

    Returns:
        bool: True si la carta es visible, False en caso contrario.
    """
    return carta_data.get('visible')

def cambiar_visibilidad_carta(carta_data: dict):
    """Cambia la visibilidad de la carta.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.
    """
    carta_data['visible'] = True

def asignar_coordenadas_carta(carta_data: dict, coordenadas: tuple[int, int]):
    """Asigna nuevas coordenadas a la carta y la hace visible.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.
        coordenadas (tuple[int, int]): Las nuevas coordenadas (x, y).
    """
    carta_data['rect'].topleft = coordenadas
    carta_data['rect_reverso'].topleft = coordenadas
    carta_data['visible'] = True

def draw_carta(carta_data: dict, screen: pg.Surface):
    """Dibuja la carta en la pantalla.

    Args:
        carta_data (dict): Diccionario con los datos de la carta.
        screen (pg.Surface): La superficie de la pantalla donde dibujar.
    """
    if carta_data['visible']:
        screen.blit(carta_data.get('imagen'), carta_data.get('rect'))
    else:
        screen.blit(carta_data.get('imagen_reverso'), carta_data.get('rect_reverso'))