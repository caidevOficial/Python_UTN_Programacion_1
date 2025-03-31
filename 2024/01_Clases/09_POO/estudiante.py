from persona import Persona

class Estudiante(Persona):
    
    def __init__(self, apellido, nombre, dni, domicilio, legajo, cant_materias):
        super().__init__(apellido, nombre, dni, domicilio)
        self.legajo_estud = legajo
        self.cantidad_materias = cant_materias