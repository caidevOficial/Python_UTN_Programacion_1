import pygame as pg 

forms_dict = {}

# def create_base_form(name: str, screen: pg.Surface, active: bool, coords: tuple[int, int], level_num: int, music_path: str) -> dict:
def create_base_form(dict_form_data: dict) -> dict:
    form = {}
    form['name'] = dict_form_data.get('name')
    form['screen'] = dict_form_data.get('screen')
    form['active'] = dict_form_data.get('active')
    form['x_coord'] = dict_form_data.get('coords')[0]
    form['y_coord'] = dict_form_data.get('coords')[1]
    form['level_number'] = dict_form_data.get('stage_number')
    form['music_path'] = dict_form_data.get('music_path')
    form['surface'] = pg.image.load(dict_form_data.get('background_path')).convert_alpha()
    form['surface'] = pg.transform.scale(form.get('surface'), dict_form_data.get('screen_dimentions'))
    
    form['rect'] = form.get('surface').get_rect()
    form['rect'].x = dict_form_data.get('coords')[0]
    form['rect'].y = dict_form_data.get('coords')[1]
    return form

def play_music(form_dict: dict):
    pg.mixer.music.load(form_dict.get('music_path'))
    pg.mixer.music.set_volume(0.4)
    pg.mixer.music.play(loops=-1, fade_ms=400)

def stop_music():
    pg.mixer.music.stop()

def set_active(name: str):
    for form in forms_dict.values():
        form['active'] = False
    forms_dict[name]['active'] = True
    print(f'Form Activo: {name}')

def update_widgets(form_data: dict):
    for widget in form_data.get('widgets_list'):
        widget.update()

def draw_widgets(form_data: dict):
    for widget in form_data.get('widgets_list'):
        widget.draw()

def draw(form_data: dict):
    form_data['screen'].blit(form_data.get('surface'), form_data.get('rect'))

def update(form_data: dict):
    update_widgets(form_data)
    
    
