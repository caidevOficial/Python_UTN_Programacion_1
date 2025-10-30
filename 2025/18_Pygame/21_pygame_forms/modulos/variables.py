import pygame as pg

# ======= PANTALLA ===========

RATIO_SD = (854, 480)
RATIO_SDP = (800, 600)
RATIO_HD = (1280, 720)
RATIO_FHD = (1920, 1080)
RATIO_UHD = (3840, 2160)

DIMENSION_PANTALLA = RATIO_HD

TITULO_JUEGO = 'Tarot Game'

FPS = 60



FUENTE_ALAGARD = './assets/fonts/alagard.ttf'
RUTA_MUSICA = './assets/sound/music.ogg'
RUTA_MUSICA_MENU = './assets/sound/level_1.mp3'
RUTA_MUSICA_RANKING = './assets/sound/level_2.mp3'
RUTA_MUSICA_JUEGO = './assets/sound/level_3.mp3'
CANTIDAD_VIDAS = 3

RUTA_ICONO = './assets/icon_4_star.png'

# ======= COLORES ===========
COLOR_NARANJA = (255, 87, 20)
COLOR_NEGRO = (0,0,0)
COLOR_AMARILLO = (255,255,0)
COLOR_CIAN = (5,239,250)
COLOR_VERDE = (0,255,0)
COLOR_BLANCO = (255,255,255)

# ======= ARCHIVOS ===========
RUTA_RANKING_CSV = './ranking.csv'

RUTA_CONFIGS_JSON = './configs.json'

timer = 60

nombres = [
    "Pepe", "Moni", "Fatiga", "Dardo", "Guarani"
]

RUTA_SONIDO_CLICK = './assets/sound/click.mp3'

# pg.mixer.init()
SOUND = pg.mixer.Sound(RUTA_SONIDO_CLICK)
