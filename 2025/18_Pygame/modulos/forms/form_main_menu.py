import sys
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.nivel_cartas as nivel_cartas
from utn_fra.pygame_widgets import (
    Label, ButtonImageSound
)


def init_form_main_menu(dict_form_data: dict):
    form = base_form.create_base_form(dict_form_data)
    
    form['lbl_titulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=100,text='La PYTHONisa del Tarot', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD, font_size=50)
    
    form['btn_jugar'] = ButtonImageSound(x=var.DIMENSION_PANTALLA[0]//2, y=150, width=126, height=33,text='', screen=form.get('screen'), image_path=dict_form_data.get('botones').get('jugar'), sound_path=dict_form_data.get('sonido_botones'),  font_size=30, on_click=cambiar_formulario_on_click, on_click_param='form_start_level')
    form['btn_ranking'] = ButtonImageSound(x=var.DIMENSION_PANTALLA[0]//2, y=225, width=126, height=33, text='', screen=form.get('screen'), image_path=dict_form_data.get('botones').get('ranking'), sound_path=dict_form_data.get('sonido_botones'),  font_size=30, on_click=cambiar_formulario_on_click, on_click_param='form_ranking')
    form['btn_historia'] = ButtonImageSound(x=var.DIMENSION_PANTALLA[0]//2, y=290, width=126, height=33, text='', screen=form.get('screen'), image_path=dict_form_data.get('botones').get('historia'), sound_path=dict_form_data.get('sonido_botones'),  font_size=30, on_click=cambiar_formulario_on_click, on_click_param='form_historia')
    form['btn_salir'] = ButtonImageSound(x=var.DIMENSION_PANTALLA[0]//2, y=370, width=126, height=33, text='', screen=form.get('screen'), image_path=dict_form_data.get('botones').get('salir'), sound_path=dict_form_data.get('sonido_botones'),  font_size=30, on_click=click_salir, on_click_param='Boton Salir')
    
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('btn_jugar'), form.get('btn_ranking'),form.get('btn_historia'), form.get('btn_salir')
    ]
    
    base_form.forms_dict[dict_form_data.get('name')] = form
    
    return form


def cambiar_formulario_on_click(parametro: str):
    print(parametro)
    
    if parametro == 'form_start_level':
        form_start_level = base_form.forms_dict[parametro]
        # form_start_level['level'] = nivel_cartas.reiniciar_nivel(
        #     form_start_level.get('level'), form_start_level.get('jugador'), 
        #     form_start_level.get('screen'), form_start_level.get('level_number')
        # )
        # nivel_cartas.inicializar_data_nivel(form_start_level.get('level'))
        
        
        form_start_level.restart_level()
        
    base_form.set_active(parametro)
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])

def click_salir(parametro: str):
    print(parametro)
    sys.exit()

def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.draw_widgets(form_data)

def update(form_data: dict):
    base_form.update(form_data) 
    