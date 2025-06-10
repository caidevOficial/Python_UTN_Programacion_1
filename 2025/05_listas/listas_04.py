lista_de_mensajes = [
    "Ganaste!!",
    "Empate!!",
    "Perdiste! :("
]


numero_pc = 6
numero = int(input('Dime un numero: '))

if numero_pc == numero:
    mensaje = lista_de_mensajes[1]
elif numero_pc < numero:
    mensaje = lista_de_mensajes[0]
else:
    mensaje = lista_de_mensajes[2]

print(mensaje)