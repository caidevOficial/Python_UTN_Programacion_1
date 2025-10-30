
import variables as var

nuevo_texto = 'Hola Mundo'
archivo = open(file=var.RUTA_ARCHIVO_TEXTO, mode='r+', encoding='utf-8')
texto = archivo.readlines()

for indice in range(len(texto)):
    texto[indice] = texto[indice].replace('\n', '')

var.informacion['data'] = ' | '.join(texto)
archivo.write(f'\n{nuevo_texto}')

archivo.close()

print(f"Mensaje: {var.informacion.get('data')}")
