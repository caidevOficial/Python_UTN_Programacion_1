from data_heroes import *
from app import utn_heroes_app
from funciones import DEBUG

if __name__ == '__main__':
    DEBUG = False
    utn_heroes_app(lista_nombres_heroes, lista_identidades_heroes,
                   lista_generos_heroes, lista_poder_heroes, lista_alturas_heroes, DEBUG)
