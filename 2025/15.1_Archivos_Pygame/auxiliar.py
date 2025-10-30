import pygame as pg
import os
import random as rd
import carta
import variables as var
from datetime import datetime

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = 'purple'):
    lista_botones = []
    for i in range(cantidad):
        boton = {}
        boton['superficie'] = pg.Surface(dimension)
        boton['rectangulo'] = boton.get('superficie').get_rect()
        boton['superficie'].fill(pg.Color(color))
        lista_botones.append(boton)
    return lista_botones

def mostrar_texto(surface: pg.Surface, texto: str, pos: tuple, font, color = pg.Color('black')):
    words = []
    
    for word in texto.splitlines():
        words.append(word.split(' '))
    
    space = font.size(' ')[0]
    ancho_max, alto_max = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            ancho_palabra, alto_palabra = word_surface.get_size()
            if x + ancho_palabra >= ancho_max:
                x = pos[0]
                y += alto_palabra
            surface.blit(word_surface, (x, y))
            x += ancho_palabra + space
        x = pos[0]
        y += alto_palabra

def crear_cuadro(dimensiones: tuple, coordenadas: tuple, color: tuple) -> dict:
    cuadro = {}
    cuadro['superficie'] = pg.Surface(dimensiones)
    cuadro['rectangulo'] = cuadro.get('superficie').get_rect()
    cuadro['rectangulo'].topleft = coordenadas
    cuadro['superficie'].fill(pg.Color(color))
    return cuadro

def crear_boton(pantalla: pg.Surface, texto: str, ruta_fuente: str, dimensiones: tuple, coordenadas: tuple,color_fondo: tuple, color_texto: tuple):
    cuadro = crear_cuadro(dimensiones, coordenadas, color_fondo)
    cuadro['texto'] = texto
    cuadro['pantalla'] = pantalla
    cuadro['color_texto'] = color_texto
    cuadro['color_boton'] = color_fondo
    cuadro['font_path'] = ruta_fuente
    cuadro['padding'] = (10,10)
    return cuadro

def mostrar_boton(boton_dict: dict):
    mostrar_texto(
        boton_dict.get('superficie'),
        boton_dict.get('texto'),
        boton_dict.get('padding'),
        boton_dict.get('font_path'),
        boton_dict.get('color_texto')
    )
    boton_dict['rectangulo'] = boton_dict.get('pantalla').blit(
        boton_dict.get('superficie'), boton_dict.get('rectangulo').topleft
    )
    pg.draw.rect(boton_dict.get('pantalla'), boton_dict.get('color_boton'), boton_dict.get('rectangulo'), 2)
    
def generar_bd(root_path_cards: str):
        
    carta_dict = {
        "cartas": {}
    }
    
    for root, dir, files in os.walk(root_path_cards, topdown=True):
        reverse_path = ''
        deck_cards = []
        deck_name = root.split('\\')[-1]
        
        for file in files:
            path_card = os.path.join(root, file)
            
            if 'reverse' in path_card:
                reverse_path = path_card
            else:
                file = file.replace('\\', '/')
                filename = file.split('/')[-1]
                datos = filename.split('.')[-2]
                
                card = {
                    'id': f'{deck_name}-{datos}',
                    "mensaje": '',
                    "frase": '',
                    'puntaje': 0,
                    "path_imagen_frente": path_card
                }
                
                deck_cards.append(card)
        
        for index_card in range(len(deck_cards)):
            deck_cards[index_card]['path_imagen_reverso'] = reverse_path
        
        carta_dict['cartas'][deck_name] = deck_cards
    return carta_dict

def asignar_frases(lista_mazo: list[dict], lista_frases: list[dict]) -> list[dict]:
    
    for index_card in range(len(lista_mazo)):
        frase = rd.choice(lista_frases)
        lista_mazo[index_card]['frase'] = frase.get('frase')
        lista_mazo[index_card]['puntaje'] = frase.get('puntaje')
    return lista_mazo

def achicar_imagen_card(path_imagen: str, porcentaje: int):
    imagen_raw = pg.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final


def generar_mazo(mazo_dict_original: list[dict]):
    lista_mazo_resultado = []
    for card in mazo_dict_original:
        carta_final = carta.inicializar_carta(card, var.COORDENADA_CARTA_MAZO)
        lista_mazo_resultado.append(carta_final)
    
    rd.shuffle(lista_mazo_resultado)
    
    return lista_mazo_resultado

def actualizar_puntaje(dict_juego: dict, puntaje: int):
    dict_juego['puntaje'] += puntaje

def verificar_tiempo_cumplido(tiempo_finalizado: int, retorno: tuple[str,str]) -> str:
    tiempo_actual = pg.time.get_ticks()
    if tiempo_actual - tiempo_finalizado >= 2000:
        return retorno[0]
    return retorno[1]

def datos_player_to_csv(dict_juego: dict):
    data = f'{datetime.now()},{dict_juego.get("nombre")},{dict_juego.get("puntaje")}\n'
    return data

def grabar_puntaje(dict_juego: dict):
    with open(var.RUTA_RANKING, '+a', encoding='utf-8') as file:
        data = datos_player_to_csv(dict_juego)
        file.write(data)

def inicializar_musica(dict_juego: dict):
    porcentaje_coma = dict_juego.get('volumen_musica') / 100
    pg.mixer.music.load(var.RUTA_MUSICA)
    pg.mixer.music.set_volume(porcentaje_coma)
    pg.mixer.music.play(-1)

def terminar_musica():
    pg.mixer.music.stop()
    