

total_numeros_str = input('Hasta que número queres imprimir?: ')
total_numeros = int(total_numeros_str)

mostrar_pares = input('Que numeros queres ver? [par/impar/todos]: ')
saltitos = 2


match mostrar_pares:
    case 'par' | 'todos':
        num_inicio = 0
        if mostrar_pares == 'todos':
            saltitos = 1
    case 'impar':
        num_inicio = 1


for iteracion in range(num_inicio, total_numeros + 1, saltitos):
    print(f'Numero: {iteracion}')

print('Fuera del bucle FOR.')

