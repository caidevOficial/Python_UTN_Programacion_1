from validaciones import  validar_numero
from output import mostrar_menu
from utn_fra.funciones.auxiliares import clear_console
from funciones_auxiliares import (
    cargar_existencias, calcular_existencias_totales,
    obtener_datos_menor_cantidad_autos, mostrar_info_garages_maximos
)


def aplicacion(lista_marcas: list, lista_modelos: list, lista_precios: list, lista_cantidades: list, lista_ganancias: list):
    lista_cantidades[2] = 7
    lista_numero_garage = []
    corriendo = True
    cantidad = len(lista_marcas)
    
    
    while corriendo:
        
        mostrar_menu()
        opcion = validar_numero(1, 10)
        
        match opcion:
            case 1:
                lista_numero_garage = cargar_existencias(cantidad)
                print(lista_numero_garage)
            case 2:
                calcular_existencias_totales(lista_cantidades)
            case 3:
                obtener_datos_menor_cantidad_autos(lista_numero_garage, lista_marcas, lista_modelos, lista_cantidades, lista_precios, lista_ganancias)
            case 4:
                mostrar_info_garages_maximos(lista_numero_garage, lista_marcas, lista_modelos, lista_cantidades, lista_precios, lista_ganancias)
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                pass
            case 10:
                corriendo = False
        clear_console()
            