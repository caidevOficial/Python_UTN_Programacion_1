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
    "año": 2023
}

division_materia["alumnos egresados"] = alumnos_2

# for clave in division_materia.keys():
#     valor = division_materia[clave]
#     print(valor)

# for valor in division_materia.values():
#     print(valor)

# for clave, valor in division_materia.items():
#     if type(valor) == list:
#         valor = ','.join(valor)
#     print(f'Clave: {clave} | Valor: {valor}')

# print(f"Institución: {division_materia.get('institucion')}")
print(division_materia)

if division_materia.get('año') != 2025:
    # division_materia["año"] = division_materia["año"] + 1
    division_materia["año"] = 2025
    
print(division_materia)