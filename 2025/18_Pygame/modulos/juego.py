import pygame as pg
import sys
import modulos.variables as var
import modulos.forms.form_manager as form_manager
import modulos.jugador as jugador_humano

def pythonisa():
    
    pg.init()
    
    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla = pg.display.set_mode(var.DIMENSION_PANTALLA)
    pg.display.set_icon(pg.image.load(var.RUTA_ICONO))
    corriendo =True
    reloj = pg.time.Clock()
    datos_juego = {
        "puntaje": 0,
        "cantidad_vidas": var.CANTIDAD_VIDAS,
        "nombre": 'PLAYER',
        'volumen_musica' : 100,
        'tiempo_finalizado': None,
        'jugador': jugador_humano.inicializar_jugador()
    }
    
    
    f_manager = form_manager.create_form_manager(pantalla, datos_juego)
    
    
    while corriendo:
        
        event_list = pg.event.get()
        reloj.tick(var.FPS)
        
        for event in event_list:
            if event.type == pg.QUIT:
                corriendo = False
                
        form_manager.update(f_manager, event_list)
        
        pg.display.flip()
    
    pg.quit()
    sys.exit()
    