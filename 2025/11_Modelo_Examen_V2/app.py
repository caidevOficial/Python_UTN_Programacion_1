"""
lista_poke_ids, lista_poke_nombres,
    lista_poke_tipos, lista_poke_poderes,
    lista_poke_condiciones
"""
import os
from validaciones import validar_input as val_input
import consola
import matrices


print(f'Modulo app.py -> {__name__}')

def aplicacion(lista_poke_ids, lista_poke_nombres, lista_poke_tipos, lista_poke_poderes, lista_poke_condiciones):
    
    
    corriendo = True
    matriz_pokemons = []
    matriz_cargada = False
    
    while corriendo:
        
        consola.mostrar_menu()
        opcion = val_input(1, 7)
        
        match opcion:
            case 1:
                matriz_pokemons = matrices.crear_matriz(
                    lista_poke_ids, lista_poke_nombres, lista_poke_tipos, 
                    lista_poke_poderes, lista_poke_condiciones)
                matriz_cargada = True
                print('Matriz cargada correctamente.')
                
            case 2:
                if matriz_cargada:
                    print(f'Esta es la opcion {opcion}')
                    matrices.mostrar_matriz(matriz_pokemons)
            case 3:
                if matriz_cargada:
                    print(f'Esta es la opcion {opcion}')
                    # filtrada = matrices.filtrar_matriz_poder_superior(matriz_pokemons, 3)
                    # matrices.mostrar_matriz(filtrada)
                    matrices.filtrar_matriz_poder_superior_V2(matriz_pokemons, 3)
            case 4:
                if matriz_cargada:
                    print(f'Esta es la opcion {opcion}')
                    matriz = matrices.ordenar_selection(matriz_pokemons, 3)
                    matriz = matrices.filtrar_matriz_pokemons(matriz, 4, 'legendario')
                    matrices.mostrar_matriz(matriz)
            case 5:
                if matriz_cargada:
                    print(f'Esta es la opcion {opcion}')
                    matriz = matrices.filtrar_matriz_pokemons(matriz_pokemons, 2, 'fuego')
                    matriz = matrices.ordenar_selection(matriz, 3)
                    matrices.mostrar_matriz(matriz)
            case 6:
                if matriz_cargada:
                    print(f'Esta es la opcion {opcion}')
                    matriz_t = matrices.trasponer_matriz(matriz_pokemons)
                    matrices.mostrar_info_traspuesta(matriz_t)
            case 7:
                corriendo = False
                print('Saliendo de la aplicación, gracias vuelvas prontossss')
        
        if not matriz_cargada:
            print('Primero Debe ir a la opcion 1')
        
        os.system('pause')
        os.system('cls')