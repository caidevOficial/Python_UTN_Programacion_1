class Persona:
    
    def __init__(self, apellido, nombre, dni, domicilio):
        self.apellido_per = apellido
        self.nombre_per = nombre
        self.dni_per = dni
        self.domicilio_per = domicilio
    
    def saludar(self)-> None:
        """
        Saluda diciendo su nombre y apellido
        """
        mensaje = f'Hola, me llamo {self.nombre_per} {self.apellido_per}!!'
        print(mensaje)
