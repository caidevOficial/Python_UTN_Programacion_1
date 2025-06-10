# 4 - Alias a funciones y/o modulos

# from validaciones import validar_edad as val_edad
# import input_usuario_2 as no_anda
from biblioteca_utn import validar_nombre_o_apellido


nombre = input('Ingrese su nombre')
nombre = validar_nombre_o_apellido(nombre, 'Incorrecto, Ingrese su nombre: ')

apellido = input('Ingrese su apellido')
apellido = validar_nombre_o_apellido(apellido, 'Incorrecto, Ingrese su apellido: ')