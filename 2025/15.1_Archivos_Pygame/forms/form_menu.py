import pygame as pg
import variables as var
import auxiliar as aux


lista_botones = aux.crear_lista_botones(4, var.DIMENSION_BOTON, 'purple')

def mostrar_menu(pantalla: pg.Surface, cola_eventos: list[pg.event.Event]) -> str:
    retorno = 'menu'
    pg.display.set_caption('MENU')
    
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = 'salir'
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if lista_botones[var.BOTON_JUGAR]['rectangulo'].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'juego'
            elif lista_botones[var.BOTON_AJUSTES]['rectangulo'].collidepoint(evento.pos):
                retorno = 'configuracion'
            elif lista_botones[var.BOTON_HISTORIA]['rectangulo'].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'historia'
                print('Click en boton historia')
            elif lista_botones[var.BOTON_SALIR]['rectangulo'].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'salir'
    
    pantalla.fill(var.COLOR_BLANCO)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    lista_botones[var.BOTON_HISTORIA]['rectangulo'] = pantalla.blit(lista_botones[var.BOTON_HISTORIA]['superficie'], (125, 275))
    lista_botones[var.BOTON_JUGAR]['rectangulo'] = pantalla.blit(lista_botones[var.BOTON_JUGAR]['superficie'], (125, 115))
    lista_botones[var.BOTON_SALIR]['rectangulo'] = pantalla.blit(lista_botones[var.BOTON_SALIR]['superficie'], (125, 355))
    
    aux.mostrar_texto(lista_botones[var.BOTON_HISTORIA]['superficie'], 'HISTORIA', (75, 20), var.FUENTE_30, var.COLOR_BLANCO)
    aux.mostrar_texto(lista_botones[var.BOTON_JUGAR]['superficie'], 'JUGAR', (75, 20), var.FUENTE_30, var.COLOR_BLANCO)
    aux.mostrar_texto(lista_botones[var.BOTON_SALIR]['superficie'], 'SALIR', (75, 20), var.FUENTE_30, var.COLOR_BLANCO)
    
    return retorno
    
    
    