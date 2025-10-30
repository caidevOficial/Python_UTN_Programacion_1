import pygame as pg 
import modulos.variables as var
import modulos.auxiliar as aux
import random as rd
import modulos.frases as fra
import modulos.carta as carta
import modulos.jugador as jugador_humano

def inicializar_nivel_cartas(jugador: dict, pantalla: pg.Surface, nro_nivel: int):
    
    nivel_data = {}
    nivel_data['nro_nivel'] = nro_nivel
    nivel_data['configs'] = {}
    nivel_data['cartas_mazo_juego'] = []
    nivel_data['cartas_mazo_juego_final'] = []
    nivel_data['cartas_mazo_juego_final_vistas'] = []
    nivel_data['ruta_mazo'] = ''
    nivel_data['screen'] = pantalla
    nivel_data['jugador'] = jugador
    
    nivel_data['juego_finalizado'] = False
    nivel_data['puntaje_guardado'] = False
    nivel_data['level_timer'] = var.timer
    nivel_data['ganador'] = None
    
    # nivel_data['surface'] = pg.image.load('./assets/background/fondo_5.png').convert_alpha()
    # nivel_data['surface'] = pg.transform.scale(nivel_data.get('surface'), var.DIMENSION_PANTALLA)
    
    # nivel_data['rect'] = nivel_data.get('surface').get_rect()
    # nivel_data['rect'].topleft = (0,0)
    
    nivel_data['puntaje_nivel'] = 0
    nivel_data['data_cargada'] = False
    
    return nivel_data

def inicializar_data_nivel(nivel_data: dict):
    print('ESTOY GASTANDO RECURSOS Y CARGANDO TODA LA DATA DEL LEVEL')
    cargar_configs_nivel(nivel_data)
    cargar_bd_cartas(nivel_data)
    asignar_frases(nivel_data)
    generar_mazo(nivel_data)

def cargar_configs_nivel(nivel_data: dict):
    if not nivel_data.get('juego_finalizado') and not nivel_data.get('data_cargada'):
        print('=============== CARGANDO CONFIGS INICIALES ===============')
        configs_globales = aux.cargar_configs(var.RUTA_CONFIGS_JSON)
        nivel_data['configs'] = configs_globales.get(f'nivel_{nivel_data.get("nro_nivel")}')
        nivel_data['ruta_mazo'] = nivel_data.get('configs').get('ruta_mazo')
        nivel_data['coords_iniciales'] = nivel_data.get('configs').get('coordenada_mazo_1')
        nivel_data['coords_finales'] = nivel_data.get('configs').get('coordenada_mazo_2')

def cargar_bd_cartas(nivel_data: dict):
    if not nivel_data.get('juego_finalizado'):
        print('=============== GENERANDO BD CARTAS INICIALES ===============')
        nivel_data['cartas_mazo_juego'] = aux.generar_bd(nivel_data.get('ruta_mazo')).get('cartas').get('./assets/decks/raider_waite')

def asignar_frases(nivel_data: dict) -> list[dict]:
    print('=============== ASIGNANDO FRASES ALEATORIAS ===============')
    lista_mazo = nivel_data.get('cartas_mazo_juego')
    for index_card in range(len(lista_mazo)):
        frase = rd.choice(fra.lista_frases)
        
        carta.set_frase(lista_mazo[index_card], frase.get('frase'))
        carta.set_puntaje(lista_mazo[index_card], frase.get('puntaje'))
    return lista_mazo

def generar_mazo(nivel_data: dict):
    print('=============== GENERANDO MAZO FINAL ===============')
    lista_mazo_original = nivel_data.get('cartas_mazo_juego')
    nivel_data['cartas_mazo_juego_final'] = []
    # print(
    #     f'Coord iniciales: {nivel_data.get('coords_iniciales')}',
    #     f'Coord finales: {nivel_data.get('coords_finales')}', sep='\n'
    # )
    for card in lista_mazo_original:
        carta_final = carta.inicializar_carta(card, nivel_data.get('coords_iniciales'))
        nivel_data['cartas_mazo_juego_final'].append(carta_final)
    
    nivel_data['cartas_mazo_juego_final'] = nivel_data['cartas_mazo_juego_final'][:10]
    
    rd.shuffle(nivel_data.get('cartas_mazo_juego_final'))

def eventos(nivel_data: dict, cola_eventos: list[pg.event.Event]):
    
    for evento in cola_eventos:
        if evento.type == pg.MOUSEBUTTONDOWN:
            print(f'Coordenada: {evento.pos}')
            # verificar la colision con el boton
            if nivel_data.get('cartas_mazo_juego_final') and\
               nivel_data.get('cartas_mazo_juego_final')[-1].get('rect').collidepoint(evento.pos) and\
               not nivel_data.get('cartas_mazo_juego_final')[-1].get('visible'):
                var.SOUND.play()
                carta.asignar_coordenadas_carta(nivel_data.get('cartas_mazo_juego_final')[-1], nivel_data.get('coords_finales'))
                carta.cambiar_visibilidad_carta(nivel_data.get('cartas_mazo_juego_final')[-1])
                
                carta_vista = nivel_data.get('cartas_mazo_juego_final').pop()
                nivel_data.get('cartas_mazo_juego_final_vistas').append(carta_vista)
                
                carta_actual = nivel_data.get('cartas_mazo_juego_final_vistas')[-1]
                jugador_humano.sumar_puntaje_carta_actual(nivel_data.get('jugador'), carta_actual)
                
                print(f'Puntaje Actual: {jugador_humano.get_puntaje_actual(nivel_data["jugador"])}')
                
                print(f'Frase actual: {nivel_data.get('cartas_mazo_juego_final_vistas')[-1].get('frase')}')

def tiempo_esta_terminado(nivel_data: dict):
    return nivel_data.get('level_timer') <= 0

def mazo_esta_vacio(nivel_data: dict):
    return len(nivel_data.get('cartas_mazo_juego_final')) == 0

def check_juego_terminado(nivel_data: dict):
    if mazo_esta_vacio(nivel_data) or\
        tiempo_esta_terminado(nivel_data):
            nivel_data['juego_finalizado'] = True

def juego_terminado(nivel_data: dict):
    return nivel_data.get('juego_finalizado')

def reiniciar_nivel(nivel_cartas: dict, jugador: dict, pantalla: pg.Surface, nro_nivel: int):
    print('=============== REINICIANDO NIVEL ===============')
    jugador_humano.set_puntaje_actual(jugador, 0)
    nivel_cartas = inicializar_nivel_cartas(jugador, pantalla, nro_nivel)
    return nivel_cartas

def draw(nivel_data: dict):
    if nivel_data.get('cartas_mazo_juego_final'):
        carta.draw_carta(nivel_data.get('cartas_mazo_juego_final')[-1], nivel_data.get('screen'))
        
    if nivel_data.get('cartas_mazo_juego_final_vistas'):
        carta.draw_carta(nivel_data.get('cartas_mazo_juego_final_vistas')[-1], nivel_data.get('screen'))

def update(nivel_data: dict, cola_eventos: list[pg.event.Event]):
    eventos(nivel_data, cola_eventos)
    check_juego_terminado(nivel_data)
    if juego_terminado(nivel_data) and not nivel_data.get('puntaje_guardado'):
        jugador_humano.actualizar_puntaje_total(nivel_data.get("jugador"))
        # nombre_elegido = rd.choice(var.nombres)
        # jugador_humano.set_nombre(nivel_data.get("jugador"), nombre_elegido)
        # aux.guardar_ranking(nivel_data.get('jugador'))
        nivel_data['puntaje_guardado'] = True
        print(f'Puntaje acumulado: {jugador_humano.get_puntaje_total(nivel_data.get("jugador"))}')
