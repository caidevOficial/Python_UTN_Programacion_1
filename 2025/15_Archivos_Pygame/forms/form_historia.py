
import pygame as pg
import variables as var
import auxiliar as aux
import frases as fra
import carta as car 

cuadro_frase = aux.crear_cuadro(var.DIMENSION_HISTORIA, var.COORDENADA_CAJA_HISTORIA, var.COLOR_NEGRO)
cuadro_titulo = aux.crear_cuadro(var.DIMENSION_TITULO, var.COORDENADA_CAJA_TITULO, var.COLOR_NEGRO)

def mostrar_historia(pantalla:pg.Surface,cola_eventos:list[pg.event.Event]):
    bandera_juego = True
    retorno = "historia"
    boton_volver = aux.crear_boton(pantalla, 'Volver', var.FUENTE_32, var.DIMENSION_BOTON_BACK, (993, 579), var.COLOR_NEGRO, var.COLOR_ROJO)
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = "salir"
        elif evento.type == pg.MOUSEBUTTONDOWN:
            print(f'Coordenada: {evento.pos}')
            if boton_volver.get('rectangulo').collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'menu'
                bandera_juego = False
                pg.mixer.music.fadeout(1)
    
    pantalla.fill(var.COLOR_VIOLETA)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    aux.mostrar_texto(cuadro_titulo["superficie"], f"La PYTHONisa del Tarot",(20,20),var.FUENTE_50,var.COLOR_VERDE)
    aux.mostrar_boton(boton_volver)
    
    aux.mostrar_texto(cuadro_frase["superficie"], fra.historia, (20,20), var.FUENTE_22,var.COLOR_VERDE)
    cuadro_frase["rectangulo"] = pantalla.blit(cuadro_frase["superficie"], cuadro_frase["rectangulo"].topleft)
    pg.draw.rect(pantalla,var.COLOR_NEGRO, cuadro_frase["rectangulo"],2)
    
    cuadro_titulo["rectangulo"] = pantalla.blit(cuadro_titulo["superficie"], cuadro_titulo["rectangulo"].topleft)
    
    return retorno, bandera_juego