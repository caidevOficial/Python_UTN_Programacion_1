
import auxiliares
from validaciones import validar_input
import os

def utn_industries_app_3(lista_heroes: list[dict]):
    
    corriendo = True
    
    while corriendo:
        
        auxiliares.imprimir_menu_desafio_3_5()
        opcion = validar_input(min_str='A', max_str='Q')
        
        match opcion:
            case 'A':
                auxiliares.utn_imprimir_heroe_genero(lista_heroes, 'Masculino')
            case 'B':
                auxiliares.utn_imprimir_heroe_genero(lista_heroes, 'Femenino')
            case 'C':
                auxiliares.utn_calcular_imprimir_heroe_raza(lista_heroes, 'maximo', 'altura_mts', 'Human')
            case 'D':
                auxiliares.utn_calcular_imprimir_heroe_raza(lista_heroes, 'maximo', 'altura_mts', 'Desconocido')
            case 'E':
                auxiliares.utn_calcular_imprimir_heroe_raza(lista_heroes, 'minimo', 'altura_mts', 'Symbiote')
            case 'F':
                auxiliares.utn_calcular_imprimir_heroe_raza(lista_heroes, 'minimo', 'altura_mts', 'Mutant')
            case 'G':
                auxiliares.utn_calcular_imprimir_promedio_altura_empresa(lista_heroes, 'altura_mts', 'DC Comics')
            case 'H':
                auxiliares.utn_calcular_imprimir_promedio_altura_empresa(lista_heroes, 'altura_mts', 'Marvel Comics')
            case 'J':
                auxiliares.utn_calcular_cantidad_por_tipo(lista_heroes, 'color_ojos')
            case 'K':
                auxiliares.utn_calcular_cantidad_por_tipo(lista_heroes, 'color_pelo')
            case 'L':
                auxiliares.utn_calcular_cantidad_por_tipo(lista_heroes, 'alineacion')
            case 'M':
                auxiliares.utn_listar_personajes_por_dato(lista_heroes,'color_ojos')
            case 'N':
                auxiliares.utn_listar_personajes_por_dato(lista_heroes, 'color_pelo')
            case 'O':
                auxiliares.utn_listar_personajes_por_dato(lista_heroes, 'empresa')
            case 'P':
                variedades = auxiliares.obtener_lista_de_tipos(lista_heroes, 'color_ojos')
                diccionario = auxiliares.obtener_personajes_por_tipo(lista_heroes, variedades, 'color_ojos')
                diccionario = auxiliares.utn_ordenar_personajes_por_dato(diccionario)
                auxiliares.imprimir_personajes_por_tipo(diccionario, 'color_ojos')
            case 'Q':
                corriendo = False

        os.system('pause')
        os.system('cls')
        