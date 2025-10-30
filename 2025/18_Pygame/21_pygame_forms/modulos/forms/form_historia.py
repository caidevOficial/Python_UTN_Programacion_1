import pygame as pg
import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.frases as fra
import random as rd
from utn_fra.pygame_widgets import (
    ButtonImage, Label, TextPoster
)

def init_form_historia(dict_form_data: dict):
    form = base_form.create_base_form(dict_form_data)
    
    form['texto'] = 'HOLA MUNDO'

    form['lbl_titulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=100,text='La PYTHONisa del Tarot', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD, font_size=50)
    form['txt_poster'] = TextPoster(text=fra.historia, screen=form.get('screen'), background_dimentions=(1200, 400), background_coords=(40, 140), font_path=var.FUENTE_ALAGARD, font_size=22, color=(0, 255, 0))
    form['btn_volver'] = ButtonImage(x=993, y=580, text='', width=126, height=33, screen=form.get('screen'), image_path=dict_form_data.get('botones').get('volver'), font_size=30, on_click=click_volver, on_click_param='form_main_menu')
    form['btn_cambiar'] = ButtonImage(x=500, y=580, text='', width=126, height=33, screen=form.get('screen'), image_path=dict_form_data.get('botones').get('volver'), font_size=30, on_click=click_cambiar, on_click_param=(form, 'Hola Div 315'))
    
    
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('txt_poster'), form.get('btn_volver'), form.get('btn_cambiar')
    ]
    
    base_form.forms_dict[dict_form_data.get('name')] = form
    
    return form

def click_volver(parametro: str):
    print(parametro)
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])
    base_form.set_active(parametro)

def click_cambiar(parametro: tuple):
    parametro[0]['txt_poster'].update_coords(rd.choice([(140, 140), (40, 140)]))
    parametro[0]['txt_poster'].update_dimentions(rd.choice([(1000, 350), (1200, 400)]))
    parametro[0]['txt_poster'].update_text(rd.choice([fra.historia, parametro[1]]))
    
def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.draw_widgets(form_data)

def update(form_data: dict):
    base_form.update(form_data)
