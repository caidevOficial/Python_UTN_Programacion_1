import modulos.forms.base_form as base_form
import modulos.variables as var
import modulos.auxiliar as aux
from utn_fra.pygame_widgets import (
    Button, Label
)


def init_form_ranking(dict_form_data: dict, jugador: dict):
    form = base_form.create_base_form(dict_form_data)
    
    form['jugador'] = jugador
    
    form['ranking_screen'] = []
    form['ranking_list'] = []
    
    form['lbl_titulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2 - 250,text='La PYTHONisa del Tarot', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD, font_size=70)
    form['lbl_subtitulo'] = Label(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2 - 175,text='TOP 10 Ranking', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD, font_size=50)
    
    form['btn_volver'] = Button(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2 + 250, text='VOLVER AL MENU', screen=form.get('screen'), font_path=var.FUENTE_ALAGARD, color=var.COLOR_NARANJA, font_size=40, on_click=click_return_menu, on_click_param='form_main_menu')
    form['data_loaded'] = False
    form['widgets_list'] = [
        form.get('lbl_titulo'), form.get('lbl_subtitulo'),
        form.get('btn_volver')
    ]
    
    base_form.forms_dict[dict_form_data.get('name')] = form
    
    return form


def click_return_menu(parametro: str):
    base_form.stop_music()
    base_form.play_music(base_form.forms_dict[parametro])
    base_form.set_active(parametro)
    base_form.forms_dict['form_ranking']['data_loaded'] = False


def init_ranking(form_data: dict):
    form_data['ranking_screen'] = []
    matrix = form_data.get('ranking_list')
    for indice_fila in range(len(matrix)):
        
        fila = matrix[indice_fila]
        
        """
        
        1                   fulano              20
        2                   mengano             15
        
        """
        
        # numero
        form_data['ranking_screen'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2 - 220, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{indice_fila + 1}', screen=form_data.get('screen'), font_path=var.FUENTE_ALAGARD, color=var.COLOR_VERDE, font_size=40)
        )
        
        # nombre
        form_data['ranking_screen'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{fila[0]}', screen=form_data.get('screen'), font_path=var.FUENTE_ALAGARD, color=var.COLOR_VERDE, font_size=40)
        )
        
        # score
        form_data['ranking_screen'].append(
            Label(x=var.DIMENSION_PANTALLA[0]//2 + 220, y=var.DIMENSION_PANTALLA[1]//2.9+indice_fila*31,text=f'{fila[1]}', screen=form_data.get('screen'), font_path=var.FUENTE_ALAGARD, color=var.COLOR_VERDE, font_size=40)
        )
    
    

def inicializar_ranking(form_data: dict):
    if not form_data.get('data_loaded'):
        form_data['ranking_list'] = aux.cargar_ranking()[:10]
        init_ranking(form_data)
        form_data['data_loaded'] = True

def draw(form_data: dict):
    base_form.draw(form_data)
    base_form.draw_widgets(form_data)
    for lbl in form_data.get('ranking_screen'):
        lbl.draw()

def update(form_data: dict):
    
    if form_data.get('active'):
        inicializar_ranking(form_data)
    base_form.update(form_data)