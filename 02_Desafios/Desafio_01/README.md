<table>
    <tr>
        <td align='center'>
            <img alt="Logo UTN Large" src="../../02_Desafios/Desafio_01/assets/img/Banner.png?raw=true" href="https://www.utnfravirtual.org.ar/" width="750px"/>
        </td>
    </tr>
</table></br>

# Enunciado Desafío UTN Industries 1:

### Desde **_UTN Industries_** queremos sacar ciertas métricas de los heroes y villanos. Para ello te guiaremos con algunas descripciones paso a paso de funciones para que puedas desarrollar el programa que nos permita saber lo que necesitamos, si logras hacerlo bien no seras contratado/a, pero quiza Batman te deje sacarte una foto con su Batimovil!


## A - Desarrolla el paquete "validaciones" y modulo "validaciones" para luego...

#### A1 - En el modulo validaciones: Desarrolla la funcion "validar_opcion" la cual tendrá dos parámetros de entrada (un numero minimo y un numero maximo, ambos enteros) y dentro debe pedirle al usuario que ingrese un numero (el cual sera usado para seleccionar alguna opcion del menu principal de la aplicacion). En caso de ingresar un valor incorrecto (algun numero fuera del rango o algo que no sea integramente numeros enteros) la funcion se ejecutara de nuevo a si misma, en caso de elegir una opcion correcta, la retornara COMO UN ENTERO.

## B - Desarrolla el paquete "funciones" con el modulo: "salida_consola" para luego...

#### B1 - En el modulo "salida_consola": Desarrolla la funcion "mostrar_menu" la cual tendra que mostrar el menu de opciones del programa. Dichas opciones son:
### Menú
* 1 - Mostrar los nombres de los heroes
* 2 - Mostrar la identidad de los heroes
* 3 - Mostrar al heroe con mayor altura
* 4 - Mostrar al/los heroe/s con mayor poder, en caso de haber mas de uno, mostrarlos a todos.
* 5 - Filtrar a los heroes Femeninos y mostrar sus nombres
* 6 - Filtrar a los heroes Masculinos y mostrar sus identidades
* 7 - Filtrar a los personajes No-Binarios y mostrar su nombre e identidad
* 8 - Determinar cuales heroes tienen un poder superior al promedio.
* 9 - Determinar cual es el maximo de poder y mostrar los nombres de cuales heroes tienen un poder inferior A LA MITAD DE PODER del heroe mas fuerte.
* 10 - Salir

## C - Desarrolla el paquete "app" y modulo "main_app" para luego...

#### C1 - En el modulo "main_app": Desarrolla la funcion "utn_heroes_app" la cual tendra como parametros 5 listas, esta funcion tendra dentro un match principal que se ejecutará dentro de un bucle while True. El match evaluará la opcion ingresada por el usuario y segun la opcion elegida ejecutará cada una de las funciones que tienen prefijo "utn_", para ello el usuario tiene que mostrar las posibles opciones a elegir, es por eso que debe llamar a "mostrar_menu" y "validar_opcion". 
_Luego de validar la opcion elegida, deberas llamar a la funcion "play_sound" la cual "UTN Industries" te la regala para tu desarrollo._

_Debajo del match, pero aun dentro del while tendra que llamar a la funcion "limpiar_consola" la cual "UTN Industries" te la regala para tu desarrollo._

## D - Agrega al paquete "funciones" los modulos: "funciones" y "auxiliares" para luego...


#### D1 - En el modulo "auxiliares": Desarrolla la funcion "mostrar_nombre" la cual recibira como parametros, la lista de nombres y un numero entero que representara el indice de la lista el cual debe extraer el nombre, luego debe retornarlo.

#### D2 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_nombres_heroes"** la cual recibira como parametro la lista de nombres. Dentro debe iterarla y mostrar en consola cada uno de los elementos.

#### D3 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_identidades_heroes"** la cual recibira como parametro la lista de identidades. Dentro debe iterarla y mostrar en consola cada uno de los elementos.

#### D4 - En el modulo "auxiliares": Desarrolla la funcion "obtener_maximo", la cual recibira como parametro una lista de numeros y debe obtener el numero mas grande, luego retornarlo como un flotante.

#### D5 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_heroe_mayor_altura"** la cual recibira por parametro las 5 listas, dentro debe mostrar todos los datos del heroe mas alto. Debe llamar a la funcion "obtener_maximo"

#### D6 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_heroes_mas_fuertes"** la cual recibira por parametros las 5 listas. Dentro debe llamar a la funcion "obtener_maximo", una vez obtenido debe iterar la lista numerica correspondiente hasta encontrar dicho valor, por cada vez que encuentre ese valor, tendra que imprimir la info completa de los heroes ubicados en esos indices.

#### D7 - En el modulo "funciones": Desarrolla la funcion **"utn_filtrar_heroes_genero"** la cual recibirá por parametros las 5 listas y el genero a filtrar. El encontrar cada elemento del genero buscado, debe imprimir los datos completos del heroe del mismo indice.

#### D8 - En el modulo "auxiliares": Desarrolla la funcion "promedio" la cual recibira como parametro una lista de numeros, debe retornar el promedio numerico.

#### D9 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_heroes_poder_superior_promedio"** la cual recibira por parametro las 5 listas, llamara a la funcion "promedio" para encontrarlo, luego debera mostrar los datos de todos los heroes que tengan un poder superior al promedio.

#### D10 - En el modulo "auxiliares": Desarrolla la funcion "obtener_mitad_de_maximo" la cual recibira como parametro una lista de numeros, dentro tendra que llamar a la funcion "obtener_maximo" y al resultado dividirlo entre dos, ese resultado tendra que retornarlo.

#### D11 - En el modulo "funciones": Desarrolla la funcion **"utn_mostrar_heroes_mas_debiles"** la cual recibira como parametro las 5 listas, dentro tendra que llamar a la funcion "obtener_mitad_de_maximo" para encontrar el valor, una ves obtenido tendra que iterar la lista correspondiente y mostrar la info completa de los heroes que cumplan la condicion.

## E - Desarrolla el modulo "main" para luego importar en el la funcion "utn_heroes_app" y poder ejecutarla