import modulos.forms.base_form as base_form
import modulos.variables as var
from utn_fra.pygame_widgets import (
    Button, Label
)

def init_form_pause(dict_form_data: dict):
    form = base_form.create_base_form(dict_form_data)
    
    form['title'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 250,
        text=var.TITULO_JUEGO, screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=75, color=var.COLOR_NEGRO
    )
    form['subtitle'] = Label(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 - 175,
        text='PAUSA, TOMATE UN CAFE!', screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, font_size=50, color=var.COLOR_NEGRO
    )
    
    form['btn_back'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 175,
        text="VOLVER AL MENU", screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, color=var.COLOR_NEGRO,
        on_click=click_change_form, on_click_param='form_main_menu'
    )
    
    form['btn_resume'] = Button(
        x=var.DIMENSION_PANTALLA[0] // 2, y=var.DIMENSION_PANTALLA[1] // 2 + 250,
        text="VOLVER AL JUEGO", screen=form.get('screen'), 
        font_path=var.FUENTE_ALAGARD, color=var.COLOR_NEGRO,
        on_click=click_change_form, on_click_param='form_start_level'
    )
    
    form['widgets_list'] = [
        form.get('title'), form.get('subtitle'),
        form.get('btn_back'), form.get('btn_resume')
    ]
    
    base_form.forms_dict[form.get('name')] = form
    
    return form

def click_change_form(param: str):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[param])
    base_form.set_active(param)

def draw(form_dict: dict):
    base_form.draw(form_dict)
    base_form.draw_widgets(form_dict)

def update(form_dict: dict):
    base_form.update(form_dict)