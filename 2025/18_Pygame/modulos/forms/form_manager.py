import pygame as pg
import modulos.variables as var
import modulos.forms.form_main_menu as form_main_menu
import modulos.forms.form_historia as form_historia
import modulos.forms.form_ranking as form_ranking
import modulos.forms.form_start_level as form_start_level
import modulos.forms.form_enter_name as form_enter_name
import modulos.forms.form_pause as form_pause
import modulos.forms.form_bonus as form_bonus


def create_form_manager(screen: pg.Surface, datos_juego: dict):
    form = {}
    form['main_screen'] = screen
    form['current_level'] = 1
    form['game_started'] = False
    form['player'] = None
    form['enemy'] = None
    
    form['jugador'] = datos_juego.get('jugador')
    
    form['form_list'] = [
        form_main_menu.init_form_main_menu(
            dict_form_data={
                "name":'form_main_menu', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "background_path": './assets/background/fondo_3.png',
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "botones": {
                    "jugar": 'assets/buttons/btn_jugar.png',
                    "historia": 'assets/buttons/btn_historia.png',
                    "ranking": 'assets/buttons/btn_ranking.png',
                    "salir": 'assets/buttons/btn_salir.png',
                },
                "sonido_botones": 'assets/sound/click.mp3'
            }
        ),
        form_historia.init_form_historia(
            dict_form_data={
                "name":'form_historia', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA,
                "background_path": './assets/background/fondo_tablero.png',
                "screen_dimentions": var.DIMENSION_PANTALLA,
                "botones": {
                    "volver": 'assets/buttons/btn_volver.png',
                }
            }
        ),
        form_ranking.init_form_ranking(
            dict_form_data={
                "name":'form_ranking', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_RANKING,
                "background_path": './assets/background/fondo_5.png',
                "screen_dimentions": var.DIMENSION_PANTALLA
            }, jugador=form.get('jugador')
        ),
        form_start_level.init_form_start_level(
            dict_form_data={
                "name":'form_start_level', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_JUEGO,
                "background_path": './assets/background/fondo_6.png',
                "screen_dimentions": var.DIMENSION_PANTALLA
            }, jugador=form.get('jugador')
        ),
        form_enter_name.init_form_enter_name(
            dict_form_data={
                "name":'form_enter_name', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA,
                "background_path": './assets/background/fondo_2.png',
                "screen_dimentions": var.DIMENSION_PANTALLA
            },jugador=form.get('jugador')
        ),
        form_pause.init_form_pause(
            dict_form_data={
                "name":'form_pause', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_MENU,
                "background_path": './assets/background/fondo_8.png',
                "screen_dimentions": var.DIMENSION_PANTALLA
            }
        ),
        form_bonus.init_form_bonus(
            dict_form_data={
                "name":'form_bonus', 
                "screen":form.get('main_screen'), 
                "active":True, "coords":(0,0), 
                "stage_number":1, 
                "music_path":var.RUTA_MUSICA_RANKING,
                "background_path": './assets/background/fondo_7.png',
                "screen_dimentions": var.DIMENSION_PANTALLA
            },jugador=form.get('jugador')
        )
    ]
    
    return form


def forms_update(form_manager: dict, lista_eventos: pg.event.Event):
    # Preguntar por cada uno de los formularios si esta activo
    # en caso de estarlo, dibujar y actualizar
    
    # FORM MENU
    if form_manager.get('form_list')[0].get('active'):
        form_main_menu.update(form_manager.get('form_list')[0])
        form_main_menu.draw(form_manager.get('form_list')[0])
    
    # FORM HISTORIA
    elif form_manager.get('form_list')[1].get('active'):
        form_historia.update(form_manager.get('form_list')[1])
        form_historia.draw(form_manager.get('form_list')[1])
    
    # FORM RANKING
    elif form_manager.get('form_list')[2].get('active'):
        form_ranking.update(form_manager.get('form_list')[2])
        form_ranking.draw(form_manager.get('form_list')[2])
    
    # FORM START LEVEL
    elif form_manager.get('form_list')[3].get('active'):
        form_start_level.update(form_manager.get('form_list')[3], lista_eventos)
        form_start_level.draw(form_manager.get('form_list')[3])
    
    # FORM ENTER NAME
    elif form_manager.get('form_list')[4].get('active'):
        form_enter_name.update(form_manager.get('form_list')[4], lista_eventos)
        form_enter_name.draw(form_manager.get('form_list')[4])
    
    # FORM PAUSE
    elif form_manager.get('form_list')[5].get('active'):
        form_pause.update(form_manager.get('form_list')[5])
        form_pause.draw(form_manager.get('form_list')[5])

    # FORM BONUS
    elif form_manager.get('form_list')[6].get('active'):
        form_bonus.update(form_manager.get('form_list')[6])
        form_bonus.draw(form_manager.get('form_list')[6])

def update(form_manager: dict, lista_eventos: pg.event.Event):
    forms_update(form_manager, lista_eventos)
    