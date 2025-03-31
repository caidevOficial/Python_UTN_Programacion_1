def mostrar_menu():
    opciones =\
        """
        1 - Mostrar los nombres de los heroes
        2 - Mostrar la identidad de los heroes
        3 - Mostrar al heroe con mayor altura
        4 - Mostrar al/los heroe/s con mayor poder, en caso de haber mas de uno, 
            mostrarlos a todos.
        5 - Filtrar a los heroes Femeninos y mostrar sus nombres
        6 - Filtrar a los heroes Masculinos y mostrar sus identidades
        7 - Filtrar a los personajes No-Binarios y mostrar su nombre e identidad
        8 - Determinar cuales heroes tienen un poder superior al promedio.
        9 - Determinar cual es el maximo de poder y mostrar los nombres de cuales heroes 
            tienen un poder inferior A LA MITAD DE PODER del heroe mas fuerte.
        10 - Ordenar los heroes por poder ascendente y mostrarlos.
        11 - Ordenar los heroes por altura descendente y mostrarlos.
        12 - Ordenar los heroes por poder y que el usuario decida ASC o DES.
        13 - Salir
        """
    print(opciones)
    
if __name__ == '__main__':
    mostrar_menu()