import os

def clear_console():
    """
    Limpia la consola luego de que el usuario presione una tecla.
    """
    command = 'clear'
    if os.name in ['nt', 'dos']:
        command = 'cls'
    
    os.system('pause')
    os.system(command)