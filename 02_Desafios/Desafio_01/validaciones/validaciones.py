
def validar_opcion(num_min: int, num_max: int):
    opcion = input(f'Ingrese una opcion [{num_min} - {num_max}]:')
    
    if not opcion or not opcion.isdigit() or not (num_min <= int(opcion) <= num_max):
        return validar_opcion(num_min, num_max)
    
    return int(opcion)



if __name__ == '__main__':
    print(validar_opcion(1, 10))