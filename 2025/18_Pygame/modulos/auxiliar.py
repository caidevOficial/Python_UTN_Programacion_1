import pygame as pg
import modulos.variables as var
import json
import os


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

def parsear_entero(valor: str):
    if valor.isdigit():
        return int(valor)
    return valor

def mapear_valores(matriz: list[list], indice_a_aplicar: int, callback):
    
    for indice_fila in range(len(matriz)):
        valor = matriz[indice_fila][indice_a_aplicar]
        matriz[indice_fila][indice_a_aplicar] = callback(valor)

def cargar_ranking():
    ranking = []
    with open(var.RUTA_RANKING_CSV, 'r', encoding='utf-8') as file:
        lineas = file.read()
        for linea in lineas.split('\n'):
            if linea:
                ranking.append(linea.split(','))
    mapear_valores(ranking, 1, parsear_entero)
    ranking.sort(key=lambda fila: fila[1], reverse=True)
    
    return ranking

def guardar_ranking(jugador_dict: dict):
    with open(var.RUTA_RANKING_CSV, 'a', encoding='utf-8') as file:
        data = f'{jugador_dict.get("nombre")},{jugador_dict.get("puntaje_actual")}\n'
        file.write(data)
        print('Datos guardados con exito: -> {data}')

def cargar_configs(path: str) -> dict:
    configuraciones = {}
    with open(path, 'r', encoding='utf-8') as file:
        configuraciones = json.load(file)
    return configuraciones

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

def achicar_imagen_card(path_imagen: str, porcentaje: int):
    imagen_raw = pg.image.load(path_imagen)
    alto = int(imagen_raw.get_height() * float(f'0.{porcentaje}'))
    ancho = int(imagen_raw.get_width() * float(f'0.{porcentaje}'))
    imagen_final = pg.transform.scale(imagen_raw, (ancho, alto))
    return imagen_final