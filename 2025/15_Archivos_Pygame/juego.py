import pygame as pg
import variables as var
import auxiliar as aux
import forms.form_menu as menu
import forms.form_opciones as opciones
import forms.form_juego as juego
import forms.form_historia as historia

def pythonisa():
    
    pg.display.set_caption(var.TITULO_JUEGO)
    pantalla = pg.display.set_mode(var.DIMENSION_PANTALLA)
    corriendo = True
    reloj = pg.time.Clock()
    datos_juego = {"puntuacion":0,"cantidad_vidas":var.CANTIDAD_VIDAS,"nombre":"","volumen_musica":100}
    ventana_actual = "menu"
    bandera_juego = False

    while corriendo:
        #Gestion de Eventos -> No lo programamos aca
        #Actualizacion de estados -> No lo programamos aca
        #Imprimir en pantalla esa informacion -> No lo programamos aca
        cola_eventos = pg.event.get()
        reloj.tick(var.FPS)
            
        if ventana_actual == "menu":
            ventana_actual = menu.mostrar_menu(pantalla,cola_eventos)
        elif ventana_actual == "juego":
            if bandera_juego == False:
                aux.iniciar_musica(datos_juego)
                bandera_juego = True
            ventana_actual, bandera_juego = juego.mostrar_juego(pantalla,cola_eventos,datos_juego)
        elif ventana_actual == "configuracion":
            ventana_actual = opciones.mostrar_ajustes(pantalla,cola_eventos,datos_juego)
        elif ventana_actual == "historia":
            if bandera_juego == False:
                aux.iniciar_musica(datos_juego)
                bandera_juego = True
            ventana_actual, bandera_juego = historia.mostrar_historia(pantalla, cola_eventos)
        elif ventana_actual == "terminado":
            pass
        elif ventana_actual == "salir":
            corriendo = False
        
        pg.display.flip()
    pg.quit()
        