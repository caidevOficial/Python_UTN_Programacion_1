matriz_tupla = (
    ["Spiderman", "Marvel Comics"],
    ["Thor", "Marvel Comics"],
    ["Venom", "Marvel Comics"],
    ["Deadpool", "Marvel Comics"]
)

la_tupla = (1,2,3,4,5)

print(matriz_tupla)
matriz_tupla[0][0] = 'Iron Man'

matriz_tupla[1].append('Dios del trueno')

print(hex(id(la_tupla)))

nueva_tupla = la_tupla + tuple(' De Marvel')

print(hex(id(nueva_tupla)))
print(nueva_tupla)