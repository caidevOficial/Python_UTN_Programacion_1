import variables as var

nuevo_texto = 'Hola Mundo'

with open(file=var.RUTA_ARCHIVO_TEXTO, mode='r', encoding='utf-8') as archivo:
    texto = archivo.read()
    print(texto)

print('Sali del bloque de archivo')