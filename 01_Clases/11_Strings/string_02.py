texto = 'estamos en la UTN aprendiendo Python en la clase virtual en la tarde del dia Lunes en mi compu'
t = ""

lista_str = texto.split()
texto = texto.title()

# for indice in range(len(lista_str)):
#     lista_str[indice] = lista_str[indice].capitalize()

# print(lista_str)

texto = ' '.join(lista_str)


def utn_join(lista: list[str], separador: str) -> str:
    texto_resultante = ''
    for indice in range(len(lista)):
        if indice < len(lista) -1:
            texto_resultante += f'{lista[indice]}{separador}'
        else:
            texto_resultante += f'{lista[indice]}'
    return texto_resultante


texto_resultante = utn_join(lista_str, ' ')
print(f'{texto_resultante}!!')