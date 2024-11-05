

class Persona:
    
    def __init__(self, apellido, nombre):
        self.apellido_per = apellido
        self.nombre_per = nombre
    
    def en_formato_csv(self) -> str:
        return f'{self.apellido_per},{self.nombre_per}'
    
    def en_diccionario(self) -> dict:
        datos = {
            "nombre": self.nombre_per,
            "apellido": self.apellido_per
        }
        return datos
