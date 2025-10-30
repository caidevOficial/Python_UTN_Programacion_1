import os
def install_requirements():
    if os.name in ['nt', 'dos']: # windows
        comando = 'python '
    else: # Mac o Linux
        comando = 'python3 '
    comando += '-m pip install -r requirements.txt'
    os.system(comando)


if __name__ == '__main__':
    """
    Para generar el archivo requirements.txt con las librerias:
    pip freeze > requirements.txt 
    """
    install_requirements()
    
    from game import pythonisa
    
    pythonisa()