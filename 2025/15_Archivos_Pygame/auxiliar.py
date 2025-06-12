import os
import pygame as pg
import random
import variables as var
import carta as car

def generar_bd(root_path_cards: str):
    cards_dict = {
        'cartas': {}
    }
    
    reverse_path = ''
    for root, dir, files in os.walk(root_path_cards, topdown=True):
        reverse_path = ''
        deck_cards = []
        deck_name = root.split('\\')[-1]
        
        for file in files:
            path_card = os.path.join(root, file) 
            if 'reverse' in file:
                reverse_path = path_card.replace('\\', '/')
            else:
                file = file.replace('\\', '/')
                filename = file.split('/')[-1]
                datos = filename.split('.')[-2]
                # print(datos)

                card = {
                    'id': f'{deck_name}-{datos}',
                    'mensaje': '',
                    'frase': '',
                    'path_imagen_frente': path_card.replace('\\', '/'),
                    'path_imagen_reverso': reverse_path
                }
                deck_cards.append(card)

        for i in range(len(deck_cards)):
            deck_cards[i]['path_imagen_reverso'] = reverse_path
        
        cards_dict['cartas'][deck_name] = deck_cards
    return cards_dict

def mostrar_texto(surface: pg.Surface, text: str, pos: tuple, font, color=pg.Color('black')):
    words = []  # 2D array where each row is a list of words.
    for word in text.splitlines():
        words.append(word.split(' '))
    
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def achicar_imagen_card(ruta_imagen: str, porcentaje: int) -> pg.Surface:
    imagen_raw = pg.image.load(ruta_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final

def crear_cuadro(dimensiones: tuple, coordenadas: tuple, color: tuple) -> dict:
    cuadro = {}
    cuadro["superficie"] = pg.Surface(dimensiones)
    cuadro["rectangulo"] = cuadro["superficie"].get_rect()
    cuadro["rectangulo"].topleft = coordenadas
    cuadro["superficie"].fill(color)
    return cuadro

def crear_boton(pantalla: pg.Surface, texto:str, font_path: str,dimensiones: tuple, coordenadas: tuple, color_fondo: tuple, color_texto: tuple):
    cuadro = crear_cuadro(dimensiones, coordenadas, color_fondo)
    cuadro['texto'] = texto
    cuadro['font_path'] = font_path
    cuadro['pantalla'] = pantalla
    cuadro['color_texto'] = color_texto
    cuadro['color_boton'] = color_fondo
    cuadro['padding'] = (10, 10)
    return cuadro

def mostrar_boton(boton_dict: dict):
    mostrar_texto(
        boton_dict.get('superficie'), boton_dict.get('texto'), 
        boton_dict.get('padding'), 
        boton_dict.get('font_path'), boton_dict.get('color_texto'))
    boton_dict["rectangulo"] = boton_dict.get('pantalla').blit(boton_dict["superficie"], boton_dict["rectangulo"].topleft)
    pg.draw.rect(boton_dict.get('pantalla'),boton_dict.get('color_boton'), boton_dict.get('rectangulo'),2)

def asignar_frases(mazo: list, frases: list):
    for i in range(len(mazo)):
        mazo[i]['frase'] = random.choice(frases).get('frase')
    return mazo

def generar_mazo(mazo: list):
    lista_cartas_dict = []
    for carta in mazo:
        lista_cartas_dict.append(
            car.inicializar_carta(carta, var.COORDENADA_CARTA_MAZO)
        )
    random.shuffle(lista_cartas_dict)
    return lista_cartas_dict

def crear_lista_botones(cantidad: int, dimension: tuple, color: str = 'purple'):
    lista_botones = []
    for i in range(cantidad):
        boton = {}
        boton["superficie"] = pg.Surface(dimension)
        boton["rectangulo"] = boton["superficie"].get_rect()
        boton["superficie"].fill(pg.Color(color))
        lista_botones.append(boton)
    return lista_botones