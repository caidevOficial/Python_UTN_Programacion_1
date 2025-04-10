"""
Validar el ingreso de una edad que este entre 18 y 98 años


"""



# while edad == None
# while edad is None
# while not edad

edad = None
while edad == None or edad > 98 or edad < 18:
# while edad == None or not (edad > 17 and edad < 99):
# while edad == None or not (18 <= edad <= 98):
    
    edad_str = input('Ingrese su edad: ')
    if edad_str.isdigit():
        edad = int(edad_str)

print(type(edad), edad)


"""
edad_str.isdigit() -> Evalua que sean todos numeros
edad_str.isalpha() -> Evalua que sean todas letras
edad_str.isalnum() -> Evalua las dos de arriba
"""


