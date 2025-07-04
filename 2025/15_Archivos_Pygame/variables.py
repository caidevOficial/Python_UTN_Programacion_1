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

# ======= BOTONES ===========

BOTON_JUGAR = 0
BOTON_AJUSTES = 1
BOTON_RANKINGS = 2
BOTON_SALIR = 3

# ======= DIMENSIONES ===========

DIMENSION_TITULO = (600, 80)
DIMENSION_PREGUNTA = (500,100)
DIMENSION_HISTORIA = (1200, 450)
DIMENSION_RESPUESTA = (250,60)
DIMENSION_BOTON = (250,60)
DIMENSION_BOTON_BACK = (200, 60)
CUADRO_TEXTO = (250,50)
DIMENSION_BOTON_VOLUMEN = (60,60)
DIMENSION_BOTON_VOLVER = (100,40)

# ======= COLORES ===========

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_AMARILLO = (239,255,0)
COLOR_VERDE_OSCURO = "#0B9827"

# ======= FUENTES ===========

FUENTE_ALAGARD = './15_Archivos_Pygame/assets/fonts/alagard.ttf'

FUENTE_20 = pg.font.SysFont("Arial",20)
FUENTE_22 = pg.font.Font(FUENTE_ALAGARD, 22)
FUENTE_25 = pg.font.Font(FUENTE_ALAGARD, 25)
FUENTE_27 = pg.font.Font(FUENTE_ALAGARD, 27)
FUENTE_30 = pg.font.Font(FUENTE_ALAGARD, 30)
FUENTE_32 = pg.font.Font(FUENTE_ALAGARD, 32)
FUENTE_50 = pg.font.Font(FUENTE_ALAGARD, 50)

# ======= RUTA ===========

RUTA_MAZO_MAIN = './15_Archivos_Pygame/assets/decks'
RUTA_FONDO = './15_Archivos_Pygame/assets/background/fondo_tablero.png'
RUTA_SONIDO_CLICK = './15_Archivos_Pygame/assets/sound/click.mp3'
RUTA_MUSICA = './15_Archivos_Pygame/assets/sound/music.ogg'


# ======= CONFIGS ===========

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25

# ======= COORDENADAS ===========

COORDENADA_CAJA_TEXTO = (390,584)
COORDENADA_CARTA_MAZO = (340,106)
COORDENADA_CARTA_VISTA = (690,106)
COORDENADA_CAJA_TITULO = (DIMENSION_PANTALLA[0]//2 - DIMENSION_TITULO[0] // 2,10)
COORDENADA_CAJA_HISTORIA = (37, 115)

# ======= OBJETOS ===========

fondo = pg.image.load(RUTA_FONDO)
CLICK_SONIDO = pg.mixer.Sound(RUTA_SONIDO_CLICK)