from persona import Persona

class Empleado(Persona):
    
    def __init__(self, apellido, nombre, dni, domicilio, nro_empleado):
        super().__init__(apellido, nombre, dni, domicilio)
        self.numero_empleado = nro_empleado