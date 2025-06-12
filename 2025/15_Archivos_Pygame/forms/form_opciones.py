import pygame as pg
import variables as var
import auxiliar as aux

boton_suma = {}
boton_suma["superficie"] = pg.Surface(var.DIMENSION_BOTON_VOLUMEN)
boton_suma["rectangulo"] = boton_suma["superficie"].get_rect()
boton_suma["superficie"].fill(var.COLOR_ROJO)

boton_resta = {}
boton_resta["superficie"] = pg.Surface(var.DIMENSION_BOTON_VOLUMEN)
boton_resta["rectangulo"] = boton_resta["superficie"].get_rect()
boton_resta["superficie"].fill(var.COLOR_ROJO)

boton_volver = {}
boton_volver["superficie"] = pg.Surface(var.DIMENSION_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(var.COLOR_AZUL)

def mostrar_ajustes(pantalla:pg.Surface,cola_eventos:list[pg.event.Event],datos_juego:dict) -> str:
    retorno = "configuracion"
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = "salir"
        elif evento.type == pg.MOUSEBUTTONDOWN:
            if boton_suma["rectangulo"].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] < 100:
                    datos_juego["volumen_musica"] += 5
                # else:
                #     # ERROR_SONIDO.play()
                print("SUMA VOLUMEN")
            elif boton_resta["rectangulo"].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                if datos_juego["volumen_musica"] > 0:
                    datos_juego["volumen_musica"] -= 5
                # else:
                #     # ERROR_SONIDO.play()
                print("RESTA VOLUMEN")
            elif boton_volver["rectangulo"].collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = "menu"
                print("VUELVE AL MENU")
    
    pantalla.fill(var.COLOR_BLANCO)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    boton_resta["rectangulo"] = pantalla.blit(boton_resta["superficie"],(20,200))
    boton_suma["rectangulo"] = pantalla.blit(boton_suma["superficie"],(420,200))    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"],(10,10))
    
    aux.mostrar_texto(boton_suma["superficie"],"VOL+",(0,10),var.FUENTE_22,var.COLOR_NEGRO)
    aux.mostrar_texto(boton_resta["superficie"],"VOL-",(0,10),var.FUENTE_22,var.COLOR_NEGRO)
    aux.mostrar_texto(boton_volver["superficie"],"VOLVER",(5,5),var.FUENTE_22,var.COLOR_BLANCO)
    aux.mostrar_texto(pantalla,f"{datos_juego["volumen_musica"]} %",(200,200),var.FUENTE_50,var.COLOR_NEGRO)
    
    return retorno