
from validacion.validaciones_num import validar_atributo
from validacion.validaciones_str import pedir_nombre

def crear_template_pokemon(nombre: str, poder: int, peso: int) -> str:
    texto =\
    f"""
    El mas poderoso es:
    Nombre: {nombre}
    Poder: {poder} UF
    Peso: {peso} KG
    """
    return texto

def main_app():
    nombre_mas_poderoso = None
    poder_mas_poderoso = None
    peso_mas_poderoso = None


    for _ in range(3):

        nombre = pedir_nombre()
        peso = validar_atributo(18, 90, 'Peso')
        poder = validar_atributo(100, 500, 'Poder')
        
        if not poder_mas_poderoso or poder_mas_poderoso < poder:
            poder_mas_poderoso = poder
            nombre_mas_poderoso = nombre
            peso_mas_poderoso = peso

    informacion = crear_template_pokemon(
        nombre_mas_poderoso, poder_mas_poderoso, peso_mas_poderoso)
    print(informacion)
