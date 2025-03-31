ruta_de_archivo = '13_archivos/texto.txt'
contenido_original = 'Este es un texto normal de la clase de archivos, usando Python. estas son letras con acento: á é í ó ú Ñ 🤖🚀'
nuevo_texto = 'Hola UTN\n'

# archivo = open(ruta_de_archivo, 'a+', encoding='UTF-8')

# archivo.write(nuevo_texto)
# archivo.seek(0)
# texto = archivo.read()
# print(texto)

# archivo.close()


with open(ruta_de_archivo, 'a+') as archivo_a:
    archivo_a.write(nuevo_texto)
    archivo_a.seek(0)
    texto = archivo_a.read()
    print(texto)
    print(archivo_a.closed)
    

print('El archivo se cerro automaticamente al salir del bloque with')
print(archivo_a.closed)