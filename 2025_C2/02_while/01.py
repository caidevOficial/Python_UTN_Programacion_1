

"""
Pedir edades hasta que se ingrese una edad superior a 95
pedir genero

sumarlas
sacar el promedio de edad
obtener edad minima
obtener edad maxima

sacar el promedio de edad de genero f
obtener suma edades de genero m
obtener edad minima genero m
obtener edad maxima genero f
"""

suma_edades = 0 # acumulador
cantidad_encuestados = 0 #contador

suma_edades_femenino = 0
cantidad_femenino = 0

suma_edades_masculino = 0

edad_minima = None
edad_maxima = None

edad_minima_m = None
edad_maxima_f = None

while True:
    
    edad = input('Ingrese su edad: ') #100
    edad_int = int(edad) #100

    
    if edad_int > 95:
        break

    genero = input('Ingrese su género [f/m]: ')
    
    if edad_minima == None or edad_minima > edad_int:
        edad_minima = edad_int
        if genero == 'm':
            edad_minima_m = edad_int

    
    if edad_maxima == None or edad_maxima < edad_int:
        edad_maxima = edad_int
        if genero == 'f':
            edad_maxima_f = edad_int

    cantidad_encuestados += 1
    suma_edades += edad_int

    match genero:
        case 'f':
            cantidad_femenino += 1
            suma_edades_femenino += edad_int

        case 'm':
            suma_edades_masculino += edad_int


promedio = suma_edades / cantidad_encuestados
promedio_edad_fem = suma_edades_femenino / cantidad_femenino

mensaje =\
f"""
La suma de edades es de: {suma_edades} años
El promedio de edad es: {promedio}
La edad mininma es {edad_minima} años.
La edad máxima es: {edad_maxima} años.

El promedio de edad Femenino es {promedio_edad_fem} años.
La suma de edades Masculino es: {suma_edades_masculino} años.
La edad minima Masculino es {edad_minima_m}.
La edad maxima Femenino es {edad_maxima_f}.
"""
print(mensaje)
