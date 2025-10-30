import pygame as pg
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.nivel_cartas as nivel_cartas
import modulos.forms.form_bonus as form_bonus
from utn_fra.pygame_widgets import (
    ButtonImage, Label, TextPoster, Button
)

def init_form_start_level(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)
    
    form['jugador'] = jugador
    
    
    form['level'] = nivel_cartas.inicializar_nivel_cartas(form.get('jugador'), form.get('screen'), form.get('level_number'))
    
    form['clock'] = pg.time.Clock()
    form['first_last_timer'] = pg.time.get_ticks()
    form['bonus_1_used'] = False
    form['bonus_2_used'] = False
    
    form['lbl_clock'] = Label(x=var.DIMENSION_PANTALLA[0] // 2, y=50, text=f'TIME LEFT: {form.get("level").get("level_timer")}', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD)
    form['lbl_score'] = Label(x=250, y=50, text=f'SCORE: {form.get("jugador").get("puntaje_actual")}', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD)
    
    form['txp_info_card'] = TextPoster(
        text='', screen=form.get('screen'), background_dimentions=(500, 100), background_coords=(390, 584),
        font_path=var.FUENTE_ALAGARD, font_size=25, color=(0,255,0), background_color=(0,0,0)
    )
    
    
    form['btn_bonus_1'] = Button(
        x=1050, y=var.DIMENSION_PANTALLA[1] // 2 + 200,
        text='BONUS X2',
        screen=form.get('screen'), font_path=var.FUENTE_ALAGARD,
        font_size=40, color=var.COLOR_NEGRO,
        on_click=select_bonus, on_click_param={'form': form, 'bonus': 'X2'}
    )
    
    form['btn_bonus_2'] = Button(
        x=1050, y=var.DIMENSION_PANTALLA[1] // 2 + 250,
        text='BONUS +50',
        screen=form.get('screen'), font_path=var.FUENTE_ALAGARD,
        font_size=40, color=var.COLOR_NEGRO,
        on_click=select_bonus, on_click_param={'form': form, 'bonus': '+50'}
    )
    
    
    form['widgets_list'] = [
        form.get('lbl_clock'), form.get('lbl_score'), form.get('txp_info_card'),
        form.get('btn_bonus_1'), form.get('btn_bonus_2')
    ]
    
    base_form.forms_dict[dict_form_data.get('name')] = form
    
    return form

def select_bonus(form_y_bonus_name: dict):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict['form_bonus'])
    base_form.set_active('form_bonus')
    # base_form.forms_dict['form_bonus'].update_button_bonus(base_form.forms_dict['form_bonus'],form_y_bonus_name)
    form_bonus.update_button_bonus(base_form.forms_dict['form_bonus'],form_y_bonus_name.get('bonus'))
    if form_y_bonus_name.get('bonus') == 'X2':
        form_y_bonus_name['form']['bonus_1_used'] = True
    else:
        form_y_bonus_name['form']['bonus_2_used'] = True

def actualizar_timer(dict_form_data: dict):
    if dict_form_data.get('level').get('level_timer') > 0:
        tiempo_actual = pg.time.get_ticks()
        if tiempo_actual - dict_form_data.get('first_last_timer') > 1000:
            dict_form_data.get('level')['level_timer'] -= 1
            dict_form_data['first_last_timer'] = tiempo_actual

def events_handler(events_list: list[pg.event.Event]):
    for evento in events_list:
        if evento.type == pg.KEYDOWN:
            if evento.key == pg.K_ESCAPE:
                base_form.set_active('form_pause')
                base_form.stop_music()
                base_form.play_music(base_form.forms_dict['form_pause'])

def draw(dict_form_data: dict):
    base_form.draw(dict_form_data)
    
    for widget_index in range(len(dict_form_data.get('widgets_list'))):
        if widget_index == 3 and dict_form_data.get('bonus_1_used') or\
            widget_index == 4 and dict_form_data.get('bonus_2_used'):
            continue

        dict_form_data.get('widgets_list')[widget_index].draw()
        
    nivel_cartas.draw(dict_form_data.get('level'))
    

def update(dict_form_data: dict, cola_eventos: list[pg.event.Event]):
    # base_form.update(dict_form_data)
    
    dict_form_data['lbl_clock'].update_text(f'TIME LEFT: {dict_form_data.get("level").get("level_timer")}', (255, 0, 0))
    dict_form_data['lbl_score'].update_text(f'SCORE: {dict_form_data.get('jugador').get('puntaje_actual')}', (255, 0, 0))
    
    
    for widget_index in range(len(dict_form_data.get('widgets_list'))):
        if widget_index == 3 and dict_form_data.get('bonus_1_used') or\
            widget_index == 4 and dict_form_data.get('bonus_2_used'):
            continue

        dict_form_data.get('widgets_list')[widget_index].update()
        
    nivel_cartas.update(dict_form_data.get('level'), cola_eventos)
    
    
    mazo_vistas = dict_form_data.get('level').get('cartas_mazo_juego_final_vistas')
    if mazo_vistas:
        dict_form_data['txp_info_card'].update_text(mazo_vistas[-1].get('frase'))
    
    dict_form_data['clock'].tick(var.FPS)
    actualizar_timer(dict_form_data)
    
    if nivel_cartas.juego_terminado(dict_form_data.get('level')):
        base_form.stop_music()
        base_form.play_music(base_form.forms_dict['form_enter_name'])
        base_form.set_active('form_enter_name')
    
    events_handler(cola_eventos)