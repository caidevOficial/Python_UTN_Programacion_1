import variables as var

nuevo_texto = 'Hola Mundo'
archivo = open(file=var.RUTA_ARCHIVO_TEXTO, mode='a+', encoding='UTF-8')

archivo.seek(0)
texto = archivo.read()

print(texto)
texto = archivo.write(f'\n{nuevo_texto}')

archivo.close()