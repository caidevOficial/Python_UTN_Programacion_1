from persona import Persona
from estudiante import Estudiante

if __name__ == '__main__':
    ser_humano = Persona("Argento", "Pepe", "11111111", "Calle falsa 123")
    ser_humano_2 = Estudiante("Argento", "Paola", "22222222", "Calle falsa 123", "2222", 8)

    personajes = [
        ser_humano,
        ser_humano_2 
        
    ]

    for personaje in personajes:
        personaje.saludar()
