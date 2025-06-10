
from biblioteca_utn import validar_numero_entre, validar_edad, validar_existencia

# from biblioteca_utn import (
#     validar_existencia, validar_edad, validar_numero_entre
# )

# from biblioteca_utn import *

# import biblioteca_utn


for vuelta in range(2):
    
    
    # genero = input("Ingrese genero ['Masculino', 'Femenino', 'Otro']:")
    # genero_validado = validar_existencia(genero, 'Masculino', 'Femenino', 'Otro')
    
    
    # sector = input("Ingrese sector ['General', 'Campo delantero', 'Vip']:")
    # sector_validado = validar_existencia(sector, 'General', 'Campo delantero', 'Vip')
    
    # tipo_pago = input("Ingrese tipo pago ['Credito', 'Debito', 'Efectivo']:")
    # tipo_pago_validado = validar_existencia(tipo_pago, 'Credito', 'Debito', 'Efectivo')
    
    numero_input = input("Ingrese un numero: ")
    numero_input_validado = validar_numero_entre(numero_input, 100, 500)
    # numero_input_validado = biblioteca_utn.validar_numero_entre(numero_input, 100, 500)
    
    
    print(
        # genero_validado,
        # sector_validado,
        # tipo_pago_validado,
        numero_input_validado,
        sep=' | '
    )