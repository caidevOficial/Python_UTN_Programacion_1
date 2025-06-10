alumnos = [
    "Manu", "Pepe", "Fatiga"
]

alumnos_2 = [
    "Facu", "Ignacio", "Nahuel", "Jorge"
]


division_materia = {
    "numero": 315,
    "alumnos": alumnos,
    "materia": 'Programación I',
    "año": 2025
}

# print(division_materia)

lista_aux = division_materia["alumnos"].copy()
lista_aux.extend(alumnos_2)

# division_materia["alumnos egresados"] = alumnos


print(division_materia)