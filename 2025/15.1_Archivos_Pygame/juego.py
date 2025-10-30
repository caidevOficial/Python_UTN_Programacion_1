import pygame as pg 
import variables as var
import forms.form_menu as form_menu
import forms.form_historia as form_historia
import forms.form_juego as form_juego
import auxiliar as aux

def pythonisa():
    
    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla = pg.display.set_mode(var.DIMENSION_PANTALLA)
    corriendo =True
    reloj = pg.time.Clock()
    form_actual = 'menu'
    bandera_juego = False
    datos_juego = {
        'volumen_musica' : 100,
        'tiempo_finalizado': None,
        "jugador": {
            "nombre": 'PLAYER',
            "puntaje": 0,
            "cantidad_vidas": var.CANTIDAD_VIDAS
        }
    }
    
    while corriendo:
        
        
        cola_eventos = pg.event.get()
        reloj.tick(var.FPS)
        
        if form_actual == 'menu':
            form_actual = form_menu.mostrar_menu(pantalla, cola_eventos)
        elif form_actual == 'historia':
            if not bandera_juego:
                aux.inicializar_musica(datos_juego)
                bandera_juego = True
            form_actual, bandera_juego = form_historia.mostrar_historia(pantalla, cola_eventos)
            
        elif form_actual == 'juego':
            if not bandera_juego:
                aux.inicializar_musica(datos_juego)
                bandera_juego = True
            form_actual, bandera_juego = form_juego.mostrar_juego(pantalla, cola_eventos, datos_juego)
        elif form_actual == 'salir':
            corriendo = False

        pg.display.flip()
    pg.quit()