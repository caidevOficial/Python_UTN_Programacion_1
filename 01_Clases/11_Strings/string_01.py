
texto = '#estamos en la UTN aprendiendo Python en la clase virtual en la tarde del dia Lunes en mi compu#'
t = ""
texto = texto.strip()

# SPLIT()
lista_str = texto.split()
texto_resultante = ''

for palabra in lista_str:
    texto_resultante += f'{palabra.capitalize()} '
texto_resultante = texto_resultante.strip()


indices_incorrectos = []
lista_str = texto.split('#')

print(f'Antes de borrrar: {lista_str}')
indice_busqueda = 0

for elemento in lista_str:
    print(len(lista_str))
    print(elemento)
    if elemento == '':
        indice = lista_str.index(elemento, indice_busqueda)
        indice_busqueda = indice + 1
        indices_incorrectos.append(
            indice
        )

print(indices_incorrectos)
indices_incorrectos.reverse()

for indice_incorrecto in indices_incorrectos:
    lista_str.pop(indice_incorrecto)
print(f'Despues de borrrar: {lista_str}')
    

# print(lista_str)
# texto_resultante = ''
# for palabra in lista_str:
#     texto_resultante += f'{palabra.capitalize()} '

# texto_resultante = f'¡{texto_resultante}'



# print(texto_resultante)