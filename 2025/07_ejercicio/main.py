from utn_fra.datasets import (
    lista_autos_cantidades, lista_autos_ganancias,
    lista_autos_marcas, lista_autos_modelos, lista_autos_precios
)
from app import aplicacion


aplicacion(lista_autos_marcas, lista_autos_modelos, lista_autos_precios,
           lista_autos_cantidades, lista_autos_ganancias)