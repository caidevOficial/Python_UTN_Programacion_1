
import copy



lista = [
    [1,2], [3,4]
]
lista_2 = copy.copy(lista)



print(f'Lista Original: {lista}')
print(f'Lista Shallow Copy: {lista_2}')

for index in range(len(lista)):
    print('Indice de sub listas:')
    index_o = hex(id(lista[index]))
    index_c = hex(id(lista_2[index]))
    print(index_o, index_c)
    
    print('Indice de elementos de sub listas:')
    for index_lista in range(len(lista_2[index])):
        index_o = hex(id(lista[index_lista]))
        index_c = hex(id(lista_2[index_lista]))
        print(index_o, index_c)
    print('')

lista_2.remove(lista_2[1])
lista_2[0][0] = 20

print(f'Lista Shallow Copy: {lista_2}')
print(f'Lista Original: {lista}')