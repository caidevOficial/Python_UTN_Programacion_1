# Ejercicios

# 2 - Crear una funcion sin parámetros que retorne el año actual como numero entero

# 3 - Crear una función que dado un parametro que corresponde a un numbre, salude.

# 5 - Crear una funcion con parámetros que dado un radio, calcule el area de un circulo

# 9 - Crear una función con parametros que dada una palabra y una letra, retorne 
#       la cantidad de letras coincidentes que tiene esa palabra

# 10 - Crear una funcion con parametros, que dada una palabra, cuente la cantidad total de letras
#       de letras y retorne dicha cantidad como un entero.

def contar_letras_texto(texto: str) -> int:
    contador_caracteres = 0
    
    # cantidad_caracteres = len(texto)
    
    for _ in texto:
        contador_caracteres += 1
    print(contador_caracteres)
    return contador_caracteres


# 11 - Crear una funcion sin parametros que pida al usuario que ingrese tres palabras, luego
#       calculará cual de ellas tiene mayor cantidad de caracteres y tendra que 
#       imprimirla en consola
#       junto con la cantidad de letras que posee


def ingresar_palabras():
    
    cantidad_caracteres_mayor = None
    palabra_mas_larga = None
    
    for i in range(3):
        palabra = input(f'Ingrese la {i + 1}° palabra: ')
        cantidad_letras_palabra_actual = contar_letras_texto(palabra)
        if cantidad_caracteres_mayor == None or\
            cantidad_letras_palabra_actual > cantidad_caracteres_mayor:
                
                cantidad_caracteres_mayor = cantidad_letras_palabra_actual
                palabra_mas_larga = palabra
    
    texto = f'La palabra con mas cantidad de letras es: {palabra_mas_larga} y '\
            f'tiene un total de {cantidad_caracteres_mayor} caracteres'
    
    print(texto)