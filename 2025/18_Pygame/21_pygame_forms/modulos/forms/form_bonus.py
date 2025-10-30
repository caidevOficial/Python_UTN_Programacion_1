import modulos.forms.base_form as base_form
import modulos.jugador as jugador_mod
import modulos.variables as var
import pygame as pg
from utn_fra.pygame_widgets import (
    Button, Label
)

def init_form_bonus(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)
    form['jugador'] = jugador
    form['bonus_info'] = ''
    
    form['title'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250,
        text=var.TITULO_JUEGO, screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=75, color=var.COLOR_BLANCO
    )
    form['subtitle'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 175,
        text='SELECCIONA EL BONUS DEL MOMENTO', screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=50, color=var.COLOR_BLANCO
    )
    
    form['btn_select'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 - 200, y=var.DIMENSION_PANTALLA[1] // 2 + 50,
        text=form.get('bonus_info'), screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=50,
        on_click=click_select_bonus, on_click_param=form
    )
    
    form['btn_back'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2 + 200, y=var.DIMENSION_PANTALLA[1] // 2 + 50,
        text="CANCELAR", screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=50,
        on_click=click_change_form, on_click_param='form_start_level'
    )
    
    form['widgets_list'] = [
        form.get('title'),form.get('subtitle'),
        form.get('btn_select'),form.get('btn_back')
    ]
    
    base_form.forms_dict[form.get('name')] = form
    
    return form


def click_change_form(param: str):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[param])
    base_form.set_active(param)

def click_select_bonus(form_dict: dict):
    option = form_dict.get('bonus_info')
    
    match option:
        case 'X2':
            jugador_mod.set_puntaje_actual(
                form_dict.get('jugador'),
                jugador_mod.get_puntaje_actual(form_dict.get('jugador')) * 2
            )
        case '+50':
            jugador_mod.set_puntaje_actual(
                form_dict.get('jugador'),
                jugador_mod.get_puntaje_actual(form_dict.get('jugador')) + 50
            )
    # reproducir sonido de bonus
    pg.time.wait(2000)
    click_change_form('form_start_level')

def update_button_bonus(form_dict: dict, new_text: str):
    form_dict['bonus_info'] = new_text
    form_dict.get('widgets_list')[2].update_text(form_dict.get('bonus_info'), var.COLOR_CIAN)


def draw(form_dict: dict):
    base_form.draw(form_dict)
    base_form.draw_widgets(form_dict)

def update(form_dict: dict):
    base_form.update(form_dict)