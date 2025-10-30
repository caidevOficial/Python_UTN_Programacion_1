import pygame as pg
import variables as var
import auxiliar as aux
import frases as fra

cuadro_titulo = aux.crear_cuadro(var.DIMENSION_TITULO, var.COORDENADA_CAJA_TITULO, var.COLOR_NEGRO)
cuadro_frase = aux.crear_cuadro(var.DIMENSION_HISTORIA, var.COORDENADA_CAJA_HISTORIA, var.COLOR_NEGRO)

def mostrar_historia(pantalla: pg.Surface, cola_eventos: list[pg.event.Event]):
    retorno = 'historia'
    bandera_juego = True
    pg.display.set_caption('HISTORIA')
    
    boton_volver = aux.crear_boton(pantalla, 'VOLVER', var.FUENTE_32, var.DIMENSION_BOTON_BACK, (993, 580), var.COLOR_NEGRO, var.COLOR_ROJO)
    
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = 'salir'
        elif evento.type == pg.MOUSEBUTTONDOWN:
            print(f'Coordenada: {evento.pos}')
            # verificar la colision con el boton
            if boton_volver.get('rectangulo').collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'menu'
                bandera_juego = False
                aux.terminar_musica()
    
    pantalla.fill(var.COLOR_BLANCO)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    
    
    # aux.mostrar_texto()
    aux.mostrar_boton(boton_volver)
    
    aux.mostrar_texto(cuadro_titulo['superficie'], 'La PYTHONisa del Tarot', (20,20), var.FUENTE_50, var.COLOR_VERDE)
    aux.mostrar_texto(cuadro_frase['superficie'], fra.historia, (20,20), var.FUENTE_22, var.COLOR_VERDE)
    
    cuadro_frase['rectangulo'] = pantalla.blit(cuadro_frase['superficie'], cuadro_frase['rectangulo'].topleft)
    cuadro_titulo['rectangulo'] = pantalla.blit(cuadro_titulo['superficie'], cuadro_titulo['rectangulo'].topleft)
    
    pg.draw.rect(pantalla, var.COLOR_NEGRO, cuadro_frase['rectangulo'], 2)
    
    
    return retorno, bandera_juego