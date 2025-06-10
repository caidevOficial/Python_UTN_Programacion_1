# Copyright (C) 2023 <UTN FRA>
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import tkinter as tk
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

NOMBRE = "Facu" # Nombre del alumno

"""
#Nos encargan el desarrollo de una aplicación que le permita a sus usuarios operar 
    en la bolsa de valores.:

A) Para ello deberás programar el botón  para poder cargar 10 operaciones de compra 
    con los siguientes datos:
    * Nombre
    * Monto en pesos de la operación (no menor a $10000)
    * Tipo de instrumento(CEDEAR, BONOS, MEP) 
    * Cantidad de instrumentos  (no menos de cero) 
    Son 10 datos

# IMPORTANTE:
    Del punto C solo deberá realizar SOLAMENTE 2 informes. 
    (PRESUPONER QUE CADA CLIENTE INGRESADO ES UN CLIENTE DISTINTO, NINGUNO SE REPITE, 
    no es necesario validar que no haya nombres repetidos)

Para determinar que informes hacer, tenga en cuenta lo siguiente:
    
    Informe 2 - Tome el último número de su DNI Personal (Ej 4) 
        y realice ese informe (Ej, Realizar informe 4) = 7

    Informe 3 - Tome el último número de su DNI Personal (Ej 4), 
        y restarle al número 9 (Ej 9-4 = 5). En caso de que su DNI 
        finalice con el número 0, deberá realizar el informe 9.

    Realizar los informes correspondientes a los números obtenidos. 
        EL RESTO DE LOS INFORMES LOS DEBE IGNORAR. 
C) 
    #! 0) - Tipo de instrumento que menos se operó en total.
    #! 1) - Tipo de instrumento que más se operó en total.
    #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
    #! 3) - Cantidad de usuarios que no compraron CEDEAR 
    #! 4) - Nombre y cantidad invertida del primer usuario que compró BONOS o CEDEAR
    #! 5) - Nombre y posicion de la persona que menos BONOS compro
    #! 6) - Nombre y posicion del usuario que invirtio menos dinero
    #! 7) - Nombre y posicion del usuario que mas cantidad de instrumentos compró
    #! 8) - Promedio de dinero en CEDEAR  ingresado en total.  
    #! 9) - Promedio de cantidad de instrumentos  MEP vendidos en total
"""

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title(f"UTN FRA - Bolsa de valores de {NOMBRE}")
        self.minsize(320, 250)

        self.label_title = customtkinter.CTkLabel(master=self, text=f"Bolsa de valores de {NOMBRE}", font=("Arial", 20, "bold"))
        self.label_title.grid(row=0, column=0, columnspan=2, padx=20, pady=10)

        self.btn_cargar = customtkinter.CTkButton(master=self, text="Cargar cartas", command=self.btn_cargar_datos_on_click)
        self.btn_cargar.grid(row=2, pady=10, columnspan=2, sticky="nsew")

    
    def btn_cargar_datos_on_click(self):
        # Desarrollá la lógica debajo
        """
        * Nombre
        * Monto en pesos de la operación (no menor a $10000)
        * Tipo de instrumento(CEDEAR, BONOS, MEP) 
        * Cantidad de instrumentos  (no menos de cero) 
        """
        
        limite_datos = 3
        cantidad_mep_entre_50_y_200 = 0
        cantidad_maxima_instrumentos = 0
        nombre_del_millonario = None
        
        while limite_datos > 0:
            
            # pedir y validar los datos
            
            # NOMBRE
            nombre = None
            while (nombre == None) or (not nombre.isalpha()):
                nombre = input('Ingrese su nombre: ')
            
            # MONTO
            monto = None
            while (monto == None) or (not monto.isdigit()) or (int(monto) < 10000):
                monto = input('Ingrese un monto [a partir de $10000]: ')
                
            monto_int = int(monto)
            
            # TIPO
            tipo = None
            while (tipo == None) or (not tipo.isalpha() or (
                tipo != 'CEDEAR' and tipo != 'MEP' and tipo != 'BONOS')):
                tipo = input('Ingrese su tipo de instrumento (CEDEAR, BONOS, MEP): ').upper()
            
            # CANTIDAD
            cantidad = None
            while (cantidad == None) or (not cantidad.isdigit()) or (int(cantidad) < 1):
                cantidad = input('Ingrese la cantidad de instrumentos [a partir de 1]: ')
                
            cantidad_int = int(cantidad)
            
            limite_datos -= 1
        
        
            # Procesar datos
            
            # 2
            #! 2) - Cantidad de usuarios que compraron entre 50  y 200 MEP 
            if tipo == 'MEP' and cantidad_int < 201 and cantidad_int > 50:
            # if tipo == 'MEP' and (50 < cantidad_int < 201):
                cantidad_mep_entre_50_y_200 += 1

            #! 7) - Nombre y cantidad de instrumentos del usuario que mas compró
            if cantidad_maxima_instrumentos == 0 or cantidad_int > cantidad_maxima_instrumentos:
                cantidad_maxima_instrumentos = cantidad_int
                nombre_del_millonario = nombre
                       
        
        # Mostrar Informes
        # Aca vas a armar tu variable con el texto del informe a entregar
        data_informe =\
            f"La cantidad de personas que compraron entre 50 y 200 MEP es: {cantidad_mep_entre_50_y_200}\n"\
            f"La persona que mas instrumentos compro es {nombre_del_millonario} con {cantidad_maxima_instrumentos} unidades."
        alert('Informe', message=data_informe)
    

if __name__ == "__main__":
    app = App()
    app.mainloop()
