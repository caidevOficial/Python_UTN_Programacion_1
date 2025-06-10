def imprimir_menu_desafio_3_5():
    texto =\
        """
        A - Recorrer la lista imprimiendo por consola el nombre de cada personaje de género Masculino
        B - Recorrer la lista imprimiendo por consola el nombre de cada personaje de género Femenino
        C - Recorrer la lista y determinar cuál es el personaje más alto de raza “Human”
        D - Recorrer la lista y determinar cuál es el personaje más alto de raza “Desconocido”
        E - Recorrer la lista y determinar cuál es el personaje más bajo  de raza “Symbiote”
        F - Recorrer la lista y determinar cuál es el personaje más bajo  de raza “Mutant”
        G - Recorrer la lista y determinar la altura promedio de los  personajes de empresa “DC Comics”
        H - Recorrer la lista y determinar la altura promedio de los  personajes de empresa “Marvel Comics”
        J - Determinar cuántos personajes tienen cada tipo de color de ojos.
        K - Determinar cuántos personajes tienen cada tipo de color de pelo.
        L - Determinar cuántos personajes tienen cada tipo de alineación (En caso de no tener ningún tipo de alineación [o tener un string vacío], Inicializarlo con ‘No Tiene’). 
        M - Listar todos los personajes agrupados por color de ojos.
        N - Listar todos los personajes agrupados por color de pelo.
        O - Listar todos los personajes agrupados por empresa
        P - Ordenar los personajes de manera ascendente según la cantidad de personajes que haya por color de ojos. 
            [Desarrollar esta función por sus propios medios siguiendo el estilo dado]. 
            Ejemplo: si hay más personajes con color de ojos verdes, todos estos tendrán que aparecer primero, 
            si en cantidad le siguen los de ojos rojos, todos esos personajes aparecerán luego en la lista resultante, 
            misma lógica con el resto.

        Q - Salir
        """
    print(texto)


"""
Crear la función 'es_dato' la cual recibirá como parámetros:

Un diccionario que representará un héroe
Un string el cual será usado para el nombre de la key la cual queremos buscar
Un string el cual será usado para evaluar si la key del héroe coincide con el valor buscado.

ejemplo de uso: es_dato(lista_de_heroes, “empresa”, “DC Comics”)
La función deberá retornar True en caso que en la clave tenga el valor pasado por parámetro, 
False caso contrario.

"""

def es_dato(heroe: dict, key: str, valor: str):
    return heroe[key] == valor

"""
Crear la función 'utn_imprimir_heroe_genero' la cual recibirá como parámetros:

La lista de personajes
Un string el cual representará el género a evaluar 
(el string puede ser ‘M’,  ‘F’ o ‘NB’ ). 

Deberá imprimir solamente los héroes  que coincidan con el género pasado por parámetro.

Se deberá utilizar la función 'es_dato'.


La función no retorna nada.

"""

def utn_imprimir_heroe_genero(lista_personajes: list[dict], genero: str):
    for heroe in lista_personajes:
        if es_dato(heroe, 'genero', genero):
            print(heroe.get('nombre'))


"""
Crear la función 'calcular_min_raza' la cual recibirá como parámetros:


A - La lista de personajes. 
B - Un string para representar el dato que deberá ser evaluado a efectos de determinar cuál es el 
minimo de la lista (por ejemplo: “altura”, “peso”, etc)
C - Un string para representar la raza


La función deberá retornar el héroe que cumpla la condición de tener el mínimo de la raza especificada.

Se deberá utilizar la función 'es_dato'

"""

def calcular_min_raza(lista_personajes: list[dict], key: str, raza: str):
    minimo = {}
    for heroe in lista_personajes:
        if es_dato(heroe, 'raza', raza) and (not minimo or minimo.get(key) > heroe.get(key)):
            minimo = heroe
    return minimo

"""
Crear la función 'calcular_max_raza' la cual recibirá como parámetros:


La lista de personajes. 
Un string para representar el dato que deberá ser evaluado a efectos de determinar cuál es el máximo de la lista (por ejemplo: “altura”, “peso”, etc)
Un string para representar la raza


La función deberá retornar el personaje que cumpla la condición de tener el máximo del género especificado.
Se deberá utilizar la función 'es_dato'

"""
def calcular_max_raza(lista_personajes: list[dict], key: str, raza: str):
    maximo = {}
    for heroe in lista_personajes:
        
        if es_dato(heroe, 'raza', raza) and (not maximo or maximo.get(key) < heroe.get(key)):
            maximo = heroe
    return maximo

"""
Crear la funcion 'calcular_max_min_dato' la cual recibiá como  parámetros:


La lista de personajes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
Un string para representar la raza

La función deberá retornar el personaje que cumpla con la condición pedida. 
Reutilizar las funciones hechas en los puntos 2.0 y 2.1
Ejemplo de llamada:
calcular_max_min_dato(lista,  "maximo", “Human” "altura")
"""

def calcular_max_min_dato(lista_personajes: list[dict], calculo: str, key: str, raza: str):
    heroe_elegido = {}
    if calculo.lower() == 'maximo':
        heroe_elegido = calcular_max_raza(lista_personajes, key, raza)
    elif calculo.lower() == 'minimo':
        heroe_elegido = calcular_min_raza(lista_personajes, key, raza)
    return heroe_elegido

"""
Crear la función 'utn_calcular_imprimir_heroe_raza' la cual recibirá como parámetros: 


La lista de personajes
El tipo de cálculo a realizar: es un valor string que puede tomar los valores ‘maximo’ o ‘minimo’
Un string para representar la raza
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.

La función deberá obtener el personaje que cumpla dichas condiciones, imprimir su nombre y el valor calculado. 

Validar que la lista de personajes no esté vacía para realizar sus acciones, caso contrario no hará nada y retornara -1.

Reutilizar la funcion ‘calcular_max_min_dato’

"""

def utn_calcular_imprimir_heroe_raza(lista_personajes: list[dict], calculo: str, key: str, raza: str):
    heroe_elegido = calcular_max_min_dato(lista_personajes, calculo, key, raza)
    nombre = heroe_elegido.get('nombre')
    valor = heroe_elegido.get(key)
    texto =\
        f"""
        El heroe que tiene el {calculo} de {key} es: {nombre}  con valor: {valor}
        """
    print(texto)


"""
Crear la función ‘sumar_dato_personaje_empresa’ la cual recibirá como parámetros:
La lista de héroes
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘edad’, etc.
Un string para representar la empresa

La función deberá devolver la suma total del dato recibido como parámetro de todos los personajes de la empresa especificada.

Antes de realizar el cálculo se deberá validar:
El tipo de dato del personaje debe ser diccionario.
El  personaje actual de la iteración no debe estar vacío (ser diccionario vacío)
 La empresa del personaje debe coincidir con el pasado por parámetro.

Una vez que cumpla con las condiciones se  podrá realizar la suma.
Se deberá utilizar la función 'es_dato'
"""

def sumar_dato_personaje_empresa(lista_personajes: list[dict], key: str, empresa: str):
    suma = 0
    
    for heroe in lista_personajes:
        if type(heroe) == dict and heroe and es_dato(heroe, 'empresa', empresa):
            suma += heroe.get(key)
    return suma

"""
3.2 - Crear la función 'cantidad_personajes_empresa' la cual recibirá como parámetros: 
La lista de personajes 
Un string que representa la empresa a buscar.
La función deberá iterar y sumar la cantidad de personajes que cumplan con la condición de empresa pasada por parámetro.

La función deberá retornar la suma de los personajes según la empresa especificada

"""

def cantidad_personajes_empresa(lista_personajes: list[dict], empresa: str):
    cantidad = 0
    for heroe in lista_personajes:
        if es_dato(heroe, 'empresa', empresa):
            cantidad += 1
    return cantidad

"""
Crear la función 'calcular_promedio_empresa' la cual recibirá como parámetros: 
La lista de personajes 
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘fuerza’, etc.
Un string que representa la empresa a buscar.

Se deberá reutilizar las funciones: 'sumar_dato_personaje_empresa', 'cantidad_personajes_empresa'

La función deberá retornar el promedio obtenido, según la key y género pasado por parámetro.

"""
def calcular_promedio_empresa(lista_personajes: list[dict], key: str, empresa: str):
    suma = sumar_dato_personaje_empresa(lista_personajes, key, empresa)
    cantidad = cantidad_personajes_empresa(lista_personajes, empresa)
    
    if cantidad != 0:
        return suma / cantidad
    return 0

"""
Crear la función 'utn_calcular_imprimir_promedio_altura_empresa' la cual recibirá como parámetros:

La lista de personajes 
Un string que representa la key del dato a calcular, por ejemplo: ‘altura’, ‘peso’, ‘fuerza’, etc.
Un string que representa la empresa a buscar.

Se deberá validar antes de hacer nada que la lista no esté vacía. 
En caso de estarlo se deberá imprimir el mensaje: "Error: Lista de personajes vacía"
En caso de no estar vacía, calcular el promedio e imprimir formateado usando f-string al estilo:
"Altura promedio empresa DC Comics: 178.45" (no es un ejemplo verídico)


Reutilizar las funciones: 'calcular_promedio_empresa' e 'imprimir_dato'

"""
def utn_calcular_imprimir_promedio_altura_empresa(lista_personajes: list[dict], key: str, empresa: str):
    
    if lista_personajes:
        # "Altura promedio empresa DC Comics: 178.45"
        promedio = calcular_promedio_empresa(lista_personajes, key, empresa)
        
        texto =\
            f"""
            {key.upper()} promedio empresa {empresa}: {promedio:.2f} mts.
            """
        print(texto)
    else:
        print("Error: Lista de personajes vacía")


"""
Crear la función 'calcular_cantidad_tipo' la cual recibirá como parámetros:

La lista de personajes
Un string que representa el tipo de dato/key a buscar (color_ojos, color_pelo, etc)

Antes de realizar cualquier cálculo se deberá validar que la lista no esté vacía

La función deberá retornar un diccionario con los distintos valores del tipo de dato recibido por 
parámetro y la cantidad de cada uno   (crear un diccionario clave valor)

Por ejemplo, si el tipo de dato fuese color_ojos, devolverá un diccionario de la siguiente manera:

{
    "Blue": 4,
    "Green": 8,
    "Brown": 6
}

"""
def calcular_cantidad_tipo(lista_personajes: list[dict], key: str):
    cantidad_tipos = {}
    
    if lista_personajes:
        
        for heroe in lista_personajes:
            valor = heroe.get(key).upper()
            if valor == '-':
                valor = 'No Tiene'
            if valor in cantidad_tipos.keys():
                cantidad_tipos[valor] += 1
            else:
                cantidad_tipos[valor] = 1
            # cantidad_tipos[valor] = cantidad_tipos.get(valor, 0) + 1

    return cantidad_tipos    

"""
Crear la funcion 'imprimir_cantidad_personajes_tipo' la cual solamente recibirá como parámetros:

Un diccionario que representara las distintas variedades del tipo de dato 
(distintos colores de ojos, pelo, etc) como clave con sus respectivas cantidades como valor.


Un string que representa el tipo de dato (color_pelo, color_ojos, etc): el cual tendrás que  usarlo 
únicamente en el mensaje final formateado.

La función deberá iterar cada key del diccionario y variabilizar dicha key con su valor para luego 
formatearlos en un mensaje el cual deberá imprimir.


Por ejemplo:
 "Característica: color_ojos Blue - Cantidad de personajes: 9" (No es un dato verídico)

Reutilizar la función 'imprimir_dato'

"""

def imprimir_cantidad_personajes_tipo(variedades_tipo: dict, key: str):
    
    for clave, valor in variedades_tipo.items():
        
        texto =\
            f"""Característica: {key} {clave} - Cantidad de personajes: {valor}"""
        print(texto)

"""
Crear la función 'utn_calcular_cantidad_por_tipo' la cual recibirá como parámetros:

La lista de personajes
Un string que representa el tipo de dato/key a buscar (color_ojos, color_pelo, etc).

Dentro deberas reutilizar las funciones:  'calcular_cantidad_tipo' e 'imprimir_cantidad_personajes_tipo'

Esta función no retorna nada.

"""

def utn_calcular_cantidad_por_tipo(lista_personajes: list[dict], key: str):
    tipos = calcular_cantidad_tipo(lista_personajes, key)
    imprimir_cantidad_personajes_tipo(tipos, key)
    



"""
Crear la función 'obtener_lista_de_tipos' la cual recibirá como parámetros:


La lista de personajes
Un string que representa el tipo de dato/key a buscar (color_ojos, color_pelo, etc)

- La función deberá iterar la lista de personajes guardando en una lista las variedades 
del tipo de dato pasado por parámetro (sus valores). 

- En caso de encontrar una key sin valor (o string vacío), deberás hardcodearlo con el 
valor 'N/A' y luego agregarlo a la lista donde irás guardando todos los valores encontrados, 
si el valor del héroe no tiene errores, guardarlo tal cual viene.

Finalmente deberás eliminar los duplicados de esa lista y retornarla.


"""

def obtener_lista_de_tipos(lista_personajes: list[dict], key: str):
    set_elementos = set()
    
    for heroe in lista_personajes:
        valor = heroe.get(key)
        valor = normalizar_dato(valor, 'N/A')
        
        if valor == None:
            print(heroe)
        
        set_elementos.add(valor.upper())
    return set_elementos
    
"""
Crear la función 'normalizar_dato' la cual recibirá como parámetros:


Un string que representa un dato del personaje (el valor de una de sus keys, por ejemplo si la key 
fuese color_ojos y su valor fuese ‘Green’, recibirá este último) 


Un string el cual se usará como valor por defecto (en caso que un valor se encuentre vacío)


La función deberá validar que el dato no esté vacío, en caso de estarlo lo reemplazará con el valor por 
defecto pasado por parámetro y lo retornara, caso contrario lo retornará sin modificaciones.

"""    
def normalizar_dato(dato: str, default: str):
    if not dato or dato == '' or dato == '-':
        dato = default
    return dato


"""
Crear la funcion 'obtener_personajes_por_tipo' el cual recibira como parametros:


La lista de personajes.
La lista de tipos/variedades que existen (colores de ojos, de pelo, etc)
El tipo de dato a evaluar (la key en cuestion, ‘color_ojos’, ‘color_pelo’, etc)


TENER EN CUENTA:
La función deberá iterar la lista de tipos/variedades y por cada tipo tendrá que evaluar si ese tipo existe como 
key en un diccionario el cual deberás armar. 

Este diccionario contendrá cada variedad como key y una lista de nombres de héroes como valor de cada una de ellas
En caso de no existir dicha key en el diccionario, agregarla con una lista vacía como valor.


Dentro de la iteración de variedades, iterar la lista de personaje (for anidado) 'normalizando' el posible 
valor que tenga la key evaluada, ya que podría venir vacía (qué función usarias aca? guiño guiño)


 Una vez normalizado el dato, evaluar si dicho dato coincide con el tipo pasado por parámetro. En caso de que coincida, 
 agregarlo a la lista (inicialmente vacía) de la variedad iterada en el primer bucle.


La función deberá retornar un diccionario con cada variedad como key y una lista de nombres como valor. Por ejemplo:
{
    "Green": [“Goblin Queen”, “Hit-Girl”, “Harry Potter”],
    "Red": [“Darkseid”, “T-800”, “Thanos”]
}


Reutilizar la función 'normalizar_dato'

"""

def obtener_personajes_por_tipo(lista_personajes: list[dict], set_tipos: set, key: str):
    
    variedades_distintas = {}
    
    for variedad in set_tipos:
        if not variedad in variedades_distintas.keys():
            variedades_distintas[variedad] = []
        
        for heroe in lista_personajes:
            dato_raw = heroe.get(key)
            dato = normalizar_dato(dato_raw, 'N/A')
            
            if dato.upper() == variedad:
                variedades_distintas[variedad].append(heroe.get('nombre'))
    return variedades_distintas
                
        
"""
Crear la funcion 'imprimir_personajes_por_tipo' la cual recibira como parámetros:


Un diccionario que representara los distintos tipos como clave y una lista de nombres como valor (lo retorna la función anterior) 


Un un string el cual representará el tipo de dato a evaluar (color_pelo, color_ojos, etc)

La función deberá recorrer cada key y cada valor (lista) que esta contenga para finalmente 
crear un string el cual será un mensaje que deberá imprimir formateado. Se la siguiente manera:
"color_ojos Red: Thanos | T-800 | Darkseid"
Esta función no tiene retorno. 

"""

def imprimir_personajes_por_tipo(tipos_distintos: dict, key: str):
    
    for clave, valor in tipos_distintos.items():
        
        # color_ojos Red: Thanos | T-800 | Darkseid
        texto =\
            f"""{key} {clave}: {' | '.join(valor[:7])}"""
        print(texto)


"""
Crear la funcion 'utn_listar_personajes_por_dato' la cual recibira como parametros:


La lista de personajes 
Un string que representa el tipo de dato a evaluar (color_pelo, color_ojos, etc)

Dentro deberás reutilizar las funciones, 'obtener_lista_de_tipos',  'obtener_personajes_por_tipo',  'imprimir_personajes_por_tipo'
Esta función no retorna nada.

"""

def utn_listar_personajes_por_dato(lista_personajes: list[dict],key: str):
    variedades = obtener_lista_de_tipos(lista_personajes, key)
    diccionario = obtener_personajes_por_tipo(lista_personajes, variedades, key)
    imprimir_personajes_por_tipo(diccionario, key)


"""
Crear la funcion 'utn_ordenar_personajes_por_dato' la cual recibira como parametros:


Un diccionario el cual cada clave sea el dato a ordenar (color_pelo, color_ojos, etc) y 
los valores sean listas con nombres de los personajes que tienen cada característica. 
(Ya hiciste una función que genera este tipo de diccionario) 

Un string que representa el orden (ASC, DESC)

La función deberá tomar dicho diccionario, comparar los tamaños de sus listas y 
ordenarlas según el string pasado por parámetro (ASC, DESC), 
El desarrollo separarlo en pequeñas 
funciones que hagan cada parte de la lógica. luego mostrarlo por consola:

Ejemplo (no verídico)
Ojos Red: 3 personajes | [LISTA DE LOS 3 PERSONAJES]
Ojos Green: 2 personajes | [LISTA DE LOS DOS PERSONAJES]
ETC.
"""


def intercambiar_columnas(matriz: list[list], primer_fila: int, segunda_fila: int):
    aux = matriz[primer_fila]
    matriz[primer_fila] = matriz[segunda_fila]
    matriz[segunda_fila] = aux

def actualizar_indice_fila(matriz: list[list], indice_fila:int, indice_elegido: int, indice_col_ordenar: int, orden: str = 'ASC'):
    for indice_prox_fila in range(indice_fila + 1, len(matriz)):
        if orden == 'ASC' and len(matriz[indice_prox_fila][indice_col_ordenar]) > len(matriz[indice_elegido][indice_col_ordenar]) or\
            orden == 'DES' and len(matriz[indice_prox_fila][indice_col_ordenar]) < len(matriz[indice_elegido][indice_col_ordenar]):
            indice_elegido = indice_prox_fila
    return indice_elegido

def ordenar_selection(matriz: list[tuple], indice_columna_ordenar: int, orden: str = 'ASC') -> list[list]:
    
    for indice_fila in range(len(matriz) -1):
        indice_elegido = indice_fila
        indice_elegido = actualizar_indice_fila(matriz, indice_fila, indice_elegido, indice_columna_ordenar, orden)
                
        if indice_elegido != indice_fila:
            intercambiar_columnas(matriz, indice_fila, indice_elegido)
    return matriz

def utn_ordenar_personajes_por_dato(tipos_distintos: dict, orden: str = 'ASC'):
    lista_ordenada = []
    
    for clave, valor in tipos_distintos.items():
        lista_ordenada.append(
            (clave, valor)
        )
    
    ordenar_selection(lista_ordenada, 1, orden)
    print(lista_ordenada)
    return dict(lista_ordenada)
    
    

if __name__ == '__main__':
    import variables
    
    variedades = obtener_lista_de_tipos(variables.lista_heroes, 'color_ojos')
    diccionario = obtener_personajes_por_tipo(variables.lista_heroes, variedades, 'color_ojos')
    utn_ordenar_personajes_por_dato(diccionario)