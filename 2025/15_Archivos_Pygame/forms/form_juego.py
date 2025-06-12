import pygame as pg
import random
import variables as var
import auxiliar as aux
import frases as fra
import carta as car 



pg.init()

cuadro_frase = aux.crear_cuadro(var.DIMENSION_PREGUNTA, var.COORDENADA_CAJA_TEXTO, var.COLOR_NEGRO)
cuadro_titulo = aux.crear_cuadro(var.DIMENSION_TITULO, var.COORDENADA_CAJA_TITULO, var.COLOR_NEGRO)



random.shuffle(fra.lista_frases)

cartas = aux.generar_bd(var.RUTA_MAZO_MAIN)
raider_waite = cartas.get('cartas').get('raider_waite')
senkai_yami = cartas.get('cartas').get('senkai_yami')


raider_waite = aux.asignar_frases(raider_waite, fra.lista_frases)
senkai_yami = aux.asignar_frases(senkai_yami, fra.lista_frases)

lista_cartas_dict = aux.generar_mazo(raider_waite)

lista_frase = []
lista_cartas_vistas = []


# cuadro_respuesta = {}
# cuadro_respuesta["superficie"] = pg.Surface(var.DIMENSION_RESPUESTA)
# cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
# cuadro_respuesta["superficie"].fill(var.COLOR_AZUL)
# lista_frase.append(cuadro_respuesta)
    
indice = 0 #Son inmutables
bandera_respuesta = False #Son inmutables

def mostrar_juego(pantalla:pg.Surface,cola_eventos:list[pg.event.Event],datos_juego:dict) -> str:
    global indice
    global bandera_respuesta
    global lista_cartas_dict
    
    boton_volver = aux.crear_boton(pantalla, 'Volver', var.FUENTE_32, var.DIMENSION_BOTON_BACK, (993, 579), var.COLOR_NEGRO, var.COLOR_ROJO)
    
    bandera_juego = True
    retorno = "juego"
    if bandera_respuesta:
        pg.time.delay(250)
        cuadro_frase["superficie"].fill(var.COLOR_ROJO)
        #Limpio la superficie
        # cuadro_frase["superficie"] = pg.image.load("fondo.jpg")
        # cuadro_frase["superficie"] = pg.transform.scale(fondo,DIMENSION_PREGUNTA)
        # for i in range(len(lista_respuestas)):
        #     lista_respuestas[i]["superficie"].fill(var.COLOR_AZUL)
        bandera_respuesta = False
    
    for evento in cola_eventos:
        if evento.type == pg.QUIT:
            retorno = "salir"
        elif evento.type == pg.MOUSEBUTTONDOWN:
            print(f'Coordenada: {evento.pos}')
            if lista_cartas_dict and lista_cartas_dict[-1]['rect'].collidepoint(evento.pos) and not lista_cartas_dict[-1].get('visible'):
                var.CLICK_SONIDO.play()
                print(car.get_id_carta(lista_cartas_dict[-1]))
                car.asignar_coordenadas_carta(lista_cartas_dict[-1], var.COORDENADA_CARTA_VISTA)
                car.cambiar_visibilidad_carta(lista_cartas_dict[-1])
                lista_cartas_vistas.append(lista_cartas_dict.pop())
                print(lista_cartas_vistas[-1].get('frase'))
                cuadro_frase["superficie"].fill(var.COLOR_NEGRO)
            if boton_volver.get('rectangulo').collidepoint(evento.pos):
                var.CLICK_SONIDO.play()
                retorno = 'menu'
                bandera_juego = False
                pg.mixer.music.fadeout(1)
    
    pantalla.fill(var.COLOR_VIOLETA)
    pantalla.blit(var.fondo, var.fondo.get_rect())
    
    aux.mostrar_texto(cuadro_titulo["superficie"], f"La PYTHONisa del Tarot",(20,20),var.FUENTE_50,var.COLOR_VERDE)
    aux.mostrar_boton(boton_volver)
    
    if lista_cartas_dict:
        car.draw_carta(lista_cartas_dict[-1],pantalla)
    if lista_cartas_vistas:
        car.draw_carta(lista_cartas_vistas[-1],pantalla)
        # print(lista_cartas_vistas[-1])
        aux.mostrar_texto(cuadro_frase["superficie"], f"{lista_cartas_vistas[-1].get('frase')}",(20,20),var.FUENTE_27,var.COLOR_VERDE)
        cuadro_frase["rectangulo"] = pantalla.blit(cuadro_frase["superficie"], cuadro_frase["rectangulo"].topleft)
        pg.draw.rect(pantalla,var.COLOR_NEGRO, cuadro_frase["rectangulo"],2)
    
    cuadro_titulo["rectangulo"] = pantalla.blit(cuadro_titulo["superficie"], cuadro_titulo["rectangulo"].topleft)
    
    return retorno, bandera_juego