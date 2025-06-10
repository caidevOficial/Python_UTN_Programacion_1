import pygame as pg
import variables as var
import auxiliares as aux
import random as rd

pg.init()

indice_actual = 0

screen = pg.display.set_mode(var.DIMENSION_PANTALLA)
pg.display.set_caption(var.TITULO_JUEGO)
clock = pg.time.Clock()

colores = [
    var.COLOR_AMARILLO, var.COLOR_AZUL, var.COLOR_BLANCO,
    var.COLOR_CIAN, var.COLOR_NARANJA, var.COLOR_VERDE,
    var.COLOR_VERDE_CLARO, var.COLOR_VIOLETA, var.COLOR_NEGRO,
    var.COLOR_ROJO
]

color_fondo = var.COLOR_NARANJA
color_texto = var.COLOR_AZUL
corriendo = True
while corriendo:
    
    eventos_pygame = pg.event.get()
    
    for evento in eventos_pygame:
        if evento.type == pg.QUIT:
            corriendo = False
        if evento.type == pg.MOUSEBUTTONDOWN:
            if evento.button == 1 and indice_actual < (len(var.frase_del_dia) - 1):
                indice_actual = rd.randint(0, len(var.frase_del_dia) - 1)
                colores_elegidos = aux.elegir_color_random(colores)
                color_fondo = colores_elegidos[0]
                color_texto = colores_elegidos[1]
            else:
                indice_actual = 0
            
    screen.fill(color_fondo)
    
    # texto = pg.font.SysFont('Arial', 40) # Para usar fuentes del sistema
    texto = pg.font.Font(var.FUENTE_ALAGARD, 40) # Para cargar una fuente externa al sistema sin instalarla
    texto = texto.render(f'{var.frase_del_dia[indice_actual]}', True, color_texto)
    rectangulo_texto = texto.get_rect()
    rectangulo_texto.center = var.CENTRO_PANTALLA
    
    screen.blit(texto, rectangulo_texto)
    
    
    pg.display.flip() # Con este metodo, actualizamos la vista en la pantalla
    
    clock.tick(var.FPS)
    
pg.quit()