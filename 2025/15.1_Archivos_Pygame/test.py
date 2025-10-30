import os
import auxiliar as aux
import frases as fra


dictionary = aux.generar_bd(r'.\assets\decks')
raider_waite = dictionary.get('cartas').get('raider_waite')

raider_waite = aux.asignar_frases(raider_waite, fra.lista_frases)
print(raider_waite)