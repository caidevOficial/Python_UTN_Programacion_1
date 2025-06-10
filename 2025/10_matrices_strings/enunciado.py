
"""
1 - Escribir una función que reciba un string y devuelva 
el string en mayúsculas.
"""

"""
2 - Escribir una función que reciba un string y devuelva el string 
en minúsculas.
"""

"""
3 - Escribir una función que tome dos strings y devuelva un nuevo string que contenga 
ambos strings concatenados, separados por un espacio.
"""

"""
4 - Escribir una función que tome un string y devuelva el 
número de caracteres que tiene el string.
"""

"""
5 - Escribir una función que tome un string y un carácter y 
devuelva el número de veces que aparece ese carácter en el string.
"""

"""
6 - Escribir una función que tome un string y un carácter y 
devuelva una lista con todas las palabras en el string 
que contienen ese carácter.
"""


"""
7 - Escribir una función que tome un string y devuelva el 
mismo string con los espacios eliminados
"""

"""
8 - Escribir una función que reciba dos string (nombre y apellido) 
y devuelva una lista con el nombre y apellido, 
eliminando los espacios del comienzo y el final y 
colocando la primer letra en mayúscula
"""

"""
8.1 - Usando la funcion anterior, escribir una función que reciba 
una lista de nombres y apellidos y retorne una matriz formateada con
los que hace la funcion anterior
"""

"""
9 - Escribir una función que tome una lista de nombres y 
los una en una sola cadena separada por un salto de línea, 
por ejemplo: ["Juan", "María", "Pedro"] -> "Juan\nMaría\nPedro".
"""

"""
10 - Escribir una función que tome un nombre y un apellido y 
devuelva un email en formato "inicial_nombre.apellido@utn-fra.com.ar".
"""


"""
11 - Escribir una función que tome una lista de palabras y 
devuelva un string que contenga todas las palabras 
concatenadas con comas y "y" antes de la última palabra. 
Por ejemplo, si la lista es ["manzanas", "naranjas", "bananas"], 
el string resultante debería ser "manzanas, naranjas y bananas"..
"""


"""
12 - Escribir una función que tome un número de tarjeta de crédito como input, 
verificar que todos los caracteres sean numéricos y 
devolver los últimos cuatro dígitos y los primeros dígitos como asteriscos, 
por ejemplo: "**** **** **** 1234". 

"""

"""
13 - Escribir una función que tome un correo electrónico y 
elimine cualquier carácter después del símbolo @, por ejemplo: 
"usuario@gmail.com" -> "usuario".
"""

def eliminar_dominio(email: str) -> str:
    partes_email = email.split('@')
    print(partes_email)
    return partes_email[0]
    
print(eliminar_dominio('pepe.argento@flores.gov.ar'))

"""
14 - Escribir una función que tome una URL y 
devuelva solo el nombre de dominio, 
por ejemplo: "https://www.ejemplo.com.ar/pagina1" -> "ejemplo"..
"""

def obtener_dominio(url: str) -> str:
    lista_str = url.split('.')
    print(lista_str)
    return lista_str[1]

print(obtener_dominio("https://www.ejemplo.com.ar/pagina1"))
    

"""
15 - Escribir una función que tome una cadena de texto y 
devuelva solo los caracteres alfabéticos, eliminando cualquier número o símbolo, 
por ejemplo: "H0l4, m4nd0!" -> "Hl, mnd.
"""


"""
16 - Escribir una función que tome una cadena de texto y la convierta en un acrónimo, 
tomando la primera letra de cada palabra, por ejemplo: 
"Universidad Tecnológica Nacional Facultad Regional Avellaneda" -> "UTNFRA”.
"""

def obtener_acronimo(texto: str) -> str:
    lista_palabras = texto.split(' ')
    lista_iniciales = []
    for indice in range(len(lista_palabras)):
        lista_iniciales.append(lista_palabras[indice][0])
    return ''.join(lista_iniciales)

print(obtener_acronimo("Universidad Tecnológica Nacional Facultad Regional Avellaneda"))
    

"""
17 - Escribir una función que tome un número binario y lo convierta en 
una cadena de 8 bits, rellenando con ceros a la izquierda 
si es necesario, por ejemplo: "101" -> "00000101".
"""

"""
18 - Escribir una función que tome una cadena de caracteres y reemplace 
todas las letras mayúsculas por letras minúsculas y 
todas las letras minúsculas por letras mayúsculas, por ejemplo: "HoLa" -> "hOlA"
"""


"""
19 - Escribir una función que tome una cadena de caracteres y cuente la 
cantidad de dígitos que contiene, por ejemplo: 
"1234 Hola Mundo" -> contiene 4 dígitos.
"""


"""
20 - Escribir una función que tome una lista de direcciones de correo electrónico 
y las concatene en una sola cadena separada por punto y coma, 
por ejemplo: ["juan@gmail.com", "maria@hotmail.com"] -> 
"juan@gmail.com;maria@hotmail.com".
"""


""""
21 - Crear una función que reciba como parámetro un string y 
devuelva una matriz donde el primer elemento de cada fila es una palabra y
el segundo elemento es un entero que indica cuántas veces aparece 
esa palabra dentro del string.
"""

# hola mundo, bienvenidos al mundo

"""
[
    [hola, 1],
    [mundo, 2],
    [bienvenidos, 1],
    [al, 1]
]
"""


  