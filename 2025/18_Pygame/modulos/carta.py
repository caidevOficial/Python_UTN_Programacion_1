import pygame as pg 
import modulos.auxiliar as aux


def inicializar_carta(carta_dict: dict, coordenadas: tuple[int,int]) -> dict:
    carta_dict_final = {}
    carta_dict_final['id'] = carta_dict.get('id')
    carta_dict_final['nombre'] = carta_dict.get('nombre')
    carta_dict_final['frase'] = carta_dict.get('frase')
    carta_dict_final['puntaje'] = carta_dict.get('puntaje')
    carta_dict_final['path_imagen_frente'] = carta_dict.get('path_imagen_frente')
    carta_dict_final['path_imagen_reverso'] = carta_dict.get('path_imagen_reverso')
    
    carta_dict_final['visible'] = False
    carta_dict_final['imagen'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_frente'), 40)
    carta_dict_final['imagen_reverso'] = aux.achicar_imagen_card(carta_dict_final.get('path_imagen_reverso'), 40)
    
    carta_dict_final['rect'] = carta_dict_final.get('imagen').get_rect()
    carta_dict_final['rect'].x = coordenadas[0]
    carta_dict_final['rect'].y = coordenadas[1]
    
    carta_dict_final['rect_reverso'] = carta_dict_final.get('imagen_reverso').get_rect()
    carta_dict_final['rect_reverso'].x = coordenadas[0]
    carta_dict_final['rect_reverso'].y = coordenadas[1]
    
    return carta_dict_final

def get_puntaje_carta(card_dict: dict):
    return card_dict.get('puntaje')

def set_frase(card_dict: dict, nueva_frase: str):
    card_dict['frase'] = nueva_frase

def set_puntaje(card_dict: dict, puntaje: int):
    card_dict['puntaje'] = puntaje

def draw_carta(card_data: dict, screen: pg.Surface):
    
    if card_data.get('visible'):
        screen.blit(card_data.get('imagen'), card_data.get('rect'))
    else:
        screen.blit(card_data.get('imagen_reverso'), card_data.get('rect_reverso'))

def asignar_coordenadas_carta(carta_dict: dict, nueva_coordenada: tuple[int,int]):
    carta_dict['rect'].topleft = nueva_coordenada
    carta_dict['rect_reverso'].topleft = nueva_coordenada

def cambiar_visibilidad_carta(carta_dict: dict):
    carta_dict['visible'] = True
    