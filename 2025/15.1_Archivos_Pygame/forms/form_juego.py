import pygame as pg
import variables as var
import auxiliar as aux
import frases as fra
import random as rd
import carta

cuadro_titulo = aux.crear_cuadro(var.DIMENSION_TITULO, var.COORDENADA_CAJA_TITULO, var.COLOR_NEGRO)
cuadro_frase = aux.crear_cuadro(var.DIMENSION_FRASE, var.COORDENADA_CAJA_FRASE, var.COLOR_NEGRO)

cuadro_puntaje = aux.crear_cuadro(var.DIMENSION_PUNTAJE, var.COORDENADA_PUNTAJE, var.COLOR_NEGRO)

rd.shuffle(fra.lista_frases)

cartas = aux.generar_bd(var.RUTA_MAZO_MAIN)
raider_waite = cartas.get('cartas').get('raider_waite')
# senkai_yami = cartas.get('cartas').get('senkai_yami')


raider_waite = aux.asignar_frases(raider_waite, fra.lista_frases)
# senkai_yami = aux.asignar_frases(senkai_yami, fra.lista_frases)

lista_cartas_dictionary = aux.generar_mazo(raider_waite)

# lista_cartas_dictionary.extend(aux.generar_mazo(senkai_yami))
rd.shuffle(lista_cartas_dictionary)

lista_cartas_dictionary = lista_cartas_dictionary[0:5]

lista_cartas_vistas = []

def mostrar_juego(pantalla: pg.Surface, cola_eventos: list[pg.event.Event], datos_juego: dict):
    bandera_juego = True
    boton_volver = aux.crear_boton(pantalla, 'VOLVER', var.FUENTE_32, var.DIMENSION_BOTON_BACK, (993, 580), var.COLOR_NEGRO, var.COLOR_ROJO)
    
    retorno = 'juego'
    
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
            
            if lista_cartas_dictionary and\
               lista_cartas_dictionary[-1].get('rect').collidepoint(evento.pos) and\
               not lista_cartas_dictionary[-1].get('visible'):
                   var.CLICK_SONIDO.play()
                   carta.asignar_coordenadas_carta(lista_cartas_dictionary[-1], var.COORDENADA_CARTA_VISTA)
                   carta.cambiar_visibilidad_carta(lista_cartas_dictionary[-1])
                   
                   carta_vista = lista_cartas_dictionary.pop()
                   lista_cartas_vistas.append(carta_vista)
                   
                   print(f'Frase actual: {lista_cartas_vistas[-1].get('frase')}')
                   cuadro_frase['superficie'].fill(var.COLOR_NEGRO)
                   
                   aux.actualizar_puntaje(datos_juego, lista_cartas_vistas[-1].get('puntaje'))
                   
                   print(f"Puntaje actual: {datos_juego.get('puntaje')}")
                   
    
    
    
    pantalla.fill(var.COLOR_VIOLETA)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    aux.mostrar_texto(cuadro_titulo['superficie'], 'La PYTHONisa del Tarot', (20,20), var.FUENTE_50, var.COLOR_VERDE)
    
    
    
    cuadro_puntaje['superficie'].fill(var.COLOR_NEGRO)
    aux.mostrar_texto(cuadro_puntaje['superficie'], f'Score: {datos_juego.get("puntaje")}', (20,20), var.FUENTE_32, var.COLOR_ROJO)
    
    aux.mostrar_boton(boton_volver)
    
    
    
    if lista_cartas_dictionary:
        carta.draw_carta(lista_cartas_dictionary[-1], pantalla)
        
            
    if lista_cartas_vistas:
        carta.draw_carta(lista_cartas_vistas[-1], pantalla)
        # Gestionar mensaje texto
        aux.mostrar_texto(cuadro_frase.get('superficie'), f'{lista_cartas_vistas[-1].get("frase")}', (20, 20), var.FUENTE_25, var.COLOR_AMARILLO)
        cuadro_frase['rectangulo'] = pantalla.blit(cuadro_frase['superficie'], cuadro_frase['rectangulo'].topleft)

    cuadro_titulo['rectangulo'] = pantalla.blit(cuadro_titulo['superficie'], cuadro_titulo['rectangulo'].topleft)
    cuadro_puntaje['rectangulo'] = pantalla.blit(cuadro_puntaje['superficie'], cuadro_puntaje['rectangulo'].topleft)
    
    if not lista_cartas_dictionary and not datos_juego.get('tiempo_finalizado'):
        datos_juego['tiempo_finalizado'] = pg.time.get_ticks()
        print(f'Tiempo finalizado: {datos_juego.get('tiempo_finalizado')}')
        aux.grabar_puntaje(datos_juego)
        # retorno = 'menu'
    
    if not lista_cartas_dictionary:
        retorno = aux.verificar_tiempo_cumplido(datos_juego.get('tiempo_finalizado'), ('historia', 'juego'))
        aux.terminar_musica()

    return retorno, bandera_juego
